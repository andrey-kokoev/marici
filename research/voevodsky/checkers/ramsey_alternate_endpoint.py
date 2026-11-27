from ramsey_paired_decoder_transfer import *
from collections import defaultdict
import sys
proto=D.parent/'ramsey_alternate_endpoint_protocol.md';C=D.parent/'ramsey_alternate_endpoint_candidates.json';O=D.parent/'ramsey_alternate_endpoint_results.json'

def generate():
    rows=[]
    for ss,es in islice(family(),128):
        S=grow(ss,1);inside=lambda m:{e for e in es if all(m>>i&1 for i in ports[e])};probes=defaultdict(list)
        for g,v in [(0,0),(9,8)]:
            T=terms(S,g)
            for h in range(32):
                if any(v in s for i,s in enumerate(S) if h>>i&1):continue
                E=inside(h);miss=[inside(q) for q in T if not h&q];
                if not miss and len(E)==1:probes[next(iter(E))].append((g,h,'B'))
                if not E and miss:
                    for e in set.intersection(*miss):
                        if {e} in miss:probes[e].append((g,h,'R'))
        targets=[(k,p,e,probes[e]) for k in range(1,9) for p in terms(S,k) if len(inside(p))==1 for e in inside(p)];rows.append(dict(rows=ss,eligible=es,targets=targets))
    return dict(protocol_sha=sha256(proto.read_bytes()).hexdigest(),families=rows)

def score(fs):
    st=Counter();ex=None
    for f in fs:
        S=grow(f['rows'],1);es=f['eligible'];states=[c for m in range(1<<len(es)) if verdict(graph(9,S,c:=sum(1<<e for j,e in enumerate(es) if m>>j&1)))];st['usable_families']+=bool(states);st['parents']+=len(states);active=False;cache={};tc={}
        for k,p,e,ps in f['targets']:
            st['targets']+=1;var=len({c>>e&1 for c in states})==2;st['variable']+=var
            if var and ps:
                base=any(h==p and mode=='B' for g,h,mode in ps);st['direct']+=base;st['new']+=not base;active|=not base
                if not base:
                    modes=''.join(sorted({mode for _,_,mode in ps}));st['new_'+modes]+=1
                    if ex is None:ex=dict(rows=f['rows'],target=[k,p,e],probe=ps[0])
            for c in states:
                if not ps:continue
                if (c,k) not in tc:
                    a=graph(9,S,c);terms0={sum(1<<(i-9) for i in q if i>=9) for q in combinations(sorted(set(range(14))-{k-1,k}),6) if all(not a[i]>>j&1 for i,j in combinations(q,2))};tc[c,k]={q for q in terms0 if not any(t!=q and t&q==t for t in terms0)}
                present=p in tc[c,k];assert present==(not(c>>e&1))
                for g,h,mode in ps:
                    if (c,g,h) not in cache:cache[c,g,h]=verdict(build({g:tuple(i+1 for i in range(5) if h>>i&1)},S,c))
                    assert cache[c,g,h]==(present if mode=='B' else not present);st['checks']+=1
        st['new_families']+=active
    return dict(counts=dict(st),example=ex)
if __name__=='__main__':
    if sys.argv[1]=='freeze':save(C,generate())
    else:
        data=json.loads(C.read_text());assert data['protocol_sha']==sha256(proto.read_bytes()).hexdigest();fs=data['families'];assert len(fs)==128;out=dict(candidate_sha=sha256(C.read_bytes()).hexdigest(),old=score(fs[:64]),fresh=score(fs[64:]));print(out);save(O,out)
