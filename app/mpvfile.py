import mpv

class Player:
    def __init__(self):
        self.player = mpv.MPV(
            vid = "no",
            input_default_bindings=True,
            input_vo_keyboard=True,
            log_handler = print,
        )

    def play(self, path):
        self.player.stop()
        self.player.play(path)

    def pause(self):
        self.player.pause = not self.player.pause


    def filename(self):
        return self.player.filename

    def stop_playback(self):
        self.player.stop()

    def start_play(self,path):
        self.player.loadfile(path, "append-play")

    def add_to_queue(self, path):
        self.player.loadfile(path, "append")

    def remove_play(self, path):
        self.player.loadfile(path, "replace")

    def play_next(self):
        if self.player.playlist_pos >= (self.player.playlist_count)-1:
            self.player.stop()
        else :
            self.player.playlist_next()

    def del_queue(self):
        self.player.stop()
        self.player.playlist_clear()

    def is_idle(self):
        return self.player.core_idle


    def is_empty(self):
        if self.player.playlist_count == 0:
            return True
        return False

