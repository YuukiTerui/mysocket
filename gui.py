import tkinter as tk
from server import Server
from client import Client


class ServerFrame(tk.Frame):
    def __init__(self) -> None:
        tk.Frame.__init__(self)
        self.server = Server()
        self.create_widgets()
        self.server.start()

    def create_widgets(self):
        self.text = tk.Text(self, width=50, height=10)
        self.text.pack()
        self.text.insert('1.0', 'Server is ready')

        self.row2 = tk.Frame(self)
        self.row2.pack()
        self.portarea = tk.Entry(self.row2)
        self.portarea.pack(side=tk.LEFT, expand=True)
        self.connect_btn = tk.Button(self.row2, text='Connect Port', command=self.connect_btn_clicked)
        self.connect_btn.pack(side=tk.LEFT, expand=True)

    def connect_btn_clicked(self):
        port = int(self.portarea.get())
        self.server.connect_port(port)


class ClientFrame(tk.Frame):
    def __init__(self) -> None:
        tk.Frame.__init__(self)
        self.client = Client()
        self.create_widgets()

    def create_widgets(self):
        self.textarea = tk.Text(self, width=50, height=10)
        self.textarea.pack()
        self.textarea.insert('1.0', 'client is ready')

        self.row2 = tk.Frame(self)
        self.row2.pack()
        self.hostarea = tk.Entry(self.row2)
        self.hostarea.pack(side=tk.LEFT, expand=True)
        self.portarea = tk.Entry(self.row2)
        self.portarea.pack(side=tk.LEFT, expand=True)
        self.connect_btn = tk.Button(self.row2, text='Connect Server', command=self.connect_btn_clicked)
        self.connect_btn.pack(side=tk.LEFT, expand=True)

        self.row3 = tk.Frame(self)
        self.row3.pack()
        self.msgarea = tk.Entry(self.row3)
        self.msgarea.pack(side=tk.LEFT, expand=True)
        self.send_btn = tk.Button(self.row3, text='Send', command=self.send_btn_clicked)
        self.send_btn.pack(side=tk.LEFT)

    def connect_btn_clicked(self):
        self.client.host = self.hostarea.get()
        port = int(self.portarea.get())
        self.client.connect_port(port)

    def send_btn_clicked(self):
        msg = self.msgarea.get()
        self.client.send(msg)
        self.textarea.insert('end', msg)

class App(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title = 'SocketApp'
        self.resizable(width=False, height=False)
        self.server = ServerFrame()
        self.server.pack(side=tk.LEFT)
        self.client = ClientFrame()
        self.client.pack(side=tk.LEFT)
        


def main():
    app = App()
    app.mainloop()


if __name__ == '__main__':
    main()