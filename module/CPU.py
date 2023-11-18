from module.Alu import Alu
import threading

class CPU:
    def __init__(self):
        self.memory = []
        self.registers = [0] * 8
        self.state = False
        self.pc = 0
        self.MAR = 0
        self.MBR = 0
        self.ir = 0

    def cargarInstrucciones(self, instrucciones):
        self.memory[:len(instrucciones)] = instrucciones

    def fetch(self):

        self.MAR = self.pc
        instruction = self.memory[self.MAR]
        self.MBR = instruction
        self.pc += 1
        self.ir = self.MBR

        opcode, dir, des, reg, operand1, operand2 = self.decode()
        operand1 = self.execute(opcode, operand1, operand2)
        return operand1

    def decode(self):
        opcode = self.ir[:5]
        dir = self.ir[5:6]
        des = self.ir[6:10]
        reg = self.ir[10:13]
        operand1 = self.ir[13:21]
        operand2 = self.ir[21:]

        return opcode, dir, des, reg, operand1, operand2

    def execute(self, opcode, operand1, operand2):

        opcode = self.binario(opcode)
        if (opcode <= 7):
            operand1 = self.binario(operand1)
            operand2 = self.binario(operand2)

            alu = Alu(opcode, operand1, operand2)

            operand1 = alu.execute()
            print(operand1)

        return operand1

    def run(self):
        self.state = True

        for i in self.memory:
            operand1 = self.fetch()
        return operand1

    def binario(self, binario):
            numero = int(binario, 2)
            return numero