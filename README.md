# PyChess

Simulates a game of chess.

## How to Play

The game is currently played in the terminal, and inputs are restricted to
algebraic notation. For example, "Nb1c3" moves white's Knight at b1 to c3.

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

* Pawns can move two spaces as first movement.
* Pawns can capture on diagonal and only on diagonal.
* Check(mate) logic
* Castling
