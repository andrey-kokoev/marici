"""Check RH stage/map/cell inventory, not compatibility or completion proofs."""
import argparse
import copy
import json
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
MODEL='research/conjecture_net/contracts/rh-stage-dictionary.v1.json'
NOTE='research/voevodsky/rh-stage-dictionary-v1.md'
OUT='research/voevodsky/results/rh-stage-dictionary-v1.json'
OWNERS={'rh-operation-composition-squares','rh-identity-continuation-transport','rh-analytic-domain-completion-transport'}
SOURCES={
 'carrier':'research/voevodsky/carrier-fourier-orbit-bridge-v1.md',
 'descent':'research/voevodsky/fourier-six-step-descent-v1.md',
 'endpoint':'research/voevodsky/full-endpoint-fourier-bridge-v1.md',
 'active':'research/voevodsky/triangle-fourier-active-bridge-v1.md',
 'riemann':'research/voevodsky/riemann-comb-specialization-v1.md',
 'lattice':'research/voevodsky/additive-lattice-fourier-bridge-v1.md',
 'radial':'research/voevodsky/oriented-log-radialization-is-a-faithful-strong-dual-realization-of-the-fourier-port-orbit.md',
 'mellin':'research/voevodsky/mellin-diagonalization-of-the-oriented-radial-fourier-kernel-recovers-the-tate-gamma-matrix.md',
 'wg':'research/strominger/wg-software-operations-composition-prior-search.md',
 'packet':'research/strominger/wg-transport-packet-geometry-prior-search.md',
 'attachment':'research/strominger/wg-I-squared-rehydration-correction.md',
 'half-phase':'research/strominger/wg-half-phase-prior-research-search.md'}
RECEIPTS={k:'research/voevodsky/results/'+v+'.json' for k,v in {
 'carrier':'carrier-fourier-orbit-bridge-v1','descent':'fourier-six-step-descent-v1',
 'endpoint':'full-endpoint-fourier-bridge-v1','active':'triangle-fourier-active-bridge-v1',
 'riemann':'riemann-comb-specialization-v1','lattice':'additive-lattice-fourier-bridge-v1'}.items()}


def require(x,m):
    if not x:raise ValueError(m)
def load(p):return json.loads((ROOT/p).read_text(encoding='utf-8'))
def sha(p):return sha256((ROOT/p).read_bytes()).hexdigest()


