"""Prospective transfer of the two-end forest -> six-cycle observation. Freeze before compare."""
import json,gzip,sys
from itertools import combinations
from ramsey38_twisted_vertex_holdout import shell_scan
from ramsey38_record4_combined_trial import prev,graph
P=prev.out/'ramsey38_cycle_direction_predictions.json';R=prev.out/'ramsey38_cycle_direction_comparison.json'
protocol='Scan records 8 onward then red edges in lexical order; mask both core attachments. Require exactly two unordered completions differing by one added vertex on one side; six or seven red neighbors per root and supports <=4 in both branches. Require forest to one six-cycle. Take first ten distinct labeled endpoint/attachment/induced-core cases. Name unchanged side by smaller endpoint (swap symmetry); compare exact single-hidden-row sets only on common outside vertices, excluding rows not short in either branch. Prediction: red branch gains a row at the unchanged-support end AND loses one at the changed-support end. This does not predict the stored optional color.'
def candidates(g,u,v):
    core=sorted(set(g)-{u,v});M=(1<<25)-1;adj=[sum(1<<i for i,x in enumerate(core) if x in g[w]) for w in core];inds=[]
    def walk(mask,s):
        inds.append(s)
        while mask:
            b=mask&-mask;mask-=b;walk(mask&~adj[b.bit_length()-1],s|b)
    walk(M,0);assert max(map(int.bit_count,inds))<=7;qs=[x for x in inds if x.bit_count()==7];ok=[x for x in inds if x.bit_count()<=6 and all(x&q for q in qs)];pairs=[set((a,b)) for a,b in combinations(ok,2) if not a&b]
    if len(pairs)!=2:return
    shared=pairs[0]&pairs[1];diff=sorted(pairs[0]^pairs[1],key=int.bit_count)
    if len(shared)!=1 or len(diff)!=2:return
    a=next(iter(shared));b,c=diff
    if b&c!=b or (c^b).bit_count()!=1 or min(a.bit_count(),b.bit_count())<5:return
    A,B,C=([x for i,x in enumerate(core) if h>>i&1] for h in (a,b,c));return A,B,C

def make(g,u,v,A,B):
    h={w:s-{u,v} for w,s in g.items() if w not in (u,v)};h.update({u:set(A)|{v},v:set(B)|{u}})
    for w in (u,v):
        for z in h[w]-{u,v}:h[z].add(w)
    return h

def cycle(g,A,B):
    nb={v:g[v]&set(B if v in A else A) for v in A+B};changed=True
    while changed:
        changed=False
        for v in list(nb):
            if len(nb[v])<2:
                for w in nb.pop(v):nb[w].remove(v)
                changed=True
    return nb

def eligible(h,r):return {v for v,s in h.items() if v not in h[r]|{r} and len(s&h[r])<4}
if __name__=='__main__' and sys.argv[1]=='freeze':
    entries=[];seen=set()
    with gzip.open(prev.catalogue,'rt') as f:
        for i,line in enumerate(f,1):
            if i<8:continue
            w=line.strip();g=graph(w)
            for u,v in combinations(sorted(g),2):
                if v not in g[u]:continue
                abc=candidates(g,u,v)
                if not abc:continue
                a,b,c=abc;cy=cycle(g,a,c)
                if cycle(g,a,b) or len(cy)!=6 or not all(len(s)==2 for s in cy.values()):continue
                gs=[make(g,u,v,a,z) for z in (b,c)]
                if any(len(h[r]&s)>4 for h in gs for r in (u,v) for z,s in h.items() if z not in h[r]|{r}):continue
                key=(u,v,tuple(a),tuple(b),tuple(c),tuple((x,y) for x,y in combinations(sorted(set(g)-{u,v}),2) if y in g[x]))
                if key in seen:continue
                seen.add(key);entries.append(dict(record=i,word=w,u=u,v=v,A=a,B=b,C=c,cycle=sorted(cy)));print(i,u,v,flush=True)
                if len(entries)==10:break
            if len(entries)==10:break
    prev.save(P,dict(protocol=protocol,cases=entries));print('frozen',prev.sha(P.read_bytes()))
elif __name__=='__main__' and sys.argv[1]=='compare':
    data=json.loads(P.read_text());assert data['protocol']==protocol;results=[]
    for e in data['cases']:
        g=graph(e['word']);u,v=e['u'],e['v'];hs=[make(g,u,v,e['A'],b) for b in (e['B'],e['C'])];z={}
        for r in (u,v):
            common=set.intersection(*(eligible(h,r) for h in hs));certs=[shell_scan(h,r) for h in hs];wins=[{row[0] for row in cs if len(row)==1}&common for cs in certs];z[r]=dict(gain=sorted(wins[1]-wins[0]),loss=sorted(wins[0]-wins[1]),all_exposed=[() in cs for cs in certs],certs=[{str(list(q)):o for q,o in cs.items()} for cs in certs]);
        success=bool(z[u]['gain'] and z[v]['loss']);print(e['record'],u,v,[(z[r]['gain'],z[r]['loss']) for r in (u,v)],success,flush=True);results.append(dict(ends=z,success=success))
    prev.save(R,dict(frozen_sha=prev.sha(P.read_bytes()),results=results))
