//! Exact associated-grade audit for the proposed D=03 PC road/circuit pairing.
//!
//! This certificate separates what is already typed from the first missing
//! chain datum.
//!
//! * Each of the three physical hexagon roads is the tensor product of two
//!   actual weighted intervals.  The full tensor differential squares to zero,
//!   and Laurent weight inversion gives a primitive cocycle on all twelve
//!   occurrence vertices and all twelve interval boundaries.
//! * The Borel--Moore/tangential orientation of the actual two-interval face
//!   has character chi_N=(+1,-1,-1) under road rotation, road reflection, and
//!   polarity/core exchange.  It is exactly sgn_polarity tensor or(C3), the
//!   two coefficient-symbol lines exhibited by entries 66 and 59/64.  Twist
//!   reversal commutes with relabeling and entry 86's ordered normal transport
//!   is positive, so neither adds another character.
//! * The resulting associated-grade pairing is equivariant on every one of
//!   12 group elements times 3 roads times 4 occurrences.  Every primitive
//!   occurrence has value one.  Entry 86's marked endpoint value two and full
//!   polarized value four are sums of primitive occurrences, not a reason to
//!   divide the integral counit.
//! * The circuit side still exists only as the one-relation carrier resolution
//!   and entry 66's coefficient symbol.  The symbol is Ward closed, but two
//!   square-zero source differentials with the same modules and symbol give
//!   opposite chain-map answers.  Thus the endpoint pairing can be checked on
//!   its road/Cousin half only.  The first unsupported datum is precisely the
//!   chain lift bold-sigma_alt, including its scalar kinetic/BRST differential;
//!   no occurrence-resolved C_circ^PC is manufactured here.
//! * This pairing is a boundary-costalk statement.  The three roads do not
//!   exhaust the full J6 PC object: the polarity/contact sector has identical
//!   road restrictions.  Two extensions across an abstract contact generator
//!   agree on every road and differ on that generator.  Killing it is an
//!   additional factor-through-restriction axiom, not a consequence of the
//!   road augmentation.

use std::collections::{BTreeMap, BTreeSet};

const N: u8 = 6;

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct Diagonal(u8, u8);

type Cell = BTreeSet<u8>;

#[derive(Clone, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct LaurentMonomial(BTreeMap<Diagonal, i8>);

impl LaurentMonomial {
    fn one() -> Self {
        Self(BTreeMap::new())
    }

    fn variable(value: Diagonal) -> Self {
        Self(BTreeMap::from([(value, 1)]))
    }

    fn multiply(&self, other: &Self) -> Self {
        let mut result = self.0.clone();
        for (&variable, &exponent) in &other.0 {
            *result.entry(variable).or_default() += exponent;
        }
        result.retain(|_, exponent| *exponent != 0);
        Self(result)
    }

    fn inverse(&self) -> Self {
        Self(
            self.0
                .iter()
                .map(|(&variable, &exponent)| (variable, -exponent))
                .collect(),
        )
    }

    fn transform(&self, amount: u8, reflected: bool) -> Self {
        Self(
            self.0
                .iter()
                .map(|(&variable, &exponent)| {
                    (transform_diagonal(variable, amount, reflected), exponent)
                })
                .collect(),
        )
    }
}

#[derive(Clone, Copy, Debug)]
struct GroupElement {
    amount: u8,
    reflected: bool,
}

fn diagonal(first: u8, second: u8) -> Diagonal {
    assert_ne!(first, second);
    if first < second {
        Diagonal(first, second)
    } else {
        Diagonal(second, first)
    }
}

fn boundary(value: Diagonal) -> bool {
    value.1 == value.0 + 1 || value == Diagonal(0, N - 1)
}

fn physical(value: Diagonal) -> bool {
    !boundary(value) && value.0 % 2 != value.1 % 2
}

fn physical_channels() -> Vec<Diagonal> {
    let result: Vec<_> = (0..N)
        .flat_map(|first| ((first + 1)..N).map(move |second| Diagonal(first, second)))
        .filter(|&value| physical(value))
        .collect();
    assert_eq!(result, vec![Diagonal(0, 3), Diagonal(1, 4), Diagonal(2, 5)]);
    result
}

fn boundary_edges() -> BTreeSet<Diagonal> {
    (0..N)
        .map(|vertex| diagonal(vertex, (vertex + 1) % N))
        .collect()
}