def initial():
    stages=[];maps=[];cells=[]
    def stage(i,t,domain,ops,choices,retained,context,evidence):
        stages.append(dict(id=i,type=t,domain=domain,operations=ops,supplied_choices=choices,retained_data=retained,context=context,evidence=evidence))
    def arrow(i,s,t,formula,domain,kernel,choices,evidence):
        maps.append(dict(id=i,source=s,target=t,formula=formula,domain=domain,kernel_or_retention=kernel,supplied_choices=choices,evidence=evidence))
    def cell(i,owner,ms,claim,status,evidence,gate):
        cells.append(dict(id=i,owner=owner,maps=ms,claim=claim,evidence_state=status,evidence=evidence,remaining_audit=gate,required_for_interface=status!='open_binding',transport_proved_by_inventory=False))
    for d in (12,11,10,9,8,6,4):
        stage('coeff-'+str(d),'R^'+str(d), 'Full finite coefficient space in the declared parity-resolved frame.',
          ['C_d (order-four permutation transport)','D_d=P_d D12 E_d (inherited continuous generator)','inherited metric/form/energy'],
          ['fixed Gram 10I12+J12','parity-resolved frame and ordered reduction schedule'],
          'At each reduction retain N_step x and provenance; hidden energy need not be zero.',
          'Coefficient model, not physical preparation or calibrated Hilbert norm.', ['descent','carrier'])
    stage('history','H_n: retained labelled-history coefficient spaces','n in {10,16,26,42}, the four actual stages in endpoint receipt; no extrapolation to all histories.',
      ['native extension step_n','lifted continuous L_n','active and full endpoint readers'],
      ['initial metric sections and complementary basis policy'], 'Endpoint-invisible Nfull_n and full history retained.', 'History source is not identified with twelve-arrow carrier.', ['endpoint','active'])
    stage('endpoint','R^4 in A,B,C,D endpoint order','Image of rank-four O_n at the four audited stages.',
      ['native M with polynomial (x^2+x+1)(x^2-x-1)','A_endpoint=Q diag(A,0,0) Q^-1','added J^-1 F J'],
      ['Q=[R,V] complementary chart','metric-correct J; added Fourier is not native M'],
      'O_n loses endpoint-invisible histories; complementary coordinates recover two omitted active-reader dimensions.',
      'Declared analytic chart; pulled-back analytic Gram not identified with native history Gram.', ['endpoint'])
    stage('cyclic','R^4 in cyclic order 0,1,2,3','Full coefficient four-port representation.',
      ['F_cyc','F_cyc-F_cyc^-1'], ['J maps AD,CA,DB,BC to 0,3,1,2'],
      'All characters 1,-1,i,-i retained; alternating character is generator-stationary.', 'Finite coefficient presentation.', ['carrier','endpoint'])
    stage('comb','Span{P_a,C_-a,P_(1-a),C_a} in S\'(R)','0<a<1, a != 1/2; distribution/test pairing.',
      ['additive Fourier exp(-2pi ixy)','reflection','skew Fourier generator'],
      ['shift a','AD seed assignment','self-dual Fourier normalization'],
      'Zero atom separately tracked; full source requires Nx archive.', 'Transported coefficient norm is not L2 norm of combs.', ['carrier'])
    stage('radial','Oriented signed log half-density test/dual image plus zero endpoint','Induced domain from nonzero additive distributions; not all growing logarithmic tests.',
      ['W_or=U F_R U^-1 on induced image','orientation swap on half-turn'],
      ['two orientations','half-density normalization','endpoint extension'],
      'Separate zero atom and full reconstructed additive distribution; do not sum orientations.', 'Compact-support test-space chart and induced dual; full endpoint extension still needs audit.', ['radial','lattice'])
    stage('mellin','Two-component spectral test/dual presentation','Common regularized core and continued dual pairing; raw comb global Mellin integral not assumed convergent.',
      ['G(t) followed by t -> -t','even/odd gamma branches'],
      ['log Fourier exp(-itu)','s=1/2+it versus reflected 1-s','regularization/continuation'],
      'Both orientations and separate endpoint data.', 'No Green Hilbert graph membership inferred.', ['mellin','carrier'])
    stage('lattice','Finite packets on Z, with declared l2(Z) and Z^D extensions','Finite support for algebraic convolution; l2 extension only for admitted maps.',
      ['shift','character modulation','finite convolution','dyadic bonding n -> 2n'],
      ['mesh h>0','dyadic refinement','channel set D','heat time t>0'],
      'Channel labels, mesh/time and zero endpoint.', 'Independent canonical channel source; no selected channel/carrier identification.', ['lattice'])
    stage('torus','Trigonometric packets / L2 normalized torus','Finite character sums; l2 Fourier extension.',
      ['lattice Fourier','character multiplication','periodic lift'], ['normalized torus measure','evaluation pairing'],
      'Mesh for periodic real lift.', 'Periodic lifts are tempered, not generally L2(R).', ['lattice'])
    stage('real-distribution','S\'(R) additive realization','Finite atoms, sampled l2 sequences and locally L2 periodic lifts under specified embeddings.',
      ['F_R','translation','modulation','finite-packet convolution'], ['additive positions hn, not exp(n)'],
      'Zero atom and induced tests.', 'Multichannel version is R^D; one-dimensional formulas do not select a channel.', ['lattice'])
    stage('riemann-boundary','Span{Delta,delta_0,1} in S\'(R)','Unshifted self-dual comb with endpoint correction.',
      ['F Delta=Delta','F delta_0=1; F 1=delta_0'], ['unit unshifted self-dual lattice'],
      'Coefficient-sum specialization has kernel dimension 3; original labelled coefficients/history retained separately.', 'Boundary extension is not three native controls.', ['riemann'])
    stage('theta','theta(t), t>0 with endpoint monomials 1,t^-1/2','Gaussian distribution pairing and reciprocal heat-time relation.',
      ['theta(t)=t^-1/2 theta(1/t)','D_s=2t d/dt+s on boundary modes'],
      ['Gaussian exp(-pi t x^2)','self-dual measure','heat scale'],
      'Zero subtraction and both endpoint modes.', 'Analytic choices not forced by finite carrier.', ['riemann'])
    stage('completed-zeta','Lambda(s), xi(s) as analytic functions','Initial Re(s)>1 Mellin formula; entire tail after split at t=1; xi continued entire.',
      ['reflection s -> 1-s','endpoint cancellation s(s-1)/2'],
      ['half-theta counting','s-dependent Gaussian Mellin convention'],
      'Polar endpoint packet and constant 1/2.', 'No all-tests positivity or zero-location claim.', ['riemann'])
    pairs=list(zip((12,11,10,9,8,6),(11,10,9,8,6,4)))
    reduction=[]
    for n,m in pairs:
        i=f'reduce-{n}-{m}';reduction.append(i)
        arrow(i,'coeff-'+str(n),'coeff-'+str(m),'x -> P_step x, with x=E_step P_step x+N_step x','Full coefficient source.',
          'Kernel N_step retained; inherited energy not assigned zero.', ['parity-resolved prefix choice'], ['descent'])
    arrow('carrier-chart','coeff-4','cyclic','J','Full four-coefficient space.','Invertible coordinate permutation.', ['basis order'], ['carrier'])
    arrow('comb-attachment','cyclic','comb','B_a c=sum c_j v_j','Generic a as declared.','Injective on four coefficients; full twelve source needs archive.', ['a','seed and normalization'], ['carrier'])
    arrow('history-endpoint','history','endpoint','O_n','Four audited retained stages.','n-4 endpoint-invisible directions retained.', ['actual history/section policy'], ['endpoint'])
    arrow('endpoint-chart','endpoint','cyclic','J=T Q^-1','Full endpoint space.','Invertible; intertwines continuous generator, not native M.', ['complementary chart V'], ['endpoint'])
    arrow('oriented-radial','comb','radial','U on R^times plus retained zero endpoint','Induced test/dual image.','Faithful away from zero; zero separately retained.', ['orientation and half-density'], ['radial','carrier'])
    arrow('spectral-mellin','radial','mellin','M_log','Common regularized core and specified continued dual pairing.','No raw-comb global integral assumed.', ['log Fourier convention and continuation'], ['mellin'])
    arrow('lattice-fourier','lattice','torus','c -> sum c_n exp(-2pi in theta)','Finite packets and l2 extension.','Fourier on normalized torus.', ['torus measure'], ['lattice'])
    arrow('atom-lift','lattice','real-distribution','j_h c=sum c_n delta_(hn)','Finite packets and sampled l2 extension.','Not an L2(R) atom realization.', ['h and channel source'], ['lattice'])
    arrow('periodic-lift','torus','real-distribution','L_h f(y)=f(hy)','Finite sums / L2 torus via local L2 periodic lift.','Not generally L2(R).', ['mesh h'], ['lattice'])
    arrow('real-radial','real-distribution','radial','U j_h, with U delta_(hn)=|hn|^-1/2 delta_(log|hn|)','Nonzero atoms plus endpoint, induced tests.','Zero stays separate; orientation retained.', ['h and induced domain'], ['lattice'])
    arrow('unshifted-specialization','cyclic','riemann-boundary','c -> (sum c_j) Delta','Specialized a=0, not a generic independent basis.','Rank one; kernel dimension 3, composed twelve kernel dimension 11.', ['unshifted unit lattice'], ['riemann'])
    arrow('theta-pairing','riemann-boundary','theta','theta(t)=<Delta,exp(-pi t x^2)> with endpoint subtraction','t>0.','Readout does not retain arbitrary full distribution; boundary corrections explicit.', ['Gaussian and measure'], ['riemann'])
    arrow('theta-mellin-completion','theta','completed-zeta','Lambda=1/2 integral (theta-1)t^(s/2) dt/t; xi=s(s-1)Lambda/2','Re(s)>1 initially, then split/continue.','Polar endpoint packet retained; xi constant 1/2.', ['heat/Mellin normalization'], ['riemann'])
    cell('finite-squares','rh-operation-composition-squares',reduction+['carrier-chart','comb-attachment'],'Permutation/generator squares and six-step composite equals direct P.','recorded_finite_checks',['descent','carrier'],'Replay/bind all cell IDs to exact checked matrices and inherited form conventions.')
    cell('history-generator','rh-operation-composition-squares',['history-endpoint','endpoint-chart','comb-attachment'],'D J=J A_endpoint and coherent sections at four actual stages.','recorded_finite_checks',['endpoint','active'],'Bind actual stages and keep continuous versus discrete operations distinct.')
    cell('native-tick-no-go','rh-operation-composition-squares',['history-endpoint','endpoint-chart'],'No fixed nonzero solution F X=X M; Fourier chart does not identify native extension.','recorded_rejection',['endpoint'],'Preserve rejected candidate; exclude tick identity from positive interface claims.')
    cell('generator-quarter-turn-no-go','rh-operation-composition-squares',['carrier-chart','comb-attachment'],'exp(pi D4/4)-C4=2M_minus; skew flow is not full Fourier tick.','recorded_finite_checks',['carrier'],'Retain alternating character and operation distinction.')
    cell('lattice-weyl-bonding','rh-operation-composition-squares',['lattice-fourier','atom-lift','periodic-lift'],'F_R j_h=L_h F; finite convolution, Weyl phase and dyadic bonding commute.','recorded_finite_checks',['lattice'],'Bind algebraic finite checks; do not silently extrapolate convolution to all l2 packets.')
    cell('radial-spectral-square','rh-operation-composition-squares',['oriented-radial','spectral-mellin','real-radial'],'M_log W_or=G(t) R_t M_log and W_or U j_h=U L_h F.','recorded_analytic_argument',['mellin','radial','lattice'],'Bind gamma/reflection conventions and analytic domains to completion-owner ledger.')
    cell('hidden-reconstruction','rh-identity-continuation-transport',reduction+['carrier-chart','comb-attachment'],'Full source reconstructed from analytic quotient and hidden records.','recorded_finite_checks',['descent','carrier'],'Audit permitted future operations and attachment meaning, not only readout recovery.')
    cell('history-retention','rh-identity-continuation-transport',['history-endpoint','endpoint-chart'],'I=Efull Pfull+Nfull and coherent hidden extension.','recorded_finite_checks',['endpoint'],'Check licensed continuation squares and unchanged original active generator.')
    cell('riemann-quotient','rh-identity-continuation-transport',['unshifted-specialization','history-endpoint','endpoint-chart'],'Rank-one specialization loses odd/alternating ports; same readout can have distinct native futures.','recorded_finite_checks',['riemann'],'Specify task-relative equivalence and explicit equal-readout/different-future witnesses.')
    cell('generic-domain','rh-analytic-domain-completion-transport',['comb-attachment'],'Distributional independence and test pairing, not comb L2 norm.','recorded_analytic_argument',['carrier'],'Audit shift limits, domains and finite coefficient norm versus analytic pairing.')
    cell('radial-endpoint-domain','rh-analytic-domain-completion-transport',['oriented-radial','real-radial'],'Nonzero oriented chart is faithful; zero atom is a separate endpoint.','recorded_analytic_argument',['radial','lattice'],'Specify complete induced tests/dual and the Fourier-coupled endpoint extension.')
    cell('mellin-domain','rh-analytic-domain-completion-transport',['spectral-mellin'],'Regularized gamma integral and continued common test/dual core.','recorded_analytic_argument',['mellin','carrier'],'Audit extension/limit witnesses; t, s and reflected argument remain distinct.')
    cell('lattice-continuity','rh-analytic-domain-completion-transport',['atom-lift','lattice-fourier','periodic-lift'],'l2-to-tempered extension; Gaussian Riemann-sum/Fourier limit for fixed heat time.','recorded_analytic_argument',['lattice'],'Specify continuity, topology and tails; finite checks alone do not certify limits.')
    cell('theta-completion','rh-analytic-domain-completion-transport',['unshifted-specialization','theta-pairing','theta-mellin-completion'],'Zero-atom exchange, polar endpoints, analytic continuation, normalization and xi constant.','recorded_analytic_argument',['riemann'],'Bind boundary algebra receipts separately from Poisson/Mellin continuation argument.')
    cell('channel-source-binding','rh-operation-composition-squares',['atom-lift','comb-attachment'],'Canonical channel lattice is not identified with twelve-arrow carrier.','open_binding',['lattice'],'Separate channel-carrier-source-map task; not required to pretend existing independent routes share one source.')
    cell('one-dimensional-binding','rh-identity-continuation-transport',['atom-lift','unshifted-specialization'],'Multichannel source does not select one zeta coordinate automatically.','open_binding',['lattice','riemann'],'Separate one-dimensional-source-selection task; retain this interface boundary.')
    paths=list(SOURCES.values())+list(RECEIPTS.values())
    return dict(schema='marici.rh-stage-dictionary.v1',inventory_only=True,stages=stages,maps=maps,cells=cells,
      evidence_sources=SOURCES,receipts=RECEIPTS,source_sha256={p:sha(p) for p in paths},
      owner_nodes=sorted(OWNERS),
      boundaries=['No new common-source map, form equality, all-tests positivity or RH proof.','No physical normalization, detector or preparation admission.','Source-search notes are reuse pointers, not new compatibility proofs.'],
      optional_control_applicability=[dict(id='relation-attachments',sources=['attachment'],status='unbound_to_RH',rule='I^2 source-module attachment obligations require a typed multiplicative source binding; a scalar observer kernel need not be an ideal.'),
                                     dict(id='half-phase-composition',sources=['half-phase'],status='unbound_to_RH',rule='Apply local-root noncomposition only if those actual packet operations are selected; no universal fractional WG inferred.')],
      separate_open_tasks=['channel-carrier-source-map','one-dimensional-source-selection','successor-form-candidate','weil-form-comparison'])


