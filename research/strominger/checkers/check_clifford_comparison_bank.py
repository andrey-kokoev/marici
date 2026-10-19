# /// script
# dependencies = ["sympy"]
# ///
"""One raw reader reproduces comparisons AND reference, preserving provenance."""
from contextlib import redirect_stdout
from dataclasses import replace
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib
import io
import json
import runpy
import sys

HERE=Path(__file__).resolve().parent
if str(HERE) not in sys.path: sys.path.insert(0,str(HERE))
from clifford_comparison_bank import coefficients,from_legs,compose,ComparisonBank,algebra,memory
from retained_reference_protocol import prepare
ROOT=HERE.parent
OUT=ROOT/'results/clifford-comparison-bank.json'
OUT.unlink(missing_ok=True)
with redirect_stdout(io.StringIO()):
    convention=runpy.run_path(str(HERE/'check_raw_sewing_reference_convention.py'))
previous=convention['previous'];m=previous['m'];flat=previous['flat'];rows=m['source'];dg=m['m']
checks=[]
def check(name,condition):
    if not condition: raise AssertionError(name)
    checks.append(name)
check('prior-reference-convention-suite-passes',convention['result']['verification_status']=='pass')
for i,e in enumerate(algebra.BASIS):
    check('existing-representation-inverse/'+str(i),coefficients(algebra.matrix(e))==e)
source=prepare(algebra.UNIT,memory.ZERO16,('explicit-unit-resource','empty-bank')).advance()
reference_bank=source.state.record
check('reference-bank-generated-by-actual-source-coupling',reference_bank==memory.lift(algebra.UNIT))
check('same-raw-reader-reproduces-direct-reference',algebra.matrix(algebra.sew(reference_bank))==flat['d'])
banks=[]
for tag,size in (('a',11),('s',4)):
    for i,j in product(range(size),repeat=2):
        row=rows[len(banks)]
        X,Y=dg['values'][f'{tag}x{i}'],dg['values'][f'{tag}y{j}']
        bank=from_legs(row,X,Y)
        check('imported-leg-roundtrip/'+str(row.label),algebra.matrix(coefficients(X))==X and algebra.matrix(coefficients(Y))==Y)
        check('same-raw-reader-reproduces-comparison/'+str(row.label),bank.raw()==row.value)
        check('normalized-response-half-raw/'+str(row.label),bank.normalized()==dg['scale'](F(1,2),row.value))
        check('comparison-bank-resource-accounted/'+str(row.label),algebra.norm2(bank.bank)==algebra.norm2(coefficients(Y))*algebra.norm2(coefficients(X)))
        banks.append(bank)
check('all137-source-labels-retained',len(banks)==137 and [bank.label for bank in banks]==[row.label for row in rows])
by_label={bank.label:bank for bank in banks}
raw_average=dg['Z'];normalized_average=dg['Z']
for bank in banks:
    raw_average=dg['add'](raw_average,dg['scale'](F(1,137),bank.raw()))
    normalized_average=dg['add'](normalized_average,dg['scale'](F(1,137),bank.normalized()))
raw_residual=dg['add'](raw_average,dg['scale'](-1,flat['d']))
norm_residual=dg['add'](normalized_average,dg['scale'](-1,algebra.matrix(algebra.UNIT)))
check('original-J4-reproduced-with-one-reader',raw_residual==previous['output'].observe(m)['J4'])
check('whole-normalized-reader-contract-scales-consistently',raw_residual==dg['scale'](F(2),norm_residual))
rectangle_count=0
for tag,size,offset in (('a',11,0),('s',4,121)):
    for i,j in product(range(1,size),repeat=2):
        ij,i0,zeroj,zerozero=[banks[offset+u*size+v] for u,v in ((i,j),(i,0),(0,j),(0,0))]
        rectangle=memory.add(memory.sub(memory.sub(ij.bank,i0.bank),zeroj.bank),zerozero.bank)
        dx=memory.sub(coefficients(dg['values'][f'{tag}x{i}']),coefficients(dg['values'][f'{tag}x0']))
        dy=memory.sub(coefficients(dg['values'][f'{tag}y{j}']),coefficients(dg['values'][f'{tag}y0']))
        check('retained-bank-mixed-factorization/'+str((tag,i,j)),rectangle==algebra.tensor(dy,dx))
        check('mixed-readout-preserved/'+str((tag,i,j)),algebra.matrix(algebra.sew(rectangle))==algebra.matrix(algebra.multiply(dy,dx)))
        rectangle_count+=1
