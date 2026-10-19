#!/usr/bin/env python3
"""Actual rational inverse circuit for history5 alpha4=0; exact arc and residues.

The circuit avoids expanding large multivariate rational expressions. Its fiber
constraints are solved symbolically, and the same operations specialize to exact
source arcs and target-direction tests.
"""
import json
import sys
import itertools
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'))
sys.path.insert(0,str(Path(__file__).resolve().parent))
import sympy as s
from check_composite_root_normalization import normalize,target_jac
PRIOR='research/benincasa/results/three_composite_normalizations.json'
SCREEN='research/benincasa/results/three_composite_boundary_residues.json'


def rational(v):return s.cancel(v)


def setup(Z):
    L=s.zeros(6,8);L[:,:6]=Z[:6,:].inv();assert L*Z==s.eye(6)
    support=[0,1,2,3,4,5,7];null=Z[support,:].T.nullspace();assert len(null)==1
    k=s.zeros(1,8)
    for j,label in enumerate(support):k[label]=null[0][j]
    assert k*Z==s.zeros(1,6) and k[6]==0
    return L,k


def fiber(Y,L,k):
    base=Y*L
    # det(base_i+q*k_i,base_j+q*k_j) is affine in q=(u,v).
    def data(i,j):
        constant=base[:,[i,j]].det()
        coeff_u=k[i]*base[1,j]-k[j]*base[1,i]
        coeff_v=base[0,i]*k[j]-base[0,j]*k[i]
        return [constant,coeff_u,coeff_v]
    entries=[data(2,3),data(5,7)]
    A=s.Matrix([entry[1:] for entry in entries]);b=s.Matrix([entry[0] for entry in entries])
    determinant=s.expand(A.det());assert determinant!=0
    adj=s.Matrix([[A[1,1],-A[0,1]],[-A[1,0],A[0,0]]])
    numerator=adj*(-b)
    assert all(rational(z)==0 for z in A*numerator+determinant*b)
    sol=(numerator/determinant).applyfunc(rational)
    def minor(i,j):
        constant,cu,cv=data(i,j)
        return rational(constant+cu*sol[0]+cv*sol[1])
    assert minor(2,3)==minor(5,7)==0
    return base,sol,minor,A,b,determinant


def recover(Y,L,k):
    base,sol,d,A,b,det=fiber(Y,L,k)
    # Gauge extraction for columns (3,4,5,6,8,-1,-2) of the H embedding.
    d23,d35,d36,d13=d(1,2),d(2,4),d(2,5),d(0,2)
    assert d23!=0 and d35!=0 and d36!=0 and d13!=0
    a1=rational(d(1,3)/d23)
    a4=rational(d35*d(0,1)/(d23*d13))
    a3=rational(d(1,5)*d35/(d23*d36)-a4)
    a2=rational(d(1,4)/d23-a3-a4)
    values=[a1,a2,a3,a4,rational(d36/d35),rational(d(2,7)/d35),rational(d13/d35),rational(d23/d35)]
    return values,{'A':A,'constant':b,'determinant':det,'solution':sol,
                   'localization':[det,d23,d35,d36,d13]}


