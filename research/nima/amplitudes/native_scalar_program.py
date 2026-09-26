"""Compile native current tables to a shared zero/one/factor/sum/product program.

This is the finite expression grammar of NativeAmplitudeResolution.agda.
Compilation reads native declarations/attachments, never cached amplitudes.
Python execution is not thereby an Agda-certified implementation.
"""
from dataclasses import dataclass
from fractions import Fraction as Q
from itertools import product
from native_scalar_recursion import Evaluation

@dataclass(frozen=True)
class Instruction:
    kind: str
    arguments: tuple = ()
    factor: tuple | None = None

@dataclass(frozen=True)
class Program:
    instructions: tuple
    factors: tuple
    root: int

    def validate(self):
        if not self.instructions or self.root != len(self.instructions)-1:
            raise ValueError('invalid program root')
        factors = dict(self.factors)
        if len(factors) != len(self.factors) or any(not isinstance(w,Q) for w in factors.values()):
            raise ValueError('duplicate/nonrational factor')
        used_factors = set()
        for i,step in enumerate(self.instructions):
            if step.kind in ('zero','one','factor'):
                if step.arguments:
                    raise ValueError('unexpected operand')
            elif step.kind in ('sum','product'):
                if len(step.arguments)!=2 or any(type(j) is not int or not 0<=j<i for j in step.arguments):
                    raise ValueError('non-topological operand')
            else:
                raise ValueError('unknown operation')
            if step.kind=='factor':
                if step.factor not in factors:
                    raise ValueError('undeclared factor')
                used_factors.add(step.factor)
            elif step.factor is not None:
                raise ValueError('unexpected factor payload')
        if used_factors != set(factors):
            raise ValueError('unused factor declaration')
        reachable = set()
        todo = [self.root]
        while todo:
            i = todo.pop()
            if i in reachable:
                continue
            reachable.add(i)
            todo.extend(self.instructions[i].arguments)
        if reachable != set(range(len(self.instructions))):
            raise ValueError('unreachable instruction')
        return factors

    def fold(self, zero, one, factor, add, multiply):
        self.validate()
        values = []
        for step in self.instructions:
            if step.kind=='zero': v=zero
            elif step.kind=='one': v=one
            elif step.kind=='factor': v=factor(step.factor)
            elif step.kind=='sum': v=add(*(values[j] for j in step.arguments))
            else: v=multiply(*(values[j] for j in step.arguments))
            values.append(v)
        return values[self.root]

    @property
    def value(self):
        weights = self.validate()
        return self.fold(Q(0),Q(1),weights.__getitem__,lambda a,b:a+b,lambda a,b:a*b)

    @property
    def diagram_count(self):
        return self.fold(0,1,lambda _:1,lambda a,b:a+b,lambda a,b:a*b)

    def diagrams(self, limit=10000):
        if self.diagram_count > limit:
            raise ValueError('diagram expansion budget exceeded')
        return self.fold((),((),),lambda a:((a,),),lambda a,b:a+b,
                         lambda a,b:tuple(x+y for x,y in product(a,b)))


def compile_table(rows, boundary='b'):
    table = Evaluation(rows,boundary)
    steps = [Instruction('zero'),Instruction('one')]
    factors = {}
    roots = {}
    def emit(kind,arguments=(),factor=None):
        steps.append(Instruction(kind,arguments,factor))
        return len(steps)-1
    def current(leaves):
        if len(leaves)==1:
            return 1
        if leaves in roots:
            return roots[leaves]
        declaration = table.groups[leaves]['declaration']
        coefficient = (-table.declaration.coupling if declaration.amputated else
                       table.declaration.coupling/declaration.denominator)
        factors[leaves] = coefficient
        factor_step = emit('factor',factor=leaves)
        subtotal = 0
        for branch in table.choices(leaves):
            term = 1
            for child in branch.children:
                term = emit('product',(term,current(child[2])))
            subtotal = emit('sum',(subtotal,term))
        roots[leaves] = emit('product',(factor_step,subtotal))
        return roots[leaves]
    root = current(table.remaining)
    program = Program(tuple(steps),tuple(factors.items()),root)
    program.validate()
    return program
