def userEntity(item) -> dict:
    return{
        "id": item["id"],
        "name": item["name"],
        "email": item["email"],
        "password": item["password"]
    }


def usersEntity(entity) -> list:
    [userEntity(item) for item in entity]

def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}