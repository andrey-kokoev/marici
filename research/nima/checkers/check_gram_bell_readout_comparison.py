"""Exact source/interference/instrument comparison; not a Born-rule derivation.
Run collect_quantum_readout_diagnostics.py under SciPy, then this under SymPy.
"""
import ast
from contextlib import redirect_stdout
from fractions import Fraction
import hashlib
import io
from itertools import product
import json
from pathlib import Path
import runpy
import sys
from types import ModuleType
import sympy as s

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parent.parent
ARCHIVE = ROOT/'quarantine/20261007-quantum-readout-evidence'
CHECKS = []


def require(name,condition):
    if not bool(condition):
        raise AssertionError(name)
    CHECKS.append(name)


def retained(path):
    """Run an inspected predecessor completely, suppressing its sole receipt write.

Unlike a static-table surrogate, this retains all original continuation tests.
"""
    tree = ast.parse(path.read_text(encoding='utf-8'))
    removed = []
    class Capture(ast.NodeTransformer):
        def visit_Expr(self,node):
            call = node.value
            f = call.func if isinstance(call,ast.Call) else None
            if (isinstance(f,ast.Attribute) and f.attr == 'write_text'
                    and isinstance(f.value,ast.Name) and f.value.id in ('output','out','OUT')):
                removed.append(f.value.id)
                return ast.copy_location(ast.parse('_captured.append(result)').body[0],node)
            return self.generic_visit(node)
    tree = Capture().visit(tree)
    require('one-known-write-suppressed:'+path.name,len(removed) == 1)
    name = '_retained_'+path.stem
    module = ModuleType(name)
    env = module.__dict__
    env.update({'__file__':str(path),'_captured':[]})
    previous = sys.modules.get(name)
    sys.modules[name] = module  # Needed by the predecessor's dataclass annotations.
    try:
        with redirect_stdout(io.StringIO()):
            exec(compile(ast.fix_missing_locations(tree),str(path),'exec'),env)
            if not env['_captured']:
                env['main']()
    finally:
        if previous is None:
            del sys.modules[name]
        else:
            sys.modules[name] = previous
    require('one-complete-predecessor-result:'+path.name,len(env['_captured']) == 1)
    return env,env['_captured'][0]


