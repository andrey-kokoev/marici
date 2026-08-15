// Exact coefficient-level audit of the normalization-conductor Bockstein.
//
// Scope: this checker identifies the two-sheet permutation sequence and its
// connecting map on the physical D3 transport group.  It does not construct
// the endpoint/Q defect map whose class would be fed into that connecting map.

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct D3 {
    rotation: i32,
    reflected: bool,
}

impl D3 {
    fn new(rotation: i32, reflected: bool) -> Self {
        Self {
            rotation: rotation.rem_euclid(3),
            reflected,
        }
    }

    fn identity() -> Self {
        Self::new(0, false)
    }

    fn compose(self, other: Self) -> Self {
        let other_rotation = if self.reflected {
            -other.rotation
        } else {
            other.rotation
        };
        Self::new(
            self.rotation + other_rotation,
            self.reflected ^ other.reflected,
        )
    }

    fn act_on_sheets(self, pair: [i64; 2]) -> [i64; 2] {
        if self.reflected {
            [pair[1], pair[0]]
        } else {
            pair
        }
    }
}

fn group() -> [D3; 6] {
    [
        D3::identity(),
        D3::new(1, false),
        D3::new(2, false),
        D3::new(0, true),
        D3::new(1, true),
        D3::new(2, true),
    ]
}

fn sign_character(element: D3) -> i64 {
    if element.reflected {
        -1
    } else {
        1
    }
}

fn diagonal(value: i64) -> [i64; 2] {
    [value, value]
}

fn sheet_difference(pair: [i64; 2]) -> i64 {
    pair[0] - pair[1]
}

fn carrier_parity_cocycle(element: D3) -> i64 {
    i64::from(element.reflected)
}

fn sheetwise_lift(element: D3) -> [i64; 2] {
    if element.reflected {
        [1, 0]
    } else {
        [0, 0]
    }
}

fn add(left: [i64; 2], right: [i64; 2]) -> [i64; 2] {
    [left[0] + right[0], left[1] + right[1]]
}

fn sub(left: [i64; 2], right: [i64; 2]) -> [i64; 2] {
    [left[0] - right[0], left[1] - right[1]]
}

fn bockstein_cocycle(left: D3, right: D3) -> i64 {
    let numerator = carrier_parity_cocycle(left) + carrier_parity_cocycle(right)
        - carrier_parity_cocycle(left.compose(right));
    assert_eq!(numerator.rem_euclid(2), 0);
    numerator / 2
}

fn check_group(group: &[D3]) {
    let rotation = D3::new(1, false);
    let reflection = D3::new(0, true);
    assert_eq!(rotation.compose(rotation).compose(rotation), D3::identity());
    assert_eq!(reflection.compose(reflection), D3::identity());
    assert_eq!(
        reflection.compose(rotation).compose(reflection),
        D3::new(2, false)
    );
    for left in group {
        for right in group {
            assert!(group.contains(&left.compose(*right)));
        }
    }
}

fn check_conductor_sequence(group: &[D3]) {
    // Entry 93's constant conductor sequence is
    // 0 -> 1 --Delta--> Z{+,-} --difference--> 1_or -> 0.
    for value in -8_i64..=8 {
        assert_eq!(sheet_difference(diagonal(value)), 0);
    }
    for first in -8_i64..=8 {
        for second in -8_i64..=8 {
            let pair = [first, second];
            if sheet_difference(pair) == 0 {
                assert_eq!(pair, diagonal(first));
            }
        }
    }
    for value in -8_i64..=8 {
        assert_eq!(sheet_difference([value, 0]), value);
    }

    for element in group {
        for value in -4_i64..=4 {
            assert_eq!(element.act_on_sheets(diagonal(value)), diagonal(value));
        }
        for first in -4_i64..=4 {
            for second in -4_i64..=4 {
                let pair = [first, second];
                assert_eq!(
                    sheet_difference(element.act_on_sheets(pair)),
                    sign_character(*element) * sheet_difference(pair)
                );
            }
        }
    }

    // An equivariant integral section of the difference map would have
    // section(1)=(a,b), a-b=1 and swap(a,b)=section(-1)=(-a,-b).
    // Hence b=-a and 2a=1, which has no integral solution.
    for first in -64_i64..=64 {
        for second in -64_i64..=64 {
            let is_section = first - second == 1;
            let is_equivariant = [second, first] == [-first, -second];
            assert!(!(is_section && is_equivariant));
        }
    }
}

