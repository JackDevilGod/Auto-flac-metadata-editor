import os
from mutagen import flac as flc
from tqdm import tqdm

from functions.path_input import get_user_path
from functions.path_grabber import grab_path_to_flacs
from functions.get_metadata import data_splicer


def main():
    repo_directory = os.path.split(__file__)[0]
    default_path = os.path.join(repo_directory, "songs")

    songs_dir = get_user_path(default_path)

    flacs = grab_path_to_flacs(songs_dir)

    print(f"working on song in {songs_dir}\nfound {len(flacs)} songs.")

    for flac in tqdm(flacs):
        current_flac = flc.Open(flac)

        artist, song_tittle, album = data_splicer(flac)

        current_flac["artist"] = [f"{artist}"]
        current_flac["tittle"] = [f"{song_tittle}"]
        current_flac["album"] = [f"{album}"]

        current_flac.save()


if __name__ == '__main__':
    main()
