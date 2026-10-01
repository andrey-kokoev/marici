"""Exact conservative sewing/record exchange for the four-packet trial.

Reuses the prior orthogonal carrier-record swap; adapter and schedule are
explicit new choices, not source-selected particle dynamics.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from pathlib import Path
import json
from check_four_packet_cycle import BASIS, UNIT, J, MAX_DEPTH, basis_product, rotate, sew, tensor, norm2


def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def scale(a,c): return tuple(c*x for x in a)
def basis(n): return tuple(tuple(F(i==j) for i in range(n)) for j in range(n))
ZERO4=(F(0),)*4
ZERO16=(F(0),)*16

def readout(t):
    if len(t)!=16: raise ValueError('Sixteen record slots required')
    return scale(sew(t),F(1,2))

def lift(x):
    if len(x)!=4: raise ValueError('Four carrier coefficients required')
    return tuple(F(basis_product(i,j)[0],2)*x[basis_product(i,j)[1]]
                 for i in range(4) for j in range(4))

def left_rotate(t):
    signs=(1,-1,-1,1)
    return tuple(signs[i]*t[4*i+j] for i in range(4) for j in range(4))

def exchange(x,t):
    a=readout(t)
    return a,add(lift(x),sub(t,lift(a)))

def cycle(x,t):
    return exchange(rotate(x),left_rotate(t))

def inverse_cycle(x,t):
    a,b=exchange(x,t)
    return rotate(a),left_rotate(b)

def budget(x,t): return norm2(x)+norm2(t)

def decompose(t):
    a=readout(t);b=readout(left_rotate(t))
    k=sub(sub(t,lift(a)),left_rotate(lift(b)))
    return a,b,k

def flatten(x,t): return x+t

def full_cycle(v): return flatten(*cycle(v[:4],v[4:]))

def matrix_of(fn,n):
    cols=[fn(e) for e in basis(n)]
    return tuple(tuple(cols[j][i] for j in range(n)) for i in range(n))

def transpose(m): return tuple(zip(*m))

def mm(a,b):
    cols=transpose(b)
    return tuple(tuple(sum((x*y for x,y in zip(row,col) if x and y),F(0))
                       for col in cols) for row in a)

def rank(rows):
    rows=[list(r) for r in rows];pivot=0
    for col in range(len(rows[0])):
        at=next((i for i in range(pivot,len(rows)) if rows[i][col]),None)
        if at is None: continue
        rows[pivot],rows[at]=rows[at],rows[pivot]
        d=rows[pivot][col];rows[pivot]=[v/d for v in rows[pivot]]
        for i in range(len(rows)):
            if i!=pivot and rows[i][col]:
                d=rows[i][col];rows[i]=[a-d*b for a,b in zip(rows[i],rows[pivot])]
        pivot+=1
        if pivot==len(rows): break
    return pivot

@dataclass(frozen=True)
class RetainedState:
    carrier: tuple
    record: tuple
    depth: int=0
    parent: 'RetainedState | None'=None

    def advance(self):
        if self.depth>=MAX_DEPTH:
            raise ValueError('Retained depth 3 reached; no history was erased')
        x,t=cycle(self.carrier,self.record)
        return RetainedState(x,t,self.depth+1,self)


def main():
    # Exact operator identities, not floating-point trajectory evidence.
    for x in BASIS:
        assert readout(lift(x))==x
        assert norm2(lift(x))==norm2(x)
        assert readout(left_rotate(lift(x)))==ZERO4
    for t in basis(16):
        assert left_rotate(left_rotate(t))==t
        for x in BASIS:
            y,u=exchange(x,t)
            assert exchange(y,u)==(x,t)
            assert budget(y,u)==budget(x,t)
        a,b,k=decompose(t)
        assert add(add(lift(a),left_rotate(lift(b))),k)==t
        assert readout(k)==readout(left_rotate(k))==ZERO4
        assert norm2(t)==norm2(a)+norm2(b)+norm2(k)
    # Raw Clifford sewing cannot be the output block of an isometry.
    assert norm2(sew(lift(UNIT)))==4 and norm2(lift(UNIT))==1
    large=scale(UNIT,F(2))
    assert norm2(sew(tensor(rotate(large),large)))==16 > norm2(large)==4
    U=matrix_of(full_cycle,20);identity=basis(20)
    assert mm(transpose(U),U)==identity
    power=identity;orders=[]
    for n in range(1,7):
        power=mm(U,power)
        if power==identity: orders.append(n)
    assert orders==[6]
    fixed_dimension=20-rank([sub(a,b) for a,b in zip(U,identity)])
    assert fixed_dimension==6
    observers=[readout(t)+readout(left_rotate(t)) for t in basis(16)]
    assert rank(transpose(observers))==8
    # A direction invisible to multiplication returns directly to the carrier.
    hidden=left_rotate(lift(UNIT))
    assert readout(hidden)==ZERO4 and norm2(hidden)==1
    assert cycle(ZERO4,hidden)==(UNIT,ZERO16)
    # An eight-dimensional remainder remains invisible under this schedule.
    dark=next(decompose(t)[2] for t in basis(16) if norm2(decompose(t)[2]))
    assert cycle(ZERO4,dark)[0]==ZERO4
    assert readout(left_rotate(dark))==ZERO4
    # Nontrivial balanced fixed preparation, not an attractor or selected state.
    balanced=add(lift(UNIT),left_rotate(lift(UNIT)))
    assert cycle(UNIT,balanced)==(UNIT,balanced)
    seeds={'empty_records':(UNIT,ZERO16),
           'hidden_record_return':(ZERO4,hidden),
           'balanced_fixed':(UNIT,balanced),
           'squared_preparation':((F(1,4),F(1,8),F(1,8),F(1,8)),None),
           'dark_record':(ZERO4,dark), 'bivector_empty':(J,ZERO16)}
    trajectories={}
    for name,(x,t) in seeds.items():
        if t is None: t=tensor(rotate(x),x)
        state=RetainedState(x,t);B=budget(x,t);rows=[]
        for n in range(4):
            a,b,k=decompose(state.record)
            rows.append({'depth':state.depth,'carrier':[str(v) for v in state.carrier],
                         'carrier_budget':str(norm2(state.carrier)),
                         'record_budget':str(norm2(state.record)), 'total_budget':str(B)})
            assert budget(state.carrier,state.record)==B
            y,u=cycle(state.carrier,state.record)
            aa,bb,kk=decompose(u)
            assert y==b and aa==rotate(state.carrier) and bb==a and kk==left_rotate(k)
            assert inverse_cycle(y,u)==(state.carrier,state.record)
            if n<3:
                previous=state;state=state.advance();assert state.parent is previous
        try: state.advance()
        except ValueError: pass
        else: raise AssertionError('Depth limit not enforced')
        # Perturbation distances, not merely each trajectory norm, are preserved.
        perturbed=add(flatten(x,t),scale(basis(20)[7],F(1,100)))
        assert norm2(sub(full_cycle(perturbed),full_cycle(flatten(x,t))))==F(1,10000)
        trajectories[name]=rows
    report={'status':'passed','classification':'conditional finite conservative record-feedback adapter; not proton',
            'carrier_dimension':4,'record_dimension':16,'coisometry':'C=Clifford_sewing/2',
            'update':'x_next=C L t; t_next=C^T R x+(I-C^T C)Lt',
            'invariant':'||x||²+||t||²','operator_order':6,'fixed_space_dimension':fixed_dimension,
            'readable_record_dimension':8,'permanently_unread_record_dimension':8,
            'stability':'distance-preserving; neutral, not attracting',
            'retained_trajectory_depth':MAX_DEPTH,'trajectories':trajectories,
            'boundaries':['Replaces repeated nonlinear squaring with closed fixed-bank exchange',
                          'Tensor seed is prepared once; preparation budget is supplied',
                          'No localization, binding energy, spin, charge, color, baryon number or physical mass']}
    dest=Path(__file__).resolve().parents[1]/'results'/'four-packet-record-feedback.json'
    dest.write_text(json.dumps(report,indent=2)+'\n')
    print('PASS: exact 20D orthogonality, sixth-order return, inverse, 6D fixed space, record feedback, budget and depth-3 histories. Neutral persistence, not proton binding.')

if __name__=='__main__': main()
