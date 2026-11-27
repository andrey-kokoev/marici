"""Fixed transfer test: permit a disjoint pair of cells iff their role sets have a literal row in common."""
from ramsey_excel_corner_collisions import D,local,cube,analyze,product,permutations,combinations,json,runpy
from collections import Counter
P=D.parent/'results/ramsey_excel_cell_collision_protocol.json';R=D.parent/'results/ramsey_excel_cell_collision_transfer.json'
rule=dict(scope='All 76 internal red edges in each of the two upper-diagonal completions; six other completions as controls. The 63 red links not between two corners are the transfer test.',relation='Cell pattern covers every corner matching its nonwildcard bits. Gather literal red-position triples realizing any covered corner in any of the four full width-nine placements. Distinct disjoint cells are licensed if these row sets intersect. No new labels, parity restriction, edge colors, or handedness used for licensing.',score='Necessary not sufficient: report unsupported red links, also licensed blue links out of possible disjoint noncorner pairs. Inspect fixed upper-diagonal mirror pair separately, do not optimize labels.')
def run():
    assert json.loads(P.read_text())==rule;C=[''.join(c) for c in product('01*',repeat=3) if c!=('*',)*3];roles={s:set() for s in C};match=lambda s,b:all(c=='*' or c==x for c,x in zip(s,b));corners=[s for s in C if '*' not in s];cc={s:{v for v in corners if match(s,v)} for s in C};
    for z in analyze(9)['pieces']:
        a=z['start']
        for r in cube(a):
            v=''.join(map(str,local(a,r)))
            for s in C:
                if v in cc[s]:roles[s].add(r)
    elig={tuple(sorted((s,t))) for s,t in combinations(C,2) if not cc[s]&cc[t]};allowed={e for e in elig if roles[e[0]]&roles[e[1]]};transfer={e for e in elig if any('*' in s for s in e)};g=runpy.run_path(str(D/'ramsey_cube_construct35.py'));assert C==g['cells'];E={tuple(sorted((C[i],C[j]))) for i,j in combinations(range(26),2) if g['G'][i]>>j&1};orbit=set()
    for perm in permutations(range(3)):
        for bits in product(range(2),repeat=3):
            def trans(s):return ''.join('*' if s[i]=='*' else str(int(s[i])^b) for i,b in zip(perm,bits))
            orbit.add(frozenset(tuple(sorted((trans(s),trans(t)))) for s,t in E))
    out=[];assert len(orbit)==8
    for e in sorted(orbit,key=lambda x:sorted(x)):
        assert e<=elig and len(e&transfer)==63;by={}
        for pair in transfer:
            k='-'.join(sorted('CEF'[s.count('*')] for s in pair));by.setdefault(k,Counter())[('red' if pair in e else 'blue')+('_licensed' if pair in allowed else '_unlicensed')]+=1
        missed=sorted((e&transfer)-allowed);out.append(dict(upper=('000','111') in e,by_type=by,missed=missed,red_licensed=len(e&transfer&allowed),blue_licensed=len((transfer-e)&allowed)));print(out[-1]['upper'],len(missed),out[-1]['blue_licensed'])
    z=dict(protocol=rule,eligible=len(transfer),licensed=len(transfer&allowed),cases=out);print(z['eligible'],z['licensed'],[v for v in out if v['upper']][0]);text=json.dumps(z,indent=2)+'\n';assert not R.exists() or R.read_text()==text;R.write_text(text)
if __name__=='__main__':
    import sys
    if sys.argv[1]=='freeze':
        text=json.dumps(rule,indent=2)+'\n';assert not P.exists() or P.read_text()==text;P.write_text(text)
    else:run()
