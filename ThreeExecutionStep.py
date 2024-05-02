class ThreeExecutionStep:
    def __init__(self, two=None, register_file=None, memory=None):
        if two is not None:
            self.opcode = two.opcode
            self.op1 = two.op1
            self.op2 = two.op2
            self.op3 = two.op3
            self.valida = two.valida
            self.register_file = register_file
            self.memory = memory
            self.finalDisplacement = None
            

        else:
            self.opcode = None
            self.op1 = None
            self.op2 = None
            self.op3 = None
            self.valida = None
            self.register_file = None
            self.memory = None
            self.displacement = None
    
    def setAttributes(self, two, register_file, memory):
        self.opcode = two.opcode
        self.op1 = two.op1
        self.op2 = two.op2
        self.op3 = two.op3
        self.valida = two.valida
        self.register_file = register_file
        self.memory = memory
        self.finalDisplacement = None
    
    def execute_instruction3(self):
        # Se a instrução for de carregamento (LW), buscar o valor na memória e armazená-lo no registrador
        if self.opcode == "lw":
            # Dividindo a string em torno de '('
            #op2 = 100($t0)
            self.displacement_str, self.register_base_str = self.op2.split('(')
            #displacement_str = 100($, register_base_str = t0)

            # Convertendo o deslocamento para inteiro
            self.displacement = int(self.displacement_str)

            # Removendo o caractere ')' do final do registrador base
            self.register_base_str = self.register_base_str.replace(')', '').replace('t', '')

            # Removendo o caractere '$' da string do registrador base
            self.register_base_str = self.register_base_str.replace('$', '')

            # Convertendo o registrador base para inteiro
            self.register_base = int(self.register_base_str)

            print("espaçamento final é " + str(self.displacement + self.register_base))

            self.finalDisplacement = self.displacement + self.register_base
            self.setfinalDisplacement(self.displacement + self.register_base)


        if self.opcode == "ADD":
            # Dividindo a string em torno de '('

            self.register_base_str = self.register_base_str.replace(')', '').replace('t', '')

            # Removendo o caractere '$' da string do registrador base
            self.register_base_str = self.register_base_str.replace('$', '')

            # Convertendo o registrador base para inteiro
            self.register_base = int(self.register_base_str)

            print("espaçamento final é " + str(self.displacement + self.register_base))

            self.finalDisplacement = self.displacement + self.register_base
            self.setfinalDisplacement(self.displacement + self.register_base)






    def getfinalDisplacement(self):
        return self.finalDisplacement
    
    def setfinalDisplacement(self, finalDisplacement):
        self.finalDisplacement = finalDisplacement


