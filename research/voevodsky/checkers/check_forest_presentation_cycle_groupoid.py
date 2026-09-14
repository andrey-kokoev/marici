#!/usr/bin/env python3
"""Exact groupoid, reciprocal naturality, and metric-congruence checks."""
from pathlib import Path
import hashlib,json
import sympy as s
ROOT=Path(__file__).resolve().parents[3]
CONTRACT=ROOT/'research/voevodsky/contracts/forest-presentation-cycle-groupoid.v1.json'
RESULT=ROOT/'research/voevodsky/results/forest_presentation_cycle_groupoid.json'
d=json.loads(CONTRACT.read_text())
edges=[(0,1),(1,0),(1,2),(2,1),(0,2),(2,0)]; forests={'T':[0,2],'RT':[1,3],'U':[0,4]}
B=s.zeros(3,6)
for j,(a,b) in enumerate(edges): B[a,j]=-1; B[b,j]=1
R=s.zeros(6)
for a,b in ((0,1),(2,3),(4,5)): R[a,b]=R[b,a]=1
def basis(tree):
 chords=[j for j in range(6) if j not in tree]; cols=[]
 for q in chords:
  x=s.zeros(6,1); x[q]=1; sol=list(s.linsolve((B[:-1,tree],-B[:-1,q])))[0]
  for j,v in zip(tree,sol): x[j]=v
  cols.append(x)
 return s.Matrix.hstack(*cols)
F={k:basis(v) for k,v in forests.items()}
def change(dst,src): return F[dst].gauss_jordan_solve(F[src])[0]
C={(a,b):change(a,b) for a in forests for b in forests}
checks={
 'cycle_rank_four':all(x.rank()==4 and B*x==s.zeros(3,4) for x in F.values()),
 'identities':all(C[(a,a)]==s.eye(4) for a in forests),
 'inverses':all(C[(a,b)]*C[(b,a)]==s.eye(4) for a in forests for b in forests),
 'composition':all(C[(a,b)]*C[(b,c)]==C[(a,c)] for a in forests for b in forests for c in forests),
 'integral_unimodular_arrows':all(all(x.q==1 for x in M) and abs(M.det())==1 for M in C.values()),
 'represented_cycles_unchanged':all(F[a]*C[(a,b)]==F[b] for a in forests for b in forests),
 'edge_reciprocal_involution':R*R==s.eye(6) and B*R*R==B,
}
# Reflected object map is explicit for T and RT; U reflects to a fourth valid forest RU.
FRU=basis([1,5]); Fall={**F,'RU':FRU}; obj={'T':'RT','RT':'T','U':'RU','RU':'U'}
def refl(a): return Fall[obj[a]].gauss_jordan_solve(R*Fall[a])[0]
def ch_all(dst,src): return Fall[dst].gauss_jordan_solve(Fall[src])[0]
checks['reciprocal_coordinate_involution']=all(refl(obj[a])*refl(a)==s.eye(4) for a in Fall)
checks['reciprocal_naturality']=all(refl(b)*ch_all(b,a)==ch_all(obj[b],obj[a])*refl(a) for a in Fall for b in Fall)
# Reflection-invariant unequal weights on reciprocal pairs.
W=s.diag(1,1,2,2,3,3); Q={a:Fall[a].T*W*Fall[a] for a in Fall}
checks['ambient_metric_reflection_invariant']=R.T*W*R==W
checks['metric_arrow_congruence']=all(Q[a]==ch_all(b,a).T*Q[b]*ch_all(b,a) for a in Fall for b in Fall)
checks['reciprocal_metric_isometry']=all(Q[a]==refl(a).T*Q[obj[a]]*refl(a) for a in Fall)
checks['no_fixed_forest_needed']=forests['T']!=forests['RT'] and checks['reciprocal_coordinate_involution']
checks['completion_and_calibration_not_promoted']=not d['claim_boundary']['cutoff_groupoid_completion_constructed'] and not d['claim_boundary']['edge_form_source_calibrated']
checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.forest-presentation-cycle-groupoid-check.v1','contract_sha256':hashlib.sha256(CONTRACT.read_bytes()).hexdigest(),'checks':checks,'passed':all(checks.values()),'objects':list(Fall),'cycle_rank':4,'disposition':{'constructed':'finite forest-presentation groupoid with reciprocal involution, naturality, and metric congruence','replaces':'unsupported fixed-forest reflection invariance','remaining':'cutoff inclusion/forest-change interchange and source-calibrated edge form'}}
RESULT.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'passed':result['passed'],'check_count':len(checks),'objects':len(Fall),'cycle_rank':4}))
raise SystemExit(0 if result['passed'] else 1)
