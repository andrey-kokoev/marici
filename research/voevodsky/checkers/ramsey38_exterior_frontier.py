"""Can a reachable middle ball make even one irreversible, target-compatible attachment?"""
from ramsey38_early_interior_holdout import P,prev,json,setup,graph,add,faces
from ramsey38_append_holdout import attaches,boundary,combinations
from collections import Counter

def run():
    audit=json.loads((prev.out/'ramsey38_sealed_star_transitions.json').read_text());e=next(e for e in json.loads(P.read_text())['cases'] if e['record']==audit['record']);g=graph(e['word']);u=e['u'];v=audit['buried'];goal=audit['goal'];
    old_triangles=[]
    for x,y in audit['moves']:
        labs,rows,_=setup(g,u);old_triangles.append(frozenset(a for i,a in enumerate(labs) if rows[x]>>i&1));g=add(g,(x,y))
    L,rs,_=setup(g,u);dec=lambda m:frozenset(x for i,x in enumerate(L) if m>>i&1);exposed={j:dec(s) for j,s in rs.items() if s.bit_count()<4 and j not in goal};late=frozenset(audit['late_tet']);ts=set(map(frozenset,combinations(L,4)));out=[]
    def traverse(M,path):
        bd=boundary(M);hidden=sorted(j for j,s in rs.items() if s.bit_count()<4 and not any(dec(s)<=f for f in bd));success=hidden==sorted(goal) and all(f not in bd for f in old_triangles) and all(any(dec(s)<=t for t in M) for s in rs.values());nodes=[dict(path=path,hidden=hidden,success=success)]
        if success:return nodes
        for t in sorted(ts-M,key=sorted):
            if v in t or not attaches(M,t):continue
            new=M|{t};newbd=boundary(new)
            if all(any(s<=f for f in newbd) for s in exposed.values()):nodes.extend(traverse(new,path+[sorted(t)]))
        return nodes
    for d in audit['middle']:
        M=frozenset(map(frozenset,d['mesh']));assert all(any(s<=f for f in boundary(M)) for s in exposed.values());steps=[]
        if late in M:
            for t in sorted(ts-M,key=sorted):
                if v in t or not attaches(M,t):continue
                bd=boundary(M|{t});lost=sorted(j for j,s in exposed.items() if not any(s<=f for f in bd));steps.append(dict(cell=sorted(t),lost=lost))
        nodes=traverse(M,[]) if late in M else [];assert any(n['success'] for n in nodes)==bool(d['post']);out.append(dict(mesh=d['mesh'],sealed_ok=late in M,steps=steps,nodes=nodes,continues=bool(d['post'])));
        if late in M:print('continues',d['post'],'nodes',nodes)
    prev.save(prev.out/'ramsey38_exterior_frontier_paths.json',dict(record=e['record'],goal=goal,protected_rows={j:sorted(s) for j,s in exposed.items()},cases=out))
if __name__=='__main__':run()
