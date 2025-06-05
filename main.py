from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from database import init_db, get_lawyers_by_specialty, get_example_cases, find_closest_example

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

init_db()

CATEGORY_KEYWORDS = {
    "Family Law": ["divorce", "marriage", "child", "custody", "alimony", "adoption"],
    "Criminal": ["crime", "theft", "assault", "arrest", "murder", "criminal", "fraud"],
    "Real Estate": ["property", "real estate", "lease", "rent", "eviction", "mortgage", "landlord"],
    "Labor Law": ["work", "salary", "employment", "labor", "job", "contract", "fired", "overtime"],
    "Immigration": ["visa", "immigration", "citizenship", "green card", "deportation", "asylum"],
}

def detect_category(text: str):
    text = text.lower()
    for category, keywords in CATEGORY_KEYWORDS.items():
        for kw in keywords:
            if kw in text:
                return category
    return None

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    examples = get_example_cases()
    return templates.TemplateResponse("index.html", {
        "request": request,
        "lawyers": None,
        "category": None,
        "query": "",
        "examples": examples
    })

@app.post("/", response_class=HTMLResponse)
async def search(request: Request, query: str = Form(...)):
    category = detect_category(query)
    examples = get_example_cases()
    closest_example = find_closest_example(query)
    # Try to infer category from closest example if not found
    if not category and closest_example:
        category = detect_category(closest_example)
    lawyers = get_lawyers_by_specialty(category) if category else []
    return templates.TemplateResponse("index.html", {
        "request": request,
        "lawyers": lawyers,
        "category": category,
        "query": query,
        "examples": examples,
        "closest_example": closest_example
    })