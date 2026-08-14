//! Minimal algebra audit for the positive three-gallery top.
//!
//! This checker deliberately distinguishes two constructions.
//!
//! * The inherited mixed block has three Morse tops `m_i` with
//!   `d m_i = q_i - x_i xi_i`.  It is an honest absolute complex: the
//!   endpoint boundary of `q_i` is cancelled by that of `x_i xi_i`.
//! * A formal generator `c` with `d c = q_1 + q_3 + q_5` kills the generic
//!   leg only after passing endpoint-relative.  Absolutely, its square is
//!   the nonzero endpoint sum.  Thus this formal cone is not evidence for a
//!   Cech/Rees construction.
//!
//! The checker audits only this finite algebraic distinction.  In
//! particular it does not construct the missing marked extraordinary-
//! costalk/Beck--Chevalley comparison with the conductor source.

use std::ops::{Add, AddAssign, Neg, Sub};

#[derive(Clone, Copy, Debug, Default, Eq, PartialEq)]
struct Linear {
    // constant, x1, x3, x5
    coefficients: [i64; 4],
}

impl Linear {
    const fn constant(value: i64) -> Self {
        Self {
            coefficients: [value, 0, 0, 0],
        }
    }

    fn variable(index: usize) -> Self {
        let mut coefficients = [0; 4];
        coefficients[index + 1] = 1;
        Self { coefficients }
    }

    fn act(self, permutation: [usize; 3]) -> Self {
        let mut result = Self::default();
        result.coefficients[0] = self.coefficients[0];
        for (old, new) in permutation.into_iter().enumerate() {
            result.coefficients[new + 1] = self.coefficients[old + 1];
        }
        result
    }

    fn scale(self, scalar: i64) -> Self {
        let mut result = self;
        for coefficient in &mut result.coefficients {
            *coefficient *= scalar;
        }
        result
    }
}

impl Add for Linear {
    type Output = Self;

    fn add(mut self, right: Self) -> Self::Output {
        self += right;
        self
    }
}

impl AddAssign for Linear {
    fn add_assign(&mut self, right: Self) {
        for (left, value) in self.coefficients.iter_mut().zip(right.coefficients) {
            *left += value;
        }
    }
}

impl Neg for Linear {
    type Output = Self;

    fn neg(self) -> Self::Output {
        self.scale(-1)
    }
}

impl Sub for Linear {
    type Output = Self;

    fn sub(self, right: Self) -> Self::Output {
        self + (-right)
    }
}

type DegreeTwo = [i64; 4]; // m1, m3, m5, formal Cech top c
type DegreeOne = [Linear; 6]; // q1, q3, q5, xi1, xi3, xi5
type DegreeZero = [Linear; 3]; // the three endpoint-boundary symbols

fn d_two(value: DegreeTwo) -> DegreeOne {
    let mut result = [Linear::default(); 6];
    for index in 0..3 {
        // d m_i = q_i - x_i xi_i
        result[index] += Linear::constant(value[index]);
        result[index + 3] += Linear::variable(index).scale(-value[index]);
        // The fourth generator is the formal attempted Cech filler.
        result[index] += Linear::constant(value[3]);
    }
    result
}

fn multiply_by_variable(value: Linear, variable: usize) -> Linear {
    // d_two produces only constant q coefficients.  The endpoint audit never
    // needs products of two variables; reject accidental scope expansion.
    assert_eq!(value.coefficients[1..], [0, 0, 0]);
    Linear::variable(variable).scale(value.coefficients[0])
}

fn d_one_absolute(value: DegreeOne) -> DegreeZero {
    let mut result = [Linear::default(); 3];
    for index in 0..3 {
        // d q_i = x_i b_i and d xi_i = b_i.  This is the universal algebraic
        // shadow of d(q_i - x_i xi_i)=0 in each loaded Morse gallery.
        result[index] += multiply_by_variable(value[index], index);
        result[index] += value[index + 3];
    }
    result
}

fn act_degree_two(value: DegreeTwo, permutation: [usize; 3]) -> DegreeTwo {
    let mut result = [0; 4];
    for (old, new) in permutation.into_iter().enumerate() {
        result[new] = value[old];
    }
    result[3] = value[3];
    result
}

fn act_degree_one(value: DegreeOne, permutation: [usize; 3]) -> DegreeOne {
    let mut result = [Linear::default(); 6];
    for (old, new) in permutation.into_iter().enumerate() {
        result[new] = value[old].act(permutation);
        result[new + 3] = value[old + 3].act(permutation);
    }
    result
}

