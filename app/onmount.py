class OnMount :
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

