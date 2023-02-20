from models.users import User
import copy


def users_backups(users: list[User], servers: list):

    backup_users = list()
    backup_user = User()

    for server in servers:
        for user in users:
            backup_user = copy.copy(user)
            backup_user.server = server
            backup_users.append(backup_user)

    users.extend(backup_users)

    return users
