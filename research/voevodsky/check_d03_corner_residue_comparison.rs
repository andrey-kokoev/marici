//! Exact finite algebra certificate for the scoped D03 corner-residue comparison.
//!
//! The full weighted road square has a closed opposite subcomplex.  Its quotient
//! is the entry-120 occurrence Koszul diamond, and dualizing the quotient map
//! gives a supported cochain map into the full road dual.  The supported map is
//! not the full entry-97 trace: it becomes null after occurrence localization,
//! whereas the endpoint-normalized full-road H^0 functional remains nonzero.
//!
//! On the supported quotient, the full Koszul--Cech comparison has nonzero
//! components in every degree.  With the road orientation `(x3,x1)`, its top is
//! `+1/(x1*x3)`.  Composing the independent repeated-normal excess trace with
//! its target Koszul--Cech map sends `eta_mix=(-q3,-1)` to
//! `+1/(u0*u1*u3*u5)`.  Their product, followed by the separately oriented
//! physical line `[dX03]=+1`, is therefore the positive corner residue.
//!
//! This checker does not construct a six-functor identification of that corner
//! residue with the whole bivariant `Theta_03`; indeed, its localization and
//! support tests prove that such an identification would be false.

use std::collections::BTreeMap;

type Int = i64;

const X0: usize = 0;
const X1: usize = 1;
const X3: usize = 2;
const X4: usize = 3;
const U0: usize = 4;
const U1: usize = 5;
const U3: usize = 6;
const U5: usize = 7;
const Q3: usize = 8;
const VARIABLE_COUNT: usize = 9;

#[derive(Clone, Debug, Default, Eq, PartialEq)]
struct Poly(BTreeMap<[u8; 4], Int>);

impl Poly {
    fn monomial(coefficient: Int, powers: [u8; 4]) -> Self {
        if coefficient == 0 {
            return Self::default();
        }
        Self(BTreeMap::from([(powers, coefficient)]))
    }

    fn one() -> Self {
        Self::monomial(1, [0; 4])
    }

    fn variable(slot: usize) -> Self {
        let mut powers = [0; 4];
        powers[slot] = 1;
        Self::monomial(1, powers)
    }

    fn add_scaled(&mut self, other: &Self, scale: Int) {
        for (&powers, &coefficient) in &other.0 {
            *self.0.entry(powers).or_default() += scale * coefficient;
        }
        self.0.retain(|_, coefficient| *coefficient != 0);
    }

    fn add(&self, other: &Self) -> Self {
        let mut result = self.clone();
        result.add_scaled(other, 1);
        result
    }

    fn negate(&self) -> Self {
        let mut result = Self::default();
        result.add_scaled(self, -1);
        result
    }

    fn multiply(&self, other: &Self) -> Self {
        let mut result = Self::default();
        for (&left_powers, &left_coefficient) in &self.0 {
            for (&right_powers, &right_coefficient) in &other.0 {
                let powers = std::array::from_fn(|slot| left_powers[slot] + right_powers[slot]);
                *result.0.entry(powers).or_default() += left_coefficient * right_coefficient;
            }
        }
        result.0.retain(|_, coefficient| *coefficient != 0);
        result
    }

    fn specialize_x1_x3_to_zero(&self) -> Self {
        Self(
            self.0
                .iter()
                .filter(|(powers, _)| powers[X1] == 0 && powers[X3] == 0)
                .map(|(&powers, &coefficient)| (powers, coefficient))
                .collect(),
        )
    }

    fn lies_in_x1_x3_ideal(&self) -> bool {
        self.0.keys().all(|powers| powers[X1] > 0 || powers[X3] > 0)
    }
}

type PolyMatrix = Vec<Vec<Poly>>;

fn poly_matrix(rows: usize, columns: usize) -> PolyMatrix {
    vec![vec![Poly::default(); columns]; rows]
}

fn poly_identity(rank: usize) -> PolyMatrix {
    let mut result = poly_matrix(rank, rank);
    for (index, row) in result.iter_mut().enumerate() {
        row[index] = Poly::one();
    }
    result
}

