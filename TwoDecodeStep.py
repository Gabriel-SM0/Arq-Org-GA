class TwoDecodeStep:
    def __init__(self, fetch_step, register_file, memory):
        self.opcode = fetch_step.opcode
        self.op1 = fetch_step.op1
        self.op2 = fetch_step.op2
        self.op3 = fetch_step.op3
        self.valida = fetch_step.valida
        self.register_file = register_file
        self.memory = memory

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
