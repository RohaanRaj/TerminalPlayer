from helpers import Helpers
from textual.widgets import ListView, ListItem
from widgets import Artists, Albums, NowPlaying 

class OnSelection:
    def on_list_view_selected(self, event: ListView.Selected):
        if isinstance(event.list_view, Artists):
            artist_selected = event.item.children[0].render()
            Helpers.load_albums(self, artist_selected)

        elif event.list_view.id in ("albums1" , "albums2"):
            selected_album = event.item.children[0].render()
            Helpers.load_songs(self, selected_album)

        elif event.list_view.id in ("songs3", "songs4"):
            now_playing = event.item.children[0].render()
            Helpers.update_nowplaying(self, now_playing)
            Helpers.update_queue2(self, now_playing)

            if self.player.is_empty() and self.player.is_idle():
                self.player.start_play(self.back.play_song(self.all_songs[now_playing]))

            else: 
                self.queue_list.clear()
                Helpers.update_queue2(self, now_playing)
                self.player.remove_play(self.back.play_song(self.all_songs[now_playing]))
