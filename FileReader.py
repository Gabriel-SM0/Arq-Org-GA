class FileReader:
    def __init__(self):
        self.content = None  # Inicializa o atributo 'content' como None

    def readFile(self, path):
        try:
            with open(path, 'r') as f:
                self.content = f.read()  # Lê o conteúdo do arquivo e salva no atributo 'content'
        except FileNotFoundError:
            print("Arquivo não encontrado.")
            

    def returnContent(self):
        return str(self.content)

