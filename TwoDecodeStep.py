class TwoDecodeStep:
    def __init__(self, fetch_step=None, register_file=None, memory=None):
        if fetch_step is not None:
            self.opcode = fetch_step.opcode
            self.op1 = fetch_step.op1
            self.op2 = fetch_step.op2
            self.op3 = fetch_step.op3
            self.valida = fetch_step.valida
            self.register_file = register_file
            self.memory = memory
        else:
            self.opcode = None
            self.op1 = None
            self.op2 = None
            self.op3 = None
            self.valida = None
            self.register_file = None
            self.memory = None

    def setAttributes(self, fetch_step):
        self.opcode = fetch_step.opcode
        self.op1 = fetch_step.op1
        self.op2 = fetch_step.op2
        self.op3 = fetch_step.op3
        self.valida = fetch_step.valida

        # Decodificação dos Operandos no construtor
    def execute_instruction2(self):
        # Se a instrução for de carregamento (LW), buscar o valor na memória e armazená-lo no registrador
        if self.opcode == "add":

            if self.op2 is not None and self.op3 is not None:

                self.op2 = int(str(self.op2).replace('$','').replace('t','').replace(',',''))
                self.op3 = int(str(self.op3).replace('$','').replace('t',''))



    def setfinalDisplacement(self, finalDisplacement):
        self.finalDisplacement = finalDisplacement


