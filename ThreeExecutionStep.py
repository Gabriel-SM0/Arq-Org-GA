class ThreeExecutionStep:
    def __init__(self, two, register_file, memory):
        self.opcode = two.opcode
        self.op1 = two.op1
        self.op2 = two.op2
        self.op3 = two.op3
        self.valida = two.valida
        self.register_file = register_file
        self.memory = memory

        # Execução da instrução
        self.execute_instruction()

    def execute_instruction(self):
        # Se a instrução for de carregamento (LW), buscar o valor na memória e armazená-lo no registrador
        if self.opcode == "LW":
            data_value = self.memory.read_memory(self.memory_address)
            self.register_file.write_register(self.op1, data_value)