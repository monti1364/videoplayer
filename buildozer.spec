[app]
title = VideoPlayerApp
package.name = videoplayerapp
package.domain = org.test

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,mp4

# ✅ REQUIRED FIX
version = 1.0

# ✅ Video player + kivy + kivymd stable combo
requirements = python3,kivy==2.3.0,kivymd==1.1.1,ffpyplayer,pillow

orientation = portrait
fullscreen = 1

# ✅ Permissions (modern android safe)
android.permissions = INTERNET,READ_MEDIA_VIDEO,READ_EXTERNAL_STORAGE

android.api = 33
android.minapi = 21
android.ndk = 25b

android.accept_sdk_license = True

# ✅ ONLY ONE ARCH (stable)
android.archs = arm64-v8a

# Optional but recommended
android.logcat_filters = *:S python:D

[buildozer]
log_level = 2
warn_on_root = 1
