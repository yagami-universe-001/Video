# MongoDB utilities for Video Encoder Bot
from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URI

class MongoDB:
    def __init__(self):
        self.client = AsyncIOMotorClient(MONGO_URI) if MONGO_URI else None
        self.db = self.client["VideoBot"] if self.client else None
    async def set_thumb(self,user_id,file_id): 
        if not self.db: return
        await self.db.users.update_one({"_id":user_id},{"$set":{"thumb":file_id}},upsert=True)
    async def get_thumb(self,user_id):
        if not self.db: return None
        user = await self.db.users.find_one({"_id":user_id})
        return user.get("thumb") if user else None
    async def del_thumb(self,user_id):
        if not self.db: return
        await self.db.users.update_one({"_id":user_id},{"$unset":{"thumb":""}})
