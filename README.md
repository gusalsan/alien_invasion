# Alien Invasion

**Alien Invasion** is a 2D arcade-style space shooter game inspired by the classic *Space Invaders*.  
Developed as a hands-on project from Eric Matthes' book *Python Crash Course* (3rd edition), this is a complete implementation featuring smooth gameplay, scoring, levels, and responsive controls.

You control a ship at the bottom of the screen, moving left/right with arrow keys and firing bullets with the spacebar to defend against waves of descending aliens.

## Features

- Player ship movement (left/right) and continuous firing  
- Alien fleet that moves side-to-side and drops down gradually  
- Bullet collision detection with aliens  
- Progressive difficulty: faster aliens and more points per level  
- Scoring system with high-score tracking  
- Multiple lives (3 by default)  
- Game over screen when all lives are lost  
- Clean, modular object-oriented code (classes for Ship, Alien, Bullet, GameStats, Settings, etc.)

## Technologies Used

- Python 3.8+  
- Pygame library (for graphics, input handling, sprites, sound, and collision detection)

## How to Run the Game

1. **Clone the repository**  
   ```bash
   git clone https://github.com/gusalsan/alien_invasion.git
   cd alien_invasion

2. Create and activate a virtual environment
   python -m venv venv
    # Windows:
    venv\Scripts\activate
    # macOS/Linux:
    source venv/bin/activate
   
4. Install Pygame
   pip install pygame
   
6. Run the game
   python alien_invasion.py
