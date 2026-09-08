#!/usr/bin/env python3
"""Exact dihedral audit of the homogeneous Morse support attachment.

Python 3.10+, standard library only. Reconstructs all 430 corrected cellular
states for each of the three transported occurrence labels. Does not download
or execute repository code. The proof distinguishes the checked linear support
model from unconstructed physical or nonlinear comparison functors.
"""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from itertools import combinations, product
import json
from pathlib import Path
from typing import TypeAlias

D = ('02','03','04','13','14','15','24','25','35')
PLUS = frozenset(('13','15','35'))
MINUS = frozenset(('02','04','24'))
SHORT = PLUS | MINUS
LONG = ('03','14','25')
VARIABLES = tuple('X'+d for d in D) + tuple('t'+d for d in sorted(SHORT)) + tuple('u'+d for d in LONG)
VI = {v:i for i,v in enumerate(VARIABLES)}
NV = len(VARIABLES)
ZERO = (0,)*NV
G = tuple((i,e) for e in (0,1) for i in range(3))
IDENTITY = (0,0)
ROTATION = (1,0)
REFLECTION = (0,1)
PIN = 'd1947b67a60d3e88ba77f4ca60ea02c2a306ee61'
SOURCE = 'research/voevodsky/check_absolute_unlocalized_support_pc.rs'
SOURCE_BLOB = 'b967151cb0ee822e2361b9334a4ab26082c12682'
CHECKS: Counter[str] = Counter()

Monomial: TypeAlias = tuple[int,...]
State: TypeAlias = tuple[tuple[str,...],tuple[str,...],int]
PolynomialVector: TypeAlias = dict[tuple[State,Monomial],int]
Vector: TypeAlias = dict[int,int]
Table: TypeAlias = dict[int,Vector]
Matrix: TypeAlias = list[list[int]]


def check(condition: bool, category: str) -> None:
    if not condition:
        raise AssertionError(category)
    CHECKS[category] += 1


def parity(n: int) -> int:
    return -1 if n % 2 else 1


def crossing(a: str,b: str) -> bool:
    x,y=map(int,a); u,v=map(int,b)
    return x<u<y<v or u<x<v<y


FACES = tuple(f for k in range(4) for f in combinations(D,k)
              if all(not crossing(a,b) for a,b in combinations(f,2)))
FACESET = set(FACES)
STATES = tuple((f,h,k) for f in FACES for j in range(len(f)+1)
               for h in combinations(f,j) for k in (0,1))
STATESET = set(STATES)


def mul_group(g: tuple[int,int],h: tuple[int,int]) -> tuple[int,int]:
    i,e=g; j,f=h
    return ((i+parity(e)*j)%3,e^f)


def inverse_group(g: tuple[int,int]) -> tuple[int,int]:
    return next(h for h in G if mul_group(g,h)==IDENTITY)


def perm_diagonal(d: str,g: tuple[int,int]) -> str:
    i,e=g
    return ''.join(map(str,sorted((parity(e)*int(v)+2*i+2*e)%6 for v in d)))


def perm_list(xs: tuple[str,...],g: tuple[int,int]) -> tuple[tuple[str,...],int]:
    ys=[perm_diagonal(x,g) for x in xs]
    sign=parity(sum(ys[i]>ys[j] for i in range(len(ys)) for j in range(i+1,len(ys))))
    return tuple(sorted(ys)),sign


def action_state(x: State,g: tuple[int,int]) -> tuple[State,int]:
    f,h,k=x
    ff,sf=perm_list(f,g); hh,sh=perm_list(h,g)
    return (ff,hh,k),parity(g[1])*sf*sh


def action_monomial(m: Monomial,g: tuple[int,int]) -> Monomial:
    out=[0]*NV
    for i,n in enumerate(m):
        if n:
            v=VARIABLES[i]
            out[VI[v[0]+perm_diagonal(v[1:],g)]]=n
    return tuple(out)


def var_monomial(*names: str) -> Monomial:
    m=[0]*NV
    for name in names: m[VI[name]]+=1
    return tuple(m)


def survives(m: Monomial) -> bool:
    return not (any(m[VI['X'+d]] for d in PLUS) and any(m[VI['X'+d]] for d in MINUS))


