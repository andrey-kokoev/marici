"""Compare the actual LR/RL path families with their existing exchange action.

Evaluate each word by the already-bound ordered primitive exchanges, then
apply the SAME final-endpoint aggregation used by the rotor attachment.
Operator-valued sums are a comparison of retained branch evaluations, NOT
an assertion that their sum is one physical pulse or a chosen superposition.
"""
from contextlib import redirect_stdout
from pathlib import Path
import hashlib
import io
import json
import runpy
import sympy as S

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
with redirect_stdout(io.StringIO()):
    exchange=runpy.run_path(str(HERE/'check_seed_port_exchange_binding.py'))
    source=runpy.run_path(str(HERE/'check_actual_triangle_branch_composition.py'))
ops=exchange['operators']; registry=exchange['registry']; anchor=exchange['anchor']
mismatch=exchange['B']; metric=exchange['metric']; ledger=source['ledger']
vertices='ABCD'; dim=22
M=S.zeros(4)
for label,(a,b) in registry.items():M[vertices.index(b),vertices.index(a)]+=1
left=ledger.compose_payloads(source['L'],source['R'])
right=ledger.compose_payloads(source['R'],source['L'])
whole=ledger.retain_payload(ledger.root,(1,)*6)
checks=[]
def check(name,condition):
    if not condition:raise AssertionError(name)
    checks.append(name)

check('same-actual-seed-ports',dict((label,(a,b)) for label,a,b in source['PACKETS'])==registry)


def word_action(path):
    value=S.eye(dim)
    for edge in path:
        label=edge[2]
        if (edge[0],edge[1])!=registry[label]:raise AssertionError('port endpoint mismatch')
        value=ops[label]*value
    return value


def evaluate(lp,rp):
    out={v:S.zeros(dim) for v in vertices}
    for sign,p in ((1,lp),(-1,rp)):
        for word,coefficient in zip(p.paths,p.values):
            out[word[-1][1]]+=sign*coefficient*word_action(word)
    return out


def extend(values):
    out={v:S.zeros(dim) for v in vertices}
    for label,(a,b) in registry.items():out[b]+=ops[label]*values[a]
    return out


def stacked(values):return S.Matrix.vstack(*(values[v] for v in vertices))

levels=[]
d0=S.Matrix([1,-1,-1,1])
for n in range(7):
    evaluated=evaluate(left,right)
    if levels:
        check('actual-word-composition-square/'+str(n),evaluated==extend(levels[-1]))
    levels.append(evaluated)
    dn=M**n*d0
    for j,v in enumerate(vertices):
        check('conserved-anchor-retains-cyclic-reading/'+str(n)+'/'+v,anchor*evaluated[v]==dn[j]*anchor)
    left,right=ledger.compose_payloads(left,whole),ledger.compose_payloads(right,whole)

polynomial=stacked(levels[0])+stacked(levels[1])+stacked(levels[2])
return_defect=stacked(levels[3])-stacked(levels[0])
full_turn_defect=stacked(levels[6])-stacked(levels[0])
check('full-exchange-evaluation-not-primitive-third-root',polynomial!=S.zeros(88,22))
check('full-exchange-evaluation-does-not-return-after-three',return_defect!=S.zeros(88,22))
check('mismatch-sector-dimension',mismatch.rank()==6)
fixed=S.Matrix.hstack(*mismatch.nullspace())
check('common-fixed-sector-dimension',fixed.cols==16)
check('matched-sector-fixed-by-every-port',all(op*fixed==fixed for op in ops.values()))
check('matched-sector-has-cubic-recurrence',polynomial*fixed==S.zeros(88,16))
check('matched-sector-has-three-return',return_defect*fixed==S.zeros(88,16))
check('cubic-recurrence-kernel-exactly-matched-sector',polynomial.rank()==6)
check('three-return-kernel-exactly-matched-sector',return_defect.rank()==6)
check('matched-sector-has-full-six-update-return',full_turn_defect*fixed==S.zeros(88,16))
check('full-turn-return-kernel-exactly-matched-sector',full_turn_defect.rank()==6)
# Inclusion of a 16-dimensional space in either 22-column kernel, together
# with rank six, proves equality of kernels for ALL initial internal states.
probe=exchange['excited']  # Existing AB-record fixture, not a fitted new input.
probe_residual=full_turn_defect*probe
check('existing-AB-record-probe-has-nonzero-full-turn-residual',probe_residual!=S.zeros(88,1))

# Existing continuous pulse: S_i(theta)=I+(exp(-i theta)-1)P_i.
# Test the generator, not only its pi endpoint. No angle calibration to the
# rotor is inserted here; endpoint failure already rules out the proposed
# all-angle equality of these endpoint-resolved full internal readings.
for label,op in ops.items():
    projector=(S.eye(dim)-op)/2
    check('prior-continuous-Hamiltonian-projector/'+label,projector*projector==projector)
    check('prior-Hamiltonian-self-adjoint/'+label,projector.T*metric==metric*projector)
    check('prior-pi-pulse-endpoint/'+label,S.eye(dim)-2*projector==op)
    check('anchor-fixed-at-every-angle/'+label,anchor*projector==S.zeros(16,22))
    check('matched-sector-idle-at-every-angle/'+label,projector*fixed==S.zeros(22,16))

nonzero=[(vertices[i//22],i%22,str(v)) for i,v in enumerate(probe_residual) if v!=0]
result={
    'schema':'marici.nima.rotor-exchange-source-operation-comparison.v1','status':'pass','checks':checks,
    'comparison':'actual LR/RL word family, existing per-primitive exchange evaluation, actual final-endpoint aggregation',
    'residual_ranks':{'cubic_polynomial':int(polynomial.rank()),'three_return':int(return_defect.rank()),'six_update_full_turn':int(full_turn_defect.rank())},
    'exact_return_domain':'ker(r-F^T H y), dimension 16: common matched states fixed by every exchange',
    'active_sector_dimension':6,
    'existing_probe_first_nonzero_residual':nonzero[0],
    'existing_probe_nonzero_residual_entries':len(nonzero),
    'positive_connection':'the conserved anchor retains the same cyclic endpoint contrast on every input and is fixed by each continuous pulse',
    'negative_connection':'endpoint-resolved full internal exchange evaluations return after three OR six updates only on the inactive matched sector; active back-action is not the current rotor orbit',
    'scope':'exact verdict for this existing source/word/endpoint comparison, not a no-go for every possible coupled Hamiltonian realization',
    'not_assumed':['a branch sum is a physical pulse','new state preparation','new coupling','new time scale','identification of two Hamiltonians merely by periodic endpoints'],
    'input_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in
        [Path(__file__),HERE/'check_seed_port_exchange_binding.py',HERE/'check_actual_triangle_branch_composition.py']},
}
(ROOT/'results/rotor-exchange-source-operation-comparison.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(f'PASS: {len(checks)} exact rotor/exchange source-operation comparison checks')
print('Three- AND six-update return defects have rank 6; both kernels are EXACTLY the common fixed sector.')
print('Conserved-anchor reading retains the rotor recurrence for all inputs; active exchange back-action does not.')
print('Existing AB-record probe first nonzero residual:',nonzero[0])
