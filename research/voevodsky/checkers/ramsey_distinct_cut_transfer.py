"""First next-width control: no duplicate supports among four labeled ports."""
from itertools import combinations
from collections import Counter, defaultdict
from pathlib import Path
import json


def run(k):
    sites=range(1,k+1);rows=[s for s in combinations(sites,3) if min(s[1]-s[0],s[2]-s[1])>=2];mask={s:sum(1<<(i-1) for i in s) for s in rows};P=[p for n in (1,2,3,4) for p in combinations(rows,n)];cap={}
    for u in range(1<<k):
        path=[i for i in sites if not u>>(i-1)&1];chosen=[]
        for i in path:
            if not chosen or i!=chosen[-1]+1:chosen.append(i)
        cap[u]=chosen
    obs={}
    for p in P:
        u=0
        for s in p:u|=mask[s]
        q=cap[u];w=(p,q) if len(p)+len(q)>=7 else None
        if not w:w=next((obs[t] for t in combinations(p,len(p)-1) if obs.get(t)),None)
        obs[p]=w
    groups=defaultdict(list);counts=Counter();example=None
    for a,b in combinations(rows,2):
        if sum(abs(x-y) for x,y in zip(a,b))==1 and not obs[a,b]:groups[next(x for x,y in zip(a,b) if x!=y)].append((a,b))
    for cut,ps in groups.items():
        for at in combinations(rows,2):
            batch=[]
            for p in ps:
                if set(p)&set(at):continue
                if any(obs[tuple(sorted((*p,s)))] for s in at):continue
                w=obs[tuple(sorted(p+at))];batch.append((p,w));counts['single_legal_joint_trials']+=1;counts['joint_rejections']+=int(bool(w))
                if w:counts[f'rejections_with_preferred_{len(w[0])}_port_witness']+=1
            for (p,w),(q,v) in combinations(batch,2):
                if bool(w)==bool(v):continue
                counts['paired_contrasts']+=1
                if example is None:
                    good,bad,ob=(q,p,w) if w else (p,q,v);example=dict(cut=cut,legal=good,illegal=bad,attachments=at,witness_rows=ob[0],witness_sites=ob[1]);
    if example:
        def direct(rows):
            red={(i,i+1) for i in range(1,k)}|{(i,k+j) for j,s in enumerate(rows,1) for i in s};vs=range(1,k+len(rows)+1)
            return not any(all((e in red)==col for e in combinations(q,2)) for n,col in [(3,True),(7,False)] for q in combinations(vs,n))
        for label in ('legal','illegal'):
            p=example[label];a,b=example['attachments'];assert all(direct(t) for t in (p,(*p,a),(*p,b))) and direct((*p,a,b))==(label=='legal')
    return dict(width=k,counts=counts,example=example)

if __name__=='__main__':
    out=[run(k) for k in (7,8)];print(out);(Path(__file__).resolve().parents[1]/'results/ramsey_distinct_cut_transfer.json').write_text(json.dumps(out,indent=2)+'\n')
