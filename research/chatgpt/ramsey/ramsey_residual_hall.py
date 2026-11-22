"""Fix seven leftover vertices, partition complement into independent fives. For each independent J inside R, each color must supply |J| distinct neighbours. Test exact sharp Hall depth against every one-vertex swap of every known feasible reservoir, without using the original partition as seed."""
from ramsey_inverse_five_motifs import D,json,inds,bits,graph,Counter,combinations

def audit(H,rows):
    F=(1<<len(H))-1;I=inds(H);fives=[s for s in I if s.bit_count()==5];N={j:0 for j in I};
    for j in N:
        for v in bits(j):N[j]|=H[v]
    true={r['leftover'] for r in rows};near={r^(1<<v)^(1<<w) for r in true for v in bits(r) for w in bits(F^r)}|true;hist=Counter();details=[];essential=Counter()
    for r in sorted(near):
        J=[j for j in I if j and not j&~r];depth={s:min(((j.bit_count() if (N[j]&s).bit_count()<j.bit_count() else 8) for j in J),default=8) for s in fives if not s&r};p=[]
        for s,t in combinations(sorted(depth),2):
            u=F^(r|s|t)
            if s&t or u<=t or u not in depth:continue
            p.append((min(depth[s],depth[t],depth[u]),s,t,u))
        h=max((x[0] for x in p),default=0);hist[h]+=1;assert (h==8)==(r in true);essential.update(x[0] for x in p);details.append(dict(R=r,depth=h,example=max(p,default=None)))
    return dict(reservoirs=hist,partitions=essential,details=details)
if __name__=='__main__':
    ls=(D/'pauli-realization-catalogues/r37_22.g6').read_bytes().splitlines();z={i:audit(graph(ls[int(i)-1]),rows) for i,rows in json.loads((D/'ramsey_uncovered_five.json').read_text()).items()};print(sum((r['reservoirs'] for r in z.values()),Counter()),sum((r['partitions'] for r in z.values()),Counter()));(D/'ramsey_residual_hall.json').write_text(json.dumps(z)+'\n')
