from chess import Game

# TODO: Line of sight check currently goes out of bounds in some cases.


def main() -> None:
    g = Game()
    g.run_game()


if __name__ == "__main__":
    main()
