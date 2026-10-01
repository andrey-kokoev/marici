"""Exact minimum-Euclidean-norm lifts for a finite rational linear interface.

A maximal independent row subset supplies nonsingular normal equations.
All original constraints are checked, so incompatible requests return None.
"""
from fractions import Fraction as F
from flint import fmpq, fmpq_mat
from biclique_complex import add_scaled, apply


class ExactMinimumLift:
    def __init__(self, columns, row_count):
        self.columns=columns
        self.row_count=row_count
        rows=[{} for _ in range(row_count)]
        for j,column in enumerate(columns):
            for i,v in column.items():
                if v: rows[i][j]=F(v)
        pivots={}; selected=[]
        for i,row in enumerate(rows):
            vector=dict(row)
            while vector:
                p=min(vector)
                if p in pivots:
                    add_scaled(vector,pivots[p],-vector[p])
                else:
                    scale=vector[p]
                    pivots[p]={j:v/scale for j,v in vector.items()}
                    selected.append(i)
                    break
        self.selected=selected
        self.rank=len(selected)
        self.matrix=fmpq_mat([[fmpq(rows[i].get(j,F(0)).numerator,rows[i].get(j,F(0)).denominator)
                               for j in range(len(columns))] for i in selected])
        self.transpose=self.matrix.transpose()
        self.gram=self.matrix*self.transpose

    def solve(self, rhs):
        rhs={i:F(v) for i,v in rhs.items() if v}
        if not set(rhs)<=set(range(self.row_count)): return None
        if not rhs: return {}
        if not self.rank: return None
        b=fmpq_mat([[fmpq(rhs.get(i,F(0)).numerator,rhs.get(i,F(0)).denominator)] for i in self.selected])
        multipliers=self.gram.solve(b)
        vector=self.transpose*multipliers
        result={i:F(str(vector[i,0])) for i in range(len(self.columns)) if vector[i,0]}
        return result if apply(self.columns,result)==rhs else None
