"""Actual RS2 quotient data and weighted-star support boundary, read-only on owner artifacts."""
from pathlib import Path
import ast,hashlib,json,itertools
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2]
source=ROOT/'research/nima/checkers/check_rs2_canonical_c3_tate_bridge.py'
weighted=ROOT/'temp/readout-weighted-three-road-star.json'
paths=[Path(__file__),HERE/'readout-contract-tate-instance.md',source,weighted,ROOT/'research/voevodsky/check_weighted_three_road_star.rs',ROOT/'research/nima/cross-sector-tate-naturality-closes-on-coefficients-but-not-yet-on-support.md']
def hashes():return {p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
before=hashes();mat={}
for node in ast.parse(source.read_text(encoding='utf-8')).body:
 if isinstance(node,ast.Assign) and len(node.targets)==1 and isinstance(node.targets[0],ast.Name) and node.targets[0].id in ('g','s','identity'):
  mat[node.targets[0].id]=ast.literal_eval(node.value)
g,reflection,identity=mat['g'],mat['s'],mat['identity']
M=[[g[i][j]-identity[i][j] for j in range(2)] for i in range(2)]
def apply(A,v):return tuple(sum(a*b for a,b in zip(row,v)) for row in A)
O=lambda v:sum(v)%3
assert M[0][0]*M[1][1]-M[0][1]*M[1][0]==3
for v in itertools.product(range(-9,10),repeat=2):
 assert O(apply(M,v))==0
 assert O(apply(g,v))==O(v)
 assert O(apply(reflection,v))==(-O(v))%3
 if O(v)==0:
  x,y=v;k=(x+y)//3
  assert apply(M,(-x+k,-k))==v
# Actual mod3 regular norm: N sends v to(sum(v),sum(v),sum(v)).
kerN={v for v in itertools.product(range(3),repeat=3) if sum(v)%3==0}
imN={(a,a,a) for a in range(3)}
assert len(kerN)==9 and len(imN)==3 and imN<=kerN
q_regular=lambda v:(-v[0]+v[2])%3
assert {v for v in kerN if q_regular(v)==0}==imN
for x,y in itertools.product(range(3),repeat=2):
 embedded=((-x)%3,(x-y)%3,y)
 assert embedded in kerN and q_regular(embedded)==O((x,y))
K={(a,b) for a,b in itertools.product(range(3),repeat=2) if (b-a)%3==0}
image={(O((a,0)),O((a,0))) for a in range(3)}
assert K==image and {(b-a)%3 for a,b in itertools.product(range(3),repeat=2)}==set(range(3))
packet=json.loads(weighted.read_text(encoding='utf-8'))
assert packet['status']=='inconclusive'
assert packet['checks']['unlocalized_Tate_realization'].startswith('FAIL')
assert 'R0/(u4,u0,u2)' in packet['comparison']['unlocalized_obstruction']
assert all(value=='PASS' for key,value in packet['checks'].items() if key!='unlocalized_Tate_realization')
assert before==hashes()
report={'passed':True,'source_unchanged':True,'source_sha256':before,'actual_matrix_M':M,'integral_lattice_controls':19**2,'mod3_norm_kernel_size':9,'mod3_norm_image_size':3,'compatible_output_count':3,'coefficient_bridge':'D3-equivariant and integral','fresh_weighted_star_status':packet['status'],'global_supported_realization_check':packet['checks']['unlocalized_Tate_realization'],'scope':'Coefficient contract verified; global supported arrow remains unsupplied in inspected package. No forbidden inversion, physical identification or owner mutation.'}
(HERE/'readout-contract-tate-instance.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,indent=2))
