import os

from functions.path_input import get_user_path
from functions.path_grabber import grab_path_to_flacs


def main():
    repo_directory = os.path.split(__file__)[0]
    default_path = os.path.join(repo_directory, "songs")

    songs_dir = get_user_path(default_path)

    print(songs_dir)

    flacs = grab_path_to_flacs(songs_dir)

    print(flacs)


if __name__ == '__main__':
    main()
