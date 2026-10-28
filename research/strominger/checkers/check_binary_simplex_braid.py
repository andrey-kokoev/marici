"""Exact candidate: retained binary communication schedule on recovered T184 frames.
No particle assignment or viewer geometry is changed. Standard-library only.
"""
from collections import defaultdict
from itertools import combinations, permutations, product
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
PATHS = {
    'definition': 'research/strominger/binary-simplex-braid-candidate-v1.json',
    'census': 'research/voevodsky/results/esd7_explicit_analytical_census.json',
    'native': 'research/strominger/results/native-fcc-end-to-end.json',
}

def clean(c): return {s: a for s, a in c.items() if a}
def parity(s): return (-1) ** sum(s[i] > s[j] for i in range(len(s)) for j in range(i + 1, len(s)))
def boundary(chain):
    out = defaultdict(int)
    for s, a in chain.items():
        if len(s) > 1:
            for i in range(len(s)): out[s[:i] + s[i+1:]] += a * (-1)**i
    return clean(out)
def transport(chain, p):
    out = defaultdict(int)
    for s, a in chain.items():
        target = tuple(p[v] for v in s)
        out[tuple(sorted(target))] += a * parity(target)
    return clean(out)
def compose(p, q): return tuple(p[q[i]] for i in range(len(p)))
def schedule(tree, address=''):
    if 'action' in tree:
        if tree['action'] not in ('L', 'R'): raise ValueError('Unknown leaf action')
        return [{'kind': tree['action'], 'address': address}]
    children = tree['split']
    if len(children) != 2: raise ValueError('Binary split required')
    return [{'kind': 'split', 'address': address}] + schedule(children[0], address+'0') + schedule(children[1], address+'1')