def validate(m):
    require(m['inventory_only'] is True,'inventory promoted to transport proof')
    require(m['schema']=='marici.rh-stage-dictionary.v1','schema')
    s={r['id']:r for r in m['stages']};a={r['id']:r for r in m['maps']};c={r['id']:r for r in m['cells']}
    require(len(s)==len(m['stages']) and len(a)==len(m['maps']) and len(c)==len(m['cells']),'duplicate ID')
    require(set(m['owner_nodes'])==OWNERS,'owner set')
    require(set(m['evidence_sources'])==set(SOURCES) and m['evidence_sources']==SOURCES and m['receipts']==RECEIPTS,'evidence inventory drift')
    require(set(m['source_sha256'])==set(SOURCES.values())|set(RECEIPTS.values()),'pin coverage')
    for p,h in m['source_sha256'].items():require(sha(p)==h,'source drift '+p)
    for rows,fields in ((s,['type','domain','operations','supplied_choices','retained_data','context']), (a,['source','target','formula','domain','kernel_or_retention','supplied_choices'])):
        for row in rows.values():
            require(all(row[k] for k in fields),'missing typed inventory field')
            require(row['evidence'] and set(row['evidence'])<=set(SOURCES),'unbound evidence')
    for row in a.values():require(row['source'] in s and row['target'] in s,'unknown stage')
    covered=set();owner_coverage=set()
    for row in c.values():
        require(row['owner'] in OWNERS,'unknown child owner');owner_coverage.add(row['owner'])
        require(row['maps'] and set(row['maps'])<=set(a),'unknown map');covered.update(row['maps'])
        require(row['evidence_state'] in ('recorded_finite_checks','recorded_analytic_argument','recorded_rejection','open_binding'),'cell state')
        require(row['claim'] and row['remaining_audit'] and row['evidence'] and set(row['evidence'])<=set(SOURCES),'unactionable cell')
        require(row['transport_proved_by_inventory'] is False,'table used as proof')
        require(row['required_for_interface'] == (row['evidence_state'] != 'open_binding'),'boundary binding made an interface prerequisite')
    require(covered==set(a) and owner_coverage==OWNERS,'unowned map or audit category')
    require(c['native-tick-no-go']['evidence_state']=='recorded_rejection','lost native rejection')
    require(a['unshifted-specialization']['kernel_or_retention'].startswith('Rank one'),'lost rank collapse')
    require(all(x['status']=='unbound_to_RH' for x in m['optional_control_applicability']),'unbound hostile made mandatory')
    # Coverage baseline guards deletion of both a map and its owning cell.
    baseline=initial()
    for key in ('stages','maps','cells'):
        require({x['id'] for x in m[key]}=={x['id'] for x in baseline[key]},'required inventory item deleted')
    return s,a,c


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--record',action='store_true');args=parser.parse_args()
    if args.record:
        require(not (ROOT/MODEL).exists(),'refusing implicit inventory overwrite')
        (ROOT/MODEL).write_text(json.dumps(initial(),indent=2)+'\n',encoding='utf-8')
    m=load(MODEL);s,a,c=validate(m);controls=[]
    for mode in ('unknown-stage','missing-domain','missing-owner','table-as-proof','lost-rejection','lost-rank-collapse','deleted-cell','stale-pin'):
        bad=copy.deepcopy(m)
        if mode=='unknown-stage':bad['maps'][0]['source']='unbound'
        elif mode=='missing-domain':bad['stages'][0]['domain']=''
        elif mode=='missing-owner':bad['cells'][0]['owner']='invented'
        elif mode=='table-as-proof':bad['inventory_only']=False
        elif mode=='lost-rejection':next(x for x in bad['cells'] if x['id']=='native-tick-no-go')['evidence_state']='recorded_finite_checks'
        elif mode=='lost-rank-collapse':next(x for x in bad['maps'] if x['id']=='unshifted-specialization')['kernel_or_retention']='injective'
        elif mode=='deleted-cell':bad['cells'].pop()
        else:bad['source_sha256'][next(iter(bad['source_sha256']))]='0'*64
        try:validate(bad)
        except ValueError:controls.append(mode)
        else:raise AssertionError('hostile accepted: '+mode)
    receipt_checks=[]
    for k,p in RECEIPTS.items():
        r=load(p);require(r['passed'] is True,'failed recorded receipt')
        for src,h in r['source_hashes'].items():
            q=Path(src);q=q if q.is_absolute() else ROOT/q
            require(q.is_file() and sha256(q.read_bytes()).hexdigest()==h,'upstream receipt drift '+src)
        receipt_checks.append(k)
    result=dict(schema='marici.rh-stage-dictionary-validation.v1',passed=True,inventory_constructed=True,
      transport_proofs_newly_obtained=False,scientific_suites_rerun=False,
      stage_count=len(s),map_count=len(a),cell_count=len(c),all_maps_owned=True,
      recorded_receipt_hashes_verified=receipt_checks,corruptions_rejected=controls,
      source_sha256={MODEL:sha(MODEL),NOTE:sha(NOTE),Path(__file__).relative_to(ROOT).as_posix():sha(Path(__file__).relative_to(ROOT).as_posix())})
    (ROOT/OUT).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result,indent=2))


if __name__=='__main__':main()
