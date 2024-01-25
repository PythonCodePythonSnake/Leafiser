import pygame
import os
import cv2
import subprocess
from Planease import all_cures
from tensorflow.keras.models import load_model
from tensorflow_hub import KerasLayer
from shutil import rmtree
import numpy as np
os.system("cls")
pygame.init()

   
def check(pos: tuple, square: tuple):
    if pos[0] <= square[0] or pos [0] >= square[2]: return False
    if pos[1] <= square[1] or pos [1] >= square[3]: return False
    return True

def blit_text(text: str, pos: tuple, size: int, center: bool):
        font = pygame.font.SysFont(["outfit", 'timesnewroman', pygame.font.get_default_font()],  size)
        text_object = font.render(text, True, WHITE)
        text_rect = text_object.get_rect()
        if center: text_rect.center = pos
        else: text_rect.topleft = pos
        screen.blit(text_object, text_rect)
        return text_rect

def set_bg(index: int):
    screen.blit(IMAGES[index], (0,0))
    pygame.display.update()

def open_window():
    set_bg(0)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:                       #Check for the QUIT event
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                return

def main_window():
    set_bg(1)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if check(event.pos, (72, 59, 213, 147)): add_image()
                elif check(event.pos, (388, 59, 529, 147)): test()
                elif check(event.pos, (72, 252, 213, 340)): show_images()
                elif check(event.pos, (388, 252, 529, 340)): subprocess.run([FILEBROWSER_PATH, os.path.abspath("Planease/data/Results")])
                elif check(event.pos, (72, 445, 213, 533)): show_diseases()
                elif check(event.pos, (388, 446, 529, 534)):
                    pygame.quit()
                    exit()

def add_image():
    webcam = cv2.VideoCapture(0)
    set_bg(2)
    while True:
        try:
            read, frame = webcam.read()
            if read == False: 
                set_bg(9)
                os.system("cls")
                back_rect = pygame.Rect(404, 404, 187, 187)
                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN and back_rect.collidepoint(event.pos):
                            set_bg(1)
                            pygame.display.update()
                            return
            cv2.imshow("Get leaf", frame)
            key = cv2.waitKey(1)
            if key == ord('s'):
                file_name =  "Planease/data/Images/image (" + str(len(os.listdir("Planease/data/Images"))+1)+").jpg"
                frame = cv2.resize(frame, (256, 256))
                cv2.imwrite(filename=file_name, img=frame)
                webcam.release()
                cv2.destroyAllWindows()
                set_bg(3)
                pygame.time.delay(2000)
                set_bg(1)
                break
            
            elif key == ord('b'):
                webcam.release()
                cv2.destroyAllWindows()
                set_bg(1)
                break
            
        except(KeyboardInterrupt):
            webcam.release()
            cv2.destroyAllWindows()
            set_bg(1)
            break

def test():
    if len(os.listdir(os.path.abspath("Planease/data/Images"))) == 0: 
        set_bg(6)
        back_rect = pygame.Rect(404, 404, 187, 187)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and back_rect.collidepoint(event.pos):
                    set_bg(1)
                    pygame.display.update()
                    return
    set_bg(4)
    model = load_model(os.path.abspath("Planease/model"), custom_objects={'KerasLayer' : KerasLayer})
    all_diseases = all_cures.classes
    
    #Arrays to contain test images and there names
    imgs = []
    img_names = []

    #Clear preveious output directory and make new
    try: os.mkdir(os.path.abspath("Planease/data/Results"))
    except FileExistsError:
        rmtree(os.path.abspath("Planease/data/Results"))
        os.mkdir(os.path.abspath("Planease/data/Results"))

    #Set values of images and image names
    for file in os.listdir(os.path.abspath("Planease/data/Images")):
        imgs.append(cv2.cvtColor(cv2.imread(os.path.abspath("Planease/data/Images/" + file)), cv2.COLOR_BGR2RGB))
        img_names.append(file.split(".")[0])
    imgs = np.array(imgs)
    
    #Allow model to perform prediction
    result = model.predict(imgs)

    #Loop thrrough the result and make new files for disease and cure or every image with same name
    for i in range(len(result)):
        result_file = open(os.path.abspath("Planease/data/Results/"+img_names[i]+".txt"), "w")
        disease = all_diseases[np.argmax(result[i])]
        result_file.write("Disease: "+disease+"\n")
        if "healthy" not in disease:
            result_file.write("To cure "+disease+"- \n")
            result_file.write(all_cures.get_cure(disease))
        result_file.write("\n")
        result_file.close()
    os.system("cls")
    set_bg(5)
    back_rect = pygame.Rect(404, 404, 187, 187)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and back_rect.collidepoint(event.pos):
                set_bg(1)
                return

def show_images():
    def blit_frame(frame_no):
        set_bg(8)
        x = [10, 207, 404]
        for i in range(7):
            try: curr_file = img_files[frame_no*7+i]
            except IndexError: return
            file_pos = (x[i%3], x[i//3])
            image = pygame.transform.scale(pygame.image.load(os.path.abspath("Planease/data/Images/" + curr_file)), (187, 187))
            screen.blit(image, file_pos)
    
    img_files = sorted(os.listdir(os.path.abspath("Planease/data/Images")))
    if len(img_files) == 0:
        set_bg(6)
        back_rect = pygame.Rect(404, 404, 187, 187)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and back_rect.collidepoint(event.pos):
                    set_bg(1)
                    return
        
    elif len(img_files) < 9:
        set_bg(7)
        back_rect = pygame.Rect(404, 404, 187, 187)
        x = [10, 207, 404]
        for i in range(len(img_files)):
            file_pos = (x[i%3], x[i//3])
            image = pygame.transform.scale(pygame.image.load(os.path.abspath("Planease/data/Images/"+img_files[i])), (187, 187))
            screen.blit(image, file_pos)
        
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and back_rect.collidepoint(event.pos):
                    set_bg(1)
                    pygame.display.update()
                    return
    
    else:
        back_rect, next_rect = pygame.Rect(207, 404, 187, 187), pygame.Rect(404, 404, 187, 187)
        frame_no = 0
        set_bg(8)
        blit_frame(frame_no)
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if back_rect.collidepoint(event.pos) and frame_no != 0:
                        frame_no -= 1
                        blit_frame(frame_no)
                        pygame.display.update()
                    elif back_rect.collidepoint(event.pos) and frame_no == 0:
                        set_bg(1)
                        return
                    elif next_rect.collidepoint(event.pos) and frame_no < len(img_files)//7:
                        frame_no += 1
                        blit_frame(frame_no)
                        pygame.display.update()

def show_diseases():
    set_bg(10)
    back_rect = pygame.Rect(404, 404, 187, 187)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and back_rect.collidepoint(event.pos):
                set_bg(1)
                return

if __name__ == "__main__":
       
    try: os.mkdir(os.path.abspath("Planease/data/Images"))
    except FileExistsError:
        rmtree(os.path.abspath("Planease/data/Images"))
        os.mkdir(os.path.abspath("Planease/data/Images"))
    
    FILEBROWSER_PATH = os.path.join(os.getenv('WINDIR'), 'explorer.exe')
    WIDTH = HEIGHT = 600
    WHITE = (255, 255, 255)
    IMAGES = []
    for i in range(1, 12):
        IMAGES.append(pygame.transform.scale(pygame.image.load(os.path.abspath("Planease/images_for_gui/Slide"+str(i)+".jpg")), (WIDTH, HEIGHT)))
        
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Vrksarognirnay")

    while True:
        open_window()
        main_window()