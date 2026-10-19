#!/usr/bin/env python3
"""Bounded canonical-seed admission screen without executing the owner matcher.

Enumerates the A-H rational library used by the historical n=8 matcher.
Does not test the algebraic four-mass branch, sums or coefficient-valued forms.
"""
import ast
import itertools
import json
import sys
from hashlib import sha256
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT/'research/benincasa/.tmp_sympy'))
sys.path.insert(0, str(ROOT/'research/nima'))
import sympy as s
from dual_r_invariant import generalized_r, theta_coefficients
from dual_spinor_kinematics import momentum_conserving_kinematics, transport_spinor
from momentum_twistor_constructors import four_bracket
from momentum_twistor_super import SuperTwistor, super_line_plane_point
from nnmhv_coherence_paths import compile_nnmhv_histories, terminal_r_state

MATCHER = 'research/nima/check_eight_point_history_positroid_matching.py'
SOURCE = 'research/sources/nima/papers/six-point-nmhv/1212.5605/positive_grassmannian_update.tex'


def library():
    # Literal token definitions only; never import/run the artifact-writing matcher.
    names = {'I456_78','I45_678','I23_456','I234_56','I34_567','I345_67','seeds','groups'}
    env = {}
    for node in ast.parse((ROOT/MATCHER).read_text()).body:
        if isinstance(node, ast.Assign) and all(isinstance(t, ast.Name) and t.id in names for t in node.targets):
            exec(compile(ast.Module(body=[node], type_ignores=[]), MATCHER, 'exec'), {'__builtins__': {}}, env)
    assert set(env['seeds']) == set('ABCDEFGH')
    return env['seeds'], env['groups']


def bracket(vertices):
    qs = [four_bracket(*(vertices[(r+j)%5].z for j in range(1,5))) for r in range(5)]
    q = {}
    for c, v in zip(qs, vertices):
        for k, w in v.chi.items(): q[k] = s.expand(q.get(k,0)+c*w)
    return q, s.prod(qs)


def run(shift, seeds, groups):
    lam, _, x = momentum_conserving_kinematics(
        [(1,j*j+j+1+shift*j) for j in range(1,9)],
        [(1,j**3+2*j+1+shift*j*j) for j in range(1,7)])
    eps = s.Matrix([[0,1],[-1,0]])
    theta = theta_coefficients(lam,8)
    Z = {}
    for j in range(1,9):
        lj = eps*lam[j]
        Z[j] = SuperTwistor(lam[j].col_join(x[j].T*lj),
            {k:s.factor((lj.T*v)[0]) for k,v in theta[j].items() if (lj.T*v)[0] != 0})
    h = compile_nnmhv_histories(8)[3]; st = terminal_r_state(h)
    _, o = generalized_r(lam,x,8,(),h.outer_pair,lam[1].T*eps,lam[5].T*eps)
    lower = transport_spinor(lam,x,st.lower_spinor.vertices)
    _, t = generalized_r(lam,x,8,h.inner_prefix,h.inner_pair,lower,transport_spinor(lam,x,st.upper_spinor.vertices))
    _, u = generalized_r(lam,x,8,h.inner_prefix,h.inner_pair,lower,lam[5].T*eps)
    assert t['xi_coefficients'] == u['xi_coefficients']
    def matrix(q1,q2):
        return s.Matrix([[lam[j][0] for j in range(1,9)], [lam[j][1] for j in range(1,9)],
                         [q1.get(j,0) for j in range(1,9)], [q2.get(j,0) for j in range(1,9)]])
    H = matrix(o['xi_coefficients'],t['xi_coefficients'])
    pivots = H.rref()[1]; assert len(pivots) == 4
    Hpivot = H[:,list(pivots)]
    matches = []; evaluated = 0; singular = []
    for name,(left,right) in seeds.items():
        support_size = 6 if name == 'F' else 7 if name in 'GH' else 8
        for chosen in itertools.combinations(range(1,9),support_size):
            for rotation in range(support_size):
                order = chosen[rotation:]+chosen[:rotation]
                mp = {j:order[j-1] for j in range(1,support_size+1)}
                def point(token):
                    if isinstance(token,int): return Z[mp[token]]
                    return super_line_plane_point(*(Z[mp[j]] for j in token))
                q1,d1 = bracket(tuple(point(z) for z in left))
                q2,d2 = bracket(tuple(point(z) for z in right))
                tag = {'seed':name,'support':list(chosen),'rotation':rotation}
                if d1*d2 == 0:
                    singular.append(tag); continue
                evaluated += 1
                C = matrix(q1,q2); Cpivot = C[:,list(pivots)]
                if Cpivot.det() == 0: continue
                change = Hpivot*Cpivot.inv()
                if change*C != H: continue
                qratio = s.factor(change.det())
                transported_ratio = s.factor(o['prefactor']*t['prefactor']*qratio**4*d1*d2)
                untransported_ratio = s.factor(o['prefactor']*u['prefactor']*qratio**4*d1*d2)
                # Independent exhaustive Plucker check, not just the pivot argument.
                minor_checks = all(s.factor(H[:,list(I)].det()-qratio*C[:,list(I)].det()) == 0
                                   for I in itertools.combinations(range(8),4))
                assert minor_checks
                classes = sorted(sorted(mp[j] for j in g) for g in groups[name])
                matches.append(tag | {'cell_key':{'parallel_classes':classes,'zero_columns':sorted(set(range(1,9))-set(chosen))},
                    'all_70_numerator_coefficients_proportional':minor_checks,
                    'transported_to_seed_full_ratio':str(transported_ratio),
                    'untransported_to_seed_full_ratio':str(untransported_ratio)})
    assert evaluated+len(singular) == 320
    assert not singular, 'Incomplete fixture coverage due to singular seed; retain before drawing a verdict'
    assert matches and all(m['transported_to_seed_full_ratio'] == '1' for m in matches)
    assert all(s.sympify(m['untransported_to_seed_full_ratio']) not in (1,-1) for m in matches)
    return {'shift':shift,'candidate_embeddings':320,'evaluated':evaluated,'singular':singular,
            'fermionic_matches':matches,'unit_or_orientation_reversed_untransported_matches':0}


