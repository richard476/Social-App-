from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from viewmodels.feed_viewmodel import FeedViewModel

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

feed_vm = FeedViewModel()

@app.get("/")
def show_feed(request: Request):
    return templates.TemplateResponse("feed.html", {"request": request, "posts": feed_vm.get_all_posts()})

@app.post("/post")
def create_post(request: Request, user_name: str = Form(...), content: str = Form(...), image_url: str = Form(None)):
    feed_vm.create_post(content=content, user_name=user_name, image_url=image_url)
    return RedirectResponse("/", status_code=303)

@app.post("/like/{post_id}")
def like_post(post_id: str):
    feed_vm.like_post(post_id)
    return RedirectResponse("/", status_code=303)

@app.post("/comment/{post_id}")
def comment_post(post_id: str, comment: str = Form(...)):
    feed_vm.add_comment(post_id, comment)
    return RedirectResponse("/", status_code=303)

@app.post("/save/{post_id}")
def save_post(post_id: str):
    feed_vm.toggle_save(post_id)
    return RedirectResponse("/", status_code=303)

@app.get("/post/{post_id}")
def view_single_post(request: Request, post_id: str):
    post = feed_vm.get_post_by_id(post_id)
    if not post:
        return RedirectResponse("/", status_code=303)
    return templates.TemplateResponse("single_post.html", {"request": request, "post": post})
