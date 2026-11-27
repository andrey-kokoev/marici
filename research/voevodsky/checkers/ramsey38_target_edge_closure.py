"""Enumerate just the missing path around the target edge; never choose a whole final shell."""
from ramsey38_middle_depth_ablation import P,R,prev,json,graph,setup,add,boundary,Counter
from itertools import combinations,permutations

def fan_paths(L,M,e,sealed):
    seg=[t-e for t in M if e<=t];deg=Counter(v for s in seg for v in s);a,b=sorted(v for v,n in deg.items() if n==1);unused=sorted(set(L)-set(e)-set(deg)-sealed)
    for k in range(len(unused)+1):
        for inter in permutations(unused,k):
            walk=(a,*inter,b);extra=frozenset(e|{x,y} for x,y in zip(walk,walk[1:]))
            if not any(t in M or t&sealed for t in extra):yield walk,extra

def fit(M,E,req,protected):
    # Include other compulsory tetrahedra even when not part of this edge fan.
    U=M|E|{s for s in req if len(s)==4};fac=Counter(frozenset(f) for t in U for f in combinations(t,3))
    if max(fac.values())>2:return False
    # A closed component of any edge link cannot have another component; a
    # closed link also forces that edge and every incident triangle off the rim.
    for e in {frozenset(e) for t in U for e in combinations(t,2)}:
        seg=[s-e for s in U if e<=s];left=set.union(set(),*seg)
        while left:
            component={min(left)}
            for _ in seg:
                for h in seg:
                    if component&h:component.update(h)
            deg=Counter(v for h in seg if h&component for v in h)
            if all(n==2 for n in deg.values()) and (len(deg)!=len(set.union(set(),*seg)) or any(e<=r for r in protected)):return False
            left-=component
    return all(any(s<=f and n==1 for f,n in fac.items()) for s in protected)

def run():
    truth=json.loads(R.read_text());it=iter(truth['results']);cnt=Counter();out=[]
    for entry in json.loads(P.read_text())['cases']:
        L=sorted(graph(entry['word'])[entry['u']]);dec=lambda m:frozenset(x for i,x in enumerate(L) if m>>i&1)
        for d in entry['requests']:
            z=next(it);assert z['goal']==d['goal'] and z['moves']==d['moves'] and z['record']==entry['record'];g=graph(entry['word']);old=[]
            for x,v in d['moves']:
                _,rs,_=setup(g,entry['u']);old.append(dec(rs[x]));g=add(g,(x,v))
            _,rs,_=setup(g,entry['u']);req=set(map(dec,rs.values()));protected={dec(s) for j,s in rs.items() if s.bit_count()<4 and j not in d['goal']};e=dec(rs[d['goal'][-1]]);assert len(e)==2;local=[];joined=[]
            for cells in d['pool']:
                M=frozenset(map(frozenset,cells));sealed=set(L)-set.union(set(),*boundary(M));paths=[];joint=[]
                if all(any(s<=t for t in M) for s in req if s&sealed):
                    for walk,E in fan_paths(L,M,e,sealed):
                        if not fit(M,E,req,protected):continue
                        paths.append(walk);U=M|E|{s for s in req if len(s)==4};triangle=old[-1];incident=[s for s in U if triangle<=s]
                        if len(incident)==2:joint.append(walk)
                        elif len(incident)==1 and any(t not in U and not t&sealed and fit(M,E|{t},req,protected) for v in set(L)-triangle for t in [triangle|{v}]):joint.append(walk)
                local.append(paths);joined.append(joint)
            passed=[i for i,p in enumerate(local) if p];actual=z['ok'];assert set(actual)<=set(passed);cnt['requests']+=1;cnt['exact']+=passed==actual;cnt['proposed']+=bool(passed);cnt['hit']+=bool(passed and passed[0] in actual);cnt['extra_meshes']+=len(passed)-len(actual);cnt['true_meshes']+=len(actual);jp=[i for i,p in enumerate(joined) if p];assert set(actual)<=set(jp);cnt['joint_exact']+=jp==actual;cnt['joint_extra']+=len(jp)-len(actual);cnt['joint_proposed']+=bool(jp);cnt['joint_hit']+=bool(jp and jp[0] in actual);out.append(dict(record=entry['record'],goal=d['goal'],moves=d['moves'],edge=sorted(e),passed=passed,joint=jp,actual=actual,paths=local))
            if entry['record']==72703 and actual:print(d['goal'],sorted(e),passed,actual,[local[i] for i in actual])
    print(cnt);prev.save(prev.out/'ramsey38_target_edge_and_face_closure.json',dict(counts=dict(cnt),results=out))
if __name__=='__main__':run()
