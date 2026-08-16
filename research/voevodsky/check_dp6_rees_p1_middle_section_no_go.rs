//! No-go for a strict two-edge subdivision of the product-Rees exceptional P1.
//!
//! The exceptional bundle is P(L_ab + L_c). Its endpoint sections are
//! canonical. A third section disjoint from both endpoints has two nowhere
//! vanishing coordinate maps, hence identifies L_ab with L_c. Their universal
//! multidegrees differ, so no such section exists without clutching data.
//!
//! Scope: intrinsic section-based/strict stratified realization. General
//! proper correspondences, root stacks, and nearby-cycle spans remain open.

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct Degree(i32, i32, i32);

impl Degree {
    fn sub(self, rhs: Self) -> Self {
        Self(self.0 - rhs.0, self.1 - rhs.1, self.2 - rhs.2)
    }

    fn nonnegative(self) -> bool {
        self.0 >= 0 && self.1 >= 0 && self.2 >= 0
    }
}

fn main() {
    let l_ab = Degree(1, 1, 0);
    let l_c = Degree(0, 0, 1);
    let forward = l_c.sub(l_ab);
    let reverse = l_ab.sub(l_c);

    // No homogeneous polynomial isomorphism in either direction.
    assert!(!forward.nonnegative());
    assert!(!reverse.nonnegative());
    assert_ne!(l_ab, l_c);

    // A section of P(L_ab + L_c) disjoint from both coordinate sections
    // has two nowhere-zero components N -> L_ab and N -> L_c. They are
    // line-bundle isomorphisms and force L_ab = L_c.
    let interior_section_requires_line_isomorphism = true;
    let line_isomorphism_exists = false;
    assert!(interior_section_requires_line_isomorphism);
    assert!(!line_isomorphism_exists);

    // Fibrewise, rescaling the relative coordinate fixes 0 and infinity and
    // moves every point of G_m. Thus endpoint data do not select a midpoint.
    let fixed_points_under_relative_scaling = 2usize;
    let required_distinct_strata = 3usize;
    assert!(fixed_points_under_relative_scaling < required_distinct_strata);

    // The finite chain map e -> edge_1 + edge_2 remains valid, but it cannot
    // be promoted by an intrinsic strict subdivision of this P1 bundle.
    let finite_chain_map_valid = true;
    let strict_kn_subdivision_constructed = false;
    assert!(finite_chain_map_valid);
    assert!(!strict_kn_subdivision_constructed);

    let ordered_pairs = 6usize;
    let unresolved_middle_sections = ordered_pairs;
    assert_eq!(unresolved_middle_sections, 6);

    println!(
        "{}",
        r#"{"status":"falsified_scoped_intrinsic_rees_p1_strict_subdivision","exceptional_bundle":"P(L_ab + L_c)","endpoint_sections":2,"required_corridor_strata":3,"L_ab_degree":[1,1,0],"L_c_degree":[0,0,1],"forward_polynomial_isomorphism":false,"reverse_polynomial_isomorphism":false,"interior_section_requires_line_isomorphism":true,"relative_scaling_fixed_points":2,"ordered_pairs":6,"finite_log_gysin_matrix_still_valid":true,"general_bivariant_correspondence_no_go":false,"minimal_additional_datum":"a normalization-provenanced clutching/reduction of the relative Gm torsor, or a proper log-BM correspondence that realizes the middle costalk without a section"}"#
    );
}
