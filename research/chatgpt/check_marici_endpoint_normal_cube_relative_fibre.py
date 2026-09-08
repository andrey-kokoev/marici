#!/usr/bin/env python3
"""Exact endpoint-sensitive short-normal continuation of Marici's target.

Python 3.10+, standard library only. Reconstructs the pinned loaded target,
computes all 64 short-normal support grades and their actual multiplication
cube, identifies the fully endpoint-framed relative fibre with B[-1], and
computes its stabilizer-equivariant homotopy groups by normalized integral
bar cochains. No normalization-sheet physical comparison is assumed.

Common source reconstruction and integral SDR helpers are included here
from check_marked_normal_q_extension.py to make this checker self-contained.
"""
from __future__ import annotations
import argparse
from collections import Counter
from fractions import Fraction
from itertools import combinations, product
import json
from pathlib import Path
from typing import TypeAlias

Diag: TypeAlias = tuple[int, int]
Face: TypeAlias = tuple[Diag, ...]
Cell: TypeAlias = tuple[Face, Face]
Exp: TypeAlias = tuple[int, ...]
Group: TypeAlias = tuple[int, int]
Vec: TypeAlias = dict
COMMIT = 'd1947b67a60d3e88ba77f4ca60ea02c2a306ee61'
SOURCES = {
 'research/voevodsky/check_global_k6_koszul_cech_promotion.rs':
 'e972b69d0e2b1b0a0aee5e0a027c8216bcace3e8',
 'research/voevodsky/check_two_endpoint_tate_carrier.rs':
 '0147e2e42dafac0da7289c571cb0331b51338be1',
 'src/ledger/20260815-143 Two-Endpoint Road Carrier and the Loaded Conductor Cospan Blocker.md':
 '02cedbb15dd385a75bab759dfcdb4daa28bd3b3c',
 'research/voevodsky/check_dp6_endpoint_q_mapping_fiber.rs':
 '592811b138855554c921dcf4269581632e8f0050',
}
COUNT: Counter[str] = Counter()
G = tuple(product(range(3), range(2)))
ZERO: Exp = (0,) * 18

def check(condition: bool, name: str) -> None:
    if not condition:
        raise AssertionError(name)
    COUNT[name] += 1

def diag(a: int, b: int) -> Diag:
    return tuple(sorted((a % 6, b % 6)))

def cross(a: Diag, b: Diag) -> bool:
    x, y = a; u, v = b
    return x < u < y < v or u < x < v < y

DIAGONALS = tuple((i,j) for i in range(6) for j in range(i+1,6)
                  if j-i not in (1,5))
SHORTS = tuple(diag(i,i+2) for i in range(6))
LONGS = tuple(diag(i,i+3) for i in range(3))
IX = {d:i for i,d in enumerate(SHORTS+LONGS)}
FACES = tuple(f for k in range(4) for f in combinations(DIAGONALS,k)
              if all(not cross(a,b) for a,b in combinations(f,2)))
CELLS = tuple((f,h) for f in FACES for k in range(len(f)+1)
              for h in combinations(f,k))
VP = tuple(sorted(SHORTS[i] for i in (1,3,5)))
VM = tuple(sorted(SHORTS[i] for i in (0,2,4)))
V = {c for c in CELLS if c[0] in (VP,VM)}
B = {c for c in CELLS if any(d in SHORTS for d in c[0])}

def add(*vectors: Vec) -> Vec:
    out = {}
    for vector in vectors:
        for key,c in vector.items():
            out[key] = out.get(key,0)+c
            if not out[key]:
                del out[key]
    return out

def scale(vector: Vec, coefficient: int) -> Vec:
    return {key:coefficient*c for key,c in vector.items() if coefficient*c}

def exp(data: dict[int,int]) -> Exp:
    return tuple(data.get(i,0) for i in range(18))

def eadd(a: Exp, b: Exp) -> Exp:
    return tuple(x+y for x,y in zip(a,b))

def weight(f: Face) -> Exp:
    return exp({**{IX[d]:1 for d in f}, **{IX[d]+9:-1 for d in f}})

def shift(cell: Cell) -> Exp:
    return tuple(-n for n in weight(cell[0]))

def legal(cell: Cell, coefficient: Exp) -> bool:
    loc = {IX[d] for d in cell[0] if d not in cell[1]}
    return (all(n>=0 for n in coefficient[:9]) and
            all(n>=0 or j in loc for j,n in enumerate(coefficient[9:])))

def degree(cell: Cell) -> int:
    return 3-len(cell[0])+len(cell[1])

