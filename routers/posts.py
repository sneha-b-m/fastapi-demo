from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import store

router=APIRouter(prefix="/posts", tags=["posts"])

class PostCreate(BaseModel):
    content: str
    author: str

class PostUpdate(BaseModel):
    content: str | None=None
    author: str | None=None

@router.post("",status_code=201)
def create_post(payload: PostCreate):
    return store.create(payload.content, payload.author)

@router.get("")
def list_posts():
    return store.get_all()

@router.get("/{post_id}")
def get_post(post_id: int):
    post= store.get_by_id(post_id)
    if not post:
        raise HTTPException(status_code=404, detail="not found")
    return post

@router.put("/{post_id}")
def update_post(post_id: int, payload: PostUpdate):
    post=store.update(post_id,payload.model_dump(exclude_unset=True))
    if not post:
        raise HTTPException(status_code=404, detail="not found")

@router.delete("/{post_id}", status_code=204)
def delete_post(post_id: int):
    if not store.remove(post_id):
        raise HTTPexception(status_code=404, detail="not found")