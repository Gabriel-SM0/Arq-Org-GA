class TwoDecodeStep:
    def __init__(self, OneFetchStep):
        self.opcode = OneFetchStep.opcode
        self.op1 = OneFetchStep.op1
        self.op2 = OneFetchStep.op2
        self.op3 = OneFetchStep.op3
        self.valida = OneFetchStep.valida