def multiply_monomials(a: Monomial,b: Monomial) -> Monomial | None:
    c=tuple(x+y for x,y in zip(a,b))
    return c if survives(c) else None


def add_term(out: dict,key: object,value: int) -> None:
    if value:
        out[key]=out.get(key,0)+value
        if not out[key]: del out[key]


def state_degree(x: State) -> int:
    f,h,k=x
    return 3-len(f)+len(h)+k


def state_weight(x: State,c: str) -> Monomial:
    f,h,k=x
    a=[0]*NV
    for d in f:a[VI['X'+d]]-=1
    for d in h:
        if d in SHORT:
            a[VI['X'+d]]+=1; a[VI['t'+d]]+=1
        else:a[VI['u'+d]]+=1
    if k:a[VI['X'+c]]+=1
    return tuple(a)


def differential(x: State,c: str) -> PolynomialVector:
    f,h,k=x; out: PolynomialVector={}
    for a in D:
        if a not in f and len(f)<3 and all(not crossing(a,b) for b in f):
            target=(tuple(sorted(f+(a,))),h,k)
            add_term(out,(target,var_monomial('X'+a)),parity(sum(b<a for b in f)))
    for j,a in enumerate(h):
        target=(f,h[:j]+h[j+1:],k)
        mon=var_monomial('X'+a,'t'+a) if a in SHORT else var_monomial('u'+a)
        add_term(out,(target,mon),parity(3-len(f)+j))
    if k:
        add_term(out,((f,h,0),var_monomial('X'+c)),parity(3-len(f)+len(h)))
    return out


def d_vector(v: PolynomialVector,c: str) -> PolynomialVector:
    out: PolynomialVector={}
    for (x,m),coef in v.items():
        for (y,n),a in differential(x,c).items():
            prod=multiply_monomials(m,n)
            if prod is not None:add_term(out,(y,prod),coef*a)
    return out


def action_vector(v: PolynomialVector,g: tuple[int,int]) -> PolynomialVector:
    out: PolynomialVector={}
    for (x,m),coef in v.items():
        y,a=action_state(x,g)
        add_term(out,(y,action_monomial(m,g)),a*coef)
    return out


def support(x: State) -> tuple[bool,bool]:
    f=x[0]
    return frozenset(f) in (PLUS,MINUS),bool(set(f)&SHORT)


def vadd(a: Vector,b: Vector,scale: int=1) -> Vector:
    out=dict(a)
    for i,c in b.items():add_term(out,i,scale*c)
    return out


def apply(table: Table,v: Vector) -> Vector:
    out: Vector={}
    for i,c in v.items():out=vadd(out,table[i],c)
    return out


def retract(original: Table,degree: dict[int,int]) -> dict:
    """Integral elementary cancellations, with complete chain witnesses."""
    d={i:dict(v) for i,v in original.items()}
    p={i:{i:1} for i in original}; inc={i:{i:1} for i in original}
    h={i:{} for i in original}; active=set(original); pivots=[]
    key=lambda i:(-degree[i],i)
    while True:
        pair=None
        for hi in sorted(active,key=key):
            for lo,a in sorted(d[hi].items(),key=lambda v:key(v[0])):
                if abs(a)==1:pair=(lo,hi,a);break
            if pair:break
        if pair is None:break
        lo,hi,a=pair;pivots.append(pair)
        tail={i:b for i,b in d[hi].items() if i!=lo}; ih=inc[hi]
        for j,pj in list(p.items()):
            b=pj.get(lo,0)
            h[j]=vadd(h[j],ih,a*b)
            p[j]=vadd({i:b for i,b in pj.items() if i not in (lo,hi)},tail,-a*b)
        for j in sorted(active-{lo,hi}):
            b=d[j].get(lo,0)
            inc[j]=vadd(inc[j],ih,-a*b)
            d[j]=vadd({i:b for i,b in d[j].items() if i not in (lo,hi)},tail,-a*b)
        for j in (lo,hi):del d[j];del inc[j]
        active-={lo,hi}
    for i,col in original.items():
        check(apply(p,col)==apply(d,p[i]),'projection_chain')
        check(vadd(apply(original,h[i]),apply(h,col))==vadd({i:1},apply(inc,p[i]),-1),'contraction_identity')
    for i,col in d.items():
        check(apply(original,inc[i])==apply(inc,col),'inclusion_chain')
        check(apply(p,inc[i])=={i:1},'retraction_identity')
    check(all(not v for v in d.values()),'residual_differential_zero')
    return {'d':d,'p':p,'i':inc,'h':h,'pivots':pivots,'basis':sorted(d)}


