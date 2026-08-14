//! Exact coefficient-level three-gluon derivation of the six-point
//! QTDS -> Ward matrix as a normalization/conductor symbol.
//!
//! The fixed scaffold pairing F_+=(12)(34)(56) has fusion normals
//!
//!   (X13,X35,X51)=(x0,x2,x4),
//!
//! while its three-gluon residue is a polynomial in the opposite short
//! invariants (X24,X46,X62)=(x1,x3,x5) and in the three long variables
//!
//!   (y0,y1,y2)=(X14,X25,X36).
//!
//! Rotating all six scalar labels once gives F_-=(23)(45)(61), whose normals
//! are (x1,x3,x5).  Put F=F_+ union F_-, Z=F_+ intersect F_-, and normalize F
//! by F_+ disjoint-union F_-.  The two residues agree on Z.  Their canonical
//! polarity-odd relative normal symbol is
//!
//!   (d_{Z/F+} A3^+, -d_{Z/F-} A3^-).
//!
//! Its shared-y linear symbol, followed by the label-determined Ward-star
//! incidence, is exactly C_QTDS and hence the existing 7x6 Ward-kernel
//! matrix.  No ambient extensions of A3^+ or A3^- are used.  Adding an element
//! of I(F_+) or I(F_-) to an ambient representative cannot change the
//! corresponding relative normal symbol; this is checked on every quadratic
//! ideal monomial relevant to A3.
//!
//! The multi-residue coefficient lines are also not arbitrarily identified.
//! One-step rotation maps the ordered fusion-normal list (x0,x2,x4) to
//! (x1,x3,x5) position by position, so it gives an orientation-preserving
//! isomorphism of their ordered conormal tensor products.
//!
//! What is not proved here is that this canonical coefficient symbol is the
//! image of a chain map in the scalar BRST/kinetic complex or that it commutes
//! with a physical Cut.

use std::collections::BTreeMap;

const X: usize = 6;
const Y: usize = 3;
const VARS: usize = X + Y;

type Linear = [i64; VARS];
type Contact = [[i64; X]; 3];
type WardMatrix = [[i64; X]; 7];

#[derive(Clone, Debug, Eq, PartialEq)]
struct Quadratic(BTreeMap<(usize, usize), i64>);

impl Quadratic {
    fn new(terms: &[(i64, usize, usize)]) -> Self {
        let mut result = BTreeMap::new();
        for &(coefficient, first, second) in terms {
            let key = if first <= second {
                (first, second)
            } else {
                (second, first)
            };
            *result.entry(key).or_insert(0) += coefficient;
        }
        result.retain(|_, coefficient| *coefficient != 0);
        Self(result)
    }

    fn relabel(&self, permutation: [usize; VARS]) -> Self {
        let terms: Vec<_> = self
            .0
            .iter()
            .map(|(&(first, second), &coefficient)| {
                (coefficient, permutation[first], permutation[second])
            })
            .collect();
        Self::new(&terms)
    }

    fn derivative(&self, variable: usize) -> Linear {
        let mut result = [0; VARS];
        for (&(first, second), &coefficient) in &self.0 {
            if first == variable {
                result[second] += coefficient;
            }
            if second == variable {
                result[first] += coefficient;
            }
        }
        result
    }

    fn add_monomial(&self, coefficient: i64, first: usize, second: usize) -> Self {
        let mut terms: Vec<_> = self
            .0
            .iter()
            .map(|(&(a, b), &value)| (value, a, b))
            .collect();
        terms.push((coefficient, first, second));
        Self::new(&terms)
    }

    fn restrict_to_z(&self) -> Self {
        Self(
            self.0
                .iter()
                .filter(|&(&(first, second), _)| first >= X && second >= X)
                .map(|(&monomial, &coefficient)| (monomial, coefficient))
                .collect(),
        )
    }
}

fn y(index: usize) -> usize {
    X + index
}

/// Documented A3^YM in the fixed F_+ scaffold:
/// X14 X26 + X36 X24 + X25 X46
/// - X25 X36 - X14 X36 - X14 X25.
/// Momentum conservation identifies X26=X62=x5.
fn a3_plus() -> Quadratic {
    Quadratic::new(&[
        (1, y(0), 5),
        (1, y(2), 1),
        (1, y(1), 3),
        (-1, y(1), y(2)),
        (-1, y(0), y(2)),
        (-1, y(0), y(1)),
    ])
}

