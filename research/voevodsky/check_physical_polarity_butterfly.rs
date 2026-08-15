// Exact audit of the physical-polarity loading of the K6 butterfly torsor.
//
// This checker deliberately proves only a character/group-cohomology theorem.
// It does not construct the loaded support-PC comparison whose obstruction
// would live in the calculated H^2 group.

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct Dihedral6 {
    // Affine action j |-> shift + (-1)^reflected j on Z/6.
    shift: i32,
    reflected: bool,
}

impl Dihedral6 {
    fn new(shift: i32, reflected: bool) -> Self {
        Self {
            shift: shift.rem_euclid(6),
            reflected,
        }
    }

    fn identity() -> Self {
        Self::new(0, false)
    }

    fn compose(self, other: Self) -> Self {
        let signed_other_shift = if self.reflected {
            -other.shift
        } else {
            other.shift
        };
        Self::new(
            self.shift + signed_other_shift,
            self.reflected ^ other.reflected,
        )
    }

    fn pow(self, exponent: usize) -> Self {
        let mut answer = Self::identity();
        for _ in 0..exponent {
            answer = answer.compose(self);
        }
        answer
    }

    fn act(self, label: i32) -> i32 {
        let signed_label = if self.reflected { -label } else { label };
        (self.shift + signed_label).rem_euclid(6)
    }
}

type Matrix = Vec<Vec<i64>>;

fn canonical_pair(left: i32, right: i32) -> (i32, i32) {
    let left = left.rem_euclid(6);
    let right = right.rem_euclid(6);
    if left < right {
        (left, right)
    } else {
        (right, left)
    }
}

fn act_pair(action: Dihedral6, pair: (i32, i32)) -> (i32, i32) {
    canonical_pair(action.act(pair.0), action.act(pair.1))
}

fn physical_triad_group() -> Vec<Dihedral6> {
    let rho = Dihedral6::new(1, false);
    let sigma_0 = Dihedral6::new(0, true);
    let rotation = rho.pow(2);
    let reflection = rho.pow(3).compose(sigma_0);
    let rotation_squared = rotation.pow(2);
    vec![
        Dihedral6::identity(),
        rotation,
        rotation_squared,
        reflection,
        rotation.compose(reflection),
        rotation_squared.compose(reflection),
    ]
}

fn group_index(group: &[Dihedral6], element: Dihedral6) -> usize {
    group
        .iter()
        .position(|candidate| *candidate == element)
        .expect("physical D3 subgroup must be closed")
}

fn road_orientation_character(element: Dihedral6) -> i64 {
    if element.reflected {
        -1
    } else {
        1
    }
}

fn polarity_character(element: Dihedral6) -> i64 {
    // Entry 93 proves that one six-label rotation exchanges the two sheets.
    if element.shift.rem_euclid(2) == 0 {
        1
    } else {
        -1
    }
}

fn loaded_character(element: Dihedral6) -> i64 {
    road_orientation_character(element) * polarity_character(element)
}

fn reflection_parity(element: Dihedral6) -> i64 {
    i64::from(element.reflected)
}

fn loaded_h2_generator(left: Dihedral6, right: Dihedral6) -> i64 {
    let numerator =
        reflection_parity(left) + reflection_parity(right) - reflection_parity(left.compose(right));
    assert_eq!(numerator.rem_euclid(2), 0);
    numerator / 2
}

fn short_diagonal(index: i32) -> (i32, i32) {
    canonical_pair(index, index + 2)
}