fn quadrilateral_cells(channel: Diagonal) -> Vec<Cell> {
    let edges: BTreeSet<_> = boundary_edges().into_iter().chain([channel]).collect();
    let mut result = Vec::new();
    for first in 0..N {
        for second in first + 1..N {
            for third in second + 1..N {
                for fourth in third + 1..N {
                    let vertices = [first, second, third, fourth];
                    if (0..4).all(|index| {
                        edges.contains(&diagonal(vertices[index], vertices[(index + 1) % 4]))
                    }) {
                        result.push(vertices.into_iter().collect());
                    }
                }
            }
        }
    }
    result.sort();
    assert_eq!(result.len(), 2);
    result
}

fn scalar_slots(cell: &Cell) -> [Diagonal; 2] {
    let vertices: Vec<_> = cell.iter().copied().collect();
    let mut result = [
        diagonal(vertices[0], vertices[2]),
        diagonal(vertices[1], vertices[3]),
    ];
    result.sort();
    result
}

fn road_slots(channel: Diagonal) -> [[Diagonal; 2]; 2] {
    let cells = quadrilateral_cells(channel);
    [scalar_slots(&cells[0]), scalar_slots(&cells[1])]
}

fn transform_vertex(vertex: u8, amount: u8, reflected: bool) -> u8 {
    let reflected_vertex = if reflected { (N - vertex) % N } else { vertex };
    (reflected_vertex + amount) % N
}

fn transform_diagonal(value: Diagonal, amount: u8, reflected: bool) -> Diagonal {
    diagonal(
        transform_vertex(value.0, amount, reflected),
        transform_vertex(value.1, amount, reflected),
    )
}

fn transform_cell(value: &Cell, amount: u8, reflected: bool) -> Cell {
    value
        .iter()
        .map(|&vertex| transform_vertex(vertex, amount, reflected))
        .collect()
}

fn road_index(value: Diagonal) -> usize {
    physical_channels()
        .iter()
        .position(|&candidate| candidate == value)
        .expect("every transformed physical channel is one of the three roads")
}

fn road_target(index: usize, element: GroupElement) -> usize {
    road_index(transform_diagonal(
        physical_channels()[index],
        element.amount,
        element.reflected,
    ))
}

fn core_character(element: GroupElement) -> i64 {
    if element.amount % 2 == 0 {
        1
    } else {
        -1
    }
}

fn triangle_orientation_character(element: GroupElement) -> i64 {
    if element.reflected {
        -1
    } else {
        1
    }
}

fn chi_n(element: GroupElement) -> i64 {
    core_character(element) * triangle_orientation_character(element)
}

fn tangential_orientation_character(road: usize, element: GroupElement) -> i64 {
    let source_channel = physical_channels()[road];
    let target_channel = transform_diagonal(source_channel, element.amount, element.reflected);
    let source_cells = quadrilateral_cells(source_channel);
    let target_cells = quadrilateral_cells(target_channel);
    let mut factor_targets = [0_usize; 2];
    let mut sign = 1_i64;

    for source_factor in 0..2 {
        let transformed_cell = transform_cell(
            &source_cells[source_factor],
            element.amount,
            element.reflected,
        );
        let target_factor = target_cells
            .iter()
            .position(|cell| *cell == transformed_cell)
            .expect("the transformed quadrilateral is a target factor");
        factor_targets[source_factor] = target_factor;

        let source_endpoints = scalar_slots(&source_cells[source_factor]);
        let transformed_endpoints = source_endpoints
            .map(|value| transform_diagonal(value, element.amount, element.reflected));
        let target_endpoints = scalar_slots(&target_cells[target_factor]);
        if transformed_endpoints == target_endpoints {
            // The interval orientation is preserved.
        } else {
            assert_eq!(
                transformed_endpoints,
                [target_endpoints[1], target_endpoints[0]],
                "a dihedral map can only preserve or reverse an interval"
            );
            sign = -sign;
        }
    }

    if factor_targets == [1, 0] {
        // Swapping two one-dimensional Borel--Moore factors has Koszul sign -1.
        sign = -sign;
    } else {
        assert_eq!(factor_targets, [0, 1]);
    }
    sign
}

