"""Exact eight-action identification with axis-dependent record channels.
uv run --with sympy python research/nima/checkers/check_record_sign_action_census.py
This computes model records, not measurements. No physical admission gate.
"""
from fractions import Fraction
from itertools import product, permutations
from pathlib import Path
import hashlib
import json
import runpy
import sympy as s

OWNER = Path(__file__).resolve().parents[1]
REPO = OWNER.parent.parent
CONTRACT = OWNER/'contracts/record-sign-action-census.v1.json'
OUT = OWNER/'results/record-sign-action-census.json'
SIGNS = (-1,1)
MASKS = tuple(product((0,1),repeat=3))
LABELS = tuple(product(range(3),repeat=3))
IDEAL = tuple(product(range(2),SIGNS,SIGNS))
CHECKS = []
J = s.Matrix([[0,1],[1,0]])


def require(name, value):
    if not bool(value):
        raise AssertionError(name)
    CHECKS.append(name)


def encode(M):
    return [[str(x) for x in row] for row in M.tolist()]


def l1(M):
    return sum(abs(x) for x in M)


def parity(p):
    return sum(p[j] > p[k] for j in range(4) for k in range(j+1,4)) % 2


def xor(a,b):
    return tuple(x ^ y for x,y in zip(a,b))


def operator(p, phases=(0,0,0,0)):
    M = s.zeros(4)
    for j in range(4):
        M[p[j],j] = s.I**phases[j]
    return M


def center(M):
    return M-(M*s.ones(M.cols,1))*(s.ones(1,M.rows)*M)


def reflect(M):
    return M-2*center(M)


def pair_marginal(P, port):
    if port == 'A':
        return s.Matrix(3,3,lambda r,a:sum(P[9*r+3*a+b] for b in range(3)))
    return s.Matrix(3,3,lambda r,b:sum(P[9*r+3*a+b] for a in range(3)))


def basis_marginal(P, port):
    if port == 'A':
        return s.Matrix([sum(P[3*a+b] for b in range(3)) for a in range(3)])
    return s.Matrix([sum(P[3*a+b] for a in range(3)) for b in range(3)])


def references(PB,PA,Q00,Q11):
    MB,MA = pair_marginal(PB,'B'),pair_marginal(PA,'A')
    az = [basis_marginal(Q00,'A'),basis_marginal(Q11,'A')]
    bz = [basis_marginal(Q00,'B'),basis_marginal(Q11,'B')]
    require('plus-reference-closure', pair_marginal(PB,'A').T*s.ones(3,1) == az[0]
            and pair_marginal(PA,'B').T*s.ones(3,1) == bz[0])
    require('common-herald-marginal', MA*s.ones(3,1) == MB*s.ones(3,1))
    return MA,MB,az,bz


def predictions(ref, mask=None):
    MA,MB,az,bz = ref
    if mask is None:
        at,bt,ms,mt = az[0],bz[0],MA,reflect(MB)
    else:
        h,a,b = mask
        at,bt = az[a],bz[b]
        mt = reflect(MB) if h ^ b else MB
        ms = reflect(MA) if h ^ a else MA
    return (s.Matrix([at[a]*mt[r,b] for r,a,b in LABELS]),
            s.Matrix([bt[b]*ms[r,a] for r,a,b in LABELS]))


def survivor(mask, flags):
    h,a,b = mask
    return ((not a or not flags['AZ']) and (h ^ b or not flags['CB'])
            and (not b or not flags['BZ']) and (not(h ^ a) or not flags['CA']))


