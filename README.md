# Solar System Simulator

A real-time, interactive 3D solar system simulation built with Python and OpenGL. The simulation includes all 8 planets orbiting the sun with hierarchical moon systems, Saturn's rings, and interactive controls for speed, direction, and planet scaling.

---

## Features

- All 8 planets orbiting the sun in real-time
- Hierarchical moon system: Earth's moons orbit relative to Earth
- Saturn's rings rendered with a tilted ellipse
- Interactive planet scaling via keyboard
- Speed control: speed up, slow down, or reverse time
- On-screen HUD showing title, controls, and selected planet

---

## Project Structure

```
solar_system/
├── main.py        # Entry point: GLUT setup, display, update, keyboard
├── constants.py   # Window, camera, and simulation settings
├── objects.py     # Planet and Moon classes, draw_orbit()
├── scene.py       # Planet and moon instances
└── hud.py         # HUD rendering and draw_text()
```

---

## Requirements

- PyOpenGL
- PyOpenGL-accelerate

Install dependencies with:

```bash
pip install PyOpenGL PyOpenGL-accelerate
```

---

## How to Run

```bash
python main.py
```

---

## Controls

| Key | Action |
|-----|--------|
| `+` | Speed up simulation |
| `-` | Slow down simulation |
| `r` | Reverse simulation direction |
| `q` | Quit |
| `1` | Select Mercury |
| `2` | Select Venus |
| `3` | Select Earth |
| `4` | Select Mars |
| `5` | Select Jupiter |
| `6` | Select Saturn |
| `7` | Select Uranus |
| `8` | Select Neptune |
| `s` | Scale selected planet up |
| `S` | Scale selected planet down |

---

## Planets

| Planet | Orbit Radius | Size | Orbit Speed | Color |
|--------|-------------|------|-------------|-------|
| Mercury | 4 | 0.6 | 2.5 | Gray |
| Venus | 6 | 0.6 | 1.5 | Orange |
| Earth | 8 | 0.7 | 1.0 | Blue |
| Mars | 11 | 0.5 | 0.8 | Red |
| Jupiter | 16 | 1.5 | 0.4 | Yellow |
| Saturn | 21 | 1.3 | 0.3 | Tan |
| Uranus | 26 | 1.0 | 0.2 | Light Blue |
| Neptune | 31 | 1.0 | 0.1 | Dark Blue |

---

## Key Concepts Demonstrated

- **Hierarchical Transformations**: `glPushMatrix()` and `glPopMatrix()` chain planet and moon transforms so moons orbit relative to their host planet
- **Matrix Stacks**: transformation sequences (rotate → translate → scale) applied in the correct order for accurate orbital positioning
- **Geometric Primitives**: all objects built programmatically using `glutWireSphere()` and `GL_LINE_LOOP` loops. No external assets were used
- **Time-Based Animation**: `glutTimerFunc()` drives a consistent update loop with parametric angle equations
- **Interactive Controls**: keyboard callbacks for real-time simulation control and planet scaling via matrix multiplication

---

## Notes

- In this project, no external assets, textures, or pre-made 3D models are used — everything is built programmatically from scratch
- Earth has two moons for demonstration of the hierarchical moon system
- Planet sizes and orbit speeds are not to scale but are tuned for visual clarity