import pygame
class Game:
    def __init__(self):
        self.move = 0
        self.turn = ['w','b']


class Pieces:
    def __init__(self,coord,id,path):
        self.horizontal = [0,1,2,3,4,5,6,7]
        self.vertical = [7,6,5,4,3,2,1,0]

        self.coord = coord
        self.id = id
        self.selected = False
        self.pic = path

        self.img = pygame.image.load(path)
        self.width = self.img.get_width()
        self.height = self.img.get_height()

        self.img = pygame.transform.scale(self.img, (2 * self.width, 2 * self.height))
        self.width *= 2
        self.height *= 2

        self.movable_coord = []

        self.alive = True

        self.move_color = (179,79,255)
    def play(self,screen):
        if self.alive:
            self.pos = self.toPos(self.coord)
            pygame.Surface.blit(screen,self.img,self.pos)

            if self.selected:
                self.show_move(screen)

    def toPos(self,coord,pieces = True):
        x = self.horizontal[coord[0]-1]*44 + 44/2 - self.width/2*pieces
        y = self.vertical[coord[1]-1]*44 + 44/2 - self.height/2*pieces

        return (x + board_offset + 4, y + board_offset + 4)
    def destroy(self):
        self.alive = False
    def ocupided(self,coord):
        if board_arr[coord[0]-1][coord[1]-1] == 1:
            return True
        return False

class Pawn(Pieces):
    def show_move(self,screen):
        self.movable_coord = []
        if self.id[0] == 'b':
            coord = (self.coord[0], self.coord[1] - 1)
            if int(coord[1]) >= 1:
                if self.ocupided(coord):
                    self.movable_coord = []
                    return
                self.movable_coord.append(coord)
                coord = (self.coord[0], self.coord[1] - 2)
                if self.coord[1] == 7:
                    self.movable_coord.append(coord)


        elif self.id[0] == 'w':
            coord = (self.coord[0], self.coord[1] + 1)
            if int(coord[1]) <= 8:
                if self.ocupided(coord):
                    self.movable_coord = []
                    return
                self.movable_coord.append(coord)
                coord = (self.coord[0], self.coord[1] + 2)
                if self.coord[1] == 2:
                    self.movable_coord.append(coord)

        for coord in self.movable_coord:
            pygame.draw.circle(screen, self.move_color, self.toPos(coord,False), 8)
class King(Pieces):
    def show_move(self,screen):
        '''
        pos1 pos2 pos3
        pos8   k  pos4
        pos7 pos6 pos5
        '''
        coord1 = (self.coord[0] - 1, self.coord[1] - 1)
        coord2 = (self.coord[0]    , self.coord[1] - 1)
        coord3 = (self.coord[0] + 1, self.coord[1] - 1)
        coord4 = (self.coord[0] + 1, self.coord[1])
        coord5 = (self.coord[0] + 1, self.coord[1] + 1)
        coord6 = (self.coord[0]    , self.coord[1] + 1)
        coord7 = (self.coord[0] - 1, self.coord[1] + 1)
        coord8 = (self.coord[0] - 1, self.coord[1])

        self.coord_list = [coord1, coord2, coord3, coord4, coord5, coord6, coord7, coord8]
        self.movable_coord = []
        for coord in self.coord_list:
            if not (coord[0] < 1 or coord[0] > 8 or coord[1] < 1 or coord[1] > 8) and not self.ocupided(coord):
                pygame.draw.circle(screen, self.move_color, self.toPos(coord, False), 8)
                self.movable_coord.append(coord)
class Knight(Pieces):
    def show_move(self,screen):
        '''
            pos1 pos2
        pos8          pos3
              knigth
        pos7          pos4
            pos6 pos5
        '''
        coord1 = (self.coord[0]-1,self.coord[1]-2)
        coord2 = (self.coord[0]+1,self.coord[1]-2)
        coord3 = (self.coord[0]+2,self.coord[1]-1)
        coord4 = (self.coord[0]+2,self.coord[1]+1)
        coord5 = (self.coord[0]+1,self.coord[1]+2)
        coord6 = (self.coord[0]-1,self.coord[1]+2)
        coord7 = (self.coord[0]-2,self.coord[1]+1)
        coord8 = (self.coord[0]-2,self.coord[1]-1)

        self.coord_list = [coord1,coord2,coord3,coord4,coord5,coord6,coord7,coord8]
        self.movable_coord = []
        for coord in self.coord_list:
            if not (coord[0] < 1 or coord[0] > 8 or coord[1] < 1 or coord[1] > 8) and not self.ocupided(coord):
                pygame.draw.circle(screen, self.move_color, self.toPos(coord,False), 8)
                self.movable_coord.append(coord)
