#!/usr/bin/env python3
"""Relative W03 Cartier Gysin comparison of the complete opposite-edge packet.

Reconstructs the 430-state coefficient complex, its 40-state edge, the
24-state relative corner, the six-generator conductor resolution through
all required relations, the Cartier Hom complexes, their counit and purity
maps, the retained W25 attachment, and physical reflection.

Standalone standard-library program. No network or companion files required.
"""
from __future__ import annotations
import argparse
from collections import Counter
from hashlib import sha256
from itertools import combinations
import json
from pathlib import Path

DIAGONALS = ('02','03','04','13','14','15','24','25','35')
PLUS = frozenset(('13','15','35'))
MINUS = frozenset(('02','04','24'))
SHORT = PLUS | MINUS
LONG = ('03','14','25')
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


SHORT_ORDER=tuple(sorted(SHORT))

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


# All new calculations below are reconstructed without reading companion files.

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


def specialize_nodal(v,x_value=1):
    # beta=1, X02=y, X35=z, X03=x_value, all remaining occurrences zero.
    out={}
    for (j,p),c in v.items():
        if any(p[k] for k,a in enumerate(DIAGONALS) if a not in ('02','35','03')):continue
        if x_value==0 and p[DIAGONALS.index('03')]:continue
        q=[0]*10
        q[DIAGONALS.index('02')]=p[DIAGONALS.index('02')]
        q[DIAGONALS.index('35')]=p[DIAGONALS.index('35')]
        put(out,(j,tuple(q)),c*(x_value**p[DIAGONALS.index('03')]))
    return out


def nodal_detector(v):
    # On M_1: coefficient of z at native 02 plus coefficient of y
    # at each of native 35 and occurrence 35.
    return v.get((1,monomial('X35')),0)+v.get((2,monomial('X02')),0)+v.get((4,monomial('X02')),0)



def conormal_detector(v):
    """Polynomial detector on M_1 with values in Z[beta,X03,X14,X25].

    beta*[X35](native02) + beta*[X02](native35) + [X02](occ35).
    Only conductor-linear coefficients enter; all other shorts are removed.
    It annihilates all M_2 boundaries, including polynomial multiples.
    """
    out={}
    for (j,p),z in v.items():
        shortpowers={a:p[DIAGONALS.index(a)] for a in SHORT}
        wanted='35' if j==1 else ('02' if j in (2,4) else None)
        if wanted is None or any(k!=int(a==wanted) for a,k in shortpowers.items()):
            continue
        q=list(p);q[DIAGONALS.index(wanted)]=0
        if j in (1,2):q[9]+=1
        put(out,tuple(q),z)
    return out

def serialize_vec(v):
    return [{'basis':j,'powers':list(p),'coefficient':z}
            for (j,p),z in sorted(v.items(),key=lambda kv:repr(kv[0]))]


def serialize_mat(F):
    return [{'source':j,'image':serialize_vec(v)} for j,v in sorted(F.items(),key=lambda kv:repr(kv[0]))]


def matrix_hash(record):
    return sha256(json.dumps(record,sort_keys=True,separators=(',',':')).encode()).hexdigest()


