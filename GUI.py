import tkinter as Tk
from tkinter import messagebox
from Rule import Rule
from Parser import Parser
from TuringMachine import TuringMachine
from Motion import Motion
import threading
class Window():
    def __init__(self) -> None:
        self.flagForActivateTuring = False
        #Ventana
        self.window = Tk.Tk()
        self.window.title("Maquina de Turing")
        self.window.geometry("500x500")
        self.window.resizable(width=False,height=False)

        #Label principal
        self.title = Tk.Label(self.window,text="Maquina de Turing")
        self.title.configure(font=("Segoe Script",23))
        self.title.pack(side=Tk.TOP)

        #Entrada del usuario
        self.input = Tk.Entry(self.window)
        self.input.insert(Tk.END,"11011")
        self.input.pack(side=Tk.TOP)

        #Boton Guardar
        self.saveButton = Tk.Button(self.window,text="Actualizar",command=self.saveButtonAction)
        self.saveButton.pack(side = Tk.TOP)

        #Frame de las instrucciones
        self.instructionsLabelFrame = Tk.LabelFrame(self.window,text="Instrucciones")
        instructionsText = """-Cada linea contiene una linea de la forma\n<estado actual><simbolo actual>\n<simbolo nuevo><direccion><estado nuevo>\n
        -Puedes usar cualquier simbolo en <estado actual>\ny <estado nuevo>\n
        -Puedes usar "_" para representar espacios en\nblanco y "*" para representar\ncualquier simbolo o estado.\n
        -La maquina se detiene cuando encuentre\nalgun estado que finalice con T.
        """
        self.instructions1 = Tk.Label(self.instructionsLabelFrame,text=instructionsText)
        self.instructions1.pack()
        self.instructionsLabelFrame.pack(side=Tk.LEFT,expand=True)


        #Se genera el area de texto
        self.textLabelFrame = Tk.LabelFrame(self.window,text="Reglas")
        self.textArea = Tk.Text(self.textLabelFrame,height=20,width=40,wrap='none')
        self.scrolly = Tk.Scrollbar(self.textLabelFrame,command=self.textArea.yview)
        self.scrollx = Tk.Scrollbar(self.textLabelFrame,command=self.textArea.xview,orient=Tk.HORIZONTAL)
        self.textArea.configure(yscrollcommand=self.scrolly.set)
        self.textArea.configure(xscrollcommand=self.scrollx.set)
        testText = """0 0 _ r 1o
0 1 _ r 1i
0 _ _ * accept T
1o _ _ l 2o
1o * * r 1o
1i _ _ l 2i
1i * * r 1i
2o 0 _ l 3
2o _ _ * accept T
2o * * * reject T
2i 1 _ l 3
2i _ _ * accept T
2i * * * reject T
3 _ _ * accept T
3 * * l 4
4 * * l 4
4 _ _ r 0"""
        self.textArea.insert(Tk.END,testText)
        self.scrolly.pack(side=Tk.RIGHT,fill=Tk.Y)
        self.scrollx.pack(side=Tk.BOTTOM)
        self.textArea.pack(side=Tk.RIGHT)
        self.textLabelFrame.pack(anchor=Tk.NE)

        #Boton para correr la Maquina
        self.runButton = Tk.Button(self.window,text="Run",command=self.runButtonAction)
        self.runButton.pack(anchor=Tk.NW)

        #Diccionario de las reglas de la maquina de Turing
        self.rules = dict()

    def saveButtonAction(self)->None:
        #Se lee el archivo y se revisa con el parser
        test = self.textArea.get("1.0", "end-1c")
        with open('turing_machine_rules.txt','w') as archivo:
            archivo.writelines([test])
        self.flagForActivateTuring = self.parseInfo() and self.parseRules()

    def parseInfo(self)->bool:
        parser = Parser()
        try:
            parser.parseFile()
            return True
        except Exception as e:
            messagebox.showerror("Error de lectura",e)
            return False
    
    def parseRules(self)->bool:
        parser = Parser()
        try:
            self.rules = parser.createRulesDictionary()
            return True
        except Exception as e:
            messagebox.showerror("Error de lectura",e)
            self.rules = dict()
            return False
    
    def readUserInput(self)->list:
        #Lee el input de la entrada del usuario
        text = self.input.get()
        userInput = []
        for symbol in text:
            if symbol == " ":
                userInput.append("_")
            else:
                userInput.append(symbol)
        return userInput

    def motionThread(self)->None:
        motion = Motion(TuringMachine(self.rules,self.readUserInput()))
        motion.runMotion()

    def runButtonAction(self):
        #Se revisa que la maquina de turing sea apta para activarla y se pasa a realizar su animacion.
        if not self.flagForActivateTuring:
            messagebox.showerror("Error al iniciar la máquina","Actualiza las reglas o escribelas correctamente")
        else:
            thread = threading.Thread(target=self.motionThread)
            thread.start()
            
    def starWindow(self):
        self.window.mainloop()
    