def main():
    OUT.unlink(missing_ok=True)
    CHECKS.clear()
    c = json.loads(CONTRACT.read_text())
    paths = {k:REPO/p for k,p in c['source'].items()}
    inputs = [Path(__file__).resolve(),CONTRACT,*paths.values()]
    before = {p:p.read_bytes() for p in inputs}
    parents = {k:json.loads(paths[k].read_text()) for k in ('bypass_receipt','projective_receipt')}
    for parent in parents.values():
        require('predecessor-current', parent['status'] == 'pass' and all(
            hashlib.sha256((REPO/p).read_bytes()).hexdigest() == h for p,h in parent['source_sha256'].items()))
    protected = [REPO/'research/aspect/results/combined_bell_instrument.json',
                 OWNER/'results/bell-preparation-herald-record.json']
    prior = {p:p.read_bytes() if p.exists() else None for p in protected}
    gram,quantum,instrument = [runpy.run_path(str(paths[k])) for k in ('fillers','states','instrument')]
    source = {name:tuple(gram['code'](f(x)) for x in gram['CODES']) for name,f in gram['FILLERS'].items()}
    parent = parents['projective_receipt']
    require('live-source-actions', {k:list(v) for k,v in source.items()} == parent['source_functions'])
    lifts = {tuple(row['permutation']):operator(row['permutation'],row['phase_exponents']) for row in parent['representatives']}
    require('actual-S4-image', sorted(lifts) == list(permutations(range(4))))
    assignments = list(product(MASKS,repeat=3))
    valid = [triple for triple in assignments if all(
        xor(xor(triple[i],triple[i+1]),triple[i]) == xor(xor(triple[i+1],triple[i]),triple[i+1]) for i in (0,1))]
    require('complete-eight-action-class', len(assignments) == 512 and valid == [(v,v,v) for v in MASKS])
    for v,p,q in product(MASKS,lifts,lifts):
        pq = tuple(p[q[j]] for j in range(4))
        require('all-action-composition-cells', pq in lifts and tuple(parity(pq)*x for x in v)
                == xor(tuple(parity(p)*x for x in v),tuple(parity(q)*x for x in v)))
    require('even-basis-reference-actions', parity(source['id']) == parity(source['flip_both']) == 0)

    I,X,Z,Q = quantum['I2'],quantum['X'],quantum['Z'],instrument['Q']
    def to_Q(M):
        M = M.applyfunc(s.simplify)
        require('native-rational-coefficients', all(x.is_Rational for x in M))
        return [[Q(Fraction(int(x.p),int(x.q))) for x in row] for row in M.tolist()]
    def from_Q(M):
        return s.Matrix([[s.Rational(x.rational.numerator,x.rational.denominator)
                          +s.sqrt(2)*s.Rational(x.root2.numerator,x.root2.denominator) for x in row] for row in M])
    rho00 = quantum['states']()['product00']
    prep = {side:{h:from_Q(instrument['instrument'](to_Q(rho00),to_Q((I+(-1)**h*X)/2),side=='A'))
                  for h in range(2)} for side in ('A','B')}
    for side,h in product(('A','B'),range(2)):
        require('balanced-native-preparation', s.trace(prep[side][h]) == s.Rational(1,2))
        require('retained-preparation-binding', encode(prep[side][h]) == parents['bypass_receipt']['preparations'][side][str(h)])
    def ideal(U,side,axes,basis=False):
        records = []
        states = [rho00] if basis else [prep[side][h] for h in range(2)]
        for rho,a,b in product(states,SIGNS,SIGNS):
            rho = U*rho*U.H
            pa,pb = (I+a*axes[0])/2,(I+b*axes[1])/2
            post = from_Q(instrument['joint_instrument'](to_Q(rho),to_Q(pa),to_Q(pb)))
            E = s.kronecker_product(pa,pb)
            require('actual-joint-continuation', post == E*rho*E.H)
            records.append(post)
        require('complete-ideal-trace', sum(s.trace(M) for M in records) == 1)
        return s.Matrix([s.trace(M) for M in records]),s.Matrix([[M[i,j] for i,j in product(range(4),repeat=2)] for M in records])
    PT,PS,PF = [operator(source[name]) for name in ('twist','swap','flip_both')]
    UT,US,UF = [lifts[source[name]] for name in ('twist','swap','flip_both')]
    ideals = {'B':ideal(s.eye(4),'B',(Z,X)), 'A':ideal(s.eye(4),'A',(X,Z)),
              'T0':ideal(PT,'B',(Z,X)), 'S0':ideal(PS,'B',(X,Z)),
              'TP':ideal(UT,'B',(Z,X)), 'SP':ideal(US,'B',(X,Z)),
              '00':ideal(s.eye(4),None,(Z,Z),True), '11':ideal(PF,None,(Z,Z),True)}
    require('projective-basis-reference', ideal(UF,None,(Z,Z),True) == ideals['11'])
    for h in range(2):
        require('native-port-transport', PS*prep['B'][h]*PS.H == US*prep['B'][h]*US.H == prep['A'][h])
    require('native-11-construction', PF*rho00*PF.H == s.diag(0,0,0,1))

    # Generic entrywise identities, independent of the numerical census.
    k0,k1,ap,am,bp,bm,zap,zam,zbp,zbm = s.symbols('k0 k1 ap am bp bm zap zam zbp zbm')
    ks,ax,bx,az,bz = (k0,k1),(ap,am),(bp,bm),(zap,zam),(zbp,zbm)
    def kernel(xs,flip):
        mean = (k0+k1)*(xs[0]+xs[1])/4
        cov = (k0-k1)*(xs[0]-xs[1])/4
        return mean+(-1)**flip*cov
    for h,a,b in MASKS:
        nativeT = az[a]*sum(ks[t ^ h]*bx[t ^ b] for t in range(2))/2
        nativeS = bz[b]*sum(ks[t ^ h]*ax[t ^ a] for t in range(2))/2
        require('generic-twist-prediction', s.expand(nativeT-az[a]*kernel(bx,h ^ b)) == 0)
        require('generic-swap-prediction', s.expand(nativeS-bz[b]*kernel(ax,h ^ a)) == 0)

    informative = {k:s.Matrix([[s.Rational(x) for x in row] for row in rows]) for k,rows in c['channels'].items()}
    order = c['degeneracy_census']['flags']
    def channels(flags):
        result = {}
        for k,active in zip(order,flags):
            R = informative[k]
            result[k] = R if active else s.Matrix.hstack((R[:,0]+R[:,1])/2,(R[:,0]+R[:,1])/2)
        return result
    def map_for(ch,axes,mask=(0,0,0),basis=False):
        h,a,b = mask
        A,B = ch['A'+axes[0]]*J**a,ch['B'+axes[1]]*J**b
        return s.kronecker_product(A,B) if basis else s.kronecker_product(ch['K']*J**h,A,B)
    def observe(ch,key,mask=(0,0,0),continuations=False):
        axes = ('X','Z') if key in ('A','S0','SP') else ('Z','Z') if key in ('00','11') else ('Z','X')
        L = map_for(ch,axes,mask,key in ('00','11'))
        P = L*ideals[key][0]
        require('all-records-normalized-positive', len(P) == (9 if key in ('00','11') else 27)
                and sum(P) == 1 and all(x >= 0 for x in P))
        return (P,L*ideals[key][1]) if continuations else P
    def calibration(ch):
        return {key:observe(ch,key) for key in ('B','A','00','11')}
    def ref_from(data):
        return references(data['B'],data['A'],data['00'],data['11'])
    def saved(P,C):
        return {'records':encode(P),'reported_continuations_flat':encode(C)}

    census = []; selected_continuations = {}; observable_strata = set()
    for flags in product((0,1),repeat=5):
        ch = channels(flags)
        for R in ch.values():
            require('complete-column-stochastic-channel', s.ones(1,3)*R == s.ones(1,2) and all(x >= 0 for x in R))
        data = calibration(ch); ref = ref_from(data)
        MA,MB,azc,bzc = ref
        obs = {'CA':center(MA) != s.zeros(3),'CB':center(MB) != s.zeros(3),
               'AZ':azc[0] != azc[1],'BZ':bzc[0] != bzc[1]}
        require('observable-flag-binding', list(obs.values()) == [bool(flags[0] and flags[1]),bool(flags[0] and flags[2]),bool(flags[3]),bool(flags[4])])
        observable_strata.add(tuple(obs.values()))
        target = (observe(ch,'TP'),observe(ch,'SP'))
        require('projective-reference-prediction', predictions(ref) == target)
        aliases = []; rows = []
        for v in MASKS:
            actual = (observe(ch,'T0',v),observe(ch,'S0',v))
            require('complete-reference-predictor', actual == predictions(ref,v))
            equal = actual == target
            require('exact-degeneracy-criterion', equal == bool(survivor(v,obs)))
            if equal:
                aliases.append(list(v))
            rows.append({'mask':list(v),'twist':encode(actual[0]),'swap':encode(actual[1]),
                         'residual_l1':[str(l1(actual[i]-target[i])) for i in (0,1)]})
        require('joint-separation-iff-four-contrasts', (not aliases) == all(obs.values()))
        # Keep full continuation matrices for the informative case and the two
        # nondegenerate-X / blind-Z counterexamples; record equality is weaker.
        if flags in ((1,1,1,1,1),(1,1,1,0,1),(1,1,1,1,0)):
            selected = {'reference':{key:saved(*observe(ch,key,continuations=True)) for key in data},
                        'projective':{key:saved(*observe(ch,key,continuations=True)) for key in ('TP','SP')},'rivals':{}}
            for row in rows:
                v = tuple(row['mask'])
                if flags == (1,1,1,1,1) or list(v) in aliases:
                    selected['rivals'][''.join(map(str,v))] = {key:saved(*observe(ch,key,v,True)) for key in ('T0','S0')}
                    if list(v) in aliases:
                        differences = [l1(observe(ch,key,v,True)[1]-observe(ch,other,continuations=True)[1])
                                       for key,other in (('T0','TP'),('S0','SP'))]
                        require('record-alias-not-instrument-identity', any(x > 0 for x in differences))
                        row['continuation_residual_entrywise_l1'] = [str(x) for x in differences]
            selected_continuations[''.join(map(str,flags))] = selected
        census.append({'channel_flags':dict(zip(order,flags)),'observable_flags':obs,
                       'channels':{k:encode(R) for k,R in ch.items()},
                       'calibration':{k:encode(P) for k,P in data.items()},
                       'projective_probes':[encode(P) for P in target], 'actions':rows,'record_aliases':aliases})
    require('all-degeneracy-strata', len(census) == 32 and len(observable_strata) == 16)
    for azbit,bzbit,expected in ((1,1,[]),(0,1,[[1,1,0]]),(1,0,[[0,0,1]]),(0,0,[[0,0,1],[1,1,0]])):
        entry = next(row for row in census if list(row['channel_flags'].values()) == [1,1,1,azbit,bzbit])
        require('strong-blind-Z-hostile', entry['record_aliases'] == expected)

    full = channels((1,1,1,1,1)); data = calibration(full)
    true = (observe(full,'TP'),observe(full,'SP'))
    refits = []
    for v,port in (((0,0,1),'BZ'),((1,1,0),'AZ')):
        fake = dict(full); plus = full[port][:,1]
        fake[port] = s.Matrix.hstack(plus,plus)
        candidate_data = calibration(fake)
        require('delete-11-calibration-refit', all(candidate_data[k] == data[k] for k in ('B','A','00')))
        require('delete-11-both-probes-alias', (observe(fake,'T0',v),observe(fake,'S0',v)) == true)
        residual = l1(candidate_data['11']-data['11'])
        require('11-reference-rejects-refit', residual > 0)
        refits.append({'mask':list(v),'changed_channel':port,'missing_reference_residual_l1':str(residual),
                       'candidate_11':encode(candidate_data['11']),'true_11':encode(data['11'])})
    require('inputs-preserved', all(p.read_bytes() == raw for p,raw in before.items()))
    require('foreign-receipts-preserved', all((p.read_bytes() if p.exists() else None) == raw for p,raw in prior.items()))
    result = {'schema':'marici.nima.record-sign-action-census-result.v1','status':'pass',
              'classification':'eight-sign-actions-reference-identifiable-with-exact-blind-channel-strata',
              'physical_admission_required':False,'measured_records':False,'checks_passed':len(CHECKS),
              'action_count':len(valid),'generator_assignments':len(assignments),'source_composition_cells':8*24*24,
              'channel_strata':len(census),'observable_strata':len(observable_strata),'census':census,
              'record_order':c['records'],'reported_label_indices':[list(x) for x in LABELS],
              'continuation_coordinate_order':[[i,j] for i,j in product(range(4),repeat=2)],
              'native_ideal_packets':{k:{'records':encode(P),'continuations_flat':encode(C)} for k,(P,C) in ideals.items()},
              'selected_reported_continuations':selected_continuations,'reference_deletion_refits':refits,
              'exact_rule':'exclude all eight iff C_A, C_B, Delta_AZ and Delta_BZ are nonzero',
              'scope':c['scope'],'source_sha256':{p.relative_to(REPO).as_posix():hashlib.sha256(raw).hexdigest() for p,raw in before.items()}}
    OUT.parent.mkdir(parents=True,exist_ok=True)
    OUT.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ('status','classification','checks_passed','action_count','generator_assignments',
                    'source_composition_cells','channel_strata','observable_strata','reference_deletion_refits')},indent=2))


if __name__ == '__main__':
    main()
