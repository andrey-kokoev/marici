"""Transport actual role-labelled successor counts through the old rung API.

Reuses its TWO policies and SAME fixed reference. This is a new ten-word
input to that API, not an identification with the historical 137-row input.
Count -> scalar times identity is explicit, not a physical calibration.
"""
from contextlib import redirect_stdout
from pathlib import Path
from fractions import Fraction as F
import io
import hashlib
import json
import runpy

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
with redirect_stdout(io.StringIO()):
    composition=runpy.run_path(str(HERE/'check_actual_triangle_branch_composition.py'))
    tower=runpy.run_path(str(HERE/'check_rung_transport_diagram.py'))
Row=tower['Row']; indexed=tower['indexed']; unindex=tower['unindex']
promote=tower['incoming_promotion']; leaves=tower['leaves']
read=tower['read_at_four']; scale=tower['scale']; I=tower['I']
words=composition['words']; registry=composition['registry']
proof_path=ROOT/'results/agda-NativeTriangleCompositionSuccessor.json'
proof=json.loads(proof_path.read_text(encoding='utf-8-sig'))
formal=ROOT/'agda/NativeTriangleCompositionSuccessor.agda'
assert proof['passed'] and proof['ignore_interfaces'] and proof['inputs_stable_during_check']
assert proof['source_sha256']==hashlib.sha256(formal.read_bytes()).hexdigest()

checks=[]
def check(name,condition):
    if not condition:raise AssertionError(name)
    checks.append(name)


def make_rows(role):
    # Full ten-word comparison frame, with the role's occurrence indicator.
    # Zeros are values in this explicitly common frame, not executed absent
    # products or fabricated measurements of an unavailable experiment.
    return tuple(Row(('leaf',role,i,word),('vertex',registry[word[0]][0]),
                     ('vertex',registry[word[-1]][1]),scale(value,I))
                 for i,(word,value) in enumerate(zip(words,composition['products'][role])))


def endpoint_counts(view):
    original=leaves(unindex(view))
    return tuple(sum(row.value[0][0] for row in original if row.target==('vertex',v)) for v in 'ABCD')


observed={}
for policy in ('inherited','common'):
    observed[policy]={}
    for role in ('LR','RL'):
        source=make_rows(role)
        def T(rows):return promote(promote(rows,1,policy),2,policy)
        upper=indexed(unindex(indexed(T(source),'source')),'target')
        left=indexed(unindex(indexed(source,'source')),'target')
        lower=indexed(T(unindex(left)),'target')
        check('both-routes/'+policy+'/'+role,upper==lower)
        check('all-role-labelled-leaves/'+policy+'/'+role,leaves(unindex(upper))==tuple(sorted(source,key=lambda r:r.label)))
        check('fixed-reference-not-changed/'+policy+'/'+role,tower['physical_reference'].rung==4 and tower['physical_reference'].value==scale(2,I))
        expected=(F(1),F(0),F(0),F(1)) if role=='LR' else (F(0),F(1),F(1),F(0))
        check('actual-endpoint-reader/'+policy+'/'+role,endpoint_counts(upper)==expected)
        check('aggregate-reader-exact/'+policy+'/'+role,read(upper)==scale(F(-9,5),I))
        observed[policy][role]={'aggregate':[[str(v) for v in row] for row in read(upper)],
                                 'endpoint_counts':list(map(str,endpoint_counts(upper))),
                                 'outer_rows':len(unindex(upper))}
    check('aggregate-erases-role-contrast/'+policy,observed[policy]['LR']['aggregate']==observed[policy]['RL']['aggregate'])
    check('retained-endpoint-reader-distinguishes/'+policy,observed[policy]['LR']['endpoint_counts']!=observed[policy]['RL']['endpoint_counts'])
for role in ('LR','RL'):
    check('policy-independent-leaf-readout/'+role,
          observed['inherited'][role]['endpoint_counts']==observed['common'][role]['endpoint_counts'])

result={
    'schema':'marici.nima.triangle-successor-rung-reader.v1','status':'pass','checks':checks,
    'native_boundary':'actual application extension derives the composed object from explicit input, composition-function and reader seeds; no automatic physical selection claimed',
    'row_adapter':'ten-word common comparison frame; role indicator times the existing 2x2 identity, unit member masses',
    'observations':observed,
    'result':'both role channels reach rung4 losslessly, but the unchanged aggregate fixed-reference reader gives -9I/5 for both; a declared leaf-target reader retains the difference',
    'scope':'compatibility with existing transport API and reference, not identification with the original 137-row shared-leg fixture or physical readout',
    'formal_receipt_sha256':hashlib.sha256(proof_path.read_bytes()).hexdigest(),
    'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
}
(ROOT/'results/triangle-successor-rung-reader.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(f'PASS: {len(checks)} exact successor-to-rung reader checks; native derivation receipt verified')
print('Retained endpoint contrast survives both transport policies.')
print('The unchanged aggregate reader is blind: LR and RL both read -9I/5.')
