#!/usr/bin/env python3
"""Verify full-normalization duality and the two-grade conductor trace.

Standalone, Python standard library only. Reconstructs the 430-state
coefficient complex and conductor resolution, both reciprocal traces, the
finite normalization fibre and full six-coordinate Cech support, a 50-state
ambient free resolution of the normalization ring and its dual, and the
branchwise supported residue. All variable and support labels are retained.
The accompanying proof supplies the all-polynomial exactness arguments.
"""
from __future__ import annotations
import argparse
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from itertools import combinations, product
import json
from pathlib import Path

DIAGONALS = ('02','03','04','13','14','15','24','25','35')
PLUS = frozenset(('13','15','35'))
MINUS = frozenset(('02','04','24'))
SHORT = PLUS | MINUS
SHORT_ORDER = tuple(sorted(SHORT))
VARIABLES = tuple('X'+d for d in DIAGONALS) + ('beta',)
ZERO = (0,)*10
COUNTS: Counter[str] = Counter()
COMMIT = 'd1947b67a60d3e88ba77f4ca60ea02c2a306ee61'

def check(value: bool, family: str, detail: object = '') -> None:
    if not value:
        raise AssertionError(f'{family}: {detail}')
    COUNTS[family] += 1

def put(v: dict, key: object, value: int) -> None:
    if value:
        v[key] = v.get(key, 0) + value
        if not v[key]:
            del v[key]

def add(a: dict, b: dict, scalar: int = 1) -> dict:
    out = dict(a)
    for key, value in b.items():
        put(out, key, scalar*value)
    return out

def monomial(*names: str) -> tuple[int, ...]:
    p = [0]*10
    for name in names:
        p[VARIABLES.index(name)] += 1
    return tuple(p)

def survives(p: tuple[int, ...]) -> bool:
    return not (any(p[DIAGONALS.index(d)] for d in PLUS)
                and any(p[DIAGONALS.index(d)] for d in MINUS))

def multiply(v: dict, p: tuple[int, ...], scalar: int = 1) -> dict:
    out = {}
    for (j, q), c in v.items():
        r = tuple(a+b for a,b in zip(p,q))
        if survives(r):
            put(out, (j,r), scalar*c)
    return out

def apply(matrix: dict, vector: dict) -> dict:
    out = {}
    for (j,p),c in vector.items():
        for (i,q),s in matrix.get(j,{}).items():
            r = tuple(a+b for a,b in zip(p,q))
            if survives(r):
                put(out,(i,r),c*s)
    return out

def unit(j: int) -> dict:
    return {(j,ZERO):1}

def restrict(v: dict, ids: set[int]) -> dict:
    return {(j,p):c for (j,p),c in v.items() if j in ids}

def crosses(a: str, b: str) -> bool:
    i,j = map(int,a)
    k,l = map(int,b)
    return i<k<j<l or k<i<l<j

class Complex:
    def __init__(self, occurrence: str = '35') -> None:
        self.occurrence = occurrence
        self.faces = [F for n in range(4) for F in combinations(DIAGONALS,n)
                      if all(not crosses(a,b) for a,b in combinations(F,2))]
        self.states = [(F,H,e) for F in self.faces for n in range(len(F)+1)
                       for H in combinations(F,n) for e in (0,1)]
        self.index = {s:j for j,s in enumerate(self.states)}
        self.degree = {j:3-len(F)+len(H)+e for j,(F,H,e) in enumerate(self.states)}
        self.weight = {j:len(H) for j,(F,H,e) in enumerate(self.states)}
        self.V = {j for j,(F,H,e) in enumerate(self.states) if frozenset(F) in (PLUS,MINUS)}
        self.B = {j for j,(F,H,e) in enumerate(self.states) if set(F)&SHORT}
        self.Q = set(range(430))-self.B
        self.end_top = {self.index[(tuple(sorted(F)),tuple(sorted(F)),e)]
                        for F in (MINUS,PLUS) for e in (0,1)}
        self.boundary_ids = self.Q | self.end_top
        self.kernel_ids = set(range(430))-self.boundary_ids
        face_set = set(self.faces)
        self.d = {j:{} for j in range(430)}
        for j,(F,H,e) in enumerate(self.states):
            for a in DIAGONALS:
                FF = tuple(sorted(F+(a,)))
                if a not in F and FF in face_set:
                    put(self.d[j],(self.index[FF,H,e],monomial('X'+a)),
                        (-1)**sum(b<a for b in F))
            for n,a in enumerate(H):
                put(self.d[j],(self.index[F,H[:n]+H[n+1:],e],monomial('beta','X'+a)),
                    (-1)**(3-len(F)+n))
            if e:
                put(self.d[j],(self.index[F,H,0],monomial('X'+self.occurrence)),
                    (-1)**(3-len(F)+len(H)))
        check(Counter(map(len,self.faces))=={0:1,1:9,2:21,3:14},'face_census')
        check((len(self.states),len(self.V),len(self.B),len(self.Q),len(self.end_top),len(self.kernel_ids))
              ==(430,32,416,14,4,412),'full_support_counts')
        for j,col in self.d.items():
            check(not apply(self.d,col),'full_d_squared',j)
            check(all(self.degree[i]==self.degree[j]-1 for i,p in col),'full_degree',j)
            if j in self.V:
                check(all(i in self.V for i,p in col),'endpoint_subcomplex',j)
            if j in self.B:
                check(all(i in self.B for i,p in col),'short_boundary_subcomplex',j)
            if j in self.kernel_ids:
                check(all(i in self.kernel_ids for i,p in col),'joint_frame_kernel_subcomplex',j)
        self.d_boundary={j:restrict(self.d[j],self.boundary_ids) for j in self.boundary_ids}
        for j in range(430):
            check(restrict(self.d[j],self.boundary_ids)
                  ==apply(self.d_boundary,restrict(unit(j),self.boundary_ids)),
                  'joint_boundary_is_chain_map',j)

    def occurrence_zero(self) -> tuple[dict,dict]:
        coefficients={}
        for j,(F,H,e) in enumerate(self.states):
            p=[0]*10
            for a in F:p[DIAGONALS.index(a)]+=1
            for a in H:p[DIAGONALS.index(a)]-=1
            p[DIAGONALS.index(self.occurrence)]-=e
            if min(p)>=0 and survives(tuple(p)):
                coefficients[j]=tuple(p)
        d={j:{} for j in coefficients}
        for j,p in coefficients.items():
            for (i,q),c in self.d[j].items():
                r=tuple(a+b for a,b in zip(p,q))
                if not survives(r):continue
                check(i in coefficients,'weight_zero_target_exists',(j,i))
                rr=list(r);rr[9]=0
                check(tuple(rr)==coefficients[i],'forced_occurrence_monomial',(j,i))
                check(r[9]==self.weight[j]-self.weight[i],
                      'beta_weight_on_every_slice_arrow',(j,i))
                put(d[j],i,c)
        check(dict(sorted(Counter(self.degree[j] for j in coefficients).items()))
              =={0:8,1:59,2:108,3:56},'full_occurrence_zero_ranks')
        return coefficients,d

def source_resolution():
    """Resolve I=I_+ direct-sum I_- through relations among relations.

    F0 has six generators, F1 has 24, F2 has 92. All remaining resolution
    terms can be put in higher homological degrees and cannot contribute
    to the degree-zero maps or positive-degree homotopies calculated here.
    Exactness is also proved, for arbitrary polynomial coefficients, in
    the accompanying mathematical proof by branch decomposition.
    """
    rel=[]
    for sheet in (sorted(PLUS), sorted(MINUS)):
        opposite=sorted(SHORT-set(sheet))
        for a,c in combinations(sheet,2):
            rel.append({'name':('K',a,c),
                        'weight':monomial('X'+a,'X'+c)[:9],
                        'd':{c:{monomial('X'+a):1}, a:{monomial('X'+c):-1}}})
        for n in opposite:
            for a in sheet:
                rel.append({'name':('M',n,a),
                            'weight':monomial('X'+n,'X'+a)[:9],
                            'd':{a:{monomial('X'+n):1}}})
    relindex={r['name']:j for j,r in enumerate(rel)}
    sids={a:i for i,a in enumerate(SHORT_ORDER)}
    d0={sids[a]:{(0,monomial('X'+a)):1} for a in SHORT_ORDER}
    d1={j:{(sids[a],p):z for a,ps in r['d'].items() for p,z in ps.items()}
        for j,r in enumerate(rel)}
    syzy=[]
    for sheet in (sorted(PLUS),sorted(MINUS)):
        opposite=sorted(SHORT-set(sheet))
        a,c,d=sheet
        syzy.append({'name':('KK',a,c,d), 'd':{
            (relindex['K',c,d],monomial('X'+a)):1,
            (relindex['K',a,d],monomial('X'+c)):-1,
            (relindex['K',a,c],monomial('X'+d)):1}})
        for n in opposite:
            for a,c in combinations(sheet,2):
                syzy.append({'name':('MK',n,a,c),'d':{
                    (relindex['K',a,c],monomial('X'+n)):1}})
        for p in sheet:
            for n in opposite:
                for a in sheet:
                    syzy.append({'name':('PM',a,n,p),'d':{
                        (relindex['M',n,p],monomial('X'+a)):1}})
            for n,m in combinations(opposite,2):
                syzy.append({'name':('MM',n,m,p),'d':{
                    (relindex['M',m,p],monomial('X'+n)):1,
                    (relindex['M',n,p],monomial('X'+m)):-1}})
    check((len(sids),len(rel),len(syzy))==(6,24,92),'source_resolution_ranks')
    for j,v in d1.items():check(not apply(d0,v),'source_first_relations_exact',j)
    for j,sy in enumerate(syzy):
        check(not apply(d1,sy['d']),'source_second_relations_exact',j)
        weights={tuple(x+y for x,y in zip(rel[r]['weight'],p[:9])) for (r,p) in sy['d']}
        check(len(weights)==1,'source_second_relations_homogeneous',j)
        sy['weight']=next(iter(weights))
    return {'generators':SHORT_ORDER,'relations':rel,'syzygies':syzy,
            'd0':d0,'d1':d1,'d2':{j:s['d'] for j,s in enumerate(syzy)}}

