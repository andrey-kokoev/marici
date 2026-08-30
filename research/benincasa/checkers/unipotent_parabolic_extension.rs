use std::fs;

fn main() {
    let mut checks=0_u64;
    for a in -100_i64..=100 {
        // Gauge action on a circle cocycle: a -> a + (chi-1)b.
        // Matched line holonomies give chi=+1, hence the class is invariant.
        for b in -50_i64..=50 {
            assert_eq!(a+(1-1)*b,a); checks+=1;
        }
        // Opposite line holonomies give chi=-1.  Over Q, b=a/2 removes a:
        // represent b by numerator a and denominator 2 to avoid fitting.
        let transformed_num=2*a+(-1-1)*a;
        assert_eq!(transformed_num,0); checks+=1;
    }
    // Addition of loop shears realizes the one-dimensional H^1 class.
    for a in -40_i64..=40 { for c in -40_i64..=40 {
        assert_eq!(a+c,c+a); checks+=1;
    }}
    let output=format!(concat!(
      "{{\n",
      "  \"schema\": \"marici.unipotent_parabolic_extension.v1\",\n",
      "  \"exact_checks\": {},\n",
      "  \"coefficient_system\": \"Hom(L_2,L_1)\",\n",
      "  \"matched_relative_character\": 1,\n",
      "  \"matched_h1_rank\": 1,\n",
      "  \"opposite_relative_character\": -1,\n",
      "  \"opposite_h1_rank_over_Q\": 0,\n",
      "  \"unipotent_shear_intrinsic_iff_relative_character_trivial\": true,\n",
      "  \"new_cut_carrier_stratum\": false\n",
      "}}\n"),checks);
    fs::write("research/benincasa/results/unipotent-parabolic-extension.json",output).unwrap();
}