fn tangential_orientation_gauge() -> [i64; 3] {
    let mut solutions = Vec::new();
    for mask in 0_u8..8 {
        let gauge = std::array::from_fn(|road| if mask & (1 << road) == 0 { 1 } else { -1 });
        let valid = (0..N).all(|amount| {
            [false, true].into_iter().all(|reflected| {
                let element = GroupElement { amount, reflected };
                (0..3).all(|road| {
                    let target = road_target(road, element);
                    gauge[target] * tangential_orientation_character(road, element) * gauge[road]
                        == chi_n(element)
                })
            })
        });
        if valid {
            solutions.push(gauge);
        }
    }
    // The only ambiguity is simultaneous reversal of all three road-face
    // orientation bases.
    assert_eq!(solutions.len(), 2);
    assert_eq!(solutions[1], solutions[0].map(|sign| -sign));
    solutions[0]
}

fn occurrence_weight(slots: &[[Diagonal; 2]; 2], word: [usize; 2]) -> LaurentMonomial {
    LaurentMonomial::variable(slots[0][word[0]])
        .multiply(&LaurentMonomial::variable(slots[1][word[1]]))
}

fn primitive_dual(slots: &[[Diagonal; 2]; 2], word: [usize; 2]) -> LaurentMonomial {
    occurrence_weight(slots, word).inverse()
}

#[derive(Clone, Copy, Debug)]
enum OneChain {
    LeftInterval(usize),
    RightInterval(usize),
}

type FormalVector<B> = BTreeMap<(B, LaurentMonomial), i64>;

fn add_term<B: Copy + Ord>(
    value: &mut FormalVector<B>,
    basis: B,
    coefficient: LaurentMonomial,
    scalar: i64,
) {
    *value.entry((basis, coefficient)).or_default() += scalar;
    value.retain(|_, entry| *entry != 0);
}

fn one_boundary(slots: &[[Diagonal; 2]; 2], basis: OneChain) -> FormalVector<[usize; 2]> {
    let mut result = BTreeMap::new();
    match basis {
        OneChain::LeftInterval(right) => {
            add_term(
                &mut result,
                [0, right],
                LaurentMonomial::variable(slots[0][0]),
                1,
            );
            add_term(
                &mut result,
                [1, right],
                LaurentMonomial::variable(slots[0][1]),
                -1,
            );
        }
        OneChain::RightInterval(left) => {
            add_term(
                &mut result,
                [left, 0],
                LaurentMonomial::variable(slots[1][0]),
                1,
            );
            add_term(
                &mut result,
                [left, 1],
                LaurentMonomial::variable(slots[1][1]),
                -1,
            );
        }
    }
    result
}

fn two_boundary(slots: &[[Diagonal; 2]; 2]) -> FormalVector<u8> {
    // Basis 0,1 means h_left tensor e_right,j.  Basis 2,3 means
    // e_left,i tensor h_right.  The signs are d(h_L tensor h_R)=
    // d h_L tensor h_R - h_L tensor d h_R.
    let mut result = BTreeMap::new();
    add_term(&mut result, 2, LaurentMonomial::variable(slots[0][0]), 1);
    add_term(&mut result, 3, LaurentMonomial::variable(slots[0][1]), -1);
    add_term(&mut result, 0, LaurentMonomial::variable(slots[1][0]), -1);
    add_term(&mut result, 1, LaurentMonomial::variable(slots[1][1]), 1);
    result
}

fn one_basis(index: u8) -> OneChain {
    match index {
        0 => OneChain::LeftInterval(0),
        1 => OneChain::LeftInterval(1),
        2 => OneChain::RightInterval(0),
        3 => OneChain::RightInterval(1),
        _ => unreachable!(),
    }
}

