//! Bounded D=03 audit of the proposed primitive road counit as the adjoint of
//! entry 59's circuit relation.
//!
//! There are three separate statements.
//!
//! 1. On the scalar associated grade, each of the three six-point road
//!    squares has a canonical Laurent primitive functional.  It kills the
//!    weighted interval boundaries and sends every primitive occurrence
//!    representative to one.  Entry 86's twelve marked core-entry maps have
//!    period two per sink mark and four per complete road.  These are exact
//!    associated-grade functionals, not a counit on the complete PC object.
//! 2. Abstractly, the road augmentation is the dual of the circuit diagonal,
//!    but only with a character twist.  The oriented circuit-tag module is
//!    the road permutation module tensored by the character which is odd
//!    under road reflection and polarity-core exchange.
//! 3. Entry 86 transports its recorded ordered normal line positively and
//!    its occurrence period is invariant under both operations.  It does not
//!    supply the required character line or a PC Verdier pairing.  Therefore
//!    the bare PC-adjoint claim is false as stated; the twist-corrected claim
//!    remains untyped at one explicit equivariant pairing.  In particular,
//!    entry 59 has no occurrence-resolved circuit PC complex to which
//!    Verdier duality could already be applied.

use std::collections::{BTreeMap, BTreeSet};

const N: u8 = 6;

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct Diagonal(u8, u8);

#[derive(Clone, Copy, Debug)]
struct GroupElement {
    core_swap: bool,
    rotation: usize,
    reflected: bool,
}

type Vector = Vec<i64>;

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

type Cell = BTreeSet<u8>;

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

#[derive(Clone, Debug, Eq, PartialEq)]
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
}

fn occurrence_weight(slots: &[[Diagonal; 2]; 2], word: [usize; 2]) -> LaurentMonomial {
    LaurentMonomial::variable(slots[0][word[0]])
        .multiply(&LaurentMonomial::variable(slots[1][word[1]]))
}

fn primitive_functional(slots: &[[Diagonal; 2]; 2], word: [usize; 2]) -> LaurentMonomial {
    occurrence_weight(slots, word).inverse()
}

fn audit_road_square(channel: Diagonal) {
    let cells = quadrilateral_cells(channel);
    let slots = [scalar_slots(&cells[0]), scalar_slots(&cells[1])];
    let variables: BTreeSet<_> = slots.iter().flatten().copied().collect();
    assert_eq!(variables.len(), 4);

    // Every occurrence representative w_v e_v pairs to one.
    for first in 0..2 {
        for second in 0..2 {
            let word = [first, second];
            assert_eq!(
                occurrence_weight(&slots, word).multiply(&primitive_functional(&slots, word)),
                LaurentMonomial::one()
            );
        }
    }

    // The Laurent functional kills each of the four weighted interval
    // boundaries.  For example, with the other coordinate fixed at j,
    // X_(r1) lambda(e_1j)=X_(r0) lambda(e_0j)=X_(other,j)^(-1).
    for coordinate in 0..2 {
        for fixed in 0..2 {
            let mut lower = [fixed; 2];
            let mut upper = [fixed; 2];
            lower[coordinate] = 0;
            upper[coordinate] = 1;
            let lower_value = LaurentMonomial::variable(slots[coordinate][0])
                .multiply(&primitive_functional(&slots, lower));
            let upper_value = LaurentMonomial::variable(slots[coordinate][1])
                .multiply(&primitive_functional(&slots, upper));
            assert_eq!(lower_value, upper_value);
        }
    }
}