fn check_bockstein(group: &[D3]) {
    let identity = D3::identity();
    let reflection = D3::new(0, true);

    // The reflection-parity function is a normalized one-cocycle with values
    // in the sign line.
    assert_eq!(carrier_parity_cocycle(identity), 0);
    for left in group {
        for right in group {
            assert_eq!(
                carrier_parity_cocycle(left.compose(*right)),
                carrier_parity_cocycle(*left)
                    + sign_character(*left) * carrier_parity_cocycle(*right)
            );
            assert_eq!(
                sheet_difference(sheetwise_lift(*left)),
                carrier_parity_cocycle(*left)
            );
        }
    }

    // Lift that one-cocycle to the + sheet.  Its coboundary lies in the
    // diagonal submodule and is exactly Delta(c), where c is the standard
    // loaded H^2 generator.
    for left in group {
        for right in group {
            let lifted_coboundary = add(
                sub(
                    left.act_on_sheets(sheetwise_lift(*right)),
                    sheetwise_lift(left.compose(*right)),
                ),
                sheetwise_lift(*left),
            );
            assert_eq!(
                lifted_coboundary,
                diagonal(bockstein_cocycle(*left, *right))
            );
        }
    }
    assert_eq!(bockstein_cocycle(reflection, reflection), 1);

    // The image is a normalized integral two-cocycle.
    for first in group {
        assert_eq!(bockstein_cocycle(identity, *first), 0);
        assert_eq!(bockstein_cocycle(*first, identity), 0);
        for second in group {
            for third in group {
                let differential = bockstein_cocycle(*second, *third)
                    - bockstein_cocycle(first.compose(*second), *third)
                    + bockstein_cocycle(*first, second.compose(*third))
                    - bockstein_cocycle(*first, *second);
                assert_eq!(differential, 0);
            }
        }
    }

    // Both displayed classes have exact order two.  Twice the sign-valued
    // one-cocycle is the coboundary of the zero-cochain -1.  Twice the
    // trivial-valued two-cocycle is the coboundary of reflection parity.
    for element in group {
        let sign_coboundary_of_minus_one = sign_character(*element) * -1 - -1;
        assert_eq!(
            sign_coboundary_of_minus_one,
            2 * carrier_parity_cocycle(*element)
        );
    }
    for left in group {
        for right in group {
            let parity_coboundary = carrier_parity_cocycle(*right)
                - carrier_parity_cocycle(left.compose(*right))
                + carrier_parity_cocycle(*left);
            assert_eq!(parity_coboundary, 2 * bockstein_cocycle(*left, *right));
        }
    }

    // Neither class is an integral coboundary on the reflection subgroup:
    // sign-valued degree-zero coboundaries are even at s, and normalized
    // trivial-valued degree-one coboundaries are even at (s,s).
    for value in -16_i64..=16 {
        let sign_coboundary_at_reflection = -2 * value;
        assert_ne!(sign_coboundary_at_reflection, 1);
        let trivial_coboundary_at_square = 2 * value;
        assert_ne!(trivial_coboundary_at_square, 1);
    }

    // Entries 138-139 independently establish that the source and target
    // groups are both Z/2.  The explicit nonzero connecting image above
    // therefore proves that the conductor Bockstein is an isomorphism.
}

fn main() {
    let group = group();
    check_group(&group);
    check_conductor_sequence(&group);
    check_bockstein(&group);

    println!(
        "{}",
        r#"{"claim":"The constant part of the scalar normalization-conductor square is the D3-module sequence 0 -> Z -> Z{+,-} -> Z_or -> 0. Its connecting homomorphism sends the carrier reflection-parity generator in H1(D3,Z_or)=Z/2 to the loaded obstruction generator in H2(D3,Z)=Z/2 and is therefore an isomorphism. Thus once-relative polarity loading transgresses, rather than discards, endpoint reflection parity.","status":"proved","assumptions":["The physical D3 transport group acts trivially by rotation on the two normalization sheets and the physical reflection exchanges them, as in entries 93 and 138.","The source and target cohomology orders H1(D3,Z_or)=2 and H2(D3,Z)=2 are the independently proved entry-138 calculation.","This is the coefficient/character shadow of the desired mapping-complex sequence, not its loaded support-PC realization."],"evidence_refs":["research/voevodsky/check_conductor_polarity_bockstein.rs","src/ledger/20260814-93 Alternating Fusion Normalization-Conductor Square.md","src/ledger/20260814-138 Physical Polarity Loading and the Shifted Butterfly Obstruction.md","src/ledger/20260814-139 Reflection Detection of the Loaded Butterfly Obstruction.md"],"factorization_test":{"module_sequence":"0 -> trivial --diagonal--> sheet permutation --difference--> sign -> 0","integral_equivariant_section":"absent; it would require 2a=1","carrier_generator":"reflection-parity sign-valued 1-cocycle","sheetwise_lift":"positive-sheet basis vector on reflections","connecting_cocycle":"c(g,h)=(eps(g)+eps(h)-eps(gh))/2","reflection_square":"c(f3,f3)=1","bockstein":"isomorphism Z/2 -> Z/2","numeric_denominator_used":false,"loaded_mapping_complex":"unconstructed"},"counterevidence":["The conductor module sequence does not determine which endpoint/Q defect class is carried by the geometric sheetwise gallery lift.","Writing partial[beta] is imprecise: the connecting input must be the defect restriction class [r(beta_+,-beta_-)].","Target edge purity is already strict under reflection, but that does not construct the source endpoint/Q restriction map."],"next_experiment":"Construct the endpoint- and Q-preserving defect restriction r from the two sheetwise marked-gallery homotopies to the sign defect complex. Compute its carrier parity before applying the conductor Bockstein. Parity zero gives the unique loaded lift; parity one gives the nonzero loaded obstruction."}"#
    );
}
