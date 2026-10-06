from datetime import datetime, timezone

posts=[]
next_id=1

def get_all():
    return posts

def get_by_id(post_id):
    return next((p for p in posts if p["id"]==post_id), None)

def create(content, author):
    global next_id
    post={
        "id":next_id,
        "content":content,
        "author":author,
        "created_at":datetime.now(timezone.utc).isoformat(),
    }
    posts.append(post)
    next_id +=1
    return post

def update(post_id, updates):
    post=get_by_id(post_id)
    if not post:
        return None
    post.update(updates)
    return post

def remove(post_id):
    global posts
    before=len(posts)
    posts=[p for p in posts if p["id"]!=post_id]
    return len(posts)<before