def main():
    seeds, groups = library()
    runs = [run(shift,seeds,groups) for shift in (0,1,2)]
    keys = [{json.dumps(m['cell_key'],sort_keys=True) for m in r['fermionic_matches']} for r in runs]
    assert all(k == keys[0] for k in keys) and len(keys[0]) == 1
    inputs = [MATCHER,SOURCE,'research/nima/dual_r_invariant.py','research/nima/dual_spinor_kinematics.py',
              'research/nima/momentum_twistor_constructors.py','research/nima/momentum_twistor_super.py',
              'research/nima/nnmhv_coherence_paths.py']
    out = {'schema':'marici.benincasa.untransported-simple-root-seed-admission.v1',
        'history_index':3,'root':[1,1],
        'candidate_class':'A-H rational source seeds with every increasing support embedding and cyclic rotation used by the historical matcher',
        'exclusions':['algebraic four-mass branch','linear combinations of cells','new target maps','coefficient-valued forms','general positive geometries outside this source library'],
        'runs':runs,
        'verdict':'rejected_single_seed_candidate_class',
        'canonical_admission':'open_outside_tested_class',
        'checks':{'960_nonsingular_exact_seed_evaluations':sum(r['evaluated'] for r in runs)==960,
                  'transported_positive_control_matches':True,'same_one_cell_key_across_fixtures':True,
                  'untransported_unit_or_signed_matches_absent':True,'all_matching_70_minors_checked':True},
        'interpretation':'The untransported numerator has the same matching cell key as the transported history, but its full normalization is a nonunit varying ratio. No tested ordinary single-seed canonical representative, even with orientation reversal, realizes this F0.',
        'claim_boundary':'Exact finite-fixture rejection of this explicit library candidate class. Does not refute weighted descent or provide a positive-domain/chart theorem, an exhaustive linear-combination exclusion, or a new Yangian classification.',
        'source_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in inputs},
        'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),'passed':True}
    path = ROOT/'research/benincasa/results/untransported_simple_root_seed_admission.json'
    path.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in out.items() if k not in ('runs','source_sha256')},indent=2))
    for r in runs: print(json.dumps({'shift':r['shift'],'matches':r['fermionic_matches']},indent=2))


if __name__ == '__main__': main()
