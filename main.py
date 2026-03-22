from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.videoplayer import VideoPlayer
from kivy.core.clipboard import Clipboard
from kivy.logger import Logger
import traceback

# KV String
KV = '''
MDScreen:
    md_bg_color: 0, 0, 0, 1
    VideoPlayer:
        id: player
        source: "assets/v1.mp4"
        state: 'play'
        options: {'allow_stretch': True}
'''

class VideoApp(MDApp):
    def build(self):
        try:
            return Builder.load_string(KV)
        except Exception as e:
            self.copy_error_to_clipboard(traceback.format_exc())

    def copy_error_to_clipboard(self, error_text):
        Logger.error(f"AppCrash: {error_text}")
        Clipboard.copy(error_text)

if __name__ == "__main__":
    try:
        VideoApp().run()
    except Exception:
        error_msg = traceback.format_exc()
        Clipboard.copy(error_msg)
        Logger.error(f"CriticalCrash: {error_msg}")
        
