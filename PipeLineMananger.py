class PipeLineMananger:
    
    def __init__(self) -> None:
        pass


    def importPipeLine(self, allFile):
        self.instructions = []
        lines = allFile.split('\n')

        for line in lines:
            self.instructions.append(line);





