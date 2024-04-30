from OneFetchStep import OneFetchStep
from TwoDecodeStep import TwoDecodeStep
from ThreeExecutionStep import ThreeExecutionStep
from FourMemoryStep import FourMemoryStep
from FiveWriteStep import FiveWriteStep
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

    def __init__(self, register_file) -> None:
        self.memory = {}  
        self.instructions = []  
        self.oneFetchStep = OneFetchStep()
        self.twoDecodeStep = TwoDecodeStep()
        self.threeExecutionStep = ThreeExecutionStep()
        self.fourMemoryStep = FourMemoryStep()
        self.fiveWriteStep = FiveWriteStep()
 
        self.PC = 0  # Inicializa o contador do Program Counter (PC)
        self.register_file = register_file  # Armazena o banco de registradores


    def importPipeLine(self, allFile):

        self.memory = [i for i in range(0, 20)]

        self.memory[1] = -1
        self.memory[2] = 10
        self.memory[3] = 1

        lines = allFile.split('\n')

        for line in lines:
            #if ':' in line:
                # label, value = line.split(':')
                # self.memory[label.strip()] = int(value.strip().split()[-1])

            #else:
                instruction_parts = line.split()  
                if instruction_parts:  
                    opcode = instruction_parts[0]  
                    operands = instruction_parts[1:]
                    instruction_object = self.Instruction(opcode, *operands)
                    self.instructions.append(instruction_object)

    def print_pipeline_state(self):
        print("Pipeline State:")
        print("Fetch Step:", self.oneFetchStep.opcode if self.oneFetchStep else None,
            self.oneFetchStep.op1 if self.oneFetchStep else None,
            self.oneFetchStep.op2 if self.oneFetchStep else None,
            self.oneFetchStep.op3 if self.oneFetchStep else None,
            self.oneFetchStep.valida if self.oneFetchStep else None)
        print("Decode Step:", self.twoDecodeStep.opcode if self.twoDecodeStep else None,
            self.twoDecodeStep.op1 if self.twoDecodeStep else None,
            self.twoDecodeStep.op2 if self.twoDecodeStep else None,
            self.twoDecodeStep.op3 if self.twoDecodeStep else None,
            self.twoDecodeStep.valida if self.twoDecodeStep else None)
        print("Execution Step:", self.threeExecutionStep.opcode if self.threeExecutionStep else None,
            self.threeExecutionStep.op1 if self.threeExecutionStep else None,
            self.threeExecutionStep.op2 if self.threeExecutionStep else None,
            self.threeExecutionStep.op3 if self.threeExecutionStep else None,
            self.threeExecutionStep.valida if self.threeExecutionStep else None)
        print("Memory Step:", self.fourMemoryStep.opcode if self.fourMemoryStep else None,
            self.fourMemoryStep.op1 if self.fourMemoryStep else None,
            self.fourMemoryStep.op2 if self.fourMemoryStep else None,
            self.fourMemoryStep.op3 if self.fourMemoryStep else None,
            self.fourMemoryStep.valida if self.fourMemoryStep else None)
        print("Write Step:", self.fiveWriteStep.opcode if self.fiveWriteStep else None,
            self.fiveWriteStep.op1 if self.fiveWriteStep else None,
            self.fiveWriteStep.op2 if self.fiveWriteStep else None,
            self.fiveWriteStep.op3 if self.fiveWriteStep else None,
            self.fiveWriteStep.valida if self.fiveWriteStep else None)
        print("Register File Registers:")
        for i, value in enumerate(self.register_file.registers):
            print(f"R{i}: {value}", end=", ")

        
        # Imprimir o banco de registradores
        # print("Register Memory:")
        # for i, register_value in enumerate(self.register_file.registers):
        #     print(f"R{i}: {register_value}")
        
        print("\n")





    def advance_pipeline(self): 

        ####Run

        if self.fiveWriteStep is not None and self.fiveWriteStep.opcode is not None:
            self.fiveWriteStep.execute_instruction5()
            self.register_file.write_register(self.fiveWriteStep.register_number,self.fourMemoryStep.memoryValue)

            if self.fiveWriteStep.opcode == "add":
                self.finalRegister= int(self.fiveWriteStep.op1.replace('$','').replace('t','').replace(',',''))

                self.register_file.write_register(self.finalRegister,self.resultCalc)

        if self.fourMemoryStep.opcode is not None:
            self.fiveWriteStep.setAttributes(self.fourMemoryStep, self.register_file)

        if self.fourMemoryStep is not None and self.fourMemoryStep.opcode is not None:
            self.fourMemoryStep.execute_instruction4()


        if self.threeExecutionStep.opcode is not None:
            self.fourMemoryStep.setAttributes(self.threeExecutionStep)
        


        if self.threeExecutionStep is not None and self.threeExecutionStep.opcode is not None:
            self.threeExecutionStep.execute_instruction3()
            self.fourMemoryStep.setfinalDisplacement(self.threeExecutionStep.getfinalDisplacement())
            if self.threeExecutionStep.opcode == "add":
                self.resultCalc = self.registerValue1+self.registerValue2

            #self.threeExecutionStep.setfinalDisplacement()

        if self.twoDecodeStep.opcode is not None:
            self.threeExecutionStep.setAttributes(self.twoDecodeStep, self.register_file, self.memory)
        

        if self.twoDecodeStep is not None and self.twoDecodeStep.opcode is not None:
            #self.twoDecodeStep.execute_instruction2()
            if self.twoDecodeStep.opcode == "add":

                if self.twoDecodeStep.op2 is not None and self.twoDecodeStep.op3 is not None:

                    self.twoDecodeStep.op2 = int(str(self.twoDecodeStep.op2).replace('$','').replace('t','').replace(',',''))
                    self.twoDecodeStep.op3 = int(str(self.twoDecodeStep.op3).replace('$','').replace('t',''))
                    

                    self.registerValue1 = self.register_file.read_register(self.twoDecodeStep.op2)
                    self.registerValue2 = self.register_file.read_register(self.twoDecodeStep.op3)


        # if self.twoDecodeStep:
        #     self.twoDecodeStep.execute_instruction()
        # else:
        #     print("Erro: twoDecodeStep is null")

        if self.oneFetchStep.opcode is not None:
            self.twoDecodeStep.setAttributes(self.oneFetchStep)
        






            #################



        if self.PC < len(self.instructions):
            next_instruction = self.instructions[self.PC]

            self.PC += 1  # Incrementa o PC para buscar a próxima instrução

            # Cria uma nova instância da classe OneFetchStep com base na próxima instrução
            self.oneFetchStep = OneFetchStep(next_instruction.opcode, next_instruction.op1, next_instruction.op2, next_instruction.op3, next_instruction.valida)
            
        else: 
            self.oneFetchStep = OneFetchStep("---", "---", "---", "---", "---")


        


