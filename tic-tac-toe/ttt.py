"""A simple tic-tac-toe game."""
class TicTacToe:
    def __init__(self):
        self.board = {'1.1':'[ ]', '1.2':'[ ]', '1.3':'[ ]', '2.1':'[ ]', '2.2':'[ ]', '2.3':'[ ]', '3.1':'[ ]', '3.2':'[ ]', '3.3':'[ ]'}
    #methods
    def update(self, player):
        """Places 'o' or 'x' on the given position on the board if it's empty"""
        while True:
            if player == 'crosses':
                position = input("Crosses: ")
                if self.board[position] == '[ ]':
                    self.board[position] = '[x]'
                    break
                else:
                    print('Forbidden move! Try again!')
            if player == 'naughts':
                position = input("Naughts: ")
                if self.board[position] == '[ ]':
                    self.board[position] = '[o]'
                    break
                else:
                    print('Forbidden move! Try again!')
    
    def showboard(self):
        """Displays a board to the user."""
        print(self.board['1.1'], self.board['1.2'], self.board['1.3'])
        print(self.board['2.1'], self.board['2.2'], self.board['2.3'])
        print(self.board['3.1'], self.board['3.2'], self.board['3.3'])

    
    def check_for_winner(self, winner):
        pass
        if self.board['1.1'] == self.board['1.2'] and self.board['1.2'] == self.board['1.3'] and self.board['1.3'] != '[ ]':
            print(f'The winner is {self.board['1.1']}')
            return True

        if self.board['2.1'] == self.board['2.2'] and self.board['2.2'] == self.board['2.3'] and self.board['2.3'] != '[ ]':
            print(f'The winner is {self.board['2.1']}')
            return True

        if self.board['3.1'] == self.board['3.2'] and self.board['3.2'] == self.board['3.3'] and self.board['3.3'] != '[ ]':
            print(f'The winner is {self.board['3.1']}')
            return True

        #rows
        if self.board['1.1'] == self.board['2.1'] and self.board['2.1'] == self.board['3.1'] and self.board['3.1'] != '[ ]':
            print(f'The winner is {self.board['1.1']}')
            return True
            
        if self.board['1.2'] == self.board['2.2'] and self.board['2.2'] == self.board['3.2'] and self.board['3.2'] != '[ ]':
            print(f'The winner is {self.board['1.2']}')
            return True

        if self.board['1.3'] == self.board['2.3'] and self.board['2.3'] == self.board['3.3'] and self.board['3.3'] != '[ ]':
            print(f'The winner is {self.board['1.3']}')
            return True

        #diagonals
        if self.board['1.1'] == self.board['2.2'] and self.board['2.2'] == self.board['3.3'] and self.board['3.3'] != '[ ]':
            print(f'The winner is {self.board['1.1']}')
            return True

        if self.board['1.3'] == self.board['2.2'] and self.board['2.2'] == self.board['3.1'] and self.board['3.1'] != '[ ]':
            print(f'The winner is {self.board['1.3']}')
            return True

        else:
            return False

ttt = TicTacToe()

#title
print('TIC-TAC-TOE')
ttt.showboard()

#clock
turn = 0
winner = False

#game loop
while winner == False and turn < 10:
    turn += 1
    if turn % 2 == 0:
        ttt.update('naughts')
    else:
        ttt.update('crosses')
    ttt.showboard()
    winner = ttt.check_for_winner(winner)

if winner == False:
    print('Tie!')