fn check_reflection_detector(group: &[Dihedral6], reflection: Dihedral6) {
    // The connecting cocycle for the quotient character
    // D3 -> C2 -> Q/Z is an integral representative of the loaded H2
    // generator.  It is normalized and restricts to the standard C2
    // generator with c(s,s)=1.
    for first in group {
        assert_eq!(loaded_h2_generator(Dihedral6::identity(), *first), 0);
        assert_eq!(loaded_h2_generator(*first, Dihedral6::identity()), 0);
        for second in group {
            for third in group {
                let cocycle_identity = loaded_h2_generator(*second, *third)
                    - loaded_h2_generator(first.compose(*second), *third)
                    + loaded_h2_generator(*first, second.compose(*third))
                    - loaded_h2_generator(*first, *second);
                assert_eq!(cocycle_identity, 0);
            }
        }
    }
    assert_eq!(loaded_h2_generator(reflection, reflection), 1);

    // A normalized integral one-cochain b on <s> changes c(s,s) by
    // 2*b(s).  Its parity is therefore independent of representative.
    for value in -8_i64..=8 {
        let coboundary_at_ss = 2 * value;
        assert_eq!(coboundary_at_ss.rem_euclid(2), 0);
        assert_ne!(coboundary_at_ss, 1);
    }

    // Both loaded H2 groups have order two: for D3 this was computed by
    // LHS below, and for the reflection C2 it is the standard cyclic
    // resolution.  A nonzero restriction between them is therefore an
    // isomorphism.  Twice the displayed C2 cocycle is the coboundary of
    // b(s)=1, making its exact order visible without rational splitting.
    assert_eq!(2 * loaded_h2_generator(reflection, reflection), 2);
}

fn tuple_digits(mut value: usize, length: usize) -> Vec<usize> {
    let mut answer = vec![0; length];
    for position in (0..length).rev() {
        answer[position] = value % 5;
        value /= 5;
    }
    answer
}

fn tuple_index(tuple: &[usize]) -> usize {
    tuple.iter().fold(0, |answer, digit| answer * 5 + digit)
}

fn normalized_bar_differential(
    group: &[Dihedral6],
    degree: usize,
    character: fn(Dihedral6) -> i64,
) -> Matrix {
    let nonidentity = &group[1..];
    let source_rank = 5_usize.pow(degree as u32);
    let target_rank = 5_usize.pow((degree + 1) as u32);
    let mut differential = vec![vec![0; source_rank]; target_rank];

    for (row, target_digits) in (0..target_rank)
        .map(|index| tuple_digits(index, degree + 1))
        .enumerate()
    {
        let target: Vec<_> = target_digits
            .iter()
            .map(|digit| nonidentity[*digit])
            .collect();

        let mut add_term = |tuple: Vec<Dihedral6>, coefficient: i64| {
            if tuple.iter().any(|element| *element == group[0]) {
                return;
            }
            let digits: Vec<_> = tuple
                .iter()
                .map(|element| group_index(group, *element) - 1)
                .collect();
            differential[row][tuple_index(&digits)] += coefficient;
        };

        add_term(target[1..].to_vec(), character(target[0]));
        for index in 0..degree {
            let mut collapsed = target[..index].to_vec();
            collapsed.push(target[index].compose(target[index + 1]));
            collapsed.extend_from_slice(&target[(index + 2)..]);
            let coefficient = if index % 2 == 0 { -1 } else { 1 };
            add_term(collapsed, coefficient);
        }
        let last_coefficient = if (degree + 1) % 2 == 0 { 1 } else { -1 };
        add_term(target[..degree].to_vec(), last_coefficient);
    }
    differential
}

fn multiply(left: &Matrix, right: &Matrix) -> Matrix {
    assert_eq!(left[0].len(), right.len());
    let mut product = vec![vec![0; right[0].len()]; left.len()];
    for (row, product_row) in product.iter_mut().enumerate() {
        for middle in 0..right.len() {
            for (column, entry) in product_row.iter_mut().enumerate() {
                *entry += left[row][middle] * right[middle][column];
            }
        }
    }
    product
}

fn assert_zero(matrix: &Matrix) {
    assert!(matrix.iter().flatten().all(|entry| *entry == 0));
}

fn modulo(value: i64, prime: i64) -> i64 {
    value.rem_euclid(prime)
}

fn modular_power(mut base: i64, mut exponent: i64, prime: i64) -> i64 {
    let mut answer = 1;
    while exponent > 0 {
        if exponent % 2 == 1 {
            answer = modulo(answer * base, prime);
        }
        base = modulo(base * base, prime);
        exponent /= 2;
    }
    answer
}

