#!/usr/bin/env python3
"""Source-constraint rational inverse circuits for the remaining A/H composites."""
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
from check_composite_nonlinear_target_normal import rational
PRIOR='research/benincasa/results/three_composite_normalizations.json'
FIRST='research/benincasa/results/composite_nonlinear_target_normal.json'


def setup_H(Z,embedding):
    support=[j-1 for j in embedding['support']];basis=support[:6]
    L=s.zeros(6,8);left=Z[basis,:].inv()
    for j,label in enumerate(basis):L[:,label]=left[:,j]
    null=Z[support,:].T.nullspace();assert len(null)==1;k=s.zeros(1,8)
    for j,label in enumerate(support):k[label]=null[0][j]
    assert L*Z==s.eye(6) and k*Z==s.zeros(1,6)
    pairs=[tuple(j-1 for j in group) for group in embedding['cell_key']['parallel_classes'] if len(group)==2]
    assert len(pairs)==2
    return L,k,pairs


def inverse_H(Y,data):
    L,k,pairs=data;base=Y*L
    def coefficients(i,j):return [base[:,[i,j]].det(),k[i]*base[1,j]-k[j]*base[1,i],base[0,i]*k[j]-base[0,j]*k[i]]
    coeffs=[coefficients(*pair) for pair in pairs];A=s.Matrix([q[1:] for q in coeffs]);b=s.Matrix([q[0] for q in coeffs])
    det=rational(A.det());assert det!=0
    adj=s.Matrix([[A[1,1],-A[0,1]],[-A[1,0],A[0,0]]]);num=adj*(-b)
    assert all(rational(z)==0 for z in A*num+det*b)
    q=(num/det).applyfunc(rational);R=(base+q*k).applyfunc(rational)
    assert all(rational(R[:,list(pair)].det())==0 for pair in pairs)
    return R,[det]


def setup_A(Z,embedding):
    triples=[tuple(j-1 for j in g) for g in embedding['cell_key']['parallel_classes'] if len(g)==3]
    assert len(triples)==2;pieces=[]
    for group in triples:
        allowed=[i for i in range(8) if i not in group];M=Z[allowed,:]
        null=M.nullspace();assert len(null)==1;h=null[0]
        piv=list(M.rref()[1]);assert len(piv)==5;lift=M[:,piv].inv()
        assert M*h==s.zeros(5,1)
        pieces.append((allowed,M,h,piv,lift))
    return pieces


def inverse_A(Y,data):
    rows=[];grows=[]
    for allowed,M,h,piv,lift in data:
        yh=Y*h;g=s.Matrix([[-yh[1],yh[0]]]);row=g*Y
        coeff=row[:,piv]*lift
        assert all(rational(z)==0 for z in coeff*M-row)
        source=s.zeros(1,8)
        for j,label in enumerate(allowed):source[label]=coeff[j]
        rows.append(source);grows.append(g)
    G=s.Matrix.vstack(*grows);det=rational(G.det());assert det!=0
    R=(G.inv()*s.Matrix.vstack(*rows)).applyfunc(rational)
    return R,[det]


def extract(R,embedding):
    support=tuple(embedding['support']);rot=embedding['rotation'];order=support[rot:]+support[:rot]
    columns=[(-1 if label<support[rot] else 1)*R[:,label-1] for label in order]
    def d(i,j):return rational(s.Matrix.hstack(columns[i],columns[j]).det())
    p=2 if embedding['seed']=='H' else 3
    W=d(0,len(columns)-1);P=d(0,p);assert W!=0 and P!=0
    def upper(j):return rational(d(j,len(columns)-1)/W)
    def lower(j):return rational(d(0,j)/P)
    a5,a6=lower(p+1),lower(p+2);a7=lower(len(columns)-2);a8=lower(len(columns)-1)
    assert a5!=0 and a7!=0
    a4=rational(upper(len(columns)-2)/a7)
    a3=rational(upper(p+1)/a5-a4) if p==2 else rational(upper(p)-a4)
    a2=rational(upper(p)-a3-a4) if p==2 else upper(2)
    return [upper(1),a2,a3,a4,a5,a6,a7,a8],[W,P,a5,a7],columns


