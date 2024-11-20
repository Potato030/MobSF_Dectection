import os

USER_HOME = os.path.expanduser("~")

DEVICE = 'android'
EMULATOR_NAME = 'Google Pixel 5_1'
EMULATOR_PATH = os.path.join(r'C:\Program Files\Genymobile\Genymotion\player.exe')
MOBSF_NAME = 'Mobile-Security-Framework-MobSF-master'

SERVER = 'http://127.0.0.1:8000'

AES_KEY = b'dbcdcfghijklmaop'
APK_PATH = os.path.join(os.getcwd(), '..', 'sample.apk')

FRIDA_PATH = 'frida_script.js'