# /// script
# dependencies = ["sympy"]
# ///
"""Audit full-state admissibility of the prior readable bank product."""
from contextlib import redirect_stdout
from fractions import Fraction as F
from pathlib import Path
import hashlib
import io
import json
import runpy
import sys

HERE=Path(__file__).resolve().parent
if str(HERE) not in sys.path: sys.path.insert(0,str(HERE))
import joint_bank_extraction as joint
from clifford_comparison_bank import algebra,memory
ROOT=HERE.parent
OUT=ROOT/'results/joint-bank-extraction.json'
OUT.unlink(missing_ok=True)
with redirect_stdout(io.StringIO()):
    prior=runpy.run_path(str(HERE/'check_clifford_comparison_bank.py'))
checks=[]
def check(name,condition):
    if not condition: raise AssertionError(name)
    checks.append(name)
check('single-reader-response-suite-still-passes',prior['result']['verification_status']=='pass')
M=memory.transpose(joint.PRODUCT_COLUMNS)
Gram=memory.mm(M,memory.transpose(M))
check('joint-product-readout-Gram4I',Gram==tuple(tuple(F(4*(i==j)) for j in range(4)) for i in range(4)))
check('product-readout-rank4',memory.rank(M)==4)
check('252-kernel-directions-must-remain',256-memory.rank(M)==252)
for i,value in enumerate(algebra.BASIS):
    bank=joint.lift(value)
    check('derived-normalized-readout-is-coisometric/'+str(i),joint.readout(bank)==value)
    check('derived-lift-is-isometric/'+str(i),algebra.norm2(bank)==algebra.norm2(value))
    check('unscaled-product-reader-has-gain2/'+str(i),joint.product_readout(bank)==memory.scale(value,F(2)))

# Direct two-bank recipe is homogeneous quadratic, while any composition of
# prior linear orthogonal updates on a direct-sum state is linear.
u=memory.lift(algebra.UNIT)
base=algebra.multiply(memory.readout(u),memory.readout(u))
scaled=algebra.multiply(memory.readout(memory.scale(u,F(2))),memory.readout(memory.scale(u,F(2))))
check('direct-sum-source-linearity-obstruction',scaled==memory.scale(base,F(4)) and scaled!=memory.scale(base,F(2)))
# Even a separable prepared joint bank can violate a proposed unscaled
# norm-conservative extraction. No entangled hostile is needed.
x=memory.add(algebra.UNIT,algebra.E1)
t=memory.lift(x);prepared=joint.tensor(t,t)
product=joint.product_readout(prepared)
check('separable-preparation-resource-accounted',algebra.norm2(prepared)==4)
check('unscaled-product-output-exceeds-input-budget',algebra.norm2(product)==8>algebra.norm2(prepared))
# A generic joint bank attains the exact operator gain2.
max_gain=joint.lift(algebra.UNIT)
check('unscaled-extraction-cannot-have-positive-conservative-remainder',algebra.norm2(max_gain)==1 and algebra.norm2(joint.product_readout(max_gain))==4)

# Constructive CONDITIONAL alternative: swap carrier with the normalized
# joint-readable sector, retaining the full kernel, on4+256 coordinates.
zero256=(F(0),)*256
operator_columns=[]
for i,v in enumerate(memory.basis(260)):
    state=(v[:4],v[4:])
    out=joint.exchange(*state)
    operator_columns.append(out[0]+out[1])
    check('full-state-extraction-is-involutive/'+str(i),joint.exchange(*out)==state)
    check('full-state-coefficient-budget-preserved/'+str(i),sum(map(algebra.norm2,out))==sum(map(algebra.norm2,state)))
    remainder=memory.sub(state[1],joint.lift(joint.readout(state[1])))
    check('joint-kernel-is-unread-and-retained/'+str(i),joint.readout(remainder)==memory.ZERO4 and memory.sub(out[1],joint.lift(state[0]))==remainder)
check('full-exchange-matrix-is-symmetric',memory.transpose(tuple(operator_columns))==tuple(operator_columns))
# By linearity E^2=I on the full basis and E=E^T give E^T E=I on every state.
# Check source/return cross terms.
for i,e in enumerate(algebra.BASIS):
    lifted=joint.lift(e)
    check('carrier-readable-swap/'+str(i),joint.exchange(e,zero256)==(memory.ZERO4,lifted) and joint.exchange(memory.ZERO4,lifted)==(e,zero256))

# Original fixture response is recovered only through an EXPLICIT gain-bearing
# observation, NOT by identifying the extracted carrier with unscaled output.
for index in (0,1,11,12,120,121,136):
    left=prior['banks'][index];right=prior['banks'][index]
    prepared=joint.tensor(right.bank,left.bank)
    carrier,outbank=joint.exchange(memory.ZERO4,prepared)
    target=prior['compose'](left,right).raw()
    check('fixture-response-requires-explicit-readout-conversion/'+str(index),algebra.matrix(memory.scale(carrier,F(4)))==target)
    check('fixture-full-joint-resource-retained/'+str(index),algebra.norm2(carrier)+algebra.norm2(outbank)==algebra.norm2(prepared))
check('joint-preparation-not-supplied-by-exchange',joint.exchange(memory.ZERO4,zero256)==(memory.ZERO4,zero256))
result={
 'schema':'marici.strominger.joint-bank-extraction.v1','verification_status':'pass','checks':checks,
 'original_recipe_obstructions':['Quadratic two-bank output is not a linear source update on their direct sum.',
                                 'Unscaled readable product is not a contraction even on a separable prepared joint bank.'],
 'prepared_joint_space':256,'readable_rank':4,'retained_kernel_dimension':252,
 'constructive_alternative':'D=M/2 is coisometric; E(x,t)=(Dt,D^T x+(I-D^T D)t) is an involutive orthogonal260-coordinate exchange.',
 'response_conversion':'Original raw reference-return response=matrix(4*extracted_carrier), while extracted_carrier=M(joint_bank)/2.',
 'normalization_derived_from_source_metric':True,
 'conservative_full_state_completion_constructed':True,
 'original_unscaled_recipe_conservative':False,'physical_instrument_realized':False,
 'preparation_boundary':'The joint tensor bank is an explicit input; exchange does not prepare it from two separate resources. Tensor preparation and apparatus/readout gain need their own resource contract.',
 'not_claimed':['No identification with original20-coordinate schedule','No physical detector/amplifier or clock selection',
                'No resource-free joint preparation/reset','No change to pinned software T9 or its J4'],
 'next_gate':'Supply source-admitted joint preparation and the physical reading of the gain-bearing observation, or reject this recipe as the intended interaction.',
 'inputs_sha256':{str(p.relative_to(ROOT.parent)).replace('\\','/'):hashlib.sha256(p.read_bytes()).hexdigest() for p in
                 (Path(__file__),HERE/'joint_bank_extraction.py',HERE/'clifford_comparison_bank.py')}}
OUT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(f'PASS: {len(checks)} full-state bank-composition/extraction checks')
print('Original recipe is not a conservative linear update; normalized260-coordinate extraction retains252 kernel directions.')
print('Joint preparation and gain-bearing physical observation remain explicit missing source operations.')
