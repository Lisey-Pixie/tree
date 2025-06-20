# Virginia Tree Identifier

## Overview

The **Virginia Tree Identifier** is a Flask web application that helps users identify, browse, and learn about native trees of Virginia. The app provides multiple ways to explore tree species, including a guided identification form, a searchable and browsable gallery, and a personal checklist for users to track which trees they have identified.

---

## Features

- **Home Page:** Welcoming introduction with images and a call-to-action to start identifying trees.
- **Tree Identifier:** Guided form where users enter leaf characteristics (type, number, shape, size, color, edge, venation, texture, autumn color) to get the top 3 matching Virginia trees.
- **Browse Trees:** Gallery view of all trees in the database, each with an image and name. Clicking a tree shows its details.
- **Tree Detail Pages:** Each tree has a dedicated page with its image, characteristics, and a descriptive summary. Navigation buttons allow users to return to browse, identify, or search pages.
- **Search:** Users can search for trees by name and view matching results.
- **Personal Treelist (Checklist):** Users can check off trees they have identified. Checked trees are italicized for visual feedback. The checklist is saved in the session and can be cleared with confirmation.
- **Identified Trees Tracking:** When a user identifies a tree via the identifier, it is added to a session-based list, which can also be cleared.
- **Responsive Design:** The app is mobile-friendly and adapts to different screen sizes.
- **Accessible Navigation:** Easy navigation between Home, Identify, Treelist, Browse, and Search pages.

---

## Project Structure

```
/Annalise
│
├── save.py                  # Main Flask application with all routes and logic
├── trees_data.py            # Data file containing all tree information
├── /templates
│   ├── base.html            # Base template with navigation and styling
│   ├── frontPage.html       # Home page
│   ├── treeIdentifier.html  # Tree identification form and results
│   ├── browse.html          # Gallery of all trees
│   ├── tree_data.html       # Detail page for each tree
│   ├── treelist.html        # User checklist page
│   └── search.html          # Search page
└── /static
    └── *.jpeg               # Tree images
```

---

## How It Works

1. **Start on the Home Page:** Users are greeted and can begin identifying trees.
2. **Identify a Tree:** Users fill out a form describing a tree’s leaves. The app suggests the top 3 matches, and users can view details for each.
3. **Browse All Trees:** Users can scroll through a gallery of all trees and click any for more information.
4. **Tree Details:** Each tree’s page shows its image, characteristics, and description, with navigation to other parts of the app.
5. **Search:** Users can search for trees by name.
6. **Treelist (Checklist):** Users can manually check off trees they have identified. Checked trees are italicized, and the list can be saved or cleared (with confirmation).
7. **Session Tracking:** Both the identifier and checklist use Flask sessions to remember user progress during their visit.

---

## Getting Started

1. **Install dependencies:**
    ```bash
    pip install flask
    ```
2. **Run the app:**
    ```bash
    python save.py
    ```
3. **Open your browser:**  
   Visit `http://127.0.0.1:5000/` to use the app.

---

## Customization

- **Add/Edit Trees:** Update `trees_data.py` to add more species or edit existing ones.
- **Add Images:** Place new images in the `static/` folder and reference them in the data file.
- **Styling:** Modify `base.html` for global styles and layout.

---

## License

This project is for educational and personal use.

---

**Created by Annalise**