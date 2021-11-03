import random

class Buscaminas:
    
    def __init__(self, rows, cols, bombs):
        self.rows = rows
        self.cols = cols
        self.bombs = bombs
        self.board = None
        self.show = None
        self.generate_board(rows,cols,bombs)

    def generate_board(self, rows, cols, bombs):                     #* Genera la tabla

        self.board = [[' ' for t in range(cols)] for l in range(rows)]
        self.show = [[' ' for t in range(cols)] for l in range(rows)]
        
        for i in range(self.bombs):                                     #* Agrega las bombas
            while True:
                fila = random.randrange(0, self.rows)
                columna = random.randrange(0, self.cols)
                if self.board[fila][columna] != 'B':
                    self.board[fila][columna] = 'B'
                    break
        
        for l in range(rows):
            for t in range(cols):
                if self.board[l][t] != 'B':
                    re = [] 
                    for sa in (-1,0,1):
                        for sb in (-1,0,1):
                            try:
                                if not ((l +  sa < 0 or t + sb < 0) or (sa == 0 and sb == 0)):
                                    re.append(self.board[l + sa][t + sb])
                            except Exception:
                                continue
                        if re.count('B') != 0:
                            self.board[l][t] = str(re.count('B')) 
                        else:
                            ' '

    def show_board(self):                                              #* Muestra la tabla

        for r in range(self.rows):
            print('{}    {}'.format(self.board[r], self.show[r]))
    
    def question(self, movs):                                         #* Realiza las preguntas
        
        self.moves = movs
        movs = ['flag','uncover']

        while True:
            mov = input('¿Qué movimiento quiere hacer? \n1.Flag 2.Uncover\n')
            if mov.lower() not in ('flag', 'uncover'):
                raise Exception()
            else:
                break
        
        while True:
            row = input('\nIngrese la fila deseada: ')
            if str(row) not in [str(l) for l in range(self.rows)]:
                raise Exception()
            else:
                row = int(row)
                break
        
        while True:
            col = input('\nIngrese la columna deseada: ')
            if str(col) not in [str(l) for l in range(self.cols)]:
                raise Exception()
            else:
                col = int(col)
                break
        
        return [mov, row, col]
    
    def play(self, mov, row, col):

        if mov == 'flag':
            self.show[row][col] = 'F'
        else:
            self.show[row][col] = self.board[row][col]
        
    def lose(self):                                         #* Condición de perdida

        for l in self.show:
            if 'B' in l:
                return True
        return False
     
    def win(self):                                           #* Condición de victoria

        wc = []
        for l in range(self.rows):
            self.board.append([])
        for t in range(self.cols):
            self.board[l].append('-')

        for l in range(self.rows):
            for t in range(self.cols):
                if self.show == wc:
                    return False
                elif self.board[l][t] == ' ':
                    continue
                if self.board[l][t].isdigit() and self.show[l][t] == 'F':
                    return False
                if self.board[l][t] == 'B' and self.show[l][t] != 'F':
                    return False
        return True