def extract_packet(c: str) -> dict:
    states=[];mons=[]
    for x in STATES:
        m=tuple(-a for a in state_weight(x,c))
        if min(m)>=0 and survives(m):states.append(x);mons.append(m)
    ids={x:i for i,x in enumerate(states)}
    degrees={i:state_degree(x) for i,x in enumerate(states)}
    d={i:{} for i in range(len(states))}
    for i,(x,m) in enumerate(zip(states,mons)):
        for (y,n),a in differential(x,c).items():
            mn=multiply_monomials(m,n)
            if mn is None:continue
            check(y in ids,'homogeneous_component_closed')
            j=ids[y]
            check(mn==mons[j],'homogeneous_coefficient_exact')
            add_term(d[i],j,a)
    supports={'M':set(d),'B':{i for i,x in enumerate(states) if support(x)[1]},
              'V':{i for i,x in enumerate(states) if support(x)[0]}}
    supports['Q']=supports['M']-supports['B']
    rets={}
    for label,sp in supports.items():
        dd={i:{j:a for j,a in d[i].items() if j in sp} for i in sp}
        for col in dd.values():check(not apply(dd,col),'homogeneous_subquotient_d_squared')
        rets[label]=retract(dd,degrees)
    return {'c':c,'states':states,'monomials':mons,'ids':ids,'degrees':degrees,
            'd':d,'supports':supports,'retracts':rets}


def integer_action(src: dict,dst: dict,g: tuple[int,int]) -> Table:
    out={}
    for i,(x,m) in enumerate(zip(src['states'],src['monomials'])):
        y,a=action_state(x,g); j=dst['ids'][y]
        check(action_monomial(m,g)==dst['monomials'][j],'homogeneous_action_weight')
        out[i]={j:a}
    for i,col in src['d'].items():check(apply(dst['d'],out[i])==apply(out,col),'homogeneous_action_chain')
    return out


def induced(src: dict,dst: dict,g: tuple[int,int],label: str) -> Matrix:
    a=integer_action(src,dst,g);r=src['retracts'][label];s=dst['retracts'][label]
    return [[apply(s['p'],apply(a,r['i'][j])).get(i,0) for j in r['basis']] for i in s['basis']]


def zeros(n: int,m: int) -> Matrix:return [[0]*m for _ in range(n)]
def eye(n: int) -> Matrix:return [[int(i==j) for j in range(n)] for i in range(n)]
def transpose(a: Matrix) -> Matrix:return [list(x) for x in zip(*a)]
def mm(a: Matrix,b: Matrix) -> Matrix:
    if len(a[0])!=len(b):raise ValueError('Incompatible matrix dimensions')
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]
def ma(a: Matrix,b: Matrix,scale: int=1) -> Matrix:
    return [[x+scale*y for x,y in zip(row,col)] for row,col in zip(a,b)]
def scale(a: Matrix,c: int) -> Matrix:return [[c*x for x in row] for row in a]
def hcat(a: Matrix,b: Matrix) -> Matrix:return [x+y for x,y in zip(a,b)]
def blockdiag(*matrices: Matrix) -> Matrix:
    n=sum(len(a) for a in matrices);m=sum(len(a[0]) for a in matrices)
    out=zeros(n,m);i=j=0
    for a in matrices:
        for x,row in enumerate(a):out[i+x][j:j+len(row)]=row
        i+=len(a);j+=len(a[0])
    return out


def determinant(a: Matrix) -> int:
    n=len(a)
    if n!=len(a[0]):raise ValueError('Matrix not square')
    b=[[Fraction(x) for x in row] for row in a];result=Fraction(1)
    for j in range(n):
        i=next((i for i in range(j,n) if b[i][j]),None)
        if i is None:return 0
        if i!=j:b[i],b[j]=b[j],b[i];result=-result
        pivot=b[j][j];result*=pivot
        for i in range(j+1,n):
            ratio=b[i][j]/pivot
            b[i]=[x-ratio*y for x,y in zip(b[i],b[j])]
    if result.denominator!=1:raise ArithmeticError('Nonintegral determinant')
    return int(result)


