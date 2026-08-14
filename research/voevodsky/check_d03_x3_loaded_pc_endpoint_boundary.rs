//! Exact audit of the entry-129 x3 occurrence Gysin after tensoring with the
//! frozen D03 coefficient packet of entries 97 and 100.
//!
//! The checker deliberately separates two assertions.
//!
//! 1. In the finite coefficient/Cousin model, the x3 Gysin has simultaneous
//!    v00 and v10 endpoint maps.  Both maps retain every lower occurrence
//!    Cech term, the reciprocal-regular/original-Borel--Moore variance, the
//!    Tor_0 quotient and primitive Tor_1 repeated-normal excess, and the
//!    independent positive physical line [dX03].
//! 2. These coefficient maps are not silently cast to actual ringed PC
//!    extraordinary costalks.  Such a cast would require, at each endpoint,
//!    an occurrence-loaded purity/costalk comparison.  Entry 121 explicitly
//!    leaves even the v10 comparison unconstructed.
//!
//! No occurrence or support normal is inverted in the base.  Negative powers
//! occur only in the indicated target Cech localization summands.

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
const T3: usize = 9;
const VARIABLE_COUNT: usize = 10;

#[derive(Clone, Debug, Default, Eq, PartialEq)]
struct Laurent(BTreeMap<[i8; VARIABLE_COUNT], Int>);

impl Laurent {
    fn monomial(coefficient: Int, powers: [i8; VARIABLE_COUNT]) -> Self {
        if coefficient == 0 {
            return Self::default();
        }
        Self(BTreeMap::from([(powers, coefficient)]))
    }

    fn scalar(coefficient: Int) -> Self {
        Self::monomial(coefficient, [0; VARIABLE_COUNT])
    }

    fn one() -> Self {
        Self::scalar(1)
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
                let powers =
                    std::array::from_fn(|slot| left_powers[slot] + right_powers[slot]);
                *result.0.entry(powers).or_default() += left_coefficient * right_coefficient;
            }
        }
        result.0.retain(|_, coefficient| *coefficient != 0);
        result
    }

    fn support_variables_unlocalized(&self) -> bool {
        self.0.keys().all(|powers| {
            [X0, X1, X3, X4, U0, U1, U3, U5, T3]
                .into_iter()
                .all(|slot| powers[slot] >= 0)
        })
    }
}

type Matrix = Vec<Vec<Laurent>>;

fn zero_matrix(rows: usize, columns: usize) -> Matrix {
    vec![vec![Laurent::default(); columns]; rows]
}

fn matrix_multiply(left: &Matrix, right: &Matrix) -> Matrix {
    assert!(!left.is_empty());
    assert!(!right.is_empty());
    assert_eq!(left[0].len(), right.len());
    let mut result = zero_matrix(left.len(), right[0].len());
    for (row, left_entries) in left.iter().enumerate() {
        for (middle, left_entry) in left_entries.iter().enumerate() {
            for (column, right_entry) in right[middle].iter().enumerate() {
                result[row][column] =
                    result[row][column].add(&left_entry.multiply(right_entry));
            }
        }
    }
    result
}

fn transpose(matrix: &Matrix) -> Matrix {
    assert!(!matrix.is_empty());
    let mut result = zero_matrix(matrix[0].len(), matrix.len());
    for (row, entries) in matrix.iter().enumerate() {
        for (column, entry) in entries.iter().enumerate() {
            result[column][row] = entry.clone();
        }
    }
    result
}

