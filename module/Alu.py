class Alu:
    operand1 = 0
    operand2 = 0
    instruction = 0
    comparacion = " "
    b = None

    def __init__(self, instruction, operand1, operand2=0):
        self.operand1 = operand1
        self.operand2 = operand2
        self.instruction = instruction

    def execute(self):
        operacion = self.codops.get(self.instruction)
        ex = operacion(self)
        return ex

    def ADD(self):
        self.operand1 = self.operand1 + self.operand2
        return self.operand1

    def SUB(self):
        self.operand1 = self.operand1 - self.operand2
        return self.operand1

    def MUL(self):
        self.operand1 = self.operand1 * self.operand2
        return self.operand1

    def DIV(self):
        self.operand1 = self.operand1 / self.operand2
        return int(self.operand1)

    def MOV(self):
        self.operand1 = self.operand2
        return self.operand1

    def DEC(self):
        self.operand1 = self.operand1 - 1
        return self.operand1

    def INC(self):
        self.operand1 = self.operand1 + 1
        return self.operand1

    def CMP(self):
        if (self.operand1 == self.operand2):
            if (self.operand1 > self.operand2):
                self.comparacion = "Mayor o igual"
            elif (self.operand1 < self.operand2):
                self.comparacion = "Menor o igual"
            else:
                self.comparacion = "Igual"
        elif(self.operand1 > self.operand2):
            self.comparacion = "Mayor"
        elif(self.operand1 < self.operand2):
            self.comparacion = "Menor"
        else:
            self.comparacion = "No igual"
        return self.comparacion


##### ?????????????????????????????????????????????????
    def NOT(self):
        self.operand1 = -self.operand1

    def AND(self):
        if (self.operand1 and self.operand2):
            self.b = True
        else:
            self.b = False
    def OR(self):
        if(self.operand1 or self.operand2):
            self.b = True
        else:
            self.b = False

    def XOR(self):
        if((self.operand1 or self.operand2) and not(self.operand1 and self.operand2)):
            self.b = True
        else:
            self.b = False

    codops = {
        0: ADD, 1: SUB, 2: MUL, 3: DIV, 4: MOV, 5: DEC, 6: INC, 7: CMP,
        ##Duda
        10:NOT, 11:AND, 12:OR, 13:XOR
    }
