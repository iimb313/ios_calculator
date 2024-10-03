import customtkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.default_variables()
        self.build_window()

    def build_window(self):
        self.configure(fg_color="#1c1c1c")
        self.title("ios calculator")
        self.geometry("500x750")
        self.resizable(False, False)

        self.input_section = customtkinter.CTkEntry(self, width=490, border_color="#1c1c1c", height=50, font=("Arial", 70), fg_color="#1c1c1c", text_color="#FFF")
        self.input_section.place(x=5, y=50)
        self.input_section.bind("<KeyRelease>", self.validate_input)

        frame = customtkinter.CTkFrame(self, height=600, width=500, fg_color="#1c1c1c")
        frame.place(x=0, y=150)

        numbers = [
            [7, 8, 9, "×"], #0
            [4, 5, 6, "-"], #1
            [1, 2, 3, "+"], #2
            [0, ".", "="], #3
            ["C", "+/-", "%", "÷"] #4
        ]

        buttons = [
            [0, 1, 2, 3], #0
            [0, 1, 2, 3], #1
            [0, 1, 2, 3], #2
            [0, 1, 2],    #3
            [0, 1, 2, 3], #4
        ]
        y=120
        x=10

        for r in range(3):
            for c in range(3):
                button_number = numbers[r][c]
                buttons[r][c]=customtkinter.CTkButton(frame, hover_color="#d4d4d2", width=100, height=100, fg_color="#505050", text_color="#fff", corner_radius=50, text=button_number, font=('', 20))
                buttons[r][c].place(y=y, x=x)
                x+=120
            y+=120
            x=10

        buttons[3][0]=customtkinter.CTkButton(frame, width=230, height=100, corner_radius=50, text=str(numbers[3][0]), font=('', 20), hover_color="#d4d4d2", fg_color="#505050", text_color="#fff")
        buttons[3][0].place(y=y, x=x)
        x+=240
        buttons[3][1]=customtkinter.CTkButton(frame, width=100, height=100, corner_radius=50, text=str(numbers[3][1]), font=('', 20), hover_color="#d4d4d2", fg_color="#505050", text_color="#fff")
        buttons[3][1].place(y=y, x=x)
        x+=120
        buttons[3][2]=customtkinter.CTkButton(frame, width=100, height=100, corner_radius=50, text=str(numbers[3][2]), font=('', 20), hover_color="#ffbe63", fg_color="#ff9500", text_color="#fff")
        buttons[3][2].place(y=y, x=x)

        y=120
        for i in range(3):
            buttons[i][3]=customtkinter.CTkButton(frame, width=100, height=100, corner_radius=50, text=str(numbers[i][3]), font=('', 20), hover_color="#ffbe63", fg_color="#ff9500", text_color="#fff")
            buttons[i][3].place(y=y, x=x)
            y+=120
        buttons[1][3].place(x=x+5)

        y=10
        x=10
        buttons[4][0]=customtkinter.CTkButton(frame, width=100, height=95, corner_radius=48.75, text=str(numbers[4][0]), font=('', 20), hover_color="#eaeae7", fg_color="#d4d4d2", text_color="black")
        buttons[4][0].place(y=(y+5), x=x)
        x+=120
        buttons[4][1]=customtkinter.CTkButton(frame, width=90, height=95, corner_radius=46.25, text=str(numbers[4][1]), font=('', 20), hover_color="#eaeae7", fg_color="#d4d4d2", text_color="black")
        buttons[4][1].place(y=(y+5), x=x)
        x+=120
        buttons[4][2]=customtkinter.CTkButton(frame, width=90, height=95, corner_radius=46.25, text=str(numbers[4][2]), font=('', 20), hover_color="#eaeae7", fg_color="#d4d4d2", text_color="black")
        buttons[4][2].place(y=(y+5), x=(x+2.5))
        x+=120
        buttons[4][3]=customtkinter.CTkButton(frame, width=100, height=95, corner_radius=48.75, text=str(numbers[4][3]), font=('', 20), hover_color="#ffbe63", fg_color="#ff9500", text_color="#fff")
        buttons[4][3].place(y=(y+5), x=(x+2))
        
        self.buttons_list = [element for row in buttons for element in row]

        for button in self.buttons_list:
            button.configure(command=lambda b=button: self.button_clicked(b))

    def button_clicked(self, button:customtkinter.CTkButton):
        value = str(button._text)
        symbols = {
            "+":"+",
            "-":"-",
            "÷":"/",
            "×":"*",
            "%":"%",
            "+/-":"-",
            ".": "."
        }
        if value == "=":
            self.evaluate_calculation()
        elif value=="C":
            self.clear_calculation()
        else:
            if value in symbols:
                if value!=".":button.configure(fg_color="#FFF", text_color="#ffbe63", hover=False)
                value=symbols[value]
            self.add_to_calculation(value)


    def clear_signs(self, pass_button:customtkinter.CTkButton=None):
        if pass_button!=None:
            pass_button = pass_button._text
  
        for btn in self.buttons_list:
            txt = btn._text
            if pass_button != txt and txt in ["+", "-", "÷", "×"]:
                btn.configure(hover_color="#ffbe63", fg_color="#ff9500", text_color="#fff", hover=True)


    def default_variables(self):
        self.calculation = ""

    def validate_input(self, event):
        input_value = self.input_section.get()
        try:
            if input_value[-1].isdigit() or input_value[-1] in "+-*/%.":
                valid_characters = "0123456789+-/*%."
                filtered_value = ''.join([char for char in input_value if char in valid_characters])
                try:self.add_to_calculation(filtered_value[-1])
                except:pass
            self.input_section.delete(0, "end")
            self.input_section.insert(0, filtered_value)
        except:pass

    def add_to_calculation(self, symbol: str):
        if symbol.isdigit() or symbol in "+-/*%.":
            if symbol.isdigit():self.clear_signs()
            self.calculation += str(symbol)
            self.input_section.delete(0, "end")
            self.input_section.insert(0, self.calculation)


    def evaluate_calculation(self):
        self.clear_signs()
        try:
            self.calculation = str(eval(self.calculation))
            self.input_section.delete(0, "end")
            self.input_section.insert(0, self.calculation)
        except SyntaxError:
            self.input_section.delete(0, "end")
            self.input_section.insert(0, "Error")

    def clear_calculation(self):
        self.clear_signs()
        self.calculation = ""
        self.input_section.delete(0, "end")
        self.input_section.insert(0, self.calculation)


app = App()
app.mainloop()
