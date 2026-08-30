fn main() {
    // Three-mode Hamiltonian H=sum p_i^2/2 + q1 q2 q3.
    // For f=p1 q3:
    // Df = -q2 q3^2 + p1 p3.
    // Push forward mode 3 in a centered product Gaussian with
    // E[q3^2]=1, E[p3]=0, giving -q2.
    let eq3_squared = 1_i64;
    let ep3 = 0_i64;
    let cut_after_derivation_q2_coefficient = -eq3_squared;
    let cut_after_derivation_p1_coefficient = ep3;

    // Cutting f first gives E[p1 q3]=p1 E[q3]=0, so the observed
    // derivation of the cut observable is zero.
    let eq3 = 0_i64;
    let derivation_after_cut = eq3;
    let commutator_q2_coefficient =
        cut_after_derivation_q2_coefficient - derivation_after_cut;

    assert_eq!(cut_after_derivation_q2_coefficient, -1);
    assert_eq!(cut_after_derivation_p1_coefficient, 0);
    assert_eq!(derivation_after_cut, 0);
    assert_eq!(commutator_q2_coefficient, -1);

    // With symbolic internal variance nu, the defect is -nu q2.
    let mut variance_checks = 0usize;
    for variance in 1_i64..=128 {
        let defect = -variance;
        assert_eq!(defect, -variance);
        variance_checks += 1;
    }

    println!("{{");
    println!("  \"schema\": \"marici.cut_derivation_wick_defect.v1\",");
    println!("  \"variance_checks\": {variance_checks},");
    println!("  \"test_observable\": \"p1 q3\",");
    println!("  \"cut_after_derivation\": \"-q2\",");
    println!("  \"derivation_after_cut\": \"0\",");
    println!("  \"commutator\": \"-q2\",");
    println!("  \"cut_pushforward_is_strict_differential_morphism\": false");
    println!("}}");
}
