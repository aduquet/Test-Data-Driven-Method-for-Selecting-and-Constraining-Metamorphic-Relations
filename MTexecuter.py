import math
import struct


class MTexecuter:
    
    def __init__(self, inputA):
        self.inputA = inputA
    
    def mr_PER(self, inputB):

        if type(self.inputA) and type(inputB) != list:
        ## MR1 -> No violation when the output remain constant
            if math.isclose(self.inputA, inputB, rel_tol=1e-9, abs_tol=0):
                return 'Not-violated'

            if not math.isclose(self.inputA, inputB, rel_tol=1e-9):
                return 'Violated'
        
        else:
            self.inputA.sort()
            inputB.sort()
            if not self.inputA == inputB:
                return 'Violated'
            else:
                return 'Not-violated'

    
    def mr_ADD(self, inputB):
        ## MR2 -> No violation when the output increace remain constant
        if type(self.inputA) and type(inputB) != list:
            if math.isclose(self.inputA, inputB, rel_tol=1e-9, abs_tol=0) or self.inputA < inputB:
                return 'Not-violated'
            
            # if math.isclose(self.inputA,self.inputB, rel_tol=1e-9, abs_tol=0) and self.inputA < self.inputB:
            else:
                return 'Violated'

        else:
            auxlist = []
            for i in range(0, len(self.inputA)):
                if math.isclose(float(self.inputA[i]), float(inputB[i]), rel_tol=1e-9, abs_tol=0) or self.inputA < inputB:
                    auxlist.append(True)
            
                # if math.isclose(self.inputA,self.inputB, rel_tol=1e-9, abs_tol=0) and self.inputA < self.inputB:
                else:
                    auxlist.append(False)
            print(auxlist)
            if sum(auxlist) == 0:
                return 'Violated'
            if sum(auxlist) == len(auxlist):
                return 'Not-violated'
            

    
    def mr_MUL(self, inputB):
        ## MR3_MUL -> No violation when the output increace remain constant
        if type(self.inputA) and type(inputB) != list:
            if math.isclose(self.inputA, inputB, rel_tol=1e-9, abs_tol=0) or self.inputA < inputB:
                return 'Not-violated'
            
            # if math.isclose(self.inputA,self.inputB, rel_tol=1e-9, abs_tol=0) and self.inputA < self.inputB:
            else:
                return 'Violated'

    def mr_INV(self, inputB):
        ## MR4 -> No violation when the output decrease or remain constant
        if type(self.inputA) and type(inputB) != list:
            if math.isclose(self.inputA, inputB, rel_tol=1e-9, abs_tol=0) or self.inputA > inputB:
                return 'Not-violated'
            
            # if math.isclose(self.inputA,self.inputB, rel_tol=1e-9, abs_tol=0) and self.inputA < self.inputB:
            else:
                return 'Violated'
    
    def mr_INC(self, inputB):
        ## MR5 -> No violation when the output increase or remain constant
        if type(self.inputA) and type(inputB) != list:
            if math.isclose(self.inputA, inputB, rel_tol=1e-9, abs_tol=0) or self.inputA < inputB:
                return 'Not-violated'
            
            else:
                return 'Violated'

    def mr_EXC(self, inputB):
        ## MR6 -> No violation when the output decrease or remain constant
        if type(self.inputA) and type(inputB) != list:
            if math.isclose(self.inputA, inputB, rel_tol=1e-9, abs_tol=0) or self.inputA > inputB:
                return 'Not-violated'
            
            else:
                return 'Violated'