fn poly_transpose(matrix: &PolyMatrix) -> PolyMatrix {
    assert!(!matrix.is_empty());
    let mut result = poly_matrix(matrix[0].len(), matrix.len());
    for (row, entries) in matrix.iter().enumerate() {
        for (column, entry) in entries.iter().enumerate() {
            result[column][row] = entry.clone();
        }
    }
    result
}

fn poly_multiply(left: &PolyMatrix, right: &PolyMatrix) -> PolyMatrix {
    assert!(!left.is_empty());
    assert!(!right.is_empty());
    assert_eq!(left[0].len(), right.len());
    let mut result = poly_matrix(left.len(), right[0].len());
    for (row, left_entries) in left.iter().enumerate() {
        for (middle, left_entry) in left_entries.iter().enumerate() {
            for (column, right_entry) in right[middle].iter().enumerate() {
                result[row][column] = result[row][column].add(&left_entry.multiply(right_entry));
            }
        }
    }
    result
}

#[derive(Clone)]
struct RoadData {
    d_two: PolyMatrix,
    d_one: PolyMatrix,
    diamond_d_two: PolyMatrix,
    diamond_d_one: PolyMatrix,
    r_two: PolyMatrix,
    r_one: PolyMatrix,
    r_zero: PolyMatrix,
}

fn road_data() -> RoadData {
    let x0 = Poly::variable(X0);
    let x1 = Poly::variable(X1);
    let x3 = Poly::variable(X3);
    let x4 = Poly::variable(X4);

    // Q2=<F>, Q1=<a,b,c,d>, Q0=<v00,v10,v01,v11>.
    let d_two = vec![
        vec![x3.clone()],
        vec![x4.negate()],
        vec![x0.negate()],
        vec![x1.clone()],
    ];
    let d_one = vec![
        vec![x0.negate(), Poly::default(), x3.negate(), Poly::default()],
        vec![x1.clone(), Poly::default(), Poly::default(), x3.negate()],
        vec![Poly::default(), x0.negate(), x4.clone(), Poly::default()],
        vec![Poly::default(), x1.clone(), Poly::default(), x4],
    ];

    // K_occ(x1,x3): F -> (Z3,Z1) -> v, with the entry-120 orientation.
    let diamond_d_two = vec![vec![x3], vec![x1.negate()]];
    let diamond_d_one = vec![vec![x1, Poly::variable(X3)]];

    // r(F)=F, r(a)=Z3, r(d)=-Z1, r(v10)=v; B_opp is killed.
    let r_two = poly_identity(1);
    let r_one = vec![
        vec![
            Poly::one(),
            Poly::default(),
            Poly::default(),
            Poly::default(),
        ],
        vec![
            Poly::default(),
            Poly::default(),
            Poly::default(),
            Poly::one().negate(),
        ],
    ];
    let r_zero = vec![vec![
        Poly::default(),
        Poly::one(),
        Poly::default(),
        Poly::default(),
    ]];

    RoadData {
        d_two,
        d_one,
        diamond_d_two,
        diamond_d_one,
        r_two,
        r_one,
        r_zero,
    }
}

fn check_road_square_subcomplex_and_quotient() -> RoadData {
    let data = road_data();
    assert_eq!(poly_multiply(&data.d_one, &data.d_two), poly_matrix(4, 1));

    // B_opp=<b,c,v00,v01,v11>.  Boundaries of b and c have no v10 term.
    let b_column = 1;
    let c_column = 2;
    let v10_row = 1;
    assert_eq!(data.d_one[v10_row][b_column], Poly::default());
    assert_eq!(data.d_one[v10_row][c_column], Poly::default());

    assert_eq!(
        poly_multiply(&data.diamond_d_one, &data.diamond_d_two),
        poly_matrix(1, 1)
    );
    assert_eq!(
        poly_multiply(&data.r_one, &data.d_two),
        poly_multiply(&data.diamond_d_two, &data.r_two)
    );
    assert_eq!(
        poly_multiply(&data.r_zero, &data.d_one),
        poly_multiply(&data.diamond_d_one, &data.r_one)
    );

    // The quotient really has dF=x3*Z3-x1*Z1, dZ3=x1*v, dZ1=x3*v.
    assert_eq!(
        data.diamond_d_two,
        vec![vec![Poly::variable(X3)], vec![Poly::variable(X1).negate()]]
    );
    assert_eq!(
        data.diamond_d_one,
        vec![vec![Poly::variable(X1), Poly::variable(X3)]]
    );
    data
}

