from textual.widgets import ListItem, ListView, Static
class DefList(ListView):

    BINDINGS = [ ("enter", "select_cursor", "Select"),
                ("k", "cursor_up", "Cursor up"),
                ("j", "cursor_down", "Cursor down"),
                    ]

class Helpers():
    def update_queue(self):
        temp1 = self.songs.query_one(ListView) 
        temp2 = temp1.children[temp1.index]
        self.song_name = temp2.children[0].render()
        self.queue_list.append(ListItem(Static(self.song_name)))

    def update_queue2(self, now_playing):
        self.queue_list.append(ListItem(Static(now_playing)))

    def update_nowplaying(self, now_playing):
        self.nowplaying.remove_children()
        self.nowplaying.mount(Static(now_playing))

    def load_albums(self , artist_selected):
        a = '1' if self.b == 0 else "2"
        self.b = 1-self.b
        self.artist_selected = artist_selected
        self.artist = self.back.get_album(artist_selected)
        albums = self.artist.keys()
        updated_albums = DefList(*[ListItem(Static(album)) for album in albums] , id = "albums"+a)
        self.albums.remove_children()
        self.albums.mount(updated_albums)
        updated_albums.focus()


    def load_songs(self, selected_album):
        a = '3' if self.c == 0 else "4"
        self.c = 1-self.c
        self.selected_album = selected_album
        self.all_songs = self.back.get_songs(self.artist, selected_album)
        allsongs = self.all_songs.keys()
        list_songs = DefList(*[ListItem(Static(song)) for song in allsongs], id = "songs"+a)
        self.songs.remove_children()
        self.songs.mount(list_songs)
        list_songs.focus()