fn rank_modulo(matrix: &Matrix, prime: i64) -> usize {
    let mut value: Matrix = matrix
        .iter()
        .map(|row| row.iter().map(|entry| modulo(*entry, prime)).collect())
        .collect();
    let row_count = value.len();
    let column_count = value.first().map_or(0, Vec::len);
    let mut pivot_row = 0;
    for column in 0..column_count {
        let Some(candidate) = (pivot_row..row_count).find(|row| value[*row][column] != 0) else {
            continue;
        };
        value.swap(pivot_row, candidate);
        let inverse = modular_power(value[pivot_row][column], prime - 2, prime);
        for entry in &mut value[pivot_row][column..] {
            *entry = modulo(*entry * inverse, prime);
        }
        for row in 0..row_count {
            if row == pivot_row || value[row][column] == 0 {
                continue;
            }
            let factor = value[row][column];
            for current_column in column..column_count {
                value[row][current_column] = modulo(
                    value[row][current_column] - factor * value[pivot_row][current_column],
                    prime,
                );
            }
        }
        pivot_row += 1;
        if pivot_row == row_count {
            break;
        }
    }
    pivot_row
}

fn cohomology_dimensions_modulo(differentials: &[Matrix], prime: i64) -> [usize; 3] {
    let ranks: Vec<_> = differentials
        .iter()
        .map(|differential| rank_modulo(differential, prime))
        .collect();
    [
        1 - ranks[0],
        5 - ranks[0] - ranks[1],
        25 - ranks[1] - ranks[2],
    ]
}

fn low_integral_cohomology_orders(reflection_action: i64) -> (usize, usize) {
    assert!(reflection_action == 1 || reflection_action == -1);

    // Lyndon-Hochschild-Serre for 1 -> C3 -> D3 -> C2 -> 1.
    // Rotation acts trivially on both coefficient lines.  For C2, the
    // standard (s-1,N) resolution gives H1=Z/2 only for the sign line and
    // H2=Z/2 only for the trivial line.  H2(C3,Z)=Z/3, and inversion acts on
    // it by -1, so the quotient reflection acts there by -reflection_action.
    // Positive C2 cohomology of a 3-primary module vanishes; the spectral
    // sequence therefore has no differential or extension ambiguity in
    // total degree <= 2.
    let h1_c2_order = if reflection_action == -1 { 2 } else { 1 };
    let h2_c2_order = if reflection_action == 1 { 2 } else { 1 };
    let h2_c3_invariant_order = if -reflection_action == 1 { 3 } else { 1 };
    (h1_c2_order, h2_c2_order * h2_c3_invariant_order)
}

