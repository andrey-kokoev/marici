"""Compare six exchange ports with the fixed-projector signed mediator gates.

No-go applies to linear intertwiners into commuting target gates. It does not
apply to the complete contact Hamiltonian (occupation need not commute with X),
port-dependent projectors, extra mediators or an independently supplied schedule.
"""
from contextlib import redirect_stdout
from itertools import combinations
from pathlib import Path
import hashlib
import io
import json
import sympy as S

from check_predictive_pair_exchange_residual import main as build

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]


def main():
    checks = []
    def check(name, condition):
        if not condition:
            raise AssertionError(name)
        checks.append(name)
    with redirect_stdout(io.StringIO()):
        binding = build()
    updates = binding['updates']
    old = binding['exchange']
    labels = tuple(updates)
    # Existing logical singlet projector, exactly rational despite sqrt(2)
    # in its normalized vector. Contact sector only; separation gives P=0.
    p = S.zeros(4)
    p[1,1] = p[2,2] = S.Rational(1,2)
    p[1,2] = p[2,1] = -S.Rational(1,2)
    x = S.Matrix([[0,1],[1,0]])
    n = S.diag(0,1)
    i4, i8 = S.eye(4), S.eye(8)
    gates = {}
    for name,control in (('contact',p),('separated',S.zeros(4))):
        plus = S.kronecker_product(i4-control,S.eye(2))+S.kronecker_product(control,x)
        minus = -S.kronecker_product(i4-control,S.eye(2))+S.kronecker_product(control,x)
        check('mediator/involutions/'+name, plus*plus == minus*minus == i8)
        check('mediator/commutation/'+name, plus*minus == minus*plus)
        check('mediator/existing-positive-generator-identity/'+name,
              (i8-plus)/2+(i8-minus)/2 == i8-S.kronecker_product(control,x))
        gates[name] = (plus,minus)
    check('boundary/occupation-does-not-commute-with-flip', n*x != x*n)
    columns, full_columns, records = [], [], []
    for a,b in combinations(labels,2):
        comm = updates[a]*updates[b]-updates[b]*updates[a]
        full = old['operators'][a]*old['operators'][b]-old['operators'][b]*old['operators'][a]
        columns.append(comm)
        full_columns.append(full)
        records.append({'ports':[a,b],'mismatch_commutator_rank':comm.rank()})
    span = S.Matrix.hstack(*columns)
    full_span = S.Matrix.hstack(*full_columns)
    check('exchange/commutator-images-span-all-mismatch', span.rank() == 6)
    check('exchange/full-commutator-rank', full_span.rank() == 6)
    check('exchange/anchor-annihilates-commutators',
          old['anchor']*full_span == S.zeros(16,full_span.cols))
    check('exchange/annihilator-exactly-anchor-rowspace',
          old['anchor'].rank() == 16 and len(full_span.T.nullspace()) == 16)
    # A concrete six-column invertible minor is a compact exact rank witness.
    pivots = span.rref()[1]
    minor = span[:,list(pivots)]
    check('certificate/invertible-minor', minor.det() != 0)
    # Commutator words need not be valid sequential endpoint histories.
    # This obstruction specifically concerns ONE global linear carrier map
    # intertwining all port operators, not endpoint-dependent maps.
    witness = next(r for r in records if r['mismatch_commutator_rank'])
    files = [Path(__file__), HERE/'check_predictive_pair_exchange_residual.py',
             HERE.parent/'results/predictive-pair-exchange-residual.json',
             ROOT/'research/voevodsky/checkers/check_proton_electron_contact_binding.py',
             ROOT/'research/voevodsky/finite-record-mediator-constructor.md']
    result = {
        'schema':'marici.nima.exchange-contact-gate-comparison.v1','status':'pass',
        'checks':checks,'port_pairs':records,
        'commutator_image_rank':span.rank(),
        'rank_certificate':{'column_indices':list(pivots),
                            'minor':[[str(x) for x in row] for row in minor.tolist()],
                            'determinant':str(minor.det())},
        'example_noncommuting_pair':witness,
        'conclusion':'Every single global linear intertwiner from the six exchange updates '
                     'to commuting target operators annihilates all six mismatch directions. '
                     'On the full 22-dimensional source it factors through the conserved anchor.',
        'scope':'Fixed common contact projector and signed mediator gates, or words in their '
                'commuting algebra. Not the full occupation-plus-contact Hamiltonian, '
                'endpoint-dependent intertwiners, port-varying controls or a no-go for interaction. '
                'Commutator comparison is an operator-law test, not asserted to be an admitted '
                'sequential seed word. No target gate assignment or physical policy selected.',
        'input_sha256':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}}
    output = HERE.parent/'results/exchange-contact-gate-comparison.json'
    output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(f'PASS: {len(checks)} exact exchange/contact gate comparison checks')
    print('Commutator images span all six mismatch directions.')
    print('A global linear map to fixed commuting mediator gates loses the entire active mismatch.')
    print('Scope excludes the full noncommuting mediator Hamiltonian and endpoint-dependent maps.')


if __name__ == '__main__':
    main()
