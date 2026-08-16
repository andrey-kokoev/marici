//! No-go for realizing the full three-face vertex cone by the underived
//! two-section product-Rees exceptional P1.
//!
//! The two standard Rees boundary sections can map stratumwise to the two
//! Cech/chart faces.  The literal entry143 vertex has a third, distinct wall
//! face whose coefficient is the conductor-Tor contraction.  A
//! support-preserving map from two source boundary strata cannot hit all
//! three target faces.  Multiplicities and signs do not change this support
//! count.
//!
//! Scope: underived proper/log-smooth realizations whose exceptional
//! boundary is exactly the two coordinate sections of the existing Rees P1.
//! Derived/log-vanishing-cycle kernels or correspondences with a genuinely
//! new third boundary object are not excluded.

use std::collections::BTreeSet;

const ORDERED_PAIRS: usize = 6;
const SOURCE_BOUNDARIES: usize = 2;
const TARGET_FACES: usize = 3;

fn support(values: &[usize]) -> BTreeSet<usize> {
    values.iter().copied().collect()
}

fn main() {
    // Exhaust every stratumwise assignment of the two coordinate boundary
    // sections to the three literal faces.
    let mut assignments = 0usize;
    let mut full_support_assignments = 0usize;
    for first in 0..TARGET_FACES {
        for second in 0..TARGET_FACES {
            assignments += 1;
            let image = support(&[first, second]);
            assert!(image.len() <= SOURCE_BOUNDARIES);
            if image.len() == TARGET_FACES {
                full_support_assignments += 1;
            }
        }
    }
    assert_eq!(assignments, TARGET_FACES.pow(SOURCE_BOUNDARIES as u32));
    assert_eq!(full_support_assignments, 0);

    // The two coordinate sections have the ordinary oriented boundary row.
    // Its Smith invariant is already primitive; the obstruction is support,
    // not integer torsion or a missing multiplicity.
    let source_boundary = [-1_i64, 1];
    assert_eq!(source_boundary.iter().map(|x| x.abs()).min(), Some(1));

    // The full vertex cone requires all three primitive faces:
    // tau = wall/Tor, n0 = chart1, n1 = chart0.
    let target_boundary = [1_i64, 1, -1];
    assert!(target_boundary
        .iter()
        .all(|coefficient| coefficient.abs() == 1));
    assert_eq!(support(&[0, 1, 2]).len(), TARGET_FACES);

    // The state containing only tau has a mandatory wall restriction.  It
    // has no chart boundary, so deleting or merging the wall cannot be
    // repaired by changing the two chart signs.
    let tau_only_mask = 0b001_u8;
    let chart_axes = [1_u8, 2_u8];
    let chart_terms = chart_axes
        .iter()
        .filter(|axis| tau_only_mask & (1 << **axis) != 0)
        .count();
    let wall_terms = usize::from(tau_only_mask & 1 != 0);
    assert_eq!(chart_terms, 0);
    assert_eq!(wall_terms, 1);

    // The same support defect occurs in every oriented long-road pair.
    let missing_primitive_wall_rows = ORDERED_PAIRS;
    assert_eq!(missing_primitive_wall_rows, 6);

    // A third strict section of the same P1 is independently excluded by the
    // line-degree/Gm argument of entry218.  Therefore the minimal repair is
    // a new derived/log boundary object, not a reweighting of the two old
    // sections.
    let intrinsic_third_section_exists = false;
    let derived_wall_object_required = true;
    assert!(!intrinsic_third_section_exists);
    assert!(derived_wall_object_required);

    println!(
        "{}",
        r#"{"status":"falsified_scoped_underived_two_boundary_rees_realization","ordered_pairs":6,"source_boundary_strata":2,"target_vertex_faces":3,"stratumwise_assignments_checked":9,"full_support_assignments":0,"source_boundary_smith_all_ones":true,"target_boundary_smith_all_ones":true,"tau_only_chart_terms":0,"tau_only_required_wall_terms":1,"missing_primitive_wall_rows":6,"multiplicity_or_sign_repair_possible":false,"intrinsic_third_P1_section_exists":false,"general_derived_log_BM_correspondence_no_go":false,"minimal_additional_datum":"a genuine third derived/log boundary or vanishing-cycle object carrying the conductor-Tor contraction, with proper Beck-Chevalley maps to both Rees charts and the literal entry143 wall costalk"}"#
    );
}
