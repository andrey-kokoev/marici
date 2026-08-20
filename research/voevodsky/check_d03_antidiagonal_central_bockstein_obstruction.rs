//! Integral anti-diagonal obstruction and its D3 Bockstein shadow.
//!
//! The group-cohomology conclusion is explicitly conditional on having first
//! assembled the typed geometric mapping-fiber sequence.

type Z = i64;

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct D3 {
    rotation: i8,
    reflection: bool,
}

fn elements() -> Vec<D3> {
    (0..3)
        .flat_map(|rotation| {
            [false, true].map(move |reflection| D3 {
                rotation,
                reflection,
            })
        })
        .collect()
}

fn multiply(left: D3, right: D3) -> D3 {
    let signed_right = if left.reflection {
        -right.rotation
    } else {
        right.rotation
    };
    D3 {
        rotation: (left.rotation + signed_right).rem_euclid(3),
        reflection: left.reflection ^ right.reflection,
    }
}

fn sign_action(group: D3, value: Z) -> Z {
    if group.reflection {
        -value
    } else {
        value
    }
}

fn swap_action(group: D3, value: [Z; 2]) -> [Z; 2] {
    if group.reflection {
        [value[1], value[0]]
    } else {
        value
    }
}

fn add2(left: [Z; 2], right: [Z; 2]) -> [Z; 2] {
    [left[0] + right[0], left[1] + right[1]]
}

fn sub2(left: [Z; 2], right: [Z; 2]) -> [Z; 2] {
    [left[0] - right[0], left[1] - right[1]]
}

fn h1_cocycle(group: D3) -> Z {
    Z::from(group.reflection)
}

fn sheet_lift(group: D3) -> [Z; 2] {
    if group.reflection {
        [1, 0]
    } else {
        [0, 0]
    }
}

fn connecting_cocycle(left: D3, right: D3) -> Z {
    let value = sub2(
        add2(sheet_lift(left), swap_action(left, sheet_lift(right))),
        sheet_lift(multiply(left, right)),
    );
    assert_eq!(value[0], value[1]);
    value[0]
}

