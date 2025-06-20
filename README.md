# Virginia Tree Identifier

## Overview

The **Virginia Tree Identifier** is a Flask-based web application that helps users identify and learn about native trees of Virginia. Users can browse a gallery of trees, use a guided form to identify a tree based on its leaf characteristics, and keep track of the trees they have identified during their session.

## Features

- **Browse Trees:** View a gallery of native Virginia trees with images and names. Click any tree to see detailed information.
- **Identify a Tree:** Fill out a form describing a tree's leaf characteristics (type, shape, size, color, edge, venation, texture, and autumn color) to get the top 3 possible matches.
- **Tree Details:** Each tree has a dedicated page with its image, characteristics, and a description.
- **Session Tracking:** The app keeps track of trees you have identified in your current session, with an option to clear the list.
- **Responsive Design:** The site is mobile-friendly and adjusts to different screen sizes.
- **User-Friendly Navigation:** Easily switch between the home page, identifier, and browse pages.

## How It Works

1. **Home Page:** Welcomes users and provides a starting point for identification.
2. **Identify Page:** Users enter leaf characteristics; the app suggests the most likely matches.
3. **Browse Page:** Users can explore all trees in the database.
4. **Tree Detail Page:** Shows detailed information about a selected tree.
5. **Identified Trees:** Users see a list of trees they've identified and can clear this list at any time.

## Project Structure

- `save.py` — Main Flask application with routes and logic.
- `trees_data.py` — Data file containing all tree information.
- `templates/` — HTML templates for all pages (`base.html`, `frontPage.html`, `treeIdentifier.html`, `browse.html`, `tree_data.html`).
- `static/` — Folder for images used in the app.

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

## Customization

- Add or edit trees in `trees_data.py` to expand the database.
- Place new tree images in the `static/` folder and reference them in the data file.

## License

This project is for educational and personal use.

---

**Created by Annalise**