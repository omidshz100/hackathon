# 🚀 Legal Assistant Web App

A full-stack web application that helps users find lawyers based on their legal issues. Built with **FastAPI**, **SQLite**, and **Bootstrap**.

## Features

- **User-Friendly Form:** Users can describe their legal problem in free text.
- **Smart Classification:** The backend classifies the user's issue into a legal category using keyword and example matching.
- **Lawyer Search:** Finds and displays lawyers specializing in the detected legal category.
- **Example Cases:** 100+ example legal queries are stored in the database and shown as clickable suggestions.
- **Searchable Examples:** Users can filter example cases with a search box and auto-fill the form by clicking an example.
- **Bootstrap Styling:** Clean, responsive UI using Bootstrap 5.
- **No External NLP:** Uses simple Python logic for classification (no external AI/NLP libraries).

## How It Works

1. **User Input:** User enters a legal issue or selects an example case.
2. **Category Detection:** The backend tries to match the input to a legal category using keywords and the closest example.
3. **Lawyer Lookup:** The app queries the SQLite database for lawyers with the matching specialty.
4. **Results Display:** Matching lawyers are shown as Bootstrap cards. The closest example is also displayed for clarity.

## Project Structure

```
.
├── main.py              # FastAPI app, routes, and server startup
├── database.py          # SQLite DB setup, fake data, and example cases
├── models.py            # Pydantic models (if needed)
├── templates/
│   └── index.html       # Jinja2 template for the main page
├── static/              # (Optional) Custom CSS/JS
└── README.md            # Project documentation
```

## Setup & Run

1. **Install dependencies:**
    ```
    pip install fastapi uvicorn jinja2 python-multipart
    ```

2. **Run the app:**
    ```
    uvicorn main:app --reload
    ```

3. **Open in browser:**
    ```
    http://127.0.0.1:8000/
    ```

## Example Use

- Type: `I’m having problems with the apartment I bought. The seller didn’t disclose existing structural damage, and now I’m stuck with unexpected repair costs. I don’t know what to do.`
- The app will suggest the closest example (e.g., "I need help with my divorce.") and show relevant lawyers.

## Customization

- Add more keywords in `main.py` for better classification.
- Add or edit example cases in `database.py`.
- Style the UI further in `templates/index.html` or add CSS in `static/`.

---

**Made with FastAPI, SQLite, and Bootstrap.**
