# Hunt the Wumpus
## Joe Pringle, CSCI-4150, HW2

### Running instructions
python3 main.py input-file.txt

### Included Files
* board.py
* knowledgebase.py
* main.py
* player.py
* README.md
* input-1.txt

### Assumptions
* Player loses 1000 points for dying, regardless of cause.
* Knowledge base is formatted as one line per coordinate on the board, 
not one line per percept. This is easy to change if we have to (a small
modification to KnowledgeBase.write() ) but doing it this way makes it
easier for a human to read and verify.
* Knowledge base can be found in file KB.dat after running the program.