def boundary(cell: Cell) -> dict[tuple[Cell,Exp],int]:
    f,h = cell; result = {}
    for a in DIAGONALS:
        if a not in f and all(not cross(a,b) for b in f):
            t = (tuple(sorted(f+(a,))),h)
            result[(t,exp({IX[a]:1,IX[a]+9:-1}))] = (-1)**sum(b<a for b in f)
    for i,a in enumerate(h):
        t = (f,tuple(b for b in h if b!=a))
        result[(t,ZERO)] = (-1)**(3-len(f)+i)
    return result

BD = {c:boundary(c) for c in CELLS}

def apply_bd(vector: dict[tuple[Cell,Exp],int]):
    out = {}
    for (c,m),a in vector.items():
        out = add(out,{(t,eadd(m,n)):a*b for (t,n),b in BD[c].items()})
    return out

def mul(g: Group, h: Group) -> Group:
    return ((g[0]+(-1)**g[1]*h[0])%3,(g[1]+h[1])%2)

def vertex(a: int, g: Group) -> int:
    # Actual closed-endpoint carrier reflection, not the older 2-v reflection.
    return (2*g[0]+(a if g[1]==0 else 3-a))%6

def image_diag(d: Diag, g: Group) -> Diag:
    return diag(vertex(d[0],g),vertex(d[1],g))

def image_face(f: Face, g: Group) -> Face:
    return tuple(sorted(image_diag(d,g) for d in f))

def permutation_sign(f: Face, g: Group) -> int:
    ordered = [image_diag(d,g) for d in f]
    return (-1)**sum(a>b for i,a in enumerate(ordered) for b in ordered[i+1:])

def act_cell(c: Cell, g: Group) -> tuple[Cell,int]:
    f,h = c
    sign = (-1)**g[1]*permutation_sign(f,g)*permutation_sign(h,g)
    return (image_face(f,g),image_face(h,g)),sign

def act_exp(m: Exp, g: Group) -> Exp:
    out = [0]*18
    for d,i in IX.items():
        j = IX[image_diag(d,g)]
        out[j] = m[i];out[j+9] = m[i+9]
    return tuple(out)

def act_loaded(vector, g):
    out = {}
    for (c,m),a in vector.items():
        t,s = act_cell(c,g)
        out = add(out,{(t,act_exp(m,g)):a*s})
    return out

# At the forced zero multidegree only unmarked states are allowed.
C0 = tuple(c for c in CELLS if legal(c,weight(c[0])))

def cellular_boundary(f: Face) -> dict[Face,int]:
    return {t[0]:a for (t,_),a in BD[(f,())].items()}

def act_chain(vector: dict[Face,int], g: Group) -> dict[Face,int]:
    return {image_face(f,g):a*(-1)**g[1]*permutation_sign(f,g)
            for f,a in vector.items()}

def apply_cellular(vector: dict[Face,int], support: set[Face]) -> dict[Face,int]:
    out = {}
    for f,a in vector.items():
        out=add(out,{t:a*b for t,b in cellular_boundary(f).items() if t in support})
    return out

def unit_cancel(support: set[Face]) -> tuple[dict[int,int],list]:
    """Integral elementary chain contractions; every pivot is a signed unit."""
    d = {f:{t:a for t,a in cellular_boundary(f).items() if t in support}
         for f in sorted(support,key=lambda x:(len(x),x))}
    pivots=[]
    while True:
        chosen = next(((b,a,c) for b in d for a,c in d[b].items() if abs(c)==1),None)
        if chosen is None:
            break
        b,a,p=chosen; db=dict(d[b]);pivots.append((b,a,p))
        for x in list(d):
            if x in (a,b):
                continue
            coefficient = d[x].get(a,0)
            if coefficient:
                d[x]=add(d[x],scale(db,-coefficient*p))
            d[x].pop(a,None);d[x].pop(b,None)
        del d[a];del d[b]
        for x in d:
            square={}
            for y,coefficient in d[x].items():
                square=add(square,scale(d[y],coefficient))
            check(not square,'integral_cancellation_preserves_d_squared')
    check(not any(d.values()),'integral_unit_contraction_complete')
    ranks = dict(Counter(3-len(f) for f in d))
    return ranks,pivots

