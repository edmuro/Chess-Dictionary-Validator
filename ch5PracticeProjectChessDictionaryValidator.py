#Write a function that takesa dictionary argument and returns True
#or False depending on if the board is valid

#A valid board will have exactly one black king
#and exactly one white king.
#Each player can only have at most 16 pieces, at most 8 pawns, and all
#pieces must be on a valid space from '1a' to '8h'
#that is, a piece can't be on space '9z'.
#The piece names begin with either a 'w' or 'b' to represent
#white or black
#followed by a 'pawn', 'knight', 'bishop', 'rook', 'queen', or 'king'.
#This function should detect when a bug has resulted in an improper chess board.

#We acknowledge, using the model handed to us below, that a dictionary
#passed to the function consists of chessboard spaces as keys
#and black and white pieces as values. Thus we know that methods
#built to verify spaces will work on the keys and spaces meant to
#verify pieces will work on the values

def isValidChessBoard(someDict):
    #use {'1h':'bking','6c':'wqueen','2g':'bbishop','5h':'bqueen','3e':'wking'} as a model
    #Keep two dictionaries for reference: One is for appropriate spaces
    validSpaces = ['1a','1b','1c','1d','1e','1f','1g','1h',
                   '2a','2b','2c','2d','2e','2f','2g','2h',
                   '3a','3b','3c','3d','3e','3f','3g','3h',
                   '4a','4b','4c','4d','4e','4f','4g','4h',
                   '5a','5b','5c','5d','5e','5f','5g','5h',
                   '6a','6b','6c','6d','6e','6f','6g','6h',
                   '7a','7b','7c','7d','7e','7f','7g','7h',
                   '8a','8b','8c','8d','8e','8f','8g','8h',]
    #The other dictionary is for appropriate pieces and number of pieces
    validPieces = {'wpawn':8,'bpawn':8,'wrook':2,'brook':2,'wknight':2,
                   'bknight':2,'wbishop':2,'bbishop':2,'wqueen':1,
                   'bqueen':1,'wking':1,'bking':1}
    #Construct a dictionary to hold all pieces and their numbers
    piece = {}
    #Iterate through the dictionary passed to the function to fill piece
    #Should any inappropriate spaces or pieces be detected, a message appears
    for k, v in someDict.items():
        if k not in validSpaces:
            print('Unrecognized chessboard space')
        if v not in validPieces.keys():
            print('Unrecognized chess piece')
        piece.setdefault(v,0)
        piece[v] = piece[v]+1
    #Check piece if any kings are missing
    if 'wking' not in piece.keys() or 'bking' not in piece.keys():
        print('One or more kings is missing.')
    #Check for inappropriate numbers of each piece
    for i,j in piece.items():
        if j > 8:
            print('Inappropriate number of pawns.')
        if i == 'wrook':
            if j > 2:
                print('Inappropriate number of rooks.')
        if i == 'brook':
            if j > 2:
                print('Inappropriate number of rooks.')
        if i == 'wknight':
            if j > 2:
                print('Inappropriate number of knights.')
        if i == 'bknight':
            if j > 2:
                print('Inappropriate number of knights.')
        if i == 'wbishop':
            if j > 2:
                print('Inappropriate number of bishops.')
        if i == 'bbishop':
            if j > 2:
                print('Inappropriate number of bishops.')
        if i == 'wqueen':
            if j > 1:
                print('Inappropriate number of queens.')
        if i == 'bqueen':
            if j > 1:
                print('Inappropriate number of queens.')
        if i == 'wking':
            if j != 1:
                print('Inappropriate number of kings.')
        if i == 'bking':
            if j != 1:
                print('Inappropriate number of kings.')

#Create test dictionary and call function
exSet = {'1h':'bking','6c':'wqueen','2g':'bbishop','3h':'bbishop',
         '5h':'bqueen','3e':'wking'}
isValidChessBoard(exSet)
