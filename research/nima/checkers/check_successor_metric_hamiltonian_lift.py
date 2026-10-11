"""Whole-successor isometry and a bounded Hamiltonian realization.

The diagonal metric is induced by the EXISTING averaging decoder, given unit
root weights. A parent/child register is explicitly added for a reversible
swap realization; this does not select an autonomous infinite-stage clock.
"""
from contextlib import redirect_stdout
from pathlib import Path
import io
import json
import runpy
import sympy as S

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
with redirect_stdout(io.StringIO()):
    prior=runpy.run_path(str(HERE/'check_triangle_hamiltonian_clock_bridge.py'))
c=prior['c']; ledger=c['ledger']
checks=[]
def check(name,condition):
    if not condition:raise AssertionError(name)
    checks.append(name)

stage=ledger.root
weights=[S.Rational(1)]*len(stage.paths)
profiles=[]
for depth in range(4):
    child=ledger.successor(stage)
    E=S.Matrix(child.step_lift)
    D=S.Matrix(child.step_decoder)
    sizes=[child.parent_slots.count(i) for i in range(len(stage.paths))]
    next_weights=[weights[i]/sizes[i] for i in child.parent_slots]
    G=S.diag(*weights); Gnext=S.diag(*next_weights)
    n,m=E.cols,E.rows
    check('existing-lossless-decoder/'+str(depth),D*E==S.eye(n))
    check('decoder-induced-weighted-adjoint/'+str(depth),Gnext*E==D.T*G)
    check('full-successor-isometry/'+str(depth),E.T*Gnext*E==G)
    check('unweighted-copy-not-isometry/'+str(depth),E.T*E!=S.eye(n))
    check('positive-inherited-weights/'+str(depth),all(w>0 for w in next_weights))
    # For each child j, the adjoint identity forces exactly this diagonal
    # weight; no signed amplitude rescaling or branch probability is applied.
    check('unique-diagonal-weights-given-parent-and-decoder/'+str(depth),
          all(Gnext[j,j]==G[i,i]*D[i,j] for j,i in enumerate(child.parent_slots)))
    P=E*D
    check('detail-orthogonal-projector/'+str(depth),P*P==P and P.T*Gnext==Gnext*P)
    # Added direct-sum register: swap each parent with its child-image,
    # leaving the complementary child detail unchanged.
    swap=S.zeros(n).row_join(D).col_join(E.row_join(S.eye(m)-P))
    metric=S.diag(G,Gnext)
    check('whole-register-involution/'+str(depth),swap*swap==S.eye(n+m))
    check('whole-register-self-adjoint/'+str(depth),swap.T*metric==metric*swap)
    minus=(S.eye(n+m)-swap)/2
    check('Hamiltonian-projector/'+str(depth),minus*minus==minus)
    check('finite-Hamiltonian-endpoint/'+str(depth),S.eye(n+m)-2*minus==swap)
    # H=(pi/tau)*minus: exp(-i*tau*H)=I-2*minus=swap.
    # A positive weighted-self-adjoint projector is a positive Hamiltonian
    # after choosing tau>0. Tau is not selected by this construction.
    if depth==1:
        # Stage now has the first successor words; use actual cross products.
        values=[]
        for role in ('LR','RL'):
            payload=ledger.compose_payloads(c[role[0]],c[role[1]])
            byword=dict(zip(payload.paths,payload.values))
            v=S.Matrix([byword.get(path,0) for path in stage.paths])
            values.append(v)
            check('actual-role-norm-preserved/'+role,(v.T*G*v)[0]==((E*v).T*Gnext*(E*v))[0]==1)
            embedded=v.col_join(S.zeros(m,1))
            check('actual-whole-state-transfer/'+role,swap*embedded==S.zeros(n,1).col_join(E*v))
        difference=values[0]-values[1]
        check('actual-contrast-history-norm',(difference.T*G*difference)[0]==2)
        # Even matching the inherited tick duration would NOT identify the
        # intermediate evolution with the earlier Hamiltonian. Use the same
        # actual endpoint-amplitude reader on either register.
        def endpoint_reader(frame):
            return S.Matrix([[int(path[-1][1]==v) for path in frame.paths] for v in 'ABCD'])
        observer=endpoint_reader(stage).row_join(endpoint_reader(child))
        initial=difference.col_join(S.zeros(m,1))
        half_swap=S.eye(n+m)+(-S.I-1)*minus
        got=observer*half_swap*initial
        wanted=prior['R']*prior['B']*(S.eye(2)+prior['C'])*prior['coordinates']
        check('swap-is-not-existing-rotor-between-ticks',S.Matrix.hstack(got,wanted).rank()==2)
    profiles.append({'parent_words':n,'child_words':m,'detail_dimension':m-n,
                     'metric':'child weight = parent weight / admissible continuation count',
                     'added_register_dimension':n+m})
    stage,weights=child,next_weights

result={
    'schema':'marici.nima.successor-metric-hamiltonian-lift.v1','status':'pass','checks':checks,
    'profiles':profiles,
    'positive_result':'existing copy successor is isometric in the diagonal metric induced by its averaging decoder; a parent/child register admits an exact Hamiltonian swap realization',
    'Hamiltonian':'H=(pi/tau)*(I-swap)/2, tau>0 supplied; weighted self-adjoint and positive',
    'no_Born_claim':'weights specify a Hilbert metric, not inferred branch probabilities or a physical mass distribution; coefficients and original word counts are unchanged',
    'clock_boundary':'this swap is an added whole-register implementation, not identification with the previous rotor clock; choosing tau=pi/3 would be an extra compatibility assumption',
    'autonomy_boundary':'one supplied pair of stages is autonomous; repeated applications reverse the swap rather than advancing forever. An infinite-stage execution architecture remains additional input.',
    'uniqueness_boundary':'the diagonal metric is forced relative to the given root metric and decoder; the register enlargement, continuous Hamiltonian logarithm and rate are not uniquely selected',
}
(ROOT/'results/successor-metric-hamiltonian-lift.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(f'PASS: {len(checks)} exact whole-successor metric/Hamiltonian checks')
print('Existing decoder induces an isometric history extension without changing coefficients.')
print('Explicit positive Hamiltonian realizes a parent/child swap; not a selected global execution clock.')
