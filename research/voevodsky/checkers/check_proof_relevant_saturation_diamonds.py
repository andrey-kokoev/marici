"""Compare existence and discrete witness equivalence in saturation diamonds."""
from pathlib import Path
from itertools import combinations, product
import subprocess
import sys
import json
import hashlib
ROOT=Path(__file__).resolve().parents[3]
DIR=ROOT/'research/voevodsky/results/continuation-quotient'
OUT=ROOT/'research/voevodsky/results'
subprocess.run([sys.executable,str(Path(__file__).with_name('check_saturation_diamond.py'))],check=True,capture_output=True,text=True)
p=DIR/'saturation-diamond.json';r=json.loads(p.read_text());L,M=r['L'],r['M'];P=sorted(L)
def subsets(S):
 for n in range(len(S)+1):
  for t in combinations(S,n):yield t

def analyze(carrier,L,M):
 gaps=[];count_gaps=[];nonempty=0
 for a,c in product(carrier,repeat=2):
  left=[b for b in carrier if L[a]==L[b] and M[b]==M[c]]
  right=[d for d in carrier if M[a]==M[d] and L[d]==L[c]]
  if bool(left)!=bool(right):gaps.append((a,c,left,right))
  if len(left)!=len(right):count_gaps.append((a,c,left,right))
  nonempty+=bool(left) and bool(right)
 return gaps,count_gaps,nonempty
actual=[]
for carrier in subsets(P):
 a,b,count=analyze(carrier,L,M)
 actual.append({'carrier':carrier,'endpoint_commutes':not a,'discrete_fibers_equicardinal':not b,'nonempty_compared_fibers':count})
# Existing commuting restrictions are too small to distinguish the two claims.
assert all(x['discrete_fibers_equicardinal'] for x in actual if x['endpoint_commutes'])
# Independent minimal adversary: two transverse equivalence relations with
# nonuniform intersection multiplicities. All four intersection cells exist,
# so endpoint composition is total both ways, but witness counts differ.
source=[('r0','c0',0),('r0','c0',1),('r0','c1',0),('r1','c0',0),('r1','c1',0)]
ids=list(range(5));row={i:s[0] for i,s in enumerate(source)};col={i:s[1] for i,s in enumerate(source)}
a,b,count=analyze(ids,row,col)
assert not a and b
witness=next(x for x in b if len(x[2])==2 and len(x[3])==1)
# Verify source witness distinctions can be observed in the declared extension:
# an identity audit of the middle source id separates both witnesses.
x,z,left,right=witness
assert len(set(left))==2
# Positive repair for this FIXTURE ONLY: retain an explicit common multiplicity
# coordinate, so every row/column cell is a copy of the same two-point space.
balanced=list(product(('r0','r1'),('c0','c1'),(0,1)))
def horizontal(s,t):return s[0]==t[0]
def vertical(s,t):return s[1]==t[1]
def rotate_middle(a,m,c):
 assert horizontal(a,m) and vertical(m,c)
 return (c[0],a[1],m[2])
checks=0
for a,c in product(balanced,repeat=2):
 left=[m for m in balanced if horizontal(a,m) and vertical(m,c)]
 right=[m for m in balanced if vertical(a,m) and horizontal(m,c)]
 assert {rotate_middle(a,m,c) for m in left}==set(right)
 for m in left:
  d=rotate_middle(a,m,c)
  restored=(a[0],c[1],d[2])
  assert restored==m
  checks+=1
# A two-point fiber has at least two bijections; endpoint equality alone
# cannot distinguish preserving the declared tag from exchanging its values.
assert {0:0,1:1}!={0:1,1:0}
report={'passed':True,'actual_source_restrictions':actual,
 'actual_conclusion':'Commuting restrictions have equicardinal discrete fibers here; no general equivalence theorem follows.',
 'independent_adversary':{'source_states':source,'endpoint_relations_commute':True,
                         'boundary':list(witness[:2]),'left_middle_witnesses':witness[2],
                         'right_middle_witnesses':witness[3],
                         'obstruction':'Two-element discrete witness type cannot be equivalent to a singleton.'},
 'balanced_fixture':{'source_states':len(balanced),'middle_witness_transport_checks':checks,
                     'transport':'(row(a),col(c),tag) maps to (row(c),col(a),same tag)',
                     'scope':'Explicitly different source with a common tag across all cells; not a repair authorized for the five-state source.'},
 'structural_result':'Permutability of kernel relations controls nonemptiness of composite fibers, not equivalence of their witness types. Proof-relevant interchange requires additional comparison data.',
 'higher_coherence_status':'Not established by cardinality or by a single chosen bijection.',
 'input_sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
(OUT/'proof-relevant-saturation-diamonds.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k!='actual_source_restrictions'},indent=2))
