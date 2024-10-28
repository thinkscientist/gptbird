# GPT Bird 🐦

Welcome to **GPT Bird**, a web-based game inspired by the classic Flappy Bird. Navigate the bird through the gaps between pipes without colliding. This project showcases HTML5 Canvas animations, sprite sheet handling, and JavaScript game logic.

## Table of Contents

- [Demo](#demo)
- [Features](#features)
- [Installation](#installation)
- [How to Play](#how-to-play)
- [Game Mechanics](#game-mechanics)
  - [Controls](#controls)
  - [Scoring](#scoring)
  - [Collision Detection](#collision-detection)
  - [Difficulty](#difficulty)
- [Assets](#assets)
  - [Images](#images)
  - [Sounds](#sounds)
- [Customization](#customization)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Demo

[Play GPT Bird Online]() <!-- Replace with the link to your live demo if available -->

## Features

- Responsive design that adapts to different screen sizes and devices.
- Smooth sprite animations for the bird and interactive start screen.
- Dynamic obstacle generation with varying pipe positions.
- Accurate collision detection using circle-rectangle collision algorithms.
- Sound effects for flapping, scoring, and background music.
- Simple and intuitive controls for desktop and mobile devices.

## Installation

To run the game locally, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/gpt-bird.git
   ```

2. Navigate to the project directory:
   ```
   cd gpt-bird
   ```

3. Open the `index.html` file in your preferred web browser.

## How to Play

1. Click the "Start" button or press the spacebar to begin the game.
2. Use the spacebar (on desktop) or tap the screen (on mobile) to make the bird flap and gain altitude.
3. Navigate the bird through the gaps between the pipes.
4. Avoid colliding with the pipes or the ground.
5. Try to achieve the highest score possible!

## Game Mechanics

### Controls

- Desktop: Press the spacebar to make the bird flap.
- Mobile: Tap anywhere on the screen to make the bird flap.

### Scoring

- Each successfully passed set of pipes awards one point.
- The current score is displayed at the top of the screen during gameplay.
- The high score is saved locally and displayed on the start screen.

### Collision Detection

The game uses precise collision detection:
- Bird-pipe collisions are checked using circle-rectangle collision algorithms.
- Ground collisions are detected when the bird's position exceeds the ground level.

### Difficulty

The game's difficulty increases as you progress:
- Pipe gaps become narrower.
- The speed of the pipes increases slightly.

## Assets

### Images

- `sprite.png`: Contains all game graphics, including the bird, pipes, and background elements.

### Sounds

- `flap.wav`: Played when the bird flaps its wings.
- `score.wav`: Played when passing through pipes successfully.
- `hit.wav`: Played upon collision with pipes or the ground.
- `die.wav`: Played when the game ends.
- `swoosh.wav`: Played during certain game state transitions.

## Customization

You can customize various aspects of the game by modifying the following files:

- `index.html`: Update the canvas size or add additional HTML elements.
- `style.css`: Modify the game's appearance and layout.
- `game.js`: Adjust game mechanics, speeds, or add new features.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Inspired by the original Flappy Bird game created by Dong Nguyen.
- Bird sprite and pipe designs inspired by the original Flappy Bird assets.
- Sound effects obtained from [freesound.org](https://freesound.org/) (specific attributions in the code comments).
