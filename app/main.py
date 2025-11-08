'''
import os
import sys
dll_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "lib")
os.environ["PATH"] = dll_dir + os.pathsep + os.environ["PATH"]
'''

from textual.app import App
from textual.widgets import ListView
from textual.containers import Vertical, Horizontal
from mpvfile import Player
from backend import RequestsLib
from helpers import Helpers
from widgets import Artists, Songs, Albums, NowPlaying, Queue
from actions import PlaybackActions
from events import OnSelection


class Project(App, PlaybackActions, OnSelection):
    CSS_PATH = "styles.css"

    BINDINGS = [
        ("h", "left_switch", "using h to switch left panels"), 
        ("l", "right_switch", "using l to switch to right panels"),
        ("b", "go_backto", "clear & goto previous pane"),
        ("p", "pause_play","control playback"),
        ("q" ,"add_queue", "add an album/song to queue"),
        ("n", "play_next", "play the next song"),
    ]

    def compose(self):
        with Horizontal():
            yield Artists(classes = "box", id = "artists")
            with Vertical():
                yield NowPlaying(classes = "box", id = "playing")
                with Horizontal():
                    yield Albums(classes = "box", id = "albums")
                    yield Queue(classes = "box", id = "queue")
                yield Songs(classes = "box", id = "songs")

    def on_mount(self):
        self.show_vertical_scrollbar = False
        self.show_horizontal_scrollbar = False
        self.artists = self.query_one("#artists", Artists)
        self.albums = self.query_one("#albums", Albums)
        self.songs = self.query_one("#songs", Songs)
        self.nowplaying = self.query_one("#playing", NowPlaying)
        self.queue = self.query_one("#queue", Queue)
        self.b = 0
        self.c = 0
        self.player = Player()
        self.back= RequestsLib()
        self.queue_list = ListView()
        self.queue.mount(self.queue_list)
        @self.player.player.event_callback('end-file')
        def _(_event):

            def ui_update():
                next_item = None
                if len(self.queue_list.children) > 1:
                    next_item = self.queue_list.children[1].children[0].render()
                
                if self.queue_list.children:
                    self.queue_list.children[0].remove()

                if next_item:
                    Helpers.update_nowplaying(self, next_item)
                else:
                    Helpers.update_nowplaying(self, "Nothing is Playing")

            self.call_from_thread(ui_update)

if __name__ == "__main__":
    app = Project()
    app.run()
