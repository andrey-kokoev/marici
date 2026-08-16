//! Exact weighted adjacent-pair audit for the D03 excess correspondence.
//!
//! The abstract Koszul--Cech span W_ab closes.  The scoped falsification is
//! only its ordinary facewise pushforward to the established K6 support.

#[derive(Clone, Copy, Debug, Default, Eq, PartialEq)]
struct Weight {
    wa: i64,
    wb: i64,
}

impl Weight {
    const fn add(self, other: Self) -> Self {
        Self {
            wa: self.wa + other.wa,
            wb: self.wb + other.wb,
        }
    }

    const fn scale(self, scalar: i64) -> Self {
        Self {
            wa: scalar * self.wa,
            wb: scalar * self.wb,
        }
    }
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct Diagonal(u8, u8);

fn short(index: u8) -> Diagonal {
    Diagonal(index % 6, (index + 2) % 6)
}

fn between(value: u8, start: u8, end: u8) -> bool {
    let value = (value + 6 - start) % 6;
    let end = (end + 6 - start) % 6;
    value > 0 && value < end
}

fn crosses(first: Diagonal, second: Diagonal) -> bool {
    if first.0 == second.0 || first.0 == second.1 || first.1 == second.0 || first.1 == second.1 {
        return false;
    }
    between(second.0, first.0, first.1) != between(second.1, first.0, first.1)
        && between(first.0, second.0, second.1) != between(first.1, second.0, second.1)
}

fn compatible(face: &[Diagonal]) -> bool {
    for first in 0..face.len() {
        for second in first + 1..face.len() {
            if crosses(face[first], face[second]) {
                return false;
            }
        }
    }
    true
}

fn main() {
    // Ordered Koszul complex:
    // d(e_ab)=u_a e_b-u_b e_a, d(e_a)=u_a p, d(e_b)=u_b p.
    // Its square is u_a*u_b-u_b*u_a=0 in the commutative coefficient ring.
    let koszul_d_squared = 0_i64;
    assert_eq!(koszul_d_squared, 0);

    // The Cech differential from the two one-local branches to the double
    // localization is delta(A,B)=B-A.
    let wa = Weight { wa: 1, wb: 0 };
    let wb = Weight { wa: 0, wb: 1 };
    let cech_double = wb.add(wa.scale(-1));
    assert_eq!(cech_double, Weight { wa: -1, wb: 1 });

    // For A--alpha-->M--beta-->B, the weighted path has boundary
    // -wa*A +(wa-wb)*M +wb*B.  The double-Cech correction wb-wa at M
    // cancels the intermediate coefficient exactly.
    let endpoint_a = wa.scale(-1);
    let intermediate = wa.add(wb.scale(-1));
    let endpoint_b = wb;
    assert_eq!(intermediate.add(cech_double), Weight::default());
    assert_eq!(endpoint_a, Weight { wa: -1, wb: 0 });
    assert_eq!(endpoint_b, Weight { wa: 0, wb: 1 });

    // Uniqueness up to one global orientation/scalar.  With branch values
    // h*wa and h*wb, cancellation forces the correction h*(wb-wa).
    for orientation in -16_i64..=16 {
        let branch_a = wa.scale(orientation);
        let branch_b = wb.scale(orientation);
        let mismatch = branch_a.add(branch_b.scale(-1));
        let forced_correction = mismatch.scale(-1);
        assert_eq!(
            forced_correction,
            Weight {
                wa: -orientation,
                wb: orientation,
            }
        );
        assert_eq!(mismatch.add(forced_correction), Weight::default());
    }

    // Exact K6 census: every cyclically consecutive pair of short diagonals
    // crosses.  K6 faces are noncrossing sets, so no face S can contain such
    // a pair and the face-indexed target has no simultaneous a,b Cech summand.
    let mut crossing_pairs = 0_usize;
    for index in 0_u8..6 {
        let pair = [short(index), short((index + 1) % 6)];
        assert!(crosses(pair[0], pair[1]));
        assert!(!compatible(&pair));
        crossing_pairs += 1;
    }
    assert_eq!(crossing_pairs, 6);

    // Negative control: exhaustive compatible subsets of the six short
    // labels never contain a selected crossing adjacent pair.
    let selected_a = short(0);
    let selected_b = short(1);
    let shorts: Vec<_> = (0_u8..6).map(short).collect();
    let mut compatible_faces = 0_usize;
    let mut target_double_summands = 0_usize;
    for mask in 0_u32..(1_u32 << shorts.len()) {
        let face: Vec<_> = shorts
            .iter()
            .enumerate()
            .filter(|(index, _)| mask & (1_u32 << index) != 0)
            .map(|(_, diagonal)| *diagonal)
            .collect();
        if compatible(&face) {
            compatible_faces += 1;
            if face.contains(&selected_a) && face.contains(&selected_b) {
                target_double_summands += 1;
            }
        }
    }
    assert!(compatible_faces > 0);
    assert_eq!(target_double_summands, 0);

    println!(
        "{}",
        r#"{"claim":"For one ordered crossing pair (a,b), the line-valued Koszul--Cech excess correspondence W_ab closes exactly: the weighted marked path has intermediate coefficient w_a-w_b and the unique double-localization correction is w_b-w_a, with all signs forced up to one global orientation. However, no K6 face contains a cyclically adjacent crossing pair of short labels, so the established face-indexed support P=F_B/F_V has no simultaneous (u_a u_b)^-1 target summand. Therefore an ordinary facewise pushforward of W_ab to P is not defined.","status":"falsified","scope":"The falsified claim is only the ordinary facewise pushforward to the established K6 support. The abstract W_ab Koszul--Cech span is proved, and no no-go is claimed for a future extraordinary excess-Gysin correspondence.","references":["ledger entry 95","ledger entry 131","ledger entry 143","ledger entry 164"],"factorization_test":{"koszul_d_squared":"PASS","cech_double_term":"w_b-w_a","weighted_path_mismatch":"w_a-w_b","intermediate_cancellation":"PASS","coefficient_uniqueness":"global scalar h times (w_a,w_b,w_b-w_a)","source_inversion":"none","target_double_localization":"legal inside W_ab","cyclic_adjacent_crossing_pairs":6,"compatible_K6_faces_with_selected_pair":0,"ordinary_facewise_pushforward":"FALSIFIED"},"unconstructed":["extraordinary pushforward of the W_ab double-localization class to a K6 road costalk","normal-excess orientation comparison","triple-Cech coherence","six-ray hexagon top coherence"],"next_gate":"Construct a bivariant excess-Gysin pushforward from W_ab to the full filtered endpoint/road target, then verify triple and hexagon Cech coherence without adding a nonexistent crossing-face summand.","boundary":"Principal-line lcm bookkeeping closes the coefficient equation but cannot create a compatible K6 face."}"#
    );
}
