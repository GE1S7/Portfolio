# Portfolio
Welcome to my portfolio! This repository showcases a variety of projects that I have completed to demonstrate my skills in Python and SQL. Each project was planned and executed by me from scratch, without following step-by-step tutorials. I hope these projects highlight my ability to identify problems, research solutions, and implement effective code. Feel free to explore the code and results for each project. If you have any questions or feedback, please don't hesitate to reach out.

## Methodological remark
For all projects, I followed a structured approach:
- Planning: Outlined the requirements and how to achieve them on paper.
- Identifying Knowledge Gaps: Identified areas where I needed more information or skills.
- Research: Sought out resources to fill in the gaps.
- Implementation: Wrote the code based on my plan and research.
- Iteration: Went back to planning if something was not right and refined the approach.


# Python Projects
## News webscraping script
This script searches Google News for articles mentioning a specified keyword and sends the links with titles to your email inbox. It checks a text file to avoid sending duplicate articles. This implementation showcases web scraping, email integration, and file handling.
### Features
- **Web Scraping with `pygooglenews`:** Searches Google News for articles containing the keyword within the last 30 days.
- **Email Integration with `smtplib`:** Sends the collected articles to a specified email address.
- **Persistence with File Handling:** Avoids duplicate emails by checking a text file containing previously sent articles.
## Pong Clone using Pygame
This project is a clone of the classic Pong game implemented using Pygame. The game features a simple graphical interface, basic physics for ball movement and collisions, and a scoring system. The code demonstrates my ability to work with graphical libraries, implement game logic, and handle user input.
### Features
- **Graphical Interface:** Utilizes Pygame to create a visual representation of the game, including paddles, ball, and scores.
- **Game Physics:** Implements ball movement with varying bounce angles depending on the paddle hit location.
- **User Input:** Supports player control through keyboard inputs.
- **Scoring System:** Tracks and displays player scores, with a win condition based on reaching 10 points.
##  Text-based Adventure Game Engine (in progress)
- This project is a rudimentary text-based game engine, showcasing my ability to work with various data structures and implement game logic for text-based adventure games. It involves moving between nodes/locations, picking up items, checking inventory, and interacting with objects. This project demands significant tinkering with different data structures and objects that refer to other objects.
### Features:
- **Game State Management:** Efficiently handles the game state, including the player's inventory, current location, and game progress.
- **Node-based Navigation:** Implements a system for moving between locations (nodes) in the game world.
- **Item Interaction:** Allows players to pick up and use items, adding depth and interactivity to the game.
- **Modular Design:** The engine is designed to be extended with new locations, items, and interactions, making it a flexible framework for creating various text-based games.

## Tic-Tac-Toe text based game
This project is a simple text-based implementation of the classic Tic-Tac-Toe game. It showcases my ability to work with basic Python constructs, handle user input, and implement game logic, particularly the logic for determining the winner in a game.
### Features:
- **Interactive Gameplay:** Allows two players to take turns and input their moves.
- **Board Representation:** Uses a dictionary to represent the game board, making it easy to update and display.
- **Winner Detection:** Implements logic to check for winning conditions after each move.
- **User-Friendly Messages:** Provides feedback for invalid moves and announces the winner or a tie game.


## Number Guessing Game between two algorithms
A simple number guessing game where one function tries to guess the (usually ridiculously high) numbers that the other chooses.
### Features
- working with random number generation using random library
- implementing guessing logic
- making two algorithms interact as players


# SQL Projects
## E-commerce Data Analysis (in progress)
This project showcases a comprehensive analysis of e-commerce sales data using SQL. The primary focus is on understanding revenue trends, identifying top-selling categories, and analyzing monthly revenue distribution across various product categories as well as performing basket analysis. The data is sourced from CSV files, which are imported into a PostgreSQL database for detailed analysis. 
### Features
- Data import and cleaning
- Exploratory data analysis
- Trends and performance analysis
- Basket analysis

## Analysis of my touch typing scores from monkeytype.com (in progress)
As for now I've cleaned, formatted the data and imported the data to my postgres db. I'm still planning what to do with this one.
