"""Can retaining literal rows, as well as swap roles, discriminate the marked corner edge?"""
from collections import defaultdict,Counter
from itertools import combinations,permutations,product
from ramsey_excel_successor_chart_audit import cube,local,mirror,D,json,runpy
from ramsey_table_cube_differences import analyze

def run():
    starts=[tuple(z['start']) for z in analyze(9)['pieces']];roles=defaultdict(set);word=lambda bs:''.join(map(str,bs))
    for a in starts:
        for r in cube(a):roles[r].add(word(local(a,r)))
    witnesses=defaultdict(list)
    for r,seen in roles.items():
        for pair in combinations(sorted(seen),2):witnesses[pair].append(r)
    corners=sorted(word(t) for t in product(range(2),repeat=3));pairs=set(combinations(corners,2));d=lambda e:sum(x!=y for x,y in zip(*e));hist=Counter(d(e) for e in witnesses);odd={e for e in witnesses if d(e)%2};raw=set(witnesses)
    print(hist,'odd',sorted(odd));assert {e for e in odd if d(e)==3}=={('000','111')};assert all(tuple(10-v for v in r[::-1]) in roles for r in roles)
    # Derive the exchange-overlap relation without graph data; only then compare.
    g=runpy.run_path(str(D/'ramsey_cube_construct35.py'));C=g['cells'];base={e for e in pairs if g['G'][C.index(e[0])]>>C.index(e[1])&1};patterns=set()
    for p in permutations(range(3)):
        for b in product(range(2),repeat=3):
            f=lambda s:word([int(s[j])^k for j,k in zip(p,b)]);patterns.add(frozenset(tuple(sorted(map(f,e))) for e in base))
    assert len(patterns)==4;checks=[dict(red_diagonal=sorted(next(e for e in E if d(e)==3)),raw_false_red=len(raw-E),odd_false_red=len(odd-E),odd_missing=len(E-odd)) for E in sorted(patterns,key=lambda E:sorted(E))];print(checks)
    # All four role charts contain this row; each of the other two labels gives a mandatory triangle if collisions are all red.
    triangles=[t for t in combinations(corners,3) if all(e in raw for e in combinations(t,2))];print('central row roles',sorted(roles[(2,5,8)]),'raw triangles',len(triangles))
    out=dict(starts=starts,histogram=dict(hist),collision_witnesses=[dict(pair=e,rows=sorted(rs)) for e,rs in sorted(witnesses.items())],raw_triangles=triangles,conditional_comparisons=checks);dest=D.parent/'results/ramsey_excel_corner_collisions.json';text=json.dumps(out,indent=2)+'\n';assert not dest.exists() or dest.read_text()==text;dest.write_text(text)
if __name__=='__main__':run()
