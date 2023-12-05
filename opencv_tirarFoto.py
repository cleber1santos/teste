import cv2
import tkinter as tk
from PIL import Image, ImageTk

class CapturadorFoto:
    def __init__(self, janela, janela_titulo, camera_index=0):
        self.janela = janela
        self.janela.title(janela_titulo)

        self.cap = cv2.VideoCapture(camera_index)

        self.canvas = tk.Canvas(janela, width=self.cap.get(3), height=self.cap.get(4))
        self.canvas.pack()

        self.nome_var = tk.StringVar()
        self.caixa_nome = tk.Entry(janela, textvariable=self.nome_var, width=30)
        self.caixa_nome.pack()

        self.botao_captura = tk.Button(janela, text="Capturar Foto", command=self.capturar_foto)
        self.botao_captura.pack()

        self.foto = None
        self.vid_id = None
        self.atualizar()
        self.janela.mainloop()

    def capturar_foto(self):
        ret, frame = self.cap.read()

        if ret:
            nome = self.nome_var.get()
            nome = nome if nome else "Desconhecido"
            
            # Salvar a foto com o nome da pessoa
            caminho_saida = f"{nome}_foto_capturada.jpg"
            cv2.imwrite(caminho_saida, frame)

            self.foto = ImageTk.PhotoImage(Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)))
            self.vid_id = self.canvas.create_image(0, 0, anchor=tk.NW, image=self.foto)

    def atualizar(self):
        ret, frame = self.cap.read()

        if ret:
            self.foto = ImageTk.PhotoImage(Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)))
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.foto)

        self.janela.after(10, self.atualizar)

if __name__ == "__main__":
    root = tk.Tk()
    app = CapturadorFoto(root, "Capturador de Foto")