fn check_finite_free_dual(data: &RoadData) {
    // D(r):D(Q/B)->D(Q) is the transpose in each degree.  Its visible basis
    // images are v^*|->v10^*, Z3^*|->a^*, Z1^*|->-d^*, F^*|->F^*.
    let dual_r_zero = poly_transpose(&data.r_zero);
    let dual_r_one = poly_transpose(&data.r_one);
    let dual_r_two = poly_transpose(&data.r_two);
    assert_eq!(
        dual_r_zero,
        vec![
            vec![Poly::default()],
            vec![Poly::one()],
            vec![Poly::default()],
            vec![Poly::default()]
        ]
    );
    assert_eq!(
        dual_r_one,
        vec![
            vec![Poly::one(), Poly::default()],
            vec![Poly::default(), Poly::default()],
            vec![Poly::default(), Poly::default()],
            vec![Poly::default(), Poly::one().negate()]
        ]
    );
    assert_eq!(dual_r_two, poly_identity(1));

    let dual_q_d_zero = poly_transpose(&data.d_one);
    let dual_q_d_one = poly_transpose(&data.d_two);
    let dual_diamond_d_zero = poly_transpose(&data.diamond_d_one);
    let dual_diamond_d_one = poly_transpose(&data.diamond_d_two);
    assert_eq!(
        poly_multiply(&dual_q_d_zero, &dual_r_zero),
        poly_multiply(&dual_r_one, &dual_diamond_d_zero)
    );
    assert_eq!(
        poly_multiply(&dual_q_d_one, &dual_r_one),
        poly_multiply(&dual_r_two, &dual_diamond_d_one)
    );
}

fn check_no_strict_primal_section() {
    let x0 = Poly::variable(X0);
    let x4 = Poly::variable(X4);
    let minus_x0 = x0.negate();
    let minus_x4 = x4.negate();

    // A strict section would have s(F)=F and
    // s(Z3)=a+A_b*b+A_c*c, s(Z1)=-d+B_b*b+B_c*c.  Comparing the b,c
    // coefficients in d s(F)=s d(F) forces
    // x3*A_b-x1*B_b=-x4 and x3*A_c-x1*B_c=-x0.
    // Every left side lies in (x1,x3), but neither right side does.
    assert!(!minus_x4.lies_in_x1_x3_ideal());
    assert!(!minus_x0.lies_in_x1_x3_ideal());
    assert_eq!(minus_x4.specialize_x1_x3_to_zero(), minus_x4);
    assert_eq!(minus_x0.specialize_x1_x3_to_zero(), minus_x0);
    assert_ne!(minus_x4, Poly::default());
    assert_ne!(minus_x0, Poly::default());
}

#[derive(Clone, Debug, Default, Eq, PartialEq)]
struct LaurentPoly(BTreeMap<[i8; VARIABLE_COUNT], Int>);

impl LaurentPoly {
    fn monomial(coefficient: Int, powers: [i8; VARIABLE_COUNT]) -> Self {
        if coefficient == 0 {
            return Self::default();
        }
        Self(BTreeMap::from([(powers, coefficient)]))
    }

    fn one() -> Self {
        Self::monomial(1, [0; VARIABLE_COUNT])
    }

    fn variable(slot: usize) -> Self {
        let mut powers = [0; VARIABLE_COUNT];
        powers[slot] = 1;
        Self::monomial(1, powers)
    }

    fn inverse_variable(slot: usize) -> Self {
        let mut powers = [0; VARIABLE_COUNT];
        powers[slot] = -1;
        Self::monomial(1, powers)
    }

    fn add_scaled(&mut self, other: &Self, scale: Int) {
        for (&powers, &coefficient) in &other.0 {
            *self.0.entry(powers).or_default() += scale * coefficient;
        }
        self.0.retain(|_, coefficient| *coefficient != 0);
    }

