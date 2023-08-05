import random
import pygame
import cv2
import numpy as np
import time
import threading
from playsound import playsound
from pygame.locals import *
from bidi import algorithm
import os
import persian_reshaper
# Initialize
import tkinter as tk
import subprocess
if __name__ == '__main__':
    flag=False
    def run_script():
        global goflag,flag, speed, score, startTime, totalTime, timeRemain
        goflag=False
        subprocess.run(['python', 'toolbox.py'])
        goflag=True
        flag=True
        speed = 8
        score = 0
        startTime = time.time()
    def reset_game():
        global flag, speed, score, startTime, totalTime, timeRemain
        flag=True
        speed = 8
        score = 0
        startTime = time.time()
        #totalTime = totalTime

    def show_window():
        root = tk.Tk()
        root.title('Game control')
        run_button = tk.Button(root, text='New contestant', command=run_script)
        run_button.pack()
        reset_button = tk.Button(root, text='Reset Game', command=reset_game)
        reset_button.pack()
        root.mainloop()

    window_thread = threading.Thread(target=show_window)
    window_thread.start()
    
    pygame.init()

    # Create Window/Display
    width, height = 1000, 800
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Balloon Pop")

    # Initialize Clock for FPS
    fps = 30
    clock = pygame.time.Clock()

    # Webcam
    cap = cv2.VideoCapture(0)
    cap.set(3, 1280)  # width
    cap.set(4, 720)  # height
    window_x = 200
    window_y = 100
    os.environ['SDL_VIDEO_WINDOW_POS'] = f"{window_x},{window_y}"
    # Images
    imgBalloon = pygame.image.load("./Resources/BalloonRed.png").convert_alpha()
    rectBalloon = imgBalloon.get_rect()
    imgBomb = pygame.image.load("./Resources/bomb.png").convert_alpha()
    rectBomb = imgBomb.get_rect()
    rectBalloon.x, rectBalloon.y = 500, 100
    #rectBomb.x, rectBomb.y = 500, 100
    script_directory = os.path.dirname(os.path.abspath(__file__))
    logo_path = os.path.join(script_directory, "Resources", "logo.png")

    # Load the logo image (with error handling)
    try:
        logo_img = pygame.image.load(logo_path).convert_alpha()
        logo_img = pygame.transform.scale(logo_img, (300, 300))  # Adjust the logo size if needed
    except pygame.error as e:
        print("Error loading the logo image:", e)
        logo_img = None  # Set to None if loading fails
    
    # Define the font size for the website address
    font_size = 40

    # Define the path to the font file (replace 'YourFont.ttf' with the actual font file name)
    font_file_path = os.path.join(script_directory, "Resources", "The Heart Maze Demo.ttf")

    # Load the font and set it to bold
    font_website = pygame.font.Font(font_file_path, font_size)
    font_website.set_bold(True)


    # Define the colors for the website address
    website_color_yellow = (255, 255, 0)    # Yellow color
    website_color_light_blue = (173, 216, 230)  # Light blue color

    # Replace 'www.example.com' with your actual website address
    website_address = "www.Nokhbehsho.com"

    # Split the website address into two parts: "www." and the rest of the address
    website_www = "www."
    website_address_rest = website_address[4:]  # Skip the first four characters ("www.")

    # Variables
    speed = 8
    score = 0
    startTime = time.time()
    totalTime = 600

    # Detector
    points = []
    def play_sound_threaded(sound_path):
        # Create a new thread to play the sound
        sound_thread = threading.Thread(target=playsound, args=(sound_path,))

        # Set the thread as a daemon so that it terminates when the main program ends
        sound_thread.daemon = True

        # Start the thread to play the sound
        sound_thread.start()
    def mouse_callback(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            points.append((x, y))

    # Calibration
    cv2.namedWindow("Webcam Calibration")
    cv2.setMouseCallback("Webcam Calibration", mouse_callback)

    while len(points) < 4:
        _, frame = cap.read()
        frame = cv2.flip(frame, 1)
        cv2.imshow("Webcam Calibration", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cv2.destroyAllWindows()

    # Calibration transformation matrix
    src_points = np.float32(points)
    dst_points = np.float32([(0, 0), (width, 0), (width, height), (0, height)])
    M = cv2.getPerspectiveTransform(src_points, dst_points)

    def resetBalloon():
        rectBalloon.x = random.randint(100, width - 100)
        rectBalloon.y = height + 50

    def balloonBurst():
        resetBalloon()

    def isCollision(circle_x, circle_y, circle_radius, rect_x, rect_y, rect_width, rect_height):
        # Check if the circle (ball) collides with the rectangle (balloon)
        dx = circle_x - max(rect_x, min(circle_x, rect_x + rect_width))
        dy = circle_y - max(rect_y, min(circle_y, rect_y + rect_height))
        return (dx**2 + dy**2) < (circle_radius**2)

    def yellowBallCollidesBalloon(circle_x, circle_y, circle_radius, balloon_rect):
        # Check if the circle (yellow ball) collides with the rectangle (balloon)
        return balloon_rect.colliderect(circle_x - circle_radius, circle_y - circle_radius, 2 * circle_radius, 2 * circle_radius)

    def transformCoordinates(x, y):
        # Apply the calibration transformation to the (x, y) coordinates
        transformed_x = M[0, 0] * x + M[0, 1] * y + M[0, 2]
        transformed_y = M[1, 0] * x + M[1, 1] * y + M[1, 2]
        transformed_w = M[2, 0] * x + M[2, 1] * y + M[2, 2]

        transformed_x /= transformed_w
        transformed_y /= transformed_w

        return int(transformed_x), int(transformed_y)
    timeRemain=0
    # Main loop
    start = True
    goflag=False
    while start:
        if goflag:
            if rectBalloon.y<(width/10*5):
                rectBomb.x=10000
                rectBomb.y=10000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    start = False
                    pygame.quit()

            timeRemain = int(totalTime - (time.time() - startTime))
            if timeRemain < 0:
                # Game Over
                window.fill((255, 255, 255))
                font = pygame.font.Font(None, 50)
                textScore = font.render(f"Your Score: {score}", True, (50, 50, 255))
                textTime = font.render(f"Time UP", True, (50, 50, 255))
                window.blit(textScore, (450, 350))
                window.blit(textTime, (530, 275))

            else:
                success, img = cap.read()

                hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
                lower_yellow = np.array([20, 100, 100])
                upper_yellow = np.array([40, 255, 255])
                mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
                contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

                if len(contours) > 0:
                    max_contour = max(contours, key=cv2.contourArea)
                    (x, y), radius = cv2.minEnclosingCircle(max_contour)
                    x, y, radius = int(x), int(y), int(radius)

                    if radius > 5:
                        cv2.circle(img, (x, y), radius, (0, 255, 255), 2)

                        # Apply the calibration transformation to the yellow ball coordinates
                        x_transformed, y_transformed = transformCoordinates(x, y)

                        # Check if the transformed yellow ball collides with the balloon
                        if yellowBallCollidesBalloon(x_transformed, y_transformed, radius, rectBalloon):
                            
                            rectBomb.x=rectBalloon.x
                            rectBomb.y=rectBalloon.y
                            #time.sleep(0.5)
                            sound_file_path = './Resources/eyval.mp3'
                            play_sound_threaded(sound_file_path)
                            balloonBurst()

                            
                            score += 10
                            speed += 0.3
                            

                rectBalloon.y -= speed
                if rectBalloon.y < -rectBalloon.height:  # Check if the balloon is completely off the screen
                    resetBalloon()
                    speed += 0.3

                imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                calibrated_frame = cv2.warpPerspective(imgRGB, M, (width, height))
                calibrated_frame = cv2.rotate(calibrated_frame, cv2.ROTATE_90_COUNTERCLOCKWISE)

                frame = pygame.surfarray.make_surface(calibrated_frame).convert()
                frame = pygame.transform.flip(frame, True, False)
                window.blit(frame, (0, 0))
                window.blit(imgBalloon, rectBalloon)
                window.blit(imgBomb, rectBomb)
                font = pygame.font.Font('./Resources/IRAN Sans Bold.ttf', 50)
                textScore = font.render(algorithm.get_display(persian_reshaper.reshape(f'امتیاز: {score}')), True, (50, 50, 255))
                textTime = font.render(algorithm.get_display(persian_reshaper.reshape(f'زمان: {timeRemain}')), True, (50, 50, 255))
                window.blit(textScore, (35, 35))
                window.blit(textTime, (800, 35))

                if logo_img:
        
                    window.blit(logo_img, (700, 520))  # Adjust the position of the logo on the screen

                # Display the "www." part in yellow
                text_website_www = font_website.render(website_www, True, website_color_yellow)

                # Display the rest of the website address in light blue
                text_website_rest = font_website.render(website_address_rest, True, website_color_light_blue)

                # Calculate the position to center the website addresses at the bottom of the screen
                website_x_www = (width - text_website_www.get_width() - text_website_rest.get_width()) // 2
                website_y = height - 50

                # Blit the website addresses on the screen
                window.blit(text_website_www, (website_x_www, website_y))
                window.blit(text_website_rest, (website_x_www + text_website_www.get_width(), website_y))

            pygame.display.update()
            clock.tick(fps)

    cap.release()
    cv2.destroyAllWindows()
    pygame.quit()
