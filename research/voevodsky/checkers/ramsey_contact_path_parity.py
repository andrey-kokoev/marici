from collections import Counter
from itertools import combinations
from ramsey_double_flank_geometry import D, json, save, sha256


def path_capacity(n, blocked):
    best = prev = 0
    for i in range(n):
        prev, best = best, (best if blocked >> i & 1 else max(best, 1 + prev))
    return best


def run():
    capacity = [path_capacity(8,b) for b in range(256)]
    for b in range(256):
        for gap in range(9):
            left = (1 << gap)-1
            child = (b & left) | ((b & ~left) << 2)
            assert path_capacity(10,child) == capacity[b]+1
    old = json.loads((D.parent/'ramsey_double_flank_contact.json').read_text())
    touching = Counter(tuple(map(tuple,c['rows'])) for chart in old['charts'] for c in chart['cases'] if c['gap'] in (chart['first'],chart['first']+1))
    profiles = Counter(); wins = Counter(); seen = set()
    rows = [s for s in combinations(range(1,9),3) if min(s[1]-s[0],s[2]-s[1])>=2]
    for ss in combinations(rows,5):
        edges = [(1<<a)|(1<<b) for a,b in combinations(range(5),2) if set(ss[a]).isdisjoint(ss[b])]
        if len(edges)!=2:continue
        masks = [sum(1<<(x-1) for x in s) for s in ss]; sizes=[]; blocked=[0]*32
        for p in range(1,32):
            bit=p&-p;blocked[p]=blocked[p^bit]|masks[bit.bit_length()-1]
        for active in ([],edges[:1],edges[1:],edges):
            sizes.append(max(p.bit_count()+capacity[blocked[p]] for p in range(32) if not any((p&e)==e for e in active)))
        key=tuple(sizes); profiles[key]+=1
        if ss in touching:
            assert sizes[-1]==5 and min(sizes[1:3])==6 and max(sizes[1:3])==6
            wins[key]+=touching[ss]; seen.add(ss)
    assert seen==set(touching) and sum(wins.values())==92 and sum(profiles.values())==4166
    encode=lambda counter:{'/'.join(map(str,k)):v for k,v in sorted(counter.items())}
    both_only=sum(n for k,n in profiles.items() if k[-1]<=5 and min(k[1:3])>=6)
    out=dict(mask_gap_checks=256*9,families=sum(profiles.values()),both_only_families=both_only,usable_touching_families=len(seen),profiles=encode(profiles),usable_touching_seams=encode(wins),protocol_sha=sha256((D.parent/'ramsey_contact_path_parity_protocol.md').read_bytes()).hexdigest());print(out);save(D.parent/'ramsey_contact_path_parity.json',out)

if __name__=='__main__':run()
