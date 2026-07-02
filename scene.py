from objects import Planet, Moon

moon1 = Moon(
    orbit_radius=2,
    size=0.2,
    orbit_speed=2,
    color=(0.8, 0.8, 0.8)
)

moon2 = Moon(
    orbit_radius=1,
    size=0.2,
    orbit_speed=1,
    color=(0, 1, 0)
)

mercury = Planet(
    orbit_radius=4,
    size=0.6,
    orbit_speed=2.5,
    color=(0.7, 0.7, 0.7),
    name="Mercury"
)

venus = Planet(
    orbit_radius=6,
    size=0.6,
    orbit_speed=1.5,
    color=(1.0, 0.6, 0.2),
    name="Venus"
)

earth = Planet(
    orbit_radius=8,
    size=0.7,
    orbit_speed=1,
    color=(0, 0, 1),
    moons=[moon1, moon2],
    name="Earth"
)

mars = Planet(
    orbit_radius=11,
    size=0.5,
    orbit_speed=0.8,
    color=(1.0, 0.2, 0.2),
    name="Mars"
)

jupiter = Planet(
    orbit_radius=16,
    size=1.5,
    orbit_speed=0.4,
    color=(1.0, 0.8, 0.2),
    name="Jupiter"
)

saturn = Planet(
    orbit_radius=21,
    size=1.3,
    orbit_speed=0.3,
    color=(0.9, 0.8, 0.6),
    name="Saturn"
)

uranus = Planet(
    orbit_radius=26,
    size=1.0,
    orbit_speed=0.2,
    color=(0.4, 0.7, 1.0),
    name="Uranus"
)

neptune = Planet(
    orbit_radius=31,
    size=1.0,
    orbit_speed=0.1,
    color=(0.2, 0.4, 1.0),
    name="Neptune"
)

planets = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]
selected_planet = None
