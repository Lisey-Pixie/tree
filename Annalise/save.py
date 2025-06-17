
import re
#import treeIdentifier.html as html
# List of tree descriptions
trees = [
    {
        "name": "White Oak",
        "leaf_type": "simple",
        "leaf_number":"1",
        "leaf_shape": "lobed",
        "leaf_size": "large",
        "leaf_color": "green",
        "leaf_edge": ["deeply lobed","smooth","serrated"],
        "venation": "pinnate",
        "texture": "rough",
        "leaf_autum": ["red","brown"],
        "description": "White Oak (Quercus alba) is a large, long-lived hardwood tree with deeply lobed leaves and a strong, straight trunk. It grows in a variety of habitats and its leaves turn red or brown in autumn. The wood is highly valued for furniture and flooring."
    },
    {
        "name": "Red Oak",
        "leaf_type": "simple",
        "leaf_number":"1",
        "leaf_shape": "lobed",
        "leaf_size": "large",
        "leaf_color": "green",
        "leaf_edge": ["sharp","serrated"],
        "venation": "pinnate",
        "texture": "rough",
        "leaf_autum": ["red"],
        "description": "Red Oak (Quercus rubra) is a fast-growing hardwood tree with pointed, sharply lobed leaves. It's commonly found in upland forests and turns bright red in fall. Its wood is used in construction and cabinetry."
    },
    {
        "name": "Red Maple",
        "leaf_type":"simple",
        "leaf_number":"1",
        "leaf_shape": "palmate",
        "leaf_size": "medium",
        "leaf_color": "green",
        "leaf_edge": "serrated",
        "venation": "palmate",
        "texture": "smooth",
        "leaf_autum": ["red","yellow"],
        "description": "Red Maple (Acer rubrum) is one of the most widespread trees in eastern North America. It has palmate leaves that turn vibrant red or yellow in autumn. It thrives in a wide range of soil types and is often planted for its ornamental value."
    },
    {
        "name": "Sugar Maple",
        "leaf_type":"simple",
        "leaf_number":"1",
        "leaf_shape": "palmate",
        "leaf_size": ["medium","large"],
        "leaf_color": "green",
        "leaf_edge": "serrated",
        "venation": "palmate",
        "texture": "smooth",
        "leaf_autum": ["red","orange","yellow"],
        "description": "Sugar Maple (Acer saccharum) is famous for its brilliant fall foliage—ranging from orange to red—and for being the primary source of maple syrup. It prefers moist, well-drained soils and can grow quite large."
    },
    {
        "name": "Birch",
        "leaf_type": "simple",
        "leaf_number": "1",
        "leaf_shape": ["oval","diamond"],
        "leaf_size": ["small","medium"],
        "leaf_color": "yellow",
        "leaf_edge": "serrated",
        "venation": "pinnate",
        "texture": "smooth",
        "leaf_autum": "yellow",
        "description": "Birch trees (Betula spp.) are medium-sized trees with smooth, often peeling bark and diamond or oval-shaped leaves. In Virginia, Yellow and River Birch are most common. Leaves are serrated and turn yellow in fall."
    },
    {
        "name": "Tulip Poplar",
        "leaf_type": "simple",
        "leaf_number": "1",
        "leaf_shape": "lobed",
        "leaf_size": "large",
        "leaf_color": "green",
        "leaf_edge": "smooth",
        "venation": "pinnate",
        "texture": "smooth",
        "leaf_autum": "yellow",
        "description": "Tulip Poplar (Liriodendron tulipifera) is one of the tallest native trees in Virginia. It has large, uniquely shaped leaves and greenish-yellow tulip-like flowers in spring. Leaves turn bright yellow in fall."
    },
    {
        "name": "Eastern Hemlock",
        "leaf_type":"compound",
        "leaf_shape": "needles",
        "leaf_number":["10","11","12","13","14","15","16","17","18","19","20"],
        "leaf_size": "small",
        "leaf_color": "green",
        "leaf_edge": "smooth",
        "venation": "parallel",
        "texture": "smooth",
        "leaf_autum": "evergreen",
        "description": "Eastern Hemlock (Tsuga canadensis) is an evergreen conifer with short, flat needles and drooping branches. It prefers cool, shady areas and moist soils, often found in ravines and along streams."
    },
    {
        "name": "American Beech",
        "leaf_type":"compound",
        "leaf_number":["7","8","9","10","11","12","13","14","15","16","17","18","19"],
        "leaf_shape": ["oval","elliptical"],
        "leaf_size": "medium",
        "leaf_color": "green",
        "leaf_edge": "serrated",
        "venation": "pinnate",
        "texture": "smooth",
        "leaf_autum": ["yellow","orange","copper"],
        "description": "American Beech (Fagus grandifolia) has smooth, gray bark and toothed, elliptical leaves that turn copper or golden-yellow in autumn. It forms dense shade and grows slowly but steadily in rich woodlands."
    },
    {
        "name": "Black Cherry",
        "leaf_type":"simple",
        "leaf_number":"1",
        "leaf_shape": "elliptical",
        "leaf_size": "medium",
        "leaf_color": "green",
        "leaf_edge": "serrated",
        "venation": "pinnate",
        "texture": "smooth",
        "leaf_autum": ["yellow","orange"],
        "description": "Black Cherry (Prunus serotina) is a medium-sized tree with glossy, serrated leaves and dark, flaky bark. In spring, it produces clusters of white flowers, followed by small, dark fruits. Its wood is prized in fine woodworking."
    },
    {
        "name": "White Pine",
        "leaf_type": "compound",
        "leaf_number":"5",
        "leaf_shape": "needles",
        "leaf_size": "large",
        "leaf_color": "green",
        "leaf_edge": "smooth",
        "venation": "parallel",
        "texture": "smooth",
        "leaf_autum": "evergreen",
        "description": "White Pine (Pinus strobus) is a tall, straight conifer with soft, flexible needles grouped in clusters of five. It grows fast and is used extensively for lumber. It remains green year-round and is found in cool, dry sites."
    },
    {
        "name": "Black Walnut",
        "leaf_type": "compound",
        "leaf_number":["9","10","11","12","13","14","15","16","17","18","19","20","21"],
        "leaf_shape": "elliptical",
        "leaf_size": "large",
        "leaf_color": "green",
        "leaf_edge": "serrated",
        "venation": "pinnate",
        "texture": "smooth",
        "leaf_autum": "yellow",
        "description": "Black Walnut (Juglans nigra) is known for its high-quality dark wood and large edible nuts. It has compound leaves and rough bark. Found in rich, moist soils, it’s valued for both wildlife and commercial use."
    },

    {
        "name": "American Sycamore",
        "leaf_type": "simple",
        "leaf_number": "1",
        "leaf_shape": "palmate",
        "leaf_size": "large",
        "leaf_color": "green",
        "leaf_edge": "lobed",
        "venation": "palmate",
        "texture": "rough",
        "leaf_autum": ["yellow"],
        "description": "American Sycamore (Platanus occidentalis) is a large, fast-growing tree often found near streams and rivers. Its broad, palmate leaves turn yellow in autumn. The tree's bark is distinctive, peeling in large patches to reveal white inner bark."
    },
    {
        "name": "Sweetgum",
        "leaf_type": "simple",
        "leaf_number": "1",
        "leaf_shape": "lobed",
        "leaf_size": "medium",
        "leaf_color": "green",
        "leaf_edge": "lobed",
        "venation": "palmate",
        "texture": "smooth",
        "leaf_autum": ["yellow", "red", "purple"],
        "description": "Sweetgum (Liquidambar styraciflua) is a medium-sized tree known for its star-shaped leaves. In autumn, its leaves turn vibrant shades of yellow, red, and purple. Sweetgum is often found in wet soils and is used for its hardwood in furniture and flooring."
    },
    {
        "name": "White Ash",
        "leaf_type": "compound",
        "leaf_number": ["5", "7", "9"],
        "leaf_shape": "ovate",
        "leaf_size": "medium",
        "leaf_color": "green",
        "leaf_edge": "serrated",
        "venation": "pinnate",
        "texture": "smooth",
        "leaf_autum": ["yellow", "purple"],
        "description": "White Ash (Fraxinus americana) is a tall deciduous tree with compound leaves that turn yellow or purple in the fall. It is commonly used for making baseball bats and furniture. White Ash grows in a variety of soil types, thriving in moist conditions."
    },
    {
        "name": "Pecan",
        "leaf_type": "compound",
        "leaf_number": ["13", "15", "17"],
        "leaf_shape": "lanceolate",
        "leaf_size": "large",
        "leaf_color": "green",
        "leaf_edge": "serrated",
        "venation": "pinnate",
        "texture": "smooth",
        "leaf_autum": ["yellow", "brown"],
        "description": "Pecan (Carya illinoinensis) is a large tree known for its edible nuts and tall, spreading canopy. Its long, lanceolate leaves have serrated edges and turn yellow or brown in autumn. Pecans grow best in deep, moist soils along rivers and floodplains."
    },
    {
        "name": "Black Locust",
        "leaf_type": "compound",
        "leaf_number": ["7", "9", "13"],
        "leaf_shape": "ovate",
        "leaf_size": "medium",
        "leaf_color": "green",
        "leaf_edge": "smooth",
        "venation": "pinnate",
        "texture": "smooth",
        "leaf_autum": "yellow",
        "description": "Black Locust (Robinia pseudoacacia) is a fast-growing, medium-sized tree with compound leaves and fragrant white flowers in spring. Its leaves turn yellow in autumn. The wood is durable and often used for fence posts, and the tree is commonly found in disturbed habitats."
    },
    {
        "name": "Redbud",
        "leaf_type": "simple",
        "leaf_number": "1",
        "leaf_shape": "heart-shaped",
        "leaf_size": "medium",
        "leaf_color": "green",
        "leaf_edge": "smooth",
        "venation": "palmate",
        "texture": "smooth",
        "leaf_autum": "yellow",
        "description": "Redbud (Cercis canadensis) is a small to medium-sized tree, often used for ornamental purposes due to its stunning spring flowers, which range from purple to pink. The heart-shaped leaves turn bright yellow in autumn."
    },
    {
        "name": "Boxelder",
        "leaf_type": "compound",
        "leaf_number": ["3", "5", "7"],
        "leaf_shape": "ovate",
        "leaf_size": "medium",
        "leaf_color": "green",
        "leaf_edge": "smooth",
        "venation": "pinnate",
        "texture": "smooth",
        "leaf_autum": "yellow",
        "description": "Boxelder (Acer negundo) is a small to medium-sized deciduous tree with compound leaves and greenish-yellow flowers in spring. Its leaves turn yellow in the fall, and the tree is commonly found in disturbed sites along rivers or floodplains."
    },
    {
        "name": "Northern Red Oak",
        "leaf_type": "simple",
        "leaf_number": "1",
        "leaf_shape": "lobed",
        "leaf_size": "large",
        "leaf_color": "green",
        "leaf_edge": "sharp",
        "venation": "pinnate",
        "texture": "rough",
        "leaf_autum": ["red", "brown"],
        "description": "Northern Red Oak (Quercus rubra) is a large, fast-growing tree with pointed lobed leaves that turn red or brown in autumn. It is native to the northeastern U.S. but also grows in parts of Virginia. Its wood is widely used for furniture and flooring."
    },
    {
        "name": "Shagbark Hickory",
        "leaf_type": "compound",
        "leaf_number": ["5", "7", "9"],
        "leaf_shape": "ovate",
        "leaf_size": "medium",
        "leaf_color": "green",
        "leaf_edge": "serrated",
        "venation": "pinnate",
        "texture": "rough",
        "leaf_autum": "yellow",
        "description": "Shagbark Hickory (Carya ovata) is a large tree with unique, shaggy bark. Its compound leaves turn yellow in the fall. The nuts are edible and are prized by wildlife. This tree is common in well-drained upland soils."
    },
    {
        "name": "Hornbeam",
        "leaf_type": "simple",
        "leaf_number": "1",
        "leaf_shape": "ovate",
        "leaf_size": "small",
        "leaf_color": "green",
        "leaf_edge": "serrated",
        "venation": "pinnate",
        "texture": "smooth",
        "leaf_autum": ["yellow", "orange"],
        "description": "Hornbeam (Carpinus caroliniana) is a small to medium-sized tree often found in moist woodlands and along streams. It has finely serrated, ovate leaves that turn yellow or orange in the fall. The wood is tough and is used for tool handles and other sturdy items."
    }
]

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
from flask import Flask, render_template, request # type: ignore

app = Flask(__name__)
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

# Main execution: ask for user inputs and show possible tree matches




@app.route('/', methods=['GET', 'POST'])
def home():
    matches = []
    if request.method == 'POST':
        user_description = {
            "leaf_type": request.form.get("leaf_type"),
            "leaf_number": request.form.get("leaf_number"),
            "leaf_shape": request.form.get("leaf_shape"),
            "leaf_size": request.form.get("leaf_size"),
            "leaf_color": request.form.get("leaf_color"),
            "leaf_edge": request.form.get("leaf_edge"),
            "venation": request.form.get("venation"),
            "texture": request.form.get("texture"),
            "leaf_autum": request.form.get("leaf_autum"),
        }
        matches = identify_tree(user_description, trees)
    return render_template('treeIdentifier.html', matches=matches)

if __name__ == '__main__':
    app.run(debug=True)