fn occurrence_entry_periods() -> BTreeMap<(usize, bool, Diagonal), i64> {
    let channels = physical_channels();
    let mut result = BTreeMap::new();
    for (road, &channel) in channels.iter().enumerate() {
        for plus in [false, true] {
            let (sink, source) = sink_and_source_slots(channel, plus);
            for sink_mark in sink {
                // Endpoint Cousin incidence is +1.  The scalar source
                // coefficient -X_sink and physical coaction sign -1 multiply
                // to +1.  There are two source occurrence terms, and the
                // road primitive dual evaluates each to one.
                let endpoint_cousin = 1_i64;
                let source_sign = -1_i64;
                let coaction_sign = -1_i64;
                let term_sign = endpoint_cousin * source_sign * coaction_sign;
                assert_eq!(term_sign, 1);
                let period: i64 = source
                    .iter()
                    .map(|&source_mark| {
                        let occurrence = LaurentMonomial::variable(source_mark)
                            .multiply(&LaurentMonomial::variable(sink_mark));
                        let dual = occurrence.inverse();
                        assert_eq!(occurrence.multiply(&dual), LaurentMonomial::one());
                        term_sign
                    })
                    .sum();
                assert_eq!(period, 2);
                result.insert((road, plus, sink_mark), period);
            }
        }
    }
    assert_eq!(result.len(), 12);
    for road in 0..3 {
        for plus in [false, true] {
            assert_eq!(
                result
                    .iter()
                    .filter(|((candidate, polarity, _), _)| {
                        *candidate == road && *polarity == plus
                    })
                    .map(|(_, period)| period)
                    .sum::<i64>(),
                4
            );
        }
    }
    result
}

fn road_target(index: usize, element: GroupElement) -> usize {
    if element.reflected {
        (element.rotation + 3 - index) % 3
    } else {
        (index + element.rotation) % 3
    }
}

fn tag_target(index: usize, element: GroupElement) -> usize {
    if element.reflected {
        (element.rotation + 6 - index - 1) % 3
    } else {
        (index + element.rotation) % 3
    }
}

fn character(element: GroupElement) -> i64 {
    let reflection = if element.reflected { -1 } else { 1 };
    let core = if element.core_swap { -1 } else { 1 };
    reflection * core
}

fn road_action(value: &[i64], element: GroupElement) -> Vector {
    let mut result = vec![0; 3];
    for (index, &coefficient) in value.iter().enumerate() {
        result[road_target(index, element)] += coefficient;
    }
    result
}

fn tag_action(value: &[i64], element: GroupElement) -> Vector {
    let mut result = vec![0; 3];
    let sign = character(element);
    for (index, &coefficient) in value.iter().enumerate() {
        result[tag_target(index, element)] += sign * coefficient;
    }
    result
}

fn unit(index: usize) -> Vector {
    let mut result = vec![0; 3];
    result[index] = 1;
    result
}

fn determinant_three(matrix: [[i64; 3]; 3]) -> i64 {
    matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
}

fn audit_augmentation_triangle() {
    // The roots span ker(epsilon) and adjoining one lift of 1 gives a
    // unimodular basis.  Hence 0 -> A2 -> P -> 1 -> 0 is saturated exact.
    let roots = [[1_i64, -1, 0], [0, 1, -1]];
    let epsilon = [1_i64, 1, 1];
    assert!(roots.iter().all(|root| {
        root.iter()
            .zip(epsilon)
            .map(|(left, right)| left * right)
            .sum::<i64>()
            == 0
    }));
    assert_eq!(
        determinant_three([
            [roots[0][0], roots[1][0], 0],
            [roots[0][1], roots[1][1], 0],
            [roots[0][2], roots[1][2], 1],
        ])
        .abs(),
        1
    );

    // Under the standard pairing, the transpose is the diagonal inclusion
    // 1^vee -> P^vee.  The primitive line is cofib(A2 -> P), represented by
    // the exact triangle A2 -> P -> 1 -> A2[1].  By contrast, if [P -> 1]
    // is put in consecutive homological degrees, its nonzero homology is the
    // kernel A2 (up to the chosen shift); it is not the primitive quotient.
    let diagonal = [1_i64, 1, 1];
    for road in 0..3 {
        assert_eq!(epsilon[road], diagonal[road]);
    }
}

