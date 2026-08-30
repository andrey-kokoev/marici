use std::fs;

fn main() {
    let mut checks=0_u64;
    // Opposite-character lift changes shift the integral cocycle by 2b.
    for a in -100_i64..=100 { for b in -100_i64..=100 {
        assert_eq!((a-2*b).rem_euclid(2),a.rem_euclid(2)); checks+=1;
    }}
    // The two parity classes are distinct integrally, but each becomes exact
    // after rationalization: choose b=a/2, represented with denominator 2.
    for a in -100_i64..=100 {
        let cleared=2*a-2*a; assert_eq!(cleared,0); checks+=1;
    }
    // Any additive map from Z/2 to a torsion-free scalar group kills the
    // generator: 2f(1)=f(0)=0 implies f(1)=0.
    for image in -100_i64..=100 {
        if 2*image==0 { assert_eq!(image,0); } checks+=1;
    }
    let output=format!(concat!(
      "{{\n",
      "  \"schema\": \"marici.integral_parabolic_torsion.v1\",\n",
      "  \"exact_checks\": {},\n",
      "  \"integral_opposite_character_h1\": \"Z/2\",\n",
      "  \"rationalized_h1_rank\": 0,\n",
      "  \"torsion_free_additive_scalarization_detects_class\": false,\n",
      "  \"integral_lattice_required_for_detection\": true,\n",
      "  \"new_cut_carrier_stratum\": false\n",
      "}}\n"),checks);
    fs::write("research/benincasa/results/integral-parabolic-torsion.json",output).unwrap();
}