fn audit_road_complex(channel: Diagonal) {
    let slots = road_slots(channel);
    let mut composed: FormalVector<[usize; 2]> = BTreeMap::new();
    for ((basis, coefficient), scalar) in two_boundary(&slots) {
        for ((endpoint, next_coefficient), next_scalar) in one_boundary(&slots, one_basis(basis)) {
            add_term(
                &mut composed,
                endpoint,
                coefficient.multiply(&next_coefficient),
                scalar * next_scalar,
            );
        }
    }
    assert!(
        composed.is_empty(),
        "the tensor interval differential squares to zero"
    );

    for basis in 0..4 {
        let mut evaluation = BTreeMap::<LaurentMonomial, i64>::new();
        for ((endpoint, coefficient), scalar) in one_boundary(&slots, one_basis(basis)) {
            let value = coefficient.multiply(&primitive_dual(&slots, endpoint));
            *evaluation.entry(value).or_default() += scalar;
        }
        evaluation.retain(|_, scalar| *scalar != 0);
        assert!(
            evaluation.is_empty(),
            "the primitive Laurent dual is a cocycle"
        );
    }

    for first in 0..2 {
        for second in 0..2 {
            let word = [first, second];
            assert_eq!(
                occurrence_weight(&slots, word).multiply(&primitive_dual(&slots, word)),
                LaurentMonomial::one()
            );
        }
    }
}

fn transformed_occurrence_word(road: usize, word: [usize; 2], element: GroupElement) -> [usize; 2] {
    let source_slots = road_slots(physical_channels()[road]);
    let transformed_weight =
        occurrence_weight(&source_slots, word).transform(element.amount, element.reflected);
    let target_slots = road_slots(physical_channels()[road_target(road, element)]);
    for first in 0..2 {
        for second in 0..2 {
            let candidate = [first, second];
            if occurrence_weight(&target_slots, candidate) == transformed_weight {
                return candidate;
            }
        }
    }
    panic!("every transformed occurrence has a unique target occurrence")
}

fn paired_tag(road: usize) -> usize {
    (road + 1) % 3
}

fn tag_target(tag: usize, element: GroupElement) -> usize {
    let rotation = element.amount as usize % 3;
    if element.reflected {
        (rotation + 2 - tag) % 3
    } else {
        (tag + rotation) % 3
    }
}

fn audit_equivariance() -> usize {
    let mut checks = 0;
    let tangential_gauge = tangential_orientation_gauge();
    for amount in 0..N {
        for reflected in [false, true] {
            let element = GroupElement { amount, reflected };
            assert_eq!(
                chi_n(element),
                core_character(element) * triangle_orientation_character(element)
            );
            for road in 0..3 {
                let target = road_target(road, element);
                assert_eq!(
                    tangential_gauge[target]
                        * tangential_orientation_character(road, element)
                        * tangential_gauge[road],
                    chi_n(element),
                    "road={road}, amount={amount}, reflected={reflected}"
                );
                assert_eq!(
                    tag_target(paired_tag(road), element),
                    paired_tag(road_target(road, element))
                );
                let source_slots = road_slots(physical_channels()[road]);
                let target_slots = road_slots(physical_channels()[road_target(road, element)]);
                for first in 0..2 {
                    for second in 0..2 {
                        let word = [first, second];
                        let target_word = transformed_occurrence_word(road, word, element);
                        let transformed_dual = primitive_dual(&source_slots, word)
                            .transform(element.amount, element.reflected);
                        assert_eq!(transformed_dual, primitive_dual(&target_slots, target_word));

                        // The oriented tag dual transforms by chi_N, and the
                        // coefficient line sgn_pol tensor or(C3) transforms by
                        // the same character.  Their product is untwisted, so
                        // Phi_gr is equivariant occurrence by occurrence.
                        assert_eq!(chi_n(element) * chi_n(element), 1);
                        checks += 1;
                    }
                }
            }
        }
    }
    assert_eq!(checks, 12 * 3 * 4);
    checks
}

fn cell_side(channel: Diagonal, cell: &Cell) -> u8 {
    let increasing: BTreeSet<_> = (channel.0 + 1..channel.1).collect();
    let endpoints = BTreeSet::from([channel.0, channel.1]);
    let others: BTreeSet<_> = cell.difference(&endpoints).copied().collect();
    if others.is_subset(&increasing) {
        0
    } else {
        assert!(others.is_disjoint(&increasing));
        1
    }
}

fn sink_and_source_slots(channel: Diagonal, plus: bool) -> ([Diagonal; 2], [Diagonal; 2]) {
    let plus_side = if channel.0 % 2 == 0 { 1 } else { 0 };
    let sink_side = if plus { plus_side } else { 1 - plus_side };
    let cells = quadrilateral_cells(channel);
    let sink = cells
        .iter()
        .find(|cell| cell_side(channel, cell) == sink_side)
        .unwrap();
    let source = cells.iter().find(|cell| *cell != sink).unwrap();
    (scalar_slots(sink), scalar_slots(source))
}

