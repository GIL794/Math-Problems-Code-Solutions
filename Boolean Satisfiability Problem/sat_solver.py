"""
Boolean Satisfiability Problem (SAT) Solver
===========================================

This implementation solves the Boolean Satisfiability Problem (SAT), one of the most
fundamental and difficult problems in computer science. SAT is the first problem proven
to be NP-complete and serves as the foundation for computational complexity theory.

The SAT Problem: Given a Boolean formula in Conjunctive Normal Form (CNF), determine
if there exists an assignment of truth values to variables that makes the formula true.

Applications:
- Hardware verification and circuit design
- Software verification and model checking
- Artificial intelligence and planning
- Cryptography and cryptanalysis
- Scheduling and resource allocation
"""

from typing import List, Set, Dict, Optional, Tuple
from collections import defaultdict
import random


class CNF:
    """
    Represents a Boolean formula in Conjunctive Normal Form (CNF).
    
    CNF: (x1 OR x2 OR NOT x3) AND (NOT x1 OR x2) AND ...
    Each clause is a disjunction (OR) of literals.
    The entire formula is a conjunction (AND) of clauses.
    """
    
    def __init__(self):
        """Initialise an empty CNF formula."""
        self.clauses: List[List[int]] = []  # Each clause is a list of literals
        self.variables: Set[int] = set()     # Set of all variable indices
        self.var_count: int = 0              # Number of variables
    
    def add_clause(self, literals: List[int]):
        """
        Add a clause to the CNF formula.
        
        Args:
            literals: List of integers representing literals
                     Positive = variable, Negative = negated variable
                     e.g., [1, -2, 3] means (x1 OR NOT x2 OR x3)
        """
        # Remove duplicates and tautologies (clauses with x and NOT x)
        clause_set = set(literals)
        if not any(-lit in clause_set for lit in clause_set):
            self.clauses.append(list(clause_set))
            for lit in clause_set:
                var = abs(lit)
                self.variables.add(var)
                self.var_count = max(self.var_count, var)
    
    def is_satisfied(self, assignment: Dict[int, bool]) -> bool:
        """
        Check if an assignment satisfies the CNF formula.
        
        Args:
            assignment: Dictionary mapping variable index to truth value
        
        Returns:
            True if assignment satisfies all clauses
        """
        for clause in self.clauses:
            clause_satisfied = False
            for lit in clause:
                var = abs(lit)
                value = assignment.get(var, False)
                if lit > 0:
                    if value:
                        clause_satisfied = True
                        break
                else:
                    if not value:
                        clause_satisfied = True
                        break
            if not clause_satisfied:
                return False
        return True
    
    def get_unit_clauses(self, assignment: Dict[int, bool]) -> List[int]:
        """
        Find unit clauses (clauses with exactly one unassigned literal).
        
        Args:
            assignment: Current partial assignment
        
        Returns:
            List of unit literals that must be true
        """
        unit_literals = []
        for clause in self.clauses:
            unassigned = [lit for lit in clause if abs(lit) not in assignment]
            if len(unassigned) == 1:
                unit_literals.append(unassigned[0])
        return unit_literals
    
    def get_pure_literals(self, assignment: Dict[int, bool]) -> List[int]:
        """
        Find pure literals (variables that appear only positively or only negatively).
        
        Args:
            assignment: Current partial assignment
        
        Returns:
            List of pure literals
        """
        positive = defaultdict(int)
        negative = defaultdict(int)
        
        for clause in self.clauses:
            # Skip satisfied clauses
            if any(abs(lit) in assignment and 
                   ((lit > 0 and assignment[abs(lit)]) or 
                    (lit < 0 and not assignment[abs(lit)])) 
                   for lit in clause):
                continue
            
            for lit in clause:
                var = abs(lit)
                if var not in assignment:
                    if lit > 0:
                        positive[var] += 1
                    else:
                        negative[var] += 1
        
        pure = []
        for var in positive:
            if var not in negative:
                pure.append(var)
        for var in negative:
            if var not in positive:
                pure.append(-var)
        
        return pure


