"""Minimal linear predictive closure of the conditional fixed seam reader.

Retain the invisible channel separately, with exact reconstruction. Inherits
all conditional interface and orphan-transport assumptions of the source test.
"""
from contextlib import redirect_stdout
from pathlib import Path
import hashlib
import io
import json
import sympy as S
from check_joint_seam_residual_transport import main as build

HERE = Path(__file__).resolve().parent


def main():
    checks = []
    def check(name, condition):
        if not condition: raise AssertionError(name)
        checks.append(name)
    def zero(m): return S.simplify(m) == S.zeros(*m.shape)
    with redirect_stdout(io.StringIO()):
        bindings = build()
    results = []
    shift = S.Matrix([[0,1,0],[0,0,1],[1,0,0]])
    for binding in bindings:
        name = binding['deleted']
        T = binding['update']
        C = S.simplify(binding['seam_reader'])
        O = S.simplify(S.Matrix.vstack(C,C*T,C*T*T))
        check('observer/three-independent-readings/'+name, O.rank() == 3)
        check('observer/closed-update/'+name, zero(O*T-shift*O))
        check('observer/current-scalar-insufficient/'+name, S.Matrix.vstack(C,C*T).rank() == 2)
        # Explicit collision on this declared four-coordinate linear carrier.
        hidden_now = next(v for v in C.nullspace() if not zero(C*T*v))
        check('observer/collision/'+name, zero(C*hidden_now) and not zero(C*T*hidden_now))
        hidden_all = O.nullspace()
        check('observer/one-invisible-direction/'+name, len(hidden_all) == 1)
        check('observer/invisible-direction-fixed/'+name, zero(T*hidden_all[0]-hidden_all[0]))
        # Choose a conserved covector independent of the three observable rows.
        fixed_covectors = (T.T-S.eye(4)).nullspace()
        H = next(v.T for v in fixed_covectors if O.col_join(v.T).rank() == 4)
        Q = O.col_join(H)
        decode = S.simplify(Q.inv())
        check('retention/hidden-coordinate-conserved/'+name, zero(H*T-H))
        check('retention/exact-inverse/'+name, zero(Q*decode-S.eye(4)) and zero(decode*Q-S.eye(4)))
        check('retention/full-update/'+name, zero(Q*T*decode-S.diag(shift,S.eye(1))))
        # Future-reading coordinates are evaluated from the current state;
        # this is a predictive linear reader, not acquisition of future data.
        check('observer/all-time-closure-certificate/'+name, zero(T**3-S.eye(4)) and shift**3 == S.eye(3))
        metric = S.simplify(decode.conjugate().T*binding['metric']*decode)
        check('retention/metric-transport/'+name,
              zero(S.diag(shift,S.eye(1)).conjugate().T*metric*S.diag(shift,S.eye(1))-metric))
        def matrix(m): return [[str(x) for x in row] for row in m.tolist()]
        results.append({'deleted':name,'observable_dimension':3,'retained_hidden_dimension':1,
                        'observer_rows':matrix(O),'hidden_covector':matrix(H),
                        'decoder':matrix(decode),'metric':matrix(metric),
                        'same_current_different_next_witness':matrix(hidden_now),
                        'next_witness_reading':matrix(S.simplify(C*T*hidden_now))})
    files = [Path(__file__),HERE/'check_joint_seam_residual_transport.py',
             HERE.parent/'results/joint-seam-residual-transport.json']
    result = {'schema':'marici.nima.joint-seam-fixed-reader-closure.v1','status':'pass','checks':checks,
              'cases':results,'predictive_update':'(y0,y1,y2,h) -> (y1,y2,y0,h)',
              'meaning':'yk=C T^k x is a present linear function predicting a future fixed-seam '
                        'reading. h is a conserved coordinate invisible to every future seam reading.',
              'scope':'Minimal linear observation space on the four-dimensional invariant span '
                      'of the conditional geometric completion. Not a physical measurement '
                      'protocol, minimal nonlinear encoding or source-selected dynamics.',
              'input_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in files}}
    out = HERE.parent/'results/joint-seam-fixed-reader-closure.json'
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(f'PASS: {len(checks)} exact fixed-seam observer-closure checks')
    print('Three predictive readings cycle; one invisible conserved coordinate retains full recovery.')
    print('Minimality is linear and conditional on the existing candidate transport.')


if __name__ == '__main__':
    main()
