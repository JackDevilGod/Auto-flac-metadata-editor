import os


def grab_path_to_flacs(base_path: str | os.PathLike, folder_name: str) -> list[str]:
    full_path = os.path.join(base_path, folder_name)

    files_in_dir = os.listdir(full_path)

    flacs_only = [_ for _ in files_in_dir if _.endswith(".flac")]

    return flacs_only
