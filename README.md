Capture the King - Terminal Chess Game

Welcome to Capture the King, a terminal-based chess game built with Python. This project is designed for chess enthusiasts who enjoy playing and developing classic games in a simple, text-based environment. Capture the King focuses on the ultimate goal of chess—capturing the opponent's king—providing a streamlined and engaging experience.

Features
•	Text-Based Interface: Enjoy the nostalgia and simplicity of playing chess directly in your terminal.
•	Interactive Gameplay: Move pieces with intuitive commands and receive real-time feedback if the move is invalid.
•	Customizable Board: Easily modify the board size and initial piece placement to create various game scenarios.
•	Rule Enforcement: All standard chess rules are enforced, including legal moves except check, checkmate, and stalemate.
•	Undo and Redo Moves: Navigate through the game history to correct mistakes or explore different strategies.
•	Save and Load Games: Save your progress at any point and resume the game later from where you left off.

Project Structure
The project is organized into several modules, each responsible for different aspects of the game. Note that this project does not contain a game.py module. The main components include which is used in the form of same name or the other:
•	board.py: Manages the chessboard representation, including piece placement and board state.
•	pieces.py: Defines the different chess pieces, their movements, and interactions.
•	player.py: Handles player interactions, including move input and validation.
•	game_manager.py: Oversees the game flow, enforcing rules, and managing turns.
•	utils.py: Contains utility functions for various tasks such as board rendering and move parsing.

Installation
To get started with Capture the King, follow these steps:
1.	Clone the repository:
2.	Install dependencies: Ensure you have Python 3.x installed. Then, install any required dependencies:
3.	Run the game: Start the game by running the main script:
Copy code
python main.py

How to Play
1.	Start a new game: Follow the on-screen instructions to set up a new game.
2.	Move pieces: Enter your moves in algebraic notation (e.g., e2 e4 to move a piece from e2 to e4).
3.	Capture the king: Strategically move your pieces to kill your opponent's king and win the game.
4.	Save/Load: Use commands to save the current game state or load a previously saved game.
   
Contributing
We welcome contributions from the community! If you'd like to contribute, please follow these steps:
1.	Fork the repository.
2.	Create a new branch for your feature or bugfix.
3.	Commit your changes and push your branch.
4.	Submit a pull request with a detailed description of your changes.

