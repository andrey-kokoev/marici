"""Expose the geometric triangle-line factor inside native neutron L.
Standard-library exact arithmetic. Imports retained-source definitions only;
no producer entrypoint or pure producer assembler is called.
"""
import json
import sys
from itertools import product as tuples
from pathlib import Path
from check_packet_handoff_naturality_09 import (
    ROOT, A, F, ZERO, ONE, CI, product, plus, scaled, encode, identity,
    invert, sub, adj, trace, rank, vec, norm, digest, read, load,
    representations, native_geometries, independent_encoders, qmode,
    diag, projector, witness, triangle, GEOMETRY)

CONTRACT = ROOT/'research/strominger/contracts/double-c-neutron-factorization.v1.json'
PRIOR = ROOT/'research/strominger/results/packet-handoff-naturality-10-v1.json'
OUT = ROOT/'research/strominger/results/double-c-neutron-factorization-v1.json'


def mm(*matrices):
    out = matrices[0]
    for m in matrices[1:]:
        out = product(out, m)
    return out


def metric_frame(K, H, n):
    gram = mm(adj(K), H, K)
    decoder = mm(invert(gram, n), adj(K), H)
    return decoder, gram


def kernel_witness(P, L, n):
    delta = mm(L, sub(identity(n), P))
    assert delta
    j = next(j for i, j in delta)
    x = product(sub(identity(n), P), {(j, 0): ONE})
    assert not product(P, x) and product(L, x)
    return {'input': encode(x), 'first_map_output': encode(product(P, x)),
            'native_L_output': encode(product(L, x))}


