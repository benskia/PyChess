from chess import Game


def main() -> None:
    g = Game()
    print(g.board)
    g.parse_command("ooWeee")
    g.parse_command("Wowwo")
    g.parse_command("Nb1e3")


if __name__ == "__main__":
    main()