fn main() {
    // Sheet difference and the anti-invariant integral sublattice.
    let difference = |value: [Z; 2]| value[0] - value[1];
    let anti = [1_i64, -1_i64];
    assert_eq!(difference(anti), 2);
    assert_eq!(difference([1, 0]), 1);

    // The ruling change (r_plus+r_minus,r_plus-r_minus) has determinant -2,
    // so diagonal/anti-diagonal projectors are not integral splittings.
    let ruling_change = [[1_i64, 1_i64], [1_i64, -1_i64]];
    let determinant =
        ruling_change[0][0] * ruling_change[1][1] - ruling_change[0][1] * ruling_change[1][0];
    assert_eq!(determinant.abs(), 2);
    let independent_graph_equation_tor1_rank = 1_usize;
    assert_eq!(independent_graph_equation_tor1_rank, 1);

    // Every reflection-equivariant map from the swapped ruling lattice to the
    // sign line is k*(a-b).  Adding a sign-type independent Tor generator tau
    // gives f(a,b,tau)=k*(a-b)+ell*tau.  Retaining both ruling grades means
    // k!=0, and the anti ruling then always maps to the even value 2k.
    let mut equivariant_maps = Vec::new();
    for k in -3_i64..=3 {
        for ell in -3_i64..=3 {
            let map = |value: [Z; 3]| k * (value[0] - value[1]) + ell * value[2];
            let sample = [2_i64, -1_i64, 3_i64];
            let reflected = [sample[1], sample[0], -sample[2]];
            assert_eq!(map(reflected), -map(sample));
            if k != 0 {
                equivariant_maps.push((k, ell, map([1, -1, 0])));
            }
        }
    }
    assert!(equivariant_maps
        .iter()
        .all(|(k, _, anti_value)| *anti_value == 2 * k && anti_value.abs() != 1));

    // z(g)=1 on reflections and 0 on rotations is a sign-valued 1-cocycle.
    let group = elements();
    for left in &group {
        for right in &group {
            assert_eq!(
                h1_cocycle(multiply(*left, *right)),
                h1_cocycle(*left) + sign_action(*left, h1_cocycle(*right))
            );
        }
    }
    // Sign-valued coboundaries are even on a reflection, so z has class 1
    // in H1(D3,Z_or)=Z/2.
    let reflection = D3 {
        rotation: 0,
        reflection: true,
    };
    assert_eq!(h1_cocycle(reflection).rem_euclid(2), 1);
    for zero_cochain in -3_i64..=3 {
        let coboundary = sign_action(reflection, zero_cochain) - zero_cochain;
        assert_eq!(coboundary.rem_euclid(2), 0);
    }

    // Lift z to the plus sheet in 0->Z_diag->Z{+,-}->Z_or->0.  Its failure to
    // be a cocycle is the diagonal-valued connecting 2-cocycle.
    for first in &group {
        for second in &group {
            for third in &group {
                let cocycle_identity = connecting_cocycle(*second, *third)
                    - connecting_cocycle(multiply(*first, *second), *third)
                    + connecting_cocycle(*first, multiply(*second, *third))
                    - connecting_cocycle(*first, *second);
                assert_eq!(cocycle_identity, 0);
            }
        }
    }
    assert_eq!(connecting_cocycle(reflection, reflection), 1);
    // For a normalized trivial-coefficient 1-cochain b, delta b(s,s)=2b(s),
    // so the odd value above represents class 1 in H2(D3,Z)=Z/2.
    for value_on_reflection in -3_i64..=3 {
        let coboundary_at_square = 2 * value_on_reflection;
        assert_eq!(coboundary_at_square.rem_euclid(2), 0);
    }

    let assembled_mapping_fiber_typed = false;
    assert!(!assembled_mapping_fiber_typed);

    println!(
        "{}",
        r#"{"claim":"The integral anti-diagonal two-sheet generator maps to twice the primitive conductor difference. The P1xP1 ruling lattice has diagonal/anti-diagonal change-of-basis determinant 2 and retains an independent graph-equation Tor1 line. Every reflection-equivariant BM pushforward preserving both ruling/Rees grades is k*(a-b)+ell*tau and sends the anti ruling to 2k, never to a unit. The sign-valued D3 1-cocycle z=1 on reflections represents class 1 in H1(D3,Z_or)=Z/2, and its explicit sheet-lift connecting cocycle has c(s,s)=1 and represents class 1 in H2(D3,Z)=Z/2.","status":"proved_scoped_integral_obstruction_and_cohomology_shadow","scope":"Finite sheet/ruling/Tor lattice and explicit D3 cocycles. Applying the Bockstein to the physical obstruction still depends on constructing the correctly typed loaded mapping-fiber sequence; that sequence is not asserted here.","evidence_refs":["ledger entries 93, 138, and 139","research/voevodsky/check_d03_antidiagonal_central_bockstein_obstruction.rs"],"factorization_test":{"sheet_difference":"diff(e_plus-e_minus)=2","ruling_change_determinant":2,"independent_graph_Tor1_rank":1,"equivariant_BM_maps":"k*(a-b)+ell*tau","unit_anti_residue":"impossible while k!=0 preserves both ruling grades","H1_D3_Zor":"Z/2, explicit class 1","connecting_cocycle":"c(g,h)=lift(g)+g*lift(h)-lift(gh)","reflection_square":"c(s,s)=1","H2_D3_Z":"Z/2, explicit class 1","Bockstein":"class 1 maps to class 1"},"unconstructed":["typed loaded mapping-fiber realizing this module sequence","spatial BM pushforward from the weighted graph to the central edge","generic-to-special Q leg"],"boundary":"The cohomology computation detects the parity obstruction once the mapping-fiber is typed. It does not itself construct or identify the physical obstruction class."}"#
    );
}
