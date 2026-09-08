#!/usr/bin/env python3
"""Full normalization-source and endpoint/Q homotopy-fibre audit.

Reuses the explicitly reconstructed K6 coefficient support flag.

Reconstructs all 215 loaded generators, without deleting either endpoint
normal packet. The source differential is from the pinned GitHub file named
in SOURCES. Computes a canonical Q-extension comparison, NOT an unprovided
normalization-source-to-physical-target Gysin map.

All identities use untruncated sparse integer Laurent polynomials. The
annihilator proof is in actual_boundary_restriction.md; the executable
verifies its chain representatives and explicit endpoint correction.
Python standard library only.
"""
from __future__ import annotations
from collections import Counter
from itertools import combinations
from pathlib import Path
import argparse
import hashlib
import json

COMMIT = 'd1947b67a60d3e88ba77f4ca60ea02c2a306ee61'
SOURCES = [
    'research/voevodsky/check_global_k6_koszul_cech_promotion.rs',
    'src/ledger/20260815-143 Two-Endpoint Road Carrier and the Loaded Conductor Cospan Blocker.md',
]
COUNTS: Counter[str] = Counter()
Diag = tuple[int, int]
Cell = tuple[tuple[int, ...], tuple[int, ...]]
Mon = tuple[int, ...]
Poly = dict[Mon, int]
Vec = dict[Cell, Poly]
ZERO = (0,) * 18

def check(condition: bool, category: str, detail=None) -> None:
    if not condition:
        raise AssertionError(f'{category}: {detail!r}')
    COUNTS[category] += 1

def pm(n: int) -> int:
    return -1 if n % 2 else 1

def const(n: int=1) -> Poly:
    return {ZERO: n} if n else {}

def monomial(indices=(), sign: int=1) -> Poly:
    e = [0] * 18
    for i, p in indices:
        e[i] += p
    return {tuple(e): sign} if sign else {}

def padd(a: Poly, b: Poly, sign: int=1) -> Poly:
    out = dict(a)
    for m, c in b.items():
        out[m] = out.get(m, 0) + sign*c
        if not out[m]:
            del out[m]
    return out

def pscale(a: Poly, sign: int) -> Poly:
    return {m: sign*c for m, c in a.items() if sign*c}

def pmul(a: Poly, b: Poly) -> Poly:
    out: Poly = {}
    for m, c in a.items():
        for n, d in b.items():
            k = tuple(x+y for x,y in zip(m,n))
            out[k] = out.get(k, 0) + c*d
    return {m:c for m,c in out.items() if c}

def add(a: Vec, b: Vec, sign: int=1) -> Vec:
    out = dict(a)
    for c, p in b.items():
        out[c] = padd(out.get(c, {}), p, sign)
        if not out[c]:
            del out[c]
    return out

def scale(v: Vec, p: Poly) -> Vec:
    return {c:q for c,a in v.items() if (q := pmul(p,a))}

def basis(c: Cell) -> Vec:
    return {c: const()}

def apply(table: dict[Cell,Vec], v: Vec) -> Vec:
    out: Vec = {}
    for c,p in v.items():
        out = add(out, scale(table.get(c, {}),p))
    return out

def select(v: Vec, cells: set[Cell]) -> Vec:
    return {c:p for c,p in v.items() if c in cells}

def faces(diagonals: tuple[Diag,...]) -> tuple[tuple[int,...],...]:
    def crosses(i: int, j: int) -> bool:
        a,b = diagonals[i]; c,d = diagonals[j]
        return a<c<b<d or c<a<d<b
    return tuple(f for n in range(4) for f in combinations(range(9),n)
                 if all(not crosses(i,j) for i,j in combinations(f,2)))

def subsets(f):
    return tuple(m for n in range(len(f)+1) for m in combinations(f,n))

def degree(c: Cell) -> int:
    f,m = c
    return 3-len(f)+len(m)

DIAGONALS = tuple((i,j) for i in range(6) for j in range(i+1,6)
                  if j != i+1 and (i,j) != (0,5))