def main():
    contract = read(CONTRACT)
    prior = read(PRIOR)
    checks = {}

    def ck(name, value):
        checks[name] = bool(value)
        assert value, name

    ck('prior_scientific_receipt_passes', prior['status'] == 'pass' and all(prior['checks'].values()))
    ck('all_prior_scientific_source_pins_current', all(digest(ROOT/p) == h for p, h in prior['source_sha256'].items()))
    objects, binding, pins = load()
    reps = representations(objects, binding)
    geometries, placements = native_geometries(objects)
    data = independent_encoders(objects, geometries, placements)
    o = objects['neutron']; g = geometries['neutron']; n = o['n']
    H = diag([A(x) for x in o['metric']]); E = data['neutron']['E']
    Eleft = mm(diag([ONE/A(x) for x in o['metric']]), adj(E))
    L, G, N = [o['ops'][s] for s in 'LGN']
    qs = [qmode([g['points'][v] for v in cell]) for cell in g['base']['faces']]
    Kworld = {(3*t+i, t): x for t, q in enumerate(qs) for (i, j), x in q.items()}
    K = product(Eleft, Kworld)
    D, gram = metric_frame(K, H, 18)
    Pi = product(K, D)
    ck('eighteen_source_geometric_modes_pull_back_exactly', product(E, K) == Kworld)
    ck('native_embedding_left_inverse', product(Eleft, E) == identity(n))
    ck('line_Gram_positive_diagonal', all(i == j and not any(x.c[1:]) and x.c[0] > 0 for (i, j), x in gram.items()) and len(gram) == 18)
    ck('triangle_line_encoder_rank18', rank(K, n, 18) == 18)
    ck('triangle_line_metric_left_inverse', product(D, K) == identity(18))
    ck('triangle_projector_native_metric_selfadjoint', product(adj(Pi), H) == product(H, Pi))
    ck('triangle_projector_idempotent_rank18', product(Pi, Pi) == Pi and trace(Pi) == A(18))
    worldPi = {(3*t+i, 3*t+j): x for t, q in enumerate(qs) for (i, j), x in projector(q, identity(3)).items()}
    ck('triangle_projector_is_direct_geometric_line_selection', mm(E, Pi) == product(worldPi, E))

    # Source incidence, not a factorization fitted to L.
    J = {(t, s): ONE for s, patch in enumerate(g['patches']) for t in patch}
    ck('three_disjoint_six_triangle_patches_cover_source', len(J) == 18 and sorted(t for t, s in J) == list(range(18)) and all(sum(s == a for t, s in J) == 6 for a in range(3)))
    Kpatch = product(K, J)
    Dpatch, patchGram = metric_frame(Kpatch, H, 3)
    S = product(Dpatch, K)
    ck('patch_projector_reproduces_original_L_on_all_raw_inputs', product(Kpatch, Dpatch) == L)
    ck('both_native_L_triangle_absorption_squares', product(L, Pi) == product(Pi, L) == L)
    ck('patch_decoder_is_source_norm_weighted_mean', S == mm(invert(patchGram, 3), adj(J), gram))
    ck('patch_incidence_is_split_by_weighted_mean', product(S, J) == identity(3))
    ck('full_L_factorization_preserves_every_raw_reader', mm(E, Kpatch, S, D) == product(E, L))
    ck('patch_aggregation_has_rank3', rank(S, 3, 18) == 3)

    # Retain original native aligned carrier and original N-to-full-raw target.
    fG = o['f']['G']; Kg, Dg = fG['K'], fG['D']
    B = mm(Dg, G, Kpatch)
    T = [D, S, B, product(N, Kg)]
    frames = [identity(n), K, Kpatch, Kg]
    decoders = [identity(n), D, Dpatch, Dg]
    primitive = [Pi, L, G, N]
    ck('all_four_exposed_geometric_reader_squares', all(mm(E, frames[(s+1)%4], T[s]) == mm(E, primitive[s], frames[s]) for s in range(4)))
    ck('exposed_raw_cycle_is_original_native_N', mm(T[3], T[2], T[1], T[0]) == N)
    ck('all_four_rooted_cycles_are_original_N_restrictions', all(mm(T[(s+3)%4], T[(s+2)%4], T[(s+1)%4], T[s]) == mm(decoders[s], N, frames[s]) for s in range(4)))
    actions = []
    for W in reps['neutron']['raw']:
        induced = [mm(d, W, k) for d, k in zip(decoders, frames)]
        ck('native_C3_all_carrier_embedding_squares', all(product(W, k) == product(k, a) for k, a in zip(frames, induced)))
        ck('native_C3_all_four_step_intertwiners', all(product(induced[(s+1)%4], T[s]) == product(T[s], induced[s]) for s in range(4)))
        ck('native_C3_preserves_line_metric', mm(adj(induced[1]), gram, induced[1]) == gram)
        ck('native_C3_preserves_geometric_patch_incidence', product(induced[1], J) == product(J, induced[2]))
        avg = scaled(A(F(1,3)), plus(identity(18), induced[1], product(induced[1], induced[1])))
        ck('line_C3_fixed_rank6_retained_as_distinct_from_native_C12', trace(avg) == A(6) and mm(K, avg, D) == product(Pi, G))
        actions.append({'triangle_action': encode(induced[1]), 'patch_action': encode(induced[2])})

    # A nonmonomial complex change of line coordinates carries every attachment.
    Z = plus(identity(18), {(0,1): CI/A(2)})
    Zi = sub(identity(18), {(0,1): CI/A(2)})
    K2, D2, J2, S2 = product(K,Z), product(Zi,D), product(Zi,J), product(S,Z)
    gram2 = mm(adj(Z),gram,Z)
    ck('line_frame_transport_preserves_full_native_factor', product(K2,D2) == Pi and product(K2,J2) == Kpatch and mm(Kpatch,S2,D2) == L)
    ck('line_frame_transport_carries_metric_and_weighted_aggregation', gram2 == mm(adj(K2),H,K2) and S2 == mm(invert(patchGram,3),adj(J2),gram2))
    A2 = mm(Zi,induced[1],Z)
    ck('line_frame_transport_carries_native_action_and_patch_maps', product(W,K2) == product(K2,A2) and product(A2,J2) == product(J2,induced[2]) and product(S2,A2) == product(induced[2],S2))

    # Strong rivals retain exact witnesses rather than just image comparisons.
    lost = sub(L,N)
    g_witness = kernel_witness(G,L,n)
    ck('original_aligned_C12_cannot_factor_full_L', rank(lost,n,n) == 2 and not product(G,lost) and product(L,lost) == lost)
    charworld = {(3*t+i,3*t+j): x for t,cell in enumerate(g['base']['faces']) for (i,j),x in triangle([g['points'][v] for v in cell])['E'].items()}
    Char = mm(Eleft,charworld,E)
    ck('oblique_character_same_triangle_line_image', product(Char,Char) == Char and product(Pi,Char) == Char and product(Char,Pi) == Pi)
    ck('oblique_character_preserves_patch_image_but_changes_full_L_reader', product(Char,L) == L and product(L,Char) != L)
    char_witness = kernel_witness(Char,L,n)
    uniform = scaled(A(F(1,6)),adj(J))
    wrong_uniform = mm(Kpatch,uniform,D)
    ck('uniform_patch_mean_changes_full_raw_L_reader', wrong_uniform != L and product(uniform,J) == identity(3))

    # Second geometric matching: same line carrier and native G/N, different L.
    geo = read(GEOMETRY); panels = geo['belt_faces']
    centers = ['F_'+'_'.join(sorted(f)) for f in panels]
    owners = [centers.index(cell[0]) for cell in g['base']['faces']]
    W = reps['neutron']['raw'][0]
    # Derive the panel permutation directly from the native geometric rotation.
    from check_packet_handoff_naturality_09 import geometry_action
    _,_,rename = geometry_action(g,reps['neutron']['V'][0])
    faceperm = [next(j for j,f in enumerate(panels) if set(f) == {rename[v] for v in panel}) for panel in panels]
    matchings = []
    for adjacent in [j for j in range(1,6) if len(set(panels[0]) & set(panels[j])) == 2]:
        pair = (0,adjacent); matching = []
        for _ in range(3):
            matching.append(pair); pair = tuple(faceperm[i] for i in pair)
        matchings.append(matching)
    alternatives = []
    for matching in matchings:
        Jalt = {(t,s):ONE for s,pair in enumerate(matching) for t,a in enumerate(owners) if a in pair}
        Kalt = product(K,Jalt); Dalt,_ = metric_frame(Kalt,H,3); Lalt = product(Kalt,Dalt)
        ck('geometric_matching_alternatives_factor_through_same_line_carrier', product(Lalt,Pi) == product(Pi,Lalt) == Lalt)
        ck('geometric_matching_alternatives_preserve_native_G_N_actions', product(Lalt,G) == product(G,Lalt) == N and product(W,Lalt) == product(Lalt,W))
        alternatives.append(Lalt)
    other = next(a for a in alternatives if a != L)
    ck('second_geometric_matching_has_full_L_residual_rank4', any(a == L for a in alternatives) and rank(sub(other,L),n,n) == 4)

    # Open windows, coarse cycles and exposed factor states are different tests.
    protocols = [r for r in prior['source_branch_and_primitive_role_descent']['source_family_rectangular_protocols'] if r['variant'] == 'native']
    windows = {r['source']: [''.join(w['roles']) for w in r['windows']] for r in protocols}
    surviving = [list(p) for p in tuples(range(3),repeat=3) if all('MM' not in windows[name][s] for name,s in zip(('proton','neutron','electron'),p))]
    ck('open_window_grammar_retains_nine_policies_neutron_phase1', len(surviving) == 9 and all(p[1] == 1 for p in surviving))
    coarse = {r['source']: ''.join(r['windows'][0]['roles']) for r in protocols}
    cyclic_ok = lambda word: all(word[i] != 'M' or word[(i-1)%len(word)] == word[(i+1)%len(word)] == 'C' for i in range(len(word)))
    ck('unchanged_three_phase_cycles_surround_M_only_for_proton_electron', {name:cyclic_ok(word) for name,word in coarse.items()} == {'proton':True,'neutron':False,'electron':True})
    ck('exposed_four_state_neutron_cycle_surrounds_both_M_states', cyclic_ok('MCMC'))
    ck('operator_rule_remains_hypothesis_not_physical_input', contract['instruction_is_evidence'] is False and contract['physical_M_C_grading_assumed'] is False)

    pins.update(prior['source_sha256'])
    for path in (CONTRACT,PRIOR,Path(__file__).resolve()):
        pins[path.relative_to(ROOT).as_posix()] = digest(path)
    for module in tuple(sys.modules.values()):
        path = getattr(module,'__file__',None)
        if path:
            path = Path(path).resolve()
            if path.suffix == '.py' and path.is_relative_to(ROOT/'research'):
                rel = path.relative_to(ROOT).as_posix()
                assert rel not in pins or pins[rel] == digest(path)
                pins[rel] = digest(path)
    ck('all_final_source_pins_current',all(digest(ROOT/p) == h for p,h in pins.items()))
    report = {'schema':'marici.double-c-neutron-factorization-check.v1','status':'pass','checks':checks,
        'dimensions':{'raw':36,'geometric_triangle_lines':18,'patch_modes':3,'native_aligned':12},
        'exposed_roles':['M','C','M','C'],'native_L_factorization':'K_patch S D_triangle',
        'source_triangle_patches':g['patches'],
        'maps':{name:encode(m) for name,m in [('line_encoder',K),('line_decoder',D),('line_Gram',gram),('line_projector',Pi),('patch_incidence',J),('weighted_patch_mean',S),('patch_encoder',Kpatch),('patch_Gram',patchGram),('patch_to_aligned',B)]},
        'native_actions':actions,
        'rivals':{'native_G_only':{'lost_local_rank':2,'kernel_witness':g_witness},
                  'oblique_character':{'L_reader_residual_rank':rank(sub(product(L,Char),L),n,n),'kernel_witness':char_witness},
                  'uniform_mean':witness(L,wrong_uniform,n),
                  'alternate_geometric_matching':witness(L,other,n)},
        'open_window_surviving_policies':surviving,'unchanged_coarse_cycles':coarse,
        'coarse_neutron_cycle_satisfies_surrounding_rule':False,
        'geometric_factor_refinement_satisfies_surrounding_rule':True,
        'native_primitive_L_unchanged':True,'exposed_factor_is_new_native_primitive':False,
        'physical_M_C_grading_verified':False,'phase_origin_uniquely_selected':False,
        'producer_entrypoints_executed':False,'pure_producer_functions_executed':False,
        'source_sha256':pins}
    OUT.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':'pass','check_groups':len(checks),'dimensions':report['dimensions'],
        'native_G_lost_rank':2,'oblique_reader_residual_rank':report['rivals']['oblique_character']['L_reader_residual_rank'],
        'uniform_reader_residual_rank':report['rivals']['uniform_mean']['difference_rank'],
        'alternate_matching_residual_rank':report['rivals']['alternate_geometric_matching']['difference_rank'],
        'open_window_policies':len(surviving)},indent=2))


if __name__ == '__main__':
    main()
