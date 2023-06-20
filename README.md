# 2048_MinMax_LocalSearch
## Simple 2048 game implementing local search and MinMax Algorithm. 

### How to run: required files
Make sure the following files are included in your directory:
• ```main.py```
• ```min_max_search.py``` 
• 2048.in.txt
• ```board.py```
*The solution is printed in real time on the console.

To run the game for both searches, simply run ```python3 main.py``` . Each search will get an empty board and add 2 random 2s to start.

### Explanation of Code:
The MinMax Search is currently set to a depth of 3. This means that the first step will be a maximum move. The code looks at what the minimum board could be for each of 4 possible moves [L, U, R, D] and again the next maximum value from each of those minimum boards. There will be 1 minimum board per move (4 total) and there for 4 maximum next states. The starting move that leads to the highest maximum end is then chosen.
