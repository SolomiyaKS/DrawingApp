import tkinter as tk

class Drawing:
    def __init__(self, root):
        self.root = root
        self.title = 'Drawing'

        self.canvas = tk.Canvas(self.root, width=700, height=500, background='white')
        self.canvas.pack()

        self.color = 'black'
        self.line_width_ = '1'

        self.red_button = tk.Button(self.root, text='Червоний', width=10, command=lambda: self.ch_color('red'))
        self.red_button.pack(side='left')

        self.blue_button = tk.Button(self.root, text='Синій', width=10, command=lambda: self.ch_color('blue'))
        self.blue_button.pack(side='left')

        self.green_button = tk.Button(self.root, text='Зелений', width=10, command=lambda: self.ch_color('green'))
        self.green_button.pack(side='left')
        self.black_button = tk.Button(self.root, text='Чорний', width=10, command=lambda: self.ch_color('black'))
        self.black_button.pack(side='left')

        self.clear_button = tk.Button(self.root, text='Очистити', width=10, command=self.clear)
        self.clear_button.pack(side='right')

        self.eraser_button = tk.Button(self.root, text = 'Стерти', width=10, command=self.eraser)
        self.eraser_button.pack(side='right')

        self.fill_canvas_button = tk.Button(self.root, text='Заливка', width=10, command=self.fill_canvas)
        self.fill_canvas_button.pack(side='right')

        self.line_width = tk.Entry(self.root)
        self.line_width.pack(side='right')
        self.line_width.insert(tk.END, "1")

        self.canvas.bind('<B1-Motion>', self.draw)

        self.d_obj = []
        self.undo_stack = []


    def draw(self, dr):
        x, y = dr.x, dr.y
        lw = self.line_width.get()
        if lw.isdigit():
            r = int(self.line_width.get())
            obj = self.canvas.create_oval(x - r, y - r, x + r, y + r, fill=self.color, outline=self.color, width=self.line_width_)
            self.d_obj.append(obj)

    def ch_color(self, new_color):
        self.color = new_color

    def eraser(self):
        self.color = 'white'
    def clear(self):
        self.canvas.delete('all')
        self.d_obj = []

    def fill_canvas(self):

        fill_color = self.color
        self.canvas.create_rectangle(0, 0, 1000, 1000, fill=fill_color, outline=fill_color)


root = tk.Tk()
d = Drawing(root)
root.mainloop()