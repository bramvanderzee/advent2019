class Computer:
    def __init__(self, name, program):
        self.__index = 0
        self.name = name
        self.program = program
        self.running = True

        self.__endInstruction(0)

    def __endInstruction(self, indexIncrement):
        self.__index += indexIncrement
        if self.program[self.__index] == 3:
            self.nextIsInput = True
        elif self.program[self.__index] == 4:
            self.nextIsOutput = True
        else:
            self.nextIsInput = False
            self.nextIsOutput = False

    def __readMode(self):
        mode = str(self.program[self.__index]).zfill(5)[:3].zfill(3)
        opcode = int(str(self.program[self.__index])[-2:])
        return (mode, opcode)

    def __readParam(self, mode, pos):
        param = self.program[self.__index+pos]
        if mode[3-pos] == '0':
            outParam = self.program[param]
        else:
            outParam = param
        return outParam

    def __writeParam(self, paramPos, value):
        posIndex = self.__readParam('111', paramPos)
        self.program[posIndex] = value

    # Adds params 1 and 2 and stores it in param 3
    def __opcode1(self, mode):
        val1 = self.__readParam(mode, 1)
        val2 = self.__readParam(mode, 2)
        self.__writeParam(3, val1 + val2)
        self.__endInstruction(4)

    # Multiplies params 1 and 2 and stores it in param 3
    def __opcode2(self, mode):
        val1 = self.__readParam(mode, 1)
        val2 = self.__readParam(mode, 2)
        self.__writeParam(3, val1 * val2)
        self.__endInstruction(4)

    # Takes input and stores it in param 1
    def __opcode3(self, mode, givenInput = None):
        if givenInput == None:
            numIn = int(input('%s: Enter value:' % self.name))
        else:
            numIn = int(givenInput)
        self.__writeParam(1, numIn)
        self.__endInstruction(2)

    # Reads and prints param 1
    def __opcode4(self, mode):
        outPos = self.__readParam(mode, 1)
        print(self.name, ': Output:', outPos)
        self.__endInstruction(2)
        return outPos

    # Jump if true
    def __opcode5(self, mode):
        if self.__readParam(mode, 1) != 0:
            self.__index = self.__readParam(mode, 2)
            self.__endInstruction(0)
        else:
            self.__endInstruction(3)

    # Jump if false
    def __opcode6(self, mode):
        if self.__readParam(mode, 1) == 0:
            self.__index = self.__readParam(mode, 2)
            self.__endInstruction(0)
        else:
            self.__endInstruction(3)

    # Less than
    def __opcode7(self, mode):
        toStore = 0
        p1 = self.__readParam(mode, 1)
        p2 = self.__readParam(mode, 2)
        if p1 < p2:
            toStore = 1
        self.__writeParam(3, toStore)
        self.__endInstruction(4)

    # Equals
    def __opcode8(self, mode):
        toStore = 0
        p1 = self.__readParam(mode, 1)
        p2 = self.__readParam(mode, 2)
        if p1 == p2:
            toStore = 1
        self.__writeParam(3, toStore)
        self.__endInstruction(4)

    def next(self, givenInput = None):
        if self.running:
            if self.__index > len(self.program):
                self.running = False
            mode, opcode = self.__readMode()
            if opcode == 1:
                self.__opcode1(mode)
            elif opcode == 2:
                self.__opcode2(mode)
            elif opcode == 3:
                if not givenInput == None:
                    self.__opcode3(mode, int(givenInput))
                else:
                    self.__opcode3(mode)
            elif opcode == 4:
                return self.__opcode4(mode)
            elif opcode == 5:
                self.__opcode5(mode)
            elif opcode == 6:
                self.__opcode6(mode)
            elif opcode == 7:
                self.__opcode7(mode)
            elif opcode == 8:
                self.__opcode8(mode)
            elif opcode == 99:
                print(self.name, ': End of program')
                self.running = False
