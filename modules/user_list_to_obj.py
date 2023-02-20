from models.users import User


def user_list_to_obj(users: list[User]):

    user_obj = User()
    users_obj = list()
    props = [prop for prop in dir(user_obj) if not prop.startswith(
        '__') and not callable(getattr(user_obj, prop))]

    for user in users:
        for prop in props:
            if prop in user:
                setattr(user_obj, prop, user[prop])
        users_obj.append(user_obj)

    return users_obj
