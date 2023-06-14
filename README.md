## Bunny Hop
A Python minigame following the client-server architecture
  - Technical University of Cluj-Napoca, Software Design, Final Project
  - Standalone Application
    - client app: GUI, event listening
    - server app: event handling, database management
    - bidirectional communication using TCP sockets, pickling and Python magic
  - Object Oriented design
    - OOP principles, DDD, SOA, GRASP, DRY 
    - design patterns: singleton, observer, proxy, command, state
    - layered architecture
  - Fun little game
    - help the bunny to reach the carrot in the maze
    - variable maze dimensions, randomly generated each time, guaranteed to be solvable
    - possibility to display ideal path at end of game (A* algorithm)
    - user profiles, keep track of games (mysql database), show statistics (matplotlib piechart)
    - intuitive GUI (tkinter), cute sprites for different cells (my sister's drawings)
    - three languages (English, Romanian, Hungarian, stored in JSON format)
  - dependencies which require extra attention:
    - pillow instead of PIL
    - mysql-connector-python instead plain mysql connector 
    - rest is just simple pip install

5/29/2023