def main():
    out = ROOT/'results/gram-bell-readout-comparison.json'
    out.unlink(missing_ok=True)
    CHECKS.clear()
    input_path = ROOT/'results/quantum-readout-transport.json'
    data = json.loads(input_path.read_text(encoding='utf-8'))
    require('transport-schema',data['schema'] == 'marici.nima.quantum-readout-transport.v1')
    expected = {'checkers/collect_quantum_readout_diagnostics.py'} | {
        'quarantine/20261007-quantum-readout-evidence/checkers/'+name
        for name in ('check_gram_selection_principle.py','check_entanglement.py')}
    require('transport-source-set',set(data['source_sha256']) == expected)
    for name,h in data['source_sha256'].items():
        require('source-current:'+name,hashlib.sha256((ROOT/name).read_bytes()).hexdigest() == h)
    entries = [line.split(maxsplit=1) for line in (ARCHIVE/'SHA256SUMS').read_text().splitlines()]
    require('seven-originals-preserved',len(entries) == 7)
    for h,name in entries:
        require('archive:'+name,hashlib.sha256((ARCHIVE/name.lstrip('*')).read_bytes()).hexdigest() == h)
    require('legacy-receipts-untouched',data['historical_receipts_unchanged'])
    require('all-ten-old-pair-expectations-fail',len(data['unasserted_zero_phase_pair_mismatches']) == 10)
    require('old-bell-readout-ignores-state',data['legacy_bell_S'] == data['state_replaced_by_product_S'])
    gp,bp = (ROOT/'checkers'/name for name in ('check_gram_selection_principle.py','check_entanglement.py'))
    gram,bell = runpy.run_path(str(gp)),runpy.run_path(str(bp))
    gram_result,bell_result = gram['verify'](),bell['verify']()
    vecs,V,G = gram['gram_data']()
    require('entire-five-filler-source-retained',vecs == data['vectors'] and list(gram['FILLERS']) == data['filler_names'])
    require('rank-four-not-rank-one',V.rank() == G.rank() == 4)
    require('first-pair-exact-old-residual',G[0,1] == s.Rational(13,14)
            and gram['N_slit_intensity'](G.extract([0,1],[0,1]),[0,0]) == s.Rational(27,7))
    require('scaled-norm-not-a-probability',s.Rational(27,14) > 1)
    packet = gram['balanced_packet'](V,[0]*5)
    W,K = packet['isometry'],packet['port']
    require('typed-five-path-isometry',W.shape == (20,5) and W.H*W == s.eye(5))
    require('balanced-port-is-a-coisometry',K.shape == (4,20) and K*K.H == s.eye(4))
    P = K.H*K
    require('complete-two-port-effects',P*P == P and (s.eye(20)-P)**2 == s.eye(20)-P)
    require('record-amplitude-attachment',s.simplify(K*W-V/s.sqrt(5)) == s.zeros(4,5))
    require('actual-five-path-click-probability',packet['click_probability'] == s.Rational(118,175))
    require('postselected-state-is-normalized',s.trace(packet['record_density']) == 1)
    # Rank of the marker Gram is not rank of a conditioned record density.
    require('rank-four-Gram-can-give-pure-record',packet['record_density'].rank() == 1)
    joint = packet['input']*packet['input'].H
    path_density = s.Matrix(5,5,lambda i,j:sum(joint[4*i+k,4*j+k] for k in range(4)))
    require('rank-four-is-a-valid-mixed-path-state',path_density == G.T/5
            and s.trace(path_density) == 1 and path_density.rank() == 4)
    require('Born-pairing-not-confined-to-rank-one',s.trace(path_density*s.ones(5)/5) == packet['click_probability'])

    raw = s.Matrix.hstack(*(s.Matrix(v) for v in vecs))
    kernel = s.Matrix([3,-4,0,3,-2])
    require('phase-family-has-no-zero-success-point',raw.rank() == 4 and raw*kernel == s.zeros(4,1)
            and kernel[2] == 0)  # Unit-modulus z_2 cannot belong to this one-dimensional kernel.
    # Necessary conditions raw*z proportional to (1,0,0,1).
    C = s.Matrix.vstack(raw[1,:],raw[2,:],raw[3,:]-raw[0,:])
    require('Bell-target-triangle-certificate',(C[0,:]+C[1,:]-C[2,:])/2 == s.Matrix([[0,0,1,2,3]]))
    # |z2+2 z3|=3 forces Re(z2 conj(z3))=1, hence z2=z3=-z4.
    x,y = s.symbols('x y',real=True)
    require('unit-circle-equality-certificate',s.solve(5+4*x-9,x) == [1]
            and (x*x+y*y-1).subs(x,1) == y*y)
    z0,z1,t = s.symbols('z0 z1 t')
    necessary = C*s.Matrix([z0,z1,-t,-t,t])
    sol = s.solve(list(necessary),(z0,z1))
    require('fixed-phase-Bell-target-impossible',sol == {z0:2*t/3,z1:2*t/3}
            and s.Rational(4,9)-1 == -s.Rational(5,9))
    # The opposite extremal Bell eigenvector needs raw*z first entry zero;
    # its actual first row is 2*z3+3*z4, impossible for unit phases.
    require('negative-extremal-state-also-excluded',raw[0,:] == s.Matrix([[0,0,0,2,3]]))
    Bop = s.kronecker_product(bell['Z'],bell['BOB'][0]+bell['BOB'][1])+s.kronecker_product(bell['X'],bell['BOB'][0]-bell['BOB'][1])
    require('fixed-CHSH-extremal-eigenspaces',Bop.eigenvals() == {2*s.sqrt(2):1,-2*s.sqrt(2):1,s.S.Zero:2}
            and Bop*s.Matrix([1,0,0,1]) == 2*s.sqrt(2)*s.Matrix([1,0,0,1])
            and Bop*s.Matrix([0,1,-1,0]) == -2*s.sqrt(2)*s.Matrix([0,1,-1,0]))

    aspect = ROOT.parent/'aspect/checkers'
    combined_path = aspect/'check_combined_bell_instrument.py'
    records_path = aspect/'check_state_effect_pairing_record_map.py'
    photon_path = ROOT/'check_photon_bell_source_packet.py'
    old_receipts = [ROOT/'results/gram-selection-principle.json',ROOT/'results/entanglement-from-gram.json',
                    aspect.parent/'results/combined_bell_instrument.json',
                    aspect.parent/'results/state_effect_pairing_record_map.json',
                    ROOT/'results/photon-bell-source-packet.json']
    before = [p.read_bytes() if p.exists() else None for p in old_receipts]
    instrument,instrument_result = retained(combined_path)
    _,record_result = retained(records_path)
    _,photon_result = retained(photon_path)
    require('complete-existing-instrument-survives',instrument_result['status'] == 'pass'
            and instrument_result['instrument_records_forgotten_to_static_table'] == 16
            and instrument_result['zxz_repeat_probability']['rational'] == '1/2')
    require('record-descent-is-still-independent',all(record_result['checks'].values())
            and record_result['disposition'] == 'pairing descent does not imply physical record descent')
    require('external-photon-packet-survives',all(v == '0' for v in photon_result['normalization_residuals'].values())
            and all(v == '0' for v in photon_result['no_signalling_residuals']))
    Q = instrument['Q']
    def encode(M):
        def coefficient(v):
            v = s.expand(v)
            b = v.coeff(s.sqrt(2)); a = s.simplify(v-b*s.sqrt(2))
            require('exact-Qsqrt2-embedding',a.is_Rational and b.is_Rational)
            return Q(Fraction(int(a.p),int(a.q)),Fraction(int(b.p),int(b.q)))
        return [[coefficient(v) for v in row] for row in M.tolist()]
    def decode(M):
        return s.Matrix([[s.Rational(q.rational.numerator,q.rational.denominator)
                          +s.sqrt(2)*s.Rational(q.root2.numerator,q.root2.denominator) for q in row] for row in M])
    st = bell['states']() | {'five_filler_record':packet['record_density']}
    for name,rho in st.items():
        table = bell['joint_table'](rho)
        for ax,bx,a,b in product(range(2),range(2),(-1,1),(-1,1)):
            pa,pb = (s.eye(2)+a*bell['ALICE'][ax])/2,(s.eye(2)+b*bell['BOB'][bx])/2
            continuation = decode(instrument['joint_instrument'](encode(rho),encode(pa),encode(pb)))
            k = s.kronecker_product(pa,pb)
            require('full-instrument-comparison:'+name+str((ax,bx,a,b)),s.simplify(continuation-k*rho*k.H) == s.zeros(4)
                    and s.simplify(s.trace(continuation)-table[ax,bx,a,b]) == 0)
    # Preserve the full original filler ACTION, not only its marker encoding.
    # The existing X+ instrument prepares |+0>; the actual twist is CNOT.
    prepared = decode(instrument['instrument'](encode(st['product00']),
                        encode((s.eye(2)+bell['X'])/2),True))
    twist = s.zeros(4)
    for j,point in enumerate(gram['CODES']):
        twist[gram['code'](gram['FILLERS']['twist'](point)),j] = 1
    require('retained-twist-is-a-unitary-action',twist.H*twist == s.eye(4))
    require('existing-instrument-plus-actual-filler-prepares-Bell',s.trace(prepared) == s.Rational(1,2)
            and twist*prepared*twist.H/s.trace(prepared) == st['bell'])
    # Explicit local unitary sends Phi+ to the predecessor's singlet.
    U = s.kronecker_product(s.eye(2),s.Matrix([[0,-1],[1,0]]))
    singlet = s.Matrix([0,1,-1,0])/s.sqrt(2)
    require('Bell-singlet-transport',U*st['bell']*U.H == singlet*singlet.H)
    for ax,bx in product(range(2),repeat=2):
        a,b = bell['ALICE'][ax],bell['BOB'][bx]
        ub = s.Matrix([[0,-1],[1,0]])
        require('transport-state-and-analyzers-together',bell['expectation'](st['bell'],a,b)
                == bell['expectation'](singlet*singlet.H,a,ub*b*ub.H))
    require('historical-and-cross-owner-receipts-untouched',before == [p.read_bytes() if p.exists() else None for p in old_receipts])
    paths = [Path(__file__).resolve(),gp,bp,input_path,ARCHIVE/'SHA256SUMS',combined_path,records_path,photon_path,
             ROOT/'photon-bell-source-packet.md',aspect.parent/'bell-sequential-polarization-instrument.md']
    paths += [ROOT/name for name in data['source_sha256']]
    result = {'schema':'marici.nima.gram-bell-readout-comparison.v1','status':'pass',
              'classification':'conditional instrument comparison constructed; legacy source dependence repaired; Born selection not derived',
              'pair_normalizations':{'raw':'27/7','coefficient_normalized':'27/14','balanced_click':'27/28'},
              'five_filler_gram_rank':4,'conditioned_record_rank':1,'five_path_click':'118/175',
              'five_filler_fixed_CHSH':str(bell['chsh'](packet['record_density'])),
              'richer_source_action_control':'existing X+ continuation on product00 followed by the actual twist filler prepares Phi+ conditionally, at probability 1/2',
              'fixed_equal_path_extremal_Bell_state':'excluded for every phase vector by unit-circle certificate, not a general Bell no-go',
              'repaired_bell_comparison':bell_result,'repaired_interference':gram_result,
              'existing_instrument':instrument_result,'independent_record_descent':record_result['disposition'],
              'checks':list(dict.fromkeys(CHECKS)),
              'source_sha256':{str(p.relative_to(REPO)).replace('\\','/'):
                               hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}}
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:result[k] for k in ('status','classification','pair_normalizations','five_filler_fixed_CHSH')},indent=2))


if __name__ == '__main__':
    main()
