"""Record-state Gram/cycle phases from existing addressed pulse histories.

Fixed feature metric, old AB preparation, actual full-turn branch words.
Common boundaries refer to the completed labelled paths, not a supplied
native equality between them. No Born or branch-sum rule is introduced.
"""
from contextlib import redirect_stdout
from functools import lru_cache
from itertools import combinations
from collections import defaultdict
from pathlib import Path
import io
import json
import hashlib
import runpy
import sympy as S

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
with redirect_stdout(io.StringIO()):
    exchange=runpy.run_path(str(HERE/'check_seed_port_exchange_binding.py'))
    source=runpy.run_path(str(HERE/'check_actual_triangle_branch_composition.py'))
ledger=source['ledger']; ops=exchange['operators']; metric=exchange['metric']
initial=exchange['excited']  # Prior AB-only preparation, not adjusted.
norm=(initial.T*metric*initial)[0]
checks=[]
def check(name,condition):
    if not condition:raise AssertionError(name)
    checks.append(name)

left=ledger.compose_payloads(source['L'],source['R'])
right=ledger.compose_payloads(source['R'],source['L'])
whole=ledger.retain_payload(ledger.root,(1,)*6)
for _ in range(6):
    left,right=ledger.compose_payloads(left,whole),ledger.compose_payloads(right,whole)
groups=defaultdict(list)
for role,payload in [('LR',left),('RL',right)]:
    for path in payload.paths:
        word=tuple(edge[2] for edge in path)
        groups[(role,path[0][0],path[-1][1])].append(word)
for key in groups:groups[key].sort()
check('all-actual-full-turn-branches',sum(map(len,groups.values()))==68)
check('prior-normalized-preparation',norm==1)

@lru_cache(None)
def endpoint_state(word):
    if not word:return initial
    return ops[word[-1]]*endpoint_state(word[:-1])


def states_at(words,phase):
    # Interpolate only the final addressed pulse of each completed path.
    # phase=0: immediately before it; phase=pi: after all six extensions.
    # At the midpoint, witness T/pi=11/6 if pulse area pi occupies one
    # already attached clock interval pi/3. The interpolation is the old
    # specified pulse, not a derivation of its rate from the primitive graph.
    factor={0:S.Integer(1),1:-S.I,2:S.Integer(-1)}[phase]
    states=[]
    for word in words:
        before=endpoint_state(word[:-1]);after=endpoint_state(word)
        states.append((before+after)/2+factor*(before-after)/2)
    return S.Matrix.hstack(*states)


def gram(V):return (V.conjugate().T*metric*V/norm).applyfunc(S.expand)

def triple(G,ids):
    a,b,c=ids
    return S.expand(G[a,b]*G[b,c]*G[c,a])

census=[]; example=None; cached={}; max_imaginary=S.Rational(0)
for key,words in sorted(groups.items()):
    grams=[]
    for phase in (0,1,2):
        V=states_at(words,phase);G=gram(V)
        check('state-norms/'+str(key)+'/'+str(phase),all(S.expand(G[i,i])==1 for i in range(len(words))))
        check('Hermitian-Gram/'+str(key)+'/'+str(phase),G.conjugate().T==G)
        grams.append(G)
    cached[key]=grams
    triples=list(combinations(range(len(words)),3))
    complex_mid=[]; negative_end=[]; changed=[]
    for ids in triples:
        values=[triple(G,ids) for G in grams]
        if S.im(values[1])!=0:
            max_imaginary=max(max_imaginary,abs(S.im(values[1])))
            complex_mid.append(ids)
            if example is None:example=(key,tuple(words[i] for i in ids),values)
        if values[2]<0:negative_end.append(ids)
        if values[0]!=values[1] or values[1]!=values[2]:changed.append(ids)
    census.append({'boundary':list(key),'paths':len(words),'triples':len(triples),
                   'nonreal_midpulse_triples':len(complex_mid),
                   'negative_full_endpoint_triples':len(negative_end),
                   'changing_cycle_products':len(changed)})
check('nonzero-record-cycle-phase-generated',example is not None)
key,words,values=example
V=states_at(words,1);G=gram(V)
check('example-nonzero-cyclic-imaginary-part',S.im(values[1])!=0)
check('endpoint-cycle-products-real',S.im(values[0])==S.im(values[2])==0)
# Same global pulse on EVERY alternative is a frame/control comparison:
# it preserves the whole Gram, unlike distinct addressed route actions.
Q=(S.eye(22)-ops['AB'])/2
common=S.eye(22)+(-S.I-1)*Q
check('common-pulse-preserves-record-Gram',S.simplify(gram(common*V)-G)==S.zeros(3))
phases=S.diag(1,S.I,-1)
rephased=gram(V*phases)
check('independent-record-rephasing-preserves-cycle',S.expand(triple(rephased,(0,1,2))-values[1])==0)
check('complex-conjugation-reverses-cycle-phase',S.expand(triple(gram(S.conjugate(V)),(0,1,2))-S.conjugate(values[1]))==0)
check('nonflat-phase-not-from-feature-variation',exchange['H']==S.kronecker_product(10*S.eye(4)+S.ones(4),10*S.eye(4)+S.ones(4)))
# Zero must not be normalized into a fabricated phase; matched input is idle
# under every old pulse and gives identical normalized record states.
matched=exchange['fixed']
check('matched-preparation-idle',all(op*matched==matched for op in ops.values()))
matched_norm=(matched.T*metric*matched)[0]
matched_states=S.Matrix.hstack(matched,matched,matched)
matched_G=matched_states.T*metric*matched_states/matched_norm
check('matched-cycle-trivial',matched_G==S.ones(3))
check('zero-preparation-has-no-normalized-Gram',(S.zeros(22,1).T*metric*S.zeros(22,1))[0]==0)

result={
    'schema':'marici.nima.retained-history-overlap-phase.v1','status':'pass','checks':checks,
    'census':census,
    'totals':{field:sum(row[field] for row in census) for field in
              ['paths','triples','nonreal_midpulse_triples','negative_full_endpoint_triples','changing_cycle_products']},
    'maximum_absolute_midpulse_imaginary_part':str(max_imaginary),
    'maximum_absolute_midpulse_imaginary_part_decimal':float(max_imaginary),
    'first_lexicographic_example':{'boundary':list(key),'words':[list(w) for w in words],
        'cycle_products_before_mid_after':list(map(str,values)),
        'midpulse_imaginary_part':str(S.im(values[1])),
        'midpulse_Gram':[[str(S.expand(v)) for v in row] for row in G.tolist()]},
    'positive_result':'different actual retained addressed histories generate nonreal gauge-invariant record-state cycle products at fixed feature geometry',
    'controls':['common pulse preserves Gram','record rephasing preserves cycle','conjugation reverses phase','matched preparation has trivial Gram','zero is not normalized'],
    'scope':'parallel labelled paths and a declared common pulse-state realization, not a proof of equality of their native fillers or a new physical measurement rule',
    'remaining':'history-state Gram is not automatically the operation-feature Gram of the curved backreaction model; no new feedback return law is installed',
    'preparation_boundary':'uses the old supplied AB record excitation; source occurrence counts alone do not prepare that mode state',
    'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
}
(ROOT/'results/retained-history-overlap-phase.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(f'PASS: {len(checks)} exact retained-history Gram/phase checks')
print('Census:',result['totals'])
print('First source-bound example:',key,words)
print('Largest absolute imaginary cyclic overlap:',float(max_imaginary))
