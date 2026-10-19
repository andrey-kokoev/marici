#!/usr/bin/env python3
"""F6 top density and normalized reference-plane bosonization component.

No boundary Berezin map is inferred from this top-degree extractor.
"""
import itertools
import json
from hashlib import sha256
from pathlib import Path
from check_history6_projection_descent import s, twistors
from check_history6_endpoint_boundary import coefficient, evaluate
from check_three_composite_internal_gluings import normalize, target_jac
from dual_r_invariant import theta_coefficients
from momentum_twistor_constructors import four_bracket
ROOT=Path(__file__).resolve().parents[3]
CHART='research/benincasa/results/history6_common_corner.json'
ENDPOINT='research/benincasa/results/history6_endpoint_boundary.json'
DIRECTION='research/benincasa/results/history6_directional_boundaries.json'
LABELS=[1,2,3,5,6,8]
PAIRS=[(0,1),(1,2),(2,3),(3,4),(4,5),(0,5)]
FULL=(1<<16)-1


def wedge_sign(a,b):
    if a&b:return 0
    parity=0
    while a:
        bit=a&-a;parity+=(b&(bit-1)).bit_count();a-=bit
    return -1 if parity%2 else 1


def add(out,mask,value):
    out[mask]=out.get(mask,0)+value


def wedge(A,B):
    out={}
    for a,x in A.items():
        for b,y in B.items():
            sign=wedge_sign(a,b)
            if sign:add(out,a|b,sign*x*y)
    return {m:v for m,v in out.items() if v!=0}


def bos_entry(row,chi):
    # phi generators row-major first; eta generators ordered per SU4 as
    # eta2^A,eta3^A. Each phi*chi entry is even, permitting ordinary det.
    out={}
    for A in range(4):
        for j,value in enumerate(chi):
            if value:out[(1<<(4*row+A))|(1<<(8+2*A+j))]=value
    return out


def power4_full(D):
    D2=wedge(D,D);total=0
    for a,x in D2.items():
        complement=FULL^a
        if complement in D2:total+=wedge_sign(a,complement)*x*D2[complement]
    return total


def normalization():
    # Independent determinant of the 2x2 bosonized fermion block with
    # chi1=(eta2^A), chi2=(eta3^A); four remaining bosonic columns are I4.
    A=bos_entry(0,[1,0]);B=bos_entry(0,[0,1]);C=bos_entry(1,[1,0]);D=bos_entry(1,[0,1])
    det=wedge(A,D)
    for mask,v in wedge(B,C).items():add(det,mask,-v)
    value=power4_full(det);assert value!=0
    return value


def component_bosonized(Z,chi):
    entries=[[bos_entry(row,chi[j]) for j in LABELS] for row in range(2)]
    determinant={}
    for i,j in itertools.combinations(range(6),2):
        complement=[k for k in range(6) if k not in (i,j)]
        minor=four_bracket(*(Z[LABELS[k]] for k in complement))
        factor=(-1)**(i+j+1)*minor
        first=wedge(entries[0][i],entries[1][j]);second=wedge(entries[0][j],entries[1][i])
        for mask,v in first.items():add(determinant,mask,factor*v)
        for mask,v in second.items():add(determinant,mask,-factor*v)
    determinant={mask:v for mask,v in determinant.items() if v!=0}
    numerator=power4_full(determinant)
    denominator=s.prod(four_bracket(*(Z[LABELS[k]] for k in range(6) if k not in pair)) for pair in PAIRS)
    assert denominator!=0
    return s.factor(numerator/denominator),len(determinant)


