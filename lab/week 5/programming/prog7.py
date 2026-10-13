'''
작성일: 2026.10.13
작성자: 조영채

문제: 하나의 앨범(Album)에는 많은 노래(Song)가 담길 수 있다. 노래를 부른 가수(Artist)는 여러 노래를 소유할 수 있다.
        재생 목록(Playlist)은 여러 노래를 가질 수 있다. has-a 관계를 염두에 두고 프로그래밍해보자.

설계:

- 클래스:
    - Album: 앨범 제목, 가수, 발매 연도, 수록곡 목록을 저장한다.
        - add_track(title): 노래를 만들어 앨범과 가수의 목록에 추가한다.

    - Song: 노래 제목과 노래를 부른 가수를 저장한다.

    - Artist: 가수 이름과 가수의 노래 목록을 저장한다.

    - Playlist: 재생 목록 이름과 노래 목록을 저장한다.
        - add_song(song): 노래를 재생 목록에 추가한다.
'''

class Artist:
    def __init__(self, name):
        self.name = name
        self.songs = []


class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist


class Album:
    def __init__(self, title, artist, year):
        self.title = title
        self.artist = artist
        self.year = year
        self.tracks = []

    def add_track(self, title):
        # 노래 객체를 만들고 앨범과 가수의 노래 목록에 각각 추가한다.
        song = Song(title, self.artist)
        self.tracks.append(song)
        self.artist.songs.append(song)
        return song


class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        # 같은 노래가 재생 목록에 중복해서 들어가지 않게 한다.
        if song not in self.songs:
            self.songs.append(song)


def test_prog7():
    top = Artist("twenty one pilots")
    album = Album("self-titled", top, 2009)
    album.add_track("Air Catcher")
    album.add_track("Johnny Boy")

    playlist = Playlist("애창곡")

    for song in album.tracks:
        playlist.add_song(song)

    print(f"{album.title} 앨범의 수록곡:")
    for song in album.tracks:
        print(f"- {song.title}")

    print(f"{playlist.name} 재생 목록:")
    for song in playlist.songs:
        print(f"- {song.title} - {song.artist.name}")


if __name__ == "__main__":
    test_prog7()
