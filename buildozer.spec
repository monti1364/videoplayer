[app]
# (str) Title of your application
title = VideoPlayerApp

# (str) Package name
package.name = videoplayerapp

# (str) Package domain (needed for android packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let's include mp4)
source.include_exts = py,png,jpg,kv,atlas,mp4

# (list) Application requirements
# CRITICAL: ffpyplayer is needed for VideoPlayer to work on Android
requirements = python3,kivy==2.3.0,kivymd==1.1.1,ffpyplayer,sdl2_ttf,pillow

# (str) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (list) Permissions
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (int) Android API to use
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) If True, then skip trying to update the Android sdk
android.skip_update = False

# (bool) If True, then automatically accept SDK license
android.accept_sdk_license = True

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = arm64-v8a, armeabi-v7a

# (list) The Android architectures to build for (e.g. adb -s <device> shell getprop ro.product.cpu.abi)
# For modern phones, arm64-v8a is best.
android.arch = arm64-v8a

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = off, 1 = on)
warn_on_root = 1

