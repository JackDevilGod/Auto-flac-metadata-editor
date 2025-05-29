import os


def get_user_path(default: str | os.PathLike):
    print(f"default path is: {default}\nEnter for default.")
    user_input = input("Input path to song directory.\n")

    while not os.path.isdir(user_input) and user_input != "":
        print(f"default path is: {default}\nEnter for default.")
        user_input = input("Input path to song directory.\n")

    if user_input == "":
        return default

    return user_input
