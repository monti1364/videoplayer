from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.videoplayer import VideoPlayer
from kivy.core.clipboard import Clipboard
import traceback

KV = '''
MDScreen:
    VideoPlayer:
        id: player
        source: "assets/v1.mp4"
        state: 'play'
        options: {'allow_stretch': True}
'''

class VideoApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

if __name__ == "__main__":
    try:
        VideoApp().run()
    except Exception as e:
        error=traceback.format_exc()
        Clipboard(str(error))                