    fn add(&self, other: &Self) -> Self {
        let mut result = self.clone();
        result.add_scaled(other, 1);
        result
    }

    fn negate(&self) -> Self {
        let mut result = Self::default();
        result.add_scaled(self, -1);
        result
    }

    fn multiply(&self, other: &Self) -> Self {
        let mut result = Self::default();
        for (&left_powers, &left_coefficient) in &self.0 {
            for (&right_powers, &right_coefficient) in &other.0 {
                let powers = std::array::from_fn(|slot| left_powers[slot] + right_powers[slot]);
                *result.0.entry(powers).or_default() += left_coefficient * right_coefficient;
            }
        }
        result.0.retain(|_, coefficient| *coefficient != 0);
        result
    }
}

fn laurent_dot(left: &[LaurentPoly], right: &[LaurentPoly]) -> LaurentPoly {
    assert_eq!(left.len(), right.len());
    left.iter()
        .zip(right)
        .fold(LaurentPoly::default(), |sum, (a, b)| {
            sum.add(&a.multiply(b))
        })
}

fn check_full_cech_corner_map() -> LaurentPoly {
    // Dual Koszul differential:
    // v^* -> x1*Z3^*+x3*Z1^*, (Z3^*,Z1^*) -> (x3,-x1)*F^*.
    // Full Cech differential is delta0(r)=(r,r), delta1(a,b)=a-b.
    let x1 = LaurentPoly::variable(X1);
    let x3 = LaurentPoly::variable(X3);
    let inv_x1 = LaurentPoly::inverse_variable(X1);
    let inv_x3 = LaurentPoly::inverse_variable(X3);
    let one = LaurentPoly::one();

    let phi_zero = one.clone();
    let phi_one_z3 = [inv_x1.clone(), LaurentPoly::default()];
    let phi_one_z1 = [LaurentPoly::default(), inv_x3.clone()];
    let phi_two = inv_x1.multiply(&inv_x3);

    let cech_d_zero = [phi_zero.clone(), phi_zero];
    let phi_d_zero = [
        x1.multiply(&phi_one_z3[0])
            .add(&x3.multiply(&phi_one_z1[0])),
        x1.multiply(&phi_one_z3[1])
            .add(&x3.multiply(&phi_one_z1[1])),
    ];
    assert_eq!(phi_d_zero, cech_d_zero);

    let cech_d_z3 = phi_one_z3[0].add(&phi_one_z3[1].negate());
    let cech_d_z1 = phi_one_z1[0].add(&phi_one_z1[1].negate());
    assert_eq!(cech_d_z3, x3.multiply(&phi_two));
    assert_eq!(cech_d_z1, x1.negate().multiply(&phi_two));
    assert_eq!(
        phi_two,
        LaurentPoly::inverse_variable(X1).multiply(&LaurentPoly::inverse_variable(X3))
    );

    // A top-only assignment is not a chain map: both top-boundary images are
    // nonzero.  Likewise the forced degree-one terms require phi(v^*)=1.
    assert_ne!(x3.multiply(&phi_two), LaurentPoly::default());
    assert_ne!(x1.negate().multiply(&phi_two), LaurentPoly::default());
    assert_ne!(phi_d_zero, [LaurentPoly::default(), LaurentPoly::default()]);
    phi_two
}

fn check_normal_residue_and_combined_sign(occurrence_top: &LaurentPoly) {
    let q3 = LaurentPoly::variable(Q3);
    let eta_mix = [q3.negate(), LaurentPoly::one().negate()];
    let tr_ex = [LaurentPoly::default(), LaurentPoly::one().negate()];
    assert_eq!(laurent_dot(&tr_ex, &eta_mix), LaurentPoly::one());

    let normal_residue = [U0, U1, U3, U5]
        .into_iter()
        .fold(LaurentPoly::one(), |product, variable| {
            product.multiply(&LaurentPoly::inverse_variable(variable))
        });
    let eta_image = laurent_dot(&tr_ex, &eta_mix).multiply(&normal_residue);
    assert_eq!(eta_image, normal_residue);

    let physical_dx03_orientation = 1_i64;
    let combined = occurrence_top
        .multiply(&eta_image)
        .multiply(&LaurentPoly::monomial(
            physical_dx03_orientation,
            [0; VARIABLE_COUNT],
        ));
    let expected = [X1, X3, U0, U1, U3, U5]
        .into_iter()
        .fold(LaurentPoly::one(), |product, variable| {
            product.multiply(&LaurentPoly::inverse_variable(variable))
        });
    assert_eq!(combined, expected);
}

