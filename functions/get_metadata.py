import os
import re


def search_string(pattern: str, raw_string) -> str:
    match_result = re.search(pattern, raw_string)

    if match_result:
        match = match_result.group(1)
    else:
        match = ""

    return match


def data_splicer(path: str) -> tuple[str, str, str]:
    file_name = os.path.split(path)[1].split(".")[0]

    album = file_name[:file_name.find("{")].strip()

    song_tittle = search_string(r"{(.+)}", file_name).strip()

    artist = search_string(r"\[(.+)\]", file_name).strip()

    return (artist, song_tittle, album)


def main():
    test_path = ("D:\\vs_projects\\flac-renamer\\songs\\" +
                 "Ace Attorney {Never Lose} [Yamashita Tomohisa].flac")

    print(data_splicer(test_path))


if __name__ == '__main__':
    main()
