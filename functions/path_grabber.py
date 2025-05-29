import os


def grab_path_to_flacs(path: str | os.PathLike) -> list[str]:
    if not os.path.isdir(path):
        return []

    files_in_dir = os.listdir(path)

    flacs_only = [_ for _ in files_in_dir if _.endswith(".flac")]

    return flacs_only
