"""Diagnose every false edge-and-face pass by the full monotone attachment frontier."""
from ramsey38_target_edge_closure import P,prev,json,graph,setup,add,boundary,combinations,Counter
from ramsey38_append_holdout import attaches,faces

def run():
    audit=json.loads((prev.out/'ramsey38_target_edge_and_face_closure.json').read_text());it=iter(audit['results']);out=[]
    for entry in json.loads(P.read_text())['cases']:
        L=sorted(graph(entry['word'])[entry['u']]);dec=lambda m:frozenset(w for i,w in enumerate(L) if m>>i&1);cells=list(map(frozenset,combinations(L,4)))
        for d in entry['requests']:
            a=next(it);assert (entry['record'],d['moves'],d['goal'])==(a['record'],a['moves'],a['goal']);g=graph(entry['word']);old=[]
            for x,v in d['moves']:
                _,rs,_=setup(g,entry['u']);old.append(dec(rs[x]));g=add(g,(x,v))
            _,rs,_=setup(g,entry['u']);req=set(map(dec,rs.values()));S={j:dec(s) for j,s in rs.items() if s.bit_count()<4};goal=set(d['goal']);edge=S[d['goal'][-1]]
            for i in sorted(set(a['joint'])-set(a['actual'])):
                M=frozenset(map(frozenset,d['pool'][i]));nodes=[]
                def visit(B,path):
                    bd=boundary(B);hidden={j for j,s in S.items() if not any(s<=f for f in bd)};assert hidden<=goal and not(hidden==goal and not set(old)&bd and all(any(s<=t for t in B) for s in req));options=[];safe=[]
                    for t in cells:
                        if t in B or not attaches(B,t):continue
                        nb=boundary(B|{t});lost=sorted(j for j,s in S.items() if j not in goal and not any(s<=f for f in nb));options.append(dict(cell=sorted(t),lost=lost))
                        if not lost:safe.append(t)
                    nodes.append(dict(path=path,hidden=sorted(hidden),options=options));
                    for t in safe:visit(B|{t},path+[sorted(t)])
                visit(M,[]);maxdepth=max(len(n['path']) for n in nodes);summary=[(n['path'],len(n['options']),sum(not o['lost'] for o in n['options'])) for n in nodes];print(entry['record'],i,maxdepth,summary);out.append(dict(record=entry['record'],moves=d['moves'],goal=d['goal'],pool=i,edge=sorted(edge),maxdepth=maxdepth,nodes=nodes))
    assert len(out)==6;prev.save(prev.out/'ramsey38_false_mesh_frontiers.json',dict(cases=out))
if __name__=='__main__':run()
