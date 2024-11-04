from tkinter import *
from tkinter import messagebox
#from tkmacosx import Button

# the game board class to handle the board logic like player switching, new game/restart. 
class board:
    def __init__(self, board_size = 8, game_mode = "Simple"):
        self.board_size = board_size
        self.board = [['' for _ in range(board_size)] for _ in range(board_size)]
        self.game_mode = game_mode
        self.player = "blue"
        self.blue_symbol = "S"
        self.red_symbol = "S"

    def reset_game(self):

        self.game_mode.set(self.game_mode.get())
        self.blue_symbol.set("S")
        self.red_symbol.set("S")

        self.board = [[''for _ in range (self.board_size)] for _ in range(self.board_size)]
        self.player = "blue"

    def switch(self): # this will simply switch players based on the current (red or blue) player.
        if self.player == "blue":
            self.player = "red"
        else:
            self.player = "blue"


# This is for sprint 4. I want to refactor the code. Things are out of place, and its a mess.
'''
# make the game more fun by adding a timer. Like chess. 
class timer:
    def __init__(self):
        pass

# this will deal with the human and computer player later on
class player_computer:
    def __init__(self):
        pass

# here I will record the game like in chess but the hard part will be making the game replay by it self.
class recorded_replay():
    def __init__(self):
        pass
'''

# class to handle the type of game
class game_type_and_conditions():
    def __init__(self, game_mode):
        self.game_mode = game_mode
        self.simple_win = False
        self.all_draw = False
        self.general_win = False
        self.blue_points = 0
        self.red_points = 0
        #self.board_size = len(board)
        self.buttons = None

    # this was the hardest part, tons of googling required. I used a tictactoe game I found and used it as the reference.
    def is_sos(self, row, col, board, buttons):
        self.board_size = len(board)
        symbol = board[row][col]
        sos_count = 0
        
        color = "green"

        # in this I couldn't figure out how to draw lines. I used a hihglighting method
        # source for this methic is codemy.com, sepcifically this video: Tic Tac Toe Game - Python Tkinter GUI Tutorial #113
        # Ik this needs to be reconfitured becaue it has so many reeating lines that can be made into functions that are dynamic
        if symbol == 'S':
            # check right and then it create the hihglihted to indicate lines.
            if col <= self.board_size - 3:
                if board[row][col+1] == 'O' and board[row][col+2] == 'S':
                    sos_count += 1
                    buttons[row][col].config(disabledforeground=color)
                    buttons[row][col+1].config(disabledforeground=color)
                    buttons[row][col+2].config(disabledforeground=color)
            
            # check left and then it create the hihglihted to indicate lines.
            if col >= 2:
                if board[row][col-1] == 'O' and board[row][col-2] == 'S':
                    sos_count += 1
                    buttons[row][col].config(disabledforeground=color)
                    buttons[row][col-1].config(disabledforeground=color)
                    buttons[row][col-2].config(disabledforeground=color)
            
            # check down and then it create the hihglihted to indicate lines.
            if row <= self.board_size - 3:
                if board[row+1][col] == 'O' and board[row+2][col] == 'S':
                    sos_count += 1
                    buttons[row][col].config(disabledforeground=color)
                    buttons[row+1][col].config(disabledforeground=color)
                    buttons[row+2][col].config(disabledforeground=color)
            
            # check up and then it create the hihglihted to indicate lines.
            if row >= 2:
                if board[row-1][col] == 'O' and board[row-2][col] == 'S':
                    sos_count += 1
                    buttons[row][col].config(disabledforeground=color)
                    buttons[row-1][col].config(disabledforeground=color)
                    buttons[row-2][col].config(disabledforeground=color)
                    
            # check to see if diagonal down-right
            if row <= self.board_size - 3 and col <= self.board_size - 3:
                if board[row+1][col+1] == 'O' and board[row+2][col+2] == 'S':
                    sos_count += 1
                    buttons[row][col].config(disabledforeground=color)
                    buttons[row+1][col+1].config(disabledforeground=color)
                    buttons[row+2][col+2].config(disabledforeground=color)
                    
            # check to see if diag right dwon
            if row >= 2 and col >= 2:
                if board[row-1][col-1] == 'O' and board[row-2][col-2] == 'S':
                    sos_count += 1
                    buttons[row][col].config(disabledforeground=color)
                    buttons[row-1][col-1].config(disabledforeground=color)
                    buttons[row-2][col-2].config(disabledforeground=color)
                    
            # check to see if diag down left
            if row <= self.board_size - 3 and col >= 2:
                if board[row+1][col-1] == 'O' and board[row+2][col-2] == 'S':
                    sos_count += 1
                    buttons[row][col].config(disabledforeground=color)
                    buttons[row+1][col-1].config(disabledforeground=color)
                    buttons[row+2][col-2].config(disabledforeground=color)
                    
            # check to see if diag up right
            if row >= 2 and col <= self.board_size - 3:
                if board[row-1][col+1] == 'O' and board[row-2][col+2] == 'S':
                    sos_count += 1
                    buttons[row][col].config(disabledforeground=color)
                    buttons[row-1][col+1].config(disabledforeground=color)
                    buttons[row-2][col+2].config(disabledforeground=color)
                    
        elif symbol == 'O':
            # look for the horizontal
            if col >= 1 and col <= self.board_size - 2:
                if board[row][col-1] == 'S' and board[row][col+1] == 'S':
                    sos_count += 1
                    buttons[row][col-1].config(disabledforeground=color)
                    buttons[row][col].config(disabledforeground=color)
                    buttons[row][col+1].config(disabledforeground=color)
            
            # thi is for verticla
            if row >= 1 and row <= self.board_size - 2:
                if board[row-1][col] == 'S' and board[row+1][col] == 'S':
                    sos_count += 1
                    buttons[row-1][col].config(disabledforeground=color)
                    buttons[row][col].config(disabledforeground=color)
                    buttons[row+1][col].config(disabledforeground=color)
            
            # check the diagonal
            if row >= 1 and row <= self.board_size - 2 and col >= 1 and col <= self.board_size - 2:
                if board[row-1][col-1] == 'S' and board[row+1][col+1] == 'S':
                    sos_count += 1
                    buttons[row-1][col-1].config(disabledforeground=color)
                    buttons[row][col].config(disabledforeground=color)
                    buttons[row+1][col+1].config(disabledforeground=color)
            
            # check the diagonal
            if row >= 1 and row <= self.board_size - 2 and col >= 1 and col <= self.board_size - 2:
                if board[row-1][col+1] == 'S' and board[row+1][col-1] == 'S':
                    sos_count += 1
                    buttons[row-1][col+1].config(disabledforeground=color)
                    buttons[row][col].config(disabledforeground=color)
                    buttons[row+1][col-1].config(disabledforeground=color)

        return sos_count

    def is_draw(self, board): # simple draw function checks for emptiness
        for row in board:
            if '' in row:
                return False
        return True

    def simple_game(self, row, col, board_placements, buttons, current_player):
        if self.is_sos(row, col, board_placements, buttons):
            self.simple_win = True
            return True  # return the True if there's a win
        if self.is_draw(board_placements):
            self.all_draw = True
            return "Draw"
        return None

    def general_game(self, row, col, board_placements, buttons, current_player):
        sos_formed = self.is_sos(row, col, board_placements, buttons)

        #simple function add up scoring
        if current_player == "blue":
            self.blue_points += sos_formed
        else:
            self.red_points += sos_formed

        # looking for the win
        if self.is_draw(board_placements):
            if self.blue_points > self.red_points:
                return "Blue Wins!"
            elif self.red_points > self.blue_points:
                return "Red Wins!"
            else:
                return "Draw"
        # this is helping with keeping the same player acutally kind of clever lol
        if sos_formed > 0:
            return True
        
        return False


