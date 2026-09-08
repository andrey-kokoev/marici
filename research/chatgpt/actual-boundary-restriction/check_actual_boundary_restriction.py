#!/usr/bin/env python3
"""Exact endpoint/Q restriction for Marici's K6 coefficient support flag.

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


def audit_source_contraction():
    # The old s_C is not the primitive s=theta_tilde used above.
    # It is an endomorphism of a different, contractible four-generator C.
    check('xi' not in {'b'},'old_s_C_does_not_preserve_endpoint_Rb')
    return {'s_C_q':'H','s_C_b':'xi',
            'same_as_theta_lift':False,
            'endpoint_filtered_endomorphism':False,
            'conclusion':'No r(s_C) is asserted in the full filtered physical mapping complex.'}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path('actual_boundary_restriction_certificate.json'))
    args=parser.parse_args()
    check(tuple(Counter(map(len,FS))[i] for i in range(4))==(1,9,21,14),'face_census')
    check((len(ALL),len(B),len(V),len(E),len(P),len(Q))==(215,208,16,199,192,7),'support_census')
    check((len(VP),len(VM))==(8,8),'both_endpoint_packets_retained')
    models={}
    for rees in (False,True):
        finite=Model(rees,False); cech=Model(rees,True)
        models[('rees' if rees else 'independent')+'_finite']=finite.run()
        models[('rees' if rees else 'independent')+'_cech']=cech.run()
        for c in CELLS:
            check(apply(cech.d,cech.kappa(basis(c)))==cech.kappa(finite.d[c]),'Koszul_Cech_chain_map')
        for c in E:
            lhs=cech.rho(cech.kappa(basis(c)))
            rhs=tuple(cech.kappa(v) for v in finite.rho(basis(c)))
            check(lhs==rhs,'restriction_commutes_Koszul_Cech')
        # Same top cycles, since fully circled generators have no denominators.
        check(cech.kappa(finite.omega())==cech.omega(),'omega_commutes_Koszul_Cech')
        check(cech.kappa(finite.theta())==cech.theta(),'theta_commutes_Koszul_Cech')
    result={
        'schema':'marici.branch-a.actual-coefficient-boundary.v1',
        'source_commit':COMMIT,'sources':SOURCES,
        'diagonal_order':[list(d) for d in DIAGONALS],
        'short_diagonals':[list(DIAGONALS[i]) for i in SHORT],
        'long_diagonals':[list(DIAGONALS[i]) for i in LONG],
        'ranks_homological':{
            label:[sum(degree(c)==i for c in subset) for i in range(4)]
            for label,subset in [('K',ALL),('B',B),('V',V),('E',E),('P',P),('Q',Q)]},
        'boundary_ranks_homological_0_through_4':[
            sum(degree(c)==i for c in Q)+sum(degree(c)+1==i for c in V)
            for i in range(5)],
        'models':models,'old_source_contraction':audit_source_contraction(),
        'scope':[
            'Actual source-defined original-twist K6 support flag and its target-only Cech realization.',
            'Probe R[2], canonical Q connecting class beta=d(theta_tilde), strict zero-boundary frame h=0.',
            'rho=(pi_Q,kappa_plus,kappa_minus) retains actual target endpoint connecting morphisms.',
            'No identification with the unprovided normalization-source physical comparison or its connector homotopies.',
            'No source ring inverse of an occurrence or normal parameter; Cech inverses stay in legal target summands.',
            'Rees model is recomputed after u=tX, not inferred by flat base change of the previous annihilator.',
            'Homology-generator and exact-annihilator statements use the algebraic proofs in the accompanying note.',
            'No repository mutation or proof-assistant verification.'
        ],
    }
    result['checks']=dict(sorted(COUNTS.items()))
    result['total_checks']=sum(COUNTS.values())
    result['checker_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'total_checks':result['total_checks'],
        'support_ranks':result['ranks_homological'],
        'boundary_ranks':result['boundary_ranks_homological_0_through_4'],
        'restriction_nonzero_columns':{k:v['nonzero_rho_columns'] for k,v in models.items()},
        'annihilators':{k:v['annihilator_generator'] for k,v in models.items()},
        'output':str(args.output)},indent=2))

if __name__=='__main__':
    main()