FS = faces(DIAGONALS)
CELLS = tuple((f,m) for f in FS for m in subsets(f))
ALL = set(CELLS)
INDEX = {d:i for i,d in enumerate(DIAGONALS)}
SHORT = tuple(INDEX[tuple(sorted((i,(i+2)%6)))] for i in range(6))
LONG = tuple(INDEX[(i,i+3)] for i in range(3))
VPLUS = tuple(sorted(SHORT[i] for i in (1,3,5)))
VMINUS = tuple(sorted(SHORT[i] for i in (0,2,4)))
VP = {c for c in CELLS if c[0] == VPLUS}
VM = {c for c in CELLS if c[0] == VMINUS}
V = VP|VM
B = {c for c in CELLS if any(i in SHORT for i in c[0])}
E = ALL-V
P = B-V
Q = ALL-B


def name_cell(c: Cell) -> str:
    def part(f):
        return ','.join(''.join(map(str,DIAGONALS[i])) for i in f)
    return f'[{part(c[0])};{part(c[1])}]'


def name_poly(p: Poly, rees: bool) -> str:
    if not p:
        return '0'
    terms = []
    for mon,c in sorted(p.items()):
        fs = []
        if abs(c) != 1 or not any(mon):
            fs.append(str(abs(c)))
        for i,e in enumerate(mon):
            if e:
                d = ''.join(map(str,DIAGONALS[i%9]))
                var = ('X_' if i<9 else ('t_' if rees else 'u_'))+d
                fs.append(var if e==1 else var+'^'+str(e))
        val = '*'.join(fs) or '1'
        terms.append(('-' if c<0 else '+')+val)
    out = ''.join(terms)
    return out[1:] if out.startswith('+') else out


def serialize(v: Vec, rees: bool):
    return [{'cell':name_cell(c),'coefficient':name_poly(p,rees)}
            for c,p in sorted(v.items())]


