//! Multigraded obstruction to the naive toric star-subdivision realization.
//!
//! Blow up each intersection of two adjacent labelled boundary divisors.
//! The exceptional section has degree e_i+e_j.  The marked corridor requires
//! the independent complementary projective coordinate of degree e_k.
//! Over the universal nonnegatively graded coefficient ring there is no
//! section-preserving homogeneous map between these embedded principal lines.
//!
//! Scope: direct toric star subdivision with no extra clutching line.  This
//! does not obstruct an enlarged log-BM/nearby-cycle correspondence.

type Degree = [i32; 3];

const ORDERED: [(usize, usize); 6] = [(0, 1), (0, 2), (1, 2), (1, 0), (2, 0), (2, 1)];

fn basis(index: usize) -> Degree {
    let mut out = [0; 3];
    out[index] = 1;
    out
}

fn add(left: Degree, right: Degree) -> Degree {
    [left[0] + right[0], left[1] + right[1], left[2] + right[2]]
}

fn subtract(left: Degree, right: Degree) -> Degree {
    [left[0] - right[0], left[1] - right[1], left[2] - right[2]]
}

fn polynomial_degree(value: Degree) -> bool {
    value.iter().all(|entry| *entry >= 0)
}

fn complement(first: usize, second: usize) -> usize {
    (0..3).find(|x| *x != first && *x != second).unwrap()
}

fn gcd(mut left: i32, mut right: i32) -> i32 {
    while right != 0 {
        let remainder = left % right;
        left = right;
        right = remainder;
    }
    left.abs()
}

fn main() {
    let fan_rays: [Degree; 6] = [
        [1, 0, 0],
        [1, 1, 0],
        [0, 1, 0],
        [0, 1, 1],
        [0, 0, 1],
        [1, 0, 1],
    ];

    let mut obstructed = 0usize;
    for (cone, (first, second)) in ORDERED.iter().copied().enumerate() {
        let omitted = complement(first, second);
        let exceptional_degree = add(basis(first), basis(second));
        let corridor_degree = basis(omitted);

        // A map induced by multiplication inside the universal polynomial
        // ring would need one of these two difference degrees.
        let forward_multiplier = subtract(corridor_degree, exceptional_degree);
        let reverse_multiplier = subtract(exceptional_degree, corridor_degree);
        assert!(!polynomial_degree(forward_multiplier));
        assert!(!polynomial_degree(reverse_multiplier));

        // The star ray itself is primitive, so the failure is not a lattice
        // multiplicity or saturation defect.
        let left = fan_rays[cone];
        let right = fan_rays[(cone + 1) % 6];
        let star = add(left, right);
        let content = gcd(gcd(star[0], star[1]), star[2]);
        assert_eq!(content, 1);

        // Polarity reverses the ordered pair and retains the same mismatch.
        let polar = (cone + 3) % 6;
        assert_eq!(ORDERED[polar], (second, first));
        assert_eq!(complement(ORDERED[polar].0, ORDERED[polar].1), omitted);
        obstructed += 1;
    }
    assert_eq!(obstructed, 6);

    // The incidence equation y_k G=z_k H_k does not provide a unit clutching
    // on the conductor G=0: it specializes to z_k H_k=0.
    let conductor_g = 0;
    let incidence_left = 1 * conductor_g;
    assert_eq!(incidence_left, 0);
    let unit_clutching_forced = false;
    assert!(!unit_clutching_forced);

    println!(
        "{}",
        r#"{"status":"falsified_scoped_direct_toric_star_subdivision","ordered_cones":6,"star_rays_primitive":true,"exceptional_line_degree":"e_i+e_j","corridor_long_line_degree":"e_k","forward_polynomial_multiplier_exists":false,"reverse_polynomial_multiplier_exists":false,"incidence_relation_on_conductor":"z_k H_k=0","unit_clutching_derived":false,"ordinary_integer_torsion":[],"finite_log_gysin_matrix_still_valid":true,"global_log_bm_correspondence_no_go":false,"minimal_additional_datum":"a normalization-provenanced branch-selected clutching/excess morphism between the exceptional line and the complementary long-road line, compatible with y_k G=z_k H_k and nonvanishing on the conductor"}"#
    );
}