def symbolic_circuit(L,k):
    xs=s.symbols('y1:9');Y=s.Matrix([[1,0,*xs[:4]],[0,1,*xs[4:]]])
    # Only polynomial fiber data are expanded. The inverse minor operations are
    # explicit rational formulas; no multivariate full-form expansion is needed.
    base=Y*L
    def coeff(i,j):return [s.expand(base[:,[i,j]].det()),
        s.expand(k[i]*base[1,j]-k[j]*base[1,i]),s.expand(base[0,i]*k[j]-base[0,j]*k[i])]
    entries=[coeff(2,3),coeff(5,7)];A=s.Matrix([v[1:] for v in entries]);b=s.Matrix([v[0] for v in entries])
    det=s.expand(A.det());assert det!=0
    adj=s.Matrix([[A[1,1],-A[0,1]],[-A[1,0],A[0,0]]]);numer=adj*(-b)
    assert all(s.expand(z)==0 for z in A*numer+det*b)
    assert base[:,6]==s.zeros(2,1)
    # Right inverse follows identically from LZ=I and kZ=0, without expanding q.
    assert L[ :,6]==s.zeros(6,1)
    return {'target_coordinates':[str(z) for z in xs],
        'fiber_coefficient_matrix':[[str(v) for v in row] for row in A.tolist()],
        'fiber_constant':[str(v) for v in b],'fiber_determinant':str(det),
        'fiber_solution_rule':'(u,v)^T = -adj(A)*constant/det(A)',
        'source_minor_rule':'Delta_ij = det(base_i,base_j) + u*(k_i*base_2j-k_j*base_2i) + v*(base_1i*k_j-base_1j*k_i)',
        'normal_rule':'b(Y)=Delta35*Delta12/(Delta23*Delta13) in the reconstructed fiber C=YL+(u,v)^T k',
        'symbolic_linear_constraint_identity':'A*(-adj(A)*constant)+det(A)*constant=0 identically',
        'forward_map_identity':'C Z = Y by LZ=I and kZ=0; C7=0 identically'}


def run(sample):
    a=s.symbols('a1:9');C=s.Matrix([[s.sympify(v) for v in row] for row in sample['source_chart_matrix']])
    Z=s.Matrix([[s.Integer(j+sample['positive_Z_moment_shift'])**p for p in range(6)] for j in range(1,9)])
    L,k=setup(Z);circuit=symbolic_circuit(L,k)
    vals={z:s.Integer(sample['source_parameters'][str(z)]) for z in a};e=3;boundary=vals|{a[e]:0}
    coords=[(i,j) for i in range(2) for j in range(6) if j not in (0,1)]
    Ntop=normalize(C.subs(vals)*Z,[0,1]);N=normalize(C.subs(boundary)*Z,[0,1])
    top,_=recover(Ntop,L,k);bottom,data=recover(N,L,k)
    assert top==[vals[z] for z in a] and bottom==[boundary[z] for z in a]
    assert all(q!=0 for q in data['localization'])
    t=s.symbols('t');arc=vals|{a[e]:t};Narc=normalize(C.subs(arc)*Z,[0,1])
    arcrecovered,arcdata=recover(Narc,L,k)
    assert all(rational(q-arc[z])==0 for q,z in zip(arcrecovered,a))
    assert arcrecovered[e]==t
    # Verify the reconstructed H chart on the rational source arc, not only its
    # component or normal. Its ordered source gauge is unique on this open.
    R=(Narc*L+arcdata['solution']*k).applyfunc(rational)
    pre=s.Matrix.hstack(R[:,2],R[:,3],R[:,4],R[:,5],R[:,7],-R[:,0],-R[:,1])
    W=s.Matrix.hstack(pre[:,0],pre[:,6]);B=(W.inv()*pre).applyfunc(rational)
    canon=(s.diag(1,1/B[1,2])*B).applyfunc(rational)
    expected=s.Matrix([[1,a[0],a[1]+a[2]+a[3],(a[2]+a[3])*a[4],(a[2]+a[3])*a[5],a[3]*a[6],0],
                       [0,0,1,a[4],a[5],a[6],a[7]]]).subs(arc)
    assert all(rational(z)==0 for z in canon-expected)
    # Target gradient from exact one-coordinate inverse specializations.
    h=s.symbols('h');grad=[]
    for i,j in coords:
        E=s.zeros(2,6);E[i,j]=1
        direction,_=recover(N+h*E,L,k)
        grad.append(rational(s.diff(direction[e],h).subs(h,0)))
    grad=s.Matrix(1,8,grad)
    Y=C.subs(boundary)*Z
    J,actualcoords=target_jac(Y,[C.diff(z).subs(boundary)*Z for z in a],[0,1])
    assert actualcoords==coords and J.det()!=0
    unit=s.zeros(1,8);unit[e]=1;assert grad*J==unit
    free=[j for j in range(8) if j!=e];Jfree=J[:,free]*s.diag(*[vals[a[j]] for j in free])
    selected=next(I for I in itertools.combinations(range(8),7) if Jfree[list(I),:].det()!=0)
    det=s.factor(Jfree[list(selected),:].det());D=s.Matrix.vstack(grad*J,J[list(selected),:]);detD=s.factor(D.det())
    A=s.factor((-1)**e/det);B=s.factor(1/(s.prod(vals[a[j]] for j in free)*detD));assert A==B and -A!=B
    tangent=rational((grad*s.Matrix([Narc[i,j]-N[i,j] for i,j in coords]))[0]);defect=rational(tangent-t)
    assert defect!=0
    return {'positive_Z_moment_shift':sample['positive_Z_moment_shift'],'inverse_circuit':circuit,
        'left_inverse':[[str(z) for z in row] for row in L.tolist()],'kernel_row':[str(z) for z in k],
        'source_transverse_arc':'prior positive alpha values except alpha4=t',
        'arc_inverse_identity':'all eight recovered alpha parameters agree identically; full H chart reconstruction agrees; b(target_arc)=t',
        'boundary_target_coordinates':[str(N[i,j]) for i,j in coords],
        'boundary_localization_values':[str(z) for z in data['localization']],
        'target_normal_gradient':[str(z) for z in grad],'normal_pullback_gradient':'unit covector in alpha4',
        'target_boundary_log_jacobian':str(det),'selected_target_coordinate_indices':list(selected),
        'source_residue_sign':(-1)**e,'full_ordinary_normal_jacobian':str(detD),
        'source_residue_then_pushforward':str(A),'top_pushforward_then_target_residue':str(B),
        'orientation_failure_residual':str(-A-B),'tangent_only_arc_defect':str(defect)}


