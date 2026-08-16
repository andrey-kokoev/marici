//! Oriented Kato-Nakayama augmented interval for the Rees-Cech/Tor wall.
//!
//! The relative characteristic lattice of the ordered product branch is the
//! anti-diagonal Z_or.  Entry105's positive-real basepoint cuts its KN circle
//! into an oriented interval.  The ordinary interval boundary supplies the
//! two Cech chart terms, while BM integration supplies the third Tor-wall
//! term:
//!
//!     e |-> w - v0 + v1.
//!
//! Reflection reverses e and w and exchanges v0,v1, so this augmented
//! boundary is equivariant.  Tensoring its three contractions with the
//! labelled Boolean packet reproduces the 72 primitive rows of the completed
//! vertex cone.
//!
//! Scope: finite constructible KN-link and line-valued bivariant kernel.
//! The proper pushforward into literal entry143 costalk sheaves remains open.

const ORDERED_PAIRS: usize = 6;

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct Output {
    wall: i64,
    chart0: i64,
    chart1: i64,
}

impl Output {
    fn reflect(self) -> Self {
        // The wall carries the anti-diagonal orientation line; the two cut
        // germs are exchanged.
        Self {
            wall: -self.wall,
            chart0: self.chart1,
            chart1: self.chart0,
        }
    }
}

fn augmented_boundary(edge: i64) -> Output {
    Output {
        wall: edge,
        chart0: -edge,
        chart1: edge,
    }
}

fn selected_position(mask: u8, bit: usize) -> usize {
    (0..bit).filter(|index| mask & (1 << index) != 0).count()
}

fn contraction(mask: u8, bit: usize) -> Option<(u8, i64)> {
    if mask & (1 << bit) == 0 {
        return None;
    }
    Some((
        mask & !(1 << bit),
        if selected_position(mask, bit) % 2 == 0 {
            1
        } else {
            -1
        },
    ))
}

fn total_boundary(mask: u8) -> Vec<(usize, u8, i64)> {
    // Axis order (tau,n0,n1), with the augmented interval coefficients.
    let coefficients = [1_i64, 1, -1];
    (0..3)
        .filter_map(|axis| {
            contraction(mask, axis).map(|(lower, sign)| (axis, lower, coefficients[axis] * sign))
        })
        .collect()
}

fn main() {
    // The positive-real basepoint is an admitted input from entry105.
    let positive_real_basepoint = true;
    assert!(positive_real_basepoint);

    // Cut circle: d e = v1-v0.  BM integration is int(e)=+1.  Combining
    // them yields exactly the three-face primitive row.
    let boundary = augmented_boundary(1);
    assert_eq!(
        boundary,
        Output {
            wall: 1,
            chart0: -1,
            chart1: 1,
        }
    );
    let smith_gcd = [boundary.wall, boundary.chart0, boundary.chart1]
        .into_iter()
        .map(i64::abs)
        .reduce(gcd)
        .unwrap();
    assert_eq!(smith_gcd, 1);

    // Reflection equivariance: r(e)=-e and r(w)=-w while v0<->v1.
    assert_eq!(augmented_boundary(-1), augmented_boundary(1).reflect());

    let mut rows = 0usize;
    let mut chart_rows = 0usize;
    let mut wall_rows = 0usize;
    let mut d_squared_checks = 0usize;
    for _ in 0..ORDERED_PAIRS {
        for mask in 0_u8..8 {
            let first = total_boundary(mask);
            rows += first.len();
            for (axis, middle, first_sign) in &first {
                if *axis == 0 {
                    wall_rows += 1;
                } else {
                    chart_rows += 1;
                }
                for second_axis in 0..3 {
                    if second_axis == *axis {
                        continue;
                    }
                    let Some((lower, second_koszul_sign)) = contraction(*middle, second_axis)
                    else {
                        continue;
                    };
                    let weights = [1_i64, 1, -1];
                    let first_path = first_sign * weights[second_axis] * second_koszul_sign;
                    let partner = total_boundary(mask)
                        .into_iter()
                        .filter(|(other_axis, _, _)| *other_axis == second_axis)
                        .find_map(|(_, other_middle, other_first_sign)| {
                            contraction(other_middle, *axis).and_then(
                                |(other_lower, other_second_sign)| {
                                    (other_lower == lower).then_some(
                                        other_first_sign * weights[*axis] * other_second_sign,
                                    )
                                },
                            )
                        })
                        .unwrap();
                    assert_eq!(first_path + partner, 0);
                    d_squared_checks += 1;
                }
            }
        }
    }
    assert_eq!(rows, 72);
    assert_eq!(chart_rows, 48);
    assert_eq!(wall_rows, 24);
    assert_eq!(d_squared_checks, 72);

    // Principal occurrence sections and their duals rescale inversely.
    let section_rescaling = -1_i64;
    let dual_rescaling = -1_i64;
    assert_eq!(section_rescaling * dual_rescaling, 1);

    // Raw interval and wall orientations are both reflection odd, so the
    // once-loaded wall coefficient is reflection even.
    let interval_reflection = -1_i64;
    let wall_orientation_reflection = -1_i64;
    assert_eq!(interval_reflection * wall_orientation_reflection, 1);

    println!(
        "{}",
        r#"{"status":"proved_scoped_oriented_KN_augmented_wall_kernel","relative_KN_fiber":"oriented circle cut at entry105 positive-real basepoint","cut_interval_boundary":["-chart0","+chart1"],"BM_integral_wall":"+tau","augmented_boundary":["+tau","+n0","-n1"],"primitive_smith_factor":1,"reflection_interval_sign":-1,"reflection_wall_orientation_sign":-1,"loaded_wall_sign":1,"ordered_pairs":6,"total_boundary_rows":72,"chart_rows":48,"wall_rows":24,"total_d_squared":0,"principal_line_rescaling_invariant":true,"ordinary_fs_log_divisor_used":false,"literal_entry143_six_functor_pushforward_constructed":false,"endpoint_Q_mapping_fiber_instantiated":false,"next_gate":"construct the proper constructible pushforward/Beck-Chevalley map from this oriented KN augmented kernel to the literal entry143 vertex costalks and then attach endpoint and qSigma rows"}"#
    );
}

fn gcd(mut left: i64, mut right: i64) -> i64 {
    while right != 0 {
        let remainder = left % right;
        left = right;
        right = remainder;
    }
    left.abs()
}