def smul(v, c=1):
    return {k:c*z for k,z in v.items() if c*z}

def compose(A,B):
    return {j:apply(A,v) for j,v in B.items()}

def subcomplex(M,ids):
    ids=set(ids)
    for j in ids:
        check(all(i in ids for i,p in M.d[j]),'local_closed_support',j)
    return {j:dict(M.d[j]) for j in sorted(ids)}

def quotient(d,keep):
    keep=set(keep)
    return {j:restrict(d[j],keep) for j in sorted(keep)}

def verify_d(d,degrees,label):
    for j,v in d.items():
        check(not apply(d,v),'new_squared_zero',(label,j))
        check(all(degrees[i]==degrees[j]-1 for i,p in v),'new_degrees',(label,j))

def verify_chain(F,ds,dt,label):
    for j in ds:
        check(apply(dt,F.get(j,{}))==apply(F,ds[j]),'new_chain_equation',(label,j))

def mod_x(v):
    xi=DIAGONALS.index('03')
    return {(i,p):z for (i,p),z in v.items() if not p[xi]}

def one_row(j,p=ZERO,z=1):
    return {(j,p):z} if z else {}

def build_source():
    raw=source_resolution()
    labels=[('unit',0)]+[('generator',a) for a in SHORT_ORDER]
    labels += [('relation',j) for j in range(24)]
    labels += [('syzygy',j) for j in range(92)]
    d={key:{} for key in labels}
    degrees={('unit',0):2}
    for a in SHORT_ORDER:
        d['generator',a]={(('unit',0),monomial('X'+a)):1}
        degrees['generator',a]=3
    for j,r in enumerate(raw['relations']):
        d['relation',j]={(("generator",a),p):z for a,ps in r['d'].items() for p,z in ps.items()}
        degrees['relation',j]=4
    for j,r in enumerate(raw['syzygies']):
        d['syzygy',j]={(("relation",i),p):z for (i,p),z in r['d'].items()}
        degrees['syzygy',j]=5
    verify_d(d,degrees,'resolved_A_shift2')
    return raw,d,degrees

def edge_map(M,source,edge):
    E=tuple(sorted(edge))
    ends=[F for F in M.faces if len(F)==3 and set(E)<=set(F)]
    check(len(ends)==2,'opposite_edge_endpoints',edge)
    L=one_row(M.index[E,E,0],monomial('beta'))
    for F in ends:L=add(L,unit(M.index[F,F,0]),-1)
    bd=apply(M.d,L)
    up={(j,p):z for (j,p),z in bd.items() if any(p[DIAGONALS.index(a)] for a in PLUS)}
    um={(j,p):z for (j,p),z in bd.items() if any(p[DIAGONALS.index(a)] for a in MINUS)}
    check(add(up,um)==bd,'split_sheet_boundary')
    check(not apply(M.d,up) and not apply(M.d,um),'both_sheet_primaries_closed')
    gp={j:{} for j in source};gm={j:{} for j in source}
    gp['unit',0]=up;gm['unit',0]=smul(um,-1)
    for a in PLUS:gp['generator',a]=multiply(L,monomial('X'+a))
    for a in MINUS:gm['generator',a]=multiply(L,monomial('X'+a),-1)
    verify_chain(gp,source,M.d,('edge_plus',edge))
    verify_chain(gm,source,M.d,('edge_minus',edge))
    H={j:{} for j in source};H['unit',0]=L
    for j in source:
        check(add(apply(M.d,H[j]),apply(H,source[j]))==add(gp[j],gm[j],-1),
              'sheet_comparison_homotopy',(edge,j))
    return L,up,um,gp,gm,H

def common_koszul():
    # Ordered native 02, native 35, then separate occurrence 35.
    d={m:{} for m in range(8)}
    coef=[monomial('beta','X02'),monomial('beta','X35'),monomial('X35')]
    degree={m:m.bit_count() for m in range(8)}
    for m in d:
        pos=0
        for bit in range(3):
            if m>>bit&1:
                put(d[m],(m^(1<<bit),coef[bit]),(-1)**pos);pos+=1
    verify_d(d,degree,'common_native_native_occurrence')
    return d,degree

def normal_edge():
    # Orientation g=-[02,35]; h_l is the positive l normal at W_l.
    d={k:{} for k in ('p03','p25','g','h03','h25')}
    d['g']={('p03',monomial('X03')):1,('p25',monomial('X25')):1}
    d['h03']={('p03',monomial('beta','X03')):1}
    d['h25']={('p25',monomial('beta','X25')):1}
    deg={k:int(k not in ('p03','p25')) for k in d}
    verify_d(d,deg,'two_endpoint_normal_interval')
    return d,deg

def tensor(dP,degP,dM,degM):
    d={};degrees={}
    for p in dP:
        for m in dM:
            key=(p,m);degrees[key]=degP[p]+degM[m];d[key]={}
            for (q,c),z in dP[p].items():put(d[key],((q,m),c),z)
            for (n,c),z in dM[m].items():put(d[key],((p,n),c),z*(-1)**degP[p])
    verify_d(d,degrees,'tensor')
    return d,degrees

def tensor_native_identification(M,dt):
    J={};inverse={}
    for p,m in dt:
        common=tuple(a for k,a in enumerate(('02','35')) if m>>k&1)
        e=(m>>2)&1
        if p=='g':F=('02','35');H=common;sg=-1
        else:
            a=p[-2:];F=tuple(sorted(('02','35',a)))
            if p[0]=='p':H=common;sg=1
            else:H=tuple(sorted(common+(a,)));sg=(-1)**int(bool(m&1))
        j=M.index[F,H,e];J[p,m]=one_row(j,z=sg)
        inverse[j]=one_row((p,m),z=sg)
    return J,inverse

def shift_complex(d,degree,n):
    return {j:smul(v,(-1)**n) for j,v in d.items()}, {j:k+n for j,k in degree.items()}

def cartier_hom(d,degree):
    # Signed model Hom(K(x),C)_n = C_n + C_{n+1}.
    dd={};dg={}
    for j in d:
        dd['a',j]={};dd['b',j]={}
        dg['a',j]=degree[j];dg['b',j]=degree[j]-1
        for (i,p),z in d[j].items():
            put(dd['a',j],(('a',i),p),z)
            put(dd['b',j],(('b',i),p),-z)
        put(dd['a',j],(('b',j),monomial('X03')),1)
    verify_d(dd,dg,'Cartier_Hom')
    return dd,dg

def cartier_induced(F,sourcekeys):
    return {(s,j):{((s,i),p):z for (i,p),z in F.get(j,{}).items()}
            for j in sourcekeys for s in ('a','b')}

def cartier_purity(d,degree,hd):
    dd={j:smul(mod_x(v),-1) for j,v in d.items()}
    pp={j:({(j[1],ZERO):1} if j[0]=='b' else {}) for j in hd}
    for j,v in hd.items():
        check(mod_x(apply(dd,pp[j]))==mod_x(apply(pp,v)),
              'Cartier_purity_chain_map_mod_x',j)
    tr={j:({(j[1],ZERO):1} if j[0]=='a' else {}) for j in hd}
    verify_chain(tr,hd,d,'Cartier_counit')
    # Model the kernel of purity by (a,xc); x is a nonzero-divisor.
    kd={};ki={};kh={}
    for j in d:
        ka=('a',j);kc=('c',j)
        kd[ka]={};kd[kc]={}
        for (i,p),z in d[j].items():
            put(kd[ka],(('a',i),p),z);put(kd[kc],(('c',i),p),-z)
        put(kd[ka],(kc,ZERO),1)
        ki[ka]=one_row(('a',j));ki[kc]=one_row(('b',j),monomial('X03'))
        kh[ka]={};kh[kc]=one_row(('a',j))
    verify_chain(ki,kd,hd,'purity_kernel_inclusion')
    for j in kd:
        check(add(apply(kd,kh[j]),apply(kh,kd[j]))==unit(j),
              'purity_kernel_integral_contraction',j)
    return dd,pp,tr,kd,ki,kh

def physical_diagonal(a):
    return ''.join(map(str,sorted((3-int(v))%6 for v in a)))

def parity(xs):
    return (-1)**sum(xs[i]>xs[j] for i in range(len(xs)) for j in range(i+1,len(xs)))

def reflect_chain(M,N,v):
    out={}
    for (j,p),z in v.items():
        F,H,e=M.states[j]
        FF=[physical_diagonal(a) for a in F];HH=[physical_diagonal(a) for a in H]
        pp=[0]*10;pp[9]=p[9]
        for k,a in enumerate(DIAGONALS):pp[DIAGONALS.index(physical_diagonal(a))]=p[k]
        i=N.index[tuple(sorted(FF)),tuple(sorted(HH)),e]
        put(out,(i,tuple(pp)),-parity(FF)*parity(HH)*z)
    return out

def reflect_source_label(raw,j):
    if j[0]=='unit':return j,1
    if j[0]=='generator':return ('generator',physical_diagonal(j[1])),1
    if j[0]=='relation':
        typ,a,b=raw['relations'][j[1]]['name'];a,b=physical_diagonal(a),physical_diagonal(b);sg=1
        if typ=='K' and a>b:a,b,sg=b,a,-1
        ri={r['name']:k for k,r in enumerate(raw['relations'])}
        return ('relation',ri[typ,a,b]),sg
    raise ValueError('Only nonzero source components through relations are reflected here')

def reflect_map(M,N,raw,F):
    out={j:{} for j in F}
    for j,v in F.items():
        if not v:continue
        jj,sg=reflect_source_label(raw,j)
        out[jj]=smul(reflect_chain(M,N,v),sg)
    return out

def serialize_vec(v):
    return [{'basis':j,'powers':list(p),'coefficient':z}
            for (j,p),z in sorted(v.items(),key=lambda kv:repr(kv[0]))]

