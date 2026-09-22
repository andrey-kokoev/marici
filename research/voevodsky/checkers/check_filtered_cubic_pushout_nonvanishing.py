"""Exact bimodule fixture: unfiltered splitting, nonsplit filtration level 2.

Left/right k[t] actions commute; IN=L while NI=0. The actual 270-row
source obstruction is separately verified by its owning source checker.
"""
from pathlib import Path
import json
import sympy as s
# K=(n,l,z); N=(n,l), L=(l). Left t sends n to l; right t sends z to l.
KL=s.Matrix([[0,0,0],[1,0,0],[0,0,0]])
KR=s.Matrix([[0,0,0],[0,0,1],[0,0,0]])
assert KL*KR==KR*KL==s.zeros(3)
N=s.eye(3)[:,:2];L=s.Matrix([[0],[1],[0]])
NL=s.Matrix([[0,0],[1,0]]);NR=s.zeros(2)
assert KL*N==N*NL and KR*N==N*NR
assert (KL*N).rank()==1 and KR*N==s.zeros(3,2)
# A=(a,b), B=(b), G=(a mod b); right t sends a to b.
AR=s.Matrix([[0,0],[1,0]]);AL=s.zeros(2)
i=s.Matrix([[0],[1]]);q=s.Matrix([[1,0]])
H=s.Matrix([[0,0],[0,1],[1,0]])
f=L
assert H*i==f and KL*H==H*AL and KR*H==H*AR
# No N-valued equivariant extension of f: right action on N is zero.
a,b,c,d=s.symbols('a b c d')
HN=s.Matrix([[a,b],[c,d]])
conditions=list(NR*HN-HN*AR)+list(HN*i-s.Matrix([[0],[1]]))
assert s.solve(conditions,(a,b,c,d))==[]
# Underlying pushout is split as K+G. Its filtration level 2 is a graph
# pullback, spanned by n,l,z+g, and level 3 is l.
PL=s.diag(KL,s.zeros(1));PR=s.diag(KR,s.zeros(1))
F2=s.Matrix([[1,0,0],[0,1,0],[0,0,1],[0,0,1]])
F3=s.Matrix([[0],[1],[0],[0]])
pG=s.Matrix([[0,0,0,1]])
assert F2.rank()==3 and F2.row_join(F3).rank()==3
assert PL*F2==F2*KL and PR*F2==F2*KR
assert pG*F2==s.Matrix([[0,0,1]])
# The unfiltered section exists but misses the F2 graph.
section=s.Matrix([[0],[0],[0],[1]])
assert pG*section==s.eye(1) and PL*section==PR*section==s.zeros(4,1)
assert F2.row_join(section).rank()==4
# Every section into F2 has z coordinate one, hence nonzero right t action.
u,v=s.symbols('u v')
section2=s.Matrix([[u],[v],[1]])
assert KR*section2==L
# Lower-filtration escape beta:G->K/N is nonzero and cannot lift to a
# bimodule map G->K (a lift has z coordinate one, contradicting KR=0).
beta=s.eye(1)
assert beta.rank()==1
result={'passed':True,'checks':{
 'commuting_bimodule_actions':True,'left_right_ideal_asymmetry':True,
 'underlying_nullhomotopy_exists':True,'N_valued_extension_impossible':True,
 'underlying_pushout_split':True,'filtration_level_two_pushout_nonsplit':True,
 'split_model_retains_nontrivial_graph_filtration':True},
 'scope':'Exact bimodule and filtration fixture. Actual filtered-derived nonvanishing is detected by the exact F2 functor and the 270-row P_y obstruction, not inferred from failure of a single filtered chain homotopy.'}
ROOT=Path(__file__).resolve().parents[3]
out=ROOT/'research/voevodsky/results/filtered-cubic-pushout-nonvanishing.json'
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
