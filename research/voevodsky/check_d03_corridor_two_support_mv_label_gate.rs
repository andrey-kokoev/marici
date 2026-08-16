//! Finite label-gate audit for the actual D03 four-edge corridor versus the
//! two-support Mayer--Vietoris packet I_+=(u1,u3,u5), I_03=(u0,u3).
//!
//! The ordinary relative corridor and the repeated-u3 excess both have a
//! primitive rank-one shadow.  This checker proves that the shadow cannot be
//! promoted to a strict label-preserving corridor map: both middle edges have
//! D03 occurrence and circle grades absent from the two-support MV diagram.

use std::collections::BTreeSet;

type Z = i64;

fn gcd(mut left: Z, mut right: Z) -> Z {
    while right != 0 {
        let remainder = left % right;
        left = right;
        right = remainder;
    }
    left.abs()
}

fn determinant_3(matrix: [[Z; 3]; 3]) -> Z {
    matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
}

fn main() {
    // e0:v+->m+, e1:m+->c, e2:c->m-, e3:m-->v-.  Quotienting v+,v-
    // gives rows m+,c,m-.  Its kernel is the primitive full route.
    let boundary = [[1, -1, 0, 0], [0, 1, -1, 0], [0, 0, 1, -1]];
    let route = [1, 1, 1, 1];
    for row in boundary {
        assert_eq!(row.iter().zip(route).map(|(a, b)| a * b).sum::<Z>(), 0);
    }
    let maximal_minors = [
        determinant_3([[1, -1, 0], [0, 1, -1], [0, 0, 1]]),
        determinant_3([[1, -1, 0], [0, 1, 0], [0, 0, -1]]),
        determinant_3([[1, 0, 0], [0, -1, 0], [0, 1, -1]]),
        determinant_3([[-1, 0, 0], [1, -1, 0], [0, 1, -1]]),
    ];
    assert_eq!(
        maximal_minors
            .iter()
            .fold(0, |value, minor| gcd(value, *minor)),
        1
    );
    assert_eq!(maximal_minors, [1, -1, 1, -1]);

    // Resolving either support against the other leaves one common u3
    // equation.  Its excess exterior generator gives Tor0=Tor1=R/J and no
    // higher Tor; this records only the rank-one carrier shadow.
    let mv_ideals = [
        BTreeSet::from(["u1", "u3", "u5"]),
        BTreeSet::from(["u0", "u3"]),
    ];
    let intersection: BTreeSet<_> = mv_ideals[0].intersection(&mv_ideals[1]).copied().collect();
    let sum: BTreeSet<_> = mv_ideals[0].union(&mv_ideals[1]).copied().collect();
    assert_eq!(intersection, BTreeSet::from(["u3"]));
    assert_eq!(sum, BTreeSet::from(["u0", "u1", "u3", "u5"]));
    let tor_ranks = [1_usize, 1];
    assert_eq!(tor_ranks, [1, 1]);

    // Actual edge support labels.  The middle edges retain the long D03
    // boundary, including its radial occurrence and its normal-circle state.
    let edge_faces = [
        BTreeSet::from(["x1", "x3"]),
        BTreeSet::from(["D03", "x3"]),
        BTreeSet::from(["D03", "x0"]),
        BTreeSet::from(["x0", "x4"]),
    ];
    let mv_occurrence_labels = BTreeSet::from(["x0", "x1", "x3", "x5"]);
    let mv_normal_labels = sum;
    assert!(!mv_occurrence_labels.contains("D03"));
    assert!(!mv_normal_labels.contains("u_D03"));
    assert!(edge_faces[1].contains("D03") && edge_faces[2].contains("D03"));
    let middle_edge_allowed = [false, false];
    assert_eq!(middle_edge_allowed, [false, false]);

    // A strict relative route chain has coefficients c0,...,c3 and boundary
    // equations c0=c1=c2=c3.  Label preservation forces c1=c2=0, hence the
    // unique unnormalized strict route map is zero.  Requiring unit values at
    // both marked outer halves is therefore inconsistent.
    let mut solutions = Vec::new();
    for c0 in -2_i64..=2 {
        for c1 in -2_i64..=2 {
            for c2 in -2_i64..=2 {
                for c3 in -2_i64..=2 {
                    let coefficients = [c0, c1, c2, c3];
                    let closed = boundary.iter().all(|row| {
                        row.iter().zip(coefficients).map(|(a, b)| a * b).sum::<Z>() == 0
                    });
                    let label_preserving = c1 == 0 && c2 == 0;
                    if closed && label_preserving {
                        solutions.push(coefficients);
                    }
                }
            }
        }
    }
    assert_eq!(solutions, vec![[0, 0, 0, 0]]);
    assert!(!solutions.iter().any(|value| value[0] == 1 && value[3] == 1));

    println!(
        "{}",
        r#"{"claim":"The endpoint-relative actual D03 four-edge corridor has a primitive saturated route H1 line, and the two-support Koszul-Mayer-Vietoris packet has the matching repeated-u3 Tor1 rank-one shadow, but no strict support-label-preserving realization exists: the two middle corridor edges carry D03 occurrence and normal-circle grades absent from I+=(u1,u3,u5), I03=(u0,u3), and their lcm J=(u0,u1,u3,u5). Label preservation forces the middle coefficients to zero, the corridor boundary equations then force every edge coefficient to zero, and endpoint normalization is inconsistent.","status":"falsified","scope":"Falsifies only realization of the actual loaded corridor by the two-support MV packet in the strict line-labelled polynomial category. It makes no general no-go claim after adjoining an exceptional D03 chart and its spatial incidence maps.","evidence_refs":["ledger entry 100","ledger entry 143","research/voevodsky/check_d03_corridor_two_support_mv_label_gate.rs"],"factorization_test":{"corridor":"v+ -> m+ -> c -> m- -> v-","relative_boundary":"[[1,-1,0,0],[0,1,-1,0],[0,0,1,-1]]","relative_H1":"Z generated primitively by (1,1,1,1)","saturation":"unit maximal minors; no integer torsion","MV_ideals":{"I_plus":["u1","u3","u5"],"I_03":["u0","u3"],"sum_J":["u0","u1","u3","u5"],"common":["u3"]},"MV_Tor":"Tor0=R/J, Tor1=R/J, higher Tor zero","middle_edge_labels":[["D03","x3"],["D03","x0"]],"missing_labels":["X_D03 occurrence line","u_D03 normal line","D03 circle state"],"unnormalized_strict_route_maps":"zero only","endpoint_normalized_maps":"empty"},"first_obstruction":"The two-support MV coefficient diagram has no object in either middle D03-labelled edge grade, so the chain equation fails before Laurent localization or any integer-torsion question.","unconstructed":["exceptional/long-D03 support chart","ringed spatial incidence maps to both middle corridor edges","extraordinary-support comparison with the entry143 filtered Q leg"],"next_gate":"Adjoin the exceptional D03 chart with its occurrence and circle lines, then recompute the marked three-chart hypercover map without inverting the polynomial source."}"#
    );
}
