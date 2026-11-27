"""Can a naked containment trap serve as a promoted-array mesh? Check the edge gate and a relaxation."""
from ramsey38_nested_ball_obstruction_trial import P,R,prev,json,gzip,setup,add,graph
from ramsey38_compare_support_fillings import boundary
from itertools import permutations,combinations
from collections import Counter

def view(cells):
    bd=boundary(cells);return ({tuple(sorted(h)) for t in cells for k in range(1,5) for h in combinations(t,k)}, {tuple(sorted(h)) for f in bd for k in (1,2,3) for h in combinations(f,k)})
def run():
    d=json.loads(P.read_text());z=json.loads(R.read_text());assert z['sample_sha']==prev.sha(P.read_bytes());roots={e['record']:e['root'] for e in d['entries']};graphs={}
    with gzip.open(prev.catalogue,'rt') as f:
        for i,line in enumerate(f,1):
            if i in roots:graphs[i]=graph(line.strip())
            if i>=max(roots):break
    traps={}
    for c in z['failures']:
        B=frozenset(map(frozenset,c['cells']));A=frozenset(frozenset(t) for i,t in enumerate(c['cells']) if c['prefix']>>i&1);traps.setdefault((A,B),[]).append(c['record'])
    out=[]
    for (A,B),ids in traps.items():
        L0=sorted(set.union(set(),*A));occupied,bd=view(A);ints=sorted(set(s for s in occupied-bd if len(s)<4));assert all(len(s)==3 for s in ints);focc,fbd=view(B);counts=Counter();examples=[]
        for i,u in roots.items():
            g=graphs[i];L,rs,moves=setup(g,u)
            def change(rs,m):x,v=m;return {**rs,x:rs[x]|1<<L.index(v)}
            for a in moves:
                r=change(rs,a);bs=setup(add(g,a),u)[2];
                if not bs:continue
                # Require all supports intact and the promoted old triangle buried;
                # allow the one other hidden row to have any short size (including three).
                for perm in permutations(L0):
                    code=lambda s:tuple(sorted(perm[j] for j in range(len(L)) if s>>j&1));rr={j:code(s) for j,s in r.items()};counts['first_edit_maps']+=1
                    if any(t and t not in occupied for t in rr.values()):continue
                    counts['all_supports_fit']+=1
                    if code(rs[a[0]]) not in ints:continue
                    counts['promotion_buried']+=1;hidden={j for j,t in rr.items() if 0<len(t)<4 and t not in bd}
                    if len(hidden)!=1:continue
                    counts['relaxed_first']+=1
                    for b in bs:
                        fin={j:code(s) for j,s in change(r,b).items()};fh={j for j,t in fin.items() if 0<len(t)<4 and t not in fbd}
                        if any(t and t not in focc for t in fin.values()) or code(rs[a[0]]) in fbd or code(r[b[0]]) in fbd or len(fh)!=2 or not hidden<fh:continue
                        counts['relaxed_pair']+=1
                        if len(examples)<3:examples.append(dict(record=i,root=u,map=perm,moves=[a,b],hidden=sorted(hidden),final=sorted(fh)))
        out.append(dict(source_records=ids,interior_short_faces=ints,edges=sum(len(s)==2 for s in occupied),counts=dict(counts),examples=examples));print(ids,ints,counts,examples)
    prev.save(prev.out/'ramsey38_trap_markability.json',dict(source_sha=prev.sha(R.read_bytes()),cases=out))
if __name__=='__main__':run()