def unimodular_inverse(a: Matrix) -> Matrix:
    n=len(a);b=[[Fraction(x) for x in row+e] for row,e in zip(a,eye(n))]
    for j in range(n):
        i=next((i for i in range(j,n) if b[i][j]),None)
        if i is None:raise ArithmeticError('Singular matrix')
        b[j],b[i]=b[i],b[j];p=b[j][j];b[j]=[x/p for x in b[j]]
        for i in range(n):
            if i!=j:
                p=b[i][j];b[i]=[x-p*y for x,y in zip(b[i],b[j])]
    inv=[row[n:] for row in b]
    if any(x.denominator!=1 for row in inv for x in row):raise ArithmeticError('Matrix is not unimodular')
    return [[int(x) for x in row] for row in inv]


def attachment(packet: dict) -> tuple[Matrix,Matrix]:
    rr=packet['retracts'];u=rr['Q'];v=rr['B'];w=rr['M']
    a=[[apply(v['p'],apply(packet['d'],u['i'][j])).get(i,0) for j in u['basis']] for i in v['basis']]
    p=[[apply(w['p'],v['i'][j]).get(i,0) for j in v['basis']] for i in w['basis']]
    return a,p


def encode_table(table: Table) -> dict:
    return {str(i):[[j,c] for j,c in sorted(col.items())] for i,col in sorted(table.items())}


def group_permutation_matrix() -> dict:
    out={}
    for name,g in [('r',ROTATION),('s',REFLECTION)]:
        a=zeros(6,6)
        for j,h in enumerate(G):a[G.index(mul_group(g,h))][j]=1
        out[name]=a
    return out


