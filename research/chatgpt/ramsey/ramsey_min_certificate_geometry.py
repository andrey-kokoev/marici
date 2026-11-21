"""Enumerate all size-three post-pair certificates by branching on a least-covered surviving quartet."""
from ramsey_integral_obstruction import classify,D,json,attach,bits,Counter
from collections import defaultdict
from itertools import product

def run():
    p=json.loads((D/'ramsey_pure_port_fork.json').read_text());H=attach(p['stem_graphs'][-1],p['alternate']['to34']);old=json.loads((D/'ramsey_reuse_stress.json').read_text())['35']['old'];r=classify(H,10,old,True);by=defaultdict(list)
    for s,m in r['row_masks'].items():by[m].append(s)
    n=r['number_quads'];full=(1<<n)-1;options=[[] for _ in range(n)]
    for m in by:
        for i in bits(m):options[i].append(m)
    order=sorted(range(n),key=lambda i:len(options[i]));sol=set()
    def dfs(U,path):
        if not U:assert len(path)==3;sol.add(tuple(sorted(path)));return
        i=next(i for i in order if U>>i&1)
        for m in options[i]:
            rest=U&~m
            if len(path)<2 or not rest:dfs(rest,path+[m])
    dfs(full,[]);counts=Counter();verts=Counter();freq=Counter();local=Counter();ends=(1<<10)|(1<<26);examples={};families=[]
    for x in sorted(sol):
        for a,b,c in product(*(by[m] for m in x)):
            S=(a,b,c);common=a&b&c;key=(tuple(sorted(s.bit_count() for s in S)),tuple(sorted((s&ends).bit_count() for s in S)),common.bit_count());counts[key]+=1;verts.update(bits(common));freq.update(S);examples.setdefault(str(key),[list(bits(s)) for s in S]);families.append(S)
    pairs=[(u,v) for u,s in enumerate(H) for v,t in enumerate(H) if s.bit_count()==t.bit_count()==7 and s>>10&1 and t>>26&1 and not s&t];diagnostics={}
    for u,v in pairs:
        m=r['row_masks'].get(H[u],0)&r['row_masks'].get(H[v],0);diagnostics[f'{u},{v}']=m.bit_count()
    print('double violations by local pair',diagnostics);out={'double_violations':diagnostics,'row_triples':len(families),'distinct_coverage_triples':len(sol),'signature':{str(k):v for k,v in counts.items()},'common_vertices':dict(verts),'row_frequency':freq.most_common(),'examples':examples,'families':families};print('row triples',len(families),'coverage triples',len(sol),'signature',counts,'common vertices',verts,'rows',len(freq));return out
if __name__=='__main__':(D/'ramsey_min_certificate_geometry.json').write_text(json.dumps(run())+'\n')
