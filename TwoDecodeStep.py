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
        #self.decode_operands()

        # def decode_operands(self):
        # # Se a instrução for uma carga (LW), buscar o valor na memória e armazená-lo no registrador
        # if self.opcode == "lw":
        #     if self.op1.startswith("$"):  # Verifica se o primeiro operando é um registrador
        #         register_name = self.op1[1:]  # Remove o símbolo $ do nome do registrador
        #         memory_address = self.memory[self.op2]  # Obtém o endereço de memória a ser carregado
        #         data_value = self.memory.read_memory(memory_address)  # Lê o valor da memória
        #         self.register_file.write_register(register_name, data_value)  # Escreve o valor no registrador