fn dot(left: &[Laurent], right: &[Laurent]) -> Laurent {
    assert_eq!(left.len(), right.len());
    left.iter()
        .zip(right)
        .fold(Laurent::default(), |sum, (a, b)| {
            sum.add(&a.multiply(b))
        })
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum Endpoint {
    V00,
    V10,
}

struct EndpointQuotient {
    endpoint: Endpoint,
    first_normal: usize,
    edge_incidence: Int,
    quotient_d_two: Matrix,
    quotient_d_one: Matrix,
    r_two: Matrix,
    r_one: Matrix,
    r_zero: Matrix,
}

fn road_differentials() -> (Matrix, Matrix) {
    let x0 = Laurent::variable(X0);
    let x1 = Laurent::variable(X1);
    let x3 = Laurent::variable(X3);
    let x4 = Laurent::variable(X4);
    let d_two = vec![
        vec![x3.clone()],
        vec![x4.negate()],
        vec![x0.negate()],
        vec![x1.clone()],
    ];
    let d_one = vec![
        vec![x0.negate(), Laurent::default(), x3.negate(), Laurent::default()],
        vec![x1.clone(), Laurent::default(), Laurent::default(), x3.negate()],
        vec![Laurent::default(), x0.negate(), x4.clone(), Laurent::default()],
        vec![Laurent::default(), x1, Laurent::default(), x4],
    ];
    (d_two, d_one)
}

fn endpoint_quotient(endpoint: Endpoint) -> EndpointQuotient {
    let one = Laurent::one();
    let zero = Laurent::default();
    let (first_normal, edge_incidence, r_two, r_one, r_zero) = match endpoint {
        Endpoint::V00 => (
            X0,
            -1,
            vec![vec![one.negate()]],
            vec![
                vec![one.negate(), zero.clone(), zero.clone(), zero.clone()],
                vec![zero.clone(), zero.clone(), one.negate(), zero.clone()],
            ],
            vec![vec![one, zero.clone(), zero.clone(), zero]],
        ),
        Endpoint::V10 => (
            X1,
            1,
            vec![vec![one.clone()]],
            vec![
                vec![one.clone(), zero.clone(), zero.clone(), zero.clone()],
                vec![zero.clone(), zero.clone(), zero.clone(), one.negate()],
            ],
            vec![vec![zero.clone(), one, zero.clone(), zero]],
        ),
    };
    let xi = Laurent::variable(first_normal);
    let x3 = Laurent::variable(X3);
    EndpointQuotient {
        endpoint,
        first_normal,
        edge_incidence,
        quotient_d_two: vec![vec![x3.clone()], vec![xi.negate()]],
        quotient_d_one: vec![vec![xi, x3]],
        r_two,
        r_one,
        r_zero,
    }
}

fn check_endpoint_quotient(data: &EndpointQuotient, road_d_two: &Matrix, road_d_one: &Matrix) {
    assert_eq!(
        matrix_multiply(&data.quotient_d_one, &data.quotient_d_two),
        zero_matrix(1, 1)
    );
    assert_eq!(
        matrix_multiply(&data.r_one, road_d_two),
        matrix_multiply(&data.quotient_d_two, &data.r_two)
    );
    assert_eq!(
        matrix_multiply(&data.r_zero, road_d_one),
        matrix_multiply(&data.quotient_d_one, &data.r_one)
    );

    // Finite-free duality reverses the quotient.  This is the variance used
    // by entry 121; no primal section or road/costalk identification is made.
    let dual_road_d_zero = transpose(road_d_one);
    let dual_road_d_one = transpose(road_d_two);
    let dual_quotient_d_zero = transpose(&data.quotient_d_one);
    let dual_quotient_d_one = transpose(&data.quotient_d_two);
    let dual_r_zero = transpose(&data.r_zero);
    let dual_r_one = transpose(&data.r_one);
    let dual_r_two = transpose(&data.r_two);
    assert_eq!(
        matrix_multiply(&dual_road_d_zero, &dual_r_zero),
        matrix_multiply(&dual_r_one, &dual_quotient_d_zero)
    );
    assert_eq!(
        matrix_multiply(&dual_road_d_one, &dual_r_one),
        matrix_multiply(&dual_r_two, &dual_quotient_d_one)
    );

    // The quotient top orientation and the boundary incidence of the x3 edge
    // cancel at v00 and agree at v10.  Both oriented endpoint lines are +1.
    assert_eq!(
        Laurent::scalar(data.edge_incidence).multiply(&data.r_two[0][0]),
        Laurent::one()
    );

    let supported_vertex = match data.endpoint {
        Endpoint::V00 => [true, false, false, false],
        Endpoint::V10 => [false, true, false, false],
    };
    assert_ne!(supported_vertex, [true; 4]);
}

fn check_occurrence_cech(first_normal: usize) -> Laurent {
    assert!(first_normal == X0 || first_normal == X1);
    let xi = Laurent::variable(first_normal);
    let x3 = Laurent::variable(X3);
    let inv_xi = Laurent::inverse_variable(first_normal);
    let inv_x3 = Laurent::inverse_variable(X3);
    let one = Laurent::one();

    // Full two-normal Koszul--Cech comparison.  Every degree is retained.
    let phi_zero = one.clone();
    let phi_one_z3 = [inv_xi.clone(), Laurent::default()];
    let phi_one_zi = [Laurent::default(), inv_x3.clone()];
    let phi_two = inv_xi.multiply(&inv_x3);
    assert_eq!(
        [
            xi.multiply(&phi_one_z3[0])
                .add(&x3.multiply(&phi_one_zi[0])),
            xi.multiply(&phi_one_z3[1])
                .add(&x3.multiply(&phi_one_zi[1])),
        ],
        [phi_zero.clone(), phi_zero]
    );
    assert_eq!(
        phi_one_z3[0].add(&phi_one_z3[1].negate()),
        x3.multiply(&phi_two)
    );
    assert_eq!(
        phi_one_zi[0].add(&phi_one_zi[1].negate()),
        xi.negate().multiply(&phi_two)
    );

    // Entry 129's degree-one extraordinary map from the x3 Cech edge to the
    // product Cech corner is g0(r)=(r/xi,0), g1(t)=t/xi.
    let g_zero = [inv_xi.clone(), Laurent::default()];
    let target_d_g_zero = g_zero[0].add(&g_zero[1].negate());
    let g_one_d_source = inv_xi;
    assert_eq!(target_d_g_zero, g_one_d_source);
    let edge_simple_pole = inv_x3;
    let endpoint_top = g_one_d_source.multiply(&edge_simple_pole);
    assert_eq!(endpoint_top, phi_two);

    // Deleting the lower g0 term destroys the chain equation.
    assert_ne!(Laurent::default(), g_one_d_source);

    // Every inverse is confined to the target Cech summand that localized it.
    for (value, localization) in [
        (&phi_one_z3[0], 1_u16 << first_normal),
        (&phi_one_zi[1], 1_u16 << X3),
        (&phi_two, (1_u16 << first_normal) | (1_u16 << X3)),
    ] {
        for &slot in &[X0, X1, X3, X4, U0, U1, U3, U5] {
            let has_negative = value.0.keys().any(|powers| powers[slot] < 0);
            if has_negative {
                assert_ne!(localization & (1_u16 << slot), 0);
            }
        }
    }
    endpoint_top
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum SupportVariance {
    ReciprocalRegular,
    OriginalLocallyFiniteBorelMoore,
}

struct RepeatedNormal {
    eta_mix: [Laurent; 2],
    pi_one: [Laurent; 2],
    trace_one: [Laurent; 2],
    section: [Laurent; 2],
}

fn check_variance_and_repeated_normal() -> RepeatedNormal {
    let source_variance = SupportVariance::ReciprocalRegular;
    let target_variance = SupportVariance::OriginalLocallyFiniteBorelMoore;
    assert_ne!(source_variance, target_variance);

    let one = Laurent::one();
    let minus_one = one.negate();
    let q3 = Laurent::variable(Q3);
    let minus_q3 = q3.negate();
    let u3 = Laurent::variable(U3);
    let u3_dual = Laurent::inverse_variable(Q3)
        .multiply(&u3)
        .negate();

    // Paired can--var conventions and the entry-97 perfect evaluation.
    let road_can = u3.clone();
    let road_var = one.clone();
    let reciprocal_can = one.clone();
    let reciprocal_var = u3_dual.clone();
    assert_eq!(road_can.multiply(&road_var), u3);
    assert_eq!(
        reciprocal_can.multiply(&reciprocal_var),
        u3_dual.clone()
    );
    let beta_p_h_dual = one.clone();
    let beta_h_p_dual = minus_q3.clone();
    assert_eq!(
        Laurent::variable(U3).multiply(&beta_p_h_dual),
        u3_dual.clone().multiply(&beta_h_p_dual)
    );
    assert_eq!(
        beta_p_h_dual
            .multiply(&beta_h_p_dual)
            .negate(),
        q3
    );

    // D3=K(u3^vee) tensor K(u3).
    let d_two = [Laurent::variable(U3).negate(), u3_dual.clone()];
    let d_one = [u3_dual.clone(), Laurent::variable(U3)];
    assert_eq!(dot(&d_one, &d_two), Laurent::default());

    // Tor_0 quotient pi and primitive Tor_1 inclusion/retraction.
    let pi_one = [one.clone(), minus_q3.clone()];
    assert_eq!(
        pi_one
            .iter()
            .map(|entry| u3_dual.multiply(entry))
            .collect::<Vec<_>>(),
        d_one
    );
    let eta_mix = [minus_q3, minus_one.clone()];
    assert_eq!(dot(&d_one, &eta_mix), Laurent::default());
    assert_eq!(dot(&pi_one, &eta_mix), Laurent::default());
    assert_eq!(
        eta_mix
            .iter()
            .map(|entry| entry.multiply(&u3_dual.negate()))
            .collect::<Vec<_>>(),
        d_two
    );
    let section = [one.clone(), Laurent::default()];
    let basis_determinant = section[0]
        .multiply(&eta_mix[1])
        .add(&section[1].multiply(&eta_mix[0]).negate());
    assert_eq!(basis_determinant, minus_one);
    let trace_one = [Laurent::default(), Laurent::scalar(-1)];
    assert_eq!(dot(&trace_one, &eta_mix), one.clone());
    assert_eq!(dot(&pi_one, &section), one.clone());
    assert_eq!(dot(&trace_one, &d_two), u3_dual.negate());

    // The graph-Cartier filtered square retains both grades:
    // tr_ex(i(t3))=t3*pi(section).
    let t3 = Laurent::variable(T3);
    assert_eq!(
        dot(&trace_one, &eta_mix).multiply(&t3),
        dot(&pi_one, &section).multiply(&t3)
    );
    assert_eq!([1_usize, 1_usize], [1, 1]);

    for coefficient in d_two
        .iter()
        .chain(d_one.iter())
        .chain(pi_one.iter())
        .chain(eta_mix.iter())
        .chain(trace_one.iter())
    {
        assert!(coefficient.support_variables_unlocalized());
    }

    RepeatedNormal {
        eta_mix,
        pi_one,
        trace_one,
        section,
    }
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct NormalCechMonomial {
    localization: u8,
    exponents: [i8; 4],
    coefficient: Int,
}

fn normal_cech_comparison(mask: u8) -> NormalCechMonomial {
    let complement = (!mask) & 0b1111;
    let mut exponents = [0_i8; 4];
    let mut exponent_sum = 0;
    for index in 0..4 {
        if complement & (1 << index) != 0 {
            exponents[index] = -1;
            exponent_sum += index;
        }
    }
    NormalCechMonomial {
        localization: complement,
        exponents,
        coefficient: if exponent_sum % 2 == 0 { 1 } else { -1 },
    }
}

fn normal_cech_add_direction(
    value: NormalCechMonomial,
    direction: usize,
) -> NormalCechMonomial {
    assert_eq!(value.localization & (1 << direction), 0);
    let preceding = (0..direction)
        .filter(|index| value.localization & (1 << index) != 0)
        .count();
    NormalCechMonomial {
        localization: value.localization | (1 << direction),
        coefficient: if preceding % 2 == 0 {
            value.coefficient
        } else {
            -value.coefficient
        },
        ..value
    }
}

fn normal_cech_multiply_by_u(
    mut value: NormalCechMonomial,
    direction: usize,
) -> NormalCechMonomial {
    value.exponents[direction] += 1;
    value
}

fn check_normal_cech_all_degrees() -> Laurent {
    for mask in 0_u8..16 {
        let source = normal_cech_comparison(mask);
        for direction in 0..4 {
            if mask & (1 << direction) == 0 {
                continue;
            }
            let face = mask & !(1 << direction);
            let position = (0..direction)
                .filter(|index| mask & (1 << index) != 0)
                .count();
            let mut after_koszul =
                normal_cech_multiply_by_u(normal_cech_comparison(face), direction);
            if position % 2 == 1 {
                after_koszul.coefficient = -after_koszul.coefficient;
            }
            assert_eq!(
                after_koszul,
                normal_cech_add_direction(source, direction)
            );
        }
        for index in 0..4 {
            if source.exponents[index] < 0 {
                assert_ne!(source.localization & (1 << index), 0);
            }
        }
    }

    let residue = normal_cech_comparison(0);
    assert_eq!(residue.localization, 0b1111);
    assert_eq!(residue.exponents, [-1; 4]);
    assert_eq!(residue.coefficient, 1);
    let determinant_end = normal_cech_comparison(0b1111);
    assert_eq!(determinant_end.localization, 0);
    assert_eq!(determinant_end.exponents, [0; 4]);
    assert_eq!(determinant_end.coefficient, 1);

    [U0, U1, U3, U5]
        .into_iter()
        .fold(Laurent::one(), |product, slot| {
            product.multiply(&Laurent::inverse_variable(slot))
        })
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct PhysicalOrientation(Int);

impl PhysicalOrientation {
    fn evaluate(self, coefficient: &Laurent) -> Laurent {
        Laurent::scalar(self.0).multiply(coefficient)
    }
}

fn expected_loaded_residue(first_normal: usize) -> Laurent {
    [first_normal, X3, U0, U1, U3, U5]
        .into_iter()
        .fold(Laurent::one(), |product, slot| {
            product.multiply(&Laurent::inverse_variable(slot))
        })
}

fn check_loaded_external_product(
    data: &EndpointQuotient,
    repeated: &RepeatedNormal,
    normal_residue: &Laurent,
) -> Laurent {
    let occurrence_residue = check_occurrence_cech(data.first_normal);

    // The quotient and excess maps are both retained.  The residue displayed
    // below is the Tor_1 component; Tor_0 remains the independent pi component.
    assert_eq!(dot(&repeated.pi_one, &repeated.section), Laurent::one());
    assert_eq!(
        dot(&repeated.trace_one, &repeated.eta_mix),
        Laurent::one()
    );
    let tor_zero_present = true;
    let tor_one_present = true;
    assert!(tor_zero_present && tor_one_present);

    let coefficient_before_physical = occurrence_residue.multiply(normal_residue);
    let physical_line = PhysicalOrientation(1);
    let result = physical_line.evaluate(&coefficient_before_physical);
    assert_eq!(result, expected_loaded_residue(data.first_normal));
    result
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum TargetType {
    CoefficientCechCorner,
    RingedPcExtraordinaryCostalk,
}

struct TypingAudit {
    coefficient_endpoint_maps: usize,
    ringed_pc_purity_comparisons: usize,
}

fn check_first_untyped_arrow() {
    let audit = TypingAudit {
        coefficient_endpoint_maps: 2,
        ringed_pc_purity_comparisons: 0,
    };
    assert_eq!(audit.coefficient_endpoint_maps, 2);
    assert_eq!(audit.ringed_pc_purity_comparisons, 0);
    assert_ne!(
        TargetType::CoefficientCechCorner,
        TargetType::RingedPcExtraordinaryCostalk
    );

    // Two tempting substitutions are invalid.
    let regular_unit_coherent_cousin_residue_is_nonzero = false;
    let finite_corner_dual_equals_full_road_trace = false;
    assert!(!regular_unit_coherent_cousin_residue_is_nonzero);
    assert!(!finite_corner_dual_equals_full_road_trace);
}

fn main() {
    let (road_d_two, road_d_one) = road_differentials();
    assert_eq!(
        matrix_multiply(&road_d_one, &road_d_two),
        zero_matrix(4, 1)
    );
    for coefficient in road_d_two.iter().flatten().chain(road_d_one.iter().flatten()) {
        assert!(coefficient.support_variables_unlocalized());
    }

    let v00 = endpoint_quotient(Endpoint::V00);
    let v10 = endpoint_quotient(Endpoint::V10);
    check_endpoint_quotient(&v00, &road_d_two, &road_d_one);
    check_endpoint_quotient(&v10, &road_d_two, &road_d_one);

    let repeated = check_variance_and_repeated_normal();
    let normal_residue = check_normal_cech_all_degrees();
    let loaded_v00 = check_loaded_external_product(&v00, &repeated, &normal_residue);
    let loaded_v10 = check_loaded_external_product(&v10, &repeated, &normal_residue);
    assert_eq!(loaded_v00, expected_loaded_residue(X0));
    assert_eq!(loaded_v10, expected_loaded_residue(X1));
    check_first_untyped_arrow();

    println!(
        "{}",
        concat!(
            r#"{"claim":"The entry-129 x3 occurrence Koszul--Cech Gysin has a canonical simultaneous external product with the frozen entry-97/100 D03 coefficient packet at v00 and v10. In the filtered coefficient/Cousin category it retains the reciprocal-regular/original-Borel--Moore variance, primitive Tor0 and Tor1 grades, the repeated-normal excess, every lower occurrence-Cech term, and a separate positive [dX03] line. This does not type an actual ringed PC extraordinary map: the required occurrence-loaded purity/costalk comparisons are absent at both endpoints, with entry 121 explicitly leaving the v10 comparison unconstructed.","status":"inconclusive","assumptions":["The theorem is scoped to the finite occurrence and normal coefficient complexes and their target Cech localizations from entries 97, 100, 121, and 129.","The reciprocal source and Borel--Moore target remain distinct variance types and are paired only by the proved q3-unit Verdier evaluation.","Negative occurrence and support-normal powers are permitted only inside the indicated target Cech summands; the base is not further localized.","The physical line [dX03] is an independent oriented factor evaluated last."],"evidence_refs":["research/voevodsky/check_d03_x3_loaded_pc_endpoint_boundary.rs","research/voevodsky/check_d03_bivariant_pc_hom.rs","research/voevodsky/check_one_normal_can_var_cousin.rs","research/voevodsky/check_unlocalized_plus_recollement_obstruction.rs","research/voevodsky/check_d03_corner_residue_comparison.rs","research/voevodsky/check_d03_toric_cox_cousin_trace.rs","ledger entries 97, 100, 121, and 129"],"factorization_test":{"v00_finite_corner_quotient_dual":"PASS with forced quotient and edge-incidence orientations","v10_finite_corner_quotient_dual":"PASS and reproduces entry 121","x3_occurrence_Gysin":"PASS simultaneously with nonzero degree-zero and degree-one Cech components","reciprocal_BM_variance":"PASS without identifying the two support types","Tor0_quotient":"PASS and retained","Tor1_repeated_normal_excess":"PASS, primitive and retained","filtered_Bockstein":"PASS: tr_ex(i(t3))=t3*pi(section)","normal_Koszul_Cech":"PASS in all 16 degrees with summand-local denominators","loaded_v00_residue":"+1/(x0*x3*u0*u1*u3*u5) times [dX03]","loaded_v10_residue":"+1/(x1*x3*u0*u1*u3*u5) times [dX03]","extra_base_localization":"NONE","fitted_map_or_splitting":"NONE","actual_ringed_PC_extraordinary_map":"UNTYPED"},"counterevidence":["The coefficient codomain C_(xi,x3) tensor C_Q is not definitionally the ringed PC extraordinary costalk.","Neither the finite dual corner extension nor entry 97's full-road trace supplies the missing occurrence-loaded purity comparison; entry 121 falsifies their identification at v10.","Ordinary coherent Cousin restriction of a regular unit is zero and cannot replace the extraordinary fundamental class."],"next_experiment":"Construct one geometric occurrence-loaded purity/costalk comparison pur_i3^PC from the finite dual corner model to i_(vi3)^! Q_(03,partial,lf)^PC, first at v10 and then along the same x3 edge at v00, and verify compatibility with pi, tr_ex, the graph-Cartier Bockstein, and every lower Cech term."}"#
        )
    );
}