class Bishop(Pieces):
    def show_move(self,screen):
        self.movable_coord = []
        # to bottom left
        for i in range(1,8):
            coord = (self.coord[0] - i,self.coord[1]-i)
            if coord[0] < 1 or coord[1] < 1 or self.ocupided(coord):
                break
            self.movable_coord.append(coord)
        # to bottom right
        for i in range(1,8):
            coord = (self.coord[0] + i,self.coord[1] - i)
            if coord[0] > 8 or coord[1] < 1 or self.ocupided(coord):
                break
            self.movable_coord.append(coord)
        # to top left
        for i in range(1,8):
            coord = (self.coord[0] - i, self.coord[1] + i)
            if coord[0] < 1 or coord[1] > 8 or self.ocupided(coord):
                break
            self.movable_coord.append(coord)
        # to top right
        for i in range(1,8):
            coord = (self.coord[0] + i, self.coord[1] + i)
            if coord[0] > 8 or coord[1] > 8 or self.ocupided(coord):
                break
            self.movable_coord.append(coord)
        for coord in self.movable_coord:
            pygame.draw.circle(screen, self.move_color, self.toPos(coord,False), 8)
class Rook(Pieces):
    def show_move(self,screen):
        self.movable_coord = []
        # to left
        for i in range(1, self.coord[0])[::-1]:
            coord = (i, self.coord[1])
            if self.ocupided(coord):
                break
            self.movable_coord.append(coord)
        # to right
        for i in range(self.coord[0]+1,9):
            coord = (i, self.coord[1])
            if self.ocupided(coord):
                break
            self.movable_coord.append(coord)
        # to bottom
        for i in range(1, self.coord[1])[::-1]:
            coord = (self.coord[0],i)
            if self.ocupided(coord):
                break
            self.movable_coord.append(coord)
        # to top
        for i in range(self.coord[1]+1, 9):
            coord = (self.coord[0],i)
            if self.ocupided(coord):
                break
            self.movable_coord.append(coord)


        for coord in self.movable_coord:
            pygame.draw.circle(screen, self.move_color, self.toPos(coord,False), 8)
class Queen(Pieces):
    def show_move(self,screen):
        self.movable_coord = []
        # to bottom left
        for i in range(1,8):
            coord = (self.coord[0] - i,self.coord[1]-i)
            if coord[0] < 1 or coord[1] < 1 or self.ocupided(coord):
                break
            self.movable_coord.append(coord)
        # to bottom right
        for i in range(1,8):
            coord = (self.coord[0] + i,self.coord[1] - i)
            if coord[0] > 8 or coord[1] < 1 or self.ocupided(coord):
                break
            self.movable_coord.append(coord)
        # to top left
        for i in range(1,8):
            coord = (self.coord[0] - i, self.coord[1] + i)
            if coord[0] < 1 or coord[1] > 8 or self.ocupided(coord):
                break
            self.movable_coord.append(coord)
        # to top right
        for i in range(1,8):
            coord = (self.coord[0] + i, self.coord[1] + i)
            if coord[0] > 8 or coord[1] > 8 or self.ocupided(coord):
                break
            self.movable_coord.append(coord)
        # to left
        for i in range(1, self.coord[0])[::-1]:
            coord = (i, self.coord[1])
            if self.ocupided(coord):
                break
            self.movable_coord.append(coord)
        # to right
        for i in range(self.coord[0] + 1, 9):
            coord = (i, self.coord[1])
            if self.ocupided(coord):
                break
            self.movable_coord.append(coord)
        # to bottom
        for i in range(1, self.coord[1])[::-1]:
            coord = (self.coord[0], i)
            if self.ocupided(coord):
                break
            self.movable_coord.append(coord)
        # to top
        for i in range(self.coord[1] + 1, 9):
            coord = (self.coord[0], i)
            if self.ocupided(coord):
                break
            self.movable_coord.append(coord)

        for coord in self.movable_coord:
            pygame.draw.circle(screen, self.move_color, self.toPos(coord,False), 8)

def clickedOn(mouse_pos,pieces):
    mouse_x,mouse_y = mouse_pos
    hit = mouse_x > pieces.pos[0] and mouse_x < pieces.pos[0] + pieces.width and  mouse_y > pieces.pos[1] and mouse_y < pieces.pos[1] + pieces.height
    if hit:
        pieces.selected = True
        print(game.move,game.turn)
        if pieces.id[0] != game.turn[game.move % 2]:
            print(game.turn[game.move % 2])
            print(pieces.id)
            print('in')
            return
    elif pieces.selected:
        for movable_coord in pieces.movable_coord:
            x,y = pieces.toPos(movable_coord)
            if mouse_x > x and mouse_x < x + 44 and mouse_y > y and mouse_y < y + 44 and pieces.selected:
                if board_arr[movable_coord[0] - 1][movable_coord[1] - 1] == 0:
                    board_arr[pieces.coord[0] - 1][pieces.coord[1] - 1] = 0
                    pieces.coord = movable_coord
                    board_arr[movable_coord[0] - 1][movable_coord[1] - 1] = 1
        game.move += 1
        pieces.selected = False

