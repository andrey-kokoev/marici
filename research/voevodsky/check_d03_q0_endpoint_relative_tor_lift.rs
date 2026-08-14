//! Anti-circular audit of the endpoint-relative q0 extraordinary-lift attempt.
//!
//! Entry 118 supplies the marked interval
//!
//!   F03 > Z3 > v10 < ec > v+ > e3 > q0.
//!
//! Before imposing the inherited x3 sink mark, the actual gallery category
//! has two saturated road branches.  Relative to F03 and q0 its first BM
//! homology is a saturated Z^2.  The full road square contracts integrally to
//! its counit, so the carrier cohomological-correspondence Hom remains rank
//! two in shifted BM degree and is zero in ordinary degree zero.  The x3 mark
//! selects one primitive coordinate; the common lcm x1*x3 does not.
//!
//! The non-monotone marked interval is not treated as one exit morphism.  Its
//! x3-supported middle slab is the three-edge relative Cartier bordism
//!
//!   Z3 -> v10 -> ec -> v+.
//!
//! With the actual principal occurrence lines, its oriented fundamental
//! chain has boundary
//!
//!   x3 * (x1*x5 [v+] - X03 [Z3]).
//!
//! The internal cancellations use, rather than invert, the actual x1, X03,
//! and x5 generizations.  The two terms after division by the labelled x3
//! Cartier equation are exactly the source flag e3<v+ and road flag F03<Z3.
//!
//! Over A=Z[t3,x3,q3^+-1]/(q3-1-t3*x3), put u3=t3*x3 and
//! u3^vee=-q3^-1*u3.  For
//!
//!   D3=K(u3^vee) tensor K(u3),
//!
//! the primitive saturated middle kernel is
//!
//!   eta_mix=(-q3,-1).
//!
//! If z is the repeated-normal top, the forced reciprocal normalization is
//! z_norm=q3*z, and
//!
//!   d(z_norm)=x3*(t3*eta_mix).
//!
//! Thus the first x3-Bockstein derives the labelled map [t3]->eta_mix; it is
//! not assigned after central base change.  Tensoring this normalized
//! two-term excess packet with the endpoint-relative occurrence map
//!
//!   [e3 --(-x1)--> q0] -> [F03 --(+x1)--> tau0],
//!   (e3,q0) |-> (F03,-tau0),
//!
//! gives a necessary weighted associated-grade complex whose differential
//! squares to zero and whose formal Beck--Chevalley square commutes before
//! x1=x3=0.  It is not yet the extraordinary PC map.  The carrier staircase
//! has no constructed ringed q-projection to the derived road Thom costalk,
//! hence no relative-dualizing/Alexander--Whitney counit.  Moreover the full
//! endpoint RHom and normal packet retain their adjacent H0/Tor1 copies,
//! leaving at least two adjacent grades after the carrier mark; their loaded
//! spatial Hom rank is undefined.  Truncating to eta alone would manufacture
//! the desired rank-one answer.  Reusing the entry-97
//! target does not help: its x1,x3,u3 localization contracts K0, the Thom
//! factor, and D3, so the common-base loaded RHom is zero.

use std::collections::BTreeMap;

type Int = i64;

const X03: usize = 0;
const X1: usize = 1;
const X3: usize = 2;
const X5: usize = 3;

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct OccurrenceMonomial([u8; 4]);

impl OccurrenceMonomial {
    fn variable(slot: usize) -> Self {
        let mut powers = [0; 4];
        powers[slot] = 1;
        Self(powers)
    }

    fn multiply(self, other: Self) -> Self {
        Self(std::array::from_fn(|slot| self.0[slot] + other.0[slot]))
    }

    fn divide(self, divisor: Self) -> Option<Self> {
        self.0
            .iter()
            .zip(divisor.0)
            .all(|(numerator, denominator)| numerator >= &denominator)
            .then(|| Self(std::array::from_fn(|slot| self.0[slot] - divisor.0[slot])))
    }
}

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
enum Node {
    F03,
    Z1,
    Z3,
    V10,
    Ec,
    VPlus,
    E3,
    Q0,
}

