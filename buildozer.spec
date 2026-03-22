[app]
title = MyVideoApp
package.name = myvideoapp
package.domain = org.example

source.dir = .
# ✅ Assets folder ko include karna zaroori hai
source.include_exts = py,png,jpg,kv,mp4
source.include_patterns = assets/*

version = 0.1

# ✅ IMPORTANT: Video ke liye ye requirements honi chahiye
requirements = python3,kivy==2.3.0,kivymd==1.1.1,pillow,ffpyplayer,ffmpeg,hostpython3

orientation = portrait
fullscreen = 1

# ✅ Permissions for Storage & Video
android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,READ_MEDIA_VIDEO

# ✅ Stability ke liye API 31-33 best hai
android.api = 31
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True

# ✅ Architecture (Sirf 64-bit rakhein fast build ke liye)
android.archs = arm64-v8a

# ✅ Debugging enabled
android.logcat_filters = *:S python:D

[buildozer]
log_level = 2
warn_on_root = 1
