class FourMemoryStep:
    def __init__(self, three=None):
        if three is not None:
            self.opcode = three.opcode
            self.op1 = three.op1
            self.op2 = three.op2
            self.op3 = three.op3
            self.valida = three.valida
            self.finalDisplacement = three.finalDisplacement
            self.memory = three.memory
        else:
            self.opcode = None
            self.op1 = None
            self.op2 = None
            self.op3 = None
            self.valida = None
            self.finalDisplacement = None
            self.memory = None



    @classmethod
    def empty_constructor(cls):
        return cls()
    
   
    def setAttributes(self, three):
        self.opcode = three.opcode
        self.op1 = three.op1
        self.op2 = three.op2
        self.op3 = three.op3
        self.valida = three.valida
        self.finalDisplacement = three.finalDisplacement
        self.memory = three.memory

    def execute_instruction4(self):
        # Se a instrução for de carregamento (LW), buscar o valor na memória e armazená-lo no registrador
        if self.opcode == "lw":

            # Dividindo a string em torno de '('
                if self.finalDisplacement < len(self.memory):
                # Obtém o valor na posição finalDisplacement de memory
                    self.memoryValue = self.memory[self.finalDisplacement]

    def setfinalDisplacement(self, finalDisplacement):
        self.finalDisplacement = finalDisplacement