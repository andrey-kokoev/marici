"""Read-only AST extraction of owner matrices; no upstream imports or writes."""
import ast,json,hashlib
from pathlib import Path
from sympy import Matrix,eye,zeros,diag
from itertools import combinations
src=Path('research/voevodsky/check_physical_derived_pullback_after_transform.py');raw=src.read_bytes();tree=ast.parse(raw)
main=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='main')
vals={}
for n in main.body:
    if isinstance(n,ast.Assign) and len(n.targets)==1 and isinstance(n.targets[0],ast.Name):
        try:vals[n.targets[0].id]=ast.literal_eval(n.value)
        except (ValueError,TypeError):pass
d1,d2,d3=[Matrix(vals[k]) for k in ('d1','d2','d3')]
assert d2==Matrix([[1,0,0,0],[1,0,0,0],[0,1,0,-1],[0,-1,1,0],[0,0,-1,1]])
assert d1*d2==zeros(1,4) and d2*d3==zeros(5,1)
P=Matrix([[0,0,1],[1,0,0],[0,1,0]]);R1=diag(eye(2),P);R2=diag(eye(1),P)
assert R1*d2==d2*R2 and R2*d3==d3 and d1*R1==d1
z=Matrix(vals['primitive']);h=Matrix([0,-1,0,0]);r=Matrix([[0,0,1,1,1]])
assert d2*h==(R1-eye(5))*z and (eye(4)+R2+R2**2)*h==-d3
assert r*R1==r and r*z==Matrix([1])
minor=next((rows,cols,int(d2.extract(rows,cols).det())) for rows in combinations(range(5),3) for cols in combinations(range(4),3) if abs(d2.extract(rows,cols).det())==1)
assert d2.rank()==3 and d3.rank()==1 and d1.rank()==1
# A unit entry and the same sampled-prime ranks do NOT establish saturation.
bad=diag(1,1,7);assert bad[0,0]==1 and bad.det()==7
assert all(int(bad.det())%p for p in (2,3,5,101))
out={'status':'passed','source_sha256':hashlib.sha256(raw).hexdigest(),'matrix_equivariance':True,'primitive_and_coherence':True,'rank_three_unit_minor':{'rows':minor[0],'columns':minor[1],'determinant':minor[2]},'unit_entry_saturation_control':'diag(1,1,7) has unit entry and full rank modulo 2,3,5,101 but nonsaturated image','source_boundary':'d1,d2,d3 and primitive are literals inside main; no matrix construction from transform outputs is serialized here','scope':'Independently verifies the specified matrix-level cyclic lift, not its upstream geometric naturality.'}
Path('research/nima/results/cyclic_source_boundary.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
