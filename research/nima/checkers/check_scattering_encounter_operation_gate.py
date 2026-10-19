"""Selected encounter: abstract metric embedding versus sourced operations."""
import importlib.util
import json
from hashlib import sha256
from pathlib import Path
import sys
import sympy as S

ROOT = Path(__file__).resolve().parents[3]
HOME = ROOT / 'research/nima'
CONTRACT = HOME / 'contracts/scattering-encounter-operation-gate.v1.json'


def require(ok, message):
    if not ok:
        raise ValueError(message)


def sha(p):
    return sha256(p.read_bytes()).hexdigest()


def main():
    c = json.loads(CONTRACT.read_text())
    paths = {CONTRACT, Path(__file__)}
    def load(name):
        p = ROOT / name
        paths.add(p)
        return json.loads(p.read_text())
    prior = load(c['prior_gate_result'])
    require(prior['status'] == 'pass', 'prior gate not passing')
    narrative_updates = []
    for name, expected in prior['source_sha256'].items():
        p = ROOT / name
        actual = sha(p)
        if actual != expected:
            require(name == 'research/strominger/retained-hamiltonian-observer.md'
                    and actual == 'b23158a3a827d3ddabff2f05aec992ad9ba573cdc6f252297591ac1c84bea0bd',
                    'prior source drift: ' + name)
            narrative_updates.append({'path': name, 'previous_sha256': expected, 'current_sha256': actual,
                                      'review': 'Freshly read added controllability follow-up; computation below reconstructs current matrices. Prior receipt is not revalidated or rewritten.'})
        paths.add(p)
    adapter = load(c['native_adapter_result'])
    typed = load(c['typed_channels_result'])
    for receipt in (adapter, typed):
        require(receipt['verification_passed'], 'native source not passing')
        for name, expected in receipt['source_hashes'].items():
            p = (ROOT / 'research/voevodsky' / name).resolve()
            require(p.is_relative_to(ROOT) and sha(p) == expected, 'native pin drift')
            paths.add(p)
    sys.path.insert(0, str(ROOT / 'research/voevodsky/checkers'))
    import check_native_spinor_pair_adapter as n
    spec = importlib.util.spec_from_file_location('coefficient_source', ROOT / c['coefficient_constructor'])
    coeff = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(coeff)
    cl = coeff.classify()
    labels = tuple(e for e in cl['edges'] if e != 'AB')
    _, a = coeff.native_generator(cl, labels)
    z = -a*a
    plow = z*(128*S.eye(137)-z)/3072
    index = next(i for i in range(137) if plow[:, i] != S.zeros(137,1))
    raw = plow[:, index]
    v = raw / S.sqrt((raw.T*raw)[0])
    omega = S.sqrt(32)
    w = a*v/omega
    plane = S.Matrix.hstack(v, -w)
    j = S.Matrix([[0,1],[-1,0]])
    eq = lambda x,y: all(S.simplify(t)==0 for t in x-y)
    require(eq(plane.T*plane,S.eye(2)), 'abstract embedding metric')
    require(eq(a*plane,plane*(omega*j)), 'abstract embedding generator')
    require(eq(plane.T*(a.T*a/2)*plane,16*S.eye(2)), 'energy Hessian pullback')
    require(eq(plane.T*(a/2)*plane,omega*j/2), 'skew form pullback')
    # Four disjoint response columns give B=I4 tensor plane in interleaved
    # real/imaginary input convention; these small identities prove all8 columns.
    actions = []
    for perm in cl['group']:
        relabel = dict(zip(cl['vertices'], perm))
        mapped = lambda e: relabel[e[0]]+relabel[e[1]]
        if set(map(mapped,labels)) != set(labels):
            continue
        r11 = S.Matrix(11,11,lambda i,k:int(labels[i]==mapped(labels[k])))
        r4 = S.Matrix(4,4,lambda i,k:int(cl['vertices'][i]==relabel[cl['vertices'][k]]))
        u = S.SparseMatrix(S.diag(S.kronecker_product(r11,r11),S.kronecker_product(r4,r4)))
        require(u*u == S.eye(137), 'native-preserving relabelling not involutive')
        actions.append({'permutation_images': ''.join(perm), 'square_is_identity': True,
                        'commutes_with_generator': u*a == a*u,
                        'reverses_generator': u*a == -a*u})
    require(len(actions)==2, 'native-preserving S4 action set changed')
    ps = n.matrix(typed['input_scalar_projector'])
    pv = n.matrix(typed['input_vector_projector'])
    identity = n.eye(4)
    require(n.mm(ps,ps)==ps and n.mm(pv,pv)==pv and n.add(ps,pv)==identity, 'channel projectors')
    two = n.matrix(typed['two_output_map'])
    three = n.matrix(typed['three_output_map'])
    # Verify supports and retain the actual Grams rather than renormalizing vertices.
    require(n.mm(two,ps)==two and n.mm(three,pv)==three, 'typed vertex support changed')
    g2 = n.mm(n.adj(two),two)
    g3 = n.mm(n.adj(three),three)
    cases=[]
    for report in adapter['adapter_reports']:
        d=n.matrix(report['effective_cycle_D'])
        pair=n.kron(d,n.conjugate_matrix(d))
        require(n.power(pair,5)==identity, 'native pair fifth-power identity')
        nontrivial=n.power(pair,2)!=identity
        require(nontrivial, 'expected native cycle obstruction absent')
        require(n.mm(pair,ps)==ps and n.mm(pair,pv)==n.mm(pv,pair), 'native scalar/vector action')
        require(n.mm(n.adj(pair),n.mm(g2,pair))==g2 and n.mm(n.adj(pair),n.mm(g3,pair))==g3, 'vertex Gram covariance')
        cases.append({'chirality':report['chirality'],'doublet_option':report['doublet_option'],
                      'pair_cycle_fifth_power_identity':True,'pair_cycle_square_not_identity':True,
                      'pair_cycle_not_scalar':True,
                      'pair_energy': report['pair_conditional_core_energy'],
                      'native_scalar_vector_and_vertex_grams_preserved':True})
    paths.add(ROOT/c['coefficient_constructor'])
    paths.update(ROOT/s for s in c['source_notes'])
    result={'schema':'marici.scattering.encounter-operation-result.v1','status':'pass',
            'conjecture_disposition':'blocked_at_existing_target_cycle_operation',
            'abstract_embedding':{'plane_source_column':index,'v':[str(x) for x in v],'minus_w':[str(-x) for x in w],
                'real_dimension':8,'metric':'I8','angular_frequency':'sqrt(32)',
                'energy_hessian':'16 I8','skew_form':'(sqrt(32)/2) direct_sum_4 [[0,1],[-1,0]]',
                'interpretation':'Mathematical coordinate witness only. Rate sqrt32/e and energy-Hessian conversion16/e are supplied separately for encounter energy e; not physical calibration or shared-leg preparation.'},
            'native_preserving_target_relabellings':actions,'native_cases':cases,
            'reviewed_narrative_updates':narrative_updates,
            'two_vertex_gram':n.encoded(g2),'vector_three_vertex_gram':n.encoded(g3),
            'obstruction':'For every existing native-preserving relabelling U, U^2=I. If UB=BDpair and B is injective, B(Dpair^2-I)=0 is impossible. All four source cases have nontrivial order5 pair action. A same-clock free flow on a scalar-energy encounter is scalar; because Dpair fixes Ps but acts nontrivially on Pv, it cannot equal such a scalar flow either.',
            'channel_transport_status':'deferred_after_upstream_operation_failure; no target vertices manufactured by Bdagger pullback',
            'scope':'Existing native-preserving simultaneous S4 relabellings (even granting the noncommuting one) or same-clock free flow. Not a theorem about arbitrary added symmetries, controls, response-column mixing, enlarged source laws or nonlinear maps.',
            'new_control_audit':'shared-leg-controllability-audit reports only conditional common gain and preparation variations, not an admitted fifth-order encounter action; not independently replayed here',
            'full_native_complement_discarded':False,'physical_scattering_explained':False,'root_outcome':None,
            'source_sha256':{p.relative_to(ROOT).as_posix():sha(p) for p in sorted(paths)}}
    output=HOME/'results/scattering-encounter-operation-gate.json'
    output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print(json.dumps({k:result[k] for k in ('status','conjecture_disposition','native_preserving_target_relabellings','channel_transport_status','root_outcome')},indent=2))


if __name__=='__main__':
    main()
