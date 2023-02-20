from models.users import User
import copy


def user_list_to_obj(users):

    # Finding the User attributes
    user_obj = User()
    users_obj = list()
    attribs = [attrib for attrib in dir(user_obj) if not attrib.startswith(
        '__') and not callable(getattr(user_obj, attrib))]

    # Create a list of objects
    for user in users:
        user_obj = User()
        for attrib in attribs:
            if attrib in user:
                setattr(user_obj, attrib, user[attrib])
        user_obj_copy = copy.copy(user_obj)
        users_obj.append(user_obj_copy)

    return users_obj
