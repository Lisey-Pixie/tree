
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
]
t = input("Is the leaf simple or compound(if it has needles it is probably compound)")
n = input("How many leaflets, or needles in a cluster(If the leaf is simple just enter 1)")
l = input("How is the leaf shaped(ex: lobed, palmate, oval, elliptical, needles, diamond)")
s = input("Is the leaf small, medium or large")
c = input("What color is the leaf")
e = input("Is the edge serrated or smooth")
v = input("What are the veins like in the leaf. Do they all meet a central vein-pinnate, do they radiate out from a single point-palmate.")
x = input("What is the texture of the leaf, smooth or rough")
a = input("What color do the leaves turn in autumn")

user_description = {
    "leaf_type": t,
    "leaf_number": n,
    "leaf_shape": l,
    "leaf_size": s,
    "leaf_color": c,
    "leaf_edge": e,
    "venation": v,
    "texture": x,
    "leaf_autum": a
}



def identify_tree(user_description, trees):
    match_scores = []
    total_attributes = len(user_description)

    for tree in trees:
        score = 0
        
        for key, user_value in user_description.items():
            tree_value = tree.get(key)

            if not tree_value:
                continue

            # Always work with lists for easier comparison
            tree_values = tree_value if isinstance(tree_value, list) else [tree_value]

            # Compare user input to each possible value in the tree's list
            if any(user_value.lower() == str(val).lower() for val in tree_values):
                score += 1
        
        # Keep trees with score at least 50% of total attributes
        if score >= total_attributes / 2:
            match_scores.append((tree['name'], score))

    # Sort matches from most likely to least likely
    match_scores.sort(key=lambda x: x[1], reverse=True)
    return match_scores

# Call the function to identify the tree
matches = identify_tree(user_description, trees)

# Display the results
print("\nPossible matches (sorted):")
for match in matches:
    print(f"{match[0]} - Match score: {match[1]}")

# Show top 3 matches
top_matches = matches[:3]
print("\nTop possible matches:")
for i, (name, score) in enumerate(top_matches, 1):
    print(f"{i}. {name} (score: {score})")

# Let user pick one
choice = input("Enter the number of the tree you'd like more information about: ")
if choice.isdigit():
    index = int(choice) - 1
    if 0 <= index < len(top_matches):
        tree_name = top_matches[index][0]
        for tree in trees:
            if tree["name"] == tree_name:
                print(f"\nMore about {tree['name']}:")
                print(tree.get("description", "No description available."))

