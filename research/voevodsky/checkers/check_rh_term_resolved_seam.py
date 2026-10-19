"""Iteration2: a term-bearing seam, address obstruction and composition gate.
Consumes read-only certified enclosures; does not rerun their Arb quadrature.
Spectral atom reevaluation is numerical, explicitly finite/nonexhaustive.
"""
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
from itertools import permutations
import json,re,sys
from check_proton_native_task_catalogue import ROOT,ZERO,ONE,mm,mv,adj,madd,msub,add,mul,conj,sparse
from check_proton_single_probe_cycle import inverse
from check_proton_unitary_probe_repair import restore
from check_rh_two_seed_route_audit import real,multiply_scalar,diagonal
try:import mpmath as mp
except ModuleNotFoundError:
    sys.path.insert(0,str(ROOT/'research/flavor/.venv/Lib/site-packages'));import mpmath as mp

PAIRS=[(i,j) for i in range(3) for j in range(i,3)]
TERMS=('endpoint','gamma_with_infinite_tail','prime_with_infinite_tail')
def ball(text):
    match=re.fullmatch(r'\[([^\[\]]+?) \+/- ([^\[\]]+?)\]',text)
    if match:
        centre,radius=map(F,match.groups());assert radius>=0
        return centre-radius,centre+radius
    value=F(text);return value,value
def badd(a,b):return a[0]+b[0],a[1]+b[1]
def bscale(q,a):return (q*a[0],q*a[1]) if q>=0 else (q*a[1],q*a[0])
def midpoint(a):return (a[0]+a[1])/2
def overlap(a,b):return max(a[0],b[0])<=min(a[1],b[1])
def weights(c):
    return [mul(conj(c[i]),c[j])[0]*(1 if i==j else 2) for i,j in PAIRS]
def score(row,w):
    out=(F(0),F(0))
    for a,q in zip(row,w):out=badd(out,bscale(q,a))
    return out
def matrix(row):
    G=[[ZERO]*3 for _ in range(3)]
    for (i,j),a in zip(PAIRS,row):G[i][j]=G[j][i]=(midpoint(a),F(0))
    return G
def qvalue(G,c):return mm(mm(adj([[x] for x in c]),G),[[x] for x in c])[0][0]
def encoded_c(c):return [[str(x),str(y)] for x,y in c]
def encoded_ball(a):return [str(a[0]),str(a[1])]
def to_mp(q):return mp.mpf(q.numerator)/q.denominator

def gaussian_values(u,t,centres):return [mp.exp(-t*(u-a)**2/2) for a in centres]
def evaluate_test(u,w,t,centres):
    g=gaussian_values(u,t,centres)
    return mp.fsum(to_mp(q)*g[i]*g[j] for q,(i,j) in zip(w,PAIRS))
def finite_atoms(w,t,centres,samples):
    records=[];total=mp.mpf(0)
    for z in samples:
        assert z['real_part']=='0.5'
        gamma=mp.mpf(z['ordinate'])
        for sign in (1,-1):
            u=sign*gamma;value=evaluate_test(u,w,t,centres)/2;total+=value
            records.append({'sample_index':z['index'],'signed_u':mp.nstr(u,70),'multiplicity':'1',
                'half_divisor_value':mp.nstr(value,70),'parameter_on_critical_line':True})
    return total,records