def solve_integral(matrix: list[list[int]], rhs: list[int]) -> list[int]:
    """Exact rational elimination; reject any nonintegral returned witness."""
    if not matrix:
        raise ValueError('Empty matrix')
    rows=len(matrix);cols=len(matrix[0]);a=[list(map(Fraction,row))+[Fraction(b)]
                                         for row,b in zip(matrix,rhs)]
    pivots=[];rr=0
    for col in range(cols):
        j=next((j for j in range(rr,rows) if a[j][col]),None)
        if j is None:
            continue
        a[rr],a[j]=a[j],a[rr];p=a[rr][col]
        a[rr]=[v/p for v in a[rr]]
        for j in range(rows):
            if j!=rr and a[j][col]:
                p=a[j][col];a[j]=[x-p*y for x,y in zip(a[j],a[rr])]
        pivots.append((rr,col));rr+=1
        if rr==rows:
            break
    if any(not any(row[:cols]) and row[cols] for row in a):
        raise ValueError('Inconsistent exact chain equation')
    result=[Fraction(0)]*cols
    for row,col in pivots:
        result[col]=a[row][cols]
    if any(v.denominator!=1 for v in result):
        raise ValueError('This elimination did not produce an integral witness')
    result=[int(v) for v in result]
    check([sum(x*y for x,y in zip(row,result)) for row in matrix]==rhs,
          'integral_linear_witness_verified')
    return result

def short_name(d: Diag) -> str:
    return 'x'+str(SHORTS.index(d)) if d in SHORTS else 'D'+str(d[0])+str(d[1])

def face_name(f: Face) -> str:
    return 'T' if not f else ','.join(short_name(d) for d in f)

def vec_json(v):
    return {face_name(f):a for f,a in sorted(v.items())}


def linear(table, vector):
    result={}
    for key,value in vector.items():
        result=add(result,scale(table[key],value))
    return result


def cell_name(c):
    f,h=c
    return face_name(f)+(('['+','.join(short_name(d) for d in h)+']') if h else '')


def encoded_vector(v):
    return {cell_name(c):a for c,a in sorted(v.items(),key=lambda kv:cell_name(kv[0]))}


def matrix_rank(a):
    if not a:return 0
    work=[list(map(Fraction,row)) for row in a];rr=0
    for j in range(len(work[0])):
        hit=next((i for i in range(rr,len(work)) if work[i][j]),None)
        if hit is None:continue
        work[rr],work[hit]=work[hit],work[rr]
        c=work[rr][j];work[rr]=[x/c for x in work[rr]]
        for i in range(len(work)):
            if i!=rr and work[i][j]:
                c=work[i][j];work[i]=[x-c*y for x,y in zip(work[i],work[rr])]
        rr+=1
        if rr==len(work):break
    return rr


class Grade:
    def __init__(self, normals, support='K'):
        self.normals=tuple(normals)
        self.gamma=exp({IX[d]+9:1 for d in normals})
        predicate={
          'K':lambda c:True, 'V':lambda c:c in V, 'B':lambda c:c in B,
          'E':lambda c:c not in V, 'BV':lambda c:c in B and c not in V,
          'Q':lambda c:c not in B}[support]
        self.cells=tuple(c for c in CELLS if
                         legal(c,eadd(self.gamma,weight(c[0]))) and predicate(c))
        self.set=set(self.cells)
        self.d={c:{t:a for (t,m),a in BD[c].items() if t in self.set} for c in self.cells}
        for c in self.cells:
            for (t,m),a in BD[c].items():
                check(legal(t,eadd(self.gamma,weight(t[0]))),'every_grade_closed_under_d')
                check(eadd(eadd(self.gamma,weight(c[0])),m)==eadd(self.gamma,weight(t[0])),
                      'every_graded_incidence_retains_actual_monomial')
            check(not linear(self.d,self.d[c]),'graded_d_squared')
        self.support=support

    def act(self,v,g):
        out={}
        for c,a in v.items():
            t,s=act_cell(c,g)
            check(t in self.set,'action_preserves_invariant_grade')
            out=add(out,{t:a*s})
        return out

    def reduce(self):
        """Signed-unit cancellations, retaining P,I,H and checking the SDR."""
        original=self.d;origcells=self.cells
        current={c:dict(v) for c,v in original.items()}
        P={c:{c:1} for c in origcells}
        I={c:{c:1} for c in origcells}
        H={c:{} for c in origcells};pivots=[]
        while True:
            hit=next(((b,a,u) for b in current for a,u in current[b].items() if abs(u)==1),None)
            if hit is None:break
            b,a,u=hit;db=dict(current[b]);pivots.append((b,a,u))
            survive=tuple(c for c in current if c not in (a,b))
            pa={c:{c:1} for c in survive}
            pa[b]={};pa[a]={t:-u*n for t,n in db.items() if t!=a}
            inc={c:add({c:1},{b:-u*current[c].get(a,0)}) for c in survive}
            # add() discards zero entries, including the possible zero coefficient of b.
            inc={c:{t:n for t,n in v.items() if n} for c,v in inc.items()}
            for c in origcells:
                coefficient=P[c].get(a,0)
                if coefficient:H[c]=add(H[c],scale(I[b],u*coefficient))
            P={c:linear(pa,v) for c,v in P.items()}
            I={c:linear(I,v) for c,v in inc.items()}
            current={c:linear(pa,linear(current,inc[c])) for c in survive}
            for c,v in current.items():
                check(not linear(current,v),'unit_cancellations_preserve_complex')
        check(not any(current.values()),'integral_reduction_has_zero_residual_differential')
        self.P,self.I,self.H=P,I,H
        self.survivors=tuple(current)
        self.homology=dict(sorted(Counter(degree(c) for c in current).items()))
        self.pivots=pivots
        for c in origcells:
            check(not linear(P,original[c]),'projection_to_homology_chain_map')
            lhs=add(linear(original,H[c]),linear(H,original[c]))
            rhs=add({c:1},scale(linear(I,P[c]),-1))
            check(lhs==rhs,'complete_integral_deformation_retraction')
        for c in self.survivors:
            check(not linear(original,I[c]),'homology_section_is_closed')
            check(linear(P,I[c])=={c:1},'projection_section_identity')
        return self.homology

    def matrix(self,g):
        cols=[linear(self.P,self.act(self.I[c],g)) for c in self.survivors]
        return [[col.get(r,0) for col in cols] for r in self.survivors]


