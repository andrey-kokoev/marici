"""Retrospective candidate for order, not native law. Input: memberships in ordered P/N/E cells and C/M kinds and three previously specified stage words. Sort slots without reversing any strict interval precedence; exhaust all orders on ties. Hold stored windows aside until comparison. No subscript comparisons."""
import itertools,json
from pathlib import Path
D=Path(__file__).resolve().parents[1];load=lambda f:json.loads((D/'results'/f).read_text());T=load('pne_body_membership_decoder.json')['template'];target=load('pne_kind_index_projection.json')['windows'];words=['CMC','MCM','MCC'];o={}
for policy in ('none','first','last','both','both_no_word','reverse'):
 rows=[]
 for i,w in enumerate(words):
  vs=[v for v in T if T[v][i]=='1'];bounds={v:(T[v].index('1'),T[v].rindex('1')) for v in vs};out=[]
  for p in itertools.permutations(vs):
   if policy!='both_no_word' and ''.join(v[0] for v in p[:3])!=w:continue
   dims={'none':[],'first':[0],'last':[1]}.get(policy,[0,1]);sign=-1 if policy=='reverse' else 1
   if any(sign*(bounds[a][k]-bounds[b][k])>0 for a,b in zip(p,p[1:]) for k in dims):continue
   out.append(p)
  rows.append(dict(count=len(out),observed=any(list(p[:3])==target[i] for p in out),orders=out if policy=='both' else None))
 o[policy]=rows
assert all(r['observed'] and r['count']==1 for r in o['both']);print({k:[(r['count'],r['observed']) for r in v] for k,v in o.items()});(D/'results/pne_body_interval_reader.json').write_text(json.dumps(o,indent=2)+'\n')
