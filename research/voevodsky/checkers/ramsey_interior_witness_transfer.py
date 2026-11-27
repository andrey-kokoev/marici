from ramsey_paired_decoder_transfer import *
from ramsey_five_port_multi import sevens
from collections import defaultdict
import sys
P0=D.parent/'ramsey_interior_witness_protocol.md';C=D.parent/'ramsey_interior_witness_candidates.json';R=D.parent/'ramsey_interior_witness_transfer.json'
def derive(ss,es):
    S=grow(ss,1);g=graph(9,S,0);V=set(range(14));ec=lambda q:sum(1<<e for e in es if all(i+9 in q for i in ports[e]));parent={ec(q) for q in sevens(g)};obs={};sources={}
    for j in range(1,9):
        f={j-1,j};rest=V-f;records={}
        for typ,n,pool in [('X',6,rest),('E',5,{i for i in rest if all(not(g[i]>>v&1) for v in f)})]:
            for q in combinations(sorted(pool),n):
                if all(not(g[x]>>y&1) for x,y in combinations(q,2)):
                    m=ec(q);records.setdefault((typ,m),q)
        residual={m for _,m in records if not any(t&m==t for t in parent)};w=next((m for m in residual if m.bit_count()==1 and all(t&m for t in residual)),None)
        if w:
            e=w.bit_length()-1;obs[j]=[e,''.join(t for t in ('X','E') if (t,w) in records)];sources[j]=[dict(kind=t,mask=m,old_sites=[v+1 for v in q if v<9],ports=[v-8 for v in q if v>=9],redundant=m not in residual) for (t,m),q in sorted(records.items())]
    targets=[]
    for k in range(1,9):
        for p in terms(S,k):
            E=[e for e in es if all(p>>i&1 for i in ports[e])];
            if len(E)==1:targets.append([k,p,E[0],[(j,t) for j,(e,t) in obs.items() if j!=k and e==E[0]]])
    return dict(rows=ss,eligible=es,targets=targets),sources

def freeze():
    source,ws=derive(*next(islice(family(),133,None)));return dict(protocol_sha=sha256(P0.read_bytes()).hexdigest(),family134_at_gap4=ws[4],families=[derive(ss,es)[0] for ss,es in islice(family(),256,320)])

def run():
    z=json.loads(C.read_text());assert z['protocol_sha']==sha256(P0.read_bytes()).hexdigest();st=Counter();types=Counter()
    for f in z['families']:
        S=grow(f['rows'],1);es=f['eligible'];states=[c for m in range(1<<len(es)) if verdict(graph(9,S,c:=sum(1<<e for j,e in enumerate(es) if m>>j&1)))];st['legal_parents']+=len(states);active=False;cache={};tc={}
        for k,p,e,ps in f['targets']:
            var=len({c>>e&1 for c in states})==2;st['variable']+=var
            if ps and var:active=True;st['read_variable']+=1;types['/'.join(sorted({t for _,t in ps}))]+=1
            for c in states if ps else []:
                if (k,c) not in tc:
                    a=graph(9,S,c);r={sum(1<<(v-9) for v in q if v>=9) for q in combinations(sorted(set(range(14))-{k-1,k}),6) if all(not(a[x]>>y&1) for x,y in combinations(q,2))};tc[k,c]={s for s in r if not any(t!=s and t&s==t for t in r)}
                for j,_ in ps:
                    if (j,c) not in cache:cache[j,c]=verdict(build({j:()},S,c))
                    assert cache[j,c]==(p not in tc[k,c])==bool(c>>e&1);st['checks']+=1
        st['active_families']+=active
    out=dict(candidate_sha=sha256(C.read_bytes()).hexdigest(),counts=st,types=types);print(z['family134_at_gap4'],out);save(R,out)
if __name__=='__main__':
    if sys.argv[1]=='freeze':save(C,freeze())
    else:run()
