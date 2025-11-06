LIKED_SONGS = {
    "Shake It Off": {
        "artist": "Taylor Swift",
        "duration": (3, 23),
        "genre": "Pop"
    },
    "Shemesh": {
        "artist": "Mergi",
        "duration": (2, 33),
        "genre": "Israeli"
    },
    "Chop Suey!": {
        "artist": "System of a Down",
        "duration": (3, 30),
        "genre": "Metal"
    },
    "Mimaamakim": {
        "artist": "Idan Raichel",
        "duration": (4, 33),
        "genre": "Israeli"
    },
    "Do I Wanna Know?": {
        "artist": "Arctic Monkeys",
        "duration": (4, 26),
        "genre": "Rock"
    },
    "Love Story": {
        "artist": "Taylor Swift",
        "duration": (3, 55),
        "genre": "Pop"
    },
    "Bo’ee": {
        "artist": "Idan Raichel",
        "duration": (4, 45),
        "genre": "Israeli"
    }
}

def check_in_liked(song_name: str) -> bool:
    return song_name in LIKED_SONGS.keys()


def add_song(song_name: str, artist: str, genre: str, duration: tuple) -> None:
    LIKED_SONGS[song_name] = {"artist": artist, "genre": genre, "duration": duration}


def get_song_info(song_amount: int) -> None:
    added_counter = 0
    while  added_counter < song_amount:
        song_name = input("Enter the name of the song: ")
        if check_in_liked(song_name):
            lower_amount = input("That song is already in the playlist of liked songs. would you like to lower the amount of songs you would like to add? ")
            if lower_amount.lower() == "yes":
                added_counter += 1
        else:
            artist = input("Enter the name of the artist: ")
            genre = input("Enter the genre: ")
            duration = (int(input("Enter the amount of minuets: ")), int(input("Enter the amount of secondes: ")))
            add_song(song_name, artist, genre, duration)
            added_counter += 1

def remove_song(song_name: str) -> None:
    del LIKED_SONGS[song_name]


def remove_by_artist(artist: str) -> None:
    remove_lst = []
    for song, info in LIKED_SONGS.items():
        if info["artist"] == artist:
            remove_lst.append(song)
    while len(remove_lst) > 0:
        remove_song(remove_lst[0])
        remove_lst.remove(remove_lst[0])


def main() -> None:
    song_amount = int(input("Enter the amount of songs you would like to add as an integer number: "))
    get_song_info(song_amount)
    song_name = input("Enter song to remove: ")
    if check_in_liked(song_name):
        remove_song(song_name)
    else:
        print(f"The song {song_name} is not in the liked songs")
    remove_by_artist(input("Enter artist name: "))
    print(LIKED_SONGS)


if __name__ == "__main__":
    main()