/// One-step boundary rotation: x_j -> x_{j+1} and
/// (X14,X25,X36) -> (X25,X36,X14).
fn one_step_rotation() -> [usize; VARS] {
    let mut permutation = [0; VARS];
    for (index, target) in permutation[..X].iter_mut().enumerate() {
        *target = (index + 1) % X;
    }
    for (index, target) in permutation[X..].iter_mut().enumerate() {
        *target = y((index + 1) % Y);
    }
    permutation
}

fn subtract(left: Linear, right: Linear) -> Linear {
    std::array::from_fn(|index| left[index] - right[index])
}

fn scale(coefficient: i64, linear: Linear) -> Linear {
    linear.map(|entry| coefficient * entry)
}

fn restrict_linear_to_z(mut linear: Linear) -> Linear {
    linear[..X].fill(0);
    linear
}

fn relative_normal_symbol(polynomial: &Quadratic, directions: [usize; 3]) -> [Linear; 3] {
    directions.map(|direction| restrict_linear_to_z(polynomial.derivative(direction)))
}

/// Assemble the polarity-odd conductor symbol in the six canonically labelled
/// normal directions, then take its shared-y linear symbol.  Odd x directions
/// are normal to Z inside F_+; even x directions are normal inside F_-.
fn mixed_conductor_symbol(plus: &Quadratic, minus: &Quadratic) -> [Linear; Y] {
    let plus_relative = relative_normal_symbol(plus, [1, 3, 5]);
    let minus_relative = relative_normal_symbol(minus, [0, 2, 4]);
    let mut by_x = [[0; VARS]; X];
    for index in 0..3 {
        by_x[2 * index + 1] = plus_relative[index];
        by_x[2 * index] = scale(-1, minus_relative[index]);
    }

    std::array::from_fn(|channel| {
        let mut result = [0; VARS];
        for normal in 0..X {
            result[normal] = by_x[normal][y(channel)];
        }
        result
    })
}

/// The road i is opposite y_i in the triangle of long channels.  With the
/// polygon orientation (0,1,2), the Ward-star boundary is
/// (d2-d1,d0-d2,d1-d0).
fn ward_star_incidence(d: [Linear; Y]) -> [Linear; 3] {
    [
        subtract(d[2], d[1]),
        subtract(d[0], d[2]),
        subtract(d[1], d[0]),
    ]
}

fn derive_contact(plus: &Quadratic, minus: &Quadratic) -> Contact {
    let channels = ward_star_incidence(mixed_conductor_symbol(plus, minus));
    assert!(channels
        .iter()
        .all(|channel| channel[X..].iter().all(|&v| v == 0)));
    std::array::from_fn(|road| std::array::from_fn(|variable| channels[road][variable]))
}

fn ward_bridge(root: [i64; 3]) -> [i64; 7] {
    assert_eq!(root.iter().sum::<i64>(), 0);
    let [p, q, _] = root;
    [q, -p, -q, p, -p, -q, p + q]
}

fn compose_to_ward(contact: Contact) -> WardMatrix {
    let columns: Vec<_> = (0..X)
        .map(|variable| ward_bridge(std::array::from_fn(|road| contact[road][variable])))
        .collect();
    std::array::from_fn(|row| std::array::from_fn(|column| columns[column][row]))
}

fn ward_contact_column(column: usize) -> [i64; 6] {
    let edge = |core: usize, road: usize| 2 * road + core;
    let mut result = [0; 6];
    match column {
        0..=3 => {
            let core = column / 2;
            let road = column % 2;
            result[edge(core, (road + 1) % 3)] += 1;
            result[edge(core, (road + 2) % 3)] -= 1;
        }
        4..=6 => {
            let road = column - 4;
            result[edge(0, road)] += 1;
            result[edge(1, road)] -= 1;
        }
        _ => unreachable!(),
    }
    result
}

fn ward_contact(chain: [i64; 7]) -> [i64; 6] {
    let mut result = [0; 6];
    for (column, coefficient) in chain.into_iter().enumerate() {
        let image = ward_contact_column(column);
        for edge in 0..6 {
            result[edge] += coefficient * image[edge];
        }
    }
    result
}

