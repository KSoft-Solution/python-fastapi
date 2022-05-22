from models.user import User
from config.db import user_collection
from schemas.user import ResponseModel, userEntity


class UserController:
   def create_User(user: User):
        try:
            new_user = userEntity(user)
            user = user_collection.insert_one(new_user)
            return ResponseModel(user,'user created successfully')
            
        except Exception as e:
            return None


user_controller = UserController
