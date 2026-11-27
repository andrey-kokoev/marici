"""No final shell or move order: cone just the protected supports to an outside label."""
from ramsey38_target_edge_closure import P,prev,json,graph,setup,add,boundary,fan_paths,fit,Counter,combinations
from ramsey38_root15_link_rotation import link_domains
from ramsey38_shared_twist10 import faces

def planar(fs):
    fs=frozenset(f for f in fs if len(f)>=2);return not fs or bool(link_domains(fs))

def witness(U,prot,L):
    best=None
    for v in L:
        base={t-{v} for t in U if v in t};by={j:(t|{0})-{v} for j,t in prot.items() if v in t and len(t)>=2}
        if planar(base|set(by.values())):continue
        for k in range(min(len(by),len(best['rows'])-1 if best else len(by))+1):
            found=next((q for q in combinations(sorted(by),k) if not planar(base|{by[j] for j in q})),None)
            if found is not None:best=dict(vertex=v,rows=list(found),links=faces(base|{by[j] for j in found}));break
        if best is not None and not best['rows']:break
    return best

def run():
    prior=json.loads((prev.out/'ramsey38_target_edge_and_face_closure.json').read_text());it=iter(prior['results']);out=[];cnt=Counter()
    for e in json.loads(P.read_text())['cases']:
        L=sorted(graph(e['word'])[e['u']]);dec=lambda m:frozenset(w for i,w in enumerate(L) if m>>i&1)
        for d in e['requests']:
            z=next(it);assert z['moves']==d['moves'] and z['goal']==d['goal'] and z['record']==e['record'];g=graph(e['word']);old=None
            for x,v in d['moves']:
                _,rs,_=setup(g,e['u']);old=dec(rs[x]);g=add(g,(x,v))
            _,rs,_=setup(g,e['u']);req=set(map(dec,rs.values()));prot={j:dec(s) for j,s in rs.items() if s.bit_count()<4 and j not in d['goal']};edge=dec(rs[d['goal'][-1]]);passed=[];aud=[]
            for i in z['joint']:
                M=frozenset(map(frozenset,d['pool'][i]));sealed=set(L)-set.union(set(),*boundary(M));tests=[]
                for path,E in fan_paths(L,M,edge,sealed):
                    if not fit(M,E,req,set(prot.values())):continue
                    U=M|E|{t for t in req if len(t)==4};n=sum(old<=t for t in U);cs=[None] if n==2 else [old|{w} for w in set(L)-old if old|{w} not in U and not (old|{w})&sealed and fit(M,E|{old|{w}},req,set(prot.values()))] if n==1 else []
                    for c in cs:
                        block=witness(U|({c} if c else set()),prot,L);tests.append(dict(path=path,tip_cell=sorted(c) if c else None,block=block))
                assert tests
                if any(t['block'] is None for t in tests):passed.append(i)
                aud.append(dict(mesh=i,tests=tests))
            assert set(z['actual'])<=set(passed);cnt['requests']+=1;cnt['exact']+=passed==z['actual'];cnt['extra']+=len(passed)-len(z['actual']);cnt['choices']+=bool(passed);cnt['hit']+=bool(passed and passed[0] in z['actual']);out.append(dict(record=e['record'],goal=d['goal'],moves=d['moves'],actual=z['actual'],passed=passed,audit=aud));
            if z['joint']!=z['actual']:print(e['record'],d['goal'],passed,[(m['mesh'],[(t['block']['vertex'],t['block']['rows']) if t['block'] else None for t in m['tests']]) for m in aud],flush=True)
    print(cnt);prev.save(prev.out/'ramsey38_exposure_cone_filter.json',dict(counts=dict(cnt),results=out))
if __name__=='__main__':run()
