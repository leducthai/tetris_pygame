import pygame
from random import choice

scr_width , scr_height = 400 , 600
block_size = 20
board_width , board_height = block_size * 10 , block_size * 20
top_left_x = (scr_width - board_width) // 3 
top_left_y = (scr_height - board_height) * 2 // 3



T =[
    [
        [0,0,0,0],
        [0,0,0,0],
        [1,1,1,0],
        [0,1,0,0]
    ],
    [
        [0,0,0,0],
        [1,0,0,0],
        [1,1,0,0],
        [1,0,0,0],
    ],
    [
        [0,0,0,0],
        [0,0,0,0],
        [0,1,0,0],
        [1,1,1,0]
    ],
    [
        [0,0,0,0],
        [0,1,0,0],
        [1,1,0,0],
        [0,1,0,0]
    ]
]

L = [
    [
        [0,0,0,0],
        [1,0,0,0],
        [1,0,0,0],
        [1,1,0,0]
    ],
    [
        [0,0,0,0],
        [0,0,0,0],
        [0,0,1,0],
        [1,1,1,0]
    ],
    [
        [0,0,0,0],
        [1,1,0,0],
        [0,1,0,0],
        [0,1,0,0]
    ],
    [
        [0,0,0,0],
        [0,0,0,0],
        [1,1,1,0],
        [1,0,0,0]
    ]
]

J = [
    [
        [0,0,0,0],
        [0,1,0,0],
        [0,1,0,0],
        [1,1,0,0]
    ],
    [
        [0,0,0,0],
        [0,0,0,0],
        [1,1,1,0],
        [0,0,1,0]
    ],
    [
        [0,0,0,0],
        [1,1,0,0],
        [1,0,0,0],
        [1,0,0,0]
    ],
    [
        [0,0,0,0],
        [0,0,0,0],
        [1,0,0,0],
        [1,1,1,0]
    ]
]

S = [
    [
        [0,0,0,0],
        [0,0,0,0],
        [0,1,1,0],
        [1,1,0,0]
    ],
    [
        [0,0,0,0],
        [1,0,0,0],
        [1,1,0,0],
        [0,1,0,0]
    ]
]

Z = [
    [
        [0,0,0,0],
        [0,0,0,0],
        [1,1,0,0],
        [0,1,1,0]
    ],
    [
        [0,0,0,0],
        [0,1,0,0],
        [1,1,0,0],
        [1,0,0,0]
    ]
]

I = [
    [
        [1,0,0,0],
        [1,0,0,0],
        [1,0,0,0],
        [1,0,0,0]
    ],
    [
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [1,1,1,1]
    ]
]

O = [
    [
        [0,0,0,0],
        [0,0,0,0],
        [1,1,0,0],
        [1,1,0,0]
    ]
]
shapes = [T,L,J,S,Z,I,O]
color = [(153, 51, 255), (255, 128, 0), (0, 0, 153), (3, 255, 28), (255, 0, 0), (3, 248, 255) , (248, 255, 3)]

class piecce:

    def __init__(self, shp) -> None:
        self.x = 4
        self.y = 0
        self.shp = shp
        self.rotation = 0
        self.p_color = shapes.index(shp)

    def rotate(self):
        self.rotation = (self.rotation + 1) % len(self.shp)

    def reverse_rotate(self):
        self.rotation = (self.rotation + len(self.shp) - 1) % len(self.shp)

    def place_ingrid(self ):
        poss = []
        getpiece = self.shp[self.rotation]
        for i in range(4):
            for j in range(4):
                if getpiece[i][j] != 0:
                    poss.append((i + self.y - 3 , j + self.x))
        return poss
        

        

class board:
    
    def __init__(self ) -> None:
        self.grid = [[(0,0,0) for _ in range(10)] for _ in range(20)]

    def check_row(self):
        ls = []

        for i in range(20):
            co = 0
            for j in range(10):
                if self.grid[i][j] == (0,0,0):
                    continue
                co += 1
            if co == 10:
                for o in range(10):
                    self.grid[i][o] = (0,0,0)
                ls.append(i)
        return ls

    def compress(self , ls):
        add_more = 0
        for i in range(19 , -1 , -1):
            if ls and i == ls[-1]:
                ls.pop()
                add_more += 1
                continue
            for j in range(10):
                if add_more != 0:
                    self.grid[i+add_more][j] = self.grid[i][j]
                    self.grid[i][j] == (0,0,0)

    def update(self, pos , clor: int):
        for i , j in pos:
            self.grid[i][j] = color[clor]

    def move_validation(self , pos):
        for i , j in pos:
            if i >= 20 or j <0 or j >= 10:
                return False
            if i >= 0 and self.grid[i][j] != (0,0,0):
                return False
        return True          
    
    def rotate_validation(self , pos):
        m = 0
        for i , j in pos:
            if i >= 0 and i < 20 and j >= 0 and j < 10:
                if self.grid[i][j] != (0,0,0):
                    return False , 0
            m = max(m , j)
        offset = m - 9
        return True , offset

    def lost(self, pos):
        for i , j in pos:
            if i <0 :
                return True
        return False