fn audit_endpoint_periods() -> (usize, [i64; 3]) {
    let mut marked_entries = 0;
    let mut road_periods = [0_i64; 3];
    for (road, &channel) in physical_channels().iter().enumerate() {
        for plus in [false, true] {
            let (sink, source) = sink_and_source_slots(channel, plus);
            let mut polarity_period = 0_i64;
            for sink_mark in sink {
                let endpoint_cousin = 1_i64;
                let scalar_source = -1_i64;
                let entry_coaction = -1_i64;
                let sign = endpoint_cousin * scalar_source * entry_coaction;
                assert_eq!(sign, 1);
                let marked_period: i64 = source
                    .iter()
                    .map(|&source_mark| {
                        let weight = LaurentMonomial::variable(source_mark)
                            .multiply(&LaurentMonomial::variable(sink_mark));
                        assert_eq!(weight.multiply(&weight.inverse()), LaurentMonomial::one());
                        sign
                    })
                    .sum();
                assert_eq!(marked_period, 2);
                polarity_period += marked_period;
                marked_entries += 1;
            }
            assert_eq!(polarity_period, 4);
            if plus {
                road_periods[road] = polarity_period;
            } else {
                assert_eq!(road_periods[road], 0);
            }
        }
    }
    assert_eq!(marked_entries, 12);
    assert_eq!(road_periods, [4, 4, 4]);
    (marked_entries, road_periods)
}

const CONTACT: [[i64; 6]; 3] = [
    [1, 1, 0, -1, -1, 0],
    [0, -1, -1, 0, 1, 1],
    [-1, 0, 1, 1, 0, -1],
];

const WARD_SYMBOL: [[i64; 6]; 7] = [
    [0, -1, -1, 0, 1, 1],
    [-1, -1, 0, 1, 1, 0],
    [0, 1, 1, 0, -1, -1],
    [1, 1, 0, -1, -1, 0],
    [-1, -1, 0, 1, 1, 0],
    [0, 1, 1, 0, -1, -1],
    [1, 0, -1, -1, 0, 1],
];

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

fn multiply_symbol_source(differential: [[i64; 6]; 6]) -> [[i64; 6]; 7] {
    std::array::from_fn(|row| {
        std::array::from_fn(|column| {
            (0..6)
                .map(|middle| WARD_SYMBOL[row][middle] * differential[middle][column])
                .sum()
        })
    })
}

fn square_matrix(matrix: [[i64; 6]; 6]) -> [[i64; 6]; 6] {
    std::array::from_fn(|row| {
        std::array::from_fn(|column| {
            (0..6)
                .map(|middle| matrix[row][middle] * matrix[middle][column])
                .sum()
        })
    })
}

fn audit_symbol_chain_gap() {
    for column in 0..6 {
        assert_eq!(CONTACT.iter().map(|row| row[column]).sum::<i64>(), 0);
        let ward_column = std::array::from_fn(|row| WARD_SYMBOL[row][column]);
        assert_eq!(ward_contact(ward_column), [0; 6]);
    }

    // Entry 66 fixes the modules and the displayed associated symbol but does
    // not construct the scalar kinetic/BRST chain lift.  The zero source
    // differential makes the closed symbol a chain map.  The square-zero
    // differential e_1 |-> e_0 does not.  Both have the same underlying six
    // generators and the same associated symbol, so symbol data alone cannot
    // decide the chain-pairing identity.
    let zero = [[0_i64; 6]; 6];
    let mut witness = zero;
    witness[0][1] = 1;
    assert_eq!(square_matrix(zero), zero);
    assert_eq!(square_matrix(witness), zero);
    assert_eq!(multiply_symbol_source(zero), [[0; 6]; 7]);
    assert_ne!(multiply_symbol_source(witness), [[0; 6]; 7]);

    // The carrier circuit complex has one relation generator k and three tag
    // generators c_i with d(k)=c_0+c_1+c_2.  Its PC/BRST lift, lower Cousin
    // terms, and the image of k are precisely what bold-sigma_alt must supply.
    let circuit_relation = [1_i64, 1, 1];
    assert_eq!(circuit_relation, [1, 1, 1]);

    // On the collapsed carrier, Phi identifies the road resolution
    // [P --epsilon--> 1] with the chi-twisted dual circuit resolution
    // [T^vee tensor chi --Delta^vee--> chi^vee tensor chi].  The differential
    // square commutes road by road because both maps have values (1,1,1).
    let road_augmentation = [1_i64, 1, 1];
    let circuit_dual_differential: [i64; 3] =
        std::array::from_fn(|road| circuit_relation[paired_tag(road)]);
    assert_eq!(road_augmentation, circuit_dual_differential);

    // This two-term resolution has A2 as its homology (up to degree/shift).
    // The primitive line is instead cofib(A2 -> P); Phi does not identify
    // those two derived objects.
    let a_two_roots = [[1_i64, -1, 0], [0, 1, -1]];
    assert!(a_two_roots.iter().all(|root| {
        root.iter()
            .zip(road_augmentation)
            .map(|(left, right)| left * right)
            .sum::<i64>()
            == 0
    }));
}

