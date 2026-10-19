#!/usr/bin/env python3
"""Bounded owner-library screen of transported history 6; no sign fitting."""
import itertools
import json
import sys
from hashlib import sha256
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT/'research/benincasa/.tmp_sympy'))
sys.path.insert(0, str(ROOT/'research/nima'))
sys.path.insert(0, str(Path(__file__).resolve().parent))
import sympy as s
from check_untransported_simple_root_seed_admission import library, bracket, MATCHER
from dual_r_invariant import generalized_r, theta_coefficients
from dual_spinor_kinematics import momentum_conserving_kinematics, transport_spinor
from momentum_twistor_super import SuperTwistor, super_line_plane_point
from nnmhv_coherence_paths import compile_nnmhv_histories, terminal_r_state


def run(shift):
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
    h = compile_nnmhv_histories(8)[6]
    st = terminal_r_state(h)
    _, o = generalized_r(lam,x,8,(),h.outer_pair,
        lam[h.outer_pair[0]-1].T*eps,lam[h.outer_pair[1]].T*eps)
    _, t = generalized_r(lam,x,8,h.inner_prefix,h.inner_pair,
        transport_spinor(lam,x,st.lower_spinor.vertices),
        transport_spinor(lam,x,st.upper_spinor.vertices))
    def matrix(q,r):
        return s.Matrix([[lam[j][0] for j in range(1,9)], [lam[j][1] for j in range(1,9)],
                         [q.get(j,0) for j in range(1,9)], [r.get(j,0) for j in range(1,9)]])
    H = matrix(o['xi_coefficients'],t['xi_coefficients'])
    piv = list(H.rref()[1]); assert len(piv) == 4
    seeds, groups = library()
    matches = []; singular = []; evaluated = 0
    for name,(left,right) in seeds.items():
        size = 6 if name == 'F' else 7 if name in 'GH' else 8
        for chosen in itertools.combinations(range(1,9),size):
            for rotation in range(size):
                order = chosen[rotation:]+chosen[:rotation]
                mp = {j:order[j-1] for j in range(1,size+1)}
                def point(token):
                    if isinstance(token,int): return Z[mp[token]]
                    return super_line_plane_point(*(Z[mp[j]] for j in token))
                q,dq = bracket(tuple(point(z) for z in left))
                r,dr = bracket(tuple(point(z) for z in right))
                tag = {'seed':name,'support':list(chosen),'rotation':rotation}
                if dq*dr == 0:
                    singular.append(tag); continue
                evaluated += 1
                C = matrix(q,r)
                if C[:,piv].det() == 0: continue
                M = H[:,piv]*C[:,piv].inv()
                if M*C != H: continue
                scale = s.factor(M.det())
                checks = all(s.factor(H[:,list(I)].det()-scale*C[:,list(I)].det()) == 0
                             for I in itertools.combinations(range(8),4))
                assert checks
                ratio = s.factor(o['prefactor']*t['prefactor']*scale**4*dq*dr)
                matches.append(tag | {'cell_key':{
                    'parallel_classes':sorted(sorted(mp[j] for j in g) for g in groups[name]),
                    'zero_columns':sorted(set(range(1,9))-set(chosen))},
                    'all_70_numerator_coefficients_proportional':checks,
                    'transported_full_superfunction_ratio':str(ratio)})
    assert evaluated+len(singular) == 320 and not singular
    assert matches and all(m['transported_full_superfunction_ratio'] == '1' for m in matches)
    keys = {json.dumps(m['cell_key'],sort_keys=True) for m in matches}
    assert len(keys) == 1
    assert all(m['seed'] == 'F' and m['support'] == [1,2,3,5,6,8] for m in matches)
    return {'shift':shift,'history_index':6,'outer_pair':list(h.outer_pair),
            'inner_pair':list(h.inner_pair),'boundary_updates':str(h.boundary_updates),
            'candidate_embeddings':320,'evaluated':evaluated,'singular':singular,
            'matches':matches,'distinct_matched_cell_keys':len(keys)}


def main():
    fixtures = [run(shift) for shift in (0,1,2)]
    out = {'schema':'marici.benincasa.history6-seed-admission.v1',
           'fixtures':fixtures,'owning_matcher':MATCHER,
           'owning_matcher_sha256':sha256((ROOT/MATCHER).read_bytes()).hexdigest(),
           'decision':'Transported history 6 identifies the six-active-label F top cell. Intrinsic corner orientation and residues remain uncomputed.',
           'not_admitted':['untransported K0','weighted nine-form map','global BCFW orientation','four-cell corner cancellation','historical bundle replay'],
           'scope':'Exact rational fixture seed identification, not a boundary-form or global identity proof.',
           'passed':True}
    path = ROOT/'research/benincasa/results/history6_seed_admission.json'
    path.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__ == '__main__': main()