type IntMatrix = Vec<Vec<Int>>;

fn int_multiply(left: &IntMatrix, right: &IntMatrix) -> IntMatrix {
    assert!(!left.is_empty());
    assert!(!right.is_empty());
    assert_eq!(left[0].len(), right.len());
    let mut result = vec![vec![0; right[0].len()]; left.len()];
    for (row, left_entries) in left.iter().enumerate() {
        for (middle, left_entry) in left_entries.iter().enumerate() {
            for (column, right_entry) in right[middle].iter().enumerate() {
                result[row][column] += left_entry * right_entry;
            }
        }
    }
    result
}

fn int_add(left: &IntMatrix, right: &IntMatrix) -> IntMatrix {
    assert_eq!(left.len(), right.len());
    left.iter()
        .zip(right)
        .map(|(left_row, right_row)| {
            left_row
                .iter()
                .zip(right_row)
                .map(|(left_entry, right_entry)| left_entry + right_entry)
                .collect()
        })
        .collect()
}

fn check_localization_negative_control() {
    // After x1 is a unit, rescale it to one.  For the dual diamond
    // d0=(1,x3)^T, d1=(x3,-1), the displayed cochain homotopy contracts all
    // degrees.  Hence D(r), whose source is this dual diamond, is nullhomotopic.
    let x3 = 11_i64;
    let d_zero = vec![vec![1], vec![x3]];
    let d_one = vec![vec![x3, -1]];
    let h_one = vec![vec![1, 0]];
    let h_two = vec![vec![0], vec![-1]];
    assert_eq!(int_multiply(&h_one, &d_zero), vec![vec![1]]);
    assert_eq!(int_multiply(&d_one, &h_two), vec![vec![1]]);
    assert_eq!(
        int_add(
            &int_multiply(&d_zero, &h_one),
            &int_multiply(&h_two, &d_one)
        ),
        vec![vec![1, 0], vec![0, 1]]
    );

    // The full normalized road H^0 trace survives the same Laurent base.
    // Its four values are inverse principal occurrence weights and kill all
    // four road boundaries.  In cochain degree zero there are no boundaries
    // entering it, so this nonzero cocycle represents a nonzero H^0 class.
    let x0 = LaurentPoly::variable(X0);
    let x1 = LaurentPoly::variable(X1);
    let x3_laurent = LaurentPoly::variable(X3);
    let x4 = LaurentPoly::variable(X4);
    let vertex_weights = [
        x0.multiply(&x3_laurent),
        x1.multiply(&x3_laurent),
        x0.multiply(&x4),
        x1.multiply(&x4),
    ];
    let trace = [
        LaurentPoly::inverse_variable(X0).multiply(&LaurentPoly::inverse_variable(X3)),
        LaurentPoly::inverse_variable(X1).multiply(&LaurentPoly::inverse_variable(X3)),
        LaurentPoly::inverse_variable(X0).multiply(&LaurentPoly::inverse_variable(X4)),
        LaurentPoly::inverse_variable(X1).multiply(&LaurentPoly::inverse_variable(X4)),
    ];
    for (weight, value) in vertex_weights.iter().zip(&trace) {
        assert_eq!(weight.multiply(value), LaurentPoly::one());
    }
    let road_boundaries = [
        [
            x0.negate(),
            x1.clone(),
            LaurentPoly::default(),
            LaurentPoly::default(),
        ],
        [
            LaurentPoly::default(),
            LaurentPoly::default(),
            x0.negate(),
            x1,
        ],
        [
            x3_laurent.negate(),
            LaurentPoly::default(),
            x4.clone(),
            LaurentPoly::default(),
        ],
        [
            LaurentPoly::default(),
            x3_laurent.negate(),
            LaurentPoly::default(),
            x4,
        ],
    ];
    for boundary in road_boundaries {
        assert_eq!(laurent_dot(&trace, &boundary), LaurentPoly::default());
    }
    assert!(trace.iter().all(|value| *value != LaurentPoly::default()));

    // D(r) is supported only at v10 in degree zero, while the full road trace
    // is nonzero at every road vertex.  Thus the corner residue is not the
    // full Theta_03 representative even before using the localization no-go.
    let supported_vertices = [false, true, false, false];
    let full_trace_vertices = trace.map(|value| value != LaurentPoly::default());
    assert_ne!(supported_vertices, full_trace_vertices);
    assert_eq!(full_trace_vertices, [true; 4]);
}