class SATSolver:
    """
    SAT Solver using DPLL (Davis-Putnam-Logemann-Loveland) algorithm.
    
    DPLL is a complete, backtracking-based search algorithm for SAT.
    Time Complexity: O(2^n) in worst case (exponential)
    Space Complexity: O(n + m) where n = variables, m = clauses
    """
    
    def __init__(self, cnf: CNF):
        """
        Initialise SAT solver with a CNF formula.
        
        Args:
            cnf: CNF formula to solve
        """
        self.cnf = cnf
        self.assignment: Dict[int, bool] = {}
        self.decision_stack: List[Tuple[int, bool, bool]] = []  # (var, value, is_decision)
    
    def dpll(self) -> Optional[Dict[int, bool]]:
        """
        DPLL algorithm: Recursive backtracking with unit propagation and pure literal elimination.
        
        Returns:
            Satisfying assignment if formula is satisfiable, None otherwise
        """
        # Unit propagation
        while True:
            unit_literals = self.cnf.get_unit_clauses(self.assignment)
            if not unit_literals:
                break
            
            for lit in unit_literals:
                var = abs(lit)
                value = lit > 0
                if var in self.assignment:
                    if self.assignment[var] != value:
                        return None  # Conflict
                else:
                    self.assignment[var] = value
                    self.decision_stack.append((var, value, False))
        
        # Pure literal elimination
        pure_literals = self.cnf.get_pure_literals(self.assignment)
        for lit in pure_literals:
            var = abs(lit)
            if var not in self.assignment:
                self.assignment[var] = lit > 0
                self.decision_stack.append((var, lit > 0, False))
        
        # Check if all clauses are satisfied
        if self.cnf.is_satisfied(self.assignment):
            return self.assignment.copy()
        
        # Check if any clause is falsified
        for clause in self.cnf.clauses:
            if all(abs(lit) in self.assignment and 
                   ((lit > 0 and not self.assignment[abs(lit)]) or 
                    (lit < 0 and self.assignment[abs(lit)])) 
                   for lit in clause):
                return None  # Conflict
        
        # Choose an unassigned variable
        unassigned = [var for var in range(1, self.cnf.var_count + 1) 
                     if var not in self.assignment]
        
        if not unassigned:
            return None  # All variables assigned but formula not satisfied
        
        # Try variable = True
        var = unassigned[0]
        self.assignment[var] = True
        self.decision_stack.append((var, True, True))
        
        result = self.dpll()
        if result is not None:
            return result
        
        # Backtrack
        while self.decision_stack and self.decision_stack[-1][2]:
            var, _, _ = self.decision_stack.pop()
            del self.assignment[var]
        
        # Try variable = False
        self.assignment[var] = False
        self.decision_stack.append((var, False, True))
        
        result = self.dpll()
        if result is not None:
            return result
        
        # Backtrack
        while self.decision_stack and self.decision_stack[-1][2]:
            var, _, _ = self.decision_stack.pop()
            del self.assignment[var]
        
        return None
    
    def solve(self) -> Tuple[bool, Optional[Dict[int, bool]]]:
        """
        Solve the SAT problem.
        
        Returns:
            Tuple of (is_satisfiable, assignment)
        """
        self.assignment = {}
        self.decision_stack = []
        assignment = self.dpll()
        return assignment is not None, assignment


def create_example_1() -> CNF:
    """Create example 1: Simple satisfiable formula."""
    cnf = CNF()
    # (x1 OR x2) AND (NOT x1 OR x2) AND (x1 OR NOT x2)
    cnf.add_clause([1, 2])
    cnf.add_clause([-1, 2])
    cnf.add_clause([1, -2])
    return cnf


def create_example_2() -> CNF:
    """Create example 2: Unsatisfiable formula."""
    cnf = CNF()
    # (x1) AND (NOT x1)
    cnf.add_clause([1])
    cnf.add_clause([-1])
    return cnf


def create_example_3() -> CNF:
    """Create example 3: More complex satisfiable formula."""
    cnf = CNF()
    # (x1 OR x2 OR x3) AND (NOT x1 OR x2) AND (NOT x2 OR x3) AND (NOT x3 OR x1)
    cnf.add_clause([1, 2, 3])
    cnf.add_clause([-1, 2])
    cnf.add_clause([-2, 3])
    cnf.add_clause([-3, 1])
    return cnf


def create_example_4() -> CNF:
    """Create example 4: Pigeonhole principle (unsatisfiable for n+1 pigeons, n holes)."""
    cnf = CNF()
    # 3 pigeons, 2 holes (unsatisfiable)
    # Each pigeon must be in at least one hole
    cnf.add_clause([1, 2])      # Pigeon 1 in hole 1 or 2
    cnf.add_clause([3, 4])      # Pigeon 2 in hole 1 or 2
    cnf.add_clause([5, 6])      # Pigeon 3 in hole 1 or 2
    # No two pigeons in the same hole
    cnf.add_clause([-1, -3])    # Not (P1 in H1 AND P2 in H1)
    cnf.add_clause([-1, -5])    # Not (P1 in H1 AND P3 in H1)
    cnf.add_clause([-3, -5])    # Not (P2 in H1 AND P3 in H1)
    cnf.add_clause([-2, -4])    # Not (P1 in H2 AND P2 in H2)
    cnf.add_clause([-2, -6])    # Not (P1 in H2 AND P3 in H2)
    cnf.add_clause([-4, -6])    # Not (P2 in H2 AND P3 in H2)
    return cnf


