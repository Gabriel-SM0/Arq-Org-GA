class FiveWriteStep:
    def __init__(self, four=None, memoryValue=None):
        if four is not None:
            self.opcode = four.opcode
            self.op1 = four.op1
            self.op2 = four.op2
            self.op3 = four.op3
            self.valida = four.valida
            self.memoryValue = four.memoryValue
        else:
            self.opcode = None
            self.op1 = None
            self.op2 = None
            self.op3 = None
            self.valida = None
            self.memoryValue = memoryValue

    @classmethod
    def empty_constructor(cls):
        return cls()


    def setAttributes(self, four, register_file):
        self.opcode = four.opcode
        self.op1 = four.op1
        self.op2 = four.op2
        self.op3 = four.op3
        self.valida = four.valida
        self.register_file = register_file


    def execute_instruction5(self):
        # Se a instrução for de carregamento (LW), salvar o valor na posição do registrador especificado
        if self.opcode == "lw":
            # Verifica se op1 é um registrador válido (deve estar na forma $tX, onde X é um número de registrador)
            if self.op1.startswith("$t"):
                # Remove quaisquer caracteres não numéricos de op1 e a vírgula
                op1_cleaned = ''.join(filter(str.isdigit, self.op1))
                # Obtém o número do registrador a partir da string op1
                self.register_number = int(op1_cleaned)

                #if 0 <= self.register_number < len(self.register_file.registers):
                    # Salva o valor da memória (memoryValue) na posição do registrador especificado
                    #self.register_file.write_register(self.register_number, self.memoryValue)


    
