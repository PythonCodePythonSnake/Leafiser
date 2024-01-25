import pygame
import os
import cv2
import subprocess
os.system("cls")
pygame.init()
FILEBROWSER_PATH = os.path.join(str(os.getenv('WINDIR')), 'explorer.exe')
WIDTH = HEIGHT = 600
RED, GREEN, BLUE, YELLOW = (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)
IMAGES = []
for i in range(1, 10):
    IMAGES.append(pygame.transform.scale(pygame.image.load(os.path.join(os.getcwd(), "GUI Images", str(i)+".jpg")), (WIDTH, HEIGHT)))

def blit_text(screen, text, color, pos, size):
    font = pygame.font.SysFont('timesnewroman',  size)
    text_object = font.render(text, True, color)
    text_rect = text_object.get_rect()
    text_rect.center = pos
    screen.blit(text_object, text_rect)

def check(pos, square):
    if pos[0] <= square[0] or pos [0] >= square[2]: return False
    if pos[1] <= square[1] or pos [1] >= square[3]: return False
    return True

def open(screen):
    pygame.draw.rect(screen, BLUE, pygame.Rect(0, 0, 600, 600))
    pygame.draw.rect(screen, YELLOW, pygame.Rect(10, 10, 580, 580))
    blit_text(screen, "PIXEL PUZZLERS", RED, (300, 250), 48)
    blit_text(screen, "CLICK ANYWHERE TO START", RED, (300, 350), 30)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:                       #Check for the QUIT event
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.update()

def main(screen):    
    screen.blit(IMAGES[1], (0, 0))
    pygame.draw.rect(screen, RED, pygame.Rect(380, 197, 141, 62))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:                       #Check for the QUIT event
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN :
                if check(event.pos, (80, 52, 221, 114)):
                    add_image()
                elif check(event.pos, (380, 52, 521, 114)):
                    show_images(screen)
                elif check(event.pos, (380, 197, 521, 259)):
                    subprocess.run([FILEBROWSER_PATH, os.path.join(os.getcwd(), "testing", "Results")])
                elif check(event.pos, (380, 342, 521, 404)):
                    subprocess.run([FILEBROWSER_PATH, os.path.join(os.getcwd(), "testing", "Results")])
                elif check(event.pos, (80, 487, 221, 549)):
                    return
                elif check(event.pos, (380, 487, 521, 549)):
                    pygame.quit()
                    exit()
        pygame.display.update()

def add_image():
    screen.blit(IMAGES[2], (0, 0))
    pygame.display.update()
    webcam = cv2.VideoCapture(0)
    while True:
        try:
            _, frame = webcam.read()
            cv2.imshow("Get leaf", frame)
            key = cv2.waitKey(1)
            if key == ord('s'):
                file_name =  "testing/Images/image (" + str(len(os.listdir("testing/Images"))+1)+").jpg"
                frame = cv2.resize(frame, (256, 256))
                cv2.imwrite(filename=file_name, img=frame)
                webcam.release()
                cv2.destroyAllWindows()
                break
            
            elif key == ord('q'):
                webcam.release()
                cv2.destroyAllWindows()
                break
            
        except(KeyboardInterrupt):
            webcam.release()
            cv2.destroyAllWindows()
            break
    screen.blit(IMAGES[3], (0, 0))
    pygame.display.update()
    pygame.time.delay(2000)
    screen.blit(IMAGES[1], (0, 0))

def show_images(screen):
    screen.blit(IMAGES[4], (0, 0))
    
    img_files = sorted(os.listdir(os.path.join(os.getcwd(), "testing", "Images")))
    
    if len(img_files) == 0:
        font = pygame.font.SysFont('timesnewroman',  48)
        text = font.render("No Images are saved!", True, RED)
        text_rect = text.get_rect()
        text_rect.center = (300, 300)
        screen.blit(text, text_rect)
        pygame.display.update()
        
    elif len(img_files) < 9:
        pygame.draw.rect(screen, GREEN, pygame.Rect(404, 404, 187, 187))
        font = pygame.font.SysFont('timesnewroman',  30)
        text = font.render('Back', True, RED)
        text_rect = text.get_rect()
        text_rect.center = (497, 497)
        screen.blit(text, text_rect)
        
        x = [10, 207, 404]
        for i in range(len(img_files)):
            file_pos = (x[i%3], x[i//3])
            image = pygame.transform.scale(pygame.image.load(os.path.join(os.getcwd(), "testing", "Images", img_files[i])), (187, 187))
            screen.blit(image, file_pos)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and check(event.pos, (404, 404, 591, 591)):
                break
    
    else:
        frame_no = 0
        pygame.draw.rect(screen, GREEN, pygame.Rect(404, 404, 187, 187))
        pygame.draw.rect(screen, GREEN, pygame.Rect(207, 404, 187, 187))
        font = pygame.font.SysFont('timesnewroman',  30)
        back_text = font.render('Back', True, RED)
        back_text_rect = back_text.get_rect()
        back_text_rect.center = (300, 497)
        screen.blit(back_text, back_text_rect)
        next_text = font.render('Next', True, RED)
        next_text_rect = next_text.get_rect()
        next_text_rect.center = (497, 497)
        screen.blit(next_text, next_text_rect)
        x = [10, 207, 404]
        for i in range(7):
            file_pos = (x[i%3], x[i//3])
            image = pygame.transform.scale(pygame.image.load(os.path.join(os.getcwd(), "testing", "Images", img_files[frame_no*7+i])), (187, 187))
            screen.blit(image, file_pos)
        pygame.display.update()
    screen.blit(IMAGES[1], (0, 0))
    pygame.display.update()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Plant Health')
while True:
    open(screen)
    main(screen)
