class LogicGate:

    def __init__(self, n):
        self.name = n
        self.output = None

    def getName(self):
        return self.name

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output


class BinaryGate(LogicGate):

    def __init__(self, n):
        LogicGate.__init__(self, n)

        self.pinA = None
        self.pinB = None

    def getPinA(self):
        if self.pinA is None:
            return int(input("Enter Pin A input for gate "+self.getName()+"->"))
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.pinB is None:
            return int(input("Enter Pin B input for gate "+self.getName()+"->"))
        else:
            return self.pinB.getFrom().getOutput()

    def setNextPin(self, source):
        if self.pinA is None:
            self.pinA = source
        else:
            if self.pinB is None:
                self.pinB = source
            else:
                print("Cannot Connect: NO EMPTY PINS on this gate")


class AndGate(BinaryGate):

    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a == 1 and b == 1:
            return 1
        else:
            return 0


class OrGate(BinaryGate):

    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a == 1 or b == 1:
            return 1
        else:
            return 0


class UnaryGate(LogicGate):

    def __init__(self, n):
        LogicGate.__init__(self, n)

        self.pin = None

    def getPin(self):
        if self.pin is None:
            return int(input("Enter Pin input for gate "+self.getName()+"-->"))
        else:
            return self.pin.getFrom().getOutput()

    def setNextPin(self, source):
        if self.pin is None:
            self.pin = source
        else:
            print("Cannot Connect: NO EMPTY PINS on this gate")


class NotGate(UnaryGate):

    def __init__(self, n):
        UnaryGate.__init__(self, n)

    def performGateLogic(self):
        if self.getPin():
            return 0
        else:
            return 1


class NandGate(AndGate):

    def performGateLogic(self):
        if super().performGateLogic() == 1:
            return 0
        else:
            return 1


class NorGate(OrGate):

    def performGateLogic(self):
        if super().performGateLogic() == 1:
            return 0
        else:
            return 1


class XorGate(NorGate):

    def performGateLogic(self):
        if super().performGateLogic() == 1:
            return 1
        else:
            return 0


class Connector:

    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate

        tgate.setNextPin(self)

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate


def HalfAdder(LC):
    def __init__(self, name):
        LC.__init__(self, name)
        self.A = Connector(self, 'A', 1)
        self.B = Connector(self, 'B', 1)
        self.S = Connector(self, 'S')
        self.C = Connector(self, 'C')
        self.X1 = XorGate("X1")
        self.A1 = AndGate("A1")
        self.A.connect([self.X1.A, self.A1.A])
        self.B.connect([self.X1.B, self.A1.B])
        self.X1.C.connect([self.S])
        self.A1.C.connect([self.C])


def main():
    g1 = AndGate("G1")
    g2 = NandGate("G2")
    g3 = OrGate("G3")
    g4 = NotGate("G4")
    c1 = Connector(g1, g3)
    c2 = Connector(g2, g3)
    c3 = Connector(g3, g4)
    print(g2.getOutput())


main()
