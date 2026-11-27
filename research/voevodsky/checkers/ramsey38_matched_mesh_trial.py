"""Prospective tip commitment, singleton-star assembly and independent all-route census."""
from ramsey38_append_holdout import freeze,P as old,sys,prev,json,attaches,graph,setup,add,faces,finals,shelling,face_assignments,Counter
from ramsey38_tip_disk_domains import disks,propagate
from ramsey38_two_move_trial import options
from ramsey38_append_531_routes import extend
P=prev.out/'ramsey38_matched_mesh_predictions.json';R=prev.out/'ramsey38_matched_mesh_comparison.json'
protocol='First five novel eligible arrays after 531, all ordered pairs. Use only one/two-cell collars and all-boundary labels. First final-disk pass commits tip AND both shells/edits/collar. Initial stars must match final stars under adding exactly collar. Propagate shared cells, propose mesh only if all domains singleton and collar attaches in order. No fallback. Separate exhaustive all-shell and arbitrary-length extension census.'
def select(e,L,rs,candidates):
    dec=lambda m:frozenset(v for i,v in enumerate(L) if m>>i&1);res=dict(pick=None,commit=None)
    for _,a,bd,w,n,end,collar in candidates:
        x,v=a;y,t=n;r1={**rs,x:rs[x]|1<<L.index(v)};r2={**r1,y:rs[y]|1<<L.index(t)};need=dec(rs[x])|{w};B=set(map(dec,bd));F=set(map(dec,end));E=set(map(frozenset,collar));
        if set.union(set(),*B)!=set.union(set(),*F) or set.union(set(),*B)!=set(L):continue
        D={i:disks(L,i,F,set(map(dec,r2.values()))|E|{need}) for i in L}
        if not all(propagate(D)[0][-1].values()):continue
        res['commit']=dict(first=a,second=n,bd=bd,end=end,tip=w,collar=collar);Q={i:[s for s in disks(L,i,B,set(map(dec,r1.values()))|{need}) if not E&s and s|{t for t in E if i in t} in D[i]] for i in L}
        while all(Q.values()):
            N={i:[s for s in Q[i] if all(any({t for t in s if j in t}=={t for t in h if i in t} for h in Q[j]) for j in L if j!=i)] for i in L}
            if N==Q:break
            Q=N
        res['sizes']={i:len(q) for i,q in Q.items()}
        if all(len(q)==1 for q in Q.values()):
            mesh=set.union(set(),*(q[0] for q in Q.values()));seq=list(map(frozenset,collar))
            for o in (seq,seq[::-1]):
                if all(attaches(mesh|set(o[:i]),c) for i,c in enumerate(o)):res['pick']=dict(mesh=faces(mesh),append=[sorted(t) for t in o]);break
        break
    return res

def compare(predictions=P,destination=R):
    cnt=Counter();out=[]
    for e in json.loads(predictions.read_text())['cases']:
        g=graph(e['word']);L,rs,moves=setup(g,e['u']);dec=lambda m:frozenset(v for i,v in enumerate(L) if m>>i&1);f=finals(e,True);cache={}
        def balls(bd,req):
            k=(tuple(bd),frozenset(req))
            if k not in cache:cache[k]=[frozenset(ts) for ts in face_assignments(L,req,set(map(dec,bd))) if shelling(ts)]
            return cache[k]
        first={j:options(L,rs,moves,j,True) for j in {d['j'] for d in e['requests']}};local=Counter()
        for d in e['requests']:
            j,l=d['j'],d['l'];q=d['commit'];pick=d['pick'];routes=0;commit_ok=False;mesh_ok=False;example=None
            for (a,b),zs in f.items():
                ends=[z for z in zs if z['hidden']==sorted((j,l))];
                if not ends:continue
                x,v=a;y,t=b;r1={**rs,x:rs[x]|1<<L.index(v)};r2={**r1,y:rs[y]|1<<L.index(t)}
                for h in first[j]:
                    if h['edge']!=list(a):continue
                    for w in h['tips']:
                        for A in balls(h['bd'],set(map(dec,r1.values()))|{dec(rs[x])|{w}}):
                            for z in ends:
                                for B in balls(z['bd'],set(map(dec,r2.values()))):
                                    o=extend(A,B)
                                    if o is None:continue
                                    routes+=1;example=example or dict(first=a,second=b,tip=w,initial=faces(A),append=[sorted(t) for t in o]);
                                    if q and (q['first'],q['second'],q['bd'],q['end'],q['tip'],q['collar'])==(list(a),list(b),h['bd'],z['bd'],w,faces(B-A)):
                                        commit_ok=True
                                        if pick and faces(A)==pick['mesh']:
                                            s=list(map(frozenset,pick['append']));mesh_ok=set(s)==B-A and all(attaches(A|set(s[:i]),t) for i,t in enumerate(s))
            for k,v in dict(requests=1,feasible=bool(routes),routes=routes,commits=bool(q),commit_ok=commit_ok,proposals=bool(pick),mesh_ok=mesh_ok).items():local[k]+=v
            out.append(dict(record=e['record'],root=e['u'],j=j,l=l,routes=routes,commit_ok=commit_ok,mesh_ok=mesh_ok,example=example))
        print(e['record'],local,flush=True);cnt.update(local)
    print(cnt);prev.save(destination,dict(prediction_sha=prev.sha(predictions.read_bytes()),counts=dict(cnt),results=out))
if __name__=='__main__':
    if sys.argv[1]=='freeze':freeze(531,(old,),select,P,protocol)
    elif sys.argv[1]=='compare':compare()
