"""Construct directly from endpoint neighbourhoods: each port takes its two named seed endpoints plus all four private neighbours of ONE of its two opposite endpoints. The two perfect matchings of this incidence cycle give two assignments. No partner search or propagation."""
from ramsey_capacity_transfer_78 import D,json,decode,bits,inds,verify,grow,Counter,combinations
from itertools import permutations

def run():
    prev=json.loads((D/'ramsey_rooted_square_propagation.json').read_text());branches={(r['record'],r['seed']):r for r in json.loads((D/'ramsey_square_branch_coordinates.json').read_text())};lines=(D/'pauli-realization-catalogues/r37_22.g6').read_bytes().splitlines();out=[];last=None
    for r in prev:
        idx=r['record'];W=r['seed'];
        if idx!=last:
            H=decode(lines[idx-1]);T=[t for t in inds(H) if t.bit_count()>=4];last=idx
        a=next(bits(W));b=next(bits(H[a]&W));c,d=bits(W^(1<<a|1<<b));edges=[(a,c),(a,d),(b,c),(b,d)];P=[H[i]&~W for i in (a,b,c,d)];private=all(not x&y for x,y in combinations(P,2));row=dict(record=idx,seed=W,private=private,good=bool(r['legal']),attempts=[]);br=branches.get((idx,W));
        if private:
            for perm in permutations((a,b,c,d)):
                if any(x in ed for x,ed in zip(perm,edges)):continue
                S=[(1<<i|1<<j)|(H[x]&~W) for (i,j),x in zip(edges,perm)];assert all(all(not H[v]&s for v in bits(s)) for s in S);bad=[t for t in T if t.bit_count()+sum(not t&s for s in S)>=8];row['attempts'].append(dict(ports=S,violations=bad));
                if not bad:verify(grow(H,S),8)
            assert len(row['attempts'])==2
        if br and 'anchors' in br:
            rot=sum(br['anchors']);row['neighbour_anchor']=sum((H[i]&W).bit_count()==1 and rot>>i&1 for i in range(22));row['other_anchor']=sum(not H[i]&W and rot>>i&1 for i in range(22));row['same_template']=sum(any(all(attempt['ports'][i] in br['groups'][i][v[i]] for i in range(4)) for v in br['boxes']) for attempt in row['attempts'])
        out.append(row)
    return out
if __name__=='__main__':
    z=run();print(Counter((r['private'],r['good'],sum(not a['violations'] for a in r['attempts'])) for r in z));print(Counter(r['same_template'] for r in z if 'same_template' in r));(D/'ramsey_neighbourhood_square.json').write_text(json.dumps(z)+'\n')
