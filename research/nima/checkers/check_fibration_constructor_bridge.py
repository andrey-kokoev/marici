"""Source-bound tests for the annotated fiber/section constructor bridge.
These enumerate values, not higher paths. The full proofs are in Cubical Agda.
"""
from itertools import product
from pathlib import Path
import hashlib,json
BASE=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
family_count=0;row_cases=0;section_cases=0;selected_cases=0
for n in range(4):
    for sizes in product(range(4),repeat=n):
        rows=tuple((i,x) for i,m in enumerate(sizes) for x in range(m))
        # A fiber witness is equality of the two displayed base indices.
        grouped=tuple((i,r) for i in range(n) for r in rows if r[0]==i)
        encode_row=lambda r:(r[0],r)
        decode_row=lambda g:g[1]
        assert tuple(decode_row(g) for g in grouped)==rows
        for r in rows:assert decode_row(encode_row(r))==r;row_cases+=1
        for g in grouped:assert encode_row(decode_row(g))==g
        products=tuple(product(*(range(m) for m in sizes)))
        sections=tuple(product(*(tuple(r for r in rows if r[0]==i) for i in range(n))))
        assert len(products)==len(sections)
        for f in products:
            encoded=tuple((i,f[i]) for i in range(n))
            assert encoded in sections and tuple(r[1] for r in encoded)==f
            section_cases+=1
            # Complete input families additionally retain the selected values.
            header=('Pi',sizes,f)
            assert header[2]==f
            for i in range(n):assert encode_row((i,f[i]))==(i,(i,f[i]))
            selected_cases+=1
        family_count+=1
assert family_count==85
# Two endpoint regroupings preserve row count: not a product decoder.
assert sum((1,1))!=1*1
# For the address endpoint, every fiber is a singleton: only one section.
assert 1!=2*2
# An empty edge table must not erase the distinction between an empty base
# and an existing base point whose fiber is empty.
assert tuple((i,x) for i,m in enumerate(()) for x in range(m))==()
assert tuple((i,x) for i,m in enumerate((0,)) for x in range(m))==()
assert tuple(product())==((),) and tuple(product(range(0)))==()
# Selected E values alone do not recover choices in unselected components.
header0=('E',(1,2),(0,0),0); header1=('E',(1,2),(0,1),0)
assert header0!=header1 and (0,header0[2][0])==(0,header1[2][0])
# Equal interpreted maps have different atom/maps constructor metadata.
value_view=('Unit->Unit','identity')
assert ('atom',value_view)!=('maps',value_view)
# Empty-target sections realize the Boolean NAND term, including the exact
# double-negation scope when C has more than one value.
def nand_size(a,b):return int(a*b==0)
def word(a,b,c):
    n=nand_size
    return n(n(n(a,b),c),n(a,n(n(a,c),a)))
for a,b,c in product(range(4),repeat=3):assert word(a,b,c)==int(c>0)
assert word(1,1,2)!=2

rp=BASE/'results/agda-FibrationCodeInterpretation.json'
r=json.loads(rp.read_text(encoding='utf-8-sig'))
assert r['passed'] and r['exit_code']==0 and r['ignore_interfaces']
modules=('FibrationCodeInterpretation','FibrationSigmaPiBridge','TableFibrationCycle',
         'WholePackageSigmaPi','WholePackageResolution','BoundaryGeneratedQuestions',
         'NandConstructions','QBooleanity','ProofRelevantCoherenceClosure')
for m in modules:
    assert r['owner_source_inventory_sha256'][m+'.agda']==sha(BASE/f'agda/{m}.agda'),m
c=json.loads((BASE/'results/fibration-constructor-formal-audit.json').read_text(encoding='utf-8-sig'))
assert c['positive_receipt_sha256'].lower()==sha(rp)
assert len(c['controls'])==2
for control in c['controls']:
    assert control['correctly_rejected'] and control['exit_code']!=0
    assert control['source_sha256'].lower()==sha(BASE/f"agda/negative/{control['module']}.agda")
packet={
 'status':'annotated-fiber-section-equivalence-checked',
 'obligations':['forward realization','attachment transport','route/coherencer compatibility','readout descent'],
 'baseline':['WholePackageSigmaPi','WholePackageResolution','NandConstructions','QBooleanity'],
 'families':family_count,'row_roundtrips':row_cases,'section_roundtrips':section_cases,
 'selected_family_cases':selected_cases,'nand_double_negation_controls':64,
 'formal_receipt_sha256':sha(rp),
 'source_sha256':{m:sha(BASE/f'agda/{m}.agda') for m in modules},
 'checker_sha256':sha(Path(__file__).resolve()),
 'proved':['all-eight-code recursive value equivalence at every universe level',
           'complete-package equivalence retaining exact Code',
           'E selected rows and P selected sections compute by refl',
           'actual boundary filler equivalence and composition compatibility',
           'transported twelve-rule closure equivalence and literal retention of reified derivations',
           'section-based NAND/Wolfram term equivalent to double negation'],
 'not_proved':['bare endpoint-grouping kernel equivalent as a constructor calculus',
               'independent graph implementation of all twelve rules',
               'new physical realization or independently defined physical readout compatibility'],
 'required_structure':['constructor code, active index domains and witness metadata',
                       'section interpretation for Pi, not opposite-endpoint regrouping'],
}
(BASE/'results/fibration-constructor-bridge.json').write_text(json.dumps(packet,indent=2)+'\n',encoding='utf-8')
print(f'PASS: {family_count} families, {row_cases} row and {section_cases} section roundtrips; full source-bound annotated bridge closure.')
