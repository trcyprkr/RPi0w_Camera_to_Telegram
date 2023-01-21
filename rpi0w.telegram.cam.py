import picamera
import telegram # pip install python-telegram-bot
from time import sleep
import asyncio
from PIL import Image

BOT_TOKEN = 'your bot token here'
CHANNEL_ID = 'your channel id here'
bot = telegram.Bot(token=BOT_TOKEN)

camera = picamera.PiCamera()
camera.start_preview()
print('Camera warm-up time')
sleep(3)
camera.capture('capture.jpg')
print('Image Captured')
camera.close()
Raw_Image = Image.open("capture.jpg")
img = Raw_Image.rotate(180)
img.save('capture.jpg')
img = '/home/pi/capture.jpg'
sleep(3)
picbot = bot.send_photo(chat_id=CHANNEL_ID, photo=open(img, 'rb'), caption=None)
asyncio.run(picbot)
print('Picture Sent')
