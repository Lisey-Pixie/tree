
import re
#import treeIdentifier.html as html
# List of tree descriptions
from trees_data import trees # type: ignore

def get_valid_input(prompt, valid_options=None, input_type=str):
    while True:
        user_input = input(prompt)
        try:
            # Case when the input is expected to be an integer
            if input_type == int:
                user_input = int(user_input)
                if user_input <= 0:
                    raise ValueError("Input must be a positive number.")
            # Case when the input is expected to be a list (e.g., multiple numbers)
            elif input_type == list:
                user_input = [int(x.strip()) for x in user_input.split(',')]
                if not all(x > 0 for x in user_input):
                    raise ValueError("All numbers must be positive.")
            # If valid_options is provided, make sure the input is in the valid options list
            elif valid_options:
                if isinstance(valid_options, list):
                    if user_input not in valid_options:
                        raise ValueError(f"Invalid input. Choose from {', '.join(valid_options)}.")
                else:
                    raise ValueError("Valid options should be a list.")
            return user_input
        except ValueError as ve:
            print(f"Error: {ve}. Please try again.")

def case_insensitive_match(user_value, tree_values):
    # Ensure tree_values is always a list for iteration
    if not isinstance(tree_values, list):
        tree_values = [tree_values]  # Make it a list if it's a single value

    # If user_value is a list, compare each value against tree_values
    if isinstance(user_value, list):
        for val in user_value:
            if case_insensitive_match(val, tree_values):  # Recursively check individual values
                return True
    else:
        # Check for string matching case-insensitively
        for val in tree_values:
            if isinstance(val, str) and str(user_value).strip().lower() == str(val).strip().lower():
                return True
    return False

# Ask for user leaf attributes
def ask_leaf_attributes():
    t = get_valid_input("Is the leaf simple or compound? (e.g., simple, compound): ", ["simple", "compound"])

    # leaf_number should accept multiple values (comma separated, like "3, 5, 7")
    n = get_valid_input("How many leaflets, or needles in a cluster? (comma separated for multiple values, e.g., 5, 7, 9): ", input_type=list)

    l = get_valid_input("How is the leaf shaped? (e.g., lobed, palmate, oval, elliptical, needles, diamond, lanceolate, ovate, heart-shaped): ", 
                        ["lobed", "palmate", "oval", "elliptical", "needles", "diamond", "lanceolate", "ovate", "heart-shaped"], input_type=str)

    s = get_valid_input("What is the size of the leaf? (e.g., small, medium, large): ", ["small", "medium", "large"], input_type=str)

    c = get_valid_input("What is the leaf color? (e.g., green, yellow, brown, red, orange, purple, gold): ", 
                        ["green", "yellow", "brown", "red", "orange", "purple", "gold"], input_type=str)

    edge = get_valid_input("What is the leaf edge like? (e.g., smooth, serrated, deeply lobed): ", 
                           ["smooth", "serrated", "deeply lobed", "toothed"], input_type=str)

    v = get_valid_input("What is the leaf venation? (e.g., pinnate, palmate): ", ["pinnate", "palmate"], input_type=str)

    texture = get_valid_input("How is the texture of the leaf? (e.g., smooth, rough): ", ["smooth", "rough"], input_type=str)

    autumn_color = get_valid_input("What color does the leaf turn in autumn? (e.g., red, yellow, orange, copper, evergreen): ", 
                                   ["red", "yellow", "orange", "copper", "evergreen"], input_type=str)

    return {
        "leaf_type": t,
        "leaf_number": n,
        "leaf_shape": l,
        "leaf_size": s,
        "leaf_color": c,
        "leaf_edge": edge,
        "venation": v,
        "texture": texture,
        "leaf_autum": autumn_color
    }

# Function to identify possible trees based on user input
from flask import Flask, render_template, request

app = Flask(__name__)

# --- Place your 'trees' list and 'case_insensitive_match' function here ---

def case_insensitive_match(user_value, tree_values):
    if not isinstance(tree_values, list):
        tree_values = [tree_values]
    if isinstance(user_value, list):
        for val in user_value:
            if case_insensitive_match(val, tree_values):
                return True
    else:
        for val in tree_values:
            if isinstance(val, str) and str(user_value).strip().lower() == str(val).strip().lower():
                return True
    return False

def identify_tree(user_description, trees):
    match_scores = []
    total_attributes = len(user_description)
    for tree in trees:
        score = 0
        for key, user_value in user_description.items():
            tree_value = tree.get(key)
            if not tree_value:
                continue
            tree_values = tree_value if isinstance(tree_value, list) else [tree_value]
            if case_insensitive_match(user_value, tree_values):
                score += 1
        if score >= total_attributes / 2:
            match_scores.append((tree['name'], score))
    match_scores.sort(key=lambda x: x[1], reverse=True)
    return match_scores

@app.route('/', methods=['GET', 'POST'])
def home():
    matches = []
    description = None
    user_description = {
        "leaf_type": "",
        "leaf_number": "",
        "leaf_shape": "",
        "leaf_size": "",
        "leaf_color": "",
        "leaf_edge": "",
        "venation": "",
        "texture": "",
        "leaf_autum": "",
    }
    if request.method == 'POST':
        user_description = {
            "leaf_type": request.form.get("leaf_type", ""),
            "leaf_number": request.form.get("leaf_number", ""),
            "leaf_shape": request.form.get("leaf_shape", ""),
            "leaf_size": request.form.get("leaf_size", ""),
            "leaf_color": request.form.get("leaf_color", ""),
            "leaf_edge": request.form.get("leaf_edge", ""),
            "venation": request.form.get("venation", ""),
            "texture": request.form.get("texture", ""),
            "leaf_autum": request.form.get("leaf_autum", ""),
        }
        matches = identify_tree(user_description, trees)
        if request.form.get("get_description") and request.form.get("tree_choice"):
            chosen = request.form.get("tree_choice")
            for tree in trees:
                if tree["name"] == chosen:
                    description = tree.get("description", "No description available.")
    return render_template('treeIdentifier.html', matches=matches, description=description, user_description=user_description)

if __name__ == '__main__':
    app.run(debug=True)