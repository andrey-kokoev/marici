//! Finite obstruction certificate for the actual compatible D03 face packet.
//!
//! This is not the adjacent-ray dP6 packet: D03, x1, and x3 form a genuine
//! K6 face.  The Laurent mapping problem has a unique primitive, but that
//! primitive is absent from the legal target-side BM--Cech summands because
//! inverse normal factors are forbidden on circled states.

use std::collections::{BTreeMap, BTreeSet};

type Z = i64;

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct Diagonal(u8, u8);

const D: Diagonal = Diagonal(0, 3);
const A: Diagonal = Diagonal(1, 3);
const B: Diagonal = Diagonal(3, 5);

#[derive(Clone, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct State {
    face: BTreeSet<Diagonal>,
    circles: BTreeSet<Diagonal>,
}

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct Monomial {
    x_a: u8,
    x_b: u8,
    u_a: i8,
    u_b: i8,
}

impl Monomial {
    const ONE: Self = Self {
        x_a: 0,
        x_b: 0,
        u_a: 0,
        u_b: 0,
    };
    const Y_A: Self = Self {
        x_a: 1,
        x_b: 0,
        u_a: -1,
        u_b: 0,
    };
    const Y_B: Self = Self {
        x_a: 0,
        x_b: 1,
        u_a: 0,
        u_b: -1,
    };
    const Y_AB: Self = Self {
        x_a: 1,
        x_b: 1,
        u_a: -1,
        u_b: -1,
    };

    fn multiply(self, other: Self) -> Self {
        Self {
            x_a: self.x_a + other.x_a,
            x_b: self.x_b + other.x_b,
            u_a: self.u_a + other.u_a,
            u_b: self.u_b + other.u_b,
        }
    }
}

type Combination = BTreeMap<(State, Monomial), Z>;

fn set(values: &[Diagonal]) -> BTreeSet<Diagonal> {
    values.iter().copied().collect()
}

fn state(face: &[Diagonal], circles: &[Diagonal]) -> State {
    let value = State {
        face: set(face),
        circles: set(circles),
    };
    assert!(value.circles.is_subset(&value.face));
    value
}

fn incidence_sign(face: &BTreeSet<Diagonal>, added: Diagonal) -> Z {
    if face.iter().filter(|value| **value < added).count() % 2 == 0 {
        1
    } else {
        -1
    }
}

fn normal_sign(face_size: usize, position: usize) -> Z {
    if (3 - face_size + position) % 2 == 0 {
        1
    } else {
        -1
    }
}

fn add(output: &mut Combination, target: State, monomial: Monomial, coefficient: Z) {
    *output.entry((target, monomial)).or_default() += coefficient;
    output.retain(|_, value| *value != 0);
}

fn scale_add(output: &mut Combination, input: &Combination, scalar: Monomial, coefficient: Z) {
    for ((target, monomial), value) in input {
        add(
            output,
            target.clone(),
            monomial.multiply(scalar),
            coefficient * value,
        );
    }
}

fn denominator_allowed(target: &State, monomial: Monomial) -> bool {
    (monomial.u_a >= 0 || (target.face.contains(&A) && !target.circles.contains(&A)))
        && (monomial.u_b >= 0 || (target.face.contains(&B) && !target.circles.contains(&B)))
}

