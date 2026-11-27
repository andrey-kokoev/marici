"""Enumerate individual vertex stars (disks), not whole fillings. Propagate star agreement."""
from ramsey38_choose_promotion_trial import P,prev,json,graph,setup,combinations
from ramsey38_novel_root8_diagonal import sub,link_profile
from collections import Counter

def disks(labs,w,bd,req,allow_interior=False):
    # Enumerate mod-2 triangle chains with prescribed rim by independent tetrahedron boundary toggles.
    vs=set(labs)-{w};base=min(vs);tri=sorted(sub(vs,3),key=sorted);bits={f:1<<i for i,f in enumerate(tri)};rim={f-{w} for f in bd if w in f};must={t-{w} for t in req if w in t};m=[sum(bits[f|{base}] for f in rim if base not in f)]
    for f in tri:
        if base not in f:
            toggle=sum(bits[h] for h in sub(f|{base},3));m += [s^toggle for s in m]
    # Boundary link: disk (chi=1). Occupied non-boundary link: sphere (chi=2).
    # An unrequired non-boundary label may also be unused.
    chi=2 if allow_interior and not rim else 1
    out=[frozenset()] if allow_interior and not rim and not must else []
    for s in m:
        fs=[f for f in tri if s&bits[f]]
        if not fs or not all(any(t<=f for f in fs) for t in must):continue
        ts=frozenset(f|{w} for f in fs)
        # Other forced tets consume face capacity, even if not incident to w.
        occ=Counter(h for t in ts|{t for t in req if len(t)==4} for h in sub(t,3))
        if any(n>(1 if h in bd else 2) for h,n in occ.items()):continue
        es=Counter(e for f in fs for e in sub(f,2));V=set.union(set(),*fs)
        if any(n!=(1 if e in rim else 2) for e,n in es.items()) or len(V)-len(es)+len(fs)!=chi or link_profile(fs)!=(1,True):continue
        for v in V:
            seg=[f-{v} for f in fs if v in f];seen=set(seg[0]);
            for _ in seg:
                for h in seg:
                    if seen&h:seen.update(h)
            if seen!=set.union(set(),*seg):break
        else:out.append(ts)
    return out

def propagate(D):
    trace=[{w:len(ss) for w,ss in D.items()}];events=[]
    while all(D.values()):
        projections={(a,b):{frozenset(t for t in s if b in t) for s in D[a]} for a,b in ((a,b) for a in D for b in D if a!=b)};N={};step={}
        for a,opts in D.items():
            N[a]=[s for s in opts if all(frozenset(t for t in s if b in t) in projections[b,a] for b in D if a!=b)]
            for b in D:
                if b!=a and projections[a,b].isdisjoint(projections[b,a]):step.setdefault(a,[]).append(b)
        if N==D:break
        D=N;trace.append({w:len(ss) for w,ss in D.items()});events.append(step)
    return trace,events

def run():
    e=next(e for e in json.loads(P.read_text())['cases'] if e['record']==426);c=next(d['choice'] for d in e['requests'] if d['row']==20);L,rs,_=setup(graph(e['word']),e['u']);dec=lambda m:frozenset(w for i,w in enumerate(L) if m>>i&1);x,v=c['edge'];S=dec(rs[x]);rs[x]|=1<<L.index(v);bd=set(map(dec,c['bd']));out=[]
    for w in c['tips']:
        req=set(map(dec,rs.values()))|{S|{w}};D={a:disks(L,a,bd,req) for a in L};trace,events=propagate(D);witness=None
        for a in L:
            rejected=[]
            for s in D[a]:
                bad=[b for b in L if b!=a and not any({t for t in s if b in t}=={t for t in u if a in t} for u in D[b])];rejected.append(bad)
            if rejected and all(rejected):
                blockers=min((q for n in range(1,len(L)) for q in combinations([b for b in L if b!=a],n) if all(set(q)&set(h) for h in rejected)),key=len);witness=dict(vertex=a,blockers=blockers,options=[dict(link=sorted(sorted(t-{a}) for t in s),incompatible=h) for s,h in zip(D[a],rejected)]);break
        print(w,trace,witness);out.append(dict(tip=w,counts=trace,conflicts=events,witness=witness))
    prev.save(prev.out/'ramsey38_tip_disk_witness.json',dict(record=426,root=e['u'],row=20,triangle=sorted(S),cases=out))
if __name__=='__main__':run()