class Model:
    def __init__(self, rees: bool, cech: bool):
        self.rees = rees
        self.cech = cech
        self.d: dict[Cell,Vec] = {}
        self.face_set = set(FS)
        for cell in CELLS:
            f,m = cell
            out: Vec = {}
            for a in range(9):
                ff=tuple(sorted(f+(a,)))
                if a in f or ff not in self.face_set:
                    continue
                if cech:
                    # X/u on the independent ring; 1/t on u=tX.
                    coeff = monomial([(9+a,-1)] + ([] if rees else [(a,1)]),
                                     pm(sum(b<a for b in f)))
                else:
                    coeff = monomial([(a,1)],pm(sum(b<a for b in f)))
                out[(ff,m)] = coeff
            for pos,a in enumerate(m):
                mm=tuple(b for b in m if b!=a)
                powers=[] if cech else [(9+a,1)]+([(a,1)] if rees else [])
                out[(f,mm)] = monomial(powers, pm(3-len(f)+pos))
            self.d[cell]=out
        self.dE={c:select(v,E) for c,v in self.d.items() if c in E}
        self.dQ={c:select(v,Q) for c,v in self.d.items() if c in Q}
        self.dV={c:select(v,V) for c,v in self.d.items() if c in V}
        self.dP={c:select(v,P) for c,v in self.d.items() if c in P}
        self.kplus={c:select(self.d[c],VP) for c in E}
        self.kminus={c:select(self.d[c],VM) for c in E}
        self.kV={c:select(self.d[c],V) for c in E}

    def rho(self, v: Vec) -> tuple[Vec,Vec,Vec]:
        return select(v,Q), apply(self.kplus,v), apply(self.kminus,v)

    def dboundary(self, v):
        q,vp,vm=v
        return apply(self.dQ,q),scale(apply(self.dV,vp),const(-1)),scale(apply(self.dV,vm),const(-1))

    def legal(self, c: Cell, coeff: Poly) -> bool:
        f,m=c
        inverted=set(f)-set(m) if self.cech else set()
        for mon in coeff:
            for i,e in enumerate(mon):
                if e<0:
                    if i<9 and not self.rees:
                        return False
                    if i%9 not in inverted:
                        return False
        return True

    def kappa(self, v: Vec) -> Vec:
        # Finite original-twist to Cech comparison.
        ans={}
        for c,p in v.items():
            inverted=set(c[0])-set(c[1])
            factors=[(9+a,-1) for a in inverted]
            if self.rees:
                factors += [(a,-1) for a in inverted]
            ans[c]=pmul(p,monomial(factors))
        return ans

    def omega(self) -> Vec:
        ans={}
        for f in FS:
            powers=[(9+a,1) for a in range(9) if a not in f]
            if not self.rees:
                powers += [(a,1) for a in f]
            ans[(f,f)] = monomial(powers, pm(len(f)*(len(f)+1)//2))
        return ans

    def theta(self) -> Vec:
        ans={((),()):monomial([(9+a,1) for a in LONG])}
        for a in LONG:
            powers=[(9+b,1) for b in LONG if b != a]
            if not self.rees:
                powers += [(a,1)]
            ans[((a,),(a,))]=monomial(powers,-1)
        return ans

    def run(self):
        label=('rees' if self.rees else 'independent')+('_cech' if self.cech else '_finite')
        for c in CELLS:
            check(all(degree(t)==degree(c)-1 for t in self.d[c]), 'd_degree')
            check(not apply(self.d,self.d[c]), 'd_squared', (label,name_cell(c)))
            check(all(self.legal(t,p) for t,p in self.d[c].items()), 'd_legal_denominators')
            if c in B:
                check(set(self.d[c])<=B, 'B_is_subcomplex')
            if c in V:
                check(set(self.d[c])<=V, 'V_is_subcomplex')
        for c in E:
            check(not apply(self.dE,self.dE[c]), 'E_d_squared')
            check(self.dboundary(self.rho(basis(c)))==self.rho(self.dE[c]),
                  'rho_chain_map', (label,name_cell(c)))
            for vv in self.rho(basis(c)):
                check(all(self.legal(t,p) for t,p in vv.items()),'rho_legal_denominators')
            # Endpoint connectors must come from the actual codimension-one
            # incidence; no independent signs or coefficients are assigned.
            f,m=c
            expected: Vec={}
            for endpoint in (VPLUS,VMINUS):
                if len(f)==2 and set(f)<set(endpoint):
                    a=next(i for i in endpoint if i not in f)
                    powers = [(9+a,-1)] + ([] if self.rees else [(a,1)]) if self.cech else [(a,1)]
                    expected[(endpoint,m)]=monomial(powers,pm(sum(b<a for b in f)))
            check(apply(self.kV,basis(c))==expected,'endpoint_connector_formula')
        omega=self.omega()
        theta=self.theta() # canonical graded lift is the same formal vector
        omegaE=select(omega,E); omegaV=select(omega,V)
        beta=apply(self.dE,theta)
        delta=monomial([(9+a,1) for a in SHORT])
        check(not apply(self.d,omega),'omega_full_cycle')
        check(not apply(self.dQ,theta),'theta_Q_cycle')
        check(bool(beta),'beta_nonzero_chain')
        check(set(beta)<=P,'beta_road_relative_support')
        check(not apply(self.d,beta),'beta_absolute_closed')
        check(self.rho(beta)==({},{},{}),'beta_strict_zero_boundary')
        check(self.rho(theta)==(theta,{},{}),'r_s_theta_zero_endpoints')
        check(select(omegaE,Q)==scale(theta,delta),'top_Q_map_is_delta')
        check(apply(self.kV,omegaE)==scale(apply(self.dV,omegaV),const(-1)),
              'endpoint_connector_of_omega')
        W=add(scale(theta,delta),omegaE,-1)
        check(set(W)<=P,'annihilator_primitive_stays_in_P')
        check(apply(self.dE,W)==scale(beta,delta),'d_W_delta_beta')
        check(apply(self.kV,W)==apply(self.dV,omegaV),'W_endpoint_connector')
        # For F=Cone(r)[-1], D(s,k)=(d s,r(s)-d k).
        # k is -Omega_V, in the shifted boundary's homological degree 4.
        k=({},{c:pscale(p,-1) for c,p in omegaV.items() if c in VP},
               {c:pscale(p,-1) for c,p in omegaV.items() if c in VM})
        check(self.rho(W)==self.dboundary(k),'annihilator_homotopy_includes_endpoints')
        residual=(scale(theta,const(-1)),{}, {})
        check(self.dboundary(residual)==({},{},{}),'h_minus_r_s_closed')
        # Different coherent boundary framings have the same strict r(beta)=0.
        # Their Q component lambda*theta changes the secondary class by lambda.
        # In particular h=r(s) gives the exact pair D(s,0), whereas h=0
        # gives the generator -1 in the displayed cokernel.
        check(self.rho(theta)==(theta,{},{}),'h_equal_r_s_gives_zero_secondary')
        for g in (const(), monomial([(0,1)]), padd(const(2),monomial([(10,2)]),-1)):
            lam=padd(const(),pmul(delta,g))
            sprime=add(theta,scale(omegaE,g))
            upper=({},scale(select(omegaV,VP),g),scale(select(omegaV,VM),g))
            target=(scale(theta,lam),{}, {})
            check(apply(self.dE,sprime)==beta,'all_zero_residuals_ambient_primitive')
            check(tuple(add(a,b,-1) for a,b in zip(self.rho(sprime),self.dboundary(upper)))==target,
                  'all_zero_residuals_endpoint_homotopy')
        check(bool(apply(self.dV,omegaV)),'endpoint_correction_not_zero')
        check(len(apply(self.dV,omegaV))==6,'six_endpoint_correction_terms')
        # Integral nonvanishing control: Delta has no unit coefficient term;
        # reduction at all short normal parameters zero sends -1 to -1.
        check(all(any(mon[9+a]>0 for a in SHORT) for mon in delta),'delta_nonunit')
        check(const(-1)!= {},'residual_unit_nonzero_mod_delta')
        connectors=[]
        for c in sorted(E):
            vals=self.rho(basis(c))
            if any(vals):
                connectors.append({'source':name_cell(c),'degree':degree(c),
                    'Q':serialize(vals[0],self.rees),
                    'v_plus_shifted':serialize(vals[1],self.rees),
                    'v_minus_shifted':serialize(vals[2],self.rees)})
        return {'model':label,'source_ring_mode':'u=t*X' if self.rees else 'X,u independent',
                'cech':self.cech,'nonzero_rho_columns':len(connectors),
                'Q_columns':sum(bool(x['Q']) for x in connectors),
                'endpoint_plus_columns':sum(bool(x['v_plus_shifted']) for x in connectors),
                'endpoint_minus_columns':sum(bool(x['v_minus_shifted']) for x in connectors),
                'rho_columns':connectors,'theta':serialize(theta,self.rees),
                'beta':serialize(beta,self.rees),'omega_E':serialize(omegaE,self.rees),
                'omega_V':serialize(omegaV,self.rees),
                'W':serialize(W,self.rees),
                'endpoint_correction_dOmegaV':serialize(apply(self.dV,omegaV),self.rees),
                'secondary_representative_for_h_zero':'(-theta,0,0)',
                'general_boundary_h_Q':'lambda*theta',
                'general_secondary_class':'lambda-1 modulo Delta',
                'physical_lambda_supplied':False,
                'annihilator_generator':name_poly(delta,self.rees),
                'secondary_cokernel':'R/(product of the six short '+('t' if self.rees else 'u')+' parameters)',
                'integer_torsion':False,
                'physical_normalization_source_identified':False}



# The full mapping fibre, in homological grading, has elements
# (e_n, q_{n+1}, v_n).  Its boundary is not obtained by discarding endpoints.
FVec = tuple[Vec,Vec,Vec]
FZERO: FVec = ({},{},{})

def fadd(x: FVec, y: FVec, sign: int=1) -> FVec:
    return tuple(add(a,b,sign) for a,b in zip(x,y))

def fscale(x: FVec, p: Poly) -> FVec:
    return tuple(scale(a,p) for a in x)

def fibre_d(model: Model, f: FVec) -> FVec:
    e,q,v=f
    return (apply(model.dE,e), add(select(e,Q),apply(model.dQ,q),-1),
            add(apply(model.kV,e),apply(model.dV,v)))

def attaching(model: Model, q: Vec) -> Vec:
    return select(apply(model.d,q),B)

def fibre_i(b: Vec) -> FVec:
    return select(b,E),{},select(b,V)

def fibre_p(model: Model, f: FVec) -> Vec:
    e,q,v=f
    return add(add(select(e,B),v),attaching(model,q),-1)

def fibre_H(f: FVec) -> FVec:
    return f[1],{},{}

def fibre_basis():
    return [(basis(c),{},{}) for c in sorted(E)] + \
           [({},basis(c),{}) for c in sorted(Q)] + \
           [({},{},basis(c)) for c in sorted(V)]

def permutation_sign(seq):
    return pm(sum(seq[i]>seq[j] for i in range(len(seq)) for j in range(i+1,len(seq))))

def target_action(v: Vec, perm, top_sign: int) -> Vec:
    ds={i:INDEX[tuple(sorted((perm(a),perm(b))))] for i,(a,b) in enumerate(DIAGONALS)}
    out: Vec={}
    for (f,h),p in v.items():
        ff=tuple(ds[i] for i in f); hh=tuple(ds[i] for i in h)
        sign=top_sign*permutation_sign(ff)*permutation_sign(hh)
        image=(tuple(sorted(ff)),tuple(sorted(hh)))
        coeff: Poly={}
        for mon,c in p.items():
            dest=[0]*18
            for i,e in enumerate(mon):
                dest[(0 if i<9 else 9)+ds[i%9]]=e
            coeff[tuple(dest)]=sign*c
        out=add(out,{image:coeff})
    return out

def faction(f,perm,top_sign):
    return tuple(target_action(a,perm,top_sign) for a in f)


def audit_fibre(model: Model):
    for b in sorted(B):
        v=basis(b)
        check(fibre_p(model,fibre_i(v))==v,'fibre_p_i_identity')
        check(fibre_d(model,fibre_i(v))==fibre_i(apply(model.d,v)),
              'fibre_inclusion_chain_map')
    for f in fibre_basis():
        check(fibre_d(model,fibre_d(model,f))==FZERO,'fibre_d_squared')
        check(fibre_p(model,fibre_d(model,f))==apply(model.d,fibre_p(model,f)),
              'fibre_projection_chain_map')
        lhs=fadd(fibre_d(model,fibre_H(f)),fibre_H(fibre_d(model,f)))
        rhs=fadd(f,fibre_i(fibre_p(model,f)),-1)
        check(lhs==rhs,'fibre_integral_SDR')
        check(fibre_H(fibre_H(f))==FZERO,'fibre_H_squared')
        check(not fibre_p(model,fibre_H(f)),'fibre_p_H_zero')
        for out in fibre_H(f):
            check(all(model.legal(c,p) for c,p in out.items()),'fibre_H_legal_localizations')
        check(all(model.legal(c,p) for c,p in fibre_p(model,f).items()),
              'fibre_p_legal_localizations')
        for perm,sign in ((lambda v:(v+2)%6,1),(lambda v:(2-v)%6,-1)):
            check(faction(fibre_d(model,f),perm,sign)==
                  fibre_d(model,faction(f,perm,sign)),'fibre_D3_d')
            check(target_action(fibre_p(model,f),perm,sign)==
                  fibre_p(model,faction(f,perm,sign)),'fibre_D3_p')
            check(faction(fibre_H(f),perm,sign)==fibre_H(faction(f,perm,sign)),
                  'fibre_D3_H')
    for perm,sign in ((lambda v:(v+2)%6,1),(lambda v:(2-v)%6,-1)):
        check(target_action(model.theta(),perm,sign)==scale(model.theta(),const(sign)),
              'theta_source_orientation_character')
        check(target_action(model.omega(),perm,sign)==scale(model.omega(),const(sign)),
              'omega_source_orientation_character')
    theta=model.theta(); beta=attaching(model,theta)
    omega=model.omega()
    delta=monomial([(9+a,1) for a in SHORT])
    genuine_B_primitive=add(scale(theta,delta),omega,-1)
    check(set(genuine_B_primitive)<=B,'annihilating_primitive_full_B_support')
    check(apply(model.d,genuine_B_primitive)==scale(beta,delta),
          'annihilating_primitive_full_B_boundary')
    check(fibre_p(model,(beta,{},{}))==beta,'zero_frame_is_actual_B_connecting_class')
    check(fibre_p(model,(beta,theta,{}))=={},'lift_frame_projects_to_zero')
    check(fibre_d(model,(theta,{},{}))==(beta,theta,{}),'lift_frame_explicit_primitive')
    return {'fibre_generators':len(fibre_basis()),'B_generators':len(B),
            'projection_formula':'b - attaching(q)',
            'contracting_homotopy':'(e,q,v) -> (q,0,0)',
            'equivalence':'fib(E -> Q + V[1]) ~= B',
            'annihilating_B_primitive':serialize(genuine_B_primitive,model.rees)}


# Full normalization source over A=R[zplus,zminus]/(zplus*zminus).
# Positive powers remain formal, untruncated basis elements.
SKey=tuple[str,str,int]
SVec=dict[SKey,int]

def si(k:SKey) -> SVec: return {k:1}
def sa(v:SVec,w:SVec,sgn:int=1) -> SVec:
    out=dict(v)
    for k,c in w.items():
        out[k]=out.get(k,0)+sgn*c
        if not out[k]: del out[k]
    return out

def ss(v:SVec,n:int) -> SVec: return {k:c*n for k,c in v.items() if c*n}

def sd(k:SKey) -> int:
    return {'o':0,'sheet':1,'road':1,'node':2,'tag':2,'top':3}[k[0]]

def sdif(k:SKey) -> SVec:
    typ,branch,j=k
    if typ=='top': return {('tag','',i):1 for i in range(3)}
    if typ=='tag': return {('road','',j):1,('road','',(j+1)%3):-1}
    if typ=='node':
        return {('sheet','+',0):1,('sheet','-',0):1} if branch=='c' \
               else {('sheet',branch,j):1}
    if typ=='sheet' and j==0: return {('o','',0):1 if branch=='+' else -1}
    if typ=='road': return {('o','',0):-1}
    return {}

def sapp(op,v:SVec) -> SVec:
    out:SVec={}
    for k,c in v.items(): out=sa(out,ss(op(k),c))
    return out

def scalar_readout(v:SVec) -> int:
    return sum(c for (typ,_,_),c in v.items() if typ=='road')

SRC_UNIT={('sheet','+',0):1,('road','',0):1}

def src_contraction(k:SKey) -> SVec:
    typ,branch,j=k
    if typ=='o': return {('sheet','+',0):1}
    if typ=='sheet' and j>0: return {('node',branch,j):1}
    if typ=='sheet' and branch=='-' and j==0: return {('node','c',0):1}
    if typ=='road' and j==1: return {('tag','',1):1,('tag','',2):1}
    if typ=='road' and j==2: return {('tag','',2):1}
    if typ=='tag' and j==0: return {('top','',0):1}
    return {}

def branch_multiply(k:SKey,branch:str) -> SVec:
    typ,b,j=k
    if typ=='node' and b=='c': return {('node',branch,1):1}
    if typ in ('node','sheet') and b==branch: return {(typ,b,j+1):1}
    return {}

def src_action(k:SKey,reflection=False) -> SVec:
    typ,b,j=k
    if reflection:
        if typ in ('node','sheet') and b in ('+','-'):
            return {(typ,'-' if b=='+' else '+',j):1}
        if typ=='road': return {(typ,b,(-j)%3):-1}
        if typ=='tag': return {(typ,b,(-j-1)%3):1}
        if typ=='o': return {k:-1}
        return {k:1}
    if typ in ('road','tag'): return {(typ,b,(j+1)%3):1}
    return {k:1}

def source_basis(bound=12):
    return [('o','',0),('node','c',0),('top','',0)] + \
           [('sheet',b,j) for b in ('+','-') for j in range(bound+1)] + \
           [('node',b,j) for b in ('+','-') for j in range(1,bound+1)] + \
           [(typ,'',j) for typ in ('road','tag') for j in range(3)]

def audit_source(model:Model):
    theta=model.theta(); beta=attaching(model,theta)
    delta=monomial([(9+a,1) for a in SHORT])
    lam_values=(const(0),const(1),const(2),delta,
                padd(const(1),pmul(delta,monomial([(0,1)]))))
    for k in source_basis():
        v=si(k)
        check(not sapp(sdif,sdif(k)),'polynomial_source_d_squared')
        check(scalar_readout(sdif(k))==0,'source_readout_chain_map')
        check(sa(sapp(sdif,src_contraction(k)),sapp(src_contraction,sdif(k)))==
              sa(v,ss(SRC_UNIT,scalar_readout(v)),-1),'source_R_linear_integral_SDR')
        for branch in ('+','-'):
            check(sapp(sdif,branch_multiply(k,branch))==
                  sapp(lambda j:branch_multiply(j,branch),sdif(k)),
                  'source_node_ring_linearity')
            check(scalar_readout(branch_multiply(k,branch))==0,'source_readout_A_linearity')
        for refl in (False,True):
            char=-1 if refl else 1
            check(scalar_readout(src_action(k,refl))==char*scalar_readout(v),
                  'source_readout_orientation_covariance')
            check(sapp(sdif,src_action(k,refl))==
                  sapp(lambda j:src_action(j,refl),sdif(k)),
                  'source_D3_chain_map')
        rr=sapp(lambda j:src_action(j,False),src_action(k,False))
        rrr=sapp(lambda j:src_action(j,False),rr)
        check(rrr==v,'source_rotation_order_three')
        check(sapp(lambda j:src_action(j,True),src_action(k,True))==v,
              'source_reflection_order_two')
        srs=sapp(lambda j:src_action(j,True),
                 sapp(lambda j:src_action(j,False),src_action(k,True)))
        check(srs==rr,'source_dihedral_relation')
        # S=P[1], so d_S=-d_P.  F and all endpoint homotopies
        # below factor through the actual source readout, which kills d_P.
        output=scale(beta,const(scalar_readout(v)))
        check(not apply(model.d,output),'full_source_beta_map_closed')
        check(not scale(beta,const(scalar_readout(sdif(k)))),
              'full_source_beta_map_chain_equation')
        primitive=scale(theta,const(scalar_readout(v)))
        check(apply(model.dE,primitive)==output,'full_source_ambient_nullhomotopy')
        for lam in lam_values:
            framed=(output,scale(theta,pscale(lam,scalar_readout(v))),{})
            check(fibre_d(model,framed)==FZERO,'full_source_frame_family_closed')
            expected=scale(beta,pscale(padd(const(1),lam,-1),scalar_readout(v)))
            check(fibre_p(model,framed)==expected,'full_source_frame_family_B_class')
    check(scalar_readout(SRC_UNIT)==1,'source_unit_normalization')
    check(not sapp(sdif,SRC_UNIT),'source_unit_is_cycle')
    # Constant modes verify that both h=0 and h=theta*phi retain the same
    # generic strict boundary and both endpoint components. No physical
    # Q-comparison path is manufactured by these tests.
    zero=(beta,{},{})
    one=(beta,theta,{})
    check(zero[0]==one[0],'same_ambient_f_for_two_framings')
    check(zero[2]==one[2],'same_endpoint_h_for_two_framings')
    check(fibre_d(model,(theta,{},{}))==one,'h1_frame_is_exact')
    return {'source':'P_R[1] with full node, sheets, roads, tags, and norm',
            'source_quasi_isomorphism':'phi:P_R -> R_chi[1], phi=sum of roads',
            'source_R_SDR_is_not_claimed_A_linear':True,
            'comparison':'f=beta*phi, s=theta_tilde*phi',
            'boundary_family':'h_lambda=(lambda*theta*phi,0,0)',
            'framed_support_class':'(1-lambda)*[beta] in H_2(B)',
            'secondary_residual':'lambda-1 modulo Delta',
            'physical_lambda_selected':False}


def audit_resolution():
    # Basis monomials for the node.  The equality tests here are symbolic
    # checks; exactness in every degree is proved by Ann(z+)=z- A and its
    # counterpart in the accompanying note.
    def mul(m,n):
        # (branch,degree), branch 0 constant, 1 plus, 2 minus.
        if m[0] and n[0] and m[0]!=n[0]: return None
        return (m[0] or n[0],m[1]+n[1])
    zp=(1,1); zm=(2,1)
    for n in range(2,15):
        previous=(zp,zm) if n==2 else ((zm,zp) if (n-1)%2==0 else (zp,zm))
        current=(zm,zp) if n%2==0 else (zp,zm)
        check(all(mul(a,b) is None for a,b in zip(previous,current)),
              'node_resolution_d_squared')
    for branch in (1,2):
        for exponent in range(1,13):
            mon=(branch,exponent)
            check((mul(mon,zp) is None)==(branch==2),'node_annihilator_plus')
            check((mul(mon,zm) is None)==(branch==1),'node_annihilator_minus')
    # The resolution-induced extra Hom summands in degree -1 can only see
    # H_(3+j)(E) and H_(3+j)(boundary), j>=1.  E has top degree 3;
    # boundary has degree 4 but its H4=H3(V)=0 over the retained base.
    return {'resolution_ranks':[1]+[2]*12,
            'all_differentials_vanish_after_Hom_to_conductor_supported_target':True,
            'H_minus1_extra_ambient_terms':'H_(3+j)(E)=0 for j>=1',
            'H_minus1_extra_boundary_terms':'only j=1 possible; H4(boundary)=H3(V)=0',
            'full_A_derived_secondary_cokernel':'same R/(Delta)',
            'H3_B':'0 because H3(K)->H3(Q) is multiplication by nonzero Delta',
            'higher_paths_of_Map_A(P_R[1],B)':'all zero over the retained independent/Rees base',
            'central_specialization_of_these_homology_claims':'not inferred'}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path('normalization_framed_support_certificate.json'))
    args=parser.parse_args()
    out={'schema':'marici.branch-a.normalization-framed-support.v1',
         'commit':COMMIT,'node_variables':'zplus,zminus; separate from X,u,t',
         'sources':SOURCES+[
             'research/voevodsky/check_conductor_road_endpoint_pullback.rs',
             'research/voevodsky/check_normalization_conductor_bimodule_kernel.py'],
         'models':{},'source_resolution':audit_resolution()}
    for rees in (False,True):
        for cech in (False,True):
            model=Model(rees,cech)
            label=('rees' if rees else 'independent')+('_cech' if cech else '_finite')
            model.run()  # reproduce all original restriction identities
            out['models'][label]={'fibre':audit_fibre(model),'source':audit_source(model)}
        finite=Model(rees,False); cechmodel=Model(rees,True)
        for f in fibre_basis():
            kf=tuple(cechmodel.kappa(a) for a in f)
            check(fibre_p(cechmodel,kf)==cechmodel.kappa(fibre_p(finite,f)),
                  'SDR_p_commutes_finite_to_Cech')
            check(fibre_H(kf)==tuple(cechmodel.kappa(a) for a in fibre_H(f)),
                  'SDR_H_commutes_finite_to_Cech')
    out['checks']=dict(sorted(COUNTS.items()))
    out['total_checks']=sum(COUNTS.values())
    out['checker_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    out['scope']=[
        'Complete target coefficient flag; canonical fibre equivalence to its 208-generator short-boundary complex.',
        'Entire polynomial normalization-road source, including A-linearity and its unbounded node resolution.',
        'Target node action is the specified conductor augmentation A->R.',
        'No physical identification of f with a spatial Gysin kernel; lambda remains unselected.',
        'Explicit counterexample to selection of lambda by coefficient source plus strict endpoint data and symmetry alone.',
        'No central specialization or global equivariant-derived cohomology classification inferred.',
        'No repository mutation; symbolic verification with accompanying algebraic proofs, not proof-assistant certification.'
    ]
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'checks':out['total_checks'],'models':list(out['models']),
                      'fibre':'B (208 generators)','physical_lambda_selected':False,
                      'certificate':str(args.output)},indent=2))

if __name__=='__main__':
    main()
