"""Fresh generic extension theorems, native instance and finite scope controls."""
from pathlib import Path
from itertools import product, permutations
import hashlib
import json
import shutil
import subprocess

ROOT=Path(__file__).resolve().parents[3]
BASE=ROOT/'research/strominger'
LIB=Path.home()/'tools/cubical-agda/cubical-0.9'
EXE=shutil.which('agda')
assert EXE and LIB.is_dir()
sources=[BASE/'agda/CoherentDependentExtensions.agda',
         BASE/'agda/CoherentExtensionNativeInstance.agda',
         BASE/'agda/negative/BadBaseOnlyExtensionComparison.agda',
         BASE/'agda/RetainedFeedbackCovariance.agda',
         BASE/'agda/RetainedPackageFeedback.agda',
         ROOT/'research/nima/agda/WholePackageResolution.agda',
         ROOT/'research/nima/agda/WholePackageSigmaPi.agda',Path(__file__).resolve()]
hashes={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sources}
common=[EXE,'--transliterate','-i',str(BASE/'agda'),'-i',str(ROOT/'research/nima/agda'),'-i',str(LIB)]
positive=subprocess.run(common+['--ignore-interfaces',str(sources[1])],capture_output=True,text=True,timeout=300)
text=positive.stdout+positive.stderr
(BASE/'results/coherent-dependent-extensions-positive.log').write_text(text,encoding='utf-8')
assert positive.returncode==0 and 'UnsupportedIndexedMatch' not in text,text[-5000:]
negative=subprocess.run(common+['-i',str(BASE/'agda/negative'),str(sources[2])],capture_output=True,text=True,timeout=120)
text=negative.stdout+negative.stderr
(BASE/'results/coherent-dependent-extensions-negative.log').write_text(text,encoding='utf-8')
assert negative.returncode!=0 and 'Bool' in text and 'Unit' in text,text
profiles=[]
for n in range(4):
    for widths in product(range(3),repeat=n):
        total=[(x,w) for x in range(n) for w in range(widths[x])]
        projected=[x for x,w in total]
        bijective=len(set(projected))==len(projected) and set(projected)==set(range(n))
        assert bijective==all(width==1 for width in widths)
        profiles.append({'base_size':n,'fiber_sizes':widths,'total_size':len(total),'projection_bijective':bijective})
assert len(profiles)==40
# An abstract total/base equivalence is not equivalence of the projection.
counterexample=next(p for p in profiles if p['fiber_sizes']==(0,2))
assert counterexample['total_size']==counterexample['base_size']==2
assert not counterexample['projection_bijective']
# Base swap and compatible fiber permutations compose on retained pairs.
F=(1,2);G=(2,1);H=F
states=[(x,w) for x in range(2) for w in range(F[x])]
checks=0
for p,q in product(tuple(permutations(range(2))),repeat=2):
    def first(z):
        x,w=z;return 1-x,p[w] if x==1 else w
    def second(z):
        y,w=z;return 1-y,q[w] if y==0 else w
    for z in states:
        x,w=z
        expected=(x,q[p[w]] if x==1 else w)
        assert second(first(z))==expected
        checks+=1
# Reassociation preserves all fields despite nonconstant, possibly empty,
# second-stage fibers. This is not a uniform Cartesian-product count.
nested=[((x,w),v) for x in range(2) for w in range(F[x]) for v in range((x+w)%3)]
combined=[(x,(w,v)) for (x,w),v in nested]
assert [((x,w),v) for x,(w,v) in combined]==nested
for path,h in hashes.items():assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==h
result={'status':'pass','fresh_agda_exit':positive.returncode,'negative_exit':negative.returncode,
        'negative_diagnostic':text.strip(),'finite_projection_profiles':profiles,
        'same_cardinality_non_equivalent_projection':counterexample,
        'finite_transport_composition_checks':checks,'dependent_reassociation_records':len(nested),
        'formal_results':['Base/fiber maps lift with identity, composition and associativity laws',
                          'Base/fiber equivalences lift to equivalences of complete extensions',
                          'Identity/composition/associativity laws for lifted equivalences',
                          'Supplied paths and two-paths between comparisons are retained',
                          'Dependent reassociation and its transport naturality square',
                          'Projection is an equivalence iff every witness fiber is contractible',
                          'Empty fibers block extensions at their boundary',
                          'Explicit source-admission evidence compiles through native rules and survives reification',
                          'Existing retained-feedback comparison realizes the generic extension square'],
        'scope':['Admission policy, tasks and actual witnesses remain explicit',
                 'No general task discovery, uniqueness of policy, or arbitrary higher filler generation',
                 'No all-dimensional categorical coherence or native feedback forward-involution theorem',
                 'Noncontractible fiber obstructs its projection, not every abstract equivalence between total and base'],
        'source_hashes':hashes}
(BASE/'results/coherent-dependent-extensions.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':'pass','fresh_agda_exit':positive.returncode,'negative_exit':negative.returncode,
                  'finite_projection_profiles':len(profiles),'composition_checks':checks}))
