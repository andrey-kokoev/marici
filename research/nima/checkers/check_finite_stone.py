"""Four-element Stone adapter audit: structure and all arrows, not cardinality alone."""
from pathlib import Path
from itertools import product, permutations
from datetime import datetime, timezone
import argparse
import hashlib
import json

BASE=Path(__file__).resolve().parents[1]
WORK=BASE/'adapters/finite-stone'
CORE_NAMES=['IndexedConstructorTables.agda','NativeTableRules.agda','WholePackageSigmaPi.agda',
            'WholePackageResolution.agda','TableFibrationCycle.agda','ProofRelevantCoherenceClosure.agda']

def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def core_snapshot(): return {name:sha(BASE/'agda'/name) for name in CORE_NAMES}

# Bit masks are an independent finite evaluator, not a new constructor runtime.
B=tuple(range(4))
MEET=tuple(tuple(a & b for b in B) for a in B)
JOIN=tuple(tuple(a | b for b in B) for a in B)
NEG=tuple(3 ^ a for a in B)

def atoms():
    return tuple(a for a in B if a!=0 and all(b==0 or b==a for b in B if MEET[b][a]==b))

def encode(a,points): return tuple(MEET[p][a]==p for p in points)

def decode(subset,points):
    value=0
    for use,p in zip(subset,points):
        if use: value=JOIN[value][p]
    return value

def pull(f,points):
    return tuple(decode(tuple(encode(a,points)[f[i]] for i in range(len(points))),points) for a in B)

def preserves(h):
    return (h[0]==0 and h[3]==3 and all(h[NEG[a]]==NEG[h[a]] for a in B)
        and all(h[MEET[a][b]]==MEET[h[a]][h[b]] and h[JOIN[a][b]]==JOIN[h[a]][h[b]] for a,b in product(B,repeat=2)))

def reconstruct_point_map(h,points):
    mapping=[]
    for target in points:
        candidates=[j for j,source in enumerate(points) if MEET[target][h[source]]==target]
        if len(candidates)!=1: raise ValueError('atom pullback is not a unique point')
        mapping.append(candidates[0])
    return tuple(mapping)

def check_roundtrips(points):
    if set(points)!=set(atoms()) or len(points)!=len(set(points)):
        raise ValueError('wrong atom interface')
    for a in B:
        if decode(encode(a,points),points)!=a: raise ValueError('algebra roundtrip')
    for u in product((False,True),repeat=len(points)):
        if encode(decode(u,points),points)!=u: raise ValueError('subset roundtrip')

