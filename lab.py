import pygame
import requests
from io import BytesIO
name='ارسلان'
greeting_str=f'یک دو سه، شروع کن {name}'
greeting_url = f"https://api.farsireader.com/ArianaCloudService/ReadTextGET?APIKey=4JN129JCAF20A6S&Text={greeting_str}&Speaker=Male1&Format=mp3"
# Initialize Pygame
pygame.init()

# URL of the MP3 file
mp3_url = "greeting_url"

# Fetch the MP3 data from the URL
response = requests.get(f"https://api.farsireader.com/ArianaCloudService/ReadTextGET?APIKey=4JN129JCAF20A6S&Text={greeting_str}&Speaker=Male1&Format=mp3")
mp3_data = BytesIO(response.content)

# Initialize Pygame mixer
pygame.mixer.init()

# Load the MP3 data
pygame.mixer.music.load(mp3_data)

# Play the MP3
pygame.mixer.music.play()

# Wait for the music to finish playing
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)

# Clean up
pygame.mixer.quit()
pygame.quit()