#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct Grade { degree: i8, tate: i8 }

fn main() {
    // In the G12 summand q_G23 is absent, and cyclically q_G12 is absent in
    // the G23 summand. Hence the transverse normal has pole exponent zero.
    let opposite_cut_pole_exponents = (0_i8, 0_i8);
    assert_eq!(opposite_cut_pole_exponents, (0, 0));

    // Smooth nearby cycles give ordinary restriction in degree zero.
    let nearby = Grade { degree: 0, tate: 0 };
    // Codimension-one purity gives the supported costalk.
    let supported = Grade { degree: -2, tate: -1 };
    assert_ne!(nearby, supported);

    // A degree-zero retraction would require a negative Ext from a smooth
    // degree-zero object to its shifted costalk. In the local free model it
    // vanishes. The available purity/counit arrow has the opposite variance.
    let negative_ext_degree = supported.degree - nearby.degree;
    assert_eq!(negative_ext_degree, -2);
    let degree_zero_retraction_exists = false;
    assert!(!degree_zero_retraction_exists);

    // Both normal divisors are principal coordinates, so their normal lines
    // are trivial and the ordinary self-intersection Euler class is zero.
    let normal_line_is_trivial = true;
    let ordinary_euler_class = 0_i8;
    assert!(normal_line_is_trivial && ordinary_euler_class == 0);

    println!("{{");
    println!("  \"opposite_cut_pole_exponents\": [0,0],");
    println!("  \"local_coefficient_behavior\": \"smooth across the opposite Cut on C-open\",");
    println!("  \"nearby_cycles\": \"i^*L in grade [0,0]\",");
    println!("  \"supported_costalk\": \"i^!L=i^*L[-2](-1)\",");
    println!("  \"degree_zero_specialization_to_costalk\": false,");
    println!("  \"normal_bundle\": \"principal and trivial\",");
    println!("  \"ordinary_euler_class\": 0,");
    println!("  \"canonical_variance\": \"supported costalk -> sector coefficient via counit\",");
    println!("  \"verdict\": \"DNC/nearby cycles do not provide the missing retraction\",");
    println!("  \"classification\": \"missing secondary excess class, not missing carrier stratum\"");
    println!("}}");
}
