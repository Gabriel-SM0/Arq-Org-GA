class TwoDecodeStep:
    def __init__(self, OneFetchStep,register_file):
        self.opcode = OneFetchStep.opcode
        self.op1 = OneFetchStep.op1
        self.op2 = OneFetchStep.op2
        self.op3 = OneFetchStep.op3
        self.valida = OneFetchStep.valida
        self.register_file = register_file

        # Decodificação dos Operandos
        self.decode_operands()

    def decode_operands(self):
        # Se os operandos forem registradores, buscar os valores nos registradores
        if self.opcode in ["ADD", "SUB", "ADDI", "SUBI"]:
            self.op2_value = self.register_file.read_register(self.op2)
            self.op3_value = self.register_file.read_register(self.op3)
        elif self.opcode in ["BEQ", "J"]:
            # Não é necessário buscar valores nos registradores para BEQ e J
            pass

    # Métodos para acessar os operandos decodificados, se necessário
    def get_operand_values(self):
        return self.op2_value, self.op3_value