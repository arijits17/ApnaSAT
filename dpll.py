class Clause:
    """
    This class represents a clause in a CNF formula
    """
    
    def  __init__(self, literals=set()):
        """
        Initializes the object for the class Clause with given set of literals and returns None
            args:
                self:
                    type: Clause
                    description: clause in CNF
                    example: Clause({-1, 2, -5}) 
                        represents the clause (not x_1 or x_2 or not x_5)
                        where x_1, x_2, x_5 are the variables in the clause
                literals:
                    type: set of int
                    description: the set of integers representing the literals in the clause
                    example:
                        {-1, 2, -5} represents the set of literals {not x1, x_2, not x_5}
            returns:
                None           
        """
        self.literals = literals
    
    def show(self):
        """
        Prints the set of literals representing the clause and returns None

            args:
                    self:
                        type: Clause
                        description: clause in CNF
                        example: Clause({-1, 2, -5}) 
                            represents the clause (not x_1 or x_2 or not x_5)
                            where x_1, x_2, x_5 are the variables in the clause
            return:
                None                

        """
        print(self.literals)


class Formula:
    """
    This class represents the CNF formula
    """
    def __init__(self, clauses):
        """
        Initializes the object representing the CNF formula given by the set of clauses and returns None
            args:
                self:
                    type: Formula
                    description: a CNF formula represented by a set of clauses
                    example: Formula({Clause({-1, 2, -5}), Clause({-3, -7, 8})})
                clauses:
                    type: set of Clause objects
                    description: set of clauses representing the formula
                    example: {Clause({-1, 2, -5}), Clause({-3, -7, 8})}
            returns:
                None           
        """
        self.clauses = clauses

    def show(self):
        """
        Prints the set of clauses representing the formula and returns None
            args:
                self:
                    type: Formula
                    description: a CNF formula represented by a set of clauses
                    example: Formula({Clause({-1, 2, -5}), Clause({-3, -7, 8})})
            returns:
                None        
        """
        print(clauses)

    def get_variables(self):
        """
        Returns the set of variables involved in a formula
            args:
                self:
                    type: Formula
                    description: a CNF formula represented by a set of clauses
                    example: Formula({Clause({-1, 2, -5}), Clause({-3, -7, 8})})
            returns:
                variables:
                    type: set(int)
                    description: set of integers representing the varibles         
        """
        variables = set()
        for clause in list(clauses):
            for literal in list(clause.literals):
                variable = abs(literal)
                variables.add(variable)        
        return variables

_undefined = -1
from collections import defaultdict
class Assignment:
    """
    Represents a partial assignment for varibles
    """
    def __init__(self, A=defaultdict(lambda:_undefined)):
        """
        Initializes the object representing the partial asignment given by A and returns None
            args:
                self:
                    type: Assignment
                    description: a partial assignment of the variables
                        each varible is assigned a value which is either True, False, or _undefined
                    example:
                        Assigment({1: True, 2: False, 3: True, 4: -1})
                A:
                    type: defaultdict(lambda:_undefined)
                    description: a dictionary representing a partial assignment
                        by default a variable is assigned the value _undefined
                    example:
                        {1: True, 2: False, 3: True}
            returns: 
                None                            
        """
        self.A = A

    def show(self):
        """
        Prints the assignment of all the varibles and returns None
            args:
                self:
                    type: Assignment
                    description: a partial assignment of the variables
                        each varible is assigned a value which is either True, False, or _undefined
                    example:
                        Assigment({1: True, 2: False, 3: True, 4: -1})
            returns:
                None
        """
        print(A)

    def assign(self, variable, value):
        """
        Assigns a value to a given variable and returns None
            args:
                self:
                    type: Assignment
                    description: a partial assignment of the variables
                        each varible is assigned a value which is either True, False, or _undefined
                    example:
                        Assigment({1: True, 2: False, 3: True, 4: -1})
                variable:
                    type: int
                    description: an integer representing the variable
                    example: 3
                value:
                    type:{True,False,_undefined}
                    description: the value to be assigned to the given variable
                        it should be one of three among True, False or _undefined
                    example: True
                        -1
            returns:
                None
        """
        A[variable] = value

class DPLLSolver:
    """
    """

    _sat = True
    _unsat = False
    _undefined = -1
    
    def __init__(self):
        pass


    def unit_propagate(self, formula, assignment):
    
        def get_singleton_literal(clause, assignment):
            literals = clause.literals
            A = assignment.A
            singleton_literal = None
            count = 0
            for literal in list(literals):
                variable = abs(literal)
                if A[variable] == _undefined:
                    singleton_literal = literal
                    count = count + 1
                if count > 1:
                    singleton_literal = None
                    break
            return singleton_literal             


        clauses = formula.clauses
        A = assignment.A

        progress = True
        while progress:
            progress = False
            for clause in list(clauses):
                literal = get_singleton_literal(clause, assignment)
                if literal:
                    variable = abs(literal)
                    A[variable] = bool(int(1+literal/abs(literal)/2))
                    progress = True

        def get_satisfying_status(formula, assignment):
            clauses = formula.clauses
            A = assignment.A
            count = 0

            def is_satisfying(clause, assignment):
                literals = clause.literals
                A = assignment.A

                for literal in list(literals):
                    variable = abs(literal)
                    if A[variable] == True and literal > 0:
                        return True
                    if A[variable] == False and literal < 0:
                        return True
                print(A)
                return False

            status = True
            for clause in list(clauses):
                if not is_satisfying(clause, assignment):
                    status = False
                    return status
            return status        


        status = get_satisfying_status(formula, assignment)
        return status                
        


    def solve(self, formula, assignment=Assignment()):

        def get_next_unassigned_variable(formula, assignment):
            variables = formula.get_variables()
            A = assignment.A
            for variable in list(variables):
                if A[variable] == _undefined:
                    return variable
            return None        

        status = self.unit_propagate(formula,assignment)
        if status == self._sat:
            print("sat")
            return True
        if status == self._unsat:
            print("unsat")
            return False

        x = get_next_unassigned_variable(formula, assignment)
        
        for value in [True, False]:
            assignment.assign(x,value)
            answer = self.solve(formula,assignment)
            if answer:
                return True
            assignment.assign(x,_undefined)
        
        return False


def test_DPLLSolver():
    F_sat = Formula({Clause({1, 2}), Clause({-1, 2})})
    F_unsat = Formula({Clause({1, 2}), Clause({-1, -2}), Clause({1, -2}), Clause({-1, 2})})
    solver = DPLLSolver()

    
    assert solver.solve(F_sat) == True
    print("Successfuly passed F_sat")
    assert solver.solve(F_unsat) == False
    print("Successfuly passed F_unsat")
    print(".")

if __name__ == '__main__':
    test_DPLLSolver()    


        