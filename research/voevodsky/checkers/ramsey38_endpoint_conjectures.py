"""Unknown final shell: enumerate each vertex star independently and find minimum contradiction."""
from ramsey38_open_middle_cone_trial import P,R,prev,json
from ramsey38_middle_choice_holdout import graph,setup,add,faces
from itertools import combinations
from collections import Counter

def connected(es):
    if not es:return False
    seen=set(es[0]);
    for _ in es:
        for e in es:
            if e&seen:seen.update(e)
    return seen==set.union(set(),*es)

def domain(L,v,M,req,protected,hidden):
    tri=list(map(frozenset,combinations(sorted(set(L)-{v}),3)));ts=[f|{v} for f in tri];forced=M|{r for r in req if len(r)==4};base=[i for i,t in enumerate(ts) if t in forced];opts=[i for i,t in enumerate(ts) if t not in forced];must=[s-{v} for s in req if v in s];out=[]
    for mask in range(1<<len(opts)):
        use=base+[i for k,i in enumerate(opts) if mask>>k&1];fs=[tri[i] for i in use]
        if not fs or not all(any(r<=f for f in fs) for r in must):continue
        edges=Counter(frozenset(x) for f in fs for x in combinations(f,2));
        if max(edges.values())>2:continue
        rim=[s for s,n in edges.items() if n==1];V=set.union(set(),*fs)
        if len(V)-len(edges)+len(fs)!=(1 if rim else 2):continue
        if not connected(list(edges)) or rim and (not connected(rim) or any(k!=2 for k in Counter(w for e in rim for w in e).values())):continue
        if not all(connected([f-{w} for f in fs if w in f]) for w in V):continue
        if any(not any(r-{v}<=e for e in rim) for r in protected if v in r) or any(any(r-{v}<=e for e in rim) for r in hidden if v in r):continue
        out.append(frozenset(ts[i] for i in use))
    return out

def solve(D):
    if not D:return True
    v=min(D,key=lambda w:len(D[w]));return any(solve({w:[t for t in opts if {q for q in t if v in q}=={q for q in s if w in q}] for w,opts in D.items() if w!=v}) for s in D[v])
def run():
    tt=json.loads(R.read_text());assert tt['prediction_sha']==prev.sha(P.read_bytes());it=iter(tt['results']);out=[];cache={}
    for e in json.loads(P.read_text())['cases']:
        for d in e['requests']:
            r=next(it);assert (r['record'],r['moves'],r['goal'])==(e['record'],d['moves'],d['goal']);bad=set(d['passes'])-set(r['ok'])
            if not bad:continue
            h=graph(e['word']);L,_,_=setup(h,e['u']);dec=lambda m:frozenset(v for i,v in enumerate(L) if m>>i&1);hidden=set()
            for x,v in d['moves']:
                _,rs,_=setup(h,e['u']);hidden.add(dec(rs[x]));h=add(h,(x,v))
            _,rs,_=setup(h,e['u']);hidden.update(dec(rs[j]) for j in d['goal']);req=set(map(dec,rs.values()));prot={dec(s) for j,s in rs.items() if s.bit_count()<4 and j not in d['goal']}
            for i in sorted(bad):
                M=frozenset(map(frozenset,d['pool'][i]));k=(tuple(L),M,frozenset(req),frozenset(prot),frozenset(hidden))
                if k not in cache:cache[k]={v:domain(L,v,M,req,prot,hidden) for v in L}
                D=cache[k];empty=[v for v in L if not D[v]];pairs=[]
                for a,b in combinations(L,2):
                    if not D[a] or not D[b]:continue
                    projects=lambda v,w:{frozenset(t for t in s if w in t) for s in D[v]};A=projects(a,b);B=projects(b,a)
                    if not A&B:pairs.append(dict(edge=[a,b],left=sorted(faces(s) for s in A),right=sorted(faces(s) for s in B)))
                core=next((ss for n in range(1,8) for ss in combinations(L,n) if not solve({v:D[v] for v in ss})),None);res=dict(record=e['record'],goal=d['goal'],moves=d['moves'],mesh=i,sizes={v:len(s) for v,s in D.items()},empty=empty,pairs=pairs,smallest=core);out.append(res);print(d['goal'],i,res['sizes'],[x['edge'] for x in pairs],core,flush=True)
    assert len(out)==6;prev.save(prev.out/'ramsey38_endpoint_conjectures.json',dict(comparison_sha=prev.sha(R.read_bytes()),cases=out))
if __name__=='__main__':run()
