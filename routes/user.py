from fastapi import APIRouter, responses
from schemas.user import userEntity, usersEntity
from models.user import User
from config.db import user_collection


user = APIRouter()

# get all users


@user.get('/users')
async def get_all_users():
    return usersEntity(user_collection.find())

# get user


@user.get('/users/{id}')
async def get_user():
    return 'i am user'

# create user


@user.post('/users')
async def create_user(user: User):
    new_user = dict(user)
    data = user_collection.insert_one(new_user)
    if data is None:
        return responses.JSONResponse(status_code=500,
                                      content={"message": "Internal Server Error"})
    return responses.JSONResponse(status_code=200,
                                  content={"message": "success", "data": userEntity(data)})

# update user


@user.put('/users/{id}')
async def update_user():
    return 'i am user'

# delete user


@user.delete('/users/{id}')
async def delete_user():
    return 'i am user'