def circuit(Z,embedding,data):
    ys=s.symbols('y1:9');Y=s.Matrix([[1,0,*ys[:4]],[0,1,*ys[4:]]])
    if embedding['seed']=='H':
        L,k,pairs=data;base=Y*L
        def coeff(i,j):return [s.expand(base[:,[i,j]].det()),s.expand(k[i]*base[1,j]-k[j]*base[1,i]),s.expand(base[0,i]*k[j]-base[0,j]*k[i])]
        cs=[coeff(*pair) for pair in pairs];A=s.Matrix([q[1:] for q in cs]);b=s.Matrix([q[0] for q in cs]);det=s.expand(A.det())
        adj=s.Matrix([[A[1,1],-A[0,1]],[-A[1,0],A[0,0]]]);assert all(s.expand(z)==0 for z in A*adj*(-b)+det*b)
        return {'type':'seven_support_two_linear_fiber_constraints','support':embedding['support'],
            'parallel_pairs':[[j+1 for j in pair] for pair in pairs],
            'left_inverse':[[str(v) for v in row] for row in L.tolist()],'kernel_row':[str(v) for v in k],
            'fiber_matrix':[[str(v) for v in row] for row in A.tolist()],'fiber_constant':[str(v) for v in b],
            'fiber_determinant':str(det),'inverse_rule':'C=YL+q*k, q=-adj(A)*constant/det(A)'}
    pieces=[];grows=[]
    for allowed,M,h,piv,lift in data:
        yh=Y*h;g=s.Matrix([[-yh[1],yh[0]]]);row=g*Y;coeff=row[:,piv]*lift
        assert all(s.expand(z)==0 for z in coeff*M-row)
        pieces.append({'allowed_labels':[i+1 for i in allowed],'hyperplane_covector':[str(v) for v in h],
            'coordinate_pivots':[i+1 for i in piv],'coefficient_lift':[[str(v) for v in rr] for rr in lift.tolist()]})
        grows.append(g)
    G=s.Matrix.vstack(*grows);assert s.expand(G.det())!=0
    return {'type':'two_five_space_intersections_for_parallel_triples','pieces':pieces,
        'row_change_matrix':[[str(v) for v in row] for row in G.tolist()],'row_change_determinant':str(s.expand(G.det())),
        'inverse_rule':'For each omitted triple, g=(-Y2*h,Y1*h), source row supported on other five labels reconstructs g*Y. C=G^{-1}*stack(source rows).',
        'forward_identity':'C Z=Y; each opposite source row vanishes on its triple, hence both triples are parallel'}


def run(row,sample):
    embedding=row['superfunction_runs'][0]['matches'][0]
    a=s.symbols('a1:9');C=s.Matrix([[s.sympify(v) for v in rr] for rr in sample['source_chart_matrix']])
    Z=s.Matrix([[s.Integer(j+sample['positive_Z_moment_shift'])**k for k in range(6)] for j in range(1,9)])
    isH=embedding['seed']=='H';data=setup_H(Z,embedding) if isH else setup_A(Z,embedding)
    inv=lambda Y:inverse_H(Y,data) if isH else inverse_A(Y,data)
    desc=circuit(Z,embedding,data)
    vals={z:s.Integer(sample['source_parameters'][str(z)]) for z in a};e=3;boundary=vals|{a[e]:0}
    coords=[(i,j) for i in range(2) for j in range(6) if j not in (0,1)]
    def recover(Y):
        R,loc=inv(Y);params,gauge,cols=extract(R,embedding)
        return params,loc+gauge,R,cols
    N=normalize(C.subs(boundary)*Z,[0,1]);Ntop=normalize(C.subs(vals)*Z,[0,1])
    top,_,_,_=recover(Ntop);bottom,loc,R,_=recover(N)
    assert top==[vals[z] for z in a] and bottom==[boundary[z] for z in a] and all(q!=0 for q in loc)
    assert all(rational(v)==0 for v in R*Z-N)
    t=s.symbols('t');arc=vals|{a[e]:t};Narc=normalize(C.subs(arc)*Z,[0,1])
    ap,_,Ra,cols=recover(Narc);assert all(rational(q-arc[z])==0 for q,z in zip(ap,a))
    assert all(rational(v)==0 for v in Ra*Z-Narc)
    pre=s.Matrix.hstack(*cols);W=s.Matrix.hstack(cols[0],cols[-1]);B=(W.inv()*pre).applyfunc(rational)
    p=2 if isH else 3;canon=(s.diag(1,1/B[1,p])*B).applyfunc(rational)
    expected=(s.Matrix([[1,a[0],a[1]+a[2]+a[3],(a[2]+a[3])*a[4],(a[2]+a[3])*a[5],a[3]*a[6],0],[0,0,1,a[4],a[5],a[6],a[7]]]) if isH else
        s.Matrix([[1,a[0],a[1],a[2]+a[3],(a[2]+a[3])*a[4],(a[2]+a[3])*a[5],a[3]*a[6],0],[0,0,0,1,a[4],a[5],a[6],a[7]]])).subs(arc)
    assert all(rational(v)==0 for v in canon-expected)
    h=s.symbols('h');gradient=[]
    for i,j in coords:
        E=s.zeros(2,6);E[i,j]=1;q,_,_,_=recover(N+h*E)
        gradient.append(rational(s.diff(q[e],h).subs(h,0)))
    grad=s.Matrix(1,8,gradient);Y=C.subs(boundary)*Z
    J,actual=target_jac(Y,[C.diff(z).subs(boundary)*Z for z in a],[0,1]);assert actual==coords and J.det()!=0
    unit=s.zeros(1,8);unit[e]=1;assert grad*J==unit
    free=[j for j in range(8) if j!=e];Jfree=J[:,free]*s.diag(*[vals[a[j]] for j in free])
    selected=next(I for I in itertools.combinations(range(8),7) if Jfree[list(I),:].det()!=0)
    det=s.factor(Jfree[list(selected),:].det());detD=s.factor(s.Matrix.vstack(grad*J,J[list(selected),:]).det())
    routeA=s.factor((-1)**e/det);routeB=s.factor(1/(s.prod(vals[a[j]] for j in free)*detD));assert routeA==routeB and -routeA!=routeB
    tangent=rational((grad*s.Matrix([Narc[i,j]-N[i,j] for i,j in coords]))[0]);defect=rational(tangent-t);assert defect!=0
    return {'positive_Z_moment_shift':sample['positive_Z_moment_shift'],'inverse_circuit':desc,
        'source_embedding':{'support':embedding['support'],'rotation':embedding['rotation'],'wrapped_sign':-1},
        'target_normal_rule':'b(Y)=det(v1,vp)*det(v(r-1),vr)/(det(v1,vr)*det(v1,v(r-1))), with v the ordered signed embedded source columns of the reconstructed fiber; p=3 for H, p=4 for A; r=number of active columns. This is canonical alpha4, not a tangent approximation.',
        'source_arc':'fixed prior source parameters except alpha4=t','full_source_chart_arc_reconstruction':True,
        'inverse_arc_identity':'all eight reconstructed parameters equal source arc; b(target_arc)=t',
        'boundary_localization_values':[str(v) for v in loc],'target_normal_gradient':[str(v) for v in grad],
        'target_boundary_log_jacobian':str(det),'full_normal_jacobian':str(detD),
        'selected_target_coordinate_indices':list(selected),'source_residue_sign':(-1)**e,
        'source_residue_then_pushforward':str(routeA),'top_pushforward_then_target_residue':str(routeB),
        'orientation_failure_residual':str(-routeA-routeB),'tangent_only_arc_defect':str(defect)}


