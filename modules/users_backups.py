from models.users import User
import copy


def users_backups(users: list[User], sites: list):

    backup_users = list()
    backup_user = User()

    for site in sites:
        for user in users:
            backup_user = copy.copy(user)
            backup_user.site = site
            backup_users.append(backup_user)

    users.extend(backup_users)

    return users
