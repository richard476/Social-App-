from models.post import Post
from uuid import uuid4
from typing import List, Optional

class FeedViewModel:
    def __init__(self):
        self.posts: List[Post] = [Post.sample(i) for i in range(6)]

    def get_all_posts(self) -> List[Post]:
        return list(reversed(self.posts))  # Most recent first

    def get_post_by_id(self, post_id: str) -> Optional[Post]:
        return next((p for p in self.posts if p.id == post_id), None)

    def create_post(self, content: str, user_name: str, image_url: Optional[str] = None):
        new_post = Post(
            id=str(uuid4()),
            content=content,
            user_name=user_name,
            image_url=image_url,
            timestamp="2025-08-06 20:00",
            likes=0,
            comments=[],
            saved=False
        )
        self.posts.append(new_post)

    def like_post(self, post_id: str):
        post = self.get_post_by_id(post_id)
        if post:
            post.likes += 1

    def add_comment(self, post_id: str, comment: str):
        post = self.get_post_by_id(post_id)
        if post:
            post.comments.append(comment)

    def toggle_save(self, post_id: str):
        post = self.get_post_by_id(post_id)
        if post:
            post.saved = not post.saved
