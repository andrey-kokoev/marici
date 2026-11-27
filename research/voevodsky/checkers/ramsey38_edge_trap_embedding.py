"""Try to realize the five-cell interior-edge trap on actual marked arrays, allowing any labeling."""
from ramsey38_trap_markability import view,prev,graph,json,gzip,setup,add,permutations
from ramsey38_disk_filter_trial import key
from collections import Counter

def run():
    trap,=json.loads((prev.out/'ramsey38_interior_edge_trap_census.json').read_text())['traps'];mask=lambda s:sum(1<<x for x in s);A,bd=view(set(map(frozenset,trap['start'])));B,end=view(set(map(frozenset,trap['end'])));encode=lambda s:{mask(f) for f in s}|{0};A,bd,B,end=map(encode,(A,bd,B,end));edge,=[s for s in A-bd if s.bit_count()==2];maps={}
    for p in permutations(range(7)):
        tr=bytes(sum(1<<p[j] for j in range(7) if m>>j&1) for m in range(128));pre=tr.index(edge);maps.setdefault(pre,[]).append(tr)
    seen=set();cnt=Counter();cert=[]
    with gzip.open(prev.catalogue,'rt') as fp:
        for i,line in enumerate(fp,1):
            if i<257404:continue
            if i>260000:break
            w=line.strip();g=graph(w)
            for u in g:
                if len(g[u])!=7:continue
                L,r,ms=setup(g,u)
                if len(ms)<2 or max(map(int.bit_count,r.values()))>4:continue
                scripts={a:setup(add(g,a),u)[2] for a in ms};scripts={a:bs for a,bs in scripts.items() if bs};k=key(L,r,ms)
                if not scripts or k in seen:continue
                seen.add(k);cnt['arrays']+=1
                for a,bs in scripts.items():
                    x,v=a;r1={**r,x:r[x]|1<<L.index(v)}
                    for s in {s for s in r1.values() if s.bit_count()==2 and list(r1.values()).count(s)==1}:
                        j=next(j for j,t in r1.items() if t==s)
                        for tr in maps[s]:
                            if tr[r[x]] in bd or any(tr[t] not in A or (z!=j and t.bit_count()<4 and tr[t] not in bd) for z,t in r1.items()):continue
                            cnt['valid_first']+=1
                            for y,b in bs:
                                r2={**r1,y:r1[y]|1<<L.index(b)}
                                if tr[r1[y]] in end or tr[r[x]] in end or any(tr[t] not in B for t in r2.values()):continue
                                hidden=[z for z,t in r2.items() if t.bit_count()<4 and tr[t] not in end]
                                if len(hidden)==2 and j in hidden and all(r2[z].bit_count()==2 for z in hidden):cert.append(dict(record=i,root=u,moves=[a,[y,b]],labels=L,image=[tr[1<<n].bit_length()-1 for n in range(7)],hidden=hidden))
    print(cnt,len(cert));prev.save(prev.out/'ramsey38_edge_trap_embedding.json',dict(range=[257404,260000],counts=dict(cnt),certificates=cert))
if __name__=='__main__':run()
