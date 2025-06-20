import re
from trees_data import trees  # Import the sorted list of tree dictionaries
from flask import Flask, render_template, request, session, redirect, url_for

# Initialize the Flask application
app = Flask(__name__)
app.secret_key = 'cYaL83303mF'  # Secret key for session management (should be kept secret in production)

# --- Helper Functions ---

def case_insensitive_match(user_value, tree_values):
    """
    Checks if user_value matches any value in tree_values, case-insensitively.
    Handles both single values and lists for flexibility.
    """
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
    """
    Compares user input (user_description) to each tree in the list.
    Returns a list of (tree name, score) tuples, sorted by score descending.
    """
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
        # Only consider trees that match at least half the attributes
        if score >= total_attributes / 2:
            match_scores.append((tree['name'], score))
    match_scores.sort(key=lambda x: x[1], reverse=True)
    return match_scores

# --- Flask Routes ---

@app.route('/')
def index():
    """
    Home page route. Renders the front page template.
    """
    return render_template('frontPage.html')

@app.route('/treeIdentifier', methods=['GET', 'POST'])
def treeIdentifier():
    """
    Main tree identifier page.
    Handles form submission, validation, matching, and session tracking of identified trees.
    """
    matches = []         # List of possible tree matches
    description = None   # Description of the selected tree
    image = None         # Image filename of the selected tree
    tree_name = "Dogwood"  # Default tree name
    error = None         # Error message for form validation

    # Default user description (empty fields)
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
        # Collect user input from the form
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

        # --- Input validation: ensure all fields are valid selections ---
        valid_leaf_types = ["simple", "compound"]
        valid_leaf_shapes = ["lobed", "palmate", "oval", "elliptical", "needles", "diamond", "lanceolate", "ovate", "heart-shaped", "triangular"]
        valid_leaf_sizes = ["small", "medium", "large"]
        valid_leaf_colors = ["green", "yellow", "brown", "red", "orange", "purple", "gold"]
        valid_leaf_edges = ["smooth", "serrated", "deeply lobed", "lobed", "sharp"]
        valid_venations = ["pinnate", "palmate", "parallel"]
        valid_textures = ["smooth", "rough"]
        valid_leaf_autums = ["red", "yellow", "orange", "copper", "brown", "purple", "gold", "evergreen"]

        # Validate each field and set an error message if invalid
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
        # Validate leaf_number: must be a number or comma-separated numbers
        elif not user_description["leaf_number"] or not re.match(r'^\d+(,\s*\d+)*$', user_description["leaf_number"]):
            error = "Please enter a valid number or comma-separated numbers for leaflets or needles."
        else:
            # If all inputs are valid, find matching trees
            matches = identify_tree(user_description, trees)
            # If user requested a description for a selected tree
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
                        session.modified = True  # Mark session as modified to ensure it saves

    # Render the identifier page with all relevant variables
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
    """
    Browse page route. Shows all trees in a grid/list.
    """
    return render_template('browse.html', trees=trees)

@app.route('/tree/<name>')
def tree_data(name):
    """
    Tree detail page route. Shows details for a single tree by name.
    """
    tree = next((t for t in trees if t['name'].lower() == name.lower()), None)
    if tree:
        return render_template('tree_data.html', tree=tree)
    else:
        return "Tree not found", 404

@app.route('/clear_identified', methods=['POST'])
def clear_identified():
    """
    Clears the list of identified trees from the user's session.
    """
    session.pop('identified_trees', None)
    return redirect(url_for('treeIdentifier'))

@app.route('/treelist', methods=['GET', 'POST'])
def treelist():
    # Initialize the treelist in the session if not present
    if 'checked_trees' not in session:
        session['checked_trees'] = []

    # If the form is submitted, update the session with checked trees
    if request.method == 'POST':
        checked = request.form.getlist('checked_trees')
        session['checked_trees'] = checked
        session.modified = True

    return render_template('treelist.html', trees=trees, checked_trees=session.get('checked_trees', []))
@app.route('/clear_treelist', methods=['POST'])
def clear_treelist():
    session.pop('checked_trees', None)
    return redirect(url_for('treelist'))
@app.route('/search', methods=['GET', 'POST'])
def search():
    results = []
    query = ""
    if request.method == 'POST':
        query = request.form.get('query', '').strip().lower()
        if query:
            # Search by name (case-insensitive, partial match)
            results = [tree for tree in trees if query in tree['name'].lower()]
    return render_template('search.html', results=results, query=query)


@app.route('/glossary')
def glossary():
    glossary_terms = [
        {"term": "Alternate", "definition": "Leaves arranged singly at different heights along the stem."},
        {"term": "Blade", "definition": "The broad, flat part of a leaf."},
        {"term": "Broadleaf", "definition": "A tree with wide, flat leaves rather than needles."},
        {"term": "Compound", "definition": "A leaf made up of two or more leaflets."},
        {"term": "Conifer", "definition": "A tree that produces cones and needle-like or scale-like leaves, usually evergreen."},
        {"term": "Deciduous", "definition": "A plant that sheds its leaves annually."},
        {"term": "Elliptical", "definition": "Shaped like an elongated oval."},
        {"term": "Evergreen", "definition": "A plant that retains green leaves throughout the year."},
        {"term": "Glabrous", "definition": "A surface that is smooth and hairless."},
        {"term": "Heart-shaped", "definition": "Shaped like a heart; often used to describe certain leaf bases."},
        {"term": "Lanceolate", "definition": "Shaped like a lance tip; longer than wide, widest below the middle."},
        {"term": "Lobed", "definition": "A leaf with large, rounded or pointed projections."},
        {"term": "Margin", "definition": "The edge of a leaf, which can be smooth, serrated, lobed, or otherwise shaped."},
        {"term": "Midrib", "definition": "The central vein running down the middle of a leaf."},
        {"term": "Needles", "definition": "Long, thin leaves typical of pines and other conifers."},
        {"term": "Node", "definition": "The part of a plant stem from which leaves or branches grow."},
        {"term": "Opposite", "definition": "Leaves paired at the same level on opposite sides of the stem."},
        {"term": "Ovate", "definition": "Egg-shaped; broadest below the middle."},
        {"term": "Palmate", "definition": "A leaf shaped like an open hand with lobes or leaflets radiating from a single point."},
        {"term": "Parallel (venation)", "definition": "Veins run parallel to each other, typical of grasses and some conifers."},
        {"term": "Petiole", "definition": "The stalk that attaches a leaf blade to the stem."},
        {"term": "Pinnate", "definition": "A leaf with smaller leaflets arranged on each side of a common axis."},
        {"term": "Pubescent", "definition": "Covered with fine, short hairs."},
        {"term": "Serrated", "definition": "A leaf edge with tooth-like projections."},
        {"term": "Simple", "definition": "A leaf with a single, undivided blade."},
        {"term": "Sinus", "definition": "The space or indentation between two lobes of a leaf."},
        {"term": "Smooth (edge)", "definition": "A leaf edge that is even and unbroken, without teeth or lobes."},
        {"term": "Texture", "definition": "The feel or appearance of a leaf surface (e.g., smooth, rough)."},
        {"term": "Venation", "definition": "The pattern of veins in a leaf."},
        {"term": "Whorled", "definition": "Three or more leaves growing from a single node on the stem."},
    ]
    return render_template('glossary.html', glossary_terms=glossary_terms)

# --- Run the Flask app in debug mode if this file is executed directly ---
if __name__ == '__main__':
    app.run(debug=True)