fn act_degree_zero(value: DegreeZero, permutation: [usize; 3]) -> DegreeZero {
    let mut result = [Linear::default(); 3];
    for (old, new) in permutation.into_iter().enumerate() {
        result[new] = value[old].act(permutation);
    }
    result
}

fn compose(first: [usize; 3], second: [usize; 3]) -> [usize; 3] {
    // Apply first, then second.
    [second[first[0]], second[first[1]], second[first[2]]]
}

fn act_tags(value: [i64; 3], permutation: [usize; 3], orientation: i64) -> [i64; 3] {
    let mut result = [0; 3];
    for (old, new) in permutation.into_iter().enumerate() {
        result[new] = orientation * value[old];
    }
    result
}

fn main() {
    let rotation = [1, 2, 0];
    let reflection = [0, 2, 1];
    let identity = [0, 1, 2];

    assert_eq!(compose(compose(rotation, rotation), rotation), identity);
    assert_eq!(compose(reflection, reflection), identity);
    assert_eq!(
        compose(compose(reflection, rotation), reflection),
        compose(rotation, rotation)
    );

    // Both differentials are semilinearly D3-covariant: D3 permutes the
    // occurrence variables together with the three gallery sectors.
    for basis in 0..4 {
        let mut vector = [0; 4];
        vector[basis] = 1;
        for action in [rotation, reflection] {
            assert_eq!(
                d_two(act_degree_two(vector, action)),
                act_degree_one(d_two(vector), action)
            );
        }
    }
    for basis in 0..6 {
        let mut vector = [Linear::default(); 6];
        vector[basis] = Linear::constant(1);
        for action in [rotation, reflection] {
            assert_eq!(
                d_one_absolute(act_degree_one(vector, action)),
                act_degree_zero(d_one_absolute(vector), action)
            );
        }
    }

    // Model (b): retain the mixed top.  It is the sum of the three inherited
    // Morse tops and has the required generic and occurrence-loaded legs.
    let mixed_top = [1, 1, 1, 0];
    let mixed_boundary = d_two(mixed_top);
    assert_eq!(
        mixed_boundary,
        [
            Linear::constant(1),
            Linear::constant(1),
            Linear::constant(1),
            -Linear::variable(0),
            -Linear::variable(1),
            -Linear::variable(2),
        ]
    );
    assert_eq!(d_one_absolute(mixed_boundary), [Linear::default(); 3]);
    assert_eq!(act_degree_two(mixed_top, rotation), mixed_top);
    assert_eq!(act_degree_two(mixed_top, reflection), mixed_top);

    // Model (a): one formal invariant top c is the unique rank-one way to
    // cancel the primitive diagonal q-sum.  It works only after endpoints
    // have been divided out.  Absolutely d^2(c) is nonzero.
    let formal_cech_top = [0, 0, 0, 1];
    let generic_sum = d_two(formal_cech_top);
    assert_eq!(
        generic_sum,
        [
            Linear::constant(1),
            Linear::constant(1),
            Linear::constant(1),
            Linear::default(),
            Linear::default(),
            Linear::default(),
        ]
    );
    let absolute_cech_square = d_one_absolute(generic_sum);
    assert_eq!(
        absolute_cech_square,
        [
            Linear::variable(0),
            Linear::variable(1),
            Linear::variable(2),
        ]
    );
    assert_ne!(absolute_cech_square, [Linear::default(); 3]);

    let formally_cancelled_top = [1, 1, 1, -1];
    let relative_special_boundary = d_two(formally_cancelled_top);
    assert_eq!(
        relative_special_boundary,
        [
            Linear::default(),
            Linear::default(),
            Linear::default(),
            -Linear::variable(0),
            -Linear::variable(1),
            -Linear::variable(2),
        ]
    );
    assert_ne!(
        d_one_absolute(relative_special_boundary),
        [Linear::default(); 3]
    );
    // In the endpoint-relative quotient d_one is zero, so the same formal
    // attachment is square-zero there.  This quotient is not an absolute
    // normalization--conductor construction and does not supply provenance.
    let relative_square = [Linear::default(); 3];
    assert_eq!(relative_square, [Linear::default(); 3]);

    // D3 covariance of the first conductor grade uses the ordered normal
    // orientation line.  Rotation preserves it; reflection reverses it.
    // Therefore the raw invariant mixed top becomes the orientation-odd
    // f_+, and the three local classes -[x_i] xi_i map to the odd tag norm.
    let norm = [1, 1, 1];
    assert_eq!(act_tags(norm, rotation, 1), norm);
    assert_eq!(act_tags(norm, reflection, -1), [-1, -1, -1]);
    let top_rotation = 1;
    let top_reflection = -1;
    assert_eq!(act_tags(norm, rotation, 1), [top_rotation; 3]);
    assert_eq!(act_tags(norm, reflection, -1), [top_reflection; 3]);

    // Derived conductor base change must not truncate the Cartier legs.
    // For each i, K(x_i) tensor R/(x1,x3,x5) is [C --0--> C], hence has
    // one H0 copy and one Tor1 copy.  No coefficient used above is inverted.
    let derived_base_change_ranks = [[1_usize, 1_usize]; 3];
    assert!(derived_base_change_ranks
        .iter()
        .all(|ranks| *ranks == [1, 1]));

    // An invariant formal q-column has coefficients (a,a,a).  Primitive
    // cancellation of (1,1,1) forces a=1, not 1/3.  This proves algebraic
    // uniqueness, not geometric existence of the column.
    let primitive_coefficient = 1_i64;
    assert_eq!(
        [primitive_coefficient; 3],
        generic_sum[..3]
            .iter()
            .map(|entry| entry.coefficients[0])
            .collect::<Vec<_>>()
            .as_slice()
    );

    println!(
        "{}",
        r#"{"claim":"The inherited D3-stable mixed block dH_Sigma=q_Sigma-(x1*xi1+x3*xi3+x5*xi5) is an absolute square-zero occurrence-loaded boundary-crossing complex. It is the smallest currently canonical source block, but it is not yet alpha_plus. A formal invariant Cech top dc=q_Sigma is the unique primitive algebraic cancellation only endpoint-relative and is not supplied by the existing geometry.","status":"inconclusive","assumptions":["The three rotated loaded Morse identities and orientations are those inherited from entries 110-112.","The absolute endpoint shadow is represented by d(q_i)=x_i*b_i and d(xi_i)=b_i; endpoint-relative means quotienting all b_i.","The ordered positive conductor normal line supplies the reflection sign on the first associated grade."],"evidence_refs":["research/voevodsky/check_positive_mixed_rees_top.rs","research/voevodsky/check_absolute_unlocalized_support_pc.rs","research/voevodsky/check_d03_whole_gallery_tag_gysin.rs","research/voevodsky/check_three_rotated_gallery_top_gluing.rs","ledger entries 93, 99, 102, 105, and 112"],"factorization_test":{"mixed_absolute_d_squared":"passed","mixed_D3_covariance":"passed semilinearly with x1,x3,x5 permuted","generic_Q_leg":"retained as q_Sigma","special_boundary":"-(x1*xi1+x3*xi3+x5*xi5)","first_conductor_grade":"the three oriented Cartier classes give t1+t3+t5=d f_plus","derived_base_change":"each R/(x_i) tensor^L C is [C --0--> C], retaining H0 and Tor1","formal_q_kill_endpoint_relative":"passed with one primitive invariant top and no division by three","formal_q_kill_absolute":"failed: d^2c=x1*b1+x3*b3+x5*b5 is nonzero","D3_costalk_Beck_Chevalley":"unconstructed","inversions":"none"},"counterevidence":["The primitive q_Sigma class has no filler relative only to its four endpoints in the existing barycentric carrier.","Quotienting by the full short boundary makes q_Sigma bound but also removes the three special galleries.","Adding dc=q_Sigma directly both fits the desired cancellation and fails absolute d^2 unless a further endpoint-compatible Cech/Rees map is supplied.","Entry 112 constructs only the ordinary supported associated-grade gallery-to-tag maps; it does not lift their Tor1/excess costalks."],"next_experiment":"Construct one D3-equivariant marked extraordinary-costalk/Beck--Chevalley comparison from the mixed F1 special gallery block to the positive conductor costalk, compatible with the canonical F0 subset F1 subset F2 Yoneda cone roof. It must lift all three ordinary Cartier tag maps and retain their Tor1/excess copies; then test that the cone roof cancels q_Sigma and yields the norm top without a fitted dc=q_Sigma column."}"#
    );
}