def main():
    chart=json.loads((ROOT/CHART).read_text());endpoint=json.loads((ROOT/ENDPOINT).read_text());directions=json.loads((ROOT/DIRECTION).read_text())
    for receipt in (chart,endpoint,directions):
        assert receipt['passed']
        for p,h in receipt['source_sha256'].items():assert sha256((ROOT/p).read_bytes()).hexdigest()==h,p
    b=s.symbols('b1:9');C=s.Matrix([[s.sympify(x,locals={str(z):z for z in b}) for x in row] for row in chart['source_chart']])
    active=[j-1 for j in LABELS]
    bare=normalize(C[:,active],[0,1]);freecoords=[(i,j) for i in range(2) for j in range(2,6)]
    Jbare=s.Matrix([[s.diff(bare[i,j],z)*z for z in b] for i,j in freecoords])
    cyclic=s.prod(bare[:,list(pair)].det() for pair in PAIRS)
    assert s.factor(Jbare.det()-cyclic)==0
    densities=[]
    for shift,vals in enumerate(([2,3,5,7,11,13,17,19],[3,5,7,11,13,17,19,23])):
        v=dict(zip(b,map(s.Integer,vals)));Z=s.Matrix([[s.Integer(j+shift)**k for k in range(6)] for j in range(1,9)])
        Y=C.subs(v)*Z;N=normalize(Y,[0,1])
        J,_=target_jac(Y,[C.diff(z).subs(v)*Z*v[z] for z in b],[0,1]);intrinsic=s.factor(1/J.det())
        D=Z[active,:].det()
        brackets=[s.Matrix.vstack(N,*[Z[LABELS[k]-1,:] for k in range(6) if k not in pair]).det() for pair in PAIRS]
        rational=s.factor(D**4/s.prod(brackets));assert rational==intrinsic
        densities.append({'positive_Z_moment_shift':shift,'intrinsic_density':str(intrinsic),'projective_formula_density':str(rational)})
    norm=normalization();runs=[];t=s.Symbol('t');c,_=coefficient(t)
    for shift in (0,1,2):
        Z,lam,x=twistors(shift);theta=theta_coefficients(lam,8)
        chi={}
        for j in range(1,9):
            ell=s.Matrix([[0,1],[-1,0]])*lam[j]
            chi[j]=[(ell.T*theta[j].get(k,s.zeros(2,1)))[0] for k in (2,3)]
        raw,count=component_bosonized(Z,chi);normalized=s.factor(raw/norm)
        existing=evaluate(shift,c,t)
        angle23=s.Matrix.hstack(lam[2],lam[3]).det()
        K=s.factor(normalized/angle23**4)
        assert K==s.Rational(existing['component']['K'])
        weight=s.factor(c.subs(t,shift))
        assert weight*K==s.Rational(existing['component']['K0'])
        assert (1-weight)*K==s.Rational(existing['component']['B22'])
        # Reference plane Y0=[I2|0] and bosonized Z=(phi chi,z).
        # Every <Y0 abcd> is the ordinary four-bracket, with no phi/eta.
        # Therefore coefficient multiplication commutes with the normalized
        # phi-top extraction exactly, not only after evaluating K.
        quotient0=s.factor(1-four_bracket(Z[6],Z[8],Z[1],Z[2])*four_bracket(Z[5],Z[1],Z[2],Z[3])/
            (four_bracket(Z[5],Z[8],Z[1],Z[2])*four_bracket(Z[6],Z[1],Z[2],Z[3])))
        assert quotient0==weight
        assert s.factor((quotient0*raw)/norm/angle23**4-weight*K)==0
        runs.append({'shift':shift,'determinant_sparse_terms':count,'raw_phi_eta_component':str(raw),
            'normalized_supercomponent':str(normalized),'K':str(K),'K0':existing['component']['K0'],
            'B22':existing['component']['B22'],'reference_plane_quotient_coefficient':str(quotient0)})
    paths=[CHART,ENDPOINT,DIRECTION,'research/benincasa/checkers/check_history6_projection_descent.py',
        'research/benincasa/checkers/check_history6_endpoint_boundary.py','research/nima/momentum_twistor_super.py',
        'research/nima/dual_r_invariant.py','research/nima/momentum_twistor_constructors.py']
    out={'schema':'marici.benincasa.history6-bosonization-bridge.v1','history_index':6,
        'top_density_formula':'Omega_F(N,Z)=det(Z_support)^4 / product_{six cyclic active pairs ij} <N external_complement_ij>',
        'density_derivation':'Exact symbolic F source Jacobian in C12 gauge equals product of cyclic minors. Under the GL6 active-basis map, Grassmann patch Jacobian is det(Z_support)^2/det((CZ)_pivot)^6; complementary brackets are det(Z_support)*Cminor/det((CZ)_pivot), giving the projective density formula. Two positive fixtures reproduce frozen reciprocal log Jacobian.',
        'berezin_normalization':{'phi_order':'row1 A1..4 then row2 A1..4','eta_order':'eta2^1,eta3^1,...,eta2^4,eta3^4',
            'independent_2by2_block_phi_eta_top_coefficient':str(norm),'extraction_rule':'Take the phi-top coefficient divided by this algebraic factor; then use the same eta23 selector / <23>^4.',
            'not_fitted':True},
        'bosonization_rule':'External six-vector (sum_A phi_1A chi_j^A, sum_A phi_2A chi_j^A, z_j); Y0=[I2|0].',
        'density_tests':densities,'component_tests':runs,'passed':True,
        'top_bridge_scope':'Actual intrinsic F density and one normalized degree-eight component at three fixtures. Coefficient is phi-independent at Y0, so its multiplication commutes algebraically with top Berezin extraction. Not a full all-components physical theorem.',
        'boundary_gap':'Top phi extraction maps the eight-form density at Y0 to a superfunction. No degree-seven/six boundary Berezin codomain, boundary delta measure, normal order or direction-retaining supercomponent object is supplied; top extraction cannot be applied to lower-degree forms by fiat.',
        'next_action':'Extend the normalized top bridge to all quotient Grassmann components or derive a source-authorized boundary Berezin/delta measure and direction-retaining codomain; do not promote the verified eta23 component to a boundary superfunction square.',
        'source_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},
        'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    (ROOT/'research/benincasa/results/history6_bosonization_bridge.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'passed':True,'independent_Berezin_factor':str(norm),'density_tests':densities,
        'component_tests':runs,'boundary_gap':out['boundary_gap']},indent=2))

if __name__=='__main__':main()
