import random, time

width = 1000
height = 800



scale = 20
def draw_lines():
    stroke(169,169,169)
    for col in range(width/scale):
        
        line(col*scale, 0, col*scale, height)
        
    for row in range(height/scale):
        line(0, scale*row, width, scale*row)

def populate_board():
    for char in range(len(board)):
        seed = random.uniform(0, 1)
        if seed >= .8:
            board[char] = '1'
        else:
            board[char] = '0'

def draw_squares():
    col = 0
    row = 0
    stroke(0,0,0,0)
    for char in board:
        if char == '0':
            fill(0,0,0)
            rect((scale*col)+1, (scale*row)+1, scale-2, scale-2)
            col+=1
        elif char == '1':
            fill(0,255,0)
            rect((scale*col)+1, (scale*row)+1, scale-2, scale-2)
            col +=1
        if col == width/scale:
            row+=1
            col = 0
        
def check_squares():
    
    toBeBorn = []
    toBeKilled = []
    height_new = height/scale
    width_new = width/scale
    for char in range(0,len(board)):
        squares_adjacent = 0
        adjacent_square_nums = []
        dist_left_wall = (char % width_new)
        dist_right_wall = ((width_new)-(char % width_new))-1
        dist_top = char//width_new
        dist_bottom = (height_new-1)-(char//width_new)
        
        if board[char] == '1' or board[char] == '0':
            #
            if dist_left_wall > 0 and dist_right_wall > 0 and dist_top > 0 and dist_bottom > 0:
                
                adjacent_square_nums.extend((char-1,char+1,(char-width_new),char+width_new,(char-width_new)-1,(char-width_new)+1,(char+width_new)-1,(char+width_new)+1))
            

            else:
            
                if dist_bottom > 0:
                    adjacent_square_nums.append(char+width_new)
                    if dist_right_wall > 0:
                        adjacent_square_nums.append(char+(width_new+1))
                    if dist_left_wall > 0:
                        adjacent_square_nums.append(char+(width_new-1))
                if dist_top > 0:
                    adjacent_square_nums.append(char-width_new)
                    if dist_right_wall > 0:
                        adjacent_square_nums.append(char-(width_new+1))
                    if dist_left_wall > 0:
                        adjacent_square_nums.append(char-(width_new-1))
                if dist_right_wall > 0:
                    adjacent_square_nums.append(char+1)
                if dist_left_wall > 0:
                    adjacent_square_nums.append(char-1)
                    
            for square in adjacent_square_nums:
                #print('%s: %s' % (square, board[square]))
                if board[square] == '1':
                    squares_adjacent += 1
                
            if (squares_adjacent >= 1 and squares_adjacent <= 5) and board[char] == '1':
                toBeBorn.append(char)
                #print("lived")
            elif (squares_adjacent >= 6 or squares_adjacent <= 0) and board[char] == '1':
                toBeKilled.append(char)
            elif squares_adjacent == 3 and board[char] == '0':
                toBeBorn.append(char)
    
    for square in toBeBorn:
        board[square] = '1'
    for square in toBeKilled:
        board[square] = '0'
                
                
class Button():
    def __init__(self, text,x,y):
        self.x = x
        self.y = y
        self.text = text
    
    def draw_button(self, color):
        rectMode(CENTER)
        fill(255,255,255)
        rect(self.x,self.y,100,50)
        fill(0,102,0)
        textSize(20)
        textAlign(CENTER)
        text(self.text, self.x,self.y+5)
    def return_x(self):
        return(self.x)
    def return_y(self):
        return(self.y)
    def mouseInButton(self,mousex,mousey):
        x_values = []
        y_values = []
        for i in range(self.x-50,self.x+50):
            x_values.append(i)
        if mousex in x_values:
            for n in range(int(self.y-25),int(self.y+25)):
                y_values.append(n)
            if mousey in y_values:
                return True
            else:
                return False
        else:
            return False

    
        
def convertToArray(x, y, delete = False):


    x -= (x % scale)
    y -= (y % scale)
    x = x / scale
    y = y / scale
    array_num = y*(width/scale)+x

    if not delete:
        if board[array_num] == '0':
            board[array_num] = '1'
        
    elif delete:
    
        if board[array_num] == '1':
        
            board[array_num] = '0'
       
        

        
def buttons():
    global start_button
    global stop_button
    global random_button
    global delete_button
    global clear_button
    
    h = 900
    fill(0,100,255)
    rect(0,800,1000,100)
    white = (255,255,255)
    start_button = Button('Start',width/15,14.15*(h/15))
    stop_button = Button('Stop',3*(width/15),14.15*(h/15))
    random_button = Button('Random',5*(width/15),14.15*(h/15))
    
    clear_button = Button('Clear',7*(width/15),14.15*(h/15))
    start_button.draw_button(white)
    stop_button.draw_button(white)

    random_button.draw_button(white)
    clear_button.draw_button(white)
                    
def setup():
    global board
    global running
    global custom
    frameRate(10)
    background(0,0,0)
    global delete
    delete = False
    running = False
    custom = False
    size(1000, 900)
    board = list('0' * ((width/scale)*(height/scale)))
    draw_lines()
    buttons()
    rectMode(CORNER)
                           
    

def draw():
    if running:
        draw_squares()
        #print(board)
        check_squares()
        #time.sleep(2)
    
def mouseClicked():
    global running
    global custom
    global board
    
    pressed_delete = False
    
    if start_button.mouseInButton(mouseX, mouseY):
        running = True
    if stop_button.mouseInButton(mouseX, mouseY):
        running = False
    #if custom_button.mouseInButton(mouseX, mouseY):
     #   custom = True
    if random_button.mouseInButton(mouseX, mouseY):
        populate_board()
        draw_squares()
    if clear_button.mouseInButton(mouseX, mouseY):
        board = list('0' * ((width/scale)*(height/scale)))
        draw_squares()
        
def mouseDragged():
    if mouseY < 800 and mouseX < 1000 and mouseX > 0:
        if mouseButton == LEFT:
            convertToArray(mouseX, mouseY, False)
            draw_squares()
        if mouseButton == RIGHT:
            convertToArray(mouseX, mouseY, True)
            draw_squares()
        
        


    
    
