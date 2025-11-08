from textual.widgets import ListView, ListItem, Static
from backend import artists



class Artists(ListView):

    BINDINGS = [ ("enter", "select_cursor", "Select"),
                ("k", "cursor_up", "Cursor up"),
                ("j", "cursor_down", "Cursor down"),
                    ]

    def compose(self):
        artist_names = list(artists.keys())
        for artist in artist_names :
            yield ListItem(Static(artist), classes = "artists1")

class Albums(Static):

    BINDINGS = [ ("enter", "select_cursor", "Select"),
                ("k", "cursor_up", "Cursor up"),
                ("j", "cursor_down", "Cursor down"),
                    ]
    def compose(self):
        yield Static("Albums")


class Songs(Static):
    def compose(self):
        yield Static("SongList")

class NowPlaying(Static):
    def compose(self):
        yield Static("Now Playing")

class Queue(Static):
    def compose(self):
        yield Static("[#87CEFA bold]Queue[/]")
