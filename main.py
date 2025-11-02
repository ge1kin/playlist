liked_songs = {
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


def add_song(song_name: str, artist: str, genre: str, duration: tuple) -> None:
    liked_songs[song_name] = {"artist": artist, "genre": genre, "duration": duration}


def main():
    song_amount = int(input("Enter the amount of songs you would like to add as an integer number: "))
    i = 0
    while i < song_amount:
        song_name = input("Enter the name of the song: ")
        while song_name in liked_songs.keys():
            lower_amount = input("That song is already in the playlist of liked songs. would you like to lower the amount of songs you would like to add? ")
            if lower_amount.lower() == "yes":
                i += 1
            i += 1
            song_name = input("Enter the name of the song: ")
        artist = input("Enter the name of the artist: ")
        genre = input("Enter the genre: ")
        duration = (int(input("Enter the amount of minuets: ")), int(input("Enter the amount of secondes: ")))
        add_song(song_name, artist, genre, duration)


if __name__ == "__main__":
    main()

