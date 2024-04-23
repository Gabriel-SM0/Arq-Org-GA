from OneFetchStep import OneFetchStep
class PipeLineMananger:
    
    class Instruction:
        def __init__(self, opcode, *operands):
            self.opcode = opcode
            self.op1 = operands[0] if len(operands) > 0 else None
            self.op2 = operands[1] if len(operands) > 1 else None
            self.op3 = operands[2] if len(operands) > 2 else None
            self.valida = operands[3] if len(operands) > 3 else None



        def __str__(self):
            return f"{self.opcode} {self.op1} {self.op2} {self.op3} {self.valida}"

    def __init__(self) -> None:
        self.memory = {}  
        self.instructions = []  
        self.fetch_step = None  
        self.decode_step = None  
        self.execution_step = None  
        self.memory_step = None  
        self.write_step = None  
        self.PC = 0  # Inicializa o contador do Program Counter (PC)

    def importPipeLine(self, allFile):
        lines = allFile.split('\n')

        for line in lines:
            if ':' in line:
                label, value = line.split(':')
                self.memory[label.strip()] = int(value.strip().split()[-1])
            else:
                instruction_parts = line.split()  
                if instruction_parts:  
                    opcode = instruction_parts[0]  
                    operands = instruction_parts[1:]
                    instruction_object = self.Instruction(opcode, *operands)
                    self.instructions.append(instruction_object)

    def print_pipeline_state(self):
        print("Pipeline State:")
        print("Fetch Step:", self.fetch_step.opcode if self.fetch_step else None,
            self.fetch_step.op1 if self.fetch_step else None,
            self.fetch_step.op2 if self.fetch_step else None,
            self.fetch_step.op3 if self.fetch_step else None,
            self.fetch_step.valida if self.fetch_step else None)
        print("Decode Step:", self.decode_step.opcode if self.decode_step else None,
            self.decode_step.op1 if self.decode_step else None,
            self.decode_step.op2 if self.decode_step else None,
            self.decode_step.op3 if self.decode_step else None,
            self.decode_step.valida if self.decode_step else None)
        print("Execution Step:", self.execution_step.opcode if self.execution_step else None,
            self.execution_step.op1 if self.execution_step else None,
            self.execution_step.op2 if self.execution_step else None,
            self.execution_step.op3 if self.execution_step else None,
            self.execution_step.valida if self.execution_step else None)
        print("Memory Step:", self.memory_step.opcode if self.memory_step else None,
            self.memory_step.op1 if self.memory_step else None,
            self.memory_step.op2 if self.memory_step else None,
            self.memory_step.op3 if self.memory_step else None,
            self.memory_step.valida if self.memory_step else None)
        print("Write Step:", self.write_step.opcode if self.write_step else None,
            self.write_step.op1 if self.write_step else None,
            self.write_step.op2 if self.write_step else None,
            self.write_step.op3 if self.write_step else None,
            self.write_step.valida if self.write_step else None)
        print("\n")


    def advance_pipeline(self):
        self.write_step = self.memory_step
        self.memory_step = self.execution_step
        self.execution_step = self.decode_step
        self.decode_step = self.fetch_step

        if self.PC < len(self.instructions):
            next_instruction = self.instructions[self.PC]
            self.PC += 1  # Incrementa o PC para buscar a próxima instrução

            # Cria uma nova instância da classe OneFetchStep com base na próxima instrução
            self.fetch_step = OneFetchStep(next_instruction.opcode, next_instruction.op1, next_instruction.op2, next_instruction.op3, next_instruction.valida)
        else: 
            self.fetch_step = OneFetchStep(None, None, None, None, None)
        


