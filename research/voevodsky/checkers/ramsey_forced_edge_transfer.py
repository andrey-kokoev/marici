from ramsey_paired_decoder_transfer import *
from ramsey_five_port_multi import sevens
import sys
proto=D.parent/'ramsey_forced_edge_transfer_protocol.md';C=D.parent/'ramsey_forced_edge_candidates.json';R=D.parent/'ramsey_forced_edge_transfer.json'
def freeze():
    fs=[]
    for ss,es in islice(family(),128,256):
        S=grow(ss,1);inside=lambda m:{e for e in es if all(m>>i&1 for i in ports[e])};forced={};a=graph(9,S,0)
        for q in sevens(a):
            t=inside(sum(1<<(j-9) for j in q if j>=9))
            if len(t)==1:forced.setdefault(next(iter(t)),q)
        F=set(forced);by={e:[set(),set()] for e in es}
        for g,v in [(0,0),(9,8)]:
            ts=terms(S,g)
            for h in range(32):
                if any(v in s for i,s in enumerate(S) if h>>i&1):continue
                E=inside(h)
                for n,f in enumerate([set(),F]):
                    if E&f:continue
                    miss=[inside(t) for t in ts if not h&t and not (inside(t)&f)]
                    if len(E)==1 and not miss:by[next(iter(E))][n].add((g,h,'B'))
                    if not E and miss:
                        for e in set.intersection(*miss):
                            if {e} in miss:by[e][n].add((g,h,'R'))
        fs.append(dict(rows=ss,eligible=es,forced=forced,targets=[(k,p,e,sorted(by[e][0]),sorted(by[e][1])) for k in range(1,9) for p in terms(S,k) if len(inside(p))==1 for e in inside(p)]))
    assert len(fs)==128;return dict(protocol_sha=sha256(proto.read_bytes()).hexdigest(),families=fs)
def test():
    z=json.loads(C.read_text());assert z['protocol_sha']==sha256(proto.read_bytes()).hexdigest();st=Counter();example=None
    for f in z['families']:
        S=grow(f['rows'],1);es=f['eligible'];states=[c for m in range(1<<len(es)) if verdict(graph(9,S,c:=sum(1<<e for j,e in enumerate(es) if m>>j&1)))];assert all(c>>int(e)&1 for e in f['forced'] for c in states);cache={};tc={};improved=False;st['parents']+=len(states);st['legal_families']+=bool(states)
        for k,p,e,old,new in f['targets']:
            var=len({c>>e&1 for c in states})==2;st['targets']+=1;st['variable']+=var
            if var:
                assert set(map(tuple,old))<=set(map(tuple,new));st['old']+=bool(old);st['augmented']+=bool(new);st['additional_target_probe_pairs']+=len(new)-len(old)
                if new and not old:
                    improved=True
                    if example is None:example=dict(rows=f['rows'],target=[k,p,e],new=new,forced=f['forced'])
            for c in states:
                if not new:continue
                if (c,k) not in tc:
                    a=graph(9,S,c);raw={sum(1<<(j-9) for j in q if j>=9) for q in combinations(sorted(set(range(14))-{k-1,k}),6) if all(not a[i]>>j&1 for i,j in combinations(q,2))};tc[c,k]={m for m in raw if not any(t!=m and t&m==t for t in raw)}
                present=p in tc[c,k];assert present==(not(c>>e&1))
                for g,h,mode in new:
                    if (c,g,h) not in cache:cache[c,g,h]=verdict(build({g:tuple(i+1 for i in range(5) if h>>i&1)},S,c))
                    assert cache[c,g,h]==(present if mode=='B' else not present);st['checks']+=1
        st['families_gained']+=improved
    out=dict(candidate_sha=sha256(C.read_bytes()).hexdigest(),counts=st,example=example);print(out);save(R,out)
if __name__=='__main__':
    if sys.argv[1]=='freeze':save(C,freeze())
    else:test()
