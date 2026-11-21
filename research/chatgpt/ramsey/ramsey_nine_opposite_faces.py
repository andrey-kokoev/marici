"""Recognition using signatures only. Match the six deletion tests to opposite faces; independent check against the classification-free local audit. Identify cube coordinate parity."""
from ramsey_address_to_cube import S,probes,D,json,combinations,Counter
from itertools import permutations

def indices(m):return [i for i in range(8) if m>>i&1]

def run():
    faces=[s for s in S if s.bit_count()==4];op=[(s,255^s) for s in faces if s<255^s];assert len(op)==3 and all(t in faces for _,t in op)
    label_coord=[sum(((t>>i)&1)<<j for j,(_,t) in enumerate(op)) for i in range(8)];assert len(set(label_coord))==8
    for a,b in combinations(range(8),2):assert (((1<<a)|(1<<b)) in S)==((label_coord[a]^label_coord[b]).bit_count()==1)
    E=[e for e in combinations(range(26),2) if not S[e[0]]&S[e[1]]];mask=sum(1<<i for i,(u,v) in enumerate(E) if S[u]|S[v]==255);assert mask.bit_count()==3;d=json.loads((D/'ramsey_nine_chart_local_audit.json').read_text());allred=set(d['wirings']);local={r['wiring'] for r in d['local_audit']};assert all(w&mask==mask for w in allred) and {v|mask for v in local}==allred and len(local)==8*len(allred)
    # Distinguish the label cube from the readout cube. For each label-cube symmetry g push the known state along edges. Test state action conjugacy with g after removing its orientation-reversing component via central inversion.
    Ws=sorted(allred,key=lambda w:sum((w>>E.index(e)&1)<<j for j,e in enumerate(probes)));gs=[];origin=Ws[0]
    for p in permutations(range(3)):
        odd=sum(a>b for a,b in combinations(p,2))%2
        for flip in range(8):
            g=lambda x:sum((x>>p[i]&1)<<i for i in range(3))^flip
            P=[label_coord.index(g(x)) for x in label_coord];A=[S.index(sum(1<<P[i] for i in indices(s))) for s in S];em=[E.index(tuple(sorted((A[i],A[j])))) for i,j in E];state=[Ws.index(sum((w>>i&1)<<a for i,a in enumerate(em))) for w in Ws];proper=[g(x)^(7 if (odd+flip.bit_count())%2 else 0) for x in range(8)];gs.append((proper,state))
    maps=[]
    for initial in range(8):
        rows={};
        for proper,state in gs:rows.setdefault(state[0],set()).add(proper[initial])
        if all(len(y)==1 for y in rows.values()):
            f=[next(iter(rows[i])) for i in range(8)];assert all(f[a[i]]==g[f[i]] for g,a in gs for i in range(8));maps.append(f)
    out=dict(opposite_face_signatures=[[indices(s),indices(t)] for s,t in op],label_coordinates=label_coord,canonical_red_links=mask.bit_count(),valid_restorations=len(allred),proper_rotation_identifications=maps);print(out);return out
if __name__=='__main__':(D/'ramsey_nine_opposite_faces.json').write_text(json.dumps(run())+'\n')
