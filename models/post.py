from typing import Optional, List
from uuid import uuid4

class Post:
    def __init__(self, id: str, content: str, user_name: str, image_url: Optional[str] = None,
                 timestamp: str = "", likes: int = 0, comments: Optional[List[str]] = None, saved: bool = False):
        self.id = id
        self.content = content
        self.user_name = user_name
        self.image_url = image_url
        self.timestamp = timestamp
        self.likes = likes
        self.comments = comments or []
        self.saved = saved

    @staticmethod
    def sample(index: int):
        usernames = ["Richard", "Pooja", "Gokul", "Asmitha", "Adithya", "Nirupama", "Salaman", "Sanjay"]
        username = usernames[index % len(usernames)]

        return Post(
            id=str(uuid4()),
            content=f"This is post #{index + 1} by {username}",
            image_url="https://picsum.photos/seed/{}/500/300".format(index) if index % 2 == 0 else None,
            user_name=username,
            timestamp="2025-08-06 19:{:02d}".format(index),
            likes=0,
            comments=[],
            saved=False
        )