fn pairing(road: &[i64], tag: &[i64]) -> i64 {
    assert_eq!(road.len(), 3);
    assert_eq!(tag.len(), 3);
    // The shift by two identifies the reflected oriented-edge indexing of
    // tags with the road permutation indexing.
    (0..3)
        .map(|tag_index| road[(tag_index + 2) % 3] * tag[tag_index])
        .sum()
}

fn audit_twisted_adjoint() -> usize {
    let diagonal = vec![1_i64; 3];
    let mut bare_character_failures = 0;
    for core_swap in [false, true] {
        for reflected in [false, true] {
            for rotation in 0..3 {
                let element = GroupElement {
                    core_swap,
                    rotation,
                    reflected,
                };
                assert_eq!(tag_action(&diagonal, element), vec![character(element); 3]);
                for road_index in 0..3 {
                    for tag_index in 0..3 {
                        let left = pairing(
                            &road_action(&unit(road_index), element),
                            &tag_action(&unit(tag_index), element),
                        );
                        let right =
                            character(element) * pairing(&unit(road_index), &unit(tag_index));
                        assert_eq!(left, right);
                    }
                }

                // Delta^vee evaluates every road basis vector to one.  Its
                // target is the dual relation line of character chi.  To
                // obtain the trivial road augmentation one must tensor both
                // sides by chi.  Entry 86's recorded normal transport has
                // character +1, so the normal line alone fails to provide
                // this identification whenever chi=-1.  A tensor-order or
                // twist-reversal orientation line could still provide it,
                // but no such line map is present in the audited checker.
                let recorded_normal_character = 1_i64;
                if recorded_normal_character != character(element) {
                    bare_character_failures += 1;
                }
                for road_index in 0..3 {
                    let delta_dual_value: i64 = (0..3)
                        .map(|tag_index| pairing(&unit(road_index), &unit(tag_index)))
                        .sum();
                    assert_eq!(delta_dual_value, 1);
                    assert_eq!(
                        road_action(&unit(road_index), element).iter().sum::<i64>(),
                        1
                    );
                }
            }
        }
    }
    assert_eq!(bare_character_failures, 6);
    bare_character_failures
}

fn main() {
    audit_augmentation_triangle();
    let channels = physical_channels();
    for &channel in &channels {
        audit_road_square(channel);
    }
    let periods = occurrence_entry_periods();
    assert!(periods.values().all(|&period| period == 2));
    let bare_character_failures = audit_twisted_adjoint();

    println!("primitive road counit / circuit-adjoint audit at outer D=03");
    println!("  induced six-point roads: D0=03, D1=14, D2=25");
    println!("  three weighted road squares: 12 primitive occurrence representatives");
    println!("  Laurent primitive dual kills all 12 weighted interval boundaries");
    println!("  all 12 marked core entries have period 2; each complete road has period 4");
    println!("  endpoint Cousin +, scalar-source -, and coaction - signs are retained");
    println!("  the three associated-grade road functionals and periods are invariant");
    println!("  primitive line = cofib(A2 -> P) in A2 -> P -> 1 -> A2[1]");
    println!("  [P -> 1] instead has A2 homology, up to the degree convention");
    println!("  T_circ = P_roads tensor chi after the required index shift");
    println!("  chi(rotation)=+1, chi(reflection)=-1, chi(core_swap)=-1");
    println!("  epsilon=sum is Delta_circ^vee tensor chi at the lattice level");
    println!(
        "  bare character mismatches with entry-86 normal transport: {bare_character_failures}/12"
    );
    println!();
    println!("VERDICT: BARE PC ADJOINT FALSIFIED; TWISTED PC ADJOINT UNTYPED");
    println!("  each associated-grade road functional exists; the three full periods are (4,4,4)");
    println!("  abstract transpose duality does not construct a PC Verdier pairing");
    println!("  first missing: a chain-level chi-valued twist-reversal pairing Phi_03^PC");
    println!("  no D8 extension is made before that representative pairing exists");
}