def advance(t, kind): return 3-t if kind == 'L' else 4-t if kind == 'R' else t
def run(t, events):
    records = []
    for e in events:
        after = advance(t, e['kind'])
        records.append({**e, 'before': {'t': t, 'grade': t//4, 'chart': t%4}, 'after': {'t': after, 'grade': after//4, 'chart': after%4}})
        t = after
    return t, records

def main():
    inputs = {k: json.loads((ROOT/p).read_text(encoding='utf-8')) for k,p in PATHS.items()}
    definition, census, native = (inputs[k] for k in ('definition','census','native'))
    checks = []
    def check(name, condition):
        if not condition: raise AssertionError(name)
        checks.append(name)
    census_hash = hashlib.sha256((ROOT/PATHS['census']).read_bytes()).hexdigest()
    check('native replay receipt is bound to the live census', native['sourceSha256'][PATHS['census']] == census_hash)
    rows = {r['id']: r for family in ('vertices','edges','triangles','tetrahedra') for r in census[family]}
    def row_vertices(id): return (id,) if id.startswith('V') else tuple(rows[id]['vertices'])
    views = native['fixture']['sevenViews']
    frame = []
    for view in views[:4]:
        extra = set(row_vertices(view['id'])) - set(frame)
        check('one new reference mark at '+view['id'], len(extra)==1)
        frame.append(extra.pop())
    check('four reference marks belong to actual T184', set(frame)==set(row_vertices('T184')))
    coords = {r['id']: tuple(r['barycentric']) for r in census['vertices']}
    by_coord = {c: id for id,c in coords.items()}
    rho_vertex = {v: by_coord[(coords[v][-1], *coords[v][:-1])] for v in frame}
    q = tuple(frame.index(rho_vertex[v]) for v in frame)
    L = tuple(native['fixture']['requiredNativeFlagPermutation'])
    R = compose(q,L)
    identity = tuple(range(4))
    check('recovered source rho is the cyclic frame successor', q==(1,2,3,0))
    check('recovered native flag reversal is order two', L==(3,2,1,0) and compose(L,L)==identity)
    check('derived second reflection is order two', compose(R,R)==identity)
    check('chronological LRRR equals the source chart successor', compose(R,compose(R,compose(R,L)))==q)
    check('two reflections satisfy length-four, not length-three, braid relation', compose(L,compose(R,compose(L,R)))==compose(R,compose(L,compose(R,L))) and compose(L,compose(R,L))!=compose(R,compose(L,R)))
    group={identity}
    while True:
        larger=group|{compose(g,h) for g in (L,R) for h in group}
        if larger==group: break
        group=larger
    check('frame quotient is D4 of order eight, not all S4', len(group)==8)
    simplices=[s for n in range(1,5) for s in combinations(sorted(frame),n)]
    for g in group:
        p={frame[i]:frame[g[i]] for i in range(4)}
        for s in simplices:
            check_name='signed incidence transport for all fifteen simplex coordinates'
            assert boundary(transport({s:1},p))==transport(boundary({s:1}),p)
    checks.append(check_name)
    check('witness tetrahedron has six edges four faces and closed signed boundary', sum(len(s)==2 for s in simplices)==6 and sum(len(s)==3 for s in simplices)==4 and not boundary(boundary({tuple(sorted(frame)):1})))
    # Dual restriction is typed by evaluation. Reverse incidence is not an
    # inverse map: deleting an edge before its boundary gives a counterexample.
    edge=tuple(sorted(frame[:2])); vertex=(edge[0],)
    project=lambda c: {s:a for s,a in c.items() if set(s)<=set(vertex)}
    check('reverse incidence cannot be silent chain-coordinate deletion', boundary(project({edge:1}))!=project(boundary({edge:1})))
    events=schedule(definition['split_tree'])
    leaves=[e for e in events if e['kind']!='split']
    check('binary comb has three splits and four retained leaf contexts', len(events)==7 and [e['address'] for e in leaves]==['0','10','110','111'])
    check('the leaf schedule is LRRR', ''.join(e['kind'] for e in leaves)=='LRRR')
    for t in range(-40,41):
        assert advance(advance(t,'L'),'L')==t and advance(advance(t,'R'),'R')==t
        assert run(t,events)[0]==t+1
        assert run(t,events*4)[0]==t+4
        assert run(t,[{'kind':k,'address':''} for k in 'LRLR'])[0]!=run(t,[{'kind':k,'address':''} for k in 'RLRL'])[0]
    checks.append('retained lift: one seven-event block advances q, four blocks advance Sigma')
    checks.append('finite braid equality does not erase the grade: opposite four-letter routes differ by one Sigma')
    end,trace=run(0,events*4)
    check('twenty-eight events retain four chart advances and one grade', len(trace)==28 and end==4 and trace[-1]['after']=={'t':4,'grade':1,'chart':0})
    independent=[advance(0,e['kind']) for e in leaves]
    check('four independent branch endpoints are not the single-state block result', independent==[3,4,4,4] and run(0,events)[0]==1)
    check('same action inventory in another order does not give the same handoff', run(0,[{'kind':k,'address':''} for k in 'RLRR'])[0]==-1)
    # A one-object, one-arrow strict 2-category with Z/2 comparison cells:
    # every face comparison is invertible, but a tetrahedral filler requires
    # agreement of its two reductions. L/R endpoint identities do not supply it.
    coherent=[]; obstructed=[]
    for h012,h013,h023,h123 in product(range(2),repeat=4):
        row=[h012,h013,h023,h123]
        (coherent if (h023+h012)%2==(h013+h123)%2 else obstructed).append(row)
    check('local invertible comparisons do not imply a witness filler', len(coherent)==len(obstructed)==8)
    # Four face ports and their ancestry, transported with the marking.
    ports=[{'address':e['address'],'action':e['kind'],'oppositeVertex':v,'face':next(r['id'] for r in census['triangles'] if set(r['vertices'])==set(frame)-{v})} for e,v in zip(leaves,frame)]
    check('binary addresses bind four distinct actual face ports', len({p['face'] for p in ports})==4)
    check('first and last ports are the actual native output and input faces', ports[0]['face']==views[4]['id'] and ports[-1]['face']==views[2]['id'])
    reversal={frame[i]:frame[L[i]] for i in range(4)}
    face_ids={frozenset(r['vertices']):r['id'] for r in census['triangles']}
    for port in ports:
        port['reversedFrameFace']=face_ids[frozenset(reversal[v] for v in rows[port['face']]['vertices'])]
    for perm in permutations(frame):
        p=dict(zip(frame,perm))
        for port in ports:
            mapped=face_ids[frozenset(p[v] for v in rows[port['face']]['vertices'])]
            expected=face_ids[frozenset(set(frame)-{p[port['oppositeVertex']]})]
            assert mapped==expected
    checks.append('four-port wiring is covariant under all24 marked frame changes')
    result={
        'status':'passed','classification':'candidate schedule and retained dihedral transport; not a PNE derivation',
        'checks':checks,'sourceSha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in PATHS.values()},
        'centralFrame':frame,'q':q,'L':L,'R':R,'finiteFrameGroupOrder':len(group),
        'eventsPerBlock':events,'facePorts':ports,'fourBlockTrace':trace,
        'witnessCounterexample':{'faceComparisons':obstructed[0],'allInvertible':True,'tetrahedralCoherence':False},
        'importantDistinction':'LRLR=RLRL only after forgetting the grade; lifted chronological routes shift t by +2 versus -2. Their difference is Sigma, not equality of retained states.',
        'unbound':definition['unbound'],
        'thirdSimplex':'T184 supplies actual incidence and the shape of a witness equation; no source-selected third-simplex attachment or analytic filler is asserted.'
    }
    out=ROOT/'research/strominger/results/binary-simplex-braid-v1.json';out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(f'PASS: {len(checks)} exact check groups; 7 events/block, 28 events/Sigma; retained braid defect preserved')

if __name__=='__main__': main()