def mulmat(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def mulvec(a,v):
    return [sum(x*y for x,y in zip(row,v)) for row in a]



def mask_normals(mask):
    return tuple(SHORTS[i] for i in range(6) if (mask>>i)&1)


def normal_mask(ds):
    selected=set(ds)
    return sum(1<<i for i,d in enumerate(SHORTS) if d in selected)


def residual_complex(remaining):
    cs=set(remaining)
    faces=tuple(f for f in FACES if f and set(f)<=cs)
    support=set(faces)
    d={f:{t:n for t,n in cellular_boundary(f).items() if t in support}
       for f in faces}
    return faces,d


def integral_smith_unit_then_two(matrix, ncols):
    """Exact unimodular elimination. Fails rather than guessing other Smith cases."""
    a=[row[:] for row in matrix];m=len(a);n=ncols;k=0
    while k<min(m,n):
        pos=next(((i,j) for i in range(k,m) for j in range(k,n)
                  if abs(a[i][j])==1),None)
        if pos is None:break
        i,j=pos;a[k],a[i]=a[i],a[k]
        for row in a:row[k],row[j]=row[j],row[k]
        if a[k][k]<0:a[k]=[-x for x in a[k]]
        for i in range(m):
            if i!=k and a[i][k]:
                c=a[i][k];a[i]=[x-c*y for x,y in zip(a[i],a[k])]
        for j in range(n):
            if j!=k and a[k][j]:
                c=a[k][j]
                for i in range(m):a[i][j]-=c*a[i][k]
        k+=1
    rem=[row[k:] for row in a[k:]]
    nonzero=[(i,j,x) for i,row in enumerate(rem) for j,x in enumerate(row) if x]
    if not nonzero:return [1]*k
    # In this calculation every non-unit residual is a single signed-2 column.
    check(len({j for i,j,x in nonzero})==1,'remaining_smith_block_single_column')
    check(all(abs(x)==2 for i,j,x in nonzero),'remaining_smith_entries_exactly_two')
    return [1]*k+[2]


def bar_model(remaining, subgroup):
    """Only cohomology degrees 0 and 1 are requested; rows through degree 2
    suffice. Total chain degree is 1 - simplicial degree - group degree.
    This is the normalized bar construction, not a truncated group sample.
    """
    faces,cd=residual_complex(remaining)
    fs=set(faces);others=tuple(g for g in subgroup if g!=(0,0))
    basis={n:[] for n in (-1,0,1)}
    for p in range(3):
        for args in product(others,repeat=p):
            for f in faces:
                n=2-len(f)-p
                if n in basis:basis[n].append((p,args,f))
    def differential(key):
        p,args,f=key
        out={(p,args,t):(-1)**p*a for t,a in cd[f].items()}
        if p<2:
            for aa in product(others,repeat=p+1):
                if aa[1:]==args:
                    fg=image_face(f,aa[0]);s=(-1)**aa[0][1]*permutation_sign(f,aa[0])
                    out=add(out,{(p+1,aa,fg):s})
                for i in range(1,p+1):
                    mid=aa[:i-1]+(mul(aa[i-1],aa[i]),)+aa[i+1:]
                    if mid==args:out=add(out,{(p+1,aa,f):(-1)**i})
                if aa[:-1]==args:out=add(out,{(p+1,aa,f):(-1)**(p+1)})
        return out
    columns={n:[differential(c) for c in basis[n]] for n in (0,1)}
    tables={n:dict(zip(basis[n],columns[n])) for n in (0,1)}
    for v in columns[1]:
        check(not linear(tables[0],v),'integral_bar_total_d_squared')
    matrices={n:[[col.get(row,0) for col in columns[n]] for row in basis[n-1]]
              for n in (0,1)}
    ranks={n:matrix_rank(matrices[n]) if matrices[n] and basis[n] else 0 for n in (0,1)}
    smith=integral_smith_unit_then_two(matrices[1],len(basis[1]))
    check(len(smith)==ranks[1],'smith_rank_matches_exact_rational_rank')
    pi0_free=len(basis[0])-ranks[0]-ranks[1]
    pi1=len(basis[1])-ranks[1]
    check(pi0_free>=0 and pi1>=0,'bar_homology_ranks_nonnegative')
    # The transported parity class is eta(g) times the sum of all remaining
    # short vertices. This is the actual projection of d_E omega.
    parity={(1,(g,),f):g[1] for g in others for f in faces if len(f)==1 and g[1]}
    check(not linear(tables[0],parity),'transported_parity_is_bar_cocycle')
    minus_vertex_sum={(0,(),f):-1 for f in faces if len(f)==1}
    check(linear(tables[1],minus_vertex_sum)==scale(parity,2),
          'transported_parity_double_explicit_boundary')
    # Finite exact search of the integral half-sum problem suffices here:
    # any solution differs by an invariant function on components. The proof
    # classifies those functions; candidate values 0,-1 choose a bipartition.
    vertices=[f for f in faces if len(f)==1]
    witness=None
    for coeff in product((0,-1),repeat=len(vertices)):
        v={(0,(),f):a for f,a in zip(vertices,coeff) if a}
        if linear(tables[1],v)==parity:
            witness=v;break
    nonzero=bool(parity) and witness is None
    check(nonzero==bool([a for a in smith if a>1]),
          'parity_accounts_for_entire_torsion_component')
    result={
        'stabilizer':[list(g) for g in subgroup],
        'remaining_short_labels':[short_name(d) for d in remaining],
        'residual_simplex_counts':dict(sorted(Counter(len(f)-1 for f in faces).items())),
        'pi0_free_rank':pi0_free,'pi0_torsion':[a for a in smith if a>1],
        'pi1_free_rank':pi1,'pi_n_ge_2':0,
        'transported_parity_nonzero':nonzero,
        'bar_chain_ranks':{str(n):len(basis[n]) for n in basis},
        'bar_differential_ranks':{str(n):r for n,r in ranks.items()},
        'bar_boundary_smith_factors':smith,
        'parity_nullhomotopy':None if witness is None else [
            {'face':face_name(k[2]),'coefficient':a} for k,a in witness.items()],
    }
    return result


def verify_endpoint_fibre(K,Vg,E,Bg,Q):
    """Fibre of E[-1] -> V + Q[-1], with full endpoint complexes, not scalars.
    The explicit signed-unit contraction retracts it onto B[-1].
    """
    dc={};inc={};proj={};hom={}
    for c in E.cells:
        key=('e',c)
        out={('e',t):-a for t,a in E.d[c].items()}
        out=add(out,{('v',t):-a for t,a in K.d[c].items() if t in Vg.set})
        if c in Q.set:out[('h',c)]=-1
        dc[key]=out
        proj[key]={c:1} if c in Bg.set else {}
        hom[key]={}
    for c in Vg.cells:
        key=('v',c);dc[key]={('v',t):-a for t,a in Vg.d[c].items()}
        proj[key]={c:1};hom[key]={}
    for c in Q.cells:
        key=('h',c)
        dc[key]={('h',t):a for t,a in Q.d[c].items()}
        crosspart={t:a for t,a in K.d[c].items() if t in Bg.set}
        check(not(set(crosspart)&Vg.set),'generic_to_endpoint_direct_differential_zero')
        proj[key]=scale(crosspart,-1)
        hom[key]={('e',c):-1}
    for c in Bg.cells:
        inc[c]={(('v' if c in Vg.set else 'e'),c):1}
    db={c:scale(v,-1) for c,v in Bg.d.items()}
    for c in dc:
        check(not linear(dc,dc[c]),'full_endpoint_Q_mapping_fibre_d_squared')
        check(linear(proj,dc[c])==linear(db,proj[c]),'relative_fibre_projection_chain_map')
        lhs=add(linear(dc,hom[c]),linear(hom,dc[c]))
        rhs=add({c:1},scale(linear(inc,proj[c]),-1))
        check(lhs==rhs,'full_endpoint_Q_fibre_integral_retraction')
    for c in Bg.cells:
        check(linear(dc,inc[c])==linear(inc,db[c]),'relative_fibre_inclusion_chain_map')
        check(linear(proj,inc[c])=={c:1},'relative_fibre_projection_section')
    return len(dc)


def main(output: Path):
    COUNT.clear();models={};rows=[];fibre_generators=0
    for mask in range(64):
        P=mask_normals(mask);normal=LONGS+P;N=set(normal)
        row={'mask':mask,'positive_short_normals':[short_name(d) for d in P]}
        for support in ('K','V','E','B','Q'):
            models[(mask,support)]=Grade(normal,support)
        K,Vg,E,Bg,Q=(models[(mask,s)] for s in ('K','V','E','B','Q'))
        fibre_generators+=verify_endpoint_fibre(K,Vg,E,Bg,Q)
        # Equivariant projection to the residual unmarked short-face cochains.
        C=tuple(d for d in SHORTS if d not in P)
        residual,rd=residual_complex(C)
        proj={c:({c[0]:1} if not(set(c[0])&N) else {}) for c in Bg.cells}
        for c in Bg.cells:
            check(linear(proj,Bg.d[c])==linear(rd,proj[c]),'residual_projection_actual_chain_map')
        # Its kernel is a closed subcomplex and contracts integrally.
        ker=Grade(normal,'B')
        ker.cells=tuple(c for c in ker.cells if set(c[0])&N);ker.set=set(ker.cells)
        ker.d={c:{t:a for t,a in Bg.d[c].items() if t in ker.set} for c in ker.cells}
        check(all(set(Bg.d[c])<=ker.set for c in ker.cells),'normal_kernel_is_strict_subcomplex')
        ker.reduce();check(ker.homology=={},'normal_projection_kernel_integrally_acyclic')
        subgroup=tuple(g for g in G if {image_diag(d,g) for d in P}==set(P))
        row.update(bar_model(C,subgroup))
        row['target_generator_counts']={s:len(models[(mask,s)].cells) for s in ('K','V','E','B','Q')}
        row['projection_kernel_generators']=len(ker.cells)
        row['endpoint_H0_ranks']={
          '+':int(not(set(P)&set(VP))),'-':int(not(set(P)&set(VM)))}
        # Independent endpoint contraction: any first allowed mark kills its
        # entire homogeneous endpoint normal cube, not just a chosen scalar.
        for endpoint in (VP,VM):
            candidates=tuple(d for d in endpoint if d in P)
            cells=tuple(c for c in Vg.cells if c[0]==endpoint)
            dd={c:Vg.d[c] for c in cells}
            if not candidates:
                check(cells==((endpoint,()),),'unhit_endpoint_is_one_integral_cycle')
            else:
                chosen=candidates[0];hh={}
                for c in cells:
                    marks=c[1]
                    hh[c]=({(endpoint,tuple(sorted(marks+(chosen,)))):
                        (-1)**sum(d<chosen for d in marks)} if chosen not in marks else {})
                for c in cells:
                    check(add(linear(dd,hh[c]),linear(hh,dd[c]))=={c:1},
                          'full_endpoint_complex_contracts_after_branch_normal')
        rows.append(row)
    # Cube multiplication and group transport: the coefficient monomials,
    # projection to residual faces, and all actual differentials commute.
    edges=squares=0
    for mask in range(64):
        P=set(mask_normals(mask))
        for i,d in enumerate(SHORTS):
            if mask>>i&1:continue
            nxt=mask|(1<<i);edges+=1
            for support in ('K','V','E','B','Q'):
                a=models[(mask,support)];bb=models[(nxt,support)]
                check(a.set<=bb.set,'short_normal_multiplication_has_legal_target')
                for c in a.cells:
                    check(a.d[c]==bb.d[c],'short_normal_multiplication_is_chain_map')
                    check(eadd(eadd(a.gamma,weight(c[0])),exp({IX[d]+9:1}))==
                          eadd(bb.gamma,weight(c[0])), 'multiplication_keeps_exact_fine_degree')
                    if support=='B':
                        left=c[0] if not(set(c[0])&(set(LONGS)|P|{d})) else None
                        before=c[0] if not(set(c[0])&(set(LONGS)|P)) else None
                        right=before if before is not None and d not in before else None
                        check(left==right,'normal_cube_becomes_induced_subcomplex_restriction')
        absent=[i for i in range(6) if not(mask>>i&1)]
        for i,j in combinations(absent,2):
            squares+=1
            for c in models[(mask,'B')].cells:
                m=eadd(models[(mask,'B')].gamma,weight(c[0]))
                ai=exp({IX[SHORTS[i]]+9:1});aj=exp({IX[SHORTS[j]]+9:1})
                check(eadd(eadd(m,ai),aj)==eadd(eadd(m,aj),ai),'all_short_normal_cube_squares_commute')
        for g in G:
            target=normal_mask(image_diag(d,g) for d in P)
            for support in ('B','V','E','Q'):
                a=models[(mask,support)];bb=models[(target,support)]
                for c in a.cells:
                    tc,sc=act_cell(c,g)
                    check(tc in bb.set,'dihedral_action_transports_short_normal_grade')
                    lhs={}
                    for t,n in a.d[c].items():
                        tt,ss=act_cell(t,g);lhs=add(lhs,{tt:n*ss})
                    check(lhs==scale(bb.d[tc],sc),'dihedral_short_normal_cube_chain_equivariance')
    check((edges,squares)==(192,240),'entire_six_normal_cube_verified')
    # Reconstruct the inherited coherent corridor, including the target endpoint
    # frames, instead of relying only on the computed fibre being nonempty.
    seed=models[(0,'E')];seedK=models[(0,'K')]
    zz={tuple(sorted((SHORTS[0],LONGS[0]))):1,
        tuple(sorted((SHORTS[0],SHORTS[4]))):1,
        tuple(sorted((LONGS[0],SHORTS[3]))):-1,
        tuple(sorted((SHORTS[1],SHORTS[3]))):-1}
    z={(f,()):n for f,n in zz.items()}
    facet=tuple((f,()) for f in FACES if len(f)==1)
    edge=tuple((f,()) for f in FACES if len(f)==2)
    mat=[[seed.d[c].get(e,0) for c in facet] for e in edge]
    hs={};ks={};T=((),())
    for g in G:
        difference=add(seed.act(z,g),scale(z,-1))
        coeff=solve_integral(mat,[difference.get(e,0) for e in edge])
        hs[g]={c:n for c,n in zip(facet,coeff) if n}
        check(linear(seed.d,hs[g])==difference,'inherited_corridor_transport_constructed')
    for g,h in product(G,repeat=2):
        difference=add(seed.act(hs[h],g),scale(hs[mul(g,h)],-1),hs[g])
        k=difference.get(facet[0],0);ks[(g,h)]=k
        check(difference==scale(seed.d[T],k),'inherited_corridor_pair_constructed')
    for g,h,k in product(G,repeat=3):
        check((-1)**g[1]*ks[(h,k)]-ks[(mul(g,h),k)]+ks[(g,mul(h,k))]-ks[(g,h)]==0,
              'inherited_corridor_all_triples_close')
    for row in rows:
        mm=row['mask'];ee=models[(mm,'E')];kk=models[(mm,'K')]
        stab=tuple(tuple(g) for g in row['stabilizer'])
        check(not linear(ee.d,z),'transported_corridor_is_endpoint_relative_cycle')
        check(linear(kk.d,z)=={(VP,()):1,(VM,()):1},'both_actual_transported_endpoint_frames')
        for g in stab:
            check(linear(ee.d,hs[g])==add(ee.act(z,g),scale(z,-1)),
                  'stabilizer_coherent_basepoint_in_each_grade')
        for g,h in product(stab,repeat=2):
            difference=add(ee.act(hs[h],g),scale(hs[mul(g,h)],-1),hs[g])
            check(difference==scale(ee.d[T],ks[(g,h)]),'stabilizer_pair_coherence_in_each_grade')
    # Omega is an actual full loaded top cycle, including both endpoint tops.
    full=models[(63,'K')];Efull=models[(63,'E')];Qfull=models[(63,'Q')]
    T=((),());ms=[((d,),(d,)) for d in LONGS]
    W=add({T:1},*({c:-1} for c in ms))
    Omega={(f,f):(-1)**(len(f)*(len(f)+1)//2) for f in FACES}
    check(not linear(full.d,Omega),'full_polynomial_top_cycle_closed')
    check({c:a for c,a in Omega.items() if c in Qfull.set}==W,'full_top_cycle_projects_to_Delta_omega')
    OmegaE={c:a for c,a in Omega.items() if c in Efull.set}
    OmegaV={c:a for c,a in Omega.items() if c in models[(63,'V')].set}
    check(not linear(Efull.d,OmegaE),'endpoint_quotient_top_cycle_closed')
    deltaOmegaE={c:a for c,a in linear(full.d,OmegaE).items() if c in models[(63,'V')].set}
    check(deltaOmegaE==scale(linear(full.d,OmegaV),-1),
          'top_loop_endpoint_restriction_has_explicit_nullhomotopy')
    primitive_beta=linear(models[(0,'E')].d,W)
    t=add(W,scale(OmegaE,-1))
    check(set(t)<=models[(63,'B')].set and not(set(t)&models[(63,'V')].set),
          'support_filler_has_exact_required_support')
    check(linear(Efull.d,t)==primitive_beta,'Delta_support_transgression_explicit_filler')
    t_full=add(t,scale(OmegaV,-1))
    check(set(t_full)<=models[(63,'B')].set,'endpoint_corrected_filler_is_short_supported')
    check(linear(full.d,t_full)==primitive_beta,'both_endpoint_corrections_complete_support_filler')
    check((len(t),len(t_full))==(39,41),'endpoint_terms_not_discarded_from_full_filler')
    for g in G:
        check(full.act(Omega,g)==scale(Omega,(-1)**g[1]),'full_top_cycle_has_required_orientation')
        check(Qfull.act(W,g)==scale(W,(-1)**g[1]),'generic_top_cycle_has_required_orientation')
        for h in G:
            check(g[1]+(-1)**g[1]*h[1]==mul(g,h)[1], 'reflection_loop_cocycle_identity')
    # The original loop projects to eta times the sum of the short vertices.
    projected_beta={c[0]:a for c,a in primitive_beta.items() if not(set(c[0])&set(LONGS))}
    check(projected_beta=={(d,):1 for d in SHORTS},'actual_18_term_boundary_projects_to_six_vertex_cocycle')
    check(rows[0]['pi0_torsion']==[2] and rows[0]['pi1_free_rank']==0,'original_two_component_fibre_recovered')
    check(rows[63]['pi0_torsion']==[] and rows[63]['pi0_free_rank']==0 and rows[63]['pi1_free_rank']==0,
          'full_normal_continuation_relative_fibre_contractible')
    for inds in ((1,3,5),(0,2,4)):
        mask=sum(1<<i for i in inds)
        check(rows[mask]['pi0_free_rank']==0 and rows[mask]['pi0_torsion']==[] and rows[mask]['pi1_free_rank']==1,
              'single_branch_grade_has_one_component_and_integer_loop')
    histogram=Counter((len(mask_normals(row['mask'])),len(row['stabilizer']),row['pi0_free_rank'],
                       tuple(row['pi0_torsion']),row['pi1_free_rank']) for row in rows)
    result={
        'status':'proved_target_side_endpoint_sensitive_short_normal_cube',
        'source_commit':COMMIT,'source_blobs':SOURCES,
        'base_long_normal_degree':'gamma = sum of all three long-normal degrees',
        'normal_cube':{'vertices':64,'edges':edges,'squares':squares},
        'relative_fibre_deformation_complex':'F_B[-1], with both complete endpoint complexes retained',
        'residual_model':'C^*(compatible remaining short faces; Z) tensor orientation, shifted by 1',
        'homotopy_formula':'pi_n = H^(1-n)_G_P(Lambda_P; Z_chi); n>=0',
        'positive_endpoint_primitive_annihilator':['u_x1','u_x3','u_x5'],
        'negative_endpoint_primitive_annihilator':['u_x0','u_x2','u_x4'],
        'full_top_cycle_terms':len(Omega),'endpoint_quotient_top_cycle_terms':len(OmegaE),
        'endpoint_top_corrections':encoded_vector(OmegaV),
        'support_filler_terms':len(t),'support_filler':encoded_vector(t),
        'endpoint_corrected_support_filler_terms':len(t_full),
        'endpoint_corrected_support_filler':encoded_vector(t_full),
        'short_support_transgression_terms':len(primitive_beta),
        'grade_records':rows,
        'classification_histogram':[{
          'number_positive_short_normals':n,'stabilizer_order':g,
          'pi0_free_rank':r,'pi0_torsion':list(tors),'pi1_free_rank':l,'number_of_grades':count}
          for (n,g,r,tors,l),count in sorted(histogram.items())],
        'assertions':dict(sorted(COUNT.items())),'total_exact_assertions':sum(COUNT.values()),
        'scopes':[
          'All fibre maps use the actual target coefficient domains and full endpoint complexes.',
          'An admissible basepoint is the transported coherent corridor from the previous construction.',
          'Each grade uses its own stabilizer; proper grades are not falsely assigned the full D3 action.',
          'Projection equivalence follows from an explicitly contracted kernel, not index contractibility.',
          'Integer bar cohomology and Smith reductions are exact; arbitrary exponents are governed by the support proof.',
          'The all-normal map identifies old parity choices; it does not select one.',
          'Normal parameters are not identified with occurrence, external Cartier, or external Tor coordinates.',
          'No normalization-sheet mixed-variance physical comparison or physical parity is claimed.'
        ]
    }
    import hashlib
    result['checker_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:result[k] for k in ('status','normal_cube','full_top_cycle_terms',
        'support_filler_terms','classification_histogram','total_exact_assertions')},indent=2))


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path('marici_endpoint_normal_cube_relative_fibre_certificate.json'))
    args=parser.parse_args();main(args.output)