def main(output: Path) -> dict:
    CHECKS.clear()
    check(len(FACES)==45,'face_census')
    check(len(STATES)==430,'full_corrected_census')
    orbit=tuple(perm_diagonal('35',(i,0)) for i in range(3))
    check(set(orbit)==PLUS,'occurrence_orbit')
    check(perm_diagonal('35',REFLECTION)=='35','stabilizer_label')
    check(perm_diagonal('35',ROTATION)!='35','no_false_full_group_on_one_label')
    for c in orbit:
        for x in STATES:
            dx=differential(x,c)
            check(all(y in STATESET and state_degree(y)==state_degree(x)-1 for y,m in dx),'full_differential_degree')
            check(not d_vector(dx,c),'full_d_squared')
            for (y,m),coef in dx.items():
                check(tuple(a+b for a,b in zip(state_weight(y,c),m))==state_weight(x,c),'full_multigrading')
                if support(x)[0]:check(support(y)[0],'endpoint_subcomplex')
                if support(x)[1]:check(support(y)[1],'short_boundary_subcomplex')
            for g in G:
                y,sign=action_state(x,g);cc=perm_diagonal(c,g)
                check(support(y)==support(x),'group_support_preservation')
                check(action_vector(dx,g)==d_vector({(y,ZERO):sign},cc),'full_action_chain')
                for h in G:
                    z,a=action_state(x,h);w,b=action_state(z,g)
                    t,e=action_state(x,mul_group(g,h))
                    check(w==t and a*b==e,'full_action_group_law')
    packets={c:extract_packet(c) for c in orbit}
    for p in packets.values():
        check(len(p['states'])==47,'exact_weight_zero_census')
        rr=p['retracts'];deg=p['degrees']
        for label,expected in [('M',{1:3}),('B',{1:5}),('Q',{2:2}),('V',{0:1})]:
            check(dict(Counter(deg[i] for i in rr[label]['basis']))==expected,'homology_and_torsion_free')
    mats={c:attachment(p) for c,p in packets.items()}
    actions={}
    for c,src in packets.items():
        for g in G:
            cc=perm_diagonal(c,g);dst=packets[cc]
            actions[(c,g)]={n:induced(src,dst,g,n) for n in ('M','B','Q','V')}
            aa,pp=mats[c];bb,qq=mats[cc];act=actions[(c,g)]
            check(mm(act['B'],aa)==mm(bb,act['Q']),'attachment_equivariance')
            check(mm(act['M'],pp)==mm(qq,act['B']),'inclusion_equivariance')
    for c in orbit:
        for g,h in product(G,repeat=2):
            cc=perm_diagonal(c,h)
            for n in ('M','B','Q','V'):
                check(mm(actions[(cc,g)][n],actions[(c,h)][n])==actions[(c,mul_group(g,h))][n],'homology_action_group_law')
    A,P=mats['35'];act=actions[('35',REFLECTION)]
    SU,SV,SW=act['Q'],act['B'],act['M']
    check(A==[[-1,0],[-1,0],[0,1],[0,-1],[0,-1]],'derived_attachment_matrix')
    check(P==[[1,-1,0,0,0],[0,0,1,1,0],[0,0,1,0,1]],'derived_inclusion_matrix')
    check(SU==[[-1,1],[0,1]],'source_oriented_filling_action')
    X=[[0,0,0],[-1,0,0],[0,0,1],[0,1,-1],[0,0,0]]
    check(mm(P,A)==zeros(3,2),'exact_sequence_complex')
    check(mm(P,X)==eye(3),'integral_section')
    check(mm(SV,X)==mm(X,SW),'section_reflection_equivariance')
    E=hcat(A,X); Einv=unimodular_inverse(E)
    check(abs(determinant(E))==1,'split_sequence_unimodular')
    check(mm(Einv,E)==eye(5),'split_sequence_inverse')
    L=Einv[:2]
    check(mm(L,A)==eye(2),'attachment_retraction')
    check(ma(mm(A,L),mm(X,P))==eye(5),'split_sequence_identity')
    check(mm(L,SV)==mm(SU,L),'attachment_retraction_equivariance')
    R2=[[0,1],[1,0]]
    BU=[[0,1],[1,1]]
    BW=[[0,1,0],[0,0,1],[1,1,0]]
    BV=hcat(mm(A,BU),mm(X,BW))
    for label,T,S0,expected in [('U',BU,SU,R2),('W',BW,SW,blockdiag(R2,[[1]])),('V',BV,SV,blockdiag(R2,R2,[[1]]))]:
        check(abs(determinant(T))==1,'regular_basis_unimodular')
        check(mm(S0,T)==mm(T,expected),'regular_module_decomposition')
    # Transport the splitting to the other occurrence labels. No averaging.
    sections={};lefts={}
    for i,c in enumerate(orbit):
        a=actions[('35',(i,0))]
        sections[c]=mm(mm(a['B'],X),unimodular_inverse(a['M']))
        lefts[c]=mm(mm(a['Q'],L),unimodular_inverse(a['B']))
        ac,pc=mats[c]
        check(mm(pc,sections[c])==eye(3),'transported_section')
        check(mm(lefts[c],ac)==eye(2),'transported_attachment_retraction')
    for c in orbit:
        for g in G:
            cc=perm_diagonal(c,g);a=actions[(c,g)]
            check(mm(a['B'],sections[c])==mm(sections[cc],a['M']),'all_transported_section_squares')
            check(mm(a['Q'],lefts[c])==mm(lefts[cc],a['B']),'all_transported_retraction_squares')
    # Form the entire three-label orbit. Export group action and splitting.
    orbit_actions={}
    for name,g in [('r',ROTATION),('s',REFLECTION)]:
        orbit_actions[name]={}
        for n,size in [('Q',2),('B',5),('M',3)]:
            mat=zeros(3*size,3*size)
            for j,c in enumerate(orbit):
                i=orbit.index(perm_diagonal(c,g));small=actions[(c,g)][n]
                for x,row in enumerate(small):mat[i*size+x][j*size:(j+1)*size]=row
            orbit_actions[name][n]=mat
    # Regular-module orbit basis generated from a single U vector.
    u_seed=[[0],[1]]
    regcols=[]
    for g in G:
        cc=perm_diagonal('35',g);v=mm(actions[('35',g)]['Q'],u_seed)
        col=[0]*6;offset=2*orbit.index(cc)
        col[offset:offset+2]=[row[0] for row in v];regcols.append(col)
    UG=transpose(regcols)
    check(abs(determinant(UG))==1,'orbit_filling_regular_unimodular')
    regactions=group_permutation_matrix()
    for name in ('r','s'):
        check(mm(orbit_actions[name]['Q'],UG)==mm(UG,regactions[name]),'orbit_filling_regular_action')
    # W = regular G module plus permutation module G/H.
    w_seed=[[0],[0],[1]];fixed_seed=[[0],[1],[0]]
    wcols=[]
    for g in G:
        cc=perm_diagonal('35',g);v=mm(actions[('35',g)]['M'],w_seed)
        col=[0]*9;offset=3*orbit.index(cc);col[offset:offset+3]=[row[0] for row in v];wcols.append(col)
    for i,c in enumerate(orbit):
        v=mm(actions[('35',(i,0))]['M'],fixed_seed)
        col=[0]*9;col[3*i:3*i+3]=[row[0] for row in v];wcols.append(col)
    WG=transpose(wcols)
    check(abs(determinant(WG))==1,'orbit_ambient_basis_unimodular')
    PG=blockdiag(*(mats[c][1] for c in orbit))
    AG=blockdiag(*(mats[c][0] for c in orbit))
    XG=blockdiag(*(sections[c] for c in orbit))
    VG=hcat(mm(AG,UG),mm(XG,WG))
    check(abs(determinant(VG))==1,'orbit_boundary_basis_unimodular')
    for name,g in [('r',ROTATION),('s',REFLECTION)]:
        perm=zeros(3,3)
        for j,c in enumerate(orbit):perm[orbit.index(perm_diagonal(c,g))][j]=1
        Wexpect=blockdiag(regactions[name],perm)
        Vexpect=blockdiag(regactions[name],regactions[name],perm)
        check(mm(orbit_actions[name]['M'],WG)==mm(WG,Wexpect),'orbit_ambient_induced_decomposition')
        check(mm(orbit_actions[name]['B'],VG)==mm(VG,Vexpect),'orbit_boundary_induced_decomposition')
    # C2 periodic resolution checks; exact kernel/image proofs are in the note.
    minus=ma(R2,eye(2),-1);norm=ma(R2,eye(2))
    check(mm(minus,norm)==zeros(2,2) and mm(norm,minus)==zeros(2,2),'periodic_d_squared')
    check(mm(minus,[[1],[1]])==[[0],[0]],'periodic_norm_kernel')
    check(mm(norm,[[-1],[1]])==[[0],[0]],'periodic_difference_kernel')
    check([row[0] for row in norm]==[1,1],'primitive_norm_image')
    check([row[0] for row in minus]==[-1,1],'primitive_difference_image')
    for prime in (2,3,5):
        for v in product(range(prime),repeat=2):
            vm=[[v[0]],[v[1]]]
            norm_zero=all(row[0]%prime==0 for row in mm(norm,vm))
            diff_zero=all(row[0]%prime==0 for row in mm(minus,vm))
            check(norm_zero==((v[0]+v[1])%prime==0),'mod_prime_regular_norm_kernel')
            check(diff_zero==((v[0]-v[1])%prime==0),'mod_prime_regular_difference_kernel')
    serial_packets={}
    for c,p in packets.items():
        rets=p['retracts']
        serial_packets[c]={
            'basis':[{'id':i,'face':list(x[0]),'marks':list(x[1]),'occurrence_bit':x[2],
                       'degree':p['degrees'][i],'coefficient_exponents':list(p['monomials'][i])} for i,x in enumerate(p['states'])],
            'differential':encode_table(p['d']),
            'retractions':{n:{'basis':a['basis'],'inclusion':encode_table(a['i']),
                              'projection':encode_table(a['p']),'homotopy':encode_table(a['h']),
                              'unit_cancellations':[list(q) for q in a['pivots']]} for n,a in rets.items()},
            'attachment':mats[c][0],'inclusion':mats[c][1],
            'equivariant_section':sections[c],'equivariant_attachment_retraction':lefts[c],
            'homology_group_actions':{str(g):actions[(c,g)] for g in G}}
    matrix_data={'packets':serial_packets,'orbit_actions':orbit_actions,'orbit_attachment':AG,
                 'orbit_inclusion':PG,'orbit_section':XG,
                 'regular_bases':{'U':BU,'V':BV,'W':BW,'UG':UG,'VG':VG,'WG':WG}}
    result={
        'schema':'marici.branchA.dihedral_morse_attachment.v1',
        'status':'proved_for_explicit_homogeneous_linear_support_model',
        'repository':'andrey-kokoev/marici','source_commit':PIN,'source_path':SOURCE,'source_blob':SOURCE_BLOB,
        'source_rules':{'rotation':'v -> v+2 modulo 6','reflection':'v -> 2-v modulo 6',
                        'top_orientation':{'r':1,'s':-1},
                        'coefficient_ring':'Z[X_d,t_s,u_l]/(X_even X_odd); u_s=t_s X_s; no coefficient inversion'},
        'variable_order':list(VARIABLES),'occurrence_label_order':list(orbit),
        'full_states_per_label':430,'full_orbit_state_count':1290,
        'fine_degree_zero_states_per_label':47,
        'homology':{'Q':{'2':2},'short_boundary':{'1':5},'full':{'1':3},'endpoints':{'0':1}},
        'fixed_label':'35','stabilizer':'H=<s> of order 2',
        'fixed_label_matrices':{'attachment':A,'inclusion':P,'section':X,'attachment_retraction':L,
                                'S_U':SU,'S_V':SV,'S_W':SW,'split_basis':E,'split_basis_inverse':Einv},
        'integral_H_modules':{'U':'Z[H]','V':'Z[H]^2 + Z_trivial','W':'Z[H] + Z_trivial'},
        'integral_G_modules_on_three_label_orbit':{'U':'Z[G]','V':'Z[G]^2 + Z[G/H]','W':'Z[G] + Z[G/H]'},
        'group_cohomology':{
            'H_positive_U':'0 in every positive degree',
            'H_positive_V_and_W':'Z/2 in positive even degrees; 0 in odd degrees; inclusion is isomorphism',
            'G_positive_U_orbit':'0 in every positive degree',
            'G_positive_V_and_W_orbit':'Z/2 in positive even degrees; 0 in odd degrees; inclusion is isomorphism',
            'sign_twist_control':'regular summands unchanged up to integral isomorphism; residual Z/2 moves to odd degrees on both V and W',
            'induced_attachment_hidden_prime_kernel':False,
            'all_degree_justification':'explicit integral regular-module bases, cyclic periodic resolution, and Shapiro lemma'},
        'scope':{
            'complete_homogeneous_component':True,'polynomial_cutoff_used':False,
            'rational_averaging_used':False,'native_245_state_kernel_contracted':False,
            'full_multidegree_mapping_category_classified':False,
            'all_admissible_spatial_homotopies_constructed':False,
            'physical_H_cond_constructed':False,'physical_Delta_J_value_assigned':False,
            'nonlinear_geometric_realization_asserted':False,
            'newest_B_C_chat_turns_completely_recovered':False},
        'cross_branch_inputs':[
            'equivariant_physical_lift.md (saved 2026-09-06): strict representative vs coherent lift distinction',
            'prime_differentiation.md (saved 2026-09-05): compute actual p-primary transport, not rank analogy',
            'deck_sphere_retraction_falsification.md (saved 2026-09-05): linear equivariance does not establish a geometric stratum map'],
        'counts':dict(sorted(CHECKS.items())), 'total_exact_checks':sum(CHECKS.values()),
        'matrix_sha256':sha256(json.dumps(matrix_data,sort_keys=True,separators=(',',':')).encode()).hexdigest(),
        'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
        'matrices':matrix_data,
        'references':[
            'https://kskedlaya.org/cft/sec_cohom-cyclic.html',
            'https://kskedlaya.org/cft/sec_cohom2.html',
            'https://stacks.math.columbia.edu/tag/0A2H']}
    output.parent.mkdir(parents=True,exist_ok=True)
    output.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:result[k] for k in ('status','total_exact_checks','matrix_sha256','integral_H_modules','integral_G_modules_on_three_label_orbit')},indent=2))
    return result


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path('branch_a_dihedral_morse_attachment_certificate.json'))
    args=parser.parse_args()
    main(args.output)