check('all109-rooted-mixed-bank-records',rectangle_count==109)
count=0
for family in m['indexed'](rows,'target').values():
    for a in family:
        for b in family:
            left,right=by_label[a.label],by_label[b.label]
            out=compose(left,right)
            check('bank-operation-square/'+str((a.label,b.label)),out.raw()==flat['chain'](b.value,flat['r'],a.value))
            check('bank-operation-retains-parents/'+str((a.label,b.label)),out.parents==(left,right) and (out.source,out.target)==(a.source,b.target))
            count+=1
check('all977-original-pair-squares',count==977)
# Unit at each target acts as identity of READABLE responses, not necessarily
# of the full16-slot bank. This is a response algebra plus retained histories.
a=banks[0]
ref=ComparisonBank(('reference',),a.target,a.target,reference_bank,('existing-unit-resource-coupling',))
right_unit=compose(a,ref)
check('reference-is-readable-unit',right_unit.raw()==a.raw())
check('unit-does-not-identify-whole-bank',right_unit.bank!=a.bank and right_unit.parents[0]==a)
# Same output bank can hide different source kernels; keep them and do not
# claim the conservative memory dynamics factors through the raw reader.
k=memory.left_rotate(memory.lift(algebra.UNIT))
hostile=replace(a,bank=memory.add(a.bank,k),provenance=('retained-kernel-control',))
check('raw-reader-blind-to-existing-hidden-return-sector',hostile.raw()==a.raw())
check('memory-exchange-sees-that-same-sector',memory.cycle(memory.ZERO4,hostile.bank)[0]!=memory.cycle(memory.ZERO4,a.bank)[0])
check('composition-retains-equal-response-distinct-kernel-parents',compose(hostile,ref).raw()==right_unit.raw() and compose(hostile,ref).parents!=right_unit.parents)
# Associativity is a readout law; expression trees remain distinct provenance.
f=next(family for family in m['indexed'](rows,'target').values() if len(family)>=3)
a,b,c=(by_label[row.label] for row in f[:3])
left=compose(compose(a,b),c);right=compose(a,compose(b,c))
check('readable-associativity',left.raw()==right.raw())
check('parenthesizations-retained',left.parents!=right.parents)
# Typed cross-target rejection is unchanged even though source coefficient
# multiplication itself exists for any pair of algebra values.
a=banks[0];b=next(bank for bank in banks if bank.target!=a.target)
try: compose(a,b)
except ValueError: check('cross-target-algebra-product-not-implicitly-admitted',True)
else: raise AssertionError('Cross-target context admitted')
result={
 'schema':'marici.strominger.clifford-comparison-bank.v1','verification_status':'pass','checks':checks,
 'single_reader':'Actual raw source sewing followed by actual Cl(2,0) matrix representation.',
 'comparisons':'137 tensor(right-leg,left-leg) banks retain source labels/ports; leg coefficients imported from frozen fixture.',
 'reference':'Actual empty-bank unit-resource coupling generates C^T(unit); same raw reader returns2I.',
 'J4_unchanged':True,'original_operation_squares':977,'retained_mixed_bank_rectangles':109,
 'response_composition':'C^T(multiply(C bank_right,C bank_left)); raw readout=Cb*(I/2)*Ca.',
 'whole_bank_identity_law':False,'conservative_exchange_factors_through_raw_reader':False,
 'retention':'All operand banks/labels/ports/provenance retained; readable associative products do not erase expression trees or kernel data.',
 'source_selection_boundary':'Comparison-leg values, unit-resource preparation, coefficient metric and operation recipe are declared inputs. The recipe is not identified with source conservative exchange or a physical instrument.',
 'physical_calibration_derived':False,'raw_policy_selected_for_physical_T9':False,
 'positive_result':'One coherent raw response convention reproduces both original comparison matrices and2I reference; no mixed readout convention is necessary.',
 'next_gate':'Bind physical preparation and actual operation to these banks while retaining kernel/resource data; matching response algebra alone is insufficient.',
 'inputs_sha256':{str(p.relative_to(ROOT.parent)).replace('\\','/'):hashlib.sha256(p.read_bytes()).hexdigest() for p in
                 (Path(__file__),HERE/'clifford_comparison_bank.py',HERE/'retained_reference_protocol.py')}}
OUT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(f'PASS: {len(checks)} single-reader source-bank/fixture checks')
print('Same raw sewing reader reproduces all137 comparisons,2I and original J4;977 readable operation squares pass.')
print('Full bank kernels, resource preparation and operation histories remain distinct from the response algebra.')
