type M4 = [[i64; 4]; 4];
type M2 = [[i64; 2]; 2];

fn conjugate_permutation(rho: M4, p: [usize; 4]) -> M4 {
    let mut out = [[0_i64; 4]; 4];
    for i in 0..4 { for j in 0..4 { out[i][j] = rho[p[i]][p[j]]; } }
    out
}

fn partial_trace_env(rho: M4) -> M2 {
    let mut out = [[0_i64; 2]; 2];
    for a in 0..2 { for b in 0..2 { for e in 0..2 {
        out[a][b] += rho[2 * a + e][2 * b + e];
    } } }
    out
}

fn embed_with_env_zero(rho: M2) -> M4 {
    let mut out = [[0_i64; 4]; 4];
    for a in 0..2 { for b in 0..2 { out[2 * a][2 * b] = rho[a][b]; } }
    out
}

fn main() {
    // CNOT in the basis 00,01,10,11 swaps basis vectors 10 and 11.
    let cnot = [0_usize, 1, 3, 2];
    let system_plus: M2 = [[1, 1], [1, 1]]; // unnormalized |+><+|
    let joint = embed_with_env_zero(system_plus);

    let once_global = conjugate_permutation(joint, cnot);
    let once_reduced = partial_trace_env(once_global);
    assert_eq!(once_reduced, [[1, 0], [0, 1]]);

    // Route A: retain the labelled internal occurrence across both steps.
    let twice_global = conjugate_permutation(conjugate_permutation(joint, cnot), cnot);
    let retain_then_cut = partial_trace_env(twice_global);
    assert_eq!(retain_then_cut, system_plus);

    // Route B: push forward after step one, reset the discarded environment,
    // then apply the same reduced step again.
    let reset_joint = embed_with_env_zero(once_reduced);
    let cut_each_then_compose = partial_trace_env(conjugate_permutation(reset_joint, cnot));
    assert_eq!(cut_each_then_compose, [[1, 0], [0, 1]]);
    assert_ne!(retain_then_cut, cut_each_then_compose);

    let mut differing_entries = 0usize;
    for i in 0..2 { for j in 0..2 {
        if retain_then_cut[i][j] != cut_each_then_compose[i][j] { differing_entries += 1; }
    } }

    println!("{{");
    println!("  \"schema\": \"marici.temporal_cut_memory_obstruction.v1\",");
    println!("  \"differing_reduced_entries\": {differing_entries},");
    println!("  \"global_two_step_channel\": \"identity on test state\",");
    println!("  \"stepwise_pushforward_channel\": \"dephasing\",");
    println!("  \"composition_commutes_before_internal_pushforward\": true,");
    println!("  \"composition_commutes_after_stepwise_pushforward\": false");
    println!("}}");
}
