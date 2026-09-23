"""Invalidate comparison on union of endpoint supports before cancellation."""
from fractions import Fraction as Q
from pathlib import Path
import json
P=(Q(1),Q(2),Q(0),Q(0));R=(Q(0),Q(1),Q(1),Q(1));single=(Q(0),Q(1),Q(0),Q(0))
packets={'P':P,'Q':R,'single':single}
support={name:{i for i,v in enumerate(m) if v} for name,m in packets.items()}
edges={'P_to_Q':('P','Q')}
edge_support={name:support[a]|support[b] for name,(a,b) in edges.items()}
index={i:{'packets':sorted(name for name,s in support.items() if i in s),'edges':sorted(name for name,s in edge_support.items() if i in s)} for i in range(4)}
assert index[0]=={'packets':['P'],'edges':['P_to_Q']}
assert index[1]=={'packets':['P','Q','single'],'edges':['P_to_Q']}
assert index[2]==index[3]=={'packets':['Q'],'edges':['P_to_Q']}
def affected(rows):return {'packets':sorted({x for i in rows for x in index[i]['packets']}),'edges':sorted({x for i in rows for x in index[i]['edges']})}
assert affected((1,3))=={'packets':['P','Q','single'],'edges':['P_to_Q']}
# A zero aggregate signed bound change does not cancel row-level invalidations.
k=tuple(R[i]-P[i] for i in range(4));changes=(Q(0),Q(1),Q(0),Q(1))
assert sum(k[i]*changes[i] for i in range(4))==0 and affected((1,3))['edges']==['P_to_Q']
report={'passed':True,'row_index':{str(i):v for i,v in index.items()},'two_changed_upper_rows':affected((1,3)),'signed_aggregate_change':'0 but edge and endpoints still invalidated','authority_scope':'all full-manifest publication claims stale on any source row edit','scope':'Conservative LOCAL dependency index for chosen packets and edge, not a claim every invalidated packet ultimately fails or that owner authorized new rows.'}
out=Path(__file__).resolve().parents[1]/'results/mixed-row-dependency-index.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
