# pychess

Machine learning chess engine powered by pytorch, sitting on top of a simple board representation and legal move generator.

### GitHub PGN Database

2013 - January

Stores 121,332 games (17.8 MB)


### Local PGN Database

2015 - August

Stores 2,621,861 games (504 MB)

Data provided by the [lichess.org open database](https://database.lichess.org/), available under the [Creative Commons CC0 License](https://creativecommons.org/publicdomain/zero/1.0/).

\*NOTE\* In order for the scripts in this repository to work, the dataset must be unzipped from the .zst format

    unzstd filename.zst

# Representations

## Board

Array[64] of integers

## Move

A tuple storing the start and end of a move

## Piece Representations

    None    = 0  : 00000
    King    = 1  : 00001
    Queen   = 2  : 00010
    Bishop  = 3  : 00011
    Knight  = 4  : 00100
    Rook    = 5  : 00101
    Pawn    = 6  : 00110
    En. Ps. = 7  : 00111

    White   = 8  : 01000
    Black   = 16 : 10000

Creating a piece representation is accomplished by OR-ing two of these values together, for example a white rook would be `8 ^ 5 = 01101`

## TBD

# The Parts of Chess

What is chess made up of? Chess has
1. A Board
2. Moves
3. Pieces
4. Captures
5. 