def get_piece():
    sh = choice(shapes)
    return piecce(sh)

def draw_board(screen):
    
    for i in range(1 , 10):
        pygame.draw.line(screen , (134 , 134 , 134) , (top_left_x + block_size * i , top_left_y) , ( top_left_x + block_size * i , top_left_y + board_height))
    for i in range(1 , 20):
        pygame.draw.line(screen , (134 , 134 , 134) , (top_left_x , top_left_y + block_size * i) , (top_left_x + board_width , top_left_y + block_size * i ))
    pygame.draw.rect(screen , (255 , 0 , 0) , (top_left_x , top_left_y , board_width , board_height) , 4)

def draw_text(screen):
    font = pygame.font.SysFont('Arial' , size= block_size * 2 , bold= True)
    text1 = font.render('TETRIS GAME' , True , (255 ,255 ,255))
    text2 = font.render('NEXT' , True , (255 ,255 ,255))

    screen.blit(text1 , (scr_width // 4 , (top_left_y)//2 - block_size))
    screen.blit(text2 , (top_left_x + board_width + block_size *2//3 , scr_height // 3))


def draw_pieces(screen, nxt , cur , gr):
    nxt_cl = color[nxt.p_color]
    for i , j in nxt.place_ingrid():
        pygame.draw.rect(screen , nxt_cl , (top_left_x + board_width + block_size *2//3 + (j-3) * block_size , scr_height // 3 + (i+3) * block_size + block_size*2 , block_size,block_size))

    cur_color = color[cur.p_color]
    for i , j in cur.place_ingrid():
        if i>=0:
            pygame.draw.rect(screen , cur_color , (top_left_x + block_size*j , top_left_y + i*block_size , block_size , block_size))

    for i in range(20):
        for j in range(10):
            if gr.grid[i][j] != (0,0,0):
                pygame.draw.rect(screen , gr.grid[i][j] , (top_left_x + block_size*j , top_left_y + i*block_size , block_size , block_size))


def main():
    pygame.init()
    try_again = True
    go = True
    
    while go:
        screen = pygame.display.set_mode((scr_width , scr_height))
        clock = pygame.time.Clock()
        run = True
        grid = board()
        cur_piece = get_piece()
        nxt_piece = get_piece()
        time_count = 0
        speed = 0.27
        

        while run:
            try_again = True
            screen.fill((0,0,0))

            time_count += clock.get_rawtime()
            clock.tick()

            if time_count / 1000 >= speed:
                time_count = 0
                cur_piece.y += 1

                if not grid.move_validation(cur_piece.place_ingrid()):
                    cur_piece.y -= 1
                    if grid.lost(cur_piece.place_ingrid()):
                        run = False 
                    else:
                        grid.update(cur_piece.place_ingrid() , cur_piece.p_color)
                        cur_piece = nxt_piece
                        nxt_piece = get_piece()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    go = False
                    run = False
                    try_again = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        cur_piece.y += 1
                        if not grid.move_validation(cur_piece.place_ingrid()):
                            cur_piece.y -=1
                    if event.key == pygame.K_UP:
                        cur_piece.rotate()
                        a , b = grid.rotate_validation(cur_piece.place_ingrid())
                        if not a:
                            cur_piece.reverse_rotate()
                        elif b > 0 :
                            cur_piece.x -= b
                            if not grid.move_validation(cur_piece.place_ingrid()):
                                cur_piece.x += b
                                cur_piece.reverse_rotate()

                    if event.key == pygame.K_RIGHT:
                        cur_piece.x += 1
                        if not grid.move_validation(cur_piece.place_ingrid()):
                            cur_piece.x -= 1
                    if event.key == pygame.K_LEFT:
                        cur_piece.x -= 1
                        if not grid.move_validation(cur_piece.place_ingrid()):
                            cur_piece.x += 1                        

            draw_board(screen)
            draw_text(screen)
            draw_pieces(screen , nxt_piece , cur_piece , grid)
            ls = grid.check_row()
            if ls:
                grid.compress(ls)

            pygame.display.update()
        
        end_screen = pygame.display.set_mode((scr_width , scr_height))
        while try_again:
            end_screen.fill((123 , 123 , 123))
            pygame.draw.rect(end_screen ,(255 , 102 , 51) ,(scr_width // 2 - 5*block_size , scr_height // 2 - block_size , 10 * block_size , 2*block_size))

            font = pygame.font.SysFont('Arial' , size= block_size , bold= True)
            text = font.render('Click Here to Retry' , True , (255 ,255 ,255))
            end_screen.blit(text , (scr_width // 2 , scr_height // 2))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    try_again = False
                    go = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mous_x , mous_y = pygame.mouse.get_pos()
                    if event.button == 1 and scr_width // 2 - 5*block_size <= mous_x <=(scr_width // 2 - 5*block_size) + (10 * block_size) and scr_height // 2 - block_size <= mous_y  <= scr_height // 2 - block_size + 2*block_size:
                        try_again = False
                        run = True
            pygame.display.update()

main()
    


