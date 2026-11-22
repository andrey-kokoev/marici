"""Given four shared flags, remove their eight vertices. On the remaining graph test whether a single 22-cycle reflected at 0,29 can use every vertex. Record degree obstructions and forced edges at degree two, before any strip search."""
from ramsey_row_quotient_constructor import R,flags
from ramsey_folded_entry_handoff import D,json

def check(extra):
    removed={x for e in list(extra)+[(9,26),(14,15)] for x in e};adj={x:set() for x in set(range(30))-removed}
    for x,y in flags:
        if x in adj and y in adj:adj[x].add(y);adj[y].add(x)
    forced={x:{y for y in adj[x] if len(adj[x])==2 or len(adj[y])==2} for x in adj};over={x:sorted(s) for x,s in forced.items() if len(s)>2};paths=[]
    def dfs(w,used):
        if len(w)==12:
            if w[-1]==29 and w[1]<R[w[1]] and len(used)==22:paths.append(w)
            return
        for y in sorted(adj[w[-1]]-used):
            if (y==29)==(len(w)==11):dfs(w+[y],used|{y,R[y]})
    dfs([0],{0});live={x:set(s) for x,s in adj.items()};rounds=[]
    while all(len(s)>=2 for s in live.values()):
        cuts=set()
        for x,s in live.items():
            must={y for y in s if len(live[y])==2}
            if len(must)==2:cuts.update(tuple(sorted((x,y))) for y in s-must)
        if not cuts:break
        rounds.append(len(cuts))
        for x,y in cuts:live[x].remove(y);live[y].remove(x)
    return dict(pruning=rounds,unresolved=[x for x,s in live.items() if len(s)>2],extra=sorted(extra),degree_low={x:sorted(s) for x,s in adj.items() if len(s)<2},forced_overload=over,paths=paths)

def run():
    data=json.loads((D/'ramsey_selfdual_fill_obstruction.json').read_text());out=[]
    for k,blocks in data['common_owner_orbits'].items():
        for i,block in enumerate(blocks):
            todo=set(map(tuple,block));
            while todo:
                x=min(todo);u={x,tuple(R[z] for z in x)};todo-=u;out.append(dict(short_fork=k,block=i,**check(u)))
    return out
if __name__=='__main__':
    out=run();print(out);(D/'ramsey_long_residual_inverse.json').write_text(json.dumps(out)+'\n')
