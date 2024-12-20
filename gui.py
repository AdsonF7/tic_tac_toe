from tkinter import Tk, Button, Frame, Label

class GUI(Tk):
    
    def __init__(self):
        super().__init__()
        self.title = "Tic Tac Toe"
        self.frame_top = Frame(self)
        frame_middle = Frame(self)
        frame_bottom = Frame(self)
        self.buttons = self.create_buttons()
        self.lb_log = Label(frame_middle)
        self.lb_log.pack()
        bt_reset = Button(frame_bottom, text="Reset", command=self.reset)
        bt_reset.pack()
        self.frame_top.pack(padx=10, pady=(10, 5))
        frame_middle.pack()
        frame_bottom.pack(pady=(5, 10))
        self.reset()
        
    def create_buttons(self):
        buttons = []
        for i in range(3):
            for j in range(3):
                button = Button(self.frame_top, text="", width=5, height=2)
                button.grid(column=i, row=j)
                button.bind("<Button-1>", lambda event, i=i, j=j: self.button_command(event, i, j))
                buttons.append(button)
        return buttons
    
    @property
    def current_player(self):
        return self._current_player

    @current_player.setter
    def current_player(self, value):
        if value in [1, 2]:
            self._current_player = value

    def button_command(self, event, x, y):
        if self.matrix[x][y] == 0 and not self.finish:
            self.change_text_button(event.widget)
            self.matrix[x][y] = self.current_player
            self.reduce_empty()
            result = self.result_verify() 
            if result == "win" or result == "draw":
                self.finish = True
                if result == "win":
                    self.lb_log["text"] = f"O jogador {self._current_player} venceu!"
                elif result == "draw":
                    self.lb_log["text"] = f"O jogo terminou empatado!"
            self.change_player()
            
    def reduce_empty(self):
        self.empty -= 1
        
    def change_text_button(self, widget):
        widget["text"] = ["X", "O"][self.current_player - 1]

    def change_text_log(self, text):
        self.lb_log["text"] = text
        
    def change_player(self):
        self.current_player = 2 // self.current_player

    def reset(self):
        self.empty = 9
        self.matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.current_player = 1
        self.finish = False
        self.lb_log["text"] = ""
        for button in self.buttons:
            button["text"] = ""
    
    def result_verify(self):
        matrix = []
        diagonal_1 = []
        diagonal_2 = []
        for i in range(3):
            rows = []
            columns = []
            diagonal_1.append(self.matrix[i][i])
            diagonal_2.append(self.matrix[2-i][i])
            for j in range(3):
                rows.append(self.matrix[j][i])
                columns.append(self.matrix[i][j])
            matrix.append(columns)
            matrix.append(rows)
        matrix.append(diagonal_1)
        matrix.append(diagonal_2)

        for l in matrix:
            if "".join(map(str, l)) in ["111", "222"]:
                return "win"
        if self.empty == 0:
            return "draw"
        return None
    