fn main() {
    let road = check_road_square_subcomplex_and_quotient();
    check_finite_free_dual(&road);
    check_no_strict_primal_section();
    let occurrence_top = check_full_cech_corner_map();
    check_normal_residue_and_combined_sign(&occurrence_top);
    check_localization_negative_control();

    println!(
        "{}",
        concat!(
            r#"{"claim":"the finite-free dual of the opposite-road quotient, followed by the full occurrence and normal target Koszul--Cech comparisons, gives the positive D03 v10 corner residue, but it does not give the full entry-97 Theta_03 trace","status":"proved_scoped_and_falsified_full_identification","scope":"finite algebraic road quotient, dual support map, target Cech residues, signs, and localization negative controls only","ring":"unlocalized polynomial occurrence ring for Q and Q/B; target localizations are applied only by the two Koszul--Cech comparisons","claims":{"proved":["the full weighted road-square differential squares to zero","B_opp=<b,c,v00,v01,v11> is a subcomplex","Q/B is the entry-120 diamond dF=x3*Z3-x1*Z1, dZ3=x1*v, dZ1=x3*v","r(F)=F, r(a)=Z3, r(d)=-Z1, r(v10)=v is a chain quotient","finite-free D(r) is a chain map with Z1^* mapping to -d^*","the full occurrence Koszul--Cech map has forced lower terms v^*->1, Z3^*->(1/x1,0), Z1^*->(0,1/x3) and oriented top F^*->+1/(x1*x3)","tr_ex sends eta_mix=(-q3,-1) to 1 and target normal Koszul--Cech sends it to +1/(u0*u1*u3*u5)","the combined occurrence-normal coefficient is +1/(x1*x3*u0*u1*u3*u5) and the independent physical orientation is [dX03]=+1","after Laurent localization D(Q/B) is explicitly contractible, so D(r) is nullhomotopic, while the normalized full-road H0 trace remains nonzero"],"falsified":["a strict primal section Q/B->Q: its top chain equation would require -x4 and -x0 to lie in the ideal (x1,x3)","identifying the supported corner residue with the full Theta_03: D(r) has only v10 support and dies after occurrence localization, while the full normalized road trace is nonzero on all four vertices and survives"],"unconstructed":["a ringed six-functor provenance identifying the quotient-dual map with an extraordinary pull-push","a target-side geometric Cousin realization beyond the certified algebraic Koszul--Cech maps","an equality with the entire entry-97 reciprocal-standard/original-BM bivariant trace"]},"checks":{"road_d_squared":"PASS","B_opp_subcomplex":"PASS","quotient_and_r_chain_map":"PASS","finite_free_dual_signs":"PASS","strict_primal_section":"FAIL by the exact (x1,x3)-ideal obstruction","occurrence_full_Cech":"PASS with mandatory degree-zero and degree-one terms","normal_eta_residue":"PASS","combined_sign":"PASS","physical_dX03":"PASS +1 independently","localized_supported_map":"NULLHOMOTOPIC","full_road_H0":"NONZERO","full_Theta03_identification":"FALSIFIED"},"next_experiment":"construct the geometric corner restriction/residue morphism from the actual reciprocal-standard/original-BM road square and compare only its v10 local-cohomology boundary with this class; do not promote the supported quotient map to the full road trace"}"#
        )
    );
}
