from ramsey_five_port_multi import graph,check,D,combinations,combinations_with_replacement,sevens,sha256,json
from itertools import permutations

def search():
    rows=[s for s in combinations(range(8),3) if min(s[1]-s[0],s[2]-s[1])>=2];pairs=list(combinations(range(5),2));eligible_seams=0
    for idx,ss in enumerate(combinations_with_replacement(rows,5),1):
        if not check(graph(8,ss,0),8191,3,7):continue
        es=[e for e in pairs if set(ss[e[0]]).isdisjoint(ss[e[1]])];
        if len(es)<3:continue
        for gap in range(9):
            eligible_seams+=1;t=[tuple(x+(x>=gap) for x in s) for s in ss];qs=list(sevens(graph(9,t,0)));ps={frozenset(j-9 for j in q if j>=9) for q in qs};ds=[{e for e in es if set(e)<=p} for p in ps];
            if not ds or not all(ds) or set.intersection(*ds):continue
            wins={s for s in combinations(es,2) if all(d.intersection(s) for d in ds)}
            if len(wins)<2:continue
            perms=[p for p in permutations(range(5)) if tuple(ss[i] for i in p)==ss];orbits={min(tuple(sorted(tuple(sorted((p[i],p[j]))) for i,j in s)) for p in perms) for s in wins};
            if len(orbits)<2:continue
            for edits in [(),*((e,) for e in es),*combinations(es,2)]:
                b=sum(1<<pairs.index(e) for e in edits);assert check(graph(8,ss,b),8191,3,7) and check(graph(9,t,b),16383,3,7)==(edits in wins)
            one=lambda s:[[i+1,j+1] for i,j in s];return dict(multisets_seen=idx,seams_examined=eligible_seams,supports=[[x+1 for x in s] for s in ss],gap=gap,group_size=len(perms),minimal_demands=[sorted(v+1 for v in p) for p in sorted(ps,key=sorted) if not any(q<p for q in ps)],legal_pairs=one(es),wins=[one(s) for s in sorted(wins)],representatives=[dict(edits=one(s),degree_sequence=sorted(b.bit_count() for b in graph(9,t,sum(1<<pairs.index(e) for e in s)))) for s in sorted(orbits)])
    return dict(no_example=True)
if __name__=='__main__':
    out=search();out['protocol_sha']=sha256((D.parent/'ramsey_port_repair_orbit_protocol.md').read_bytes()).hexdigest();print(out);r=D.parent/'ramsey_port_repair_orbits.json';s=json.dumps(out,indent=2)+'\n';assert not r.exists() or r.read_text()==s;r.write_text(s)
