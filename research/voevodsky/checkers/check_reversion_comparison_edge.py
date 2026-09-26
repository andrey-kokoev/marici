"""Restored row bytes require fresh valid packet endpoints and a fresh typed edge."""
from pathlib import Path
import json
rows=(((-1,0),0),((1,0),1),((0,-1),0),((0,1),1))
def packet(id,m,c):return {'id':id,'generation':3,'weights':m,'surplus':c,'target':((1,0),2)}
p=packet('P-g3',(0,1,0,0),1);q=packet('Q-g3',(1,2,0,0),0)
def valid(v):
 m=v['weights'];c=v['surplus'];normal,bound=v['target']
 return v['generation']==3 and min((*m,c))>=0 and tuple(sum(rows[i][0][j]*m[i] for i in range(4)) for j in (0,1))==normal and sum(rows[i][1]*m[i] for i in range(4))+c==bound
catalogue={p['id']:p,q['id']:q}
def edge(e):
 if e['generation']!=3:return 'STALE_EDGE_GENERATION'
 if e['from'] not in catalogue or e['to'] not in catalogue:return 'STALE_ENDPOINT_ID'
 a,b=catalogue[e['from']],catalogue[e['to']]
 if not valid(a) or not valid(b) or a['target']!=b['target'] or e['rule']!='comparison@1':return 'INVALID_COMPARISON'
 return 'LOCAL_RECHECKED_EDGE_NO_AUTHORITY'
assert valid(p) and valid(q)
assert edge({'from':'P-g3','to':'Q-g3','rule':'comparison@1','generation':3})=='LOCAL_RECHECKED_EDGE_NO_AUTHORITY'
assert edge({'from':'P-g1','to':'Q-g1','rule':'comparison@1','generation':3})=='STALE_ENDPOINT_ID'
assert edge({'from':'P-g3','to':'Q-g3','rule':'comparison@1','generation':1})=='STALE_EDGE_GENERATION'
report={'passed':True,'new_packets':'two exact x<=2 proofs on restored matrix g3','new_comparison':'locally rechecked, not historical/authorized','copied_old_endpoint_ids':'rejected despite equal g1/g3 matrix bytes','old_edge_generation':'rejected','scope':'No persistent edit, source issuer or analytic mapping.'}
out=Path(__file__).resolve().parents[1]/'results/reversion-comparison-edge.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
