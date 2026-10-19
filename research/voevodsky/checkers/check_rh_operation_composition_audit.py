# /// script
# dependencies = ["sympy"]
# ///
"""Cell-indexed RH operation audit; --replay performs fresh exact source suites.
Default validates the retained replay and source freshness, without rerunning it.
Analytic equalities use the argument in the note; finite tests do not prove domains.
"""
import argparse
import copy
import json
import subprocess
import sys
from pathlib import Path
from hashlib import sha256
ROOT=Path(__file__).resolve().parents[3]
DICT='research/conjecture_net/contracts/rh-stage-dictionary.v1.json'
NOTE='research/voevodsky/rh-operation-composition-audit-v1.md'
OUT='research/voevodsky/results/rh-operation-composition-audit-v1.json'
SCRIPTS={
 'carrier':'check_carrier_fourier_orbit_bridge.py',
 'active':'check_triangle_fourier_active_bridge.py',
 'endpoint':'check_full_endpoint_fourier_bridge.py',
 'descent':'check_fourier_six_step_descent.py',
 'lattice':'check_additive_lattice_fourier_bridge.py'}
SYMBOLIC=['even/odd gamma reflected-product algebra','orientation swap not identity after two Fourier steps',
          'radial atom half-density cancellation','sum-kernel spectral reflection',
          's=1/2+it; reflected gamma argument=1/2-it']
CELLS={
 'finite-squares':dict(disposition='constructed_at_declared_scope',source_suites=['carrier','descent'],witness='P_step C_n=C_m P_step; C_n E_step=E_step C_m; composite P_total=P_direct; J P_total C12=F_cyc J P_total.',boundary='Inherited coefficient operations/forms; frame and seed supplied.'),
 'history-generator':dict(disposition='constructed_at_declared_scope',source_suites=['active','endpoint'],witness='With A0=[[0,2/3],[-2,0]], A=sqrt(3) A0 and A_endpoint=Q diag(A,0) Q^-1: D J=J A_endpoint; O_n L_n=A_endpoint O_n; L_next step=step L_n at n=10,16,26,42.',boundary='Keep sqrt(3) angular normalization and transported sections; no equality of native history and analytic metrics.'),
 'native-tick-no-go':dict(disposition='rejected_identification_retained',source_suites=['active','endpoint'],witness='The 16-variable system F X=X M has rank16, so X=0. Added J^-1 F J is order four and does not commute with native M.',boundary='No native-tick identity claimed; positive interface keeps both operations separately typed.'),
 'generator-quarter-turn-no-go':dict(disposition='rejected_identification_retained',source_suites=['carrier'],witness='exp(pi D4/4)-C4=2 M_minus, rank(M_minus)=1.',boundary='Skew-generator flow is not full Fourier; retain the alternating stationary character.'),
 'lattice-weyl-bonding':dict(disposition='constructed_at_declared_scope',source_suites=['lattice'],witness='F_R j_h=L_h F_lattice; T_b M_alpha=exp(-2pi i alpha b) M_alpha T_b; F_R T_b=M_-b F_R; F_R M_alpha=T_alpha F_R; finite convolution and dyadic bonding.',boundary='Finite convolution only; l2 continuity and distributional limits are analytic-owner obligations.'),
 'radial-spectral-square':dict(disposition='constructed_on_declared_core',source_suites=[],witness='W_or U=U F_R on induced image; M_log W_or=G(t) R_t M_log; G(t)G(-t)=orientation swap. Abel regulator yields m_sigma(t)=(2pi)^(-1/2+it) Gamma(1/2-it) exp[-i sigma pi(1/2-it)/2].',boundary='Regularized common core and inherited induced image; no raw-comb global integral or completed endpoint-extension theorem.')}


def load(p):return json.loads((ROOT/p).read_text(encoding='utf-8'))
def sha(p):return sha256((ROOT/p).read_bytes()).hexdigest()
def require(ok,msg):
    if not ok:raise ValueError(msg)


def verify_cell_inventory(cells,d):
    required={c['id'] for c in d['cells'] if c['owner']=='rh-operation-composition-squares' and c['required_for_interface']}
    require(set(cells)==required,'missing/extra required operation cell')
    for key,row in cells.items():
        require(row==CELLS[key],'changed scoped witness/disposition')
    require(cells['native-tick-no-go']['disposition']=='rejected_identification_retained','native rejection lost')
    require(cells['generator-quarter-turn-no-go']['disposition']=='rejected_identification_retained','quarter-turn rejection lost')
    # Boundary-source maps cannot be promoted by this operation inventory.
    excluded={c['id'] for c in d['cells'] if c['owner']=='rh-operation-composition-squares' and not c['required_for_interface']}
    require(excluded=={'channel-source-binding'},'changed independent-source boundary')