def main(output):
    M=Complex('35');raw,ds,sdg=build_source()
    E=('02','35');W03=('02','03','35');W25=('02','25','35')
    ids={j for j,(F,H,e) in enumerate(M.states) if set(E)<=set(F)}
    V25={j for j in ids if M.states[j][0]==W25}
    V03={j for j in ids if M.states[j][0]==W03}
    keep=ids-V25;dE=subcomplex(M,ids);dR=quotient(dE,keep)
    verify_d(dR,M.degree,'actual_relative_edge')
    q={j:(unit(j) if j in keep else {}) for j in ids}
    verify_chain(q,dE,dR,'actual_relative_quotient')
    check((len(ids),len(keep),len(V25),len(V03))==(40,24,16,16),'relative_ranks')
    L,U,Um,Gp,Gm,H=edge_map(M,ds,E)
    for Fmap in (Gp,Gm):
        for j,v in Fmap.items():
            check(not restrict(v,M.V|M.Q),'original_physical_endpoint_and_Q_values',j)
            check(not restrict(apply(M.d,v),M.V),'original_physical_endpoint_incoming',j)
    Lr=apply(q,L);Gr=compose(q,Gp);Gmr=compose(q,Gm);Hr=compose(q,H)
    verify_chain(Gr,ds,dR,'relative_conductor_map')
    for j in ds:
        check(add(apply(dR,Hr[j]),apply(Hr,ds[j]))==add(Gr[j],Gmr[j],-1),
              'relative_sheet_homotopy',j)
    # The omitted endpoint and its connecting map are retained as separate blocks.
    jrel={j:unit(j) for j in keep}
    kap={j:restrict(dE[j],V25) for j in keep};d25=quotient(dE,V25)
    G25={j:restrict(v,V25) for j,v in Gp.items()}
    for j in ds:
        check(add(apply(d25,G25[j]),apply(kap,Gr[j]))==apply(G25,ds[j]),
              'discarded_endpoint_full_map_equation',j)
    cut=compose(jrel,Gr)
    defect={j:add(apply(dE,cut[j]),apply(cut,ds[j]),-1) for j in ds}
    expected=one_row(M.index[W25,('02',),0],monomial('beta','beta','X25','X35'),-1)
    check(defect['unit',0]==expected,'exact_companion_primary_defect')

    dM,mdeg=common_koszul();dP,pdeg=normal_edge();dt,td=tensor(dP,pdeg,dM,mdeg)
    J,Ji=tensor_native_identification(M,dt)
    verify_chain(J,dt,dE,'full_edge_tensor_factorization')
    check(compose(J,Ji)=={j:unit(j) for j in ids},'full_tensor_inverse_native')
    check(compose(Ji,J)=={j:unit(j) for j in dt},'full_tensor_inverse_factor')
    prkeys={'p03','g','h03'}
    dpr={j:restrict(dP[j],prkeys) for j in prkeys}
    dtr,trdeg=tensor(dpr,pdeg,dM,mdeg)
    Jr={j:J[j] for j in dtr};Jri={j:Ji[j] for j in keep}
    verify_chain(Jr,dtr,dR,'relative_tensor_factorization')
    verify_chain(Jri,dR,dtr,'relative_tensor_inverse')
    relfactor=compose(Jri,Gr)
    zeta={('h03',ZERO):1,('g',monomial('beta')):-1}
    # Pi_zeta is the projection to the free excess summand M[1].
    dzeta,zdeg=shift_complex(dM,mdeg,1)
    pi_zeta={j:unit(j[1]) if j[0]=='h03' else {} for j in dtr}
    izeta={(m):{(('h03',m),ZERO):1,(('g',m),monomial('beta')):-1} for m in dM}
    verify_chain(pi_zeta,dtr,dzeta,'excess_projection')
    verify_chain(izeta,dzeta,dtr,'excess_inclusion')
    check(compose(pi_zeta,izeta)=={j:unit(j) for j in dM},'excess_split')
    gx=compose(pi_zeta,relfactor)
    check(compose(izeta,gx)==relfactor,'entire_map_lands_in_excess_summand')
    check(apply(Jri,Lr)=={(('h03',3),ZERO):1,(('g',3),monomial('beta')):-1},
          'relative_primitive_exact_excess_form')
    check(gx['unit',0]==one_row(1,monomial('beta','X35')),'relative_primary_excess_form')
    for a in PLUS:check(gx['generator',a]==one_row(3,monomial('X'+a)),
                        'relative_source_generator_excess_form',a)
    # Polynomial beta times the endpoint retraction. No inverse beta needed here.
    rr={j:{} for j in dtr}
    for p,m in dtr:
        if p=='g':rr[p,m]=one_row(('h03',m))
        else:rr[p,m]=one_row((p,m),monomial('beta'))
    corner={j:v for j,v in dtr.items() if j[0] in ('p03','h03')}
    verify_chain(rr,dtr,corner,'regularized_corner_retraction')
    for j,v in compose(rr,relfactor).items():check(not v,'corner_retraction_kills_entire_map',j)

    # Complete affine Cartier costalk, source retyping, and naturality.
    dHR,hrdeg=cartier_hom(dR,M.degree)
    dpurity,purity,counit,kd,ki,kh=cartier_purity(dR,M.degree,dHR)
    dHS,hsdeg=cartier_hom(ds,sdg)
    ds_purity,ps,trs,_,_,_=cartier_purity(ds,sdg,dHS)
    iF=cartier_induced(Gr,ds)
    verify_chain(iF,dHS,dHR,'Cartier_induced_resolved_map')
    verify_chain(compose(counit,iF),dHS,dR,'Cartier_source_counit_composite')
    check(compose(counit,iF)==compose(Gr,trs),'Cartier_counit_naturality')
    F_D={j:mod_x(v) for j,v in Gr.items()}
    for j in dHS:
        check(mod_x(apply(purity,iF[j]))==mod_x(apply(F_D,ps[j])),
              'Cartier_purity_naturality',j)
    # Counit on the excess summand is zero on homology. Its cycle input's
    # first component is x-torsion; x acts injectively on H(M)[1].
    # Concrete independent detector after x=1 (and also after x=0 for i^!F).
    for m in dM:
        if mdeg[m]==2:
            check(nodal_detector(specialize_nodal(dM[m]))==0,
                  'nodal_functional_kills_all_degree2_boundary_columns',m)
    for m in dM:
        if mdeg[m]==2:
            check(not conormal_detector(dM[m]),'polynomial_conormal_boundary_detector',m)
            for name in VARIABLES:
                check(not conormal_detector(multiply(dM[m],monomial(name))),
                      'polynomial_conormal_boundary_module_generators',(m,name))
    polynomial_value=conormal_detector(gx['unit',0])
    check(polynomial_value=={monomial('beta','beta'):1},
          'polynomial_primary_detector_is_beta_squared')
    for a in SHORT_ORDER:
        check(apply(dR,Gr['generator',a])==multiply(Gr['unit',0],monomial('X'+a)),
              'six_exact_primary_annihilator_homotopies',a)
    # The Cartier first normal Bockstein is (g,h)->(p,beta*p).
    bockP={'p03':{},'g':unit('p03'),'h03':one_row('p03',monomial('beta'))}
    check(not apply(bockP,zeta),'relative_excess_in_Bockstein_kernel')
    det1=nodal_detector(specialize_nodal(gx['unit',0],1))
    det0=nodal_detector(specialize_nodal(gx['unit',0],0))
    check((det1,det0)==(1,1),'generic_and_Cartier_supported_nonvanishing')
    # At x=1 Hom(K(x),C) is contracted by (a,b)->(b,0).
    dH1={j:specialize_nodal(v,1) for j,v in dHR.items()}
    h1={j:(unit(('a',j[1])) if j[0]=='b' else {}) for j in dH1}
    for j in dH1:
        check(add(apply(dH1,h1[j]),apply(h1,dH1[j]))==unit(j),
              'x_unit_Cartier_costalk_contraction',j)

    # Transport the retained endpoint and the actual source maps under f3.
    N=Complex('04');Np={j:reflect_chain(M,N,unit(j)) for j in M.d}
    for j in M.d:
        check(reflect_chain(M,N,M.d[j])==apply(N.d,Np[j]),'physical_f3_full_chain_map',j)
        check(reflect_chain(N,M,Np[j])==unit(j),'physical_f3_involution',j)
    Ep=('04','13');W03p=('03','04','13');W14p=('04','13','14')
    idsN={j for j,(F,H,e) in enumerate(N.states) if set(Ep)<=set(F)}
    removedN={j for j in idsN if N.states[j][0]==W14p};keepN=idsN-removedN
    dEN=subcomplex(N,idsN);dRN=quotient(dEN,keepN)
    qN={j:(unit(j) if j in keepN else {}) for j in idsN}
    Ln,Un,Umn,Gpn,Gmn,Hn=edge_map(N,ds,Ep)
    check(reflect_map(M,N,raw,Gp)==Gmn,'physical_positive_to_negative_source_map')
    check(reflect_chain(M,N,L)==smul(Ln,-1),'physical_relative_orientation')
    Trel={j:restrict(Np[j],keepN) for j in keep}
    for j in keep:
        check(reflect_chain(M,N,dR[j])==apply(dRN,Trel[j]),'physical_relative_chain_map',j)
    for j in ids:
        check(restrict(reflect_chain(M,N,unit(j)),keepN)==reflect_chain(M,N,q[j]),
              'physical_relative_quotient_naturality',j)
    dHN,hndeg=cartier_hom(dRN,N.degree)
    Tcart=cartier_induced(Trel,dR)
    # Semilinearity fixes x03 and beta, transports all other X labels.
    for j,v in dHR.items():
        out={}
        for ((component,state),p),c in v.items():
            for (i,pp),z in reflect_chain(M,N,{(state,p):c}).items():
                put(out,((component,i),pp),z)
        check(out==apply(dHN,Tcart[j]),'physical_Cartier_Hom_naturality',j)

    # Reciprocal native/original pairing, before using any residue value.
    # Generic Laurent ring Z[b,x,q,q^-1]: verify u+q*u_dual=0 and determinant q.
    def laurent_mul(a,b):
        out={}
        for p,c in a.items():
            for q,z in b.items():put(out,tuple(x+y for x,y in zip(p,q)),c*z)
        return out
    u={(1,1,0):1};udual={(1,1,-1):-1};qm={(0,0,1):1}
    check(not add(u,laurent_mul(qm,udual)),'reciprocal_pairing_d_squared_contract')
    # Evaluation(p,hvee)=1, Evaluation(h,pvee)=-q.
    pairdet={(0,0,1):1}
    check(laurent_mul(pairdet,{(0,0,-1):1})=={(0,0,0):1},
          'reciprocal_pairing_perfect_unit_determinant')

    records={
       'coefficient_variables':VARIABLES,
       'coefficient_ring_relations':'X_minus*X_plus=0; x=X03 remains regular; beta is not inverted',
       'original_physical_endpoint_state_indices':sorted(M.V),
       'original_full_Q_state_indices':sorted(M.Q),
       'state_basis_430':[{'index':j,'face':F,'marks':H,'occurrence':e,'degree':M.degree[j]}
                           for j,(F,H,e) in enumerate(M.states)],
       'source_resolution':serialize_mat(ds),
       'edge_differential_40':serialize_mat(dE),
       'relative_differential_24':serialize_mat(dR),
       'relative_projection':serialize_mat(q),
       'discarded_endpoint_connecting_map':serialize_mat(kap),
       'full_positive_map':serialize_mat(Gp),
       'relative_positive_map':serialize_mat(Gr),
       'discarded_endpoint_map':serialize_mat(G25),
       'full_sheet_homotopy':serialize_mat(H),
       'relative_sheet_homotopy':serialize_mat(Hr),
       'relative_cut_defect':serialize_mat(defect),
       'common_Koszul_differential':serialize_mat(dM),
       'normal_edge_differential':serialize_mat(dP),
       'full_tensor_identification':serialize_mat(J),
       'relative_tensor_identification':serialize_mat(Jr),
       'relative_tensor_inverse':serialize_mat(Jri),
       'excess_inclusion':serialize_mat(izeta),
       'excess_projection':serialize_mat(pi_zeta),
       'excess_source_map':serialize_mat(gx),
       'beta_regularized_corner_retraction':serialize_mat(rr),
       'Cartier_Hom_target_differential_48':serialize_mat(dHR),
       'Cartier_Hom_source_differential_246':serialize_mat(dHS),
       'Cartier_induced_map':serialize_mat(iF),
       'Cartier_purity_matrix':serialize_mat(purity),
       'Cartier_counit_matrix':serialize_mat(counit),
       'Cartier_purity_kernel_inclusion':serialize_mat(ki),
       'Cartier_purity_kernel_contraction':serialize_mat(kh),
       'physical_reflection_relative':serialize_mat(Trel),
       'physical_reflection_Cartier':serialize_mat(Tcart),
       'normal_Cartier_Bockstein':serialize_mat(bockP),
       'polynomial_conormal_detector_value':[{'powers':list(p),'coefficient':z} for p,z in polynomial_value.items()],
       'relative_primary_exact_annihilator':'I=(X02,X04,X13,X15,X24,X35)',
       'nonvanishing_detector_at_x1':det1,
       'nonvanishing_detector_after_supported_retyping_at_x0':det0,
       'scope':{
         'relative_corner_complex_constructed':True,
         'Cartier_source_and_target_costalk_constructed':True,
         'same_unrestricted_source_lift_through_Cartier_counit':False,
         'retyped_source':'A/(X03)[1] tensor dual Cartier conormal, via i^!(A[2])',
         'physical_scalar_residue_assigned':False,
         'physical_Delta_J_identified':False,
         'geometric_KN_at_beta_zero_claimed':False},
       'exact_checks':dict(sorted(COUNTS.items()))}
    records['matrix_sha256']=matrix_hash({k:v for k,v in records.items() if k not in ('exact_checks','matrix_sha256')})
    Path(output).write_text(json.dumps(records,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'output':str(output),'new_and_reconstructed_exact_checks':sum(COUNTS.values()),
       'matrix_sha256':records['matrix_sha256'],
       'relative_rank':24,'Cartier_Hom_rank':48,
       'relative_map_lands_in_excess':True,'same_source_Gysin_lift':False,
       'retyped_Gysin_map_nonzero':True},indent=2))


if __name__=='__main__':
    ap=argparse.ArgumentParser(description='Relative W03 Cartier Gysin audit; no network or companion files')
    ap.add_argument('--output',default=str(Path(__file__).with_name('branch_a_relative_w03_cartier_gysin_certificate.json')))
    main(ap.parse_args().output)