# GUI class for the game interface
class gui (board): # this will make it so inhertis the board for access.
    def __init__(self, display):
        self.display = display
        self.display.title("S.O.S")
        super().__init__() # this applies the intial setting.

        self.game_mode = StringVar(value = self.game_mode) # intital starting game mode
        self.player = StringVar(value="blue") # initial starting player
        self.blue_symbol = StringVar(value="S") # initial starting plater symbol
        self.red_symbol = StringVar(value="S") # intial second player symbol


        self.labels()
        self.buttons()
        self.grid()
        self.reset_game()

        self.game_handler = game_type_and_conditions(self.game_mode.get()) # works here because it is an instance variable.

    def start_new_game(self):

        new_board_size = int(self.board_size_entry.get())

        if new_board_size < 3 or new_board_size > 12:
            messagebox.showerror("Invalid Input", "Size in between 3 and 12.")
            return

        if new_board_size != self.board_size:
            self.board_size = new_board_size
            self.grid_frame.destroy()
            self.grid()

        else:
            # clear the existing grid if size hasn't changed
            for row_buttons in self.buttons:
                for button in row_buttons:
                    button.config(text=" ", state = NORMAL)

        self.reset_game()
        self.status_label.config(text = "")  # cleaing the label o
        self.game_handler.blue_points = 0
        self.blue_score.config(text = f"Score: {self.game_handler.blue_points}")
        self.game_handler.red_points = 0
        self.red_score.config(text = f"Score: {self.game_handler.red_points}")
        self.turn_label.config(text="Current Player: Blue")

    def labels(self): # referenced W3schools and stackoverflow to create the frame.
        self.game_type_frame = Frame(self.display)
        self.game_type_frame.pack(side=TOP, fill=X)

        self.place_left_frame = Frame(self.game_type_frame)
        self.place_left_frame.pack(side = LEFT)

        self.place_right_frame = Frame(self.game_type_frame)
        self.place_right_frame.pack(side=RIGHT)
        Label(self.place_right_frame, text="Board size").pack(side=LEFT)
        self.board_size_entry = Entry(self.place_right_frame, width = 3)
        self.board_size_entry.insert(0, "8")
        self.board_size_entry.pack(side=LEFT)

        self.control_frame_blue = Frame(self.display)
        self.control_frame_blue.pack(side = LEFT)
        Label(self.control_frame_blue, text="Blue Player", fg = "cyan").grid(row = 0, column = 0)
        self.blue_score = Label(self.control_frame_blue, text = f"Score: {game_type_and_conditions(self.game_mode.get()).red_points}")
        self.blue_score.grid(row = 4, column = 0)

        self.control_frame_red = Frame(self.display)
        self.control_frame_red.pack(side=RIGHT)
        Label(self.control_frame_red, text="Red Player", fg = "red").grid(row = 3, column = 0)
        self.red_score = Label(self.control_frame_red, text = f"Score: {game_type_and_conditions(self.game_mode.get()).red_points}")
        self.red_score.grid(row = 7, column = 0) # this makes it so the valye isn't None. Solution found through stackoverflow

        self.turn_label = Label(self.display, text="Current Player: Blue")
        self.turn_label.pack(side=BOTTOM)

        self.status_label = Label(self.display, text = "", fg = "green")
        self.status_label.pack(side=BOTTOM)

    def buttons(self): # utilized geeksforgeeks examples to implement this.
        #buttons for the game selection
        Radiobutton(self.place_left_frame, text="Simple", variable = self.game_mode, value = "Simple").pack(side=LEFT)
        Radiobutton(self.place_left_frame, text="General", variable = self.game_mode, value = "General").pack(side=LEFT)


         #buttons for the blue player's S or O selection
        Radiobutton(self.control_frame_blue, text = "S", fg = "cyan", variable = self.blue_symbol, value="S").grid(row = 1, column = 0)
        Radiobutton(self.control_frame_blue, text = "O", fg = "cyan", variable = self.blue_symbol, value="O").grid(row = 2, column = 0)

        #buttons for the red player's S or O selection
        Radiobutton(self.control_frame_red, text = "S", fg = "red", variable = self.red_symbol, value = "S").grid(row=4, column=0)
        Radiobutton(self.control_frame_red, text = "O", fg = "red", variable = self.red_symbol, value = "O").grid(row=5, column=0)

        # IK this is a ceneted but it makes sense.
        Button(self.display, text = "New Game", command = self.start_new_game).pack(side = BOTTOM)

    def SOS_button(self, row, col):
        if self.player == "blue":
            self.sos_symbol = self.blue_symbol.get()
            color = "cyan"
        else:  # red player
            self.sos_symbol = self.red_symbol.get()
            color = "red"


        self.buttons[row][col].config(text=self.sos_symbol, state = DISABLED, disabledforeground = color)
        self.board[row][col] = self.sos_symbol

        if self.game_mode.get() == "Simple":
            result = self.game_handler.simple_game(row, col, self.board, self.buttons, self.player)
            if result == True:
                self.status_label.config(text = f"{self.player} Wins!")
                return
            elif result == "Draw":
                self.status_label.config(text = f"{result}")
                return
            else:
                self.switch()

        else:  # General mode
            result = self.game_handler.general_game(row, col, self.board, self.buttons, self.player)
            if result == "Blue Wins!" or result == "Red Wins!":
                self.blue_score.config(text = f"Score: {self.game_handler.blue_points}")
                self.red_score.config(text = f"Score: {self.game_handler.red_points}")
                self.status_label.config(text = f"{result}")
                return
            elif result == "Draw":
                self.blue_score.config(text = f"Score: {self.game_handler.blue_points}")
                self.red_score.config(text = f"Score: {self.game_handler.red_points}")
                self.status_label.config(text = f"{result}")
            elif not result:
                self.switch()
            else:
                self.blue_score.config(text = f"Score: {self.game_handler.blue_points}")
                self.red_score.config(text = f"Score: {self.game_handler.red_points}")


        self.turn_label.config(text=f"Current Player: {'Blue' if self.player == 'blue' else 'Red'}")

    def grid(self):
        self.grid_frame = Frame(self.display)
        self.grid_frame.pack()
        self.buttons = []
        for r in range(self.board_size):
            button_r = []
            for c in range(self.board_size):
                #, width = 1, height = 1
                SOS_buttons = Button(self.grid_frame, text = " ", command = lambda row = r, col = c: self.SOS_button(row, col))
                SOS_buttons.grid(row = r, column = c)
                button_r.append(SOS_buttons)
            self.buttons.append(button_r)



# Main function to start the application
class main(board):
    def __init__(self):
        board.__init__(self, board_size = 8, game_mode = "Simple")
        display = Tk()
        app = gui(display)
        display.geometry("1000x500")

        display.mainloop()

# this helps with indicating that this file is to executed. (Source: M1Coding)
if __name__ == "__main__":
    main()