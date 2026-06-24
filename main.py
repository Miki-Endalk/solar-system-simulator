from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from OpenGL.GLUT.fonts import GLUT_BITMAP_HELVETICA_18

from constants import *
from scene import planets, selected_planet
from hud import draw_hud

def keyboard(key, x, y):
    global INITIAL_SIMULATION_SPEED, selected_planet

    if key == b'+':
        INITIAL_SIMULATION_SPEED += SPEED_STEP

    elif key == b'-':
        INITIAL_SIMULATION_SPEED -= SPEED_STEP

    elif key == b'r':
        INITIAL_SIMULATION_SPEED *= -1

    elif key == b'q':
        glutLeaveMainLoop()
    
    # Planet selection
    elif key == b'1':
        selected_planet = planets[0]  # Mercury

    elif key == b'2':
        selected_planet = planets[1]  # Venus

    elif key == b'3':
        selected_planet = planets[2]  # Earth

    elif key == b'4':
        selected_planet = planets[3]  # Mars
    
    elif key == b'5':
        selected_planet = planets[4]  # jupiter

    elif key == b'6':
        selected_planet = planets[5]  # saturn
    
    elif key == b'7':
        selected_planet = planets[6]  # uranus
    
    elif key == b'8':
        selected_planet = planets[7]  # neptune

    # Scaling
    elif key == b's' and selected_planet:
        selected_planet.scale += 0.1
        
    elif key == b'S' and selected_planet:
        selected_planet.scale = max(0.1, selected_planet.scale - 0.1)

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glLoadIdentity()

    # Move the camera
        #glTranslatef(0, 0, -30)
    gluLookAt(*CAMERA_POS, *CAMERA_TARGET, *CAMERA_UP)

    # SUN
    glColor3f(1, 1, 0)
    glutWireSphere(2, 200, 200)

    # PLANETS
    for planet in planets:
        planet.draw()

    # Draw title text
    draw_hud(selected_planet)

    glutSwapBuffers()
