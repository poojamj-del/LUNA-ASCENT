# LUNA-ASCENT

An educational web game where you design a simplified lunar orbiter mission and test whether your design would work.

**Live demo:** (https://luna-ascent.onrender.com/)
**Source code:** https://github.com/poojamj-del/LUNA-ASCENT

> **Note:** All numbers in this project are simplified game-balance values made for learning. They are **not** real NASA engineering specifications or validated mission calculations.


<!-- Add a screenshot of your game to the repository, name it screenshot.png, and it will appear here. -->

## About the project

Real space missions are about balancing trade-offs. A more capable instrument brings more science, but it also costs more, weighs more, needs more power and produces more data. Next Frontier lets players discover this by building a lunar mission and seeing which limits their design breaks.

This project was created for the NASA Space Apps Challenge 2026 (theme: The Next Frontier).
Challenge chosen: WRITE-YOUR-CHALLENGE-NAME-HERE

## How to play

1. Choose a **mission objective**:
   - Search for Water Ice
   - Map the Lunar Surface
   - Study Lunar Minerals
2. Choose a **rocket**: Pioneer (small), Pathfinder (medium) or Atlas (heavy).
3. Choose an **orbit**: Low, Polar or High Lunar Orbit.
4. Choose your **instruments**: High-Resolution Camera, Mineral Spectrometer, Subsurface Radar and Magnetometer.
5. Click **Simulate** to see the result.

## The four rules

Your design is checked against four constraints:

| Rule | Requirement |
|---|---|
| Mass | Spacecraft mass must not exceed the rocket's capacity |
| Budget | Total cost must stay within 120 |
| Power | Power needed must not exceed 100 |
| Communications | Data generated must fit what the chosen orbit can transmit |

## Scoring

- Each rule you pass earns 25 points.
- 0 problems: **MISSION READY**
- 1 problem: **MISSION AT RISK**
- 2 or more problems: **MISSION NOT READY**
- The result also lists exactly what needs fixing, so players can improve their design and try again.

## Game data

**Instruments**

| Instrument | Mass | Power | Cost | Data | Science |
|---|---|---|---|---|---|
| High-Resolution Camera | 40 | 20 | 12 | 25 | 25 |
| Mineral Spectrometer | 55 | 30 | 18 | 35 | 35 |
| Subsurface Radar | 70 | 40 | 22 | 45 | 40 |
| Magnetometer | 25 | 15 | 9 | 15 | 18 |

**Rockets**

| Rocket | Capacity | Cost |
|---|---|---|
| Pioneer | 180 | 25 |
| Pathfinder | 300 | 40 |
| Atlas | 500 | 60 |

**Orbits**

| Orbit | Cost | Communications | Coverage |
|---|---|---|---|
| Low Lunar Orbit | 10 | 70 | 65 |
| Polar Lunar Orbit | 15 | 60 | 95 |
| High Lunar Orbit | 8 | 85 | 55 |

## Technology

- **Python 3 and Flask**: backend game logic and calculations
- **HTML, CSS and JavaScript**: the game interface (`templates/index.html`)
- **gunicorn**: production web server
- **GitHub**: source code storage
- **Render**: online hosting

## Project structure

```
app.py                 game data and the /simulate calculation
requirements.txt       Python dependencies (Flask, gunicorn)
templates/index.html   the game interface
README.md              this file
```

## Run it on your own computer

1. Install Python 3 from https://www.python.org/downloads/
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Install the dependencies: `python -m pip install -r requirements.txt`
5. Start the app: `python app.py`
6. Open http://127.0.0.1:5000 in your browser.

## Future improvements

- Make each rule worth 20 points so the science value can add up to 20 bonus points.
- Use orbit coverage in the score, for example mapping missions needing high coverage.
- Reward instruments that match the chosen objective, such as radar for the ice objective.
- Add real NASA lunar mission examples and data as learning notes.

## References

- NASA Space Apps Challenge: https://www.spaceappschallenge.org/
- ADD-ANY-NASA-PAGES-OR-OTHER-SOURCES-YOU-USED-FOR-IDEAS-HERE

## Disclaimer

This is an educational prototype. All values are simplified for gameplay and do not represent real spacecraft design, NASA data or validated mission calculations.