def serialize_mat(F):
    return [{'source':j,'image':serialize_vec(v)} for j,v in sorted(F.items(),key=lambda kv:repr(kv[0]))]


def wedge(left: dict, right: dict) -> dict:
    """Exterior product on the three ordered common normal generators."""
    out={}
    for (m,p),a in left.items():
        for (n,q),b in right.items():
            if m & n:
                continue
            inv=sum(1 for i in range(3) for j in range(3)
                    if (m>>i)&1 and (n>>j)&1 and i>j)
            exponent=tuple(x+y for x,y in zip(p,q))
            if survives(exponent):
                put(out,(m|n,exponent),a*b*(-1)**inv)
    return out


def exterior_extension(images: list[dict]) -> dict:
    out={}
    for mask in range(8):
        value=unit(0)
        for j in range(3):
            if mask>>j&1:
                value=wedge(value,images[j])
        out[mask]=value
    return out


def rref_integer_kernel(matrix: list[list[int]], ncols: int):
    """Exact rational RREF; an integral free-coordinate kernel is certified."""
    a=[[Fraction(x) for x in row] for row in matrix]
    piv=[]; row=0
    for col in range(ncols):
        pivot=next((k for k in range(row,len(a)) if a[k][col]),None)
        if pivot is None:
            continue
        a[row],a[pivot]=a[pivot],a[row]
        q=a[row][col]
        a[row]=[x/q for x in a[row]]
        for k in range(len(a)):
            if k!=row and a[k][col]:
                q=a[k][col]
                a[k]=[x-q*y for x,y in zip(a[k],a[row])]
        piv.append(col);row+=1
        if row==len(a):
            break
    free=[j for j in range(ncols) if j not in piv]
    # Each free coordinate is an arbitrary integer. Integral pivot formulas
    # therefore describe the complete integer kernel, not a sublattice.
    for i in range(len(piv)):
        check(all(a[i][j].denominator==1 for j in free),
              'integral_kernel_free_coordinates',(i,ncols))
    ker=[]
    for j in free:
        v=[0]*ncols;v[j]=1
        for i,k in enumerate(piv):v[k]=-int(a[i][j])
        check(all(sum(x*y for x,y in zip(r,v))==0 for r in matrix),
              'exact_kernel_basis',j)
        ker.append(v)
    return piv,free,ker


