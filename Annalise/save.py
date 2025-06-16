
trees = [
    {
        "name": "Oak",
        "leaf_type": "simple",
        "leaf_shape": "lobed",
        "leaf_size": "large",
        "leaf_color": "green",
        "leaf_edge": "smooth",
        "venation": "pinnate",
        "texture": "rough"
    },
    {
        "name": "Maple",
        "leaf_type":"simple",
        "leaf_shape": "palmate",
        "leaf_size": "medium",
        "leaf_color": "green",
        "leaf_edge": "serrated",
        "venation": "palmate",
        "texture": "smooth"
    },
    {
        "name": "Birch",
        "leaf_type": "simple"
        "leaf_shape": "oval",
        "leaf_size": "small",
        "leaf_color": "yellow",
        "leaf_edge": "serrated",
        "venation": "pinnate",
        "texture": "smooth"
    }
    {
        "name": "Birch",
        "leaf_shape": "diamond",
        "leaf_size": "medium",
        "leaf_color": "yellow",
        "leaf_edge": "serrated",
        "venation": "pinnate",
        "texture": "smooth"
    }
    {
        "name": "Tulip Poplar",
        "leaf_type":"simple",
        "leaf_shape":"lobed",
        "leaf_size":"medium",
        "leaf_color":"green",
        "leaf_edge":"smooth",
        "venation":"palmate",
        "texture":"smooth",
    }
]
t = input("Is the leaf simple or compound")
l = input("How is the leaf shaped(ex: lobed, palmate)")
s = input("Is the leaf small medium or large")
c = input("What color is the leaf")
e = input("Is the edge serrated or smooth")
v = input("whate are the veins like in the leaf. Do they all meet a central vein-pinnate, do they radiate out from a single point-palmate.")
x = input("what is the texture of the leaf, smooth or rough")
user_description = {
    "leaf_type": t,
    "leaf_shape": l,
    "leaf_size": s,
    "leaf_color": c,
    "leaf_edge": e,
    "venation": v,
    "texture": x
}


def identify_tree(user_description, trees):
    match_scores = []  # List to hold trees with their match scores
    total_attributes = len(user_description)  # Get the total number of user attributes
    
    # Loop through each tree in the database
    for tree in trees:
        score = 0  # Initialize the match score
        
        # For each attribute in the user description
        for key, user_value in user_description.items():
            tree_value = tree.get(key, None)  # Get the tree's attribute value
            
            # If the attribute exists and matches the user input, increment the score
            if tree_value and tree_value.lower() == user_value.lower():
                score += 1
        
        # Only add trees to the list if they match at least half of the user description
        if score >= total_attributes // 2:  # If it matches at least half the criteria
            match_scores.append((tree['name'], score))
    
    # Sort the match scores in descending order (most likely match first)
    match_scores.sort(key=lambda x: x[1], reverse=True)
    
    # Return the sorted list of matches (tree name and score)
    return match_scores

# Run the matching function
matches = identify_tree(user_description, trees)
print("Possible matches (sorted):")
for match in matches:
    print(f"{match[0]} - Match score: {match[1]}")