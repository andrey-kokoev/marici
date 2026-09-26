"""Direct specialization of authored PNNMHVnew summation and boundary rules."""
from pathlib import Path
import json,hashlib
root=Path(__file__).resolve().parents[3]
source=root/'research/sources/nima/papers/n2mhv-tree/0808.2475/newrecursionv6.tex'
text=source.read_text()
for label in ('PNNMHVnew','generalR','Lrep','Urep'):assert r'\label{'+label+'}' in text
rows=[];n=9
for a in range(2,n):
 for b in range(a+2,n):
  for c in range(a+1,b+1):
   for d in range(c+2,b+1):
    rows.append(dict(outer_pair=[a,b],inner_pair=[c,d],branch='left-nested',coefficient=1,terminal_xi_path=[n,b,a],boundary_updates=[{'side':'upper','replacement_path':[a,b]}] if d==b else []))
  for c in range(b,n):
   for d in range(c+2,n):
    rows.append(dict(outer_pair=[a,b],inner_pair=[c,d],branch='right-nested',coefficient=1,terminal_xi_path=[n],boundary_updates=[{'side':'lower','replacement_path':[a,b]}] if c==b else []))
prior=json.loads((root/'research/nima/results/nine-point-authored-four-pair-history-screen.json').read_text())
def key(r):return tuple(r['outer_pair']),tuple(r['inner_pair']),r['branch']
old={key(r):r for r in prior['all_history_records']}
assert len(rows)==len(old)==50 and len({key(r) for r in rows})==50
for r in rows:
 previous=old[key(r)]
 assert r['terminal_xi_path']==previous['terminal_xi_path']
 assert r['boundary_updates']==previous['boundary_updates'],(r,previous)
report={'passed':True,'source':str(source.relative_to(root)),'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'formula':'A9 NNMHV = A9 MHV times P9 NNMHV; P9 is the authored nested-R sum','histories':len(rows),'left':sum(r['branch']=='left-nested' for r in rows),'right':sum(r['branch']=='right-nested' for r in rows),'boundary_corrected':sum(bool(r['boundary_updates']) for r in rows),'records':rows,'scope':'Exact authored index/coefficient/boundary specialization and agreement with inherited history ledger. Does not evaluate generalized-R denominators, prove geometric cell correspondence, or identify the four barrier channels with the full amplitude.'}
p=root/'research/voevodsky/results/nine-point-source-history-contract.json';p.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({k:v for k,v in report.items() if k!='records'},indent=2))