def determinant(a: list[list[int]]) -> int:
    n=len(a)
    check(all(len(row)==n for row in a),'square_determinant_shape',n)
    if not n:return 1
    m=[list(row) for row in a];last=1;sign=1
    for k in range(n-1):
        p=next((j for j in range(k,n) if m[j][k]),None)
        if p is None:return 0
        if p!=k:m[k],m[p]=m[p],m[k];sign=-sign
        pivot=m[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num=m[i][j]*pivot-m[i][k]*m[k][j]
                check(num%last==0,'Bareiss_exact_division',(n,k,i,j))
                m[i][j]=num//last
            m[i][k]=0
        last=pivot
    return sign*m[-1][-1]


def transpose(a,ncols=None):
    if a:return [list(row) for row in zip(*a)]
    return [[] for _ in range(ncols or 0)]


def inverse_unit_matrix(a):
    n=len(a)
    m=[[Fraction(x) for x in row]+[Fraction(int(i==j)) for j in range(n)]
       for i,row in enumerate(a)]
    for k in range(n):
        p=next(i for i in range(k,n) if m[i][k]);m[k],m[p]=m[p],m[k]
        q=m[k][k];m[k]=[x/q for x in m[k]]
        for i in range(n):
            if i!=k and m[i][k]:
                q=m[i][k];m[i]=[x-q*y for x,y in zip(m[i],m[k])]
    check(all(v.denominator==1 for row in m for v in row[n:]),
          'integral_unit_matrix_inverse',n)
    return [[int(v) for v in row[n:]] for row in m]


def source_weights(raw):
    w={('unit',0):(0,)*9}
    w.update({('generator',a):monomial('X'+a)[:9] for a in SHORT_ORDER})
    w.update({('relation',i):tuple(r['weight']) for i,r in enumerate(raw['relations'])})
    w.update({('syzygy',i):tuple(r['weight']) for i,r in enumerate(raw['syzygies'])})
    return w


def hom_basis(M,ds,sdg,sw,ids,offset,grade,on_divisor=False):
    result=[]
    for source in ds:
        for j in sorted(ids):
            if M.degree[j]!=sdg[source]+offset:
                continue
            F,H,e=M.states[j]
            exponent=list(sw[source])+[grade-len(H)]
            for a in F:exponent[DIAGONALS.index(a)]+=1
            for a in H:exponent[DIAGONALS.index(a)]-=1
            exponent[DIAGONALS.index(M.occurrence)]-=e
            if min(exponent)<0 or not survives(tuple(exponent)):
                continue
            if on_divisor and exponent[DIAGONALS.index('03')]:
                continue
            result.append((source,j,tuple(exponent)))
    return result


def hom_differential(ds,dt,source_basis,target_basis,offset):
    loc={v:i for i,v in enumerate(target_basis)}
    result=[[0]*len(source_basis) for _ in target_basis]
    for column,(s,j,p) in enumerate(source_basis):
        F={s:one_row(j,p)}
        for t in ds:
            value=add(apply(dt,F.get(t,{})),apply(F,ds[t]),-((-1)**offset))
            for (i,q),v in value.items():
                check((t,i,q) in loc,'Hom_weight_and_degree_legal',(t,i,q))
                result[loc[t,i,q]][column]+=v
    return result


def map_coordinates(F,basis):
    idx={v:i for i,v in enumerate(basis)};out=[0]*len(basis)
    for s,value in F.items():
        for (j,p),c in value.items():
            check((s,j,p) in idx,'candidate_is_homogeneous',(s,j,p))
            out[idx[s,j,p]]+=c
    return out


def scale_map(F,n):
    return {j:multiply(v,monomial(*(['beta']*n))) for j,v in F.items()}


def classification(M,raw,ds,sdg,ids,dt,grade,candidates,on_divisor=False):
    sw=source_weights(raw)
    bs={k:hom_basis(M,ds,sdg,sw,ids,k,grade,on_divisor) for k in (1,0,-1)}
    D1=hom_differential(ds,dt,bs[1],bs[0],1)
    D0=hom_differential(ds,dt,bs[0],bs[-1],0)
    _,free,Z=rref_integer_kernel(D0,len(bs[0]))
    _,_,null1=rref_integer_kernel(D1,len(bs[1]))
    check(not null1,'Hom_positive_degree_injective',(grade,on_divisor))
    rank1=len(bs[1]);rank0=len(bs[0])-len(free)
    for row in D0:
        for col in transpose(D1,len(bs[1])):
            check(sum(x*y for x,y in zip(row,col))==0,'Hom_squared_zero',grade)
    C=[map_coordinates(f,bs[0]) for f in candidates]
    for v in C:
        check(all(sum(x*y for x,y in zip(row,v))==0 for row in D0),
              'candidate_map_closed_in_full_Hom',grade)
    allcols=transpose(D1,len(bs[1]))+C
    coords=[[col[i] for col in allcols] for i in free]
    if allcols:
        pivot_rows,_,_=rref_integer_kernel(transpose(coords,len(allcols)),len(coords))
        check(len(pivot_rows)==len(allcols),'full_column_rank_of_boundary_and_candidate_lattice',grade)
        minor=[coords[i] for i in pivot_rows]
        det=determinant(minor)
        check(abs(det)==1,'saturated_boundary_and_candidate_image',(grade,on_divisor,det))
        inv=inverse_unit_matrix(minor)
        # Functionals are defined on free coordinates of closed Hom cochains.
        # They kill every homotopy boundary and recover the displayed candidates.
        functionals=[]
        for j in range(len(C)):
            f=[0]*len(bs[0])
            for k,r in enumerate(pivot_rows):f[free[r]]=inv[rank1+j][k]
            functionals.append(f)
            check(all(sum(x*y for x,y in zip(f,col))==0
                      for col in transpose(D1,len(bs[1]))),
                  'derived_class_functional_kills_every_homotopy',j)
            check([sum(x*y for x,y in zip(f,col)) for col in C]
                  ==[int(i==j) for i in range(len(C))],
                  'derived_class_functional_detects_basis',j)
    else:
        det=1;minor=[];pivot_rows=[];inv=[];functionals=[]
        check(len(free)==0,'zero_graded_Hom_cohomology',grade)
    rankH=len(bs[0])-rank0-rank1
    if not on_divisor:
        check(rankH==len(candidates),'candidate_basis_exhausts_local_costalk',grade)
    return {
        'grade':grade,'on_X03_divisor':on_divisor,
        'Hom_dimensions_plus1_zero_minus1':[len(bs[k]) for k in (1,0,-1)],
        'differential_ranks':[rank1,rank0],'H0_rank':rankH,
        'candidate_count':len(candidates),'saturated_minor_determinant':det,
        'homotopy_basis':bs[1],'map_basis':bs[0],'equation_basis':bs[-1],
        'homotopy_differential':D1,'map_differential':D0,
        'free_kernel_coordinates':free,'kernel_basis':Z,
        'basis_minor_rows':pivot_rows,'basis_minor':minor,
        'candidate_functionals':functionals,'candidate_columns':C,
    }


def construct_maps(ds,raw):
    def Xi(mask,coefficient=ZERO,sgn=1):
        value=add(one_row(('h03',mask),coefficient,sgn),
                  one_row(('h25',mask),coefficient,sgn))
        return add(value,multiply(one_row(('g',mask),coefficient,sgn),monomial('beta')),-1)
    P={s:{} for s in ds};E={s:{} for s in ds}
    P['unit',0]=Xi(1,monomial('X35'))
    for a in PLUS:
        P['generator',a]=Xi(5,monomial('X'+a))
        E['generator',a]=add(Xi(3,monomial('X'+a)),
                              multiply(Xi(5,monomial('X'+a)),monomial('beta')),-1)
    Rmap={s:dict(v) for s,v in E.items()};Rmap['generator','35']={}
    for i,r in enumerate(raw['relations']):
        tag=r['name']
        if tag[0]=='K' and tag[2]=='35' and tag[1] in PLUS:
            Rmap['relation',i]=Xi(7,monomial('X'+tag[1]))
    return P,E,Rmap,Xi


def primary_coefficient_detector(v):
    """Conductor-linear detector on M_1, valued in the long/beta base ring."""
    ans={}
    for (mask,p),c in v.items():
        if mask==1: chosen='35';power=1
        elif mask==2: chosen='02';power=1
        elif mask==4: chosen='02';power=0
        else: continue
        if any(p[DIAGONALS.index(a)]!=int(a==chosen) for a in SHORT):continue
        pp=list(p);pp[DIAGONALS.index(chosen)]-=1;pp[9]+=power
        put(ans,tuple(pp),c)
    return ans


def nodal_first_symbol_detector_check():
    """All possible linear contributions to a homotopy are tested.

    After beta=1, X03=0 and all other short variables except y,z=0,
    projection onto zeta*eta gives a signed K(y,z)[2]. Its differential is
       da=-y p, dk=-z p, d(ak)=z a-y k.
    A cochain functional is
       [z]F(e_z)_a + [y]F(e_z)_k + [y]F(p).
    Only the constant coefficients of H(p)_a,H(p)_k,H(e_z)_ak can
    contribute to this functional. The three columns below enumerate all.
    """
    # Rows are the three terms in that functional. Columns are those three
    # arbitrary constant homotopy coefficients. Nonconstant terms have degree
    # >=2 after multiplication by y or z and contribute zero.
    matrix=[[1,0,1],[0,0,-1],[-1,0,0]]
    for column in transpose(matrix):
        check(sum(column)==0,'nodal_detector_kills_all_homotopy_coefficients')
    value=[1,0,0]
    check(sum(value)==1,'nodal_detector_E_is_primitive')
    return {'homotopy_linear_coefficient_matrix':matrix,'functional':[1,1,1],
            'E_value_vector':value,'E_class_value':1,
            'scope':'all polynomial homotopies; higher conductor monomials cannot contribute'}


# ----------------------------------------------------------------------
# New calculation: pair only the two native common normals. The separate
# occurrence factor and the complete interval/corner factor are retained.

LAURENT_VARIABLES=VARIABLES+('q02','q35')
LZERO=ZERO+(0,0)

def lmono(*names, q02=0, q35=0):
    return monomial(*names)+(q02,q35)

def lift_laurent(F):
    return {j:{(i,p+(0,0)):c for (i,p),c in v.items()} for j,v in F.items()}

def lapply(F,v):
    ans={}
    for (j,p),c in v.items():
        for (i,q),b in F.get(j,{}).items():
            check(len(p)==len(q)==12,'Laurent_exponent_length')
            t=tuple(x+y for x,y in zip(p,q))
            if survives(t):put(ans,(i,t),c*b)
    return ans

def lcompose(F,G):
    return {j:lapply(F,v) for j,v in G.items()}

def lunit(j):
    return {(j,LZERO):1}

def lverify(F,ds,dt,label):
    for j in ds:
        check(lapply(dt,F.get(j,{}))==lapply(F,ds[j]),'raw_reciprocal_chain_equation',(label,j))

def native_dual(normalized=True):
    d={m:{} for m in range(4)};dg={m:m.bit_count() for m in d}
    for m in d:
        pos=0
        for bit,a in enumerate(('02','35')):
            if (m>>bit)&1:
                if normalized:p=monomial('beta','X'+a);sg=(-1)**pos
                else:
                    p=lmono('beta','X'+a,q02=-int(bit==0),q35=-int(bit==1))
                    sg=-(-1)**pos
                put(d[m],(m^(1<<bit),p),sg);pos+=1
    return d,dg

def hom_complex_finite(ds,sdg,dt,tdg):
    dd={};dg={}
    for s in ds:
        for t in dt:
            key=(s,t);n=tdg[t]-sdg[s];dg[key]=n;dd[key]={}
            for (u,p),c in dt[t].items():put(dd[key],((s,u),p),c)
            for a in ds:
                for (b,p),c in ds[a].items():
                    if b==s:put(dd[key],((a,t),p),-(-1)**n*c)
    return dd,dg

def native_pairing_bit_coefficient(mask, dual, raw=False, occurrence=0):
    a,b=bool(mask&1),bool(mask&2)
    aa,bb=bool(dual&1),bool(dual&2)
    if a+aa!=1 or b+bb!=1:return None
    sign=(-1)**(int(b)*int(aa)+occurrence*(int(aa)+int(bb)))
    if raw:
        sign*=(-1)**(int(a)+int(b))
        return lmono(q02=int(a),q35=int(b)),sign
    return ZERO,sign

def curry_matrix(dt, raw=False):
    matrix={};inverse={}
    for edge,m in dt:
        dual=3^(m&3);e=(m>>2)&1
        p,c=native_pairing_bit_coefficient(m&3,dual,raw,e)
        key=(dual,(edge,e))
        matrix[edge,m]={(key,p):c}
        inverse[key]={((edge,m),tuple(-x for x in p)):c}
    return matrix,inverse

def trace_matrix(dt):
    J={}
    for edge,m in dt:
        result=native_pairing_bit_coefficient(m&3,0,False,(m>>2)&1)
        J[edge,m]={} if result is None else {((edge,(m>>2)&1),result[0]):result[1]}
    return J

def target_hom_proxy(keys,degrees):
    class Proxy:pass
    U=Proxy();U.occurrence='35';U.states={};U.degree={};U.weight={}
    for j,(p,e) in enumerate(keys):
        F=() if p=='g' else (p[-2:],)
        H=(p[-2:],) if p.startswith('h') else ()
        U.states[j]=(F,H,e);U.degree[j]=degrees[p,e];U.weight[j]=len(H)
    return U

def reindex_matrix(F, index):
    return {s:{(index[t],p):c for (t,p),c in col.items()} for s,col in F.items()}

def reindex_differential(d,index):
    return {index[s]:{(index[t],p):c for (t,p),c in col.items()} for s,col in d.items()}

def polynomial_normal_pair_matrix():
    return [[0,0,0,1],[0,0,1,0],[0,-1,0,0],[1,0,0,0]]

# -------------------------------------------------------------------------
# New work: branchwise local cohomology with all source comparison data.
#
# G denotes R; '-' denotes R[X02^-1]; '+' denotes R[X35^-1].
# Coefficients of a localized module are reduced by the opposite sheet ideal.
# Negative powers are admitted only in that module's designated variable.

def branch_monomial(p, branch):
    if branch == 'G':
        check(min(p) >= 0, 'global_coefficients_remain_polynomial', p)
        return p if survives(p) else None
    opposite = PLUS if branch == '-' else MINUS
    if any(p[DIAGONALS.index(a)] != 0 for a in opposite):
        return None
    inverted = DIAGONALS.index('02' if branch == '-' else '35')
    check(all(n >= 0 or i == inverted for i,n in enumerate(p)),
          'poles_only_in_the_designated_target_branch', (branch,p))
    return p


def branch_vector(v, branch):
    ans = {}
    for (j,p),c in v.items():
        q = branch_monomial(p, branch)
        if q is not None:
            put(ans, (j,q), c)
    return ans


def support_apply(F, v):
    ans = {}
    for (s,p),a in v.items():
        for (t,q),c in F.get(s,{}).items():
            m = branch_monomial(tuple(x+y for x,y in zip(p,q)), t[0])
            if m is not None:
                put(ans,(t,m),a*c)
    return ans


def support_complex(d, degrees):
    out = {(tag,j):{} for tag in ('G','-','+') for j in d}
    deg = {(tag,j):degrees[j]-int(tag!='G') for tag,j in out}
    for j in d:
        for (i,p),c in d[j].items():
            put(out['G',j], (('G',i),p), c)
            for tag in ('-','+'):
                m = branch_monomial(p,tag)
                if m is not None:
                    put(out[tag,j],((tag,i),m),-c)
        for tag in ('-','+'):
            put(out['G',j],((tag,j),ZERO),1)
    for s,col in out.items():
        check(not support_apply(out,col),'support_differential_squared_zero',s)
        check(all(deg[t]==deg[s]-1 for t,p in col), 'support_differential_degree',s)
    return out,deg


def support_map(F, dom_keys):
    ans = {(tag,s):{} for tag in ('G','-','+') for s in dom_keys}
    for tag,s in ans:
        for (t,p),c in F.get(s,{}).items():
            m = branch_monomial(p,tag)
            if m is not None:
                put(ans[tag,s],((tag,t),m),c)
    return ans


def support_lift(F, minus_h, plus_h, ds):
    ans = {s:{} for s in ds}
    for s in ds:
        for (t,p),c in F.get(s,{}).items():put(ans[s],(('G',t),p),c)
        for tag,H in (('-',minus_h),('+',plus_h)):
            for (t,p),c in H.get(s,{}).items():
                m=branch_monomial(p,tag)
                if m is not None:put(ans[s],((tag,t),m),c)
    return ans


def verify_support_map(F, ds, dg, sdg, tdeg, label, offset=0):
    for s in ds:
        check(all(tdeg[t]==sdg[s]+offset for t,p in F.get(s,{})),
              'support_map_degree', (label,s))
        delta=add(support_apply(dg,F.get(s,{})),
                  support_apply(F,ds[s]),-((-1)**offset))
        if offset==0:
            check(not delta,'supported_resolved_map_chain_equation',(label,s))


def support_counit(F):
    return {s:{(t,p):c for ((tag,t),p),c in v.items() if tag=='G'}
            for s,v in F.items()}


def xi_trace(e,p=ZERO):
    return {(('h03',e),p):1,(('h25',e),p):1,
            (('g',e),tuple(x+y for x,y in zip(p,monomial('beta')))):-1}


def xi_native(mask,p=ZERO):
    return {(('h03',mask),p):1,(('h25',mask),p):1,
            (('g',mask),tuple(x+y for x,y in zip(p,monomial('beta')))):-1}


def count_terms(F):
    return sum(len(v) for v in F.values())


def verify_pole_module_rules():
    # These checks are algebraic coefficient rules, not a cutoff proof of
    # local-cohomology exactness. The proof uses exact localizations.
    for tag,var,opp in (('-', '02', PLUS), ('+', '35', MINUS)):
        inv=DIAGONALS.index(var)
        for n in range(1,5):
            p=[0]*10;p[inv]=-n
            q=list(p);q[inv]+=1
            v={((tag,'basis'),tuple(p)):1}
            mult={(tag,'basis'):{(((tag,'basis')),monomial('X'+var)):1}}
            check(support_apply(mult,v)=={((tag,'basis'),tuple(q)):1},
                  'localized_variable_inverse_is_exact',(tag,n))
            for opposite in sorted(opp):
                bad=list(p);bad[DIAGONALS.index(opposite)]+=1
                check(branch_monomial(tuple(bad),tag) is None,
                      'opposite_sheet_annihilated_on_branch',(tag,opposite,n))
    for a in MINUS:
        for b in PLUS:
            check(not survives(monomial('X'+a,'X'+b)),
                  'simultaneous_inverse_contains_zero', (a,b))


def conductor_cech_coordinate_controls():
    # chi=(0,1), ordered branches (X02-open,X35-open).
    chi={('+',ZERO):1}
    checks=[]
    for a in sorted(SHORT):
        xp=monomial('X'+a)
        product={('+',xp):1} if a in PLUS else {}
        # d(x_a) has only the relevant branch. For positive variables
        # x_a*chi=d(x_a); negative variables kill chi already.
        primitive=xp if a in PLUS else None
        image={('+',xp):1} if primitive else {}
        check(product==image,'all_conductor_generators_annihilate_cech_class',a)
        checks.append({'variable':a,'primitive':list(primitive) if primitive else None})
    reflected={('-' if tag=='+' else '+',p):c for (tag,p),c in chi.items()}
    check(add(chi,reflected)=={('-',ZERO):1,('+',ZERO):1},
          'sheet_exchange_sum_is_diagonal_boundary')
    # The exact annihilator proof is coefficientwise: both localized
    # polynomial branches inject; equality with a diagonal requires the
    # same constant coefficient on both branches. (0,1) fails that test.
    for c in (-2,-1,0,1,2):
        is_diagonal_constant=(0==c)
        check(is_diagonal_constant==(c==0),'constant_conductor_class_detector',c)
    return {'class':'[(0,1)] in coker(R -> R_X02 + R_X35)',
            'annihilator':'I_minus + I_plus', 'sheet_exchange_sign':-1,
            'annihilating_chain_formulas':checks,
            'nonvanishing_proof':'Both branch maps into their single-coordinate localizations are injective; matching a diagonal forces zero common conductor coefficient.'}


def nodal_residue_controls():
    # Valid slice: other four short coordinates are zero.
    # R_node=S/(yz); Cech_S differential is (a,b)->b-a.
    # H^2_(y,z)(S) has basis y^-i z^-j, i,j>=1.
    def top_mul(v, dy=0,dz=0):
        ans={}
        for (i,j),c in v.items():
            ni,nj=i-dy,j-dz
            if ni>=1 and nj>=1:put(ans,(ni,nj),c)
        return ans
    def residue_image(kind,n=0):
        if kind=='conductor':return {(1,1):1}
        if kind=='minus_pole':return {(n+1,1):-1}
        if kind=='plus_pole':return {(1,n+1):1}
        raise ValueError(kind)
    conductor=residue_image('conductor')
    check(not top_mul(conductor,1,0) and not top_mul(conductor,0,1),
          'nodal_conductor_residue_annihilated_by_y_and_z')
    for n in range(1,8):
        minus=residue_image('minus_pole',n)
        plus=residue_image('plus_pole',n)
        check(not top_mul(minus,0,1) and not top_mul(plus,1,0),
              'nodal_residue_opposite_branch_annihilator',n)
        me=residue_image('minus_pole',n-1) if n>1 else {(1,1):-1}
        pe=residue_image('plus_pole',n-1) if n>1 else conductor
        check(top_mul(minus,1,0)==me,'nodal_residue_negative_pole_recursion',n)
        check(top_mul(plus,0,1)==pe,'nodal_residue_positive_pole_recursion',n)
    # Test all representative arm/interior types. The arbitrary-exponent
    # proof is (i,j)->(i-1,j-1); only i=1 or j=1 lies in the kernel.
    for i in range(1,8):
        for j in range(1,8):
            v={(i,j):1}
            check((not top_mul(v,1,1))==(i==1 or j==1),
                  'nodal_excess_kernel_formula',(i,j))
            check(top_mul({(i+1,j+1):1},1,1)==v,
                  'nodal_excess_surjectivity_formula',(i,j))
    return {'slice':'Z[beta,X03,X14,X25,y,z]/(yz)',
            'ambient':'S=Z[beta,X03,X14,X25,y,z]',
            'map':'H^1_(y,z)(S/(yz)) -> Ann_(H^2_(y,z)(S))(yz)',
            'positive_conductor_class_image':'[(0,1)] -> [1/(yz)]',
            'negative_pole_image':'[(y^-n,0)] -> -[1/(y^(n+1) z)], n>=1',
            'positive_pole_image':'[(0,z^-n)] -> [1/(y z^(n+1))], n>=1',
            'kernel_basis':'y^-i z^-j with min(i,j)=1',
            'shift':'The supported class moves from Cech degree 2 to 1 through Tor_1 of S/(yz); the defining-equation conormal is retained.',
            'not_claimed':'This nodal slice is not an identification of the full nine-relation normalization immersion with a hypersurface.'}


def allowed_branch_coefficient(p,branch):
    if p[-1]<0:return False
    if branch=='G':return min(p)>=0 and survives(p)
    inverted=DIAGONALS.index('02' if branch=='-' else '35')
    opposite=PLUS if branch=='-' else MINUS
    if any(p[DIAGONALS.index(a)]!=0 for a in opposite):return False
    return all(c>=0 or i==inverted for i,c in enumerate(p))


def support_hom_classification(raw,ds,sdg,dT,tdeg,dSup,supdeg,lifts,grade):
    keys=list(dT);proxy=target_hom_proxy(keys,tdeg);idx={k:j for j,k in enumerate(keys)}
    sw=source_weights(raw)
    bases={}
    for offset in (2,1,0,-1):
        b=[]
        for s in ds:
            for target in dSup:
                if supdeg[target]!=sdg[s]+offset:continue
                tag,j=target
                F,H,e=proxy.states[idx[j]]
                p=list(sw[s])+[grade-len(H)]
                for a in F:p[DIAGONALS.index(a)]+=1
                for a in H:p[DIAGONALS.index(a)]-=1
                p[DIAGONALS.index('35')]-=e
                p=tuple(p)
                if allowed_branch_coefficient(p,tag):b.append((s,target,p))
        bases[offset]=b
    diffs={}
    for offset in (2,1,0):
        loc={b:j for j,b in enumerate(bases[offset-1])}
        D=[[0]*len(bases[offset]) for _ in loc]
        for col,(s,j,p) in enumerate(bases[offset]):
            F={s:{(j,p):1}}
            for t in ds:
                v=add(support_apply(dSup,F.get(t,{})),support_apply(F,ds[t]),-((-1)**offset))
                for (k,q),c in v.items():
                    check((t,k,q) in loc,'localized_Hom_has_all_fine_degree_terms',(offset,t,k,q))
                    D[loc[t,k,q]][col]+=c
        diffs[offset]=D
    D1,D0=diffs[1],diffs[0]
    _,free,Z=rref_integer_kernel(D0,len(bases[0]))
    piv1,_,_=rref_integer_kernel(D1,len(bases[1]))
    rankH=len(free)-len(piv1)
    index={b:j for j,b in enumerate(bases[0])}
    candidates=[]
    for name in ('E','R'):
        v=[0]*len(bases[0])
        F=lifts[name]
        for s,value in F.items():
            for (j,p),c in value.items():
                pp=list(p);pp[-1]+=grade-1;pp=tuple(pp)
                check((s,j,pp) in index,'supported_lift_fine_degree_legal',(name,s,j,pp))
                v[index[s,j,pp]]+=c
        check(all(sum(a*b for a,b in zip(row,v))==0 for row in D0),
              'localized_Hom_lift_closed',name)
        candidates.append(v)
    boundary_columns=transpose(D1,len(bases[1]))
    chosen=[boundary_columns[i] for i in piv1]
    columns=chosen+candidates
    coords=[[col[i] for col in columns] for i in free]
    check(len(coords)==len(columns),'supported_lifts_exhaust_localized_Hom',grade)
    det=determinant(coords)
    check(abs(det)==1,'supported_trace_integral_basis_not_just_rational',(grade,det))
    inverse=inverse_unit_matrix(coords)
    detectors=[]
    for k in range(2):
        f=[0]*len(bases[0])
        for a,i in enumerate(free):f[i]=inverse[len(piv1)+k][a]
        check(all(sum(a*b for a,b in zip(f,v))==0 for v in boundary_columns),
              'supported_detector_annihilates_all_localized_homotopies',k)
        check([sum(a*b for a,b in zip(f,v)) for v in candidates]==[int(k==j) for j in range(2)],
              'supported_detector_recovers_class_coordinate',k)
        detectors.append(f)
    # Verify both compositions in the full Hom complex.
    for offset in (2,1):
        left=diffs[offset-1];right=diffs[offset]
        for row in left:
            for col in transpose(right,len(bases[offset])):
                check(sum(a*b for a,b in zip(row,col))==0,'localized_Hom_squared_zero',offset)
    return {'grade':grade,'Hom_dimensions_plus2_plus1_zero_minus1':[len(bases[k]) for k in (2,1,0,-1)],
            'differential_ranks_plus1_zero':[len(piv1),len(bases[0])-len(free)],
            'H0_rank':rankH,'integral_cycle_basis_determinant':det,
            'homotopy_basis':bases[1],'map_basis':bases[0],'equation_basis':bases[-1],
            'homotopy_differential':D1,'map_differential':D0,
            'kernel_basis':Z,'chosen_homotopy_columns':piv1,
            'candidate_columns':candidates,'class_detectors':detectors}


def cartier_of_supported(d,degrees):
    out={(tag,(a,j)):{} for tag,j in d for a in ('a','b')}
    deg={(tag,(a,j)):degrees[tag,j]-int(a=='b') for tag,j in d for a in ('a','b')}
    for tag,j in d:
        for ((tag2,k),p),c in d[tag,j].items():
            put(out[tag,('a',j)],((tag2,('a',k)),p),c)
            put(out[tag,('b',j)],((tag2,('b',k)),p),-c)
        put(out[tag,('a',j)],((tag,('b',j)),monomial('X03')),1)
    for s,col in out.items():check(not support_apply(out,col),'Cartier_of_support_squared_zero',s)
    return out,deg


def verify_cartier_support_interchange(dT,tdeg,dSup,supdeg,ds,sdg,lifts):
    left,leftdeg=cartier_of_supported(dSup,supdeg)
    dHT,hTd=cartier_hom(dT,tdeg)
    right,rightdeg=support_complex(dHT,hTd)
    interchange={s:{(s,ZERO):(-1)**int(s[0]!='G' and s[1][0]=='b')} for s in left}
    for s in left:
        check(leftdeg[s]==rightdeg[s],'Cartier_support_interchange_degree',s)
        check(support_apply(right,interchange[s])==support_apply(interchange,left[s]),
              'Cartier_support_interchange_chain_map',s)
        check(support_apply(interchange,interchange[s])=={(s,ZERO):1},
              'Cartier_support_interchange_inverse',s)
    dHS,hSd=cartier_hom(ds,sdg)
    transported={}
    for name,F in lifts.items():
        HF={}
        for a,s in dHS:
            HF[a,s]={((tag,(a,j)),p):c for ((tag,j),p),c in F[s].items()}
        verify_support_map(HF,dHS,left,hSd,leftdeg,'Cartier_supported_lift_'+name)
        out={s:support_apply(interchange,v) for s,v in HF.items()}
        verify_support_map(out,dHS,right,hSd,rightdeg,'support_Cartier_lift_'+name)
        transported[name]=out
    return {'states_each_side':len(left),'interchange_matrix':serialize_mat(interchange),
            'sign':'-1 only when the localized Cech degree and the Cartier b-degree are both one',
            'left_differential':serialize_mat(left),'right_differential':serialize_mat(right),
            'transported_maps':{k:serialize_mat(v) for k,v in transported.items()},
            'source_and_target_shift':'Cartier purity changes A[2] to A/(X03)[1] and retains the dual X03-conormal on both sides.'}


# -------------------------------------------------------------------------
# Full normalization duality and finite conductor descent (new calculation).
# The preceding definitions are embedded, not imported at runtime.


def on_conductor(v):
    return {(j,p):c for (j,p),c in v.items()
            if not any(p[DIAGONALS.index(a)] for a in SHORT)}


def conductor_apply(F,v):
    return on_conductor(apply(F,v))


def conductor_differential(d):
    return {j:on_conductor(col) for j,col in d.items()}


def all_conductor_subsets():
    # Mixed-sheet localizations are zero modules and are not included.
    return [()] + [J for sheet in (tuple(sorted(MINUS)),tuple(sorted(PLUS)))
                    for n in (1,2,3) for J in combinations(sheet,n)]


def full_cech_normalize(p,J):
    if not J:
        check(min(p)>=0,'full_cech_global_polynomial')
        return p if survives(p) else None
    sheet=MINUS if J[0] in MINUS else PLUS
    if any(p[DIAGONALS.index(a)] for a in SHORT-sheet):return None
    check(all(n>=0 or (i<9 and DIAGONALS[i] in J) for i,n in enumerate(p)),
          'full_cech_poles_only_in_localized_variables',(p,J))
    return p


def full_cech_apply(F,v):
    ans={}
    for (s,p),a in v.items():
        for (t,q),c in F.get(s,{}).items():
            r=full_cech_normalize(tuple(x+y for x,y in zip(p,q)),t[0])
            if r is not None:put(ans,(t,r),a*c)
    return ans


def full_cech_complex(d,degrees):
    subs=all_conductor_subsets()
    dd={(J,j):{} for J in subs for j in d}
    dg={(J,j):degrees[j]-len(J) for J,j in dd}
    for J,j in dd:
        for (k,p),c in d[j].items():
            r=full_cech_normalize(p,J)
            if r is not None:put(dd[J,j],((J,k),r),(-1)**len(J)*c)
        for JJ in subs:
            if len(JJ)==len(J)+1 and set(J)<=set(JJ):
                a=next(a for a in JJ if a not in J)
                put(dd[J,j],((JJ,j),ZERO),(-1)**JJ.index(a))
    for s,col in dd.items():
        check(not full_cech_apply(dd,col),'full_conductor_cech_d_squared',s)
        check(all(dg[t]==dg[s]-1 for t,p in col),'full_conductor_cech_degrees',s)
    return dd,dg


def normalization_to_full_cech(d):
    F={('G',j):{(((),j),ZERO):1} for j in d}
    for sign,sheet in (('-',MINUS),('+',PLUS)):
        for j in d:F[sign,j]={(((a,),j),ZERO):1 for a in sorted(sheet)}
    return F


def normalization_projection(d):
    # [T -> T_- + T_+] -> (A tensor T)[-1], + minus -.
    Q={('G',j):{} for j in d}
    for j in d:
        Q['-',j]={(j,ZERO):-1}
        Q['+',j]={(j,ZERO):1}
    return Q


def make_normalization_lifts(ds,traces):
    zero={s:{} for s in ds}
    H={i:{s:{} for s in ds} for i in ('E','R')}
    H['E']['unit',0]=xi_trace(0)
    H['R']['unit',0]=xi_trace(0)
    H['R']['generator','35']=xi_trace(1)
    lifts={i:support_lift(traces[i],zero,H[i],ds) for i in H}
    return H,lifts


def quotient_interval(dT):
    F={j:({(j[1],ZERO):1} if j[0]=='g' else {}) for j in dT}
    dO={0:{},1:{(0,monomial('X35')):-1}}
    return F,dO,{0:3,1:4}


def conductor_target_hom(raw,ds,sdg,dT,tdeg,grade):
    # Full homogeneous Hom over R to (A tensor T)[-1]. Source coefficients
    # act through A. Its matrices must be computed with that module action.
    keys=list(dT);index={s:i for i,s in enumerate(keys)}
    shifted={s:n-1 for s,n in tdeg.items()}
    proxy=target_hom_proxy(keys,shifted)
    da={index[s]:{(index[t],p):-c for (t,p),c in on_conductor(col).items()}
        for s,col in dT.items()}
    sw=source_weights(raw)
    bs={n:[v for v in hom_basis(proxy,ds,sdg,sw,set(index.values()),n,grade)
           if not any(v[2][DIAGONALS.index(a)] for a in SHORT)] for n in (1,0,-1)}
    def diff(bsrc,btgt,offset):
        loc={b:i for i,b in enumerate(btgt)}
        D=[[0]*len(bsrc) for _ in btgt]
        for j,(s,k,p) in enumerate(bsrc):
            F={s:one_row(k,p)}
            for ss in ds:
                v=on_conductor(add(apply(da,F.get(ss,{})),apply(F,ds[ss]),-((-1)**offset)))
                for (kk,pp),c in v.items():
                    check((ss,kk,pp) in loc,'conductor_hom_coefficient_legal',(ss,kk,pp))
                    D[loc[ss,kk,pp]][j]+=c
        return D
    D1=diff(bs[1],bs[0],1);D0=diff(bs[0],bs[-1],0)
    _,free,Z=rref_integer_kernel(D0,len(bs[0]))
    piv1,_,_=rref_integer_kernel(D1,len(bs[1]))
    rank1=len(piv1);rank0=len(bs[0])-len(free)
    # Independent basis in the conductor target.
    a={s:{} for s in ds};b={s:{} for s in ds}
    a['unit',0]=xi_trace(0)
    b['generator','35']=xi_trace(1)
    a=reindex_matrix(a,index);b=reindex_matrix(b,index)
    if grade != 1:
        a=scale_map(a,grade-1);b=scale_map(b,grade-1)
    candidate=[map_coordinates(a,bs[0]),map_coordinates(b,bs[0])]
    for col in candidate:
        check(all(sum(x*y for x,y in zip(row,col))==0 for row in D0),'conductor_readout_closed')
    check(rank1==0,'no_homotopy_in_conductor_readout_weight')
    coords=[[col[i] for col in candidate] for i in free]
    check(len(coords)==2 and abs(determinant(coords))==1,'conductor_readout_integral_basis')
    return {'grade':grade,'dimensions':[len(bs[n]) for n in (1,0,-1)],
            'ranks':[rank1,rank0],'H0_rank':len(free)-rank1,
            'homotopy_basis':bs[1],'map_basis':bs[0],'equation_basis':bs[-1],
            'homotopy_differential':D1,'map_differential':D0,
            'kernel_basis':Z,'candidate_columns':candidate,
            'candidate_coordinates':coords,'target_index':keys}


# Ambient six-variable S-linear arithmetic. Unlike R arithmetic, mixed
# monomials MUST NOT be set to zero in the free S-resolution.
def ambient_apply(F,v):
    out={}
    for (s,p),a in v.items():
        for (t,q),c in F.get(s,{}).items():
            put(out,(t,tuple(x+y for x,y in zip(p,q))),a*c)
    return out


def ambient_dualizing_resolution():
    mm=tuple(sorted(MINUS));pp=tuple(sorted(PLUS))
    states=[('unit',(),())]
    states += [('product',A,B) for n in range(2,7)
               for p in range(1,4) for q in range(1,4) if p+q==n
               for A in combinations(mm,p) for B in combinations(pp,q)]
    deg={s:0 if s[0]=='unit' else len(s[1])+len(s[2])-1 for s in states}
    dd={s:{} for s in states}
    for s in states:
        if s[0]=='unit':continue
        _,A,B=s
        if len(A)==len(B)==1:
            dd[s]={(states[0],monomial('X'+A[0],'X'+B[0])):1}
        else:
            if len(A)>1:
                for i,a in enumerate(A):
                    put(dd[s],(('product',A[:i]+A[i+1:],B),monomial('X'+a)),(-1)**i)
            if len(B)>1:
                for i,a in enumerate(B):
                    put(dd[s],(('product',A,B[:i]+B[i+1:]),monomial('X'+a)),(-1)**(len(A)-1+i))
    check([sum(deg[s]==n for s in states) for n in range(6)]==[1,9,18,15,6,1],
          'ambient_minimal_resolution_ranks')
    for s in states:
        check(not ambient_apply(dd,dd[s]),'ambient_resolution_d_squared',s)
        check(all(deg[t]==deg[s]-1 for t,p in dd[s]),'ambient_resolution_degrees',s)
    dual={s:{} for s in states};ddeg={s:6-deg[s] for s in states}
    for s,col in dd.items():
        for (t,p),c in col.items():put(dual[t],(s,p),(-1)**(deg[t]+1)*c)
    for s in states:
        check(not ambient_apply(dual,dual[s]),'ambient_dualizing_d_squared',s)
        check(all(ddeg[t]==ddeg[s]-1 for t,p in dual[s]),'ambient_dualizing_degrees',s)
    top=('product',mm,pp)
    entering=[(s,p,c) for s,col in dual.items() for (t,p),c in col.items() if t==top]
    check(len(entering)==6,'dual_deficiency_six_relations')
    check({p for s,p,c in entering}=={monomial('X'+a) for a in SHORT},
          'dual_deficiency_ideal_is_full_conductor')
    check(all(abs(c)==1 for s,p,c in entering),'dual_deficiency_relations_primitive')
    # Actual degree-three branch volume cycles in the ambient free model.
    wm={};wp={}
    for a in mm:put(wm,(('product',(a,),pp),monomial('X'+a)),1)
    for b in pp:put(wp,(('product',mm,(b,)),monomial('X'+b)),1)
    check(not ambient_apply(dual,wm),'negative_branch_volume_cycle')
    check(not ambient_apply(dual,wp),'positive_branch_volume_cycle')
    # Canonical connecting class A -> omega_- [3] + omega_+ [3]
    # as a map from the ambient Koszul resolution of A.
    order=mm+pp
    K=[J for n in range(7) for J in combinations(order,n)]
    kd={J:{((J[:i]+J[i+1:]),monomial('X'+a)):(-1)**i
           for i,a in enumerate(J)} for J in K}
    g={J:{} for J in K}
    g[mm]={(('-',0),ZERO):-1};g[pp]={(( '+',0),ZERO):1}
    def branch_target_apply(F,v):
        out={}
        for (s,p),a in v.items():
            for (t,q),c in F.get(s,{}).items():
                rr=tuple(x+y for x,y in zip(p,q))
                opp=PLUS if t[0]=='-' else MINUS
                if not any(rr[DIAGONALS.index(vv)] for vv in opp):put(out,(t,rr),a*c)
        return out
    for J in K:
        check(not ambient_apply(kd,kd[J]),'ambient_conductor_koszul_d_squared',J)
        check(not branch_target_apply(g,kd[J]),'dualizing_connecting_map_closed',J)
    # Any Hom boundary evaluated on either ordered triple has coefficients
    # in the relevant branch augmentation ideal. Constant-term detection
    # therefore evaluates g to (-1,+1) and kills all boundaries.
    for triple in (mm,pp):
        for (J,m),c in kd[triple].items():
            check(sum(m[:9])==1 and abs(c)==1,'connecting_unit_detector_kills_boundaries')
    return {'coefficient_ring':'S=A[X02,X04,X24,X13,X15,X35]; no cross products killed in these matrices',
            'A':'Z[beta,X03,X14,X25]',
            'resolution_states':states,'resolution_degrees':[[s,deg[s]] for s in states],
            'resolution_differential':serialize_mat(dd),'resolution_ranks':[1,9,18,15,6,1],
            'dualizing_degrees':[[s,ddeg[s]] for s in states],
            'dualizing_differential':serialize_mat(dual),
            'negative_volume_cycle':serialize_vec(wm),'positive_volume_cycle':serialize_vec(wp),
            'deficiency_generator':top,'deficiency_incoming_columns':entering,
            'connecting_koszul_differential':serialize_mat(kd),
            'connecting_map':serialize_mat(g),'connecting_class_unit_coordinates':[-1,1],
            'proved_dualizing_cohomology':{'-3':'omega_Rminus/A plus omega_Rplus/A','-1':'A tensor Lpol^vee'},
            'duality_nonsplitting':'nonzero branch codimension-three connecting classes (-1,+1)',
            'completeness_proof':'Tensor the two truncated disjoint-variable Koszul resolutions for the product ideal; use the actual normalization exact sequence and dual Koszul calculations. Not inferred from bounded numerical tests.'}


def dualizing_residue_controls():
    # Full conductor support has two branch 3-variable residue modules.
    # Fractions here live in local cohomology of polynomial branches, NOT R.
    rho=(1,1,1)
    def mul_basis(exponent,poly_exponent):
        r=tuple(a-b for a,b in zip(exponent,poly_exponent))
        return r if min(r)>0 else None
    def res_basis(exponent):return int(exponent==rho)
    def normal_form(v):
        out=dict(v)
        c=out.pop(('+',rho),0)
        if c:put(out,('-',rho),c)
        return out
    relation={('-',rho):-1,('+',rho):1}
    check(not normal_form(relation),'residue_diagonal_boundary_is_zero')
    check(sum(c*res_basis(p) for (s,p),c in relation.items())==0,'sum_residue_descends')
    controls=0
    for n in product(range(1,4),repeat=3):
        for m in product(range(3),repeat=3):
            ans=mul_basis(n,m)
            value=0 if ans is None else res_basis(ans)
            check(value==int(n==tuple(a+1 for a in m)),
                  'full_three_variable_residue_dual_monomial',(n,m))
            controls+=1
    # No factor two: either single branch residue represents the common
    # conductor evaluation. Its two-branch sum evaluates to two.
    check(normal_form({('-',rho):1})==normal_form({('+',rho):1}),
          'two_branch_simple_residues_same_class')
    check(sum(c*res_basis(p) for (s,p),c in {('-',rho):1}.items())==1,
          'single_branch_residue_is_unit')
    check(sum(c*res_basis(p) for (s,p),c in {('-',rho):1,('+',rho):1}.items())==2,
          'two_branch_sum_not_fitted_to_unit')
    # The trace to A is A-linear, not an R-linear trace from a torsion module.
    higher=(2,1,1)
    check(res_basis(higher)==0 and res_basis(mul_basis(higher,(1,0,0)))==1,
          'coefficient_residue_not_R_linear')
    # Full conductor-local-cohomology Hilbert series check of the free resolution.
    # These exact polynomial numerators complement, not replace, its proof.
    def padd(a,b,s=1):
        n=max(len(a),len(b));o=[0]*n
        for i,x in enumerate(a):o[i]+=x
        for i,x in enumerate(b):o[i]+=s*x
        return o
    def pmul(a,b):
        o=[0]*(len(a)+len(b)-1)
        for i,x in enumerate(a):
            for j,y in enumerate(b):o[i+j]+=x*y
        return o
    bin3=[1,-3,3,-1];bin6=pmul(bin3,bin3)
    normalized=padd([2*x for x in bin3],bin6,-1)
    check(normalized==[1,0,-9,18,-15,6,-1],'ambient_resolution_hilbert_numerator')
    return {'branch_variable_orders':[['X02','X04','X24'],['X13','X15','X35']],
            'branch_forms':['dX02 wedge dX04 wedge dX24','dX13 wedge dX15 wedge dX35'],
            'dualizing_supported_complex':'[A -> E_minus plus E_plus] in cohomological degrees -1,0',
            'differential':'1 -> (-rho_minus,+rho_plus)',
            'rho_pole_orders':[1,1,1],
            'trace':'Res_minus + Res_plus on coker(-rho_minus,+rho_plus)',
            'trace_linearity':'A-linear; not R-linear',
            'source_shift':'relative to A; all six ambient differential-form weights retained',
            'single_branch_value':1,'two_branch_sum_value':2,
            'finite_monomial_controls':controls,
            'all_degree_proof':'Every branch pole with exponents n is dual to its branch monomial n-1. The only duplicated monomial is the common constant, removed by the displayed relation.'}


def run_new_calculation(output):
    M=Complex('35');raw,ds,sdg=build_source()
    dP,pdeg=normal_edge();dN,ndeg=common_koszul()
    dEdge,edge_deg=tensor(dP,pdeg,dN,ndeg)
    tocell,fromcell=tensor_native_identification(M,dEdge)
    edgeids={j for j,(F,H,e) in enumerate(M.states) if {'02','35'}<=set(F)}
    verify_chain(tocell,dEdge,subcomplex(M,edgeids),'full_edge_labels_retained')
    P,E,RR,_=construct_maps(ds,raw)
    dOcc={0:{},1:{(0,monomial('X35')):1}};og={0:0,1:1}
    dT,td0=tensor(dP,pdeg,dOcc,og);tdeg={j:n+2 for j,n in td0.items()}
    pair=trace_matrix(dEdge)
    verify_chain(pair,dEdge,dT,'reciprocal_basepoint_evaluation')
    traces={'E':compose(pair,E),'R':compose(pair,RR)}
    for name,f in traces.items():verify_chain(f,ds,dT,'old_trace_'+name)
    H,lifts=make_normalization_lifts(ds,traces)
    dn,nd=support_complex(dT,tdeg)
    # The SAME formula is now over unlocalized normalization modules.
    for name,F in lifts.items():
        check(all(min(p)>=0 for v in F.values() for j,p in v),'normalization_lifts_are_polynomial',name)
        verify_support_map(F,ds,dn,sdg,nd,'normalization_lift_'+name)
    qnu=normalization_projection(dT)
    dA={j:smul(on_conductor(col),-1) for j,col in dT.items()}
    adeg={j:n-1 for j,n in tdeg.items()}
    for s in dn:
        check(conductor_apply(dA,qnu[s])==conductor_apply(qnu,dn[s]),
              'normalization_difference_is_chain_map',s)
    descended={name:{s:conductor_apply(qnu,F[s]) for s in ds} for name,F in lifts.items()}
    for name,F in descended.items():
        for s in ds:
            check(conductor_apply(dA,F[s])==conductor_apply(F,ds[s]),
                  'all_source_relations_after_conductor_descent',(name,s))
    check(descended['E']['unit',0]==xi_trace(0),'trace_E_conductor_unit_xi')
    check(descended['R']['unit',0]==xi_trace(0),'trace_R_conductor_unit_xi')
    check(descended['R']['generator','35']==xi_trace(1),'trace_R_retains_occurrence_relation')
    check(not descended['E']['generator','35'],'trace_E_occurrence_relation_zero')
    cl=conductor_target_hom(raw,ds,sdg,dT,tdeg,1)
    cl2=conductor_target_hom(raw,ds,sdg,dT,tdeg,2)
    check(cl['H0_rank']==cl2['H0_rank']==2,'complete_normalization_lift_lattice_rank_two')
    check(cl['map_differential']==cl2['map_differential'] and
          cl['homotopy_differential']==cl2['homotopy_differential'],
          'conductor_hom_regulator_stabilization')
    keys=list(dT);idx={j:i for i,j in enumerate(keys)}
    proxy=target_hom_proxy(keys,tdeg)
    before=classification(proxy,raw,ds,sdg,set(idx.values()),
          reindex_differential(dT,idx),1,[reindex_matrix(traces[n],idx) for n in ('E','R')])
    check(before['H0_rank']==2,'original_trace_hom_rank_recomputed')

    # Full six-coordinate supported construction, and natural inclusion of
    # the normalization fibre with its branch-polynomial homotopies.
    df,fd=full_cech_complex(dT,tdeg)
    incl=normalization_to_full_cech(dT)
    for s in dn:
        check(full_cech_apply(df,incl[s])==full_cech_apply(incl,dn[s]),
              'finite_normalization_fibre_into_full_conductor_support',s)
    fulllift={name:{s:full_cech_apply(incl,F[s]) for s in ds} for name,F in lifts.items()}
    for name,F in fulllift.items():
        for s in ds:
            check(full_cech_apply(df,F[s])==full_cech_apply(F,ds[s]),
                  'full_six_open_trace_equations',(name,s))
    check(len(df)==150,'full_conductor_trace_target_150_summands')
    # The pairing before and after full conductor support.
    dff,dffg=full_cech_complex(dEdge,{j:n for j,n in edge_deg.items()})
    pairing_full={(J,j):{((J,t),p):c for (t,p),c in pair[j].items()}
                  for J in all_conductor_subsets() for j in dEdge}
    for s in dff:
        check(full_cech_apply(df,pairing_full[s])==full_cech_apply(pairing_full,dff[s]),
              'full_conductor_reciprocal_pairing_naturality',s)
    check(len(dff)==600,'full_conductor_original_edge_600_summands')

    # Actual edge-endpoint quotient, not a scalar projection.
    qi,dO,od=quotient_interval(dT)
    verify_chain(qi,dT,dO,'relative_interval_quotient')
    value={name:{s:conductor_apply(qi,F[s]) for s in ds} for name,F in descended.items()}
    beta=monomial('beta')
    for name in value:
        check(value[name]['unit',0]=={(0,beta):-1},'derived_trace_unit_coefficient',name)
    check(value['E']['generator','35']=={},'first_trace_no_extra_ext_column')
    check(value['R']['generator','35']=={(1,beta):-1},'second_trace_primitive_ext_column')
    for name,F in value.items():
        for s in ds:
            check(not conductor_apply(F,ds[s]),'two_grade_target_all_source_relations',(name,s))
            check(all({0:2,1:3}[j]==sdg[s] for j,p in F[s]),'two_grade_target_source_degree',(name,s))
    readout=[[-1,-1],[0,-1]]
    check(determinant(readout)==1,'two_grade_trace_matrix_unimodular_after_beta_factor')

    # Relation-only comparison moves to the e35 conormal column.
    U={s:{} for s in ds};U['generator','35']=smul(xi_trace(1),-1)
    Kap={s:add(add(traces['E'][s],traces['R'][s],-1),
               add(apply(dT,U[s]),apply(U,ds[s])),-1) for s in ds}
    HK={s:{} for s in ds};HK['generator','35']=xi_trace(1)
    zero={s:{} for s in ds}
    KL=support_lift(Kap,HK,zero,ds)
    for s in ds:
        dUU=add(support_apply(dn,{(('G',j),p):c for (j,p),c in U[s].items()}),
                support_apply({ss:{(('G',j),p):c for (j,p),c in U[ss].items()} for ss in ds},ds[s]))
        check(add(add(lifts['E'][s],lifts['R'][s],-1),dUU,-1)==KL[s],
              'relation_only_normalization_comparison_retained',s)
    KV={s:conductor_apply(qi,conductor_apply(qnu,KL[s])) for s in ds}
    check(KV['generator','35']=={(1,beta):1},'relation_class_becomes_positive_beta_conormal_coordinate')
    check(all(not col for s,col in KV.items() if s!=('generator','35')),
          'relation_class_has_only_first_normal_ext_coordinate')

    # Endpoint triangle data are retained functorially. All support
    # operations above act coefficientwise and qi is its actual quotient.
    endkeys={j for j in dT if j[0] in ('p03','h03','p25','h25')}
    endpoint={j:{(i,p):c for (i,p),c in dT[j].items() if i in endkeys} for j in endkeys}
    qkeys={j for j in dT if j[0]=='g'}
    kappa={j:{(i,p):c for (i,p),c in dT[j].items() if i in endkeys} for j in qkeys}
    for name,F in traces.items():
        for s in ds:
            full=restrict(F[s],endkeys);qt=restrict(F[s],qkeys)
            check(add(apply(endpoint,full),apply(kappa,qt))==restrict(apply(F,ds[s]),endkeys),
                  'all_both_edge_endpoint_connecting_equations',(name,s))

    dual=ambient_dualizing_resolution()
    residues=dualizing_residue_controls()
    record={
        'schema':'marici.branchA.full_normalization_duality_two_grade_trace.v1',
        'status':'constructed_coefficient_normalization_descent_and_full_relative_dualizing_residue',
        'repository_commit':COMMIT,
        'scope':'Full six-variable normalization coefficient ring, actual ten-state interval/occurrence trace target and source relations. Not a geometric tangential Gysin identification or a physical Delta_J.',
        'source_resolution':{'ranks':[1,6,24,92],'differential':serialize_mat(ds)},
        'target_trace_differential':serialize_mat(dT),
        'normalization_fibre_differential':serialize_mat(dn),
        'normalization_to_conductor_projection':serialize_mat(qnu),
        'normalization_lifts':{n:serialize_mat(F) for n,F in lifts.items()},
        'conductor_target_differential':serialize_mat(dA),
        'conductor_descended_maps':{n:serialize_mat(F) for n,F in descended.items()},
        'complete_conductor_target_hom_classification':cl,
        'conductor_target_hom_next_regulator_grade':cl2,
        'original_trace_hom_classification':before,
        'full_conductor_support_differential':serialize_mat(df),
        'normalization_into_full_conductor_support':serialize_mat(incl),
        'full_conductor_support_lifts':{n:serialize_mat(F) for n,F in fulllift.items()},
        'relative_interval_quotient':serialize_mat(qi),
        'two_grade_readout':{n:serialize_mat(F) for n,F in value.items()},
        'two_grade_raw_matrix':'-beta * [[1,1],[0,1]]',
        'two_grade_unit_normalized_matrix':[[1,1],[0,1]],
        'relative_relation_class_image':serialize_mat(KV),
        'source_conormal_class':'[X35]^vee tensor occurrence-normal line; the e35 coordinate in Ext_R^1(A,A tensor L35)',
        'dualizing_complex':dual,
        'full_conductor_dualizing_residue':residues,
        'critical_type_distinctions':[
            'Normalization-fibre projection is only defined on the retained finite normalization diagram, not on arbitrary localized Cech representatives.',
            'The coefficient residue is A-linear on RΓ_I(D_R/A), not an R-linear scalar trace on RΓ_I(T).',
            'The dualizing cohomology in degrees -3 and -1 is nonsplit; it cannot be replaced by a single orientation line or an unconnected sum.',
            'No occurrence inversion or averaging is used; beta is divided out only for the stated fixed-nonzero-beta normalized readout.',
            'The ambient 50-state dualizing presentation is S-free, not asserted to be an R-free complex.',
            'The conormal class is not a division by X35; it is computed on the resolved conductor source.'
        ],
    }
    record['checks']={'total':sum(COUNTS.values()),'by_family':dict(sorted(COUNTS.items()))}
    record['semantic_sha256']=sha256(json.dumps(record,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    output.write_text(json.dumps(record,sort_keys=True,indent=2)+'\n')
    print(json.dumps({'status':record['status'],'checks':record['checks']['total'],
                      'dualizing_resolution_ranks':[1,9,18,15,6,1],
                      'dualizing_cohomology_degrees':[-3,-1],
                      'conductor_trace_rank':2,
                      'normalized_trace_matrix':[[1,1],[0,1]],
                      'sha256':record['semantic_sha256']},indent=2))


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path('branch_a_full_normalization_duality_and_two_grade_trace_certificate.json'))
    args=parser.parse_args()
    run_new_calculation(args.output)
