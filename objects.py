from OpenGL.GL import *
from OpenGL.GLUT import *
import math

def draw_orbit(radius):
    glBegin(GL_LINE_LOOP)

    for i in range(360):
        angle = math.radians(i)

        x = radius * math.cos(angle)
        z = radius * math.sin(angle)

        glVertex3f(x, 0, z)

    glEnd()

class Planet:
    def __init__(
        self,
        orbit_radius,
        size,
        orbit_speed,
        color,
        moons=None,
        name=""
    ):
        self.orbit_radius = orbit_radius
        self.size = size
        self.orbit_speed = orbit_speed
        self.color = color
        self.name = name

        self.angle = 0
        self.scale = 1.0
        self.moons = moons if moons else []
    
    def update(self, simulation_speed):
        self.angle += self.orbit_speed * simulation_speed
        self.angle %= 360

        for moon in self.moons:
            moon.update(simulation_speed)
    
    def draw_rings(self):
        glPushMatrix()
        glRotatef(30, 1, 0, 0)  # tilt the rings slightly

        glColor3f(0.8, 0.7, 0.5)
        glBegin(GL_LINE_LOOP)
        for i in range(360):
            angle = math.radians(i)
            x = 2.2 * math.cos(angle)  # outer ring radius
            z = 1.6 * math.sin(angle)  # flatten to make it look like a disk
            glVertex3f(x, 0, z)
        glEnd()

        # Draw a second slightly smaller ring for thickness
        glBegin(GL_LINE_LOOP)
        for i in range(360):
            angle = math.radians(i)
            x = 2.0 * math.cos(angle)
            z = 1.4 * math.sin(angle)
            glVertex3f(x, 0, z)
        glEnd()

        glPopMatrix()
    
    def draw(self):
        # Orbit ring
        glColor3f(0.5, 0.5, 0.5)
        draw_orbit(self.orbit_radius)

        # Planet
        glPushMatrix()

        glRotatef(self.angle, 0, 1, 0)
        glTranslatef(self.orbit_radius, 0, 0)
        glScalef(self.scale, self.scale, self.scale)

        glColor3f(*self.color)
        glutWireSphere(self.size, 100, 200)

        for moon in self.moons:
            moon.draw()
        
        # Draw rings if this planet has them
        if self.name == "Saturn":
            self.draw_rings()

        glPopMatrix()

class Moon:
    def __init__(
        self,
        orbit_radius,
        size,
        orbit_speed,
        color
    ):
        self.orbit_radius = orbit_radius
        self.size = size
        self.orbit_speed = orbit_speed
        self.color = color

        self.angle = 0

    def update(self, simulation_speed):
        self.angle += self.orbit_speed * simulation_speed
        self.angle %= 360
    
    def draw(self):
        glPushMatrix()

        glRotatef(self.angle, 0, 1, 0)
        glTranslatef(self.orbit_radius, 0, 0)

        glColor3f(*self.color)
        glutWireSphere(self.size, 15, 15)

        glPopMatrix()