fn main() {
    let plus = a3_plus();
    let rotation = one_step_rotation();
    let minus = plus.relabel(rotation);

    // The ordered residue products are carried position by position, hence
    // with positive orientation (and with no sign at all for tensor products).
    let plus_fusion_normals = [0, 2, 4];
    let minus_fusion_normals = [1, 3, 5];
    assert_eq!(
        plus_fusion_normals.map(|normal| rotation[normal]),
        minus_fusion_normals
    );

    // A fixed residue has forgotten its own fusion normals.  Therefore it
    // cannot determine the corresponding three columns of C_QTDS.
    for normal in [0, 2, 4] {
        assert_eq!(plus.derivative(normal), [0; VARS]);
    }
    for normal in [1, 3, 5] {
        assert_eq!(minus.derivative(normal), [0; VARS]);
    }

    // The rotated polynomial is
    // y1*x0 + y0*x2 + y2*x4 - y0*y1 - y0*y2 - y1*y2.
    let expected_minus = Quadratic::new(&[
        (1, y(1), 0),
        (1, y(0), 2),
        (1, y(2), 4),
        (-1, y(0), y(1)),
        (-1, y(0), y(2)),
        (-1, y(1), y(2)),
    ]);
    assert_eq!(minus, expected_minus);

    // The normalization branches glue on their conductor Z after transporting
    // the ordered residue line by the one-step rotation.
    assert_eq!(plus.restrict_to_z(), minus.restrict_to_z());

    // Relative derivatives inside a branch are independent of its ambient
    // representative.  Exhaust the quadratic monomial basis of I(F_+) and
    // I(F_-), the full degree relevant to A3.
    let plus_symbol = relative_normal_symbol(&plus, [1, 3, 5]);
    let minus_symbol = relative_normal_symbol(&minus, [0, 2, 4]);
    let mut representative_checks = 0;
    for ideal_normal in [0, 2, 4] {
        for other in 0..VARS {
            assert_eq!(
                relative_normal_symbol(&plus.add_monomial(1, ideal_normal, other), [1, 3, 5]),
                plus_symbol
            );
            representative_checks += 1;
        }
    }
    for ideal_normal in [1, 3, 5] {
        for other in 0..VARS {
            assert_eq!(
                relative_normal_symbol(&minus.add_monomial(1, ideal_normal, other), [0, 2, 4]),
                minus_symbol
            );
            representative_checks += 1;
        }
    }
    assert_eq!(representative_checks, 54);

    let contact = derive_contact(&plus, &minus);
    let expected_contact = [
        [1, 1, 0, -1, -1, 0],
        [0, -1, -1, 0, 1, 1],
        [-1, 0, 1, 1, 0, -1],
    ];
    assert_eq!(contact, expected_contact);

    let ward = compose_to_ward(contact);
    let expected_ward = [
        [0, -1, -1, 0, 1, 1],
        [-1, -1, 0, 1, 1, 0],
        [0, 1, 1, 0, -1, -1],
        [1, 1, 0, -1, -1, 0],
        [-1, -1, 0, 1, 1, 0],
        [0, 1, 1, 0, -1, -1],
        [1, 0, -1, -1, 0, 1],
    ];
    assert_eq!(ward, expected_ward);
    for variable in 0..X {
        let column = std::array::from_fn(|row| ward[row][variable]);
        assert_eq!(ward_contact(column), [0; 6]);
    }

    println!("Three-gluon normalization-symbol transgression certificate");
    println!("=========================================================");
    println!("  F_+ normals: (x0,x2,x4)=(X13,X35,X51)");
    println!("  F_- normals: (x1,x3,x5)=(X24,X46,X62)");
    println!("  fixed-stratum blind columns: 3+3");
    println!("  ambient-representative invariance checks: {representative_checks}");
    println!("  ordered residue-line rotation sign: +1");
    println!("  derived contact matrix: 3x6 = C_QTDS");
    println!("  derived Ward matrix:   7x6; kernel columns 6/6");
    println!();
    println!("VERDICT: proved at coefficient-symbol level");
    println!("  no common ambient lift or GL(6) choice is required");
    println!("  still open: scalar BRST chain realization and physical Cut naturality");
}