pygame.init()

screen = pygame.display.set_mode((512,512))

board = pygame.image.load("assets/chess/board.png")
board = pygame.transform.scale(board,(360,360))

board_offset = 76

bn1 = Knight((2,8),'bn1',"assets/chess/black_knight.png")
bn2 = Knight((7,8),'bn2',"assets/chess/black_knight.png")
bb1 = Bishop((3,8),'bb1',"assets/chess/black_bishop.png")
bb2 = Bishop((6,8),'bb2',"assets/chess/black_bishop.png")
br1 = Rook((1,8),'br1',"assets/chess/black_rook.png")
br2 = Rook((8,8),'br2',"assets/chess/black_rook.png")
bk1 = King((5,8),'bk1',"assets/chess/black_king.png")
bq1 = Queen((4,8),'bq1',"assets/chess/black_queen.png")

bp1 = Pawn((1,7),'bp1',"assets/chess/black_pawn.png")
bp2 = Pawn((2,7),'bp2',"assets/chess/black_pawn.png")
bp3 = Pawn((3,7),'bp3',"assets/chess/black_pawn.png")
bp4 = Pawn((4,7),'bp4',"assets/chess/black_pawn.png")
bp5 = Pawn((5,7),'bp5',"assets/chess/black_pawn.png")
bp6 = Pawn((6,7),'bp6',"assets/chess/black_pawn.png")
bp7 = Pawn((7,7),'bp7',"assets/chess/black_pawn.png")
bp8 = Pawn((8,7),'bp8',"assets/chess/black_pawn.png")

wn1 = Knight((2,1),'wn1',"assets/chess/white_knight.png")
wn2 = Knight((7,1),'wn2',"assets/chess/white_knight.png")
wb1 = Bishop((3,1),'wb1',"assets/chess/white_bishop.png")
wb2 = Bishop((6,1),'wb2',"assets/chess/white_bishop.png")
wr1 = Rook((1,1),'wr1',"assets/chess/white_rook.png")
wr2 = Rook((8,1),'wr2',"assets/chess/white_rook.png")
wk1 = King((5,1),'wk1',"assets/chess/white_king.png")
wq1 = Queen((4,1),'wq1',"assets/chess/white_queen.png")

wp1 = Pawn((1,2),'wp1',"assets/chess/white_pawn.png")
wp2 = Pawn((2,2),'wp2',"assets/chess/white_pawn.png")
wp3 = Pawn((3,2),'wp3',"assets/chess/white_pawn.png")
wp4 = Pawn((4,2),'wp4',"assets/chess/white_pawn.png")
wp5 = Pawn((5,2),'wp5',"assets/chess/white_pawn.png")
wp6 = Pawn((6,2),'wp6',"assets/chess/white_pawn.png")
wp7 = Pawn((7,2),'wp7',"assets/chess/white_pawn.png")
wp8 = Pawn((8,2),'wp8',"assets/chess/white_pawn.png")

board_arr = [[1, 1, 0, 0, 0, 0, 1, 1],
             [1, 1, 0, 0, 0, 0, 1, 1],
             [1, 1, 0, 0, 0, 0, 1, 1],
             [1, 1, 0, 0, 0, 0, 1, 1],
             [1, 1, 0, 0, 0, 0, 1, 1],
             [1, 1, 0, 0, 0, 0, 1, 1],
             [1, 1, 0, 0, 0, 0, 1, 1],
             [1, 1, 0, 0, 0, 0, 1, 1]]

game = Game()

RUN = True
while RUN:
    screen.fill((31,31,31))
    pygame.Surface.blit(screen,board,(board_offset,board_offset))

    all_pieces = [bn1,bn2,bb1,bb2,br1,br2,bk1,bq1,bp1,bp2,bp3,bp4,bp5,bp6,bp7,bp8
                 ,wn1,wn2,wb1,wb2,wr1,wr2,wk1,wq1,wp1,wp2,wp3,wp4,wp5,wp6,wp7,wp8]

    for piece in all_pieces:
        piece.play(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for piece in all_pieces:
                clickedOn(pos,piece)

    pygame.display.update()
