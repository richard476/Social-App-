from typing import List
from models.post import Post
import asyncio

class PostService:
    @staticmethod
    async def get_all_posts() -> List[Post]:
        await asyncio.sleep(0.5)  # Simulate network/database delay
        return [Post.sample(i) for i in range(8)]