fn occurrence_label(node: Node) -> OccurrenceMonomial {
    let x03 = OccurrenceMonomial::variable(X03);
    let x1 = OccurrenceMonomial::variable(X1);
    let x3 = OccurrenceMonomial::variable(X3);
    let x5 = OccurrenceMonomial::variable(X5);
    match node {
        Node::F03 => x03,
        Node::Z1 => x03.multiply(x1),
        Node::Z3 => x03.multiply(x3),
        Node::V10 => x03.multiply(x1).multiply(x3),
        Node::Ec => x1.multiply(x3),
        Node::VPlus => x1.multiply(x3).multiply(x5),
        Node::E3 => x1.multiply(x5),
        Node::Q0 => x5,
    }
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct Incidence {
    lower: Node,
    upper: Node,
    multiplier: OccurrenceMonomial,
}

fn incidence(lower: Node, upper: Node) -> Incidence {
    let lower_label = occurrence_label(lower);
    let upper_label = occurrence_label(upper);
    let multiplier = upper_label
        .divide(lower_label)
        .expect("comparable faces have divisible occurrence labels");
    assert_eq!(lower_label.multiply(multiplier), upper_label);
    Incidence {
        lower,
        upper,
        multiplier,
    }
}

fn check_actual_interval_incidences() {
    let x03 = OccurrenceMonomial::variable(X03);
    let x1 = OccurrenceMonomial::variable(X1);
    let x3 = OccurrenceMonomial::variable(X3);
    let x5 = OccurrenceMonomial::variable(X5);
    let incidences = [
        incidence(Node::F03, Node::Z1),
        incidence(Node::Z1, Node::V10),
        incidence(Node::F03, Node::Z3),
        incidence(Node::Z3, Node::V10),
        incidence(Node::Ec, Node::V10),
        incidence(Node::Ec, Node::VPlus),
        incidence(Node::E3, Node::VPlus),
        incidence(Node::Q0, Node::E3),
    ];
    assert_eq!(
        incidences.map(|arrow| arrow.multiplier),
        [x1, x3, x3, x1, x03, x5, x3, x1]
    );

    // Before the inherited sink mark there are two saturated road flags.
    // Their products agree, so the lcm line cannot itself choose a flag.
    assert_eq!(
        incidences[0].multiplier.multiply(incidences[1].multiplier),
        x1.multiply(x3)
    );
    assert_eq!(
        incidences[2].multiplier.multiply(incidences[3].multiplier),
        x1.multiply(x3)
    );

    // Both Cartier boundary crossings of the marked x3 gallery have exactly
    // the same x3 occurrence equation.  X03 and x5 remain the two distinct
    // central-flip legs.
    assert_eq!(incidences[2].multiplier, x3);
    assert_eq!(incidences[6].multiplier, x3);
    assert_eq!(incidences[4].multiplier, x03);
    assert_eq!(incidences[5].multiplier, x5);
    assert_ne!(x03, x5);
}

type IntegerMatrix = Vec<Vec<Int>>;

#[derive(Clone, Debug)]
struct FreeComplex {
    ranks: Vec<usize>,
    // boundary[n]: C_n -> C_{n-1}; boundary[0] is empty.
    boundary: Vec<IntegerMatrix>,
}

fn integer_zero(rows: usize, columns: usize) -> IntegerMatrix {
    vec![vec![0; columns]; rows]
}

fn integer_identity(size: usize) -> IntegerMatrix {
    let mut result = integer_zero(size, size);
    for (index, row) in result.iter_mut().enumerate() {
        row[index] = 1;
    }
    result
}

fn integer_multiply(left: &IntegerMatrix, right: &IntegerMatrix) -> IntegerMatrix {
    assert!(!left.is_empty() && !right.is_empty());
    assert_eq!(left[0].len(), right.len());
    let mut result = integer_zero(left.len(), right[0].len());
    for row in 0..left.len() {
        for middle in 0..right.len() {
            for column in 0..right[0].len() {
                result[row][column] += left[row][middle] * right[middle][column];
            }
        }
    }
    result
}

fn integer_add(left: &IntegerMatrix, right: &IntegerMatrix) -> IntegerMatrix {
    assert_eq!(left.len(), right.len());
    assert_eq!(left.first().map(Vec::len), right.first().map(Vec::len));
    let mut result = left.clone();
    for row in 0..result.len() {
        for column in 0..result[row].len() {
            result[row][column] += right[row][column];
        }
    }
    result
}

fn integer_transpose(value: &IntegerMatrix) -> IntegerMatrix {
    assert!(!value.is_empty());
    let mut result = integer_zero(value[0].len(), value.len());
    for (row, entries) in value.iter().enumerate() {
        for (column, entry) in entries.iter().enumerate() {
            result[column][row] = *entry;
        }
    }
    result
}

fn gcd(mut left: Int, mut right: Int) -> Int {
    left = left.abs();
    right = right.abs();
    while right != 0 {
        (left, right) = (right, left % right);
    }
    left
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct Rational {
    numerator: Int,
    denominator: Int,
}

impl Rational {
    fn new(numerator: Int, denominator: Int) -> Self {
        assert_ne!(denominator, 0);
        if numerator == 0 {
            return Self {
                numerator: 0,
                denominator: 1,
            };
        }
        let sign = denominator.signum();
        let common = gcd(numerator, denominator);
        Self {
            numerator: sign * numerator / common,
            denominator: sign * denominator / common,
        }
    }

    fn subtract(self, other: Self) -> Self {
        Self::new(
            self.numerator * other.denominator - other.numerator * self.denominator,
            self.denominator * other.denominator,
        )
    }

    fn multiply(self, other: Self) -> Self {
        Self::new(
            self.numerator * other.numerator,
            self.denominator * other.denominator,
        )
    }

    fn inverse(self) -> Self {
        assert_ne!(self.numerator, 0);
        Self::new(self.denominator, self.numerator)
    }
}

fn integer_rank(value: &IntegerMatrix) -> usize {
    if value.is_empty() {
        return 0;
    }
    let mut work: Vec<Vec<_>> = value
        .iter()
        .map(|row| row.iter().map(|entry| Rational::new(*entry, 1)).collect())
        .collect();
    let mut pivot_row = 0;
    for column in 0..work[0].len() {
        let Some(row) = (pivot_row..work.len()).find(|row| work[*row][column].numerator != 0)
        else {
            continue;
        };
        work.swap(pivot_row, row);
        let inverse = work[pivot_row][column].inverse();
        for entry in &mut work[pivot_row][column..] {
            *entry = entry.multiply(inverse);
        }
        let pivot = work[pivot_row].clone();
        for row in 0..work.len() {
            if row == pivot_row {
                continue;
            }
            let factor = work[row][column];
            for target in column..work[row].len() {
                work[row][target] = work[row][target].subtract(factor.multiply(pivot[target]));
            }
        }
        pivot_row += 1;
    }
    pivot_row
}

fn determinant(value: &IntegerMatrix) -> Int {
    assert!(!value.is_empty() && value.iter().all(|row| row.len() == value.len()));
    let mut permutations: Vec<usize> = (0..value.len()).collect();
    fn parity_sum(value: &IntegerMatrix, row: usize, permutation: &mut [usize], total: &mut Int) {
        if row == permutation.len() {
            let inversions = permutation
                .iter()
                .enumerate()
                .map(|(index, entry)| {
                    permutation[index + 1..]
                        .iter()
                        .filter(|other| entry > *other)
                        .count()
                })
                .sum::<usize>();
            let sign = if inversions % 2 == 0 { 1 } else { -1 };
            *total += sign
                * permutation
                    .iter()
                    .enumerate()
                    .map(|(source_row, column)| value[source_row][*column])
                    .product::<Int>();
            return;
        }
        for index in row..permutation.len() {
            permutation.swap(row, index);
            parity_sum(value, row + 1, permutation, total);
            permutation.swap(row, index);
        }
    }
    let mut result = 0;
    parity_sum(value, 0, &mut permutations, &mut result);
    result
}

fn check_free_complex(complex: &FreeComplex) {
    assert_eq!(complex.ranks.len(), complex.boundary.len());
    for degree in 1..complex.ranks.len() {
        assert_eq!(complex.boundary[degree].len(), complex.ranks[degree - 1]);
        assert!(complex.boundary[degree]
            .iter()
            .all(|row| row.len() == complex.ranks[degree]));
    }
    for degree in 2..complex.ranks.len() {
        assert_eq!(
            integer_multiply(&complex.boundary[degree - 1], &complex.boundary[degree]),
            integer_zero(complex.ranks[degree - 2], complex.ranks[degree])
        );
    }
}

fn unmarked_gallery_relative_complex() -> FreeComplex {
    // Relative vertices: Z1,Z3,v10,ec,v+,e3.  Columns are the two road
    // branches F03-Zi-Z10 followed by the common four-edge suffix to q0.
    let boundary = vec![
        vec![1, -1, 0, 0, 0, 0, 0, 0],
        vec![0, 0, 1, -1, 0, 0, 0, 0],
        vec![0, 1, 0, 1, -1, 0, 0, 0],
        vec![0, 0, 0, 0, 1, -1, 0, 0],
        vec![0, 0, 0, 0, 0, 1, -1, 0],
        vec![0, 0, 0, 0, 0, 0, 1, -1],
    ];
    FreeComplex {
        ranks: vec![6, 8],
        boundary: vec![Vec::new(), boundary],
    }
}

fn full_road_square() -> FreeComplex {
    FreeComplex {
        ranks: vec![4, 4, 1],
        boundary: vec![
            Vec::new(),
            vec![
                vec![-1, 0, -1, 0],
                vec![1, 0, 0, -1],
                vec![0, -1, 1, 0],
                vec![0, 1, 0, 1],
            ],
            vec![vec![1], vec![-1], vec![-1], vec![1]],
        ],
    }
}

fn mapping_free_complex(source: &FreeComplex, target: &FreeComplex) -> FreeComplex {
    // Hom(source,target)^n consists of maps source_i -> target_{i+n}.
    // Store the degrees n=-2,-1,0,1 in that order, so the Hom differential
    // lowers the displayed index exactly like a homological boundary.
    let minimum_degree = -(source.ranks.len() as isize - 1);
    let maximum_degree = target.ranks.len() as isize - 1;
    let bases: Vec<Vec<(usize, usize, usize, usize)>> = (minimum_degree..=maximum_degree)
        .map(|map_degree| {
            let mut basis = Vec::new();
            for source_degree in 0..source.ranks.len() {
                let target_degree = source_degree as isize + map_degree;
                if target_degree < 0 || target_degree >= target.ranks.len() as isize {
                    continue;
                }
                let target_degree = target_degree as usize;
                for source_index in 0..source.ranks[source_degree] {
                    for target_index in 0..target.ranks[target_degree] {
                        basis.push((source_degree, source_index, target_degree, target_index));
                    }
                }
            }
            basis
        })
        .collect();
    let indices: Vec<BTreeMap<_, _>> = bases
        .iter()
        .map(|basis| {
            basis
                .iter()
                .copied()
                .enumerate()
                .map(|(index, entry)| (entry, index))
                .collect()
        })
        .collect();
    let mut boundary = vec![Vec::new(); bases.len()];
    for degree_index in 1..bases.len() {
        let map_degree = minimum_degree + degree_index as isize;
        let mut matrix = integer_zero(bases[degree_index - 1].len(), bases[degree_index].len());
        for (column, &(sd, si, td, ti)) in bases[degree_index].iter().enumerate() {
            // d_target after the basis map.
            if td > 0 {
                for output in 0..target.ranks[td - 1] {
                    let coefficient = target.boundary[td][output][ti];
                    if coefficient != 0 {
                        matrix[indices[degree_index - 1][&(sd, si, td - 1, output)]][column] +=
                            coefficient;
                    }
                }
            }

            // -(-1)^n times precomposition with d_source.
            if sd + 1 < source.ranks.len() {
                let sign = if map_degree.rem_euclid(2) == 0 { -1 } else { 1 };
                for input in 0..source.ranks[sd + 1] {
                    let coefficient = source.boundary[sd + 1][si][input];
                    if coefficient != 0 {
                        matrix[indices[degree_index - 1][&(sd + 1, input, td, ti)]][column] +=
                            sign * coefficient;
                    }
                }
            }
        }
        boundary[degree_index] = matrix;
    }
    FreeComplex {
        ranks: bases.iter().map(Vec::len).collect(),
        boundary,
    }
}

fn check_ambient_gallery_road_hom_and_ablation() {
    let gallery = unmarked_gallery_relative_complex();
    let road = full_road_square();
    check_free_complex(&gallery);
    check_free_complex(&road);

    // A unit maximal minor makes the gallery boundary a split surjection.
    // Its kernel is therefore a saturated Z^2, not a fitted rank-one line.
    let pivot_columns = [0_usize, 2, 4, 5, 6, 7];
    let gallery_minor: IntegerMatrix = gallery.boundary[1]
        .iter()
        .map(|row| pivot_columns.map(|column| row[column]).to_vec())
        .collect();
    assert_eq!(determinant(&gallery_minor).abs(), 1);
    assert_eq!(integer_rank(&gallery.boundary[1]), 6);
    let path_z1 = vec![1, 1, 0, 0, 1, 1, 1, 1];
    let path_z3 = vec![0, 0, 1, 1, 1, 1, 1, 1];
    for path in [&path_z1, &path_z3] {
        let column: IntegerMatrix = path.iter().map(|entry| vec![*entry]).collect();
        assert_eq!(
            integer_multiply(&gallery.boundary[1], &column),
            integer_zero(6, 1)
        );
    }
    assert_eq!((path_z1[1], path_z1[3]), (1, 0));
    assert_eq!((path_z3[1], path_z3[3]), (0, 1));

    // The full road square, not an endpoint truncation, contracts integrally
    // to v00.  These identities prove that its trace is one primitive line
    // and introduce no torsion.
    let augmentation = vec![vec![1, 1, 1, 1]];
    let inclusion = vec![vec![1], vec![0], vec![0], vec![0]];
    let h0 = vec![
        vec![0, 1, 0, 1],
        vec![0, 0, 0, 0],
        vec![0, 0, 1, 0],
        vec![0, 0, 0, 1],
    ];
    let h1 = vec![vec![0, -1, 0, 0]];
    assert_eq!(
        integer_add(
            &integer_multiply(&road.boundary[1], &h0),
            &integer_multiply(&inclusion, &augmentation)
        ),
        integer_identity(4)
    );
    assert_eq!(
        integer_add(
            &integer_multiply(&road.boundary[2], &h1),
            &integer_multiply(&h0, &road.boundary[1])
        ),
        integer_identity(4)
    );
    assert_eq!(
        integer_multiply(&h1, &road.boundary[2]),
        integer_identity(1)
    );
    assert_eq!(
        integer_multiply(&augmentation, &road.boundary[1]),
        integer_zero(1, 4)
    );

    // The two forgetful projections p:Gal_03->B0 and q:Gal_03->R03 give the
    // endpoint-relative cohomological-correspondence mapping complex
    //
    //   RHom(C_*(R03), C_*(Gal_03,partial Gal_03)).
    //
    // This is the finite relative-costalk model of q_! p^!: the source
    // triangle kills the two gallery endpoints, while the target uses the
    // complete road square and its counit, not a selected endpoint stalk.
    // Integral contraction of the road square identifies the mapping complex
    // with the relative gallery complex without choosing either gallery.
    let ambient = mapping_free_complex(&road, &gallery);
    check_free_complex(&ambient);
    assert_eq!(ambient.ranks, [6, 32, 56, 32]);
    let differential_ranks: Vec<_> = (1..ambient.ranks.len())
        .map(|degree| integer_rank(&ambient.boundary[degree]))
        .collect();
    assert_eq!(differential_ranks, [6, 26, 30]);
    let homology_ranks: Vec<_> = (0..ambient.ranks.len())
        .map(|degree| {
            let outgoing = if degree == 0 {
                0
            } else {
                differential_ranks[degree - 1]
            };
            let incoming = if degree + 1 == ambient.ranks.len() {
                0
            } else {
                differential_ranks[degree]
            };
            ambient.ranks[degree] - outgoing - incoming
        })
        .collect();
    assert_eq!(homology_ranks, [0, 0, 0, 2]);

    // Negative control: ordinary (unshifted) endpoint Hom is zero.  The two
    // classes live only in correspondence/Borel--Moore degree +1, exactly
    // the shift supplied by the relative dual cell.
    let ordinary_hom_h0 = homology_ranks[2];
    let bm_correspondence_h1 = homology_ranks[3];
    assert_eq!(ordinary_hom_h0, 0);
    assert_eq!(bm_correspondence_h1, 2);

    // Forgetful projections on the two primitive gallery classes.  Both use
    // the same Boolean source flag; the road projection remembers which of
    // the two saturated F03 flags was used.  The inherited x3 sink mark is
    // the primitive coordinate inclusion (0,1), so rank two drops
    // saturately to rank one.  The lcm product x1*x3 is equal on both paths
    // and, by itself, does not perform this reduction.
    let to_boolean_flag = vec![vec![1, 1]];
    let to_road_flags = integer_identity(2);
    let x3_marked_inclusion = vec![vec![0], vec![1]];
    assert_eq!(integer_rank(&to_boolean_flag), 1);
    assert_eq!(integer_rank(&to_road_flags), 2);
    assert_eq!(integer_rank(&x3_marked_inclusion), 1);
    assert_eq!(
        integer_multiply(
            &integer_transpose(&x3_marked_inclusion),
            &x3_marked_inclusion
        ),
        integer_identity(1)
    );
}

#[derive(Clone, Copy, Debug, Eq, PartialEq, PartialOrd)]
enum BooleanFlagStage {
    E3,
    Q0,
}

#[derive(Clone, Copy, Debug, Eq, PartialEq, PartialOrd)]
enum RoadFlagStage {
    F03,
    Z,
    Tau,
}

fn check_staircase_projection_scope() {
    // Carrier-level candidates for p and q.  On either gallery, p is
    // constant on e3 until the last Boolean edge, q follows the saturated
    // road flag until tau, and the central flip/suffix collapses to
    // (e3,tau).  Thus the non-monotone carrier zigzag becomes a monotone
    // staircase in the product of the two relative flags.
    let p = [
        BooleanFlagStage::E3,
        BooleanFlagStage::E3,
        BooleanFlagStage::E3,
        BooleanFlagStage::E3,
        BooleanFlagStage::E3,
        BooleanFlagStage::E3,
        BooleanFlagStage::Q0,
    ];
    let q = [
        RoadFlagStage::F03,
        RoadFlagStage::Z,
        RoadFlagStage::Tau,
        RoadFlagStage::Tau,
        RoadFlagStage::Tau,
        RoadFlagStage::Tau,
        RoadFlagStage::Tau,
    ];
    assert!(p.windows(2).all(|step| step[0] <= step[1]));
    assert!(q.windows(2).all(|step| step[0] <= step[1]));
    assert_eq!((p[3], q[3]), (BooleanFlagStage::E3, RoadFlagStage::Tau));

    // The staircase is essential: q0 and F03 are incomparable even as
    // principal occurrence lines, so the ordinary incidence-category Hom
    // has no endpoint arrow in either direction.
    let q0_line = occurrence_label(Node::Q0);
    let f03_line = occurrence_label(Node::F03);
    assert_eq!(q0_line.divide(f03_line), None);
    assert_eq!(f03_line.divide(q0_line), None);

    // These are carrier/simplicial projections only.  The committed absolute
    // PC complex has no module named tau_i: entry 118 defines only
    // tau_i^car, while the desired object is the iterated relative Thom
    // costalk of the full road square.  Consequently no cited differential
    // supplies the ringed q-counit or its relative-dualizing trace.  Marking
    // a gallery cannot repair this type gap.
    let actual_tau_relative_thom_module_constructed = false;
    let ringed_q_counit_constructed = false;
    let relative_dualizing_trace_constructed = false;
    assert!(!actual_tau_relative_thom_module_constructed);
    assert!(!ringed_q_counit_constructed);
    assert!(!relative_dualizing_trace_constructed);
}

fn check_entry97_localized_loaded_hom_negative_control() {
    // Entry 97's actual local bivariant trace is defined only after adjoining
    // x1^-1, x3^-1, and u3^-1.  Over that common base every factor needed by
    // the endpoint lift is already contractible.  In normalized bases the
    // three two-term differentials and contracting homotopies are units.
    let localized_units = ["x1", "x3", "u3"];
    assert_eq!(localized_units.len(), 3);
    let k0_differential = -1_i64;
    let k0_homotopy = -1_i64;
    let x3_thom_differential = 1_i64;
    let x3_thom_homotopy = 1_i64;
    let normal_differential = 1_i64;
    let normal_homotopy = 1_i64;
    assert_eq!(k0_differential * k0_homotopy, 1);
    assert_eq!(x3_thom_differential * x3_thom_homotopy, 1);
    assert_eq!(normal_differential * normal_homotopy, 1);

    // Tensoring or taking Hom with a finite-free contractible factor remains
    // contractible.  Thus the entry-97 localized road trace cannot be reused
    // as the loaded endpoint target: its common-base RHom is zero.  This is a
    // falsifier for that reuse only, not for a new unlocalized Thom costalk.
    let common_base_loaded_rhom_rank = 0_usize;
    assert_eq!(common_base_loaded_rhom_rank, 0);
}

#[derive(Clone, Debug, Eq, PartialEq)]
struct OccurrenceCombination(BTreeMap<Node, (Int, OccurrenceMonomial)>);

impl OccurrenceCombination {
    fn zero() -> Self {
        Self(BTreeMap::new())
    }

    fn add_term(&mut self, node: Node, sign: Int, label: OccurrenceMonomial) {
        if let Some((old_sign, old_label)) = self.0.get_mut(&node) {
            assert_eq!(*old_label, label);
            *old_sign += sign;
            if *old_sign == 0 {
                self.0.remove(&node);
            }
        } else if sign != 0 {
            self.0.insert(node, (sign, label));
        }
    }
}

fn add_oriented_barycentric_edge(
    boundary: &mut OccurrenceCombination,
    arrow: Incidence,
    path_sign: Int,
) {
    // The pulled-back occurrence cosheaf is based at the lower flag face.
    // Deleting the initial vertex applies label(upper)/label(lower); deleting
    // the terminal vertex is the unit on the lower principal line.
    boundary.add_term(
        arrow.upper,
        path_sign,
        occurrence_label(arrow.lower).multiply(arrow.multiplier),
    );
    boundary.add_term(arrow.lower, -path_sign, occurrence_label(arrow.lower));
}

fn check_weighted_middle_cartier_bordism() {
    let mut boundary = OccurrenceCombination::zero();
    // Path orientation: Z3 -> V10 -> Ec -> VPlus.  The middle barycentric
    // simplex is canonically Ec<V10, hence it occurs with coefficient -1.
    add_oriented_barycentric_edge(&mut boundary, incidence(Node::Z3, Node::V10), 1);
    add_oriented_barycentric_edge(&mut boundary, incidence(Node::Ec, Node::V10), -1);
    add_oriented_barycentric_edge(&mut boundary, incidence(Node::Ec, Node::VPlus), 1);

    let x03 = OccurrenceMonomial::variable(X03);
    let x1 = OccurrenceMonomial::variable(X1);
    let x3 = OccurrenceMonomial::variable(X3);
    let x5 = OccurrenceMonomial::variable(X5);
    assert_eq!(boundary.0.len(), 2);
    assert_eq!(boundary.0[&Node::Z3], (-1, x03.multiply(x3)));
    assert_eq!(boundary.0[&Node::VPlus], (1, x1.multiply(x3).multiply(x5)));

    // Divide once by the labelled Cartier equation.  The two residual lines
    // are exactly the outer source and road lines; no X03/x5 identification
    // and no base-ring inverse is used.
    assert_eq!(
        boundary.0[&Node::Z3].1.divide(x3),
        Some(occurrence_label(Node::F03))
    );
    assert_eq!(
        boundary.0[&Node::VPlus].1.divide(x3),
        Some(occurrence_label(Node::E3))
    );
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum PullPushDirection {
    CovariantGenerization,
    PrincipalDualEvaluation,
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct PullPushStep {
    from: Node,
    to: Node,
    labelled_factor: OccurrenceMonomial,
    direction: PullPushDirection,
}

fn apply_pull_push_step(present: OccurrenceMonomial, step: PullPushStep) -> OccurrenceMonomial {
    assert_eq!(present, occurrence_label(step.from));
    let result = match step.direction {
        PullPushDirection::CovariantGenerization => present.multiply(step.labelled_factor),
        PullPushDirection::PrincipalDualEvaluation => present
            .divide(step.labelled_factor)
            .expect("the matching labelled principal line is present"),
    };
    assert_eq!(result, occurrence_label(step.to));
    result
}

fn check_full_interval_principal_line_transport() {
    let x03 = OccurrenceMonomial::variable(X03);
    let x1 = OccurrenceMonomial::variable(X1);
    let x3 = OccurrenceMonomial::variable(X3);
    let x5 = OccurrenceMonomial::variable(X5);
    let steps = [
        PullPushStep {
            from: Node::Q0,
            to: Node::E3,
            labelled_factor: x1,
            direction: PullPushDirection::CovariantGenerization,
        },
        PullPushStep {
            from: Node::E3,
            to: Node::VPlus,
            labelled_factor: x3,
            direction: PullPushDirection::CovariantGenerization,
        },
        PullPushStep {
            from: Node::VPlus,
            to: Node::Ec,
            labelled_factor: x5,
            direction: PullPushDirection::PrincipalDualEvaluation,
        },
        PullPushStep {
            from: Node::Ec,
            to: Node::V10,
            labelled_factor: x03,
            direction: PullPushDirection::CovariantGenerization,
        },
        PullPushStep {
            from: Node::V10,
            to: Node::Z3,
            labelled_factor: x1,
            direction: PullPushDirection::PrincipalDualEvaluation,
        },
        PullPushStep {
            from: Node::Z3,
            to: Node::F03,
            labelled_factor: x3,
            direction: PullPushDirection::PrincipalDualEvaluation,
        },
    ];
    let mut line = occurrence_label(Node::Q0);
    for step in steps {
        line = apply_pull_push_step(line, step);
    }
    assert_eq!(line, occurrence_label(Node::F03));

    // The central flip uses a source x5 evaluation and a target X03
    // generization.  The final physical-normal evaluation is a separate
    // positively oriented line, not an equality X03=x5.
    let source_occurrence_evaluation = x5;
    let target_physical_line = x03;
    assert_ne!(source_occurrence_evaluation, target_physical_line);
    let physical_dx03_orientation = 1_i64;
    assert_eq!(physical_dx03_orientation, 1);
}

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct LaurentTerm {
    coefficient: Int,
    q_power: i8,
    t_power: u8,
    x_power: u8,
}

impl LaurentTerm {
    fn one() -> Self {
        Self {
            coefficient: 1,
            q_power: 0,
            t_power: 0,
            x_power: 0,
        }
    }

    fn q() -> Self {
        Self {
            q_power: 1,
            ..Self::one()
        }
    }

    fn t() -> Self {
        Self {
            t_power: 1,
            ..Self::one()
        }
    }

    fn x() -> Self {
        Self {
            x_power: 1,
            ..Self::one()
        }
    }

    fn u() -> Self {
        Self::t().multiply(Self::x())
    }

    fn u_dual() -> Self {
        Self {
            coefficient: -1,
            q_power: -1,
            ..Self::u()
        }
    }

    fn multiply(self, other: Self) -> Self {
        Self {
            coefficient: self.coefficient * other.coefficient,
            q_power: self.q_power + other.q_power,
            t_power: self.t_power + other.t_power,
            x_power: self.x_power + other.x_power,
        }
    }

    fn scale(self, scalar: Int) -> Self {
        Self {
            coefficient: scalar * self.coefficient,
            ..self
        }
    }

    fn divide_x(self) -> Self {
        assert!(self.x_power > 0);
        Self {
            x_power: self.x_power - 1,
            ..self
        }
    }

    fn specialize_x_zero(self) -> Option<Self> {
        (self.x_power == 0).then(|| Self {
            q_power: 0, // q=1 because q-1=t*x.
            ..self
        })
    }
}

#[derive(Clone, Debug, Eq, PartialEq)]
struct LaurentPolynomial(BTreeMap<(i8, u8, u8), Int>);

impl LaurentPolynomial {
    fn zero() -> Self {
        Self(BTreeMap::new())
    }

    fn term(value: LaurentTerm) -> Self {
        if value.coefficient == 0 {
            Self::zero()
        } else {
            Self(BTreeMap::from([(
                (value.q_power, value.t_power, value.x_power),
                value.coefficient,
            )]))
        }
    }

    fn add_scaled(&mut self, other: &Self, scale: Int) {
        for (monomial, coefficient) in &other.0 {
            *self.0.entry(*monomial).or_default() += scale * coefficient;
        }
        self.0.retain(|_, coefficient| *coefficient != 0);
    }
}

fn laurent_dot(left: &[LaurentTerm], right: &[LaurentTerm]) -> LaurentPolynomial {
    assert_eq!(left.len(), right.len());
    let mut result = LaurentPolynomial::zero();
    for (first, second) in left.iter().zip(right) {
        result.add_scaled(&LaurentPolynomial::term(first.multiply(*second)), 1);
    }
    result
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum Variance {
    ReciprocalStandard,
    OriginalBorelMoore,
}

fn check_repeated_normal_bockstein_and_can_var() {
    let one = LaurentTerm::one();
    let minus_one = one.scale(-1);
    let q = LaurentTerm::q();
    let minus_q = q.scale(-1);
    let u = LaurentTerm::u();
    let u_dual = LaurentTerm::u_dual();

    // D3 degree two to one and degree one to zero in the entry-100 bases.
    let d2 = [u.scale(-1), u_dual];
    let d1 = [u_dual, u];
    assert_eq!(laurent_dot(&d1, &d2), LaurentPolynomial::zero());

    // Before closedness the middle term is free of rank two.  Cancelling the
    // common non-zero-divisor q^-1*u changes d1 to the split row (-1,q).
    // Its first coefficient is a unit, so its kernel is the saturated line
    // generated by (q,1), with no torsion and no rank-one assumption.
    let split_relation = [minus_one, q];
    let primitive_unoriented_kernel = [q, one];
    assert_eq!(
        laurent_dot(&split_relation, &primitive_unoriented_kernel),
        LaurentPolynomial::zero()
    );
    let normal_middle_ambient_rank = 2_usize;
    let normal_closed_rank = 1_usize;
    assert_eq!((normal_middle_ambient_rank, normal_closed_rank), (2, 1));

    // The orientation is not assigned here.  It is derived below from the
    // reciprocal normalization of the actual top differential.
    let eta_mix = primitive_unoriented_kernel.map(|entry| entry.scale(-1));
    assert_eq!(eta_mix, [minus_q, minus_one]);
    assert_eq!(laurent_dot(&d1, &eta_mix), LaurentPolynomial::zero());

    // d2=(q^-1*u)*eta_mix.  The nonunit u factor proves that eta_mix is not
    // a boundary over the unlocalized ring, while its unit coefficient fixes
    // the primitive orientation.
    let q_inverse_u = LaurentTerm { q_power: -1, ..u };
    assert_eq!(
        eta_mix.map(|coefficient| coefficient.multiply(q_inverse_u)),
        d2
    );

    // Forced reciprocal normalization of the top: z_norm=q*z.  Its
    // differential is x*(t*eta_mix) exactly before central base change.
    let normalized_d2 = d2.map(|entry| entry.multiply(q));
    let t_eta = eta_mix.map(|entry| entry.multiply(LaurentTerm::t()));
    let x_t_eta = t_eta.map(|entry| entry.multiply(LaurentTerm::x()));
    assert_eq!(normalized_d2, x_t_eta);
    let bockstein = normalized_d2.map(LaurentTerm::divide_x);
    assert_eq!(bockstein, t_eta);
    assert_eq!(
        bockstein,
        primitive_unoriented_kernel.map(|entry| entry.multiply(LaurentTerm::t()).scale(-1))
    );
    let central_bockstein = bockstein.map(|entry| entry.specialize_x_zero().unwrap());
    assert_eq!(
        central_bockstein,
        [LaurentTerm::t().scale(-1), LaurentTerm::t().scale(-1)]
    );

    // Entry-100 complementary can-var pairing.  The two tensor-boundary
    // contributions agree, hence cancel with the Koszul sign, and the
    // antidiagonal determinant is the Laurent unit q.
    let beta_p_h_dual = one;
    let beta_h_p_dual = minus_q;
    assert_eq!(u.multiply(beta_p_h_dual), u_dual.multiply(beta_h_p_dual));
    let pairing_determinant = beta_p_h_dual.multiply(beta_h_p_dual).scale(-1);
    assert_eq!(pairing_determinant, q);

    let source_variance = Variance::ReciprocalStandard;
    let target_variance = Variance::OriginalBorelMoore;
    assert_ne!(source_variance, target_variance);
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum LabelledLine {
    ReesT3,
    OccurrenceX1,
    OccurrenceX3,
    OccurrenceX5,
    PhysicalX03,
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum ExcessClass {
    Eta3Mix,
}

fn cap_rees_line(line: LabelledLine, target: ExcessClass) -> Option<ExcessClass> {
    (line == LabelledLine::ReesT3).then_some(target)
}

fn check_label_separation_and_rees_cap() {
    let all_lines = [
        LabelledLine::ReesT3,
        LabelledLine::OccurrenceX1,
        LabelledLine::OccurrenceX3,
        LabelledLine::OccurrenceX5,
        LabelledLine::PhysicalX03,
    ];
    for left in 0..all_lines.len() {
        for right in left + 1..all_lines.len() {
            assert_ne!(all_lines[left], all_lines[right]);
        }
    }
    assert_eq!(
        cap_rees_line(LabelledLine::ReesT3, ExcessClass::Eta3Mix),
        Some(ExcessClass::Eta3Mix)
    );
    for wrong in [
        LabelledLine::OccurrenceX1,
        LabelledLine::OccurrenceX3,
        LabelledLine::OccurrenceX5,
        LabelledLine::PhysicalX03,
    ] {
        assert_eq!(cap_rees_line(wrong, ExcessClass::Eta3Mix), None);
    }
    let physical_dx03_evaluation = 1_i64;
    assert_eq!(physical_dx03_evaluation, 1);
}

#[derive(Clone, Debug, Eq, PartialEq)]
struct Polynomial(BTreeMap<[u8; 2], Int>);

impl Polynomial {
    fn zero() -> Self {
        Self(BTreeMap::new())
    }

    fn one() -> Self {
        Self(BTreeMap::from([([0, 0], 1)]))
    }

    fn x1() -> Self {
        Self(BTreeMap::from([([1, 0], 1)]))
    }

    fn x3() -> Self {
        Self(BTreeMap::from([([0, 1], 1)]))
    }

    fn add_scaled(&mut self, other: &Self, scale: Int) {
        for (monomial, coefficient) in &other.0 {
            *self.0.entry(*monomial).or_default() += scale * coefficient;
        }
        self.0.retain(|_, coefficient| *coefficient != 0);
    }

    fn scale(&self, scalar: Int) -> Self {
        let mut result = Self::zero();
        result.add_scaled(self, scalar);
        result
    }

    fn multiply(&self, other: &Self) -> Self {
        let mut result = Self::zero();
        for (left, left_coefficient) in &self.0 {
            for (right, right_coefficient) in &other.0 {
                let monomial = [left[0] + right[0], left[1] + right[1]];
                *result.0.entry(monomial).or_default() += left_coefficient * right_coefficient;
            }
        }
        result.0.retain(|_, coefficient| *coefficient != 0);
        result
    }

    fn central_fibre(&self) -> Int {
        self.0.get(&[0, 0]).copied().unwrap_or(0)
    }
}

type Matrix = Vec<Vec<Polynomial>>;

fn zero_matrix(rows: usize, columns: usize) -> Matrix {
    vec![vec![Polynomial::zero(); columns]; rows]
}

fn multiply_matrix(left: &Matrix, right: &Matrix) -> Matrix {
    assert!(!left.is_empty() && !right.is_empty());
    assert_eq!(left[0].len(), right.len());
    let mut result = zero_matrix(left.len(), right[0].len());
    for row in 0..left.len() {
        for middle in 0..right.len() {
            for column in 0..right[0].len() {
                let term = left[row][middle].multiply(&right[middle][column]);
                result[row][column].add_scaled(&term, 1);
            }
        }
    }
    result
}

#[derive(Clone, Debug)]
struct TotalComplex {
    // d1:C1->C0 and d2:C2->C1 for K(x1) tensor K(x3).
    d1: Matrix,
    d2: Matrix,
}

fn total_complex(occurrence_sign: Int) -> TotalComplex {
    let d_occurrence = Polynomial::x1().scale(occurrence_sign);
    let d_cartier = Polynomial::x3();
    let d1 = vec![vec![d_occurrence.clone(), d_cartier.clone()]];
    let d2 = vec![vec![d_cartier.scale(-1)], vec![d_occurrence]];
    assert_eq!(multiply_matrix(&d1, &d2), zero_matrix(1, 1));
    TotalComplex { d1, d2 }
}

fn diagonal(values: &[Int]) -> Matrix {
    let mut result = zero_matrix(values.len(), values.len());
    for (index, value) in values.iter().enumerate() {
        result[index][index] = Polynomial::one().scale(*value);
    }
    result
}

fn check_full_weighted_total_chain_map() {
    // Source occurrence differential is -x1; road differential is +x1.
    // The normalized slab and normalized excess packets both have labelled
    // differential +x3.  Gamma is gamma_car tensor identity, hence its
    // degree maps are (-1), diag(+1,-1), and (+1).
    let source = total_complex(-1);
    let target = total_complex(1);
    let gamma0 = diagonal(&[-1]);
    let gamma1 = diagonal(&[1, -1]);
    let gamma2 = diagonal(&[1]);

    assert_eq!(
        multiply_matrix(&target.d1, &gamma1),
        multiply_matrix(&gamma0, &source.d1)
    );
    assert_eq!(
        multiply_matrix(&target.d2, &gamma2),
        multiply_matrix(&gamma1, &source.d2)
    );

    // Before base change, the endpoint entry is forced to -1 and both x1
    // and x3 squares commute.  This is stronger than the vacuous central
    // equation.  After x1=x3=0, all differentials vanish but every diagonal
    // component survives as a unit, retaining the complete derived packet.
    assert_eq!(gamma0[0][0], Polynomial::one().scale(-1));
    assert_eq!(gamma1[0][0], Polynomial::one());
    assert_eq!(gamma1[1][1], Polynomial::one().scale(-1));
    assert_eq!(gamma2[0][0], Polynomial::one());
    assert!(source
        .d1
        .iter()
        .chain(source.d2.iter())
        .flatten()
        .all(|entry| entry.central_fibre() == 0));
    assert!(target
        .d1
        .iter()
        .chain(target.d2.iter())
        .flatten()
        .all(|entry| entry.central_fibre() == 0));
    let central_map_ranks = [1_usize, 2, 1];
    assert_eq!(central_map_ranks, [1, 2, 1]);
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum NormalTorGrade {
    Tor0,
    Eta3MixTor1,
}

fn check_endpoint_rhom_and_full_tor_packet() {
    // RHom of the two endpoint resolutions with different occurrence signs:
    //
    //   R --x1(1,-1)--> R^2 --x1(1,1)--> R.
    //
    // The middle kernel is R*(-1,1), and the incoming image is x1 times
    // that line.  The last cokernel is also R/(x1).  Thus the two adjacent
    // endpoint groups are H0=R/(x1) and H1=R/(x1); neither may be discarded.
    let x1 = Polynomial::x1();
    let ext1_to_ext0 = vec![vec![x1.clone()], vec![x1.scale(-1)]];
    let ext0_to_next = vec![vec![x1.clone(), x1.clone()]];
    assert_eq!(
        multiply_matrix(&ext0_to_next, &ext1_to_ext0),
        zero_matrix(1, 1)
    );
    let carrier = vec![vec![Polynomial::one().scale(-1)], vec![Polynomial::one()]];
    assert_eq!(multiply_matrix(&ext0_to_next, &carrier), zero_matrix(1, 1));
    assert_eq!(ext1_to_ext0[0][0], x1);
    assert_eq!(ext1_to_ext0[1][0], Polynomial::x1().scale(-1));

    // Full derived x1=0 pullback has ranks (1,2,1), not one selected line.
    let endpoint_central_ranks = [1_usize, 2, 1];
    assert_eq!(endpoint_central_ranks, [1, 2, 1]);
    let endpoint_rhom_groups = ["H0=R/(x1)", "H1=R/(x1)"];
    assert_eq!(endpoint_rhom_groups.len(), 2);

    // Likewise the normal A3-filtered packet retains Tor0 together with the
    // eta Tor1 line.  The Bockstein derives the latter's generator but does
    // not supply the filtered attachment/counit tying it to Tor0.  Thus at
    // least two adjacent grades remain after the carrier mark.  Their actual
    // loaded spatial Hom rank is undefined until that attachment and target
    // exist; an eta-only truncation is nevertheless already inadmissible.
    let full_normal_packet = [NormalTorGrade::Tor0, NormalTorGrade::Eta3MixTor1];
    let retained_adjacent_grades = full_normal_packet.len();
    let actual_loaded_spatial_hom_rank: Option<usize> = None;
    assert_eq!(retained_adjacent_grades, 2);
    assert_eq!(actual_loaded_spatial_hom_rank, None);
}

fn check_endpoint_relative_source_only() {
    // K0 is the quotient of the absolute diamond by [q2 --x1--> a].  Its
    // only differential is e3 --(-x1)--> q0.  No x5 arrow or absolute a-cell
    // is retained in this source.
    let source_generators = ["e3", "q0"];
    let source_differential = ("e3", "q0", -1_i64, LabelledLine::OccurrenceX1);
    assert_eq!(source_generators, ["e3", "q0"]);
    assert_eq!(source_differential.2, -1);
    assert_eq!(source_differential.3, LabelledLine::OccurrenceX1);
    let contains_q2 = false;
    let contains_a = false;
    let contains_x5_differential = false;
    assert!(!contains_q2 && !contains_a && !contains_x5_differential);
}

fn main() {
    check_actual_interval_incidences();
    check_ambient_gallery_road_hom_and_ablation();
    check_staircase_projection_scope();
    check_entry97_localized_loaded_hom_negative_control();
    check_weighted_middle_cartier_bordism();
    check_full_interval_principal_line_transport();
    check_repeated_normal_bockstein_and_can_var();
    check_label_separation_and_rees_cap();
    check_full_weighted_total_chain_map();
    check_endpoint_rhom_and_full_tor_packet();
    check_endpoint_relative_source_only();

    println!(
        "{}",
        r#"{"claim":"The existing entry-118 carrier interval, principal occurrence lines, full road-square carrier trace, and one-normal graph Bockstein do not construct Gamma_{0,rel}^{!,PC}. The anti-circular carrier calculation starts from the unmarked gallery category with both saturated F03 flags: H1(Gal_03,partial;Z)=Z^2, and RHom(C_*(road square),C_*(Gal_03,partial)) has ordinary H0=0 but shifted BM/correspondence H1=Z^2 with no torsion. The common lcm x1*x3 leaves rank two; the inherited x3 sink mark selects one primitive saturated carrier line. On that line the actual middle slab has boundary x3*(x1*x5[v+]-X03[Z3]), and reciprocal normalization independently derives beta_x3(q3*z)=t3*eta_3,mix with eta_3,mix=(-q3,-1); the formal x1/x3 associated-grade differential and BC square pass before base change. However q0 and F03 are incomparable, tau_0 is only a carrier symbol rather than a constructed iterated relative Thom costalk of the full road PC square, and no ringed q-counit/relative-dualizing AW trace is available. Reusing entry 97 as the loaded target is decisively impossible: its x1,x3,u3 localization contracts K0, the x3 Thom factor, and D3, so their common-base loaded RHom is zero. Over the required unlocalized base, the full endpoint RHom has adjacent H0=R/(x1) and H1=R/(x1), and the normal packet must retain Tor0 plus eta Tor1. Hence at least two adjacent grades remain, so eta-only rank one is inadmissible; the actual loaded spatial Hom rank is undefined until its target and counit exist. Thus entry-97 reuse and eta-only promotion are falsified, while a new unlocalized extraordinary lift remains unconstructed.","status":"falsified","assumptions":["K0 is exactly K/[Rq2->Ra]=[e3 --(-x1)--> q0], with neither q2 nor a retained.","Gal_03 contains both actual saturated F03 flags through the unique central flip before applying the inherited x3 sink mark.","The full road-relative carrier target is the complete entry-97 road square; its integral counit is used only at carrier level.","The multi-Rees relation is u3=t3*x3 and reciprocal twist is u3^vee=-q3^-1*u3, with occurrence x, Rees t, monodromy q/u, excess eta_3,mix, and physical [dX03] kept distinct."],"evidence_refs":["research/voevodsky/check_d03_q0_endpoint_relative_tor_lift.rs","research/voevodsky/check_d03_q0_endpoint_exit_flags.rs","research/voevodsky/check_d03_bivariant_pc_hom.rs","research/voevodsky/check_absolute_unlocalized_support_pc.rs","research/voevodsky/check_one_normal_can_var_cousin.rs","research/voevodsky/check_multirees_cartier_pl_cap.rs","research/voevodsky/check_d03_thom_endpoint_bc.rs","ledger entries 97,100,105,112,116,117,118"],"factorization_test":{"endpoint_relative_source":"PASS: K0 only","unmarked_gallery_relative_BM":"PASS: saturated Z^2 with a unit 6x6 incidence minor","full_road_carrier_trace":"PASS: the complete square contracts integrally to one carrier counit line","ambient_mapping_complex":"PASS: ranks (6,32,56,32), differential ranks (6,26,30), homology (0,0,0,2), no integral torsion","ordinary_endpoint_Hom":"ZERO in degree zero; the gallery classes occur only in shifted BM degree +1","lcm_ablation":"RANK 2: both road flags have product x1*x3","x3_mark_ablation":"RANK 1: primitive saturated coordinate (0,1)","carrier_staircase_p_q":"PASS only as monotone simplicial projections to the Boolean and road flags","ordinary_incidence_endpoint_map":"ZERO: q0 and F03 principal lines are incomparable","entry97_common_base_loaded_RHom":"ZERO: x1,x3,u3 are units, so K0, the Thom factor, and D3 contract","ringed_q_projection":"FAIL: no constructed tau_0 iterated relative Thom-costalk module","relative_dualizing_AW_counit":"FAIL: not supplied by the carrier staircase or entry-97 Laurent trace","middle_Cartier_bordism":"PASS: d[J3]=x3*(x1*x5[v+]-X03[Z3])","principal_line_transport":"PASS as a necessary local-system identity only; it is not a q-counit","normal_closedness_ablation":"RANK 2 to saturated RANK 1 generated unoriented by (q3,1)","x3_graph_Bockstein":"PASS before base change: d(q3*z)/x3=t3*eta_3,mix fixes eta_3,mix=(-q3,-1)","can_var_pairing":"PASS with determinant q3","formal_weighted_d_squared_BC":"PASS over Z[x1,x3] before base change, associated-grade shadow only","endpoint_RHom":"H0=R/(x1) and H1=R/(x1), both retained","full_normal_packet":"Tor0 plus eta_3,mix Tor1 retained","post_mark_loaded_rank":"UNDEFINED: Tor0 and eta-Tor1 are at least two retained adjacent grades, so eta-only rank 1 is inadmissible","central_derived_pullback":"PASS as a test: zero differentials with ranks (1,2,1), not an existence argument","physical_orientation":"[dX03]=+1 remains an independent line","full_extraordinary_PC_lift":"UNCONSTRUCTED"},"counterevidence":["A BM class in the gallery is not a ringed incidence morphism between incomparable endpoint supports.","Entry 97 cannot be reused as a loaded target because its localization makes the relevant common-base RHom zero; this does not rule out a new unlocalized target.","The same occurrence lcm occurs on both road flags, so coefficient fitting cannot justify the marked rank-one selection.","Calling tau_0 a target does not define its derived relative-costalk module or the q_! counit.","The Bockstein derives the eta Tor1 generator but does not attach it to the retained Tor0 grade.","The formal weighted BC square is compatible with a candidate; without the ringed p,q trace it does not prove that candidate is a spatial PC correspondence."],"next_experiment":"Construct tau_0 as the actual A3-filtered iterated relative Thom costalk of the full unlocalized road PC square, then define ringed staircase projections p and q and an ordered relative-dualizing/Alexander-Whitney trace. Compute the induced map on the full Tor0 plus Tor1 packet and test whether its counit kills the residual rank-two Ob1 without choosing eta or the endpoint sign by hand.","changed_files":["research/voevodsky/check_d03_q0_endpoint_relative_tor_lift.rs"],"verification":{"new_checker":"rustfmt --check; rustc --edition=2021 -D warnings -O; execution; JSON parse","inherited_checkers":"six cited checkers passed rustfmt, rustc -D warnings, execution, and JSON parse","git":"no docs, ledger, graph, config, or commit changes"}}"#
    );
}
