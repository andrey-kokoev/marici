"""Compile composition-complete finite residual cut states from actual transitions.

Freeze finite-state representation (<=70 classes), not stored execution words.
Start from 61 observed local tuples and split only by transition behavior.
"""
from pathlib import Path
from collections import deque
import subprocess
import json
import hashlib
import sys
ROOT = Path(__file__).resolve().parents[3]
N = ROOT / 'research/nima'
OUT = ROOT / 'research/voevodsky/results'
p = N / 'results/relational-live-witness-runtime.json'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p, x): p.write_text(json.dumps(x, indent=2) + '\n')
cp = OUT / 'residual-cut-relation-contract.json'
save(cp, {'source_packet_sha256': sha(p),
 'observations': 'Local view tuple; acceptance/rejection of all 18 declared labels.',
 'representation': 'At most 70 finite cut-state classes, output map, and accepted/rejected edge relations; no execution words retained as live state.',
 'construction': 'Begin with equality of local tuples; refine by accepted/rejected successor classes to a fixed point.',
 'prediction': 'Derived cut relations compose exactly with source projection, preserve transpose and all marked-cut path queries.',
 'scope': 'Existing finite behavioral source packet; fixed alphabet. Claim not extended to arbitrary nonlocal constraints or new labels.'})
subprocess.run([sys.executable, str(N / 'checkers/verify_relational_membership_live_witness.py')], check=True, capture_output=True, text=True)
d = json.loads(p.read_text()); rows = d['lifted_rows']; labels = d['labels']; n = len(rows)
lookup = {(tuple(r['views']),r['origin']): i for i,r in enumerate(rows)}
table = [[(ok,lookup[tuple(v),b]) for ok,v,b in r['transitions']] for r in rows]
outputs = [tuple(r['views']) for r in rows]
def classify(keys):
 ids={}; return [ids.setdefault(k,len(ids)) for k in keys]
classes = classify(outputs); old = list(classes); sizes=[len(set(classes))]
while True:
 nxt=classify([(outputs[i],tuple((ok,classes[j]) for ok,j in row)) for i,row in enumerate(table)])
 sizes.append(len(set(nxt)))
 if nxt==classes: break
 classes=nxt
assert sizes[0]==61 and len(set(classes))==70
qtable=[None]*70; qout=[None]*70
for i,c in enumerate(classes):
 edges=[(ok,classes[j]) for ok,j in table[i]]
 if qtable[c] is not None: assert qtable[c]==edges and qout[c]==outputs[i]
 qtable[c]=edges; qout[c]=outputs[i]
def relation(a,ok): return {(i,j) for i,row in enumerate(table) for flag,j in [row[a]] if flag==ok}
rels=[relation(a,ok) for a in range(18) for ok in (False,True)]
def project(R,part): return {(part[i],part[j]) for i,j in R}
def transpose(R): return {(j,i) for i,j in R}
def compose(R,S):
 nxt={}
 for j,k in S:nxt.setdefault(j,set()).add(k)
 return {(i,k) for i,j in R for k in nxt.get(j,())}
old_failures=0; tests=0
for R in rels:
 assert project(transpose(R),classes)==transpose(project(R,classes))
 for S in rels:
  source=compose(R,S)
  assert project(source,classes)==compose(project(R,classes),project(S,classes))
  old_failures += project(source,old)!=compose(project(R,old),project(S,old))
  tests+=1
assert old_failures==12
# Every marked source path transports pointwise through a bijection on these
# behavioral rows. This gives exact path lifting for every finite chain.
assert len(set(classes))==n
inverse={c:i for i,c in enumerate(classes)}
for i,row in enumerate(table):
 for a,(ok,j) in enumerate(row):
  qok,qj=qtable[classes[i]][a]
  assert qok==ok and inverse[qj]==j
# Minimality certificates of split tuples, constructed from continuations.
def distinguish(i,j):
 todo=deque([(i,j,())]);seen=set()
 while todo:
  a,b,w=todo.popleft()
  if outputs[a]!=outputs[b]:return w
  if (a,b) in seen:continue
  seen.add((a,b))
  for k,((ok,x),(flag,y)) in enumerate(zip(table[a],table[b])):
   if ok!=flag:return w+(k,)
   todo.append((x,y,w+(k,)))
 raise AssertionError('no distinguishing word')
splits=[]
for c in set(old):
 group=[i for i in range(n) if old[i]==c]
 if len(group)>1:
  assert len(group)==2
  word=distinguish(*group)
  splits.append({'local_tuple':list(outputs[group[0]]),'source_rows':group,'word':[labels[a] for a in word]})
assert len(splits)==9
assert sha(p)==json.loads(cp.read_text())['source_packet_sha256']
packet={'classes':classes,'outputs':qout,'transitions':qtable,'labels':labels,
        'construction_sizes':sizes,'split_witnesses':splits}
packet_path=OUT / 'compiled-residual-cut-relations.json';save(packet_path,packet)
report={'passed':True,'contract_sha256':sha(cp),'compiled_packet_sha256':sha(packet_path),
 'refinement_sizes':sizes,'minimal_residual_cut_states':70,'split_local_fibers':9,
 'old_projected_composition_failures':old_failures,'compiled_stratum_pair_checks':tests,
 'transpose_checks':36,'step_lift_checks':n*18,
 'disposition':'Corroborated for the frozen behavioral source. Residual compiler recovers all 70 behavioral distinctions from the 61-view starting partition.',
 'limitation':'No further state compression survives this full audit language. The method uses the independently verified finite source packet; no bound for open-ended source constraints follows.',
 'structural_result':'The residual state is the information that must persist at the shared cut for relational joins to preserve source witnesses.'}
save(OUT / 'residual-cut-relation-verification.json',report)
print(json.dumps(report,indent=2))
