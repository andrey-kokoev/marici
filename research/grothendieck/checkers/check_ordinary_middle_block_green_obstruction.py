"""Exact ordinary-sector compression hostile; no spectral sampling."""
from pathlib import Path
import runpy,json
import sympy as s
ROOT=Path(__file__).resolve().parents[3]
b=runpy.run_path(str(ROOT/'research/grothendieck/checkers/check_six_prime_derived_block_associativity.py'))
rel,mul,D,record=b['relation'],b['multiply'],b['derivative'],b['record']
a0,a1=rel((0,1),0),rel((0,1),1)
c0=rel((4,5),0)
w1={((2,3),(True,False)):1};w0={((2,3),(False,False)):1}
def tensor(*cols):
    out={():1}
    for col in cols:out={keys+(k,):v*c for keys,v in out.items() for k,c in col.items()}
    return out
def fixture_pair(v,w):return sum(s.conjugate(c)*w.get(k,0) for k,c in v.items())
# Positive orthonormal vertex-potential coordinates, tau=1, are an algebraic
# fixture ONLY. The actual function-valued nonvanishing is proved separately.
dc=D(c0,15)
left_x=tensor(D(mul(a0,w1),0),dc)
left_y=tensor(D(mul(a1,w0),0),dc)
right_x=tensor(D(a0,0),D(mul(w1,c0),3))
right_y=tensor(D(a1,0),D(mul(w0,c0),3))
common_x=tensor(D(a0,0),record((2,3),(True,False),3),dc)
common_y=tensor(D(a1,0),record((2,3),(False,False),3),dc)
assert fixture_pair(common_x,common_y)==0
assert fixture_pair(right_x,right_y)==0
assert fixture_pair(left_x,left_y)==-8

# Verify the stronger FORMAL kernel coefficient, without assigning a feature Gram.
# Pair each matching seam shape with independent variables G_(u,v) per feature slot.
def seam_pair(k,l):
    x,y,pre,letter,post=k;xx,yy,pre2,letter2,post2=l
    if (x,y,len(pre),letter==0,len(post))!=(xx,yy,len(pre2),letter2==0,len(post2)):return 0
    val=s.Integer(1)
    slots=list(zip(pre,pre2))+([] if letter==0 else [(letter,letter2)])+list(zip(post,post2))
    for i,j in slots:val*=s.Symbol(f'G_{i}_{j}')
    return val
formal=0
for (k1,k2),u in left_x.items():
    for (l1,l2),v in left_y.items():formal+=u*v*seam_pair(k1,l1)*seam_pair(k2,l2)
# middle g=u_7-u_3; first-block h=2u_3-u_1-u_2.
expected=4*(2*s.Symbol('G_7_3')-s.Symbol('G_7_1')-s.Symbol('G_7_2')
            -2*s.Symbol('G_3_3')+s.Symbol('G_3_1')+s.Symbol('G_3_2'))
assert s.expand(formal-expected)==0

# Actual fixed Clark sewing: raw four-port coefficient is rank two;
# the nondegenerate signature is on the normalized TWO-sheet carrier.
sewing=s.I*s.Matrix([[-1,1,1,1],[-1,1,-1,-1]])/2
phase=s.diag(s.I,-s.I,s.I,-s.I)
A=sewing*phase;J=s.diag(1,-1);C=A.H*J*A
assert A.rank()==2 and C.rank()==2 and C*C!=s.eye(4)
assert J*J==s.eye(2)

# Observer correspondences do not require equality of pulled-back forms.
G=s.diag(1,1,-1)
jL=s.Matrix([[1,0],[0,1],[0,0]])
jR=s.Matrix([[1,0],[0,1],[1,0]])
OL=jL.H*G;OR=jR.H*G
assert jL.H*G*jL!=jR.H*G*jR
assert OL.rank()==OR.rank()==2
fiber_dimension=6-OL.row_join(-OR).rank()
assert fiber_dimension==4
assert fiber_dimension-((3-OL.rank())+(3-OR.rank()))==2
result={'schema':'marici.grothendieck.ordinary-middle-block-green-obstruction.v1','passed':True,
        'fixture_pairings':{'common':0,'left_compressed':-8,'right_compressed':0},
        'formal_residual':'4 tau^2 K(g_middle, g_p_to_pq + g_q_to_pq)',
        'checks':{'middle_grade_preserved_on_common_carrier':True,
                  'coarse_left_and_right_forms_differ':True,
                  'unassigned_feature_gram_residual_verified':True,
                  'raw_four_port_coefficient_not_confused_with_two_sheet_signature':True,
                  'paired_observer_correspondence_without_relation_metric':True},
        'scope':'Exact source differentiation and formal pairing residual. Actual full spectral nonvanishing uses the four-trace span lemma in the companion note, not the fixture Gram or sampled spectral rank.'}
p=ROOT/'research/grothendieck/results/ordinary-middle-block-green-obstruction.json'
p.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
