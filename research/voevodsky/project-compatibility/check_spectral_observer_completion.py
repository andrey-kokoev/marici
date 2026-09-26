"""Exact, read-only audit of the recovered source observer and its compatibility complex."""
from pathlib import Path
import hashlib,json
import sympy as s
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2]
paths=[Path(__file__),HERE/'spectral-observer-compatible-completion.md',ROOT/'research/benincasa/checkers/gram_wall_smith_nearby_cone.rs',ROOT/'research/benincasa/spectral-gaussian-source-to-observer-complex.json']
def hashes():return {p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
before=hashes();c=s.symbols('c',real=True)
T=s.Matrix([[1,0,0],[1,1,-c],[1,1,c]])
Q=s.Matrix([[1,2,0],[1,-1,-1],[1,-1,1]])
A=T.T;B=Q.T;k=s.Matrix([0,1,-1]);I=s.eye(3)
assert T.det()==2*c and Q.det()==-6
assert A.subs(c,0)*k==s.zeros(3,1) and B*k==s.Matrix([0,0,-2])
assert Q.T*Q==s.diag(3,6,2)
assert sorted(B.singular_values(),key=lambda v:float(v))==[s.sqrt(2),s.sqrt(3),s.sqrt(6)]
F=A.col_join(B);H=I.row_join(-A*B.inv());L=s.zeros(3).row_join(B.inv())
assert H*F==s.zeros(3) and L*F==I
assert F.rank()==3 and H.rank()==3
assert 6-F.rank()==3 # ordinary two-term cone has nonzero cokernel
for value in (-2,-1,0,1,2):
 assert F.subs(c,value).rank()==3 and H.subs(c,value).rank()==3
 assert (H*F).subs(c,value)==s.zeros(3)
C=s.symbols('C1:4',nonzero=True,real=True);W=-8*s.diag(*C)
AC=A*W;BC=B*W
assert s.simplify(AC*BC.inv()-A*B.inv())==s.zeros(3)
FC=AC.col_join(BC);HC=I.row_join(-AC*BC.inv())
assert s.simplify(HC*FC)==s.zeros(3)
assert s.simplify(BC.inv()*BC)==I
assert before==hashes()
report={'passed':True,'source_unchanged':True,'source_sha256':before,
 'tensor_determinant':str(T.det()),'direct_score_determinant':int(B.det()),
 'wall_kernel':[0,1,-1],'direct_score_on_wall_kernel':[0,0,-2],
 'stacked_observer_rank':3,'ordinary_stacked_cone_cokernel_rank':3,
 'compatible_complex_ranks':[3,6,3],'compatibility_differential':'H(y,z)=y-A B^-1 z',
 'normalized_lower_bound':'sqrt(2)','contact_weighted_lower_bound':'8 sqrt(2) min_e |C_e|',
 'scope':'Existing local source representative and Euclidean finite-packet norm. Exactness is for the stated compatibility complex, not the ordinary stacked cone. No global physical completion or owner adoption inferred.'}
(HERE/'spectral-observer-compatible-completion.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,indent=2))
