import re
from trees_data import trees  # type: ignore
from flask import Flask, render_template, request, session, redirect, url_for
app = Flask(__name__)
app.secret_key = 'cYaL83303mF'

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

@app.route('/')
def index():
    return render_template('frontPage.html')

@app.route('/treeIdentifier', methods=['GET', 'POST'])
def treeIdentifier():
    matches = []
    description = None
    image = None
    tree_name = "Dogwood"
    error = None
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
        # --- Input validation ---
        valid_leaf_types = ["simple", "compound"]
        valid_leaf_shapes = ["lobed", "palmate", "oval", "elliptical", "needles", "diamond", "lanceolate", "ovate", "heart-shaped", "triangular"]
        valid_leaf_sizes = ["small", "medium", "large"]
        valid_leaf_colors = ["green", "yellow", "brown", "red", "orange", "purple", "gold"]
        valid_leaf_edges = ["smooth", "serrated", "deeply lobed", "lobed", "sharp"]
        valid_venations = ["pinnate", "palmate", "parallel"]
        valid_textures = ["smooth", "rough"]
        valid_leaf_autums = ["red", "yellow", "orange", "copper", "brown", "purple", "gold", "evergreen"]

        if not user_description["leaf_type"] or user_description["leaf_type"] not in valid_leaf_types:
            error = "Please select 'simple' or 'compound' for leaf type."
        elif not user_description["leaf_shape"] or user_description["leaf_shape"] not in valid_leaf_shapes:
            error = "Please select a valid leaf shape."
        elif not user_description["leaf_size"] or user_description["leaf_size"] not in valid_leaf_sizes:
            error = "Please select a valid leaf size."
        elif not user_description["leaf_color"] or user_description["leaf_color"] not in valid_leaf_colors:
            error = "Please select a valid leaf color."
        elif not user_description["leaf_edge"] or user_description["leaf_edge"] not in valid_leaf_edges:
            error = "Please select a valid leaf edge."
        elif not user_description["venation"] or user_description["venation"] not in valid_venations:
            error = "Please select a valid leaf venation."
        elif not user_description["texture"] or user_description["texture"] not in valid_textures:
            error = "Please select a valid leaf texture."
        elif not user_description["leaf_autum"] or user_description["leaf_autum"] not in valid_leaf_autums:
            error = "Please select a valid autumn color."
        elif not user_description["leaf_number"] or not re.match(r'^\d+(,\s*\d+)*$', user_description["leaf_number"]):
            error = "Please enter a valid number or comma-separated numbers for leaflets or needles."
        else:
            matches = identify_tree(user_description, trees)
            if request.form.get("get_description") and request.form.get("tree_choice"):
                chosen = request.form.get("tree_choice")
                for tree in trees:
                    if tree["name"] == chosen:
                        description = tree.get("description", "No description available.")
                        image = tree.get("image", None)
                        tree_name = tree.get("name", "Unknown Tree")
                        # --- Add to identified trees in session ---
                        if "identified_trees" not in session:
                            session["identified_trees"] = []
                        if chosen not in session["identified_trees"]:
                            session["identified_trees"].append(chosen)
                        session.modified = True
    return render_template(
        'treeIdentifier.html',
        matches=matches,
        description=description,
        image=image,
        tree_name=tree_name,
        user_description=user_description,
        error=error
    )

@app.route('/browse')
def browse():
    return render_template('browse.html', trees=trees)

@app.route('/tree/<name>')
def tree_data(name):
    tree = next((t for t in trees if t['name'].lower() == name.lower()), None)
    if tree:
        return render_template('tree_data.html', tree=tree)
    else:
        return "Tree not found", 404
@app.route('/clear_identified', methods=['POST'])
def clear_identified():
    session.pop('identified_trees', None)
    return redirect(url_for('treeIdentifier'))

if __name__ == '__main__':
    app.run(debug=True)