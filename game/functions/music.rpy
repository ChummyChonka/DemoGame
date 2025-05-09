init python:
    from enum import Enum

    class MusicState(Enum):
        STOPPED = 0
        PLAYING = 1
        PAUSED = 2
        FULL_STOPPED = 3

    class GameMusic():
        def __init__(self):
            self.currently_playing = "audio/music/kevinmacleod/Funky Boxstep.mp3"
            self.currently_playing_short = self.get_song_title_only(self.currently_playing)
            self.state = MusicState.STOPPED #0 -> stopped, 1 -> playing, 2 -> paused


        def stop_music(self, full_stop=False):
            renpy.music.stop(fadeout=2.0)
            if full_stop:
                self.state = MusicState.FULL_STOPPED
            else:
                self.state = MusicState.STOPPED


        def play_song(self, song):
            if(self.state == MusicState.FULL_STOPPED):
                return
            if(self.state == MusicState.PLAYING) and (self.currently_playing == song):
                return
            self.currently_playing = song
            self.currently_playing_short = self.get_song_title_only(song)
            self.state = MusicState.PLAYING
            if(renpy.music.is_playing):
                renpy.music.stop(fadeout=2)
                renpy.music.queue(self.currently_playing, loop=True, fadein=2)
            else:
                renpy.music.play(self.currently_playing, loop=True, fadein=2)


        def get_song_title_only(self, song):
            '''
            Removes leading path and file extension from filename
            '''
            # split at /, get last index
            # split that at 0 and take first index
            return song.split("/")[-1].split(".")[0]
