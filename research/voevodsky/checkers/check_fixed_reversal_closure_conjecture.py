"""Falsification test for ONE frozen finite closure conjecture.

Success of this checker does not mean survival of the conjecture. It means
that its outcome and its counterexamples have been verified exactly.
"""
from itertools import combinations, permutations
from pathlib import Path
from hashlib import sha256
from fractions import Fraction as Q
import json

from check_reversed_coefficient_attachment import (
    SOURCE, verify, weight, ZERO, ONE, POINTS, times, plus, sub, conj,
    div, transpose, adjoint, multiply, identity, encode)

BASE = Path(__file__).resolve().parents[1]
CONTRACT = {
    'reversal':'K-linear dual: reverse every arrow, retain its coefficient',
    'field':'Q(sqrt(-3))',
    'direct_identifications':'24 tetrahedral vertex permutations, acting on triangle labels and spatial axes',
    'closure':'aligned reversed return E satisfies E N = N',
    'observable':'the complete source return N on its retained image',
    'conjecture':'one fixed law admits a direct closure and an inequivalent closure requiring extra retained structure',
    'necessary_prediction':'at least one permitted direct identification closes',
    'excluded_repairs':['conjugating coefficients','adding a fitted complex phase identification','changing the observable'],
    'scope':'finite candidate contract, not a law derived from the geometric flags',
}

def apply(a,v):
    return [row[0] for row in multiply(a,[[x] for x in v])]

def digest(value):
    return sha256(json.dumps(value,sort_keys=True,separators=(',',':')).encode()).hexdigest()

def main():
    original = SOURCE.read_bytes(); packet = json.loads(original)
    evidence,rows = verify(packet)
    labels = sorted({tuple(r['source'][1:]) for r in rows})
    index = {p:i for i,p in enumerate(labels)}; n = len(labels)
    matrices = {s:[[ZERO]*n for _ in labels] for s in ('raw','local','aligned')}
    for r in rows:
        matrices[r['source'][0]][index[tuple(r['target'][1:])]][index[tuple(r['source'][1:])]] = weight(r)
    L,G,N = (matrices[s] for s in ('raw','local','aligned'))
    E = multiply(transpose(L),multiply(transpose(G),transpose(N)))
    w = [N[i][0] for i in range(n)]
    cases=[]; orthogonal=True; maps=[]
    for perm in permutations('ABCD'):
        rename=dict(zip('ABCD',perm))
        R=[[sum(Q(POINTS[rename[v]][a]*POINTS[v][b],4) for v in 'ABCD')
            for b in range(3)] for a in range(3)]
        orthogonal &= all(sum(R[k][i]*R[k][j] for k in range(3)) == (i==j)
                          for i in range(3) for j in range(3))
        mapping=[]
        for edge,axis in labels:
            b='xyz'.index(axis); a=next(a for a in range(3) if R[a][b])
            mapping.append((index[(''.join(rename[v] for v in edge),'xyz'[a])],R[a][b]))
        maps.append(tuple(mapping))
        aligned=[[ZERO]*n for _ in labels]
        for i,(di,si) in enumerate(mapping):
            for j,(dj,sj) in enumerate(mapping):
                aligned[di][dj]=times((si*sj,Q(0)),E[i][j])
        image=apply(aligned,w)
        bad=next((i for i in range(n) if image[i]!=w[i]),None)
        cases.append({'alignment':''.join(perm),'closes':bad is None,
                      'counterexample':None if bad is None else {
                          'input':'first column of N, a state fixed by N',
                          'output_port':list(labels[bad]),
                          'required':encode(w[bad]),'actual':encode(image[bad]),
                          'defect':encode(sub(image[bad],w[bad]))}})
    # Boundary data cannot discriminate transpose from adjoint: every
    # signed incidence coefficient is real. Both rules agree on it.
    cells=[c for k in range(1,5) for c in combinations(range(4),k)]
    ci={c:i for i,c in enumerate(cells)}
    boundary=[[ZERO]*len(cells) for _ in cells]
    for cell in cells:
        if len(cell)==1: continue
        for k in range(len(cell)):
            boundary[ci[cell[:k]+cell[k+1:]]][ci[cell]]=(Q((-1)**k),Q(0))
    # Out-of-contract controls: repairs remain excluded from the outcome.
    D=[div(x,conj(x)) for x in w]
    repaired=[[times(times(D[i],E[i][j]),conj(D[j])) for j in range(n)] for i in range(n)]
    # Factoring D through a new coordinate copy supplies no independent
    # retained object at this observable: B A contracts to the same D.
    A=[[div(ONE,conj(w[i])) if i==j else ZERO for j in range(n)] for i in range(n)]
    B=[[w[i] if i==j else ZERO for j in range(n)] for i in range(n)]
    diagonal=[[D[i] if i==j else ZERO for j in range(n)] for i in range(n)]
    checks={
        'fresh_source_verified':evidence['verified'],
        'literal_reverse_of_full_return_is_transpose':E==transpose(N),
        'counterexample_state_is_nonzero_and_retained':any(x!=ZERO for x in w) and apply(N,w)==w,
        'all_24_identifications_are_distinct_and_orthogonal':len(set(maps))==24 and orthogonal,
        'each_identification_is_a_signed_coordinate_bijection':all(
            sorted(i for i,s in m)==list(range(n)) and all(abs(s)==1 for i,s in m) for m in maps),
        'every_alignment_has_an_exact_retained_state_counterexample':all(c['counterexample'] is not None for c in cases),
        'incidence_boundary_squared_zero':multiply(boundary,boundary)==[[ZERO]*len(cells) for _ in cells],
        'geometric_incidence_does_not_select_complex_reversal':transpose(boundary)==adjoint(boundary),
        'same_two_reversals_differ_on_actual_coefficients':transpose(N)!=adjoint(N),
        'excluded_adjoint_control_closes':apply(adjoint(N),w)==w,
        'excluded_phase_control_closes':repaired==N,
        'explicit_intermediate_factor_contracts_to_same_alignment':multiply(B,A)==diagonal,
        'coefficient_source_unchanged':SOURCE.read_bytes()==original,
    }
    direct=sum(c['closes'] for c in cases)
    result={
        'verification_passed':all(checks.values()),
        'conjecture_status':'refuted_under_frozen_contract' if direct==0 else 'necessary_prediction_survives',
        'reason':'No permitted direct closure exists; the required hydrogen-like branch is absent.' if direct==0 else 'Further inequivalence tests required.',
        'contract':CONTRACT,'contract_sha256':digest(CONTRACT),
        'source_root':packet['root'],'source_sha256':sha256(original).hexdigest(),
        'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
        'checks':checks,'direct_closures':direct,'tested_alignments':len(cases),
        'retained_test_state':encode(w),'alignment_results':cases,
        'unresolved':'An attachment law and a retained-structure equivalence derived from outward geometry; neither is selected by incidence reversal alone.',
    }
    dest=BASE/'results/fixed_reversal_closure_conjecture.json'
    dest.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k not in ('alignment_results','retained_test_state')},indent=2))
    if not result['verification_passed']: raise SystemExit(1)

if __name__=='__main__': main()