def create_example_5() -> CNF:
    """Create example 5: Random 3-SAT instance (difficult)."""
    cnf = CNF()
    # Random 3-SAT with 10 variables, 30 clauses
    random.seed(42)
    for _ in range(30):
        clause = []
        vars_used = set()
        while len(clause) < 3:
            var = random.randint(1, 10)
            if var not in vars_used:
                vars_used.add(var)
                if random.random() < 0.5:
                    clause.append(var)
                else:
                    clause.append(-var)
        cnf.add_clause(clause)
    return cnf


def print_cnf(cnf: CNF):
    """Print CNF formula in human-readable format."""
    print("CNF Formula:")
    print("-" * 70)
    clauses_str = []
    for clause in cnf.clauses:
        literals_str = []
        for lit in sorted(clause, key=abs):
            if lit > 0:
                literals_str.append(f"x{lit}")
            else:
                literals_str.append(f"NOT x{abs(lit)}")
        clauses_str.append("(" + " OR ".join(literals_str) + ")")
    print(" AND ".join(clauses_str))
    print(f"\nVariables: {cnf.var_count}, Clauses: {len(cnf.clauses)}")


def print_assignment(assignment: Optional[Dict[int, bool]], var_count: int):
    """Print variable assignment."""
    if assignment is None:
        print("No satisfying assignment exists (UNSATISFIABLE)")
    else:
        print("\nSatisfying Assignment:")
        print("-" * 70)
        for var in range(1, var_count + 1):
            value = assignment.get(var, False)
            print(f"  x{var} = {value}")


def main():
    """Main function demonstrating SAT solving."""
    
    print("=" * 70)
    print("BOOLEAN SATISFIABILITY PROBLEM (SAT) SOLVER")
    print("=" * 70)
    print("\nSAT is the first problem proven to be NP-complete.")
    print("Solving SAT efficiently would solve thousands of other problems!")
    print("\n" + "=" * 70)
    
    examples = [
        ("Example 1: Simple Satisfiable", create_example_1),
        ("Example 2: Simple Unsatisfiable", create_example_2),
        ("Example 3: Complex Satisfiable", create_example_3),
        ("Example 4: Pigeonhole Principle (Unsatisfiable)", create_example_4),
        ("Example 5: Random 3-SAT (Difficult)", create_example_5),
    ]
    
    for title, create_func in examples:
        print(f"\n{title}")
        print("=" * 70)
        
        cnf = create_func()
        print_cnf(cnf)
        
        solver = SATSolver(cnf)
        is_sat, assignment = solver.solve()
        
        print(f"\nResult: {'SATISFIABLE' if is_sat else 'UNSATISFIABLE'}")
        print_assignment(assignment, cnf.var_count)
    
    print("\n" + "=" * 70)
    print("COMPLEXITY ANALYSIS")
    print("=" * 70)
    print("""
SAT Problem Complexity:
- Time Complexity: O(2^n) in worst case (exponential)
- Space Complexity: O(n + m) where n = variables, m = clauses
- NP-Complete: First problem proven NP-complete (Cook-Levin Theorem, 1971)

Why SAT is Fundamental:
1. NP-Completeness: If SAT can be solved in polynomial time, P = NP
2. Reductions: Thousands of problems reduce to SAT
3. Practical Applications: Used in hardware/software verification
4. Algorithm Development: Basis for modern SAT solvers (CDCL, etc.)

DPLL Algorithm Features:
- Unit Propagation: Automatically assign variables from unit clauses
- Pure Literal Elimination: Assign pure literals to simplify formula
- Backtracking: Systematic search through assignment space
- Complete: Guaranteed to find solution if one exists

Modern SAT Solvers:
- Use Conflict-Driven Clause Learning (CDCL)
- Employ sophisticated heuristics (VSIDS, etc.)
- Can solve instances with millions of variables
- Used in industry for verification and planning
    """)
    
    print("=" * 70)


if __name__ == "__main__":
    main()

