# PyChess

Simulates a game of chess.

## How to Use

1. Install Python from the official Python website.
2. Clone this repo.  ```git clone https://github.com/benskia/PyChess```
3. Either: (a) add execute permissions to main.sh and run it or (b) directly run main.py (located in /src/)  ```python main.py``` or ```python3 main.py```

## How to Play

The game is currently played in the terminal, and inputs are restricted to algebraic notation. For example, "Nb1c3" moves white's Knight at b1 to c3.

There isn't logic for castling nor check(mate). In the case of checks, the natural conclusion for these states is that the game is over when the King is captured.

For the time being, I will leave the game in this playable-adjacent state and revisit it after I catch up on studies.

## Example

```
❯ ./main.sh

 White's Turn

  a   b   c   d   e   f   g   h
  |   |   |   |   |   |   |   | 

 wR  wN  wB  wK  wQ  wB  wN  wR  --1

 wP  wP  wP  wP  wP  wP  wP  wP  --2

 ,.  ,.  ,.  ,.  ,.  ,.  ,.  ,.  --3

 ,.  ,.  ,.  ,.  ,.  ,.  ,.  ,.  --4

 ,.  ,.  ,.  ,.  ,.  ,.  ,.  ,.  --5

 ,.  ,.  ,.  ,.  ,.  ,.  ,.  ,.  --6

 bP  bP  bP  bP  bP  bP  bP  bP  --7

 bR  bN  bB  bK  bQ  bB  bN  bR  --8


Input command in algebraic notation (ex: Nb1c3) (Q to quit): Nb1c3

 Black's Turn

  a   b   c   d   e   f   g   h
  |   |   |   |   |   |   |   | 

 wR  ,.  wB  wK  wQ  wB  wN  wR  --1

 wP  wP  wP  wP  wP  wP  wP  wP  --2

 ,.  ,.  wN  ,.  ,.  ,.  ,.  ,.  --3

 ,.  ,.  ,.  ,.  ,.  ,.  ,.  ,.  --4

 ,.  ,.  ,.  ,.  ,.  ,.  ,.  ,.  --5

 ,.  ,.  ,.  ,.  ,.  ,.  ,.  ,.  --6

 bP  bP  bP  bP  bP  bP  bP  bP  --7

 bR  bN  bB  bK  bQ  bB  bN  bR  --8
```

Input command in algebraic notation (ex: Nb1c3) (Q to quit):

## Roadmap

* Check(mate) logic
* Castling
