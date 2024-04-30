class OneFetchStep:
    def __init__(self, opcode=None, op1=None, op2=None, op3=None, valida=None):
        self.opcode = opcode
        self.op1 = op1
        self.op2 = op2
        self.op3 = op3
        self.valida = valida


    
    def execute_instruction(self):
        print("Oque está acontecendo aqui")