def main():
    prior=json.loads((ROOT/PRIOR).read_text());first=json.loads((ROOT/FIRST).read_text())
    for r,checker in [(prior,'research/benincasa/checkers/check_three_composite_normalizations.py'),
                       (first,'research/benincasa/checkers/check_composite_nonlinear_target_normal.py')]:
        for p,h in r['source_sha256'].items():assert sha256((ROOT/p).read_bytes()).hexdigest()==h,p
        assert r['checker_sha256']==sha256((ROOT/checker).read_bytes()).hexdigest()
    rows=[]
    for row in prior['rows']:
        runs=[run(row,sample) for sample in row['target_runs']]
        if row['history_index']==5:
            for new,old in zip(runs,first['runs']):assert new['source_residue_then_pushforward']==old['source_residue_then_pushforward']
        rows.append({'history_index':row['history_index'],'root':row['root'],'seed':row['seed'],'runs':runs})
    paths=[PRIOR,FIRST,'research/benincasa/checkers/check_three_composite_normalizations.py',
        'research/benincasa/checkers/check_composite_nonlinear_target_normal.py','research/benincasa/checkers/check_composite_root_normalization.py']
    out={'schema':'marici.benincasa.three-composite-inverse-normals.v1','rows':rows,
        'checks':{'three_actual_source_constraint_inverse_circuits':True,'six_exact_full_source_arc_reconstructions':True,
            'six_target_normal_pullback_unit_covectors':True,'six_oriented_local_residue_square_equalities':True,
            'six_orientation_hostiles_nonzero':True,'six_tangent_only_substitutes_rejected':True,'history5_receipt_preserved':True},
        'passed':True,'disposition':'all_three_selected_alpha4_nonlinear_target_normals_and_local_squares_constructed',
        'scope':'Rational source-constraint circuits for two fixed positive external Z, exact full transverse arcs and local residue algebra. No invariant atlas completeness, global positive-covering theorem, BCFW orientation anchors, target supercomponent extraction or weighted shared-residue theorem.',
        'next_action':'Test the common physical Y1234 facet of histories5 and8 (alpha2=0 in both): invert the same target point into the other source chart, establish overlap/localization/positivity or retain a nonoverlap disposition, then compare oriented residues in the same target tangent coordinates. Do not infer weighted cancellation from local squares alone.',
        'source_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},
        'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    path=ROOT/'research/benincasa/results/three_composite_inverse_normals.json';path.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'passed':True,'histories':[r['history_index'] for r in rows],'checks':out['checks'],'disposition':out['disposition']},indent=2))


if __name__=='__main__':main()
