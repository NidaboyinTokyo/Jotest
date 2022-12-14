import json

user = json.loads('{"id" : 100, "name" : "홍길동"}')

# print('usename is ' + user['name'])
print(f'usename is {user["name"]}')

def userinfo(u):
    """ 사용자 정보를 상세히 보여줌
    
    Args : 
        u (User) : User Json Object

    Returns :
        String : User Information
    """

    id = u["id"]
    name = u["name"]
    return f'ID is {id}, Name is {name}'

print(f'User Information : {userinfo(user)}')