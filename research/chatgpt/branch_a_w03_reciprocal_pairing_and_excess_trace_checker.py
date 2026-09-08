#!/usr/bin/env python3
"""Verify W03 reciprocal two-normal currying and the independent excess traces.

Standard-library only; no network, companion files, or optional packages.
Reconstructs the full cellular differential and conductor resolution,
checks the raw reciprocal pairing with Laurent monodromy units, and
computes integral trace classes before and after relative Cartier purity.
"""
from __future__ import annotations
import argparse
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from itertools import combinations
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

def run_reciprocal(output: Path):
    M=Complex('35');raw,ds,sdg=build_source()
    dP,pd=normal_edge();dM,md=common_koszul();dt,td=tensor(dP,pd,dM,md)
    to_native,from_native=tensor_native_identification(M,dt)
    ids={j for j,(F,H,e) in enumerate(M.states) if {'02','35'}<=set(F)}
    dEdge=subcomplex(M,ids)
    verify_chain(to_native,dt,dEdge,'edge_tensor_native_identification')
    check(compose(to_native,from_native)=={j:unit(j) for j in ids},'native_tensor_inverse')
    P,E,Rm,Xi=construct_maps(ds,raw)
    maps={'P':P,'E':E,'R':Rm}
    for name,F in maps.items():verify_chain(F,ds,dt,'original '+name)
    L,up,um,Gnative,Gnegative,Hsheet=edge_map(M,ds,('02','35'))
    G={s:add(multiply(P[s],monomial('beta')),E[s]) for s in ds}
    check(compose(to_native,G)==Gnative,'actual_source_map_decomposition_replayed')
    native_maps={name:compose(to_native,F) for name,F in maps.items()}
    for name,F in native_maps.items():
        for s,v in F.items():
            check(not restrict(v,M.V|M.Q),'physical_endpoints_and_Q_retained',(name,s))
            check(not restrict(apply(M.d,v),M.V),'incoming_physical_endpoint_zero',(name,s))

    # Leave the occurrence factor unpaired. The native-pair orientation
    # contributes homological shift +2 and occurrence weight eps02+eps35.
    dO={0:{},1:{(0,monomial('X35')):1}};od={0:0,1:1}
    dT,td0=tensor(dP,pd,dO,od);tdeg={k:v+2 for k,v in td0.items()}
    verify_d(dT,tdeg,'native_pair_output_shift2')
    dD,ddg=native_dual(True);verify_d(dD,ddg,'normalized_reciprocal_pair')
    dHom,hdeg=hom_complex_finite(dD,ddg,dT,tdeg)
    verify_d(dHom,hdeg,'full_native_reciprocal_Hom')
    C,CI=curry_matrix(dt)
    verify_chain(C,dt,dHom,'native_pair_currying')
    verify_chain(CI,dHom,dt,'native_pair_uncurrying')
    check(compose(C,CI)=={j:unit(j) for j in dHom},'currying_inverse_on_all_40_Hom_states')
    check(compose(CI,C)=={j:unit(j) for j in dt},'currying_inverse_on_all_40_edge_states')
    check(determinant(polynomial_normal_pair_matrix())==-1,'normalized_two_normal_pair_determinant')

    # Raw reciprocal coefficients are -q^-1 beta X; only q-units are used.
    dDr,_=native_dual(False);dTr=lift_laurent(dT);dtr=lift_laurent(dt)
    dHr,_=hom_complex_finite(dDr,ddg,dTr,tdeg)
    Cr,CIr=curry_matrix(dt,True)
    lverify(Cr,dtr,dHr,'raw_native_pair_currying')
    lverify(CIr,dHr,dtr,'raw_native_pair_uncurrying')
    check(lcompose(CIr,Cr)=={j:lunit(j) for j in dt},'raw_unit_inverse_all_edge_states')
    check(lcompose(Cr,CIr)=={j:lunit(j) for j in dHr},'raw_unit_inverse_all_Hom_states')
    Dframe={m:{(m,lmono(q02=-int(not(m&1)),q35=-int(not(m&2)))):
                  (-1)**(2-m.bit_count())} for m in range(4)}
    lverify(Dframe,lift_laurent(dD),dDr,'reciprocal_frame_change')
    for j in dt:
        for dual in range(4):
            normalized={}
            for (dref,p),c in Dframe[dual].items():
                for ((dtarget,t),q),a in Cr[j].items():
                    if dtarget==dref:put(normalized,(t,tuple(x+y for x,y in zip(p,q))),c*a)
            expected={(t,p+(0,0)):a for ((dref,t),p),a in C[j].items() if dref==dual}
            check(normalized==expected,'raw_to_normalized_pairing_all_160_columns',(j,dual))

    # Tensor evaluation is a full 160-to-10 chain map, not only a
    # complementary-degree determinant calculation.
    dPair,pairdeg=tensor(dt,td,dD,ddg)
    ev={j:{} for j in dPair}
    for j in ev:
        edge_state,dual=j
        ev[j]={ (t,p):a for ((dref,t),p),a in C[edge_state].items() if dref==dual}
    verify_chain(ev,dPair,dT,'full_160_state_evaluation')
    J=trace_matrix(dt);verify_chain(J,dt,dT,'closed_reciprocal_basepoint_trace')
    evUnit={(d,t):(unit(t) if d==0 else {}) for d,t in dHom}
    verify_chain(evUnit,dHom,dT,'evaluate_curried_map_at_closed_basepoint')
    check(compose(evUnit,C)==J,'two_definitions_of_trace_agree')

    curr={name:compose(C,F) for name,F in maps.items()}
    traces={name:compose(J,F) for name,F in maps.items()}
    for name in maps:
        verify_chain(curr[name],ds,dHom,'curried resolved '+name)
        verify_chain(traces[name],ds,dT,'unit trace resolved '+name)
    check(all(not v for v in traces['P'].values()),'primary_basis_trace_zero')
    check(compose(J,G)==traces['E'],'specified_source_trace_equals_E_trace')

    # Literal expected unit-slot maps, including both endpoints of the
    # edge and all first-relation columns.
    def xi_occ(e,poly=ZERO):
        return { (('h03',e),poly):1,(('h25',e),poly):1,
                (('g',e),tuple(a+b for a,b in zip(poly,monomial('beta')))):-1}
    CE={s:{} for s in ds};CR={s:{} for s in ds}
    for a in sorted(PLUS):CE['generator',a]=xi_occ(0,monomial('X'+a))
    for a in ('13','15'):CR['generator',a]=xi_occ(0,monomial('X'+a))
    for i,rel in enumerate(raw['relations']):
        tag=rel['name']
        if tag[0]=='K' and tag[1] in PLUS and tag[2]=='35':CR['relation',i]=xi_occ(1,monomial('X'+tag[1]))
    check(CE==traces['E'] and CR==traces['R'],'explicit_trace_formula_all_source_relations')

    # Comparing the two traces exposes a source-relation-only class.
    relation_homotopy={s:{} for s in ds}
    relation_homotopy['generator','35']=smul(xi_occ(1),-1)
    relation_only={s:{} for s in ds}
    for i,rel in enumerate(raw['relations']):
        tag=rel['name']
        if tag[0]=='M' and tag[1] in MINUS and tag[2]=='35':
            relation_only['relation',i]=xi_occ(1,monomial('X'+tag[1]))
    verify_chain(relation_only,ds,dT,'trace_relation_only_cocycle')
    for s in ds:
        dh=add(apply(dT,relation_homotopy[s]),apply(relation_homotopy,ds[s]))
        check(add(add(CE[s],CR[s],-1),dh,-1)==relation_only[s],
              'trace_difference_retains_mixed_source_relations',s)

    # The reciprocal b-bar slot is not a closed test. Its differential
    # supplies exactly the information needed to retain the primary.
    Bslot={s:{(t,p):c for ((dref,t),p),c in compose(C,G)[s].items() if dref==2} for s in ds}
    for s in ds:
        delta=add(apply(dT,Bslot[s]),apply(Bslot,ds[s]))
        check(delta==multiply(traces['E'][s],monomial('beta','X35')),
              'reciprocal_boundary_ties_primary_to_trace',s)

    # Independent integral classifications, with complete polynomial
    # coefficient exponents forced by the fine gradings.
    original_classification=[]
    for grade in (2,3):
        candidates=[scale_map(native_maps['P'],grade-2)]
        if grade==3:candidates += [native_maps['E'],native_maps['R']]
        original_classification.append(classification(M,raw,ds,sdg,ids,dEdge,grade,candidates))
    keys=list(dT);index={key:i for i,key in enumerate(keys)}
    T=target_hom_proxy(keys,tdeg);dTi=reindex_differential(dT,index)
    ti={name:reindex_matrix(F,index) for name,F in traces.items()}
    trace_classification=[]
    for grade in (0,1,2):
        candidates=[] if grade==0 else [scale_map(ti['E'],grade-1),scale_map(ti['R'],grade-1)]
        trace_classification.append(classification(T,raw,ds,sdg,set(index.values()),dTi,grade,candidates))
    check(trace_classification[1]['H0_rank']==trace_classification[2]['H0_rank']==2,
          'trace_classes_independent_and_exhaustive')
    check(trace_classification[1]['homotopy_differential']==trace_classification[2]['homotopy_differential']
          and trace_classification[1]['map_differential']==trace_classification[2]['map_differential'],
          'all_higher_trace_regulator_grades_stabilize')

    relation_only_i=reindex_matrix(relation_only,index)
    relation_coords=map_coordinates(relation_only_i,trace_classification[1]['map_basis'])
    trace_detectors=trace_classification[1]['candidate_functionals']
    check([sum(x*y for x,y in zip(f,relation_coords)) for f in trace_detectors]==[1,-1],
          'mixed_relation_class_is_primitive_difference_of_two_traces')

    # The unit test together with the original primary separates all
    # three source-map classes. The primary coordinate is read using P.
    check(not traces['E']['unit',0] and not traces['R']['unit',0],
          'both_trace_classes_are_zero_primary')
    p_common={(m,p):c for ((normal,m),p),c in P['unit',0].items() if normal=='h03'}
    check(primary_coefficient_detector(p_common)=={monomial('beta'):1},
          'independent_original_primary_detector')
    joint_matrix=[[1,0,0],[0,1,0],[0,0,1]]
    check(determinant(joint_matrix)==1,'joint_primary_and_trace_coordinates_complete')

    # Opposite endpoint W25 remains with its connecting map. It is not
    # replaced by either physical central endpoint.
    removed={key for key in dT if key[0] in ('p25','h25')}
    kept=set(dT)-removed
    d25={j:restrict(v,removed) for j,v in dT.items() if j in removed}
    dRel={j:restrict(v,kept) for j,v in dT.items() if j in kept}
    kappa={j:restrict(dT[j],removed) for j in kept}
    rtr={name:{s:restrict(v,kept) for s,v in F.items()} for name,F in traces.items()}
    vtr={name:{s:restrict(v,removed) for s,v in F.items()} for name,F in traces.items()}
    for name in traces:
        verify_chain(rtr[name],ds,dRel,'relative unit trace '+name)
        for s in ds:
            check(add(apply(d25,vtr[name][s]),apply(kappa,rtr[name][s]))==apply(vtr[name],ds[s]),
                  'all_opposite_endpoint_comparison_columns',(name,s))

    # Cartier applied to source and target; both acquire the same -1
    # shift and the same dual X03-conormal line under purity.
    dHS,hSd=cartier_hom(ds,sdg);_,ps,trS,*_=cartier_purity(ds,sdg,dHS)
    dHT,hTd=cartier_hom(dRel,tdeg);_,pt,trT,*_=cartier_purity(dRel,tdeg,dHT)
    cartier_maps={}
    for name in traces:
        CF=cartier_induced(rtr[name],ds);cartier_maps[name]=CF
        verify_chain(CF,dHS,dHT,'Cartier reciprocal unit trace '+name)
        check(compose(trT,CF)==compose(rtr[name],trS),'Cartier_counit_commutes_with_trace',name)
        for s in dHS:
            check(mod_x(apply(pt,CF[s]))==mod_x(apply(rtr[name],ps[s])),
                  'Cartier_purity_commutes_with_trace',(name,s))
    retained_ids={index[j] for j in kept}
    dRelativeDivisor={index[j]:{(index[t],p):c for (t,p),c in mod_x(col).items()}
                      for j,col in dRel.items()}
    onDiv={name:reindex_matrix({s:mod_x(v) for s,v in F.items()},index) for name,F in rtr.items()}
    cartier_classification=classification(T,raw,ds,sdg,retained_ids,dRelativeDivisor,1,
                                          [onDiv['E'],onDiv['R']],True)
    check(cartier_classification['H0_rank']==4 and cartier_classification['candidate_count']==2,
          'two_trace_classes_survive_inside_four_dimensional_divisor_Hom')

    # Swapping the ordered native normal pair reverses its determinant.
    # Both original and reciprocal exterior signs must participate.
    for m in range(4):
        for n in range(4):
            swap=lambda a:((a&1)<<1)|((a&2)>>1)
            left=native_pairing_bit_coefficient(m,n)
            right=native_pairing_bit_coefficient(swap(m),swap(n))
            lv=0 if left is None else left[1]
            rv=0 if right is None else right[1]*(-1)**(int(m==3)+int(n==3))
            check(rv==-lv,'ordered_pair_swap_has_determinant_minus_one',(m,n))

    # Transport original source maps under the supplied physical reflection.
    # The pairing's normal order is transported as (02,35)->(13,04),
    # not silently re-sorted. The previous tests give the re-sort sign.
    N=Complex('04')
    for j in M.d:
        image=reflect_chain(M,N,unit(j))
        check(reflect_chain(M,N,M.d[j])==apply(N.d,image),'physical_reflection_full_chain',j)
        check(reflect_chain(N,M,image)==unit(j),'physical_reflection_square_full_chain',j)
    reflected={}
    for name,F in native_maps.items():
        rf=reflect_map(M,N,raw,F);reflected[name]=rf
        verify_chain(rf,ds,N.d,'reflected source '+name)
        check(reflect_map(N,M,raw,rf)==F,'reflected_source_map_involution',name)

    record={
      'schema':'marici.branchA.w03_reciprocal_pairing_and_excess_trace.v1',
      'source_commit':COMMIT,
      'status':'verified_full_reciprocal_currying_and_two_independent_excess_traces',
      'scope':{'coefficient_ring':'Z[beta,X_d]/(I_minus I_plus); raw normal pairing adjoins only monodromy units q02,q35',
        'source':'P_A[2], free conductor resolution with ranks 1,6,24,92',
        'paired_factors':'native 02 and native 35 only',
        'unpaired_factors':'complete two-endpoint interval and separate occurrence 35',
        'normal_orientation':'ordered native pair (02,35), shift +2; occurrence degree eps02+eps35',
        'raw_pairing_values':['B(p,h_dual)=1','B(h,p_dual)=-q'],
        'reciprocal_frame':'p_bar=-q^{-1} p_dual; h_bar=h_dual',
        'normalization':'unit reciprocal input is pbar02 tensor pbar35 = (q02 q35)^-1 pdual02 tensor pdual35',
        'scalar_trace_claim':False,'physical_Delta_J_identified':False,
        'full_spatial_Gysin_identified':False,'no_occurrence_inverse':True,'no_normal_or_beta_inverse':True},
      'result':{'full_currying_is_chain_isomorphism':True,'currying_state_counts':[40,40],
        'bilinear_evaluation_state_counts':[160,10],
        'closed_basepoint_trace_matrix_on_grade3_basis':[[0,1,0],[0,0,1]],
        'basis_order':['beta P','E','R'],
        'trace_basis':['nu_E','nu_R'],'source_G_coordinates':[1,1,0],
        'source_G_trace_coordinates':[1,0],'collapsed_G_trace_coordinates':[0,0],
        'trace_Hom_module':'Lambda(-1) nu_E + Lambda(-1) nu_R before adding the paired orientation grade 2',
        'trace_kernel_in_original_module':'Lambda(-2) P',
        'joint_primary_trace_matrix':joint_matrix,
        'Cartier_divisor_Hom_rank':4,'Cartier_trace_image_rank':2,
        'Cartier_trace_image_saturated':True},
      'source_differential':serialize_mat(ds),
      'native_edge_identification':serialize_mat(to_native),
      'edge_differential':serialize_mat(dt),'original_basis_maps':{n:serialize_mat(F) for n,F in maps.items()},
      'original_G':serialize_mat(G),
      'reciprocal_normalized_differential':serialize_mat(dD),
      'reciprocal_raw_differential':serialize_mat(dDr),'raw_polynomial_variable_order':LAURENT_VARIABLES,
      'reciprocal_frame_matrix':serialize_mat(Dframe),
      'raw_currying_matrix':serialize_mat(Cr),'raw_uncurrying_matrix':serialize_mat(CIr),
      'normalized_currying_matrix':serialize_mat(C),'normalized_uncurrying_matrix':serialize_mat(CI),
      'curried_target_differential':serialize_mat(dHom),
      'bilinear_evaluation':serialize_mat(ev),'reduced_trace_target_differential':serialize_mat(dT),
      'trace_matrix':serialize_mat(J),'unit_trace_maps':{n:serialize_mat(F) for n,F in traces.items()},
      'full_curried_maps':{n:serialize_mat(F) for n,F in curr.items()},
      'trace_relation_only_map':serialize_mat(relation_only),
      'trace_relation_comparison_homotopy':serialize_mat(relation_homotopy),
      'trace_relation_only_coordinates':[1,-1],
      'reciprocal_b35_slot_of_original_map':serialize_mat(Bslot),
      'opposite_endpoint_differential':serialize_mat(d25),
      'opposite_endpoint_connecting_map':serialize_mat(kappa),
      'opposite_endpoint_trace_values':{n:serialize_mat(F) for n,F in vtr.items()},
      'relative_trace_values':{n:serialize_mat(F) for n,F in rtr.items()},
      'original_integral_classification':original_classification,
      'trace_integral_classification':trace_classification,
      'Cartier_trace_integral_classification':cartier_classification,
      'Cartier_source_differential':serialize_mat(dHS),'Cartier_relative_target_differential':serialize_mat(dHT),
      'Cartier_maps':{n:serialize_mat(F) for n,F in cartier_maps.items()},
      'reflected_original_source_maps':{n:serialize_mat(F) for n,F in reflected.items()},
    }
    record['semantic_sha256']=sha256(json.dumps(record,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    record['checks']={'total':sum(COUNTS.values()),'by_family':dict(sorted(COUNTS.items()))}
    output.write_text(json.dumps(record,sort_keys=True,indent=2)+'\n')
    print(json.dumps({'status':record['status'],'checks':record['checks']['total'],
      'trace_rank':2,'trace_of_G':[1,0],'Cartier_image_rank':2,
      'sha256':record['semantic_sha256']},indent=2))

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,
      default=Path('branch_a_w03_reciprocal_pairing_and_excess_trace_certificate.json'))
    args=parser.parse_args()
    run_reciprocal(args.output)