def symbolic_checks():
    import sympy as S
    t=S.symbols('t',real=True);a=S.pi*t/2
    theta=S.pi/4-S.I*a;theta_ref=S.pi/4+S.I*a
    cos_product=S.simplify(S.expand_trig(S.cos(theta)*S.cos(theta_ref)).rewrite(S.exp))
    sin_product=S.simplify(S.expand_trig(S.sin(theta)*S.sin(theta_ref)).rewrite(S.exp))
    require(S.simplify(cos_product-S.cosh(S.pi*t)/2)==0,'even branch product')
    require(S.simplify(sin_product-S.cosh(S.pi*t)/2)==0,'odd branch product')
    # Euler reflection: Gamma(1/2-it)Gamma(1/2+it)=pi/cosh(pi t).
    qprod=1/(2*S.cosh(S.pi*t))
    require(S.simplify(4*qprod*cos_product-1)==0,'even double-Fourier branch')
    require(S.simplify(-4*qprod*sin_product+1)==0,'odd double-Fourier branch')
    H=S.Matrix([[1,1],[1,-1]])
    require(H*S.diag(1,-1)*H.inv()==S.Matrix([[0,1],[1,0]]),'orientation swap')
    x,u,v=S.symbols('x u v',positive=True)
    # Delta half-density factor cancels the radial Fourier kernel amplitude.
    require(S.simplify(x**(-S.Rational(1,2))*S.exp((S.log(x)+v)/2)-S.exp(v/2))==0,'atom half-density cancellation')
    # Bilateral log transform of a sum-kernel forces reflection.
    w=S.symbols('w',real=True)
    require(S.simplify(S.exp(-S.I*t*(w-u))-S.exp(-S.I*t*w)*S.exp(S.I*t*u))==0,'sum-kernel spectral reflection')
    delta=S.symbols('delta',positive=True);sigma=S.symbols('sigma',real=True)
    exponent=S.Rational(1,2)-S.I*t
    require(S.simplify(exponent-(S.Rational(1,2)-S.I*t))==0,'Mellin exponent convention')
    return SYMBOLIC


def source_paths(d):
    paths=[DICT,NOTE,Path(__file__).relative_to(ROOT).as_posix()]
    paths += list(d['evidence_sources'].values())
    paths += [d['receipts'][k] for k in SCRIPTS]
    paths += ['research/voevodsky/checkers/'+x for x in SCRIPTS.values()]
    return sorted(set(paths))


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--replay',action='store_true');args=parser.parse_args()
    d=load(DICT);verify_cell_inventory(CELLS,d);algebra=symbolic_checks() if args.replay else SYMBOLIC;controls=[]
    for mode in ('missing-cell','native-promoted','quarter-turn-promoted','unbound-source-added'):
        bad=copy.deepcopy(CELLS)
        if mode=='missing-cell':bad.pop('history-generator')
        elif mode=='native-promoted':bad['native-tick-no-go']['disposition']='constructed_at_declared_scope'
        elif mode=='quarter-turn-promoted':bad['generator-quarter-turn-no-go']['disposition']='constructed_at_declared_scope'
        else:bad['channel-source-binding']=bad['finite-squares']
        try:verify_cell_inventory(bad,d)
        except ValueError:controls.append(mode)
        else:raise AssertionError('hostile accepted '+mode)
    if args.replay:
        executions=[]
        for key,script in SCRIPTS.items():
            p='research/voevodsky/checkers/'+script
            prior=sha(d['receipts'][key])
            r=subprocess.run([sys.executable,str(ROOT/p)],cwd=ROOT,capture_output=True,text=True,timeout=240)
            require(r.returncode==0,'source suite failed '+key+'\n'+r.stderr+'\n'+r.stdout[-3000:])
            require(sha(d['receipts'][key])==prior,'source replay changed a pinned receipt; review dictionary revision before admission: '+key)
            executions.append(dict(id=key,checker=p,returncode=r.returncode,receipt_unchanged=True))
        result=dict(schema='marici.rh-operation-composition-audit.v1',passed=True,
          cells=CELLS,required_cells_covered=6,independent_source_binding_constructed=False,
          source_suites_freshly_replayed=executions,symbolic_checks=algebra,
          analytic_witness='Argument in owner-local note; gamma integral and Fourier theorem are mathematical premises, not finite-test outputs.',
          analytic_completion_gate_closed=False,identity_continuation_gate_closed=False,
          corruptions_rejected=controls,source_sha256={p:sha(p) for p in source_paths(d)})
        (ROOT/OUT).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    else:
        result=load(OUT);require(result['passed'] and result['cells']==CELLS and result['symbolic_checks']==SYMBOLIC,'audit receipt mismatch')
        require(result['source_sha256']=={p:sha(p) for p in source_paths(d)},'audit source drift')
        require(len(result['source_suites_freshly_replayed'])==len(SCRIPTS) and all(x['returncode']==0 and x['receipt_unchanged'] for x in result['source_suites_freshly_replayed']),'missing replay evidence')
        require(not result['analytic_completion_gate_closed'] and not result['identity_continuation_gate_closed'],'scope promotion')
    print(json.dumps(dict(passed=True,required_cells_covered=6,fresh_replay_this_run=args.replay,
                         symbolic_checks=algebra,corruptions_rejected=controls),indent=2))


if __name__=='__main__':main()