def main():
    prior=json.loads((ROOT/PRIOR).read_text());screen=json.loads((ROOT/SCREEN).read_text())
    for receipt,checker in [(prior,'research/benincasa/checkers/check_three_composite_normalizations.py'),
                            (screen,'research/benincasa/checkers/check_three_composite_boundary_residues.py')]:
        for p,h in receipt['source_sha256'].items():assert sha256((ROOT/p).read_bytes()).hexdigest()==h,p
        assert receipt['checker_sha256']==sha256((ROOT/checker).read_bytes()).hexdigest()
    row=next(r for r in prior['rows'] if r['history_index']==5);runs=[run(q) for q in row['target_runs']]
    checks={'symbolic_rational_fiber_constraints':True,'right_inverse_circuit_from_LZ_and_kernel':True,
        'inverse_top_and_boundary_parameters':True,'two_full_rational_transverse_arc_identities':True,
        'full_H_chart_arc_reconstruction':True,'actual_normal_gradient_is_alpha4_covector':True,
        'two_exact_residue_route_equalities':True,'orientation_failures_nonzero':True,'tangent_only_substitute_rejected':True}
    paths=[PRIOR,SCREEN,'research/benincasa/checkers/check_three_composite_normalizations.py',
        'research/benincasa/checkers/check_three_composite_boundary_residues.py',
        'research/benincasa/checkers/check_composite_root_normalization.py']
    out={'schema':'marici.benincasa.composite-nonlinear-target-normal.v1','root':[1,2],'history_index':5,
        'source_boundary':'alpha4=0','runs':runs,'checks':checks,'passed':True,
        'disposition':'actual_rational_inverse_circuit_normal_and_oriented_local_residue_square_constructed',
        'implementation_history':'Initial multivariate expansion timed out at 240 seconds. Replaced expansion with the same rational inverse circuit and exact univariate specializations; mathematical criterion unchanged.',
        'claim_boundary':'Symbolic fiber inverse circuit at two fixed positive external Z, exact full source arcs and local differential residue controls. Does not classify the nonlinear divisor globally, certify all positive target fibers, BCFW orientation anchor or supercomponent boundary extraction.',
        'next_action':'Extend inverse-normal construction to histories 8 and 9 or compare shared composite facets in common target coordinates. Global atlas/weighted map gates remain distinct.',
        'source_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},
        'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    path=ROOT/'research/benincasa/results/composite_nonlinear_target_normal.json'
    path.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'passed':True,'checks':checks,'disposition':out['disposition']},indent=2))


if __name__=='__main__':main()
