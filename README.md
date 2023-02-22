## How to run and demonstrate
  - In the folder, we have 3 executable files has name *Test.py
  - To run those files and demonstrate A* algorithm in **command line**:
  ```
    python3 -u <filename>
  ```

  - To run program and demonstrate A* algorithm in **Development Server**:
  ```
    python3 -u gridworld.py
  ```

  and launch web url based on your local server's configuration:
  For example: "Running on http://127.0.0.1:5000"

  ### There are 2 types of testing to execute:
    1. For demonstrative and visualize A*: Just run like normal
    2. To gather **Time Measurement** for different types of A*:
      - Please change the code as follow:
        - In file AStar.py: Commenting line 37 (maze.print_maze())  


## NOTICE: HEAP Implemetation for tie-breaker

- MinHeap implements 2 tie-breakers: (represented by MinHeap.mode)
  - **default** mode = 1: favouring smaller g values if f values are equal
  - mode = 2: favouring larger g values if f values are equal

- In order to change heap's mode, preset MinHeap.mode = {ModeNumber} as static varible in test files.
- If not set heap's mode, it always use **default**
