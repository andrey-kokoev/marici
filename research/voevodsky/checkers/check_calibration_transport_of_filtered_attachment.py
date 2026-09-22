"""Exact finite fixture for coherent gain transport and its kernel boundary.

This checks algebraic transport, not which alternative physical calibrations
are realized by the theta model.
"""
from pathlib import Path
from itertools import product
import json,runpy
import sympy as s
ROOT=Path(__file__).resolve().parents[3]
# E=(b,a,n,l,z). Left t: b->a,n->l. Right t: b->n,a->l,z->l.
EL=s.zeros(5);ER=s.zeros(5)
EL[1,0]=EL[3,2]=1
ER[2,0]=ER[3,1]=ER[3,4]=1
assert EL*ER==ER*EL
pi=s.Matrix([[1,0,0,0,0],[0,1,0,0,0]])
E2L=s.Matrix([[0,0],[1,0]]);E2R=s.zeros(2)
assert pi*EL==E2L*pi and pi*ER==E2R*pi
unit=s.eye(5)
K=unit[:,[2,3,4]];M=unit[:,[1,2,3]];N=unit[:,[2,3]];L=unit[:,[3]]
assert pi*K==s.zeros(2,3)
assert EL.row_join(ER).rank()==M.rank()==EL.row_join(ER).row_join(M).rank()==3
assert (EL*M).row_join(ER*M).rank()==1
assert (EL*N).rank()==1 and ER*N==s.zeros(5,2)
# Source A=(a,n,l), B=(l), G=(a,n). The source itself is not recalibrated.
AL=s.zeros(3);AR=s.zeros(3);AL[2,1]=1;AR[2,0]=1
i=s.Matrix([[0],[0],[1]])
q=s.Matrix([[1,0,0],[0,1,0]])
Bev=M;H=unit[:,[4,2,3]];f=L
j=unit[:,1]-unit[:,4]
w=s.Matrix([[1,0]])
assert H==Bev-j*w*q and H*i==f
assert EL*H==H*AL and ER*H==H*AR
P=s.Matrix([[0,0,0,1,0]])
assert P*f==s.eye(1) and P*ER*N==s.zeros(1,2)
gains=[(s.eye(5),s.eye(2)),
 (s.diag(1,1,2,3,5),s.eye(2)),
 (s.diag(2,3,5,7,11),s.diag(13,17)),
 (s.diag(s.Rational(1,2),s.Rational(2,3),s.Rational(3,5),s.Rational(5,7),s.Rational(7,11)),s.diag(2,5))]
states=[]
for D,C in gains:
    left=D*EL*D.inv();right=D*ER*D.inv();transition=C*pi*D.inv()
    lower_left=C*E2L*C.inv();lower_right=C*E2R*C.inv()
    assert transition*left==lower_left*transition
    assert transition*right==lower_right*transition
    assert transition*(D*K)==s.zeros(2,3)
    assert left*(D*N)==D*EL*N and right*(D*N)==s.zeros(5,2)
    assert left*(D*H)==D*H*AL and right*(D*H)==D*H*AR
    assert transition*(D*H)==s.zeros(2,3)
    assert (D*H)*i==D*f
    normal=P*D.inv()
    assert normal*(D*f)==s.eye(1) and normal*right*(D*N)==s.zeros(1,2)
    states.append((left,right,transition,normal))
for a,b in product(range(len(gains)),repeat=2):
    Da,Ca=gains[a];Db,Cb=gains[b]
    U=Db*Da.inv();V=Cb*Ca.inv()
    la,ra,pa,fa=states[a];lb,rb,pb,fb=states[b]
    assert U*la==lb*U and U*ra==rb*U
    assert pb*U==V*pa
    for flag in (K,M,N,L):assert U*(Da*flag)==Db*flag
    assert U*(Da*H)==Db*H and fb*U==fa
    # Pushout relation vectors transport with identity on the source A.
    graph_a=(Da*f).col_join(-i);graph_b=(Db*f).col_join(-i)
    assert s.diag(U,s.eye(3))*graph_a==graph_b
for a,b,c in product(range(len(gains)),repeat=3):
    Da,Ca=gains[a];Db,Cb=gains[b];Dc,Cc=gains[c]
    assert (Dc*Db.inv())*(Db*Da.inv())==Dc*Da.inv()
    assert (Cc*Cb.inv())*(Cb*Ca.inv())==Cc*Ca.inv()
# Raw diagonal multiplication is NOT generally an automorphism with the
# old action matrices fixed. Transport of those matrices is essential.
D=gains[1][0]
assert D*ER!=ER*D
# Internal positive sector factors: ell=-a*early+b*late.
# Both gaps are positive, but kernels of the combined detector differ.
# Check those two actual source shapes with the independent cut evaluator,
# rather than assuming their detector coefficient vectors from the fixture.
v=runpy.run_path(str(ROOT/'research/voevodsky/certificates/verify_filtered_obstruction.py'))
rows=[tuple(tuple(e) for e in row) for row in v['expected_problem']()['old_seams']]
b0=v['relation']((2,3),0)
sector_columns=[]
for marks in ((1,0),(0,1)):
    source=v['multiply']({((0,1),marks):1},b0)
    image=v['vacuum_rows'](0,15,source,2)
    sector_columns.append([image.get(row,0) for row in rows])
assert sector_columns==[[1,0],[0,1]]
v2=v['multiply'](v['relation']((0,1),1),b0)
im=v['vacuum_rows'](0,15,v2,2)
assert [im.get(row,0) for row in rows]==[1,1]
ell0=s.Matrix([[-1,3]]);ell1=s.Matrix([[-2,3]])
h=s.Matrix([[3],[1]])
assert ell0*h==s.zeros(1,1) and ell1*h==s.Matrix([[-3]])
assert ell0*s.Matrix([[1],[1]])==s.Matrix([[2]])
assert ell1*s.Matrix([[1],[1]])==s.Matrix([[1]])
# No source-evaluation-compatible map U can send zero to -3. Separate
# acquisition of the two sectors, in contrast, has invertible gains.
separate0=s.diag(1,3);separate1=s.diag(2,3)
assert separate1*separate0.inv()*separate0==separate1
result={'passed':True,'calibration_presentations':len(gains),
 'coherent_pair_comparisons':len(gains)**2,'cocycle_checks':len(gains)**3,
 'checks':{'transported_actions_and_transition':True,'K_M_N_L_preserved':True,
 'source_pushout_relations_transport':True,'normalized_private_obstruction_invariant':True,
 'unfiltered_homotopy_transports':True,'fixed_action_naive_scaling_rejected':True,
 'internal_sector_reweighting_changes_source_kernel':True,
 'actual_two_sector_source_coefficients':True},
 'scope':'Exact gain-presentation transport and algebraic counterexample. No assertion that the two internal sector settings occur in the physical theta family.'}
(ROOT/'research/voevodsky/results/calibration-transport-filtered-attachment.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
