"""Width transfer with four distinct all-blue-to-each-other ports, fixed (3,7) bans."""
from collections import Counter
from itertools import combinations
from pathlib import Path
import json


def run(k):
    rows=[sum(1<<v for v in q) for q in combinations(range(k),3) if min(q[1]-q[0],q[2]-q[1])>=2];sites=lambda m:[v+1 for v in range(k) if m>>v&1];cap=[];sets=[]
    for m in range(1<<k):
        q=[]
        for v in range(k):
            if not m>>v&1 and (not q or q[-1]!=v-1):q.append(v)
        sets.append(q);cap.append(len(q))
    count=Counter();ex={}
    for p,q in combinations(rows,2):
        delta=p^q
        if delta.bit_count()!=2 or not delta&(delta>>1):continue
        if cap[0]>=7 or cap[p]>=6 or cap[q]>=6 or cap[p|q]>=5:continue
        single=[s for s in rows if s not in (p,q) and cap[s]<6 and max(cap[s|p],cap[s|q])<5 and cap[s|p|q]<4];
        for s,t in combinations(single,2):
            count['eligible']+=1;u=s|t
            if cap[u|p|q]>=3:count['four_port']+=1;continue
            if max(cap[u|p],cap[u|q])>=4:
                mode='three_only_or_two';z=p if cap[u|p]>=4 else q;ports=(s,t,z);m=u|z
            elif cap[u]>=5:mode='needs_two';ports=(s,t);m=u
            else:count['accept']+=1;continue
            count[mode]+=1
            if mode not in ex or (mode=='three_only_or_two' and ex[mode]['two_port_possible'] and cap[u]<5):
                ex[mode]=dict(parent=list(map(sites,(p,q))),attachments=list(map(sites,(s,t))),witness_ports=list(map(sites,ports)),witness_sites=[i+1 for i in sets[m][:7-len(ports)]],two_port_possible=cap[u]>=5)
    for z in ex.values():
        def legal(ss):
            red={(i,i+1) for i in range(1,k)}|{(v,k+j) for j,row in enumerate(ss,1) for v in row};vs=range(1,k+len(ss)+1);return not any(all((e in red)==color for e in combinations(c,2)) for n,color in [(3,True),(7,False)] for c in combinations(vs,n))
        a,b=z['attachments'];p=z['parent'];assert legal(p+[a]) and legal(p+[b]) and not legal(p+[a,b]);assert len(sets[sum(1<<(v-1) for v in set().union(*(set(s) for s in p+[a,b])))])<3
    return dict(width=k,counts=count,examples=ex)

if __name__=='__main__':
    data=[run(k) for k in range(7,13)];print(data);(Path(__file__).resolve().parents[1]/'results/ramsey_joint_witness_sizes.json').write_text(json.dumps(data,indent=2)+'\n')
