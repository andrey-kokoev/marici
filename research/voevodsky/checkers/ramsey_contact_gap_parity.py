from itertools import combinations
from collections import Counter
from ramsey_contact_path_parity import path_capacity, D, json, save, sha256


def side_length(blocked, indices):
    return next((k for k,i in enumerate(indices) if blocked>>i&1),len(indices))


def run():
    old=json.loads((D.parent/'ramsey_double_flank_contact.json').read_text()); expected={(tuple(map(tuple,c['rows'])),z['first'],c['gap']) for z in old['charts'] for c in z['cases'] if c['gap'] in (z['first'],z['first']+1)}
    predicted=set(); counts=Counter(); example=None; caps=[path_capacity(8,b) for b in range(256)]
    rows=[s for s in combinations(range(1,9),3) if min(s[1]-s[0],s[2]-s[1])>=2]
    for ss in combinations(rows,5):
        edges=[(1<<i)|(1<<j) for i,j in combinations(range(5),2) if set(ss[i]).isdisjoint(ss[j])]
        if len(edges)!=2:continue
        masks=[sum(1<<(i-1) for i in row) for row in ss];six=[set(),set()];both=True
        for p in range(32):
            u=0
            for i,m in enumerate(masks):
                if p>>i&1:u|=m
            if caps[u]+p.bit_count()<6:continue
            if all((p&e)!=e for e in edges):both=False;break
            for j,e in enumerate(edges):
                if (p&e)!=e:
                    assert caps[u]+p.bit_count()==6;six[j].add(u)
        if not both or not all(six):continue
        counts['families']+=1
        for f in range(9):
            lr=[[(side_length(u,range(f-1,-1,-1)),side_length(u,range(f,8))) for u in us] for us in six];parents=all((l+r)%2 for vals in lr for l,r in vals)
            for d,g in enumerate((f,f+1)):
                if not 1<=g<=8:continue
                if not parents:counts['parent_fails']+=1;continue
                passes=[any(v[d]%2 for v in vals) for vals in lr];counts['old_witnesses_'+str(sum(passes))]+=1
                if all(passes):predicted.add((ss,f,g))
                if example is None and parents and 0<f<8 and all(passes) and not all(any(v[1-d]%2 for v in vals) for vals in lr):example=dict(rows=ss,first=f,second=g,run_lengths=[sorted(set(vals)) for vals in lr])
    assert predicted==expected and counts['families']==40
    out=dict(counts=counts,example=example,protocol_sha=sha256((D.parent/'ramsey_contact_gap_parity_protocol.md').read_bytes()).hexdigest());print(out);save(D.parent/'ramsey_contact_gap_parity.json',out)

if __name__=='__main__':run()
