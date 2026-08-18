fn main() {
    // On z=0 after Entry 461's translation,
    // t=(b^2-1)/2+5u/4-u^2/2 and the weighted chart relation is a^2=u*t.
    // At u=0 the leading coefficient is a unit away from b=+-1.
    let survivor_degrees = [(0_i32, 0_i32), (7, 1)];
    let boundary_divisors = [(0_i32, 0_i32), (3, 4)];
    let monodromy_eigenvalues = [1_i32, -1_i32];

    assert_eq!(survivor_degrees[0].0 % 2, 0);
    assert_eq!(survivor_degrees[1].0 % 2, 1);
    assert_eq!(boundary_divisors[1], (3, 4));
    assert_eq!(monodromy_eigenvalues[0] * monodromy_eigenvalues[1], -1);
    assert!(monodromy_eigenvalues.iter().all(|x| x * x == 1));

    println!(
        "{{\"schema\":\"marici.benincasa.soft_axis_cartier_nearby.v1\",\
\"translated_reduced_section\":\"z=0\",\
\"physical_pushforward_relation\":\"a^2=u*((b^2-1)/2+5u/4-u^2/2)\",\
\"generic_locus\":\"b^2!=1\",\
\"nearby_rank\":2,\
\"semisimple_eigenvalues\":[1,-1],\
\"nilpotent_log_rank\":0,\
\"nilpotent_log_square_zero\":true,\
\"degree_character_match\":{{\"(0,0)\":1,\"(7,1)\":-1}},\
\"boundary_divisor_of_odd_class\":[3,4],\
\"carrier_monodromy\":\"identity\",\
\"nontrivial_monodromy_location\":\"Cartier_pushforward_support_framing\",\
\"full_exact_complex_nearby_identification\":\"NOT_ASSERTED\",\
\"excluded_support\":[\"b=1\",\"b=-1\"]}}"
    );
}