fn main() {
    let group = physical_triad_group();
    assert_eq!(group.len(), 6);
    for left in &group {
        for right in &group {
            group_index(&group, left.compose(*right));
        }
    }

    let rho = Dihedral6::new(1, false);
    let sigma_0 = Dihedral6::new(0, true);
    let rotation = rho.pow(2);
    let reflection = rho.pow(3).compose(sigma_0);
    assert_eq!(rotation.pow(3), Dihedral6::identity());
    assert_eq!(reflection.pow(2), Dihedral6::identity());
    assert_eq!(
        reflection.compose(rotation).compose(reflection),
        rotation.pow(2)
    );

    let roads = [(1, 4), (0, 3), (2, 5)];
    assert_eq!(act_pair(rotation, roads[0]), roads[1]);
    assert_eq!(act_pair(rotation, roads[1]), roads[2]);
    assert_eq!(act_pair(rotation, roads[2]), roads[0]);
    assert_eq!(act_pair(reflection, roads[0]), roads[2]);
    assert_eq!(act_pair(reflection, roads[1]), roads[1]);
    assert_eq!(act_pair(reflection, roads[2]), roads[0]);

    assert_eq!(road_orientation_character(rotation), 1);
    assert_eq!(road_orientation_character(reflection), -1);
    assert_eq!(polarity_character(rotation), 1);
    assert_eq!(polarity_character(reflection), -1);
    assert!(group.iter().all(|element| loaded_character(*element) == 1));

    check_reflection_detector(&group, reflection);
    assert_eq!(act_pair(reflection, short_diagonal(0)), short_diagonal(1));
    assert_eq!(act_pair(reflection, short_diagonal(1)), short_diagonal(0));
    assert_eq!(act_pair(reflection, short_diagonal(3)), short_diagonal(4));
    assert_eq!(act_pair(reflection, short_diagonal(4)), short_diagonal(3));

    let carrier_differentials: Vec<_> = (0..=2)
        .map(|degree| normalized_bar_differential(&group, degree, road_orientation_character))
        .collect();
    let loaded_differentials: Vec<_> = (0..=2)
        .map(|degree| normalized_bar_differential(&group, degree, loaded_character))
        .collect();
    assert_zero(&multiply(
        &carrier_differentials[1],
        &carrier_differentials[0],
    ));
    assert_zero(&multiply(
        &carrier_differentials[2],
        &carrier_differentials[1],
    ));
    assert_zero(&multiply(
        &loaded_differentials[1],
        &loaded_differentials[0],
    ));
    assert_zero(&multiply(
        &loaded_differentials[2],
        &loaded_differentials[1],
    ));

    let carrier_orders = low_integral_cohomology_orders(-1);
    let loaded_orders = low_integral_cohomology_orders(1);
    assert_eq!(carrier_orders, (2, 3));
    assert_eq!(loaded_orders, (1, 2));

    // Independent normalized-bar checks.  The large prime ranks are the
    // characteristic-zero ranks.  The F2/F3 dimensions detect exactly the
    // primary torsion predicted by the integral LHS calculation.
    let carrier_ranks_q: Vec<_> = carrier_differentials
        .iter()
        .map(|matrix| rank_modulo(matrix, 1009))
        .collect();
    let loaded_ranks_q: Vec<_> = loaded_differentials
        .iter()
        .map(|matrix| rank_modulo(matrix, 1009))
        .collect();
    assert_eq!(carrier_ranks_q, [1, 4, 21]);
    assert_eq!(loaded_ranks_q, [0, 5, 20]);
    assert_eq!(
        cohomology_dimensions_modulo(&carrier_differentials, 2),
        [1, 1, 1]
    );
    assert_eq!(
        cohomology_dimensions_modulo(&carrier_differentials, 3),
        [0, 1, 1]
    );
    assert_eq!(
        cohomology_dimensions_modulo(&loaded_differentials, 2),
        [1, 1, 1]
    );
    assert_eq!(
        cohomology_dimensions_modulo(&loaded_differentials, 3),
        [1, 0, 0]
    );

    println!(
        "{}",
        r#"{"claim":"On the D3 transport symmetry of the three physical long channels, generated in the six-label dihedral action by r=rho^2 and s=rho^3*sigma_0, the road-orientation line and the independently established polarity line are both reflection-sign modules. Their product chi_N is the trivial D3 module. Therefore, if the endpoint-fixed butterfly mapping fiber is loaded by this relative polarity line exactly once, its low integral obstruction theory changes from H1(D3,Z_or)=Z/2 and H2(D3,Z_or)=Z/3 to H1(D3,Z_chiN)=0 and H2(D3,Z_chiN)=Z/2. The loaded H2 class is detected isomorphically on the physical reflection subgroup <f3>: for a normalized cocycle omega, its class is omega(f3,f3) mod 2. Loading before pointing eliminates the carrier parity choice, but existence becomes a new binary obstruction test; existence is not proved.","status":"proved","status_meaning":"The character identity, exact low-degree group cohomology, and reflection-subgroup detection theorem are proved. The actual loaded support-PC butterfly and its H2 obstruction cocycle remain unconstructed.","assumptions":["D3 is the transport symmetry of the ordered long-channel triad (F14,F03,F25), not the literal stabilizer of the single channel D03.","The relative mapping coefficient is loaded once by L_pol, so Z_or becomes Z_or tensor L_pol=Z_chiN. If the same invertible polarity line is placed on both mapping endpoints, it cancels in internal Hom and this theorem does not change the carrier torsor.","The six-label rotation exchanges normalization sheets as proved in entry 93, while entries 92 and 94 retain the road-orientation, polarity, and physical-normal lines independently.","No coefficient map from the sign module to the trivial module is asserted; the known zero carrier obstruction in Z/3 does not determine the new loaded Z/2 obstruction."],"evidence_refs":["research/voevodsky/check_physical_polarity_butterfly.rs","src/ledger/20260814-92 Character Match and the Vanishing Star-Costalk Map.md","src/ledger/20260814-93 Alternating Fusion Normalization-Conductor Square.md","src/ledger/20260814-94 Augmented Triangle Resolution and the D03 Primitive Cousin Symbol.md","src/ledger/20260814-120 Unlocalized Road-Flag Diamond and the Filtered LCM-Cartier Trace.md","src/ledger/20260814-131 D03 Cartier Edge Purity and the Scoped PC Promotion.md","src/ledger/20260814-134 Framed Lift-Space Theorem and the Relative AW Reference-Lift Gap.md","src/ledger/20260814-136 Canonical AW-Cap Roof and the Endpoint-Connector Gap.md"],"exact_test":{"physical_generators":"r=rho^2 cycles F14->F03->F25; s=rho^3*sigma_0 fixes F03 and exchanges F14,F25","characters":{"road_orientation":"r:+1,s:-1","polarity":"r:+1,s:-1","loaded_product":"r:+1,s:+1"},"normalized_bar_ranks":{"cochain_ranks":[1,5,25,125],"carrier_characteristic_zero_differential_ranks":[1,4,21],"loaded_characteristic_zero_differential_ranks":[0,5,20],"carrier_mod2_H012_dimensions":[1,1,1],"carrier_mod3_H012_dimensions":[0,1,1],"loaded_mod2_H012_dimensions":[1,1,1],"loaded_mod3_H012_dimensions":[1,0,0]},"integral_LHS":{"extension":"1 -> C3 -> D3 -> C2 -> 1","carrier_H1":"Z/2","carrier_H2":"Z/3","loaded_H1":"0","loaded_H2":"Z/2","numeric_denominator_used":false},"reflection_detector":{"subgroup":"<f3>=<s>","restriction":"H2(D3,Z)->H2(<f3>,Z) is an isomorphism Z/2->Z/2","generator":"c(g,h)=(eps(g)+eps(h)-eps(gh))/2","generator_value":"c(f3,f3)=1","coboundary_invariance":"delta b(f3,f3)=2 b(f3), so parity is representative-independent","decision_rule":"omega_load=0 iff omega_load(f3,f3) is even","short_edge_action":"f3 exchanges x3<->x4 and x0<->x1"}},"sharp_blocker":{"first_missing_datum":"an endpoint-coherent loaded reflection connector pairing the x3 and x4 D03 edge-costalk diagrams inside one support-PC two-extension mapping category; its reflection-square defect must define omega_load(f3,f3)","required_test":"construct the two loaded endpoint extensions globally enough that restriction is defined, then compute the single f3-square parity. If it is even, the global loaded path component is unique because H1=0; if it is odd, the proposed physical loading is obstructed.","why_current_entries_do_not_decide_it":"entries 120 and 131 close the finite x3 road-flag trace and target edge purity, but they do not construct the support/Yoneda-to-Tate endpoint connector. Moreover f3 sends the displayed x3 edge to the opposite x4 edge. Rotating or reflecting the proved local unit without constructing this paired connector would assume the equivariance whose square is being tested."},"counterevidence":["The actual stabilizer of D03 sees only the product character; entry 93 must retain the polarity factor independently before the restriction theorem applies.","The vanishing carrier obstruction lies in a different coefficient group Z/3 and cannot be transported to the loaded Z/2 group without a coefficient-level comparison that does not exist.","The x3 purity arrow is a local target-costalk equivalence, not a path between the two loaded global two-extensions.","H1=0 gives uniqueness only after existence; it is not evidence that omega_load vanishes.","No scalar differential, endpoint connector, PC comparison, or rational splitting is inserted by this checker."],"next_experiment":"Construct the f3-paired x3/x4 endpoint connector over the canonical loaded roof, retain both Tor grades and lower Cousin terms, and compute only its reflection-square parity omega_load(f3,f3). Full D3 cocycle enumeration is unnecessary once this connector is typed."}"#
    );
}