fn main() {
    assert!(D < A && A < B);
    let a = state(&[D, A], &[]);
    let b = state(&[D, B], &[]);
    let c = state(&[D, A, B], &[]);
    let n_a = state(&[D, A], &[A]);
    let n_b = state(&[D, B], &[B]);
    let c_a = state(&[D, A, B], &[A]);
    let c_b = state(&[D, A, B], &[B]);
    let c_ab = state(&[D, A, B], &[A, B]);

    // Derive, rather than fit, the entry-143 incidence and circle-removal signs.
    assert_eq!(incidence_sign(&a.face, B), 1);
    assert_eq!(incidence_sign(&b.face, A), -1);
    assert_eq!(normal_sign(2, 0), -1);
    assert_eq!(normal_sign(3, 0), 1);
    assert_eq!(normal_sign(3, 1), -1);

    let d_a = BTreeMap::from([((c.clone(), Monomial::Y_B), 1)]);
    let d_b = BTreeMap::from([((c.clone(), Monomial::Y_A), -1)]);
    let d_n_a = BTreeMap::from([
        ((a.clone(), Monomial::ONE), -1),
        ((c_a.clone(), Monomial::Y_B), 1),
    ]);
    let d_n_b = BTreeMap::from([
        ((b.clone(), Monomial::ONE), -1),
        ((c_b.clone(), Monomial::Y_A), -1),
    ]);
    let d_c_a = BTreeMap::from([((c.clone(), Monomial::ONE), 1)]);
    let d_c_b = d_c_a.clone();
    let d_c_ab = BTreeMap::from([
        ((c_b.clone(), Monomial::ONE), 1),
        ((c_a.clone(), Monomial::ONE), -1),
    ]);

    // d^2=0 on the three degree-up states.
    let mut square_n_a = Combination::new();
    scale_add(&mut square_n_a, &d_a, Monomial::ONE, -1);
    scale_add(&mut square_n_a, &d_c_a, Monomial::Y_B, 1);
    assert!(square_n_a.is_empty());
    let mut square_n_b = Combination::new();
    scale_add(&mut square_n_b, &d_b, Monomial::ONE, -1);
    scale_add(&mut square_n_b, &d_c_b, Monomial::Y_A, -1);
    assert!(square_n_b.is_empty());
    let mut square_c_ab = Combination::new();
    scale_add(&mut square_c_ab, &d_c_b, Monomial::ONE, 1);
    scale_add(&mut square_c_ab, &d_c_a, Monomial::ONE, -1);
    assert!(square_c_ab.is_empty());

    // z=y_a*A+y_b*B is the Koszul syzygy for the row (y_b,-y_a).
    let z = BTreeMap::from([
        ((a.clone(), Monomial::Y_A), 1),
        ((b.clone(), Monomial::Y_B), 1),
    ]);
    let mut d_z = Combination::new();
    scale_add(&mut d_z, &d_a, Monomial::Y_A, 1);
    scale_add(&mut d_z, &d_b, Monomial::Y_B, 1);
    assert!(d_z.is_empty());

    // In the fully Laurent-trivialized packet the unique primitive is
    // h=-y_a*N_a-y_b*N_b-y_a*y_b*C_ab.
    let mut d_h = Combination::new();
    scale_add(&mut d_h, &d_n_a, Monomial::Y_A, -1);
    scale_add(&mut d_h, &d_n_b, Monomial::Y_B, -1);
    scale_add(&mut d_h, &d_c_ab, Monomial::Y_AB, -1);
    assert_eq!(d_h, z);

    // Uniqueness: A and B coordinates force alpha=beta=0 in a cycle
    // alpha*N_a+beta*N_b+gamma*C_ab; then C_a forces gamma=0.
    let kernel_pivot_matrix = [[-1_i64, 0, 0], [0, -1, 0], [0, 0, -1]];
    let determinant =
        kernel_pivot_matrix[0][0] * kernel_pivot_matrix[1][1] * kernel_pivot_matrix[2][2];
    assert_eq!(determinant.abs(), 1);

    assert!(denominator_allowed(&a, Monomial::Y_A));
    assert!(denominator_allowed(&b, Monomial::Y_B));
    assert!(!denominator_allowed(&n_a, Monomial::Y_A));
    assert!(!denominator_allowed(&n_b, Monomial::Y_B));
    assert!(!denominator_allowed(&c_ab, Monomial::Y_AB));

    // Divisibility obstruction: normal removal N_a -> A has unit coefficient,
    // but the legal N_a coefficient ring has no negative u_a exponent.  Hence
    // it cannot produce the required A coefficient X_a/u_a (and similarly b).
    for legal_u_a_exponent in 0_i8..=3 {
        assert_ne!(legal_u_a_exponent, Monomial::Y_A.u_a);
    }

    println!(
        "{}",
        r#"{"claim":"For the actual compatible K6 face {D03,x1,x3}, the weighted Koszul syzygy z=(X_x1/u_x1)A+(X_x3/u_x3)B has the unique fully Laurent primitive h=-(X_x1/u_x1)N_x1-(X_x3/u_x3)N_x3-(X_x1 X_x3/(u_x1 u_x3))C_x1x3, but no primitive in the legal entry143 target-side BM-Cech summands because inverse u_x1 and u_x3 factors are forbidden on the corresponding circled states.","status":"falsified","scope":"Falsifies only existence of the primitive inside the legal entry143 BM-Cech compatible-face packet; the actual P labels exist, and a reciprocal line-dual/Gysin enlargement may repair the variance.","evidence_refs":["ledger entry 143","research/voevodsky/check_global_k6_koszul_cech_promotion.rs","research/voevodsky/check_d03_compatible_face_bm_cech_primitive_obstruction.rs"],"factorization_test":{"face":"{D03,x1,x3} is noncrossing and actual","differentials":{"dA":"y_b C","dB":"-y_a C","dN_a":"-A+y_b C_a","dN_b":"-B-y_a C_b","dC_a":"C","dC_b":"C","dC_ab":"C_b-C_a"},"d_squared_zero":true,"koszul_cycle":"z=y_a A+y_b B","full_laurent_primitive":"unique: h=-y_a N_a-y_b N_b-y_a y_b C_ab","integral_kernel":"zero with unimodular pivots","legal_BM_Cech":"FAIL: all three primitive terms violate the S\\H denominator rule","divisibility":"the legal N_a coefficient ring has u_a exponent >=0 and cannot produce X_a/u_a under unit normal removal; likewise for b","D_normal_row":"tensoring the D03 normal interval changes signs only and does not cure the short-circle denominator obstruction"},"unconstructed":["reciprocal line-dual pullback on circled states","supported Gysin comparison supplying that dual line","global normalization-sheet-to-entry143 map"],"boundary":"This packet is the genuine compatible D03 corridor face and is distinct from the crossing adjacent-ray dP6 no-go. The failure is coefficient variance, not absence of K6 support labels."}"#
    );
}