def main():
    base=ROOT/'research/voevodsky';cp=base/'inputs/rh-term-resolved-seam-v1.json';contract=json.loads(cp.read_text())
    files={k:ROOT/contract[k] for k in ('prior','packet','certification','source')}
    prior=json.loads(files['prior'].read_text());assert prior['passed']
    for path,h in prior['source_hashes'].items():assert sha256((ROOT/path).read_bytes()).hexdigest()==h,path
    packet=json.loads(files['packet'].read_text());cert=json.loads(files['certification'].read_text());assert packet['status']==cert['status']=='passed'
    assert packet['parameters']['t']==cert['parameters']['t'] and packet['parameters']['frequency_centres']==cert['parameters']['frequency_centres']
    entries={tuple(x['indices']):x for x in cert['term_enclosures']};assert set(entries)==set(PAIRS)
    rows={term:[ball(entries[pair][term]) for pair in PAIRS] for term in TERMS}
    total_row=[tuple(sum(rows[term][k][j] for term in TERMS) for j in (0,1)) for k in range(6)]
    for k,pair in enumerate(PAIRS):assert overlap(total_row[k],ball(entries[pair]['certified_entry']))
    matrices={term:matrix(rows[term]) for term in TERMS};Ga=matrix(total_row)
    assert Ga==madd(madd(matrices[TERMS[0]],matrices[TERMS[1]]),matrices[TERMS[2]])
    # Actual certified diagonal intervals are disjoint: fixed labels cannot
    # make this arithmetic form invariant under the triangle's3-cycle.
    diagonal_balls=[total_row[PAIRS.index((i,i))] for i in range(3)]
    assert all(not overlap(diagonal_balls[i],diagonal_balls[j]) for i in range(3) for j in range(i+1,3))
    C=real([[0,1,0],[0,0,1],[1,0,0]]);I=real([[1,0,0],[0,1,0],[0,0,1]])
    assignments=[]
    for order in permutations(range(3)):
        P=real([[int(j==order[i]) for j in range(3)] for i in range(3)])
        labelled=mm(mm(P,Ga),adj(P));assert mm(mm(adj(C),labelled),C)!=labelled
        assignments.append({'slot_to_test':list(order),'fixed_label_C3_covariant':False})
    controls=[(ONE,ZERO,ZERO),(ZERO,ONE,ZERO),(ZERO,ZERO,ONE),(ONE,ONE,ONE),(ONE,(F(0),F(1)),ZERO),
              ((F(2),F(0)),(F(-1),F(1)),(F(1,2),F(-1,3)))]
    moving=[];Ck=I
    for frame in range(3):
        for c in controls:
            cc=tuple(mv(Ck,c))
            for term,G in matrices.items():
                Gk=mm(mm(Ck,G),adj(Ck));assert qvalue(Gk,cc)==qvalue(G,c)
        order=[next(j for j,z in enumerate(row) if z==ONE) for row in Ck]
        moving.append({'frame':frame,'basis_label_order':order,'every_term_readout_preserved':True})
        Ck=mm(C,Ck)
    assert Ck==I
    # A six-occurrence retained query ledger. These are DECLARED evaluators,
    # not assertions that existing native arrows perform source evaluation.
    routes=[]
    with mp.workdps(80):
        t=to_mp(F(packet['parameters']['t']));centres=[to_mp(F(x)) for x in packet['parameters']['frequency_centres']]
        scout=packet['calculations'][-1];samples=scout['critical_line_zero_samples'];assert len(samples)==16
        # Independently reevaluate every matrix entry from the stored zero
        # atoms, not from G_arithmetic or the stored finite matrix itself.
        for k,(i,j) in enumerate(PAIRS):
            w=[F(0)]*6;w[k]=1
            z,atoms=finite_atoms(w,t,centres,samples)
            assert abs(z-mp.mpf(scout['finite_zero_packet'][i][j]))<mp.mpf('1e-55')
        for c in controls:
            w=weights(c);mirror=tuple((-x,-y) for x,y in c);assert weights(mirror)==w
            contributions={term:score(rows[term],w) for term in TERMS}
            arithmetic=(F(0),F(0))
            for value in contributions.values():arithmetic=badd(arithmetic,value)
            finite,atoms=finite_atoms(w,t,centres,samples)
            numerical_compatible=to_mp(arithmetic[0])<=finite<=to_mp(arithmetic[1]);assert numerical_compatible
            history=[{'occurrence':'AB','action':'transport retained query to arithmetic route','coefficients':encoded_c(c)},
              {'occurrence':'BC','action':'evaluate separately labelled arithmetic source terms','terms':{term:encoded_ball(a) for term,a in contributions.items()}},
              {'occurrence':'CA','action':'sum arithmetic values, retaining input and term records','arithmetic_interval':encoded_ball(arithmetic)},
              {'occurrence':'BA','action':'transport mirrored query to spectral route','coefficients':encoded_c(mirror),'polarized_test_unchanged':True},
              {'occurrence':'AD','action':'evaluate independently sampled spectral atoms','atoms':atoms,
               'unresolved_remainder':{'kind':'full_signed_divisor_minus_sampled_32_atoms','value':None,'certified':False}},
              {'occurrence':'DB','action':'return spectral partial sum and remainder status','finite_value':mp.nstr(finite,70),
               'full_divisor_value_available':False}]
            routes.append({'input_coefficients':encoded_c(c),'polarized_test_weights':list(map(str,w)),'history':history,
                'finite_scout_compatible_with_arithmetic_interval_numerically':True,
                'shared_edge_full_equality_accepted':False,'rejection_reason':'Full signed divisor remainder and external normalization are not certified.'})
        # Do not substitute a positive real-ordinate Gram for complex zero
        # evaluation. Same exact quartet sign control as iteration1, evaluated
        # here through the route evaluator itself.
        off=[sign*20*mp.pi+mp.j*imag_sign/4 for sign in (1,-1) for imag_sign in (1,-1)]
        w=[F(1),F(0),F(0),F(0),F(0),F(0)]
        signed=mp.fsum(evaluate_test(u,w,t,centres)/2 for u in off)
        projected=mp.fsum(evaluate_test(mp.re(u),w,t,centres)/2 for u in off)
        assert mp.re(signed)<0 and abs(mp.im(signed))<mp.mpf('1e-100') and projected>0
        off_control={'full_value':mp.nstr(signed,60),'real_ordinate_substitution':mp.nstr(projected,60),'actual_zeta_divisor_claimed':False}
    # Term-level native form transport, not mere replay of the total packet.
    # Each lift contains one common X. Naively summing3 lifts includes X3x
    # and gives3Ga. The corrected composition retains X only once.
    term_transport={}
    for name,channels in prior['native_packet_channels'].items():
        X,Y,D=[restore(channels[k]) for k in ('source','sink','gram')]
        native_metric=prior['native_metrics']['proton' if name=='protonlike' else 'neutron'];M=diagonal([F(x) for x in native_metric]*3)
        # Reconstruct weighted signed F from live native operators rather than
        # trusting form equality asserted by the previous result.
        from check_proton_native_task_catalogue import parse,mzero
        from check_rh_two_seed_route_audit import build
        if name=='protonlike':
            source_path=ROOT/'research/nima/results/twelve-triangle-1836-arrows.json';_,ops=parse(json.loads(source_path.read_text()))
        else:
            source_path=ROOT/'research/voevodsky/results/belt_three_by_twelve_store.json';ns=json.loads(source_path.read_text());ds=[F(x['d']) for x in ns['coordinates']];ops=[mzero(36,36) for _ in range(3)]
            for a in ns['arrows']:
                x,b,y,d2=map(F,a['numerator']);assert b==d2==0
                ops['LGN'.index(a['stage'])][a['target']][a['source']]=(x/ds[a['source']],y/ds[a['source']])
        native=build(name,ops,[F(x) for x in native_metric]);H=native['H']
        assert native['X']==X and native['Y']==Y and native['D']==D
        lifts={term:madd(X,mm(mm(Y,inverse(D)),G)) for term,G in matrices.items()}
        for term,lift in lifts.items():assert mm(mm(adj(lift),H),lift)==matrices[term]
        naive=madd(madd(lifts[TERMS[0]],lifts[TERMS[1]]),lifts[TERMS[2]])
        corrected=msub(naive,multiply_scalar(X,2))
        assert mm(mm(adj(naive),H),naive)==multiply_scalar(Ga,3)
        assert mm(mm(adj(corrected),H),corrected)==Ga
        term_transport[name]={'term_midpoint_attachments':{k:sparse(v) for k,v in lifts.items()},
            'combined_once_retained_source':sparse(corrected),'naive_sum_triples_form':True,'corrected_sum_preserves_arithmetic_midpoint':True,
            'midpoint_attachment_is_exact_analytic_ball_equality':False,'source_path':source_path.relative_to(ROOT).as_posix()}
    result={'schema':'marici.rh-term-resolved-seam.v1','passed':True,'iteration':2,
        'source_term_reported_enclosures':{k:[encoded_ball(x) for x in row] for k,row in rows.items()},
        'term_midpoint_forms':{k:sparse(G) for k,G in matrices.items()},'arithmetic_midpoint':sparse(Ga),
        'six_fixed_label_assignments':assignments,'moving_basis_frames':moving,
        'frame_register_is_native_W_intertwiner':False,'retained_evaluator_routes':routes,
        'independently_reevaluated_spectral_atoms_per_query':32,'offcritical_evaluator_control':off_control,
        'native_term_transport':term_transport,'same_term_forms_survive_in_both':True,
        'shared_seam_object':'Gaussian family/parameters, coefficients modulo mirrored sign, polarized test, source conventions, separate arithmetic labels and signed-divisor remainder status',
        'full_zero_divisor_certified':False,'native_arrows_execute_these_evaluators':False,
        'original_triangle_geometric_operation_assignment_source_selected':False,'RH_proved':False,
        'next_nonredundant_obligation':'Compare this retained evaluator ledger with actual six native occurrence operations; construct or reject an enlarged typed record-bank intertwiner, including the basis-frame register.',
        'scope':contract['scope'],'shared_sources_modified':False}
    bound=[cp,*files.values(),Path(__file__),Path(mp.__file__),base/'checkers/check_rh_two_seed_route_audit.py',
           ROOT/'research/nima/results/twelve-triangle-1836-arrows.json',base/'results/belt_three_by_twelve_store.json']
    result['source_hashes']={str(p.resolve()):sha256(p.read_bytes()).hexdigest() for p in bound}
    (base/'results/rh-term-resolved-seam-v1.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'passed':True,'retained_query_histories':len(routes),'source_terms':3,'independent_scout_atoms':32,
       'fixed_label_assignments_surviving':0,'moving_basis_frames':3,'term_forms_preserved_in_both':True,'full_RH_seam_equality_certified':False},indent=2))
if __name__=='__main__':main()
