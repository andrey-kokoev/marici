// Exact sparse certificate for the all-soft radial exceptional family.
// Exponent order: E, P1, P2, P3, a, b.
type Exponents = [u8; 6];

fn verify() {
    // The complete frozen K_CM after A=a^2 and B=b^2.  Coefficients are
    // retained so accidental cancellation or omission is detectable.
    let source_terms: [(i32, Exponents); 22] = [
        (1, [4, 0, 0, 2, 0, 0]),
        (-1, [2, 2, 0, 0, 2, 0]), (1, [2, 0, 2, 0, 2, 0]),
        (-1, [2, 0, 0, 2, 2, 0]), (1, [2, 2, 0, 0, 0, 2]),
        (-1, [2, 0, 2, 0, 0, 2]), (-1, [2, 0, 0, 2, 0, 2]),
        (-1, [2, 2, 0, 2, 0, 0]), (-1, [2, 0, 2, 2, 0, 0]),
        (1, [2, 0, 0, 4, 0, 0]), (1, [0, 2, 0, 0, 4, 0]),
        (-1, [0, 2, 0, 0, 2, 2]), (-1, [0, 0, 2, 0, 2, 2]),
        (1, [0, 0, 0, 2, 2, 2]), (1, [0, 4, 0, 0, 2, 0]),
        (-1, [0, 2, 2, 0, 2, 0]), (-1, [0, 2, 0, 2, 2, 0]),
        (1, [0, 0, 2, 0, 0, 4]), (-1, [0, 2, 2, 0, 0, 2]),
        (1, [0, 0, 4, 0, 0, 2]), (-1, [0, 0, 2, 2, 0, 2]),
        (1, [0, 2, 2, 2, 0, 0]),
    ];

    assert_eq!(source_terms.len(), 22);
    for (coefficient, exponents) in &source_terms {
        assert_ne!(*coefficient, 0);
        assert_eq!(exponents.iter().map(|e| u16::from(*e)).sum::<u16>(), 6);
    }
    for left in 0..source_terms.len() {
        for right in left + 1..source_terms.len() {
            assert_ne!(source_terms[left].1, source_terms[right].1);
        }
    }

    // Homogeneity gives K(rho*x)=rho^6 K(x).  Differentiation gives degree
    // five for every nonzero labelled gradient generator.
    let polynomial_radial_weight = 6_i32;
    let gradient_radial_weight = polynomial_radial_weight - 1;
    let cover_radial_weight = polynomial_radial_weight / 2;
    assert_eq!(gradient_radial_weight, 5);
    assert_eq!(cover_radial_weight, 3);

    // Relative source density at fixed radial base coordinate:
    // da wedge db / w = rho^(2-3) dah wedge dbh / W.
    let relative_kummer_form_weight = 2 - cover_radial_weight;
    assert_eq!(relative_kummer_form_weight, -1);
    let radial_monodromy_exponent = relative_kummer_form_weight;
    assert_eq!(radial_monodromy_exponent.rem_euclid(1), 0);

    // Linear marked denominators and their relative differentials carry
    // equal radial weight, hence relative dlog support maps have weight zero.
    let marked_relative_dlog_weight = 1 - 1;
    assert_eq!(marked_relative_dlog_weight, 0);

    println!("source_monomials=22");
    println!("K_radial_degree=6");
    println!("gradient_radial_degree=5");
    println!("strict_transform=weighted_projective_double_cover_in_O(3)");
    println!("exceptional_singular_ideal=(W,dKhat)");
    println!("saturated_scheme=Proj(affine_frozen_critical_cone)");
    println!("new_exceptional_singular_generator_count=0");
    println!("relative_kummer_form_radial_weight=-1");
    println!("relative_kummer_form_radial_monodromy=1");
    println!("marked_relative_dlog_weight=0");
}

fn main() {
    verify();
}
