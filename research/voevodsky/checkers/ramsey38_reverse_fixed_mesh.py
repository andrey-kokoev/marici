"""Independent backward peel: enumerate endpoint balls, do not seed with forward meshes."""
from ramsey38_one_pin_holdout import P,prev,json
from ramsey38_middle_choice_holdout import graph,setup,add,face_assignments,shelling,faces,boundary
from itertools import combinations

def run():
    audit=json.loads((prev.out/'ramsey38_mesh_equivariance_audit.json').read_text());out=[]
    for z in audit['cases']:
        e=next(e for e in json.loads(P.read_text())['cases'] if e['record']==z['record']);j,l=z['targets'];c=next(d['commit'] for d in e['requests'] if (d['j'],d['l'])==(j,l));g=graph(e['word']);u=e['u'];L,rs,_=setup(g,u);dec=lambda m:frozenset(w for i,w in enumerate(L) if m>>i&1);a,b=c['first'];h=add(g,c['first']);req1=set(map(dec,setup(h,u)[1].values()))|{dec(rs[a])|{c['tip']}};req2=set(map(dec,setup(add(h,c['second']),u)[1].values()));bd=set(map(dec,c['bd']));end=set(map(dec,c['end']));E=frozenset(map(frozenset,c['collar']));
        # Inverse attachment criterion: exposed and shared facets form complementary disks,
        # and removing the cell does not leave an isolated edge or vertex of intersection.
        def peelable(B,t):
            A=B-{t};internal=[f for f in map(frozenset,combinations(t,3)) if any(f<=s for s in A)]
            return 1<=len(internal)<=3 and all(any((s&t)<=f for f in internal) for s in A)
        terminals=[];reverse=set();counts=dict(final_balls=0,with_collar=0,with_prefix_supports=0);forward={frozenset(map(frozenset,ts)) for ts in z['meshes'].values()}
        for ts in face_assignments(L,req2,end):
            B=frozenset(ts)
            if not shelling(B):continue
            counts['final_balls']+=1
            if not E<=B:continue
            counts['with_collar']+=1
            if not all(any(s<=t for t in B-E) for s in req1):continue
            counts['with_prefix_supports']+=1;paths=[];stuck=[]
            def walk(now,left,path):
                if not left:
                    if boundary(now)==bd and shelling(now):paths.append(path);reverse.add(now)
                    return
                for t in sorted(left,key=sorted):
                    if peelable(now,t):walk(now-{t},left-{t},path+[sorted(t)])
                    else:stuck.append(path+[sorted(t)])
            walk(B,E,[]);terminals.append(dict(final_cells=faces(B),start_cells=faces(B-E),peel_orders=paths,blocked_prefixes=stuck))
        starts={frozenset(ts) for ts in face_assignments(L,req1,bd) if shelling(ts)};assert reverse<=starts;res=dict(record=z['record'],root=u,counts=counts,all_start_balls=len(starts),recovered=len(reverse),only_forward=[faces(m) for m in forward-reverse],only_reverse=[faces(m) for m in reverse-forward],terminals=terminals);out.append(res);print(z['record'],counts,len(starts),len(reverse),len(forward-reverse),len(reverse-forward),[(r['peel_orders'],r['blocked_prefixes']) for r in terminals])
    prev.save(prev.out/'ramsey38_reverse_fixed_mesh.json',dict(forward_sha=prev.sha((prev.out/'ramsey38_mesh_equivariance_audit.json').read_bytes()),cases=out))
if __name__=='__main__':run()
