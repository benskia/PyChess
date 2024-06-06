def validate_command(command: str) -> bool:
    # Commands are in a verbose form of algebraic notation (ex: Nb1c3)
    # piece id --- origin file and rank --- destination file and rank
    print(f"Validating command: '{command}' ...")
    return all(
        [
            validate_length(command),
            validate_piece_id(command[0]),
            validate_file(command[1]),
            validate_rank(command[2]),
            validate_file(command[3]),
            validate_rank(command[4]),
        ]
    )


def validate_length(command: str) -> bool:
    valid_command_length: int = 5
    if not len(command) is valid_command_length:
        print(f"'{command}' is an invalid length. Expected 5 characters. (ex: Nb1c3)")
        return False
    return True


def validate_piece_id(piece_id: str) -> bool:
    piece_ids: str = "PRNBKQ"
    if not piece_id in piece_ids:
        print(f"'{piece_id}' is an invalid piece ID. Valid IDs are '{piece_ids}'")
        return False
    return True


def validate_file(file: str) -> bool:
    files: str = "abcdefgh"
    if not file in files:
        print(f"'{file}' is an invalid file. Valid files are '{files}'")
        return False
    return True


def validate_rank(rank: str) -> bool:
    ranks: str = "12345678"
    if not rank in ranks:
        print(f"'{rank}' is an invalid rank. Valid ranks are '{ranks}'")
        return False
    return True