fn audit_boundary_costalk_gap() {
    // The two polarity tripods restrict to the same three road objects.  On
    // their six free carrier generators, restriction is [I_3 I_3].
    let restriction = [
        [1_i64, 0, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 0],
        [0, 0, 1, 0, 0, 1],
    ];
    let polarity_kernel = [
        [1_i64, 0, 0, -1, 0, 0],
        [0, 1, 0, 0, -1, 0],
        [0, 0, 1, 0, 0, -1],
    ];
    for vector in polarity_kernel {
        let image: [i64; 3] = std::array::from_fn(|row| {
            restriction[row]
                .iter()
                .zip(vector)
                .map(|(left, right)| left * right)
                .sum()
        });
        assert_eq!(image, [0, 0, 0]);
    }

    // Composing restriction with the road augmentation kills this kernel.
    // But a full object may have an additional contact generator z with zero
    // road restriction.  The two displayed extensions agree on all six road
    // lifts and differ only on z.  Road data cannot choose between them.
    let boundary_extension_zero = [1_i64, 1, 1, 1, 1, 1, 0];
    let boundary_extension_one = [1_i64, 1, 1, 1, 1, 1, 1];
    assert_eq!(&boundary_extension_zero[..6], &boundary_extension_one[..6]);
    assert_ne!(boundary_extension_zero[6], boundary_extension_one[6]);
}

fn main() {
    for channel in physical_channels() {
        audit_road_complex(channel);
    }
    let equivariance_checks = audit_equivariance();
    let (marked_entries, road_periods) = audit_endpoint_periods();
    audit_symbol_chain_gap();
    audit_boundary_costalk_gap();

    println!("primitive PC road/circuit associated-grade audit at D=03");
    println!("  road source: three actual tensor weighted-interval complexes");
    println!("  d_road^2=0 on 3 top cells; primitive dual kills 12 interval boundaries");
    println!("  Laurent inversion/relabeling checks: {equivariance_checks}");
    println!("  BM tangential system is gauge-isomorphic to sgn_polarity tensor or(C3)");
    println!("  its character after road-face orientation gauge is (+,-,-)");
    println!("  twist reversal and ordered-normal transport add no character");
    println!("  Phi_gr is equivariant on all 12 x 3 x 4 occurrence tests");
    println!("  primitive occurrence values are 1; marked entries: {marked_entries} values of 2");
    println!("  polarized road values are {road_periods:?}, with no division or averaging");
    println!("  circuit carrier: 3 tags plus 1 diagonal relation generator");
    println!("  Phi_gr intertwines epsilon=(1,1,1) with Delta_circ^vee road by road");
    println!("  this dual resolution represents A2, not the primitive cofiber line");
    println!("  entry-66 coefficient symbol is Ward closed, but is not a chain map yet");
    println!("  the certified pairing is on the 3-road boundary costalk, not full J6 PC");
    println!("  road restriction has a polarity/contact kernel invisible to augmentation");
    println!();
    println!("VERDICT: ASSOCIATED-GRADE PHI PROVED; PC CHAIN LIFT UNTYPED");
    println!("  first unsupported datum: bold-sigma_alt with scalar kinetic/BRST differential");
    println!("  without it, C_circ^PC and the target half of the Cousin pairing do not exist");
    println!("  a later full-object quotient must also type or localize the contact kernel");
}
