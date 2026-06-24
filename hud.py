from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from OpenGL.GLUT.fonts import GLUT_BITMAP_HELVETICA_18

from constants import WINDOW_WIDTH, WINDOW_HEIGHT

def draw_text(x, y, text):
    glDisable(GL_DEPTH_TEST)

    # Save current matrix state
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()

    # Switch to 2D orthographic projection matching window size
    gluOrtho2D(0, 1000, 0, 700)

    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()

    # Draw the text at pixel coordinates
    glColor3f(1, 1, 1)
    glRasterPos2f(x, y)
    for ch in text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(ch))

    # Restore previous matrix state
    glPopMatrix()
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)

    glEnable(GL_DEPTH_TEST)

def draw_hud(selected_planet):
    # Title
    draw_text(10, WINDOW_HEIGHT - 20, "Solar System")

    # Selected planet
    if selected_planet:
        draw_text(10, WINDOW_HEIGHT - 45, f"Selected: {selected_planet.name}")

    # Controls
    draw_text(10, 60, "1-8: Select Planet  |  s/S: Scale Up/Down")
    draw_text(10, 40, "+/-: Speed Up/Down  |  r: Reverse")
    draw_text(10, 20, "q: Quit")