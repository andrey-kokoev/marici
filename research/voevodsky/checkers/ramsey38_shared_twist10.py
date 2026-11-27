"""Record 162: compare named partial links, keeping the two boundary rims distinct."""
from itertools import combinations
from collections import Counter
from ramsey38_early_sign_trial import P,prev,inputs,json,neg
from ramsey38_signed_swap_transport import replay,transport

def faces(fs):return sorted(sorted(f) for f in fs)
def minimal(base,optional):
    hits=[]
    for n in range(len(optional)+1):
        for q in combinations(sorted(optional,key=sorted),n):
            q=frozenset(q)
            if not any(h<=q for h in hits) and neg(base|q):hits.append(q)
    return hits

def face_assignments(labs,req,bd):
    # Enumerate mod-two chains with the given boundary via toggles of 4-simplex boundaries.
    p=set(labs);v=min(p);cells=list(map(frozenset,combinations(labs,4)));bits={t:1<<i for i,t in enumerate(cells)};m=[sum(bits[f|{v}] for f in bd if v not in f)]
    for t in cells:
        if v not in t:
            toggle=sum(b for q,b in bits.items() if q<=t|{v});m += [i^toggle for i in m]
    forced=sum(bits[t] for t in req if len(t)==4)
    for i in m:
        if i&forced!=forced:continue
        ts=[t for t,b in bits.items() if i&b];hits=Counter(frozenset(f) for t in ts for f in combinations(t,3));
        if all(any(s<=t for t in ts) for s in req) and all(n==(1 if f in bd else 2) for f,n in hits.items()):yield ts

def face_only(labs,req,bd,target):
    return dict(Counter(str(target in ts) for ts in face_assignments(labs,req,bd)))

def run():
    audit=json.loads((prev.out/'ramsey38_early_sign_join_and_links.json').read_text());e=next(e for e in json.loads(P.read_text())['cases'] if e['record']==162 and e['u']==5);b,_,x,rs,v=inputs(e);labs=sorted(b[5]);decode=lambda m:frozenset(a for i,a in enumerate(labs) if m>>i&1);S=rs[x];rs[x]|=v;out=[]
    for z in audit['unfilled']:
        if z['core'] is not None:continue
        assert (z['record'],z['root'])==(162,5);bd=set(map(decode,z['bd']));req=set(map(decode,rs.values()))|{decode(S)|{z['tip']}};ts,=replay(dict(enumerate(req)),bd);link={t-{10} for t in ts if 10 in t};fixed={t-{10} for t in req if len(t)==4 and 10 in t};cap={(f-{10})|{0} for f in bd if 10 in f};z['face_only_contains_target']=face_only(labs,req,bd,frozenset((8,10,19,24)));out.append((z,link,fixed,cap))
    (_,a,_,ca),(_,b,_,cb)=out;shared=a&b;print('intersection',faces(shared),'orientable?',not neg(shared),'common cap conflict?',neg(shared|(ca&cb)));results=[]
    for z,link,fixed,cap in out:
        assert fixed<=shared and not neg(cap|fixed);hs=minimal(cap|fixed,link-fixed);plain=minimal(fixed,link-fixed);sharedhits=[faces(h) for h in hs if h<=shared];target=frozenset((8,19,24));assert neg(fixed|{target}|(ca&cb)) and not neg(fixed|(ca&cb));r=dict(row=z['row'],tip=z['tip'],face_only=z['face_only_contains_target'],fixed=faces(fixed),rim=faces({s-{0} for s in cap}),shared_witnesses=sharedhits,capped_witnesses=[faces(h) for h in hs],uncapped_witnesses=[faces(h) for h in plain]);results.append(r);print(r)
    prev.save(prev.out/'ramsey38_shared_twist10_face_audit.json',dict(shared=faces(shared),shared_negative_walk=transport(shared)[0],shared_with_common_rim_walk=transport(shared|(ca&cb))[0],cases=results))
if __name__=='__main__':run()