def runtime():
    points=atoms()
    assert points==(1,2)
    check_roundtrips(points)
    maps=tuple(product(range(2),repeat=2))
    # Enumerate ALL 4^4 raw algebra maps, not just arrows generated from points.
    homs=tuple(h for h in product(B,repeat=4) if preserves(h))
    assert len(homs)==4
    assert set(homs)=={pull(f,points) for f in maps}
    for h in homs:
        f=reconstruct_point_map(h,points)
        assert pull(f,points)==h
        for a,i in product(B,range(2)):
            assert encode(h[a],points)[i]==encode(a,points)[f[i]]
    for f in maps: assert reconstruct_point_map(pull(f,points),points)==f
    assert pull((0,1),points)==B
    for f,g in product(maps,repeat=2):
        fg=tuple(f[g[i]] for i in range(2))
        pf,pg=pull(f,points),pull(g,points)
        assert pull(fg,points)==tuple(pg[pf[a]] for a in B)
    # The enumeration of points is a coordinate choice, not a preferred atom.
    for perm in permutations(points):
        check_roundtrips(perm)
        for h in homs: assert pull(reconstruct_point_map(h,perm),perm)==h
    controls=[]
    for wrong in [(1,3),(1,), (1,1)]:
        try: check_roundtrips(wrong)
        except ValueError: controls.append('wrong-atoms-'+str(wrong))
        else: raise AssertionError('bad atom schema accepted')
    f,g=(0,0),(1,0)
    pf,pg=pull(f,points),pull(g,points)
    assert pull(tuple(f[g[i]] for i in range(2)),points)!=tuple(pf[pg[a]] for a in B)
    controls.append('covariant-composition-rejected')
    swap=pull((1,0),points)
    assert swap[1]==2 and swap!=B
    assert (1).bit_count()==(2).bit_count() and 1!=2
    controls.append('cardinality-does-not-identify-atoms')
    assert not preserves((0,0,0,0))
    controls.append('nonunital-map-rejected')
    return {'algebra_elements':4,'actual_atoms':list(points),'all_raw_algebra_maps':256,
            'boolean_homomorphisms':len(homs),'point_maps':len(maps),'composition_pairs':16,
            'point_orderings':2,'controls':controls}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--freeze-core',action='store_true')
    parser.add_argument('--runtime-only',action='store_true')
    args=parser.parse_args()
    freeze=WORK/'core-freeze.json'
    if args.freeze_core:
        if freeze.exists(): raise RuntimeError('core freeze already exists; refusing to move the baseline')
        freeze.write_text(json.dumps({'schema':'marici.finite-stone.core-freeze.v1',
            'created_at':datetime.now(timezone.utc).isoformat(),'sha256':core_snapshot()},indent=2)+'\n')
        print('Frozen unchanged constructor interfaces')
        return
    assert json.loads(freeze.read_text())['sha256']==core_snapshot(), 'generic constructor changed'
    finite=runtime()
    if args.runtime_only:
        print(json.dumps(finite)); return
    kernel=json.loads((BASE/'results/finite-stone-kernel.json').read_text(encoding='utf-8-sig'))
    assert kernel['schema']=='marici.finite-stone.kernel-audit.v1'
    assert kernel['module']=='FiniteStoneAdapter' and kernel['passed'] is True
    assert kernel['fresh'] is True and kernel['inputs_stable'] is True
    assert kernel['positive_exit_code']==0 and '--ignore-interfaces' in kernel['args']
    assert {x['module'] for x in kernel['controls']}=={'StoneBadAtom','StoneBadVariance','StoneBadSymmetry'}
    assert all(x['correctly_rejected'] and x['exit_code']!=0 and x['diagnostic']=='[UnequalTerms]' for x in kernel['controls'])
    assert sha(kernel['compiler'])==kernel['compiler_sha256'].lower()
    assert sha(BASE/'checkers/check_finite_stone_kernel.ps1')==kernel['checker_sha256'].lower()
    for path,digest in kernel['source_sha256'].items(): assert sha(path)==digest.lower()
    required={str(p) for p in (WORK/'agda').glob('*.agda')} | {str(BASE/'agda'/n) for n in CORE_NAMES}
    assert required<=set(kernel['source_sha256'])
    result={'schema':'marici.finite-stone.audit.v1','status':'four-element-adapter-kernel-checked',
        'generated_at':datetime.now(timezone.utc).isoformat(),'core_unchanged':True,
        'scope':'One four-element Boolean algebra, its actual atoms, all its endomorphisms, and native constructor witness retention.',
        'finite':finite,'kernel_sha256':sha(BASE/'results/finite-stone-kernel.json'),
        'core_freeze_sha256':sha(freeze),'checker_sha256':sha(__file__),
        'general_finite_stone_theorem':False,'automatic_domain_theorem_discovery':False,
        'residuals':['General finite Boolean algebras and cross-object arrows are not formalized by this pilot.',
                     'The adapter supplies domain definitions and proofs; the constructor only retains and composes them.',
                     'No finite-to-infinite promotion, arbitrary-vocabulary reconstruction, or convergence theorem.']}
    (BASE/'results/finite-stone-audit.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))

if __name__=='__main__':
    if not __debug__: raise RuntimeError('audit assertions must remain enabled')
    main()
