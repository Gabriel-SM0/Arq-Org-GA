class RegisterFile:
    def __init__(self, num_registers):
        self.registers = [0] * num_registers  # Inicializa todos os registradores com o valor 0

    def read_register(self, register_num):
        return self.registers[register_num]

    def write_register(self, register_num, value):
        self.registers[register_num] = value

    def __getitem__(self, key):
        return self.registers[key]

    def __setitem__(self, key, value):
        self.registers[key] = value
