from helpers import Helpers
from textual.widgets import Static

class PlaybackActions:
    def action_play_next(self):
        self.player.play_next()

    def action_add_queue(self):
        if self.focused.id in ("songs3", "songs4"):
            Helpers.update_queue(self)

            if self.player.is_idle():
                song_url = self.back.play_song(self.all_songs[self.song_name])
                Helpers.update_nowplaying(self,self.song_name)
                self.run_worker(lambda: self.player.start_play(song_url), thread=True)

            else :
                song_url = self.back.play_song(self.all_songs[self.song_name])
                self.run_worker(lambda: self.player.add_to_queue(song_url), thread=True)
            

    def action_pause_play(self):
            self.player.pause()


    def action_go_backto(self):
        if self.focused.id in ("songs3", "songs4"):
            self.songs.remove_children()
            ab = Static("select an album", id = "songs2")
            self.songs.mount(Static("Select an Album"))
            self.albums.children[0].focus()

        elif self.focused.id in ("albums1", "albums2"):
            self.albums.remove_children()
            ab = Static("select an artist", id = "songs")
            self.albums.mount(ab)
            self.artists.focus()

    def action_right_switch(self):
        if self.focused is self.artists:
            self.albums.children[0].focus()

        if self.focused.id in ("albums1", "albums2"):
            self.queue.focus()


    def action_left_switch(self):
        if self.focused is self.albums or self.songs:
            self.artists.focus()

        if self.focused.id is "queue":
            self.albums.children[0].focus()
