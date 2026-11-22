"""Classify first supports via nested union tests, no SAT. Count sorted maximal port multisets surviving each level; repeats permitted."""
from ramsey_capacity_transfer_78 import D,json,decode,inds,bits

def audit(H):
    I=inds(H);M=sorted(s for s in I if all(s>>v&1 or s&h for v,h in enumerate(H)));n=len(M);miss={k:[sum(1<<i for i,t in enumerate([t for t in I if t.bit_count()==k]) if not s&t) for s in M] for k in (4,5,6)};p=miss[6];q=miss[5];w=miss[4];adj=[sum(1<<j for j in range(i,n) if not p[i]&p[j]) for i in range(n)];counts=[0]*3;first=[set() for _ in counts]
    for i,row in enumerate(adj):
        for j in bits(row):
            common=row&adj[j];ij=q[i]&q[j];ij4=w[i]&w[j]
            for k in bits(common):
                tails=common&adj[k];
                if not tails:continue
                fixed=(i,j,k);counts[0]+=tails.bit_count();first[0].update(fixed);first[0].update(bits(tails));
                if ij&q[k]:continue
                ban=ij|(q[i]&q[k])|(q[j]&q[k]);ban4=ij4&w[k]
                for l in bits(tails):
                    if q[l]&ban:continue
                    counts[1]+=1;first[1].update((*fixed,l));
                    if w[l]&ban4:continue
                    counts[2]+=1;first[2].update((*fixed,l))
    return counts,[[M[i] for i in sorted(s)] for s in first]

def run():
    lines=(D/'pauli-realization-catalogues/r37_22.g6').read_bytes().splitlines();out=[]
    for r in json.loads((D/'ramsey_bare_core_rank.json').read_text()):
        H=decode(lines[r['parent']-1]);V=[x for x in range(22) if x!=r['deleted']];counts,sets=audit([sum(1<<j for j,y in enumerate(V) if H[x]>>y&1) for x in V]);assert sets[2]==r['good'];out.append(dict(parent=r['parent'],deleted=r['deleted'],candidates=r['firsts'],counts=counts,first=[len(s) for s in sets]))
    return out
if __name__=='__main__':
    out=run();print(sum(r['candidates'] for r in out));print([[sum(r[key][i] for r in out) for i in range(3)] for key in ('counts','first')]);print([sum(bool(r['first'][i]) for r in out) for i in range(3)]);(D/'ramsey_port_union_hierarchy.json').write_text(json.dumps(out)+'\n')
