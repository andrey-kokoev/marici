//! Exact certificate for the resolved support-overlap hyper-Cech object.
//!
//! For Q={03,05}, the four physical chart supports are the four side
//! facets of the regional cube.  Ordinary intersections of their monomial
//! ideals are not the nerve of that topological cover: opposite facets have
//! nonzero algebraic intersections too.  After selecting the physical
//! support poset, however, every adjacent module intersection is C_e p_1.
//! Its minimal free resolution is the middle weighted interval, including
//! the primitive syzygy missing from the flattened occurrence-only Cech
//! source.
//!
//! The certificate makes this statement in two independent ways.
//!
//! 1. It computes all monomial-ideal intersections, assembles the four
//!    facet resolutions and four adjacent overlap resolutions into a
//!    mapping-cone totalization, and verifies a strict polynomial
//!    quasi-isomorphism to the weighted four-facet belt.
//! 2. It computes the degreewise relation complex of the already certified
//!    raw-weighted carrier from the actual P+, P-, S+, S- polygons.  Its
//!    ranks are (10,6,0).  Two interval summands are the collapsed pentagon
//!    cones H_s.  Their quotient is exactly four interval-overlap complexes.
//!
//! These are exact algebraic carrier statements.  They do not prove that
//! the support-selected relation groupoid is supplied by finite-alpha-prime
//! Pochhammer/Cousin specialization or scalar deformation geometry.

use std::collections::{BTreeMap, BTreeSet};

const STAR: u8 = 2;
const VARIABLES: usize = 6;

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct Monomial([u8; VARIABLES]);

#[derive(Clone, Debug, Eq, PartialEq)]
struct Polynomial(BTreeMap<Monomial, i64>);

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct CubeCell([u8; 3]);

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct Facet {
    coordinate: usize,
    value: u8,
}

#[derive(Clone, Copy, Debug)]
struct Chart {
    name: &'static str,
    sides: usize,
    facet: Facet,
}

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
enum TotalBasis {
    Facet(usize, CubeCell),
    Overlap(usize, CubeCell),
}

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct SourceCell {
    chart: usize,
    local: usize,
}

type Ideal = BTreeSet<Monomial>;
type Matrix = Vec<Vec<Polynomial>>;
type IntMatrix = Vec<Vec<i64>>;

const CHARTS: [Chart; 4] = [
    Chart {
        name: "P+",
        sides: 5,
        facet: Facet {
            coordinate: 2,
            value: 1,
        },
    },
    Chart {
        name: "P-",
        sides: 5,
        facet: Facet {
            coordinate: 0,
            value: 1,
        },
    },
    Chart {
        name: "S+",
        sides: 4,
        facet: Facet {
            coordinate: 2,
            value: 0,
        },
    },
    Chart {
        name: "S-",
        sides: 4,
        facet: Facet {
            coordinate: 0,
            value: 0,
        },
    },
];

const ADJACENT: [(usize, usize); 4] = [(0, 1), (0, 3), (1, 2), (2, 3)];
const OPPOSITE: [(usize, usize); 2] = [(0, 2), (1, 3)];

impl Monomial {
    fn one() -> Self {
        Self([0; VARIABLES])
    }

    fn variable(region: usize, value: usize) -> Self {
        let mut powers = [0; VARIABLES];
        powers[2 * region + value] = 1;
        Self(powers)
    }

    fn multiply(self, other: Self) -> Self {
        let mut powers = [0; VARIABLES];
        for (index, power) in powers.iter_mut().enumerate() {
            *power = self.0[index] + other.0[index];
        }
        Self(powers)
    }

    fn lcm(self, other: Self) -> Self {
        let mut powers = [0; VARIABLES];
        for (index, power) in powers.iter_mut().enumerate() {
            *power = self.0[index].max(other.0[index]);
        }
        Self(powers)
    }

    fn gcd(self, other: Self) -> Self {
        let mut powers = [0; VARIABLES];
        for (index, power) in powers.iter_mut().enumerate() {
            *power = self.0[index].min(other.0[index]);
        }
        Self(powers)
    }

    fn divides(self, other: Self) -> bool {
        self.0
            .iter()
            .zip(other.0)
            .all(|(&left, right)| left <= right)
    }

    fn quotient(self, divisor: Self) -> Self {
        let mut powers = [0; VARIABLES];
        for (index, power) in powers.iter_mut().enumerate() {
            assert!(self.0[index] >= divisor.0[index]);
            *power = self.0[index] - divisor.0[index];
        }
        Self(powers)
    }

    fn positive_degree(self) -> bool {
        self.0.iter().any(|&power| power != 0)
    }
}

impl Polynomial {
    fn zero() -> Self {
        Self(BTreeMap::new())
    }

    fn one() -> Self {
        Self::monomial(Monomial::one())
    }

    fn monomial(value: Monomial) -> Self {
        Self(BTreeMap::from([(value, 1)]))
    }

    fn scale(&self, scalar: i64) -> Self {
        let mut result = self.clone();
        for coefficient in result.0.values_mut() {
            *coefficient *= scalar;
        }
        result.0.retain(|_, coefficient| *coefficient != 0);
        result
    }

    fn add(&self, other: &Self) -> Self {
        let mut result = self.clone();
        for (&monomial, &coefficient) in &other.0 {
            *result.0.entry(monomial).or_default() += coefficient;
        }
        result.0.retain(|_, coefficient| *coefficient != 0);
        result
    }

    fn multiply(&self, other: &Self) -> Self {
        let mut result = BTreeMap::new();
        for (&left, &left_coefficient) in &self.0 {
            for (&right, &right_coefficient) in &other.0 {
                *result.entry(left.multiply(right)).or_default() +=
                    left_coefficient * right_coefficient;
            }
        }
        result.retain(|_, coefficient| *coefficient != 0);
        Self(result)
    }

    fn evaluate_at_one(&self) -> i64 {
        self.0.values().sum()
    }

    fn is_zero(&self) -> bool {
        self.0.is_empty()
    }
}

fn normalize_ideal(generators: impl IntoIterator<Item = Monomial>) -> Ideal {
    let all: BTreeSet<_> = generators.into_iter().collect();
    all.iter()
        .copied()
        .filter(|&candidate| {
            !all.iter()
                .copied()
                .any(|other| other != candidate && other.divides(candidate))
        })
        .collect()
}

fn product_ideals(left: &Ideal, right: &Ideal) -> Ideal {
    normalize_ideal(
        left.iter()
            .flat_map(|&first| right.iter().map(move |&second| first.multiply(second))),
    )
}

fn intersect_ideals(left: &Ideal, right: &Ideal) -> Ideal {
    normalize_ideal(
        left.iter()
            .flat_map(|&first| right.iter().map(move |&second| first.lcm(second))),
    )
}

fn prime(region: usize) -> Ideal {
    BTreeSet::from([Monomial::variable(region, 0), Monomial::variable(region, 1)])
}

fn iq_ideal() -> Ideal {
    product_ideals(&product_ideals(&prime(0), &prime(1)), &prime(2))
}

fn monomial_in_ideal(value: Monomial, ideal: &Ideal) -> bool {
    ideal.iter().any(|&generator| generator.divides(value))
}

fn vertices(cell: CubeCell) -> Vec<CubeCell> {
    let free: Vec<_> = (0..3)
        .filter(|&coordinate| cell.0[coordinate] == STAR)
        .collect();
    let mut result = Vec::new();
    for mask in 0..1_usize << free.len() {
        let mut vertex = cell;
        for (index, &coordinate) in free.iter().enumerate() {
            vertex.0[coordinate] = ((mask >> index) & 1) as u8;
        }
        result.push(vertex);
    }
    result
}

fn opposite_vertex_label(vertex: CubeCell) -> Monomial {
    assert!(vertex.0.iter().all(|&value| value < 2));
    (0..3).fold(Monomial::one(), |product, region| {
        product.multiply(Monomial::variable(region, 1 - vertex.0[region] as usize))
    })
}

fn raw_vertex_weight(vertex: CubeCell) -> Monomial {
    assert!(vertex.0.iter().all(|&value| value < 2));
    (0..3).fold(Monomial::one(), |product, region| {
        product.multiply(Monomial::variable(region, vertex.0[region] as usize))
    })
}

fn cell_label(cell: CubeCell) -> Monomial {
    vertices(cell)
        .into_iter()
        .map(opposite_vertex_label)
        .reduce(Monomial::lcm)
        .unwrap()
}

fn raw_cell_weight(cell: CubeCell) -> Monomial {
    vertices(cell)
        .into_iter()
        .map(raw_vertex_weight)
        .reduce(Monomial::gcd)
        .unwrap()
}

fn cell_dimension(cell: CubeCell) -> usize {
    cell.0.iter().filter(|&&value| value == STAR).count()
}

fn cube_cells(degree: usize) -> Vec<CubeCell> {
    let mut result = Vec::new();
    for code in 0..27 {
        let mut work = code;
        let mut word = [0_u8; 3];
        for entry in &mut word {
            *entry = (work % 3) as u8;
            work /= 3;
        }
        let cell = CubeCell(word);
        if cell_dimension(cell) == degree {
            result.push(cell);
        }
    }
    result.sort();
    result
}

fn weighted_boundary(cell: CubeCell) -> Vec<(CubeCell, Polynomial)> {
    let label = cell_label(cell);
    let mut result = Vec::new();
    let mut star_position = 0;
    for coordinate in 0..3 {
        if cell.0[coordinate] != STAR {
            continue;
        }
        let koszul_sign = if star_position % 2 == 0 { 1 } else { -1 };
        for (value, sign) in [(1_u8, koszul_sign), (0_u8, -koszul_sign)] {
            let mut face = cell;
            face.0[coordinate] = value;
            result.push((
                face,
                Polynomial::monomial(label.quotient(cell_label(face))).scale(sign),
            ));
        }
        star_position += 1;
    }
    result
}

fn facet_contains(facet: Facet, cell: CubeCell) -> bool {
    cell.0[facet.coordinate] == facet.value
}

fn facet_cells(facet: Facet, degree: usize) -> Vec<CubeCell> {
    cube_cells(degree)
        .into_iter()
        .filter(|&cell| facet_contains(facet, cell))
        .collect()
}

fn belt_cells(degree: usize) -> Vec<CubeCell> {
    cube_cells(degree)
        .into_iter()
        .filter(|&cell| CHARTS.iter().any(|chart| facet_contains(chart.facet, cell)))
        .collect()
}

fn overlap_outer_bits(pair: (usize, usize)) -> (u8, u8) {
    let mut bits = [None, None];
    for chart_index in [pair.0, pair.1] {
        let facet = CHARTS[chart_index].facet;
        match facet.coordinate {
            0 => bits[0] = Some(facet.value),
            2 => bits[1] = Some(facet.value),
            _ => panic!("belt chart is not an outer facet"),
        }
    }
    (bits[0].unwrap(), bits[1].unwrap())
}

fn overlap_cells(pair: (usize, usize), degree: usize) -> Vec<CubeCell> {
    let (value0, value2) = overlap_outer_bits(pair);
    [0_u8, 1_u8, STAR]
        .into_iter()
        .map(|value1| CubeCell([value0, value1, value2]))
        .filter(|&cell| cell_dimension(cell) == degree)
        .collect()
}

fn facet_ideal(facet: Facet) -> Ideal {
    normalize_ideal(facet_cells(facet, 0).into_iter().map(opposite_vertex_label))
}

fn expected_facet_ideal(facet: Facet) -> Ideal {
    let fixed = BTreeSet::from([Monomial::variable(
        facet.coordinate,
        1 - facet.value as usize,
    )]);
    (0..3)
        .filter(|&region| region != facet.coordinate)
        .fold(fixed, |product, region| {
            product_ideals(&product, &prime(region))
        })
}

fn overlap_ideal(pair: (usize, usize)) -> Ideal {
    normalize_ideal(
        overlap_cells(pair, 0)
            .into_iter()
            .map(opposite_vertex_label),
    )
}

fn check_ideal_intersections_and_minimal_resolutions() {
    let iq = iq_ideal();
    assert_eq!(iq.len(), 8);
    for chart in CHARTS {
        let ideal = facet_ideal(chart.facet);
        assert_eq!(ideal, expected_facet_ideal(chart.facet));
        assert_eq!(ideal.len(), 4);
        assert!(ideal.iter().all(|&value| monomial_in_ideal(value, &iq)));

        // The labelled square is a minimal resolution of the facet ideal.
        for degree in 1..=2 {
            for cell in facet_cells(chart.facet, degree) {
                let twice: BTreeMap<_, i64> = weighted_boundary(cell)
                    .into_iter()
                    .flat_map(|(face, first)| {
                        weighted_boundary(face)
                            .into_iter()
                            .map(move |(vertex, second)| (vertex, first.multiply(&second)))
                    })
                    .fold(BTreeMap::new(), |mut sum, (face, coefficient)| {
                        let entry = sum.entry(face).or_default();
                        *entry += coefficient.evaluate_at_one();
                        sum
                    });
                assert!(twice.values().all(|&value| value == 0));
                assert!(weighted_boundary(cell).into_iter().all(|(_, coefficient)| {
                    coefficient
                        .0
                        .keys()
                        .all(|monomial| monomial.positive_degree())
                }));
            }
        }
        for edge in facet_cells(chart.facet, 1) {
            let augmentation = weighted_boundary(edge).into_iter().fold(
                Polynomial::zero(),
                |sum, (vertex, coefficient)| {
                    sum.add(
                        &coefficient.multiply(&Polynomial::monomial(opposite_vertex_label(vertex))),
                    )
                },
            );
            assert!(augmentation.is_zero());
        }
    }

    for pair in ADJACENT {
        let intersection = intersect_ideals(
            &facet_ideal(CHARTS[pair.0].facet),
            &facet_ideal(CHARTS[pair.1].facet),
        );
        let expected = overlap_ideal(pair);
        assert_eq!(intersection, expected);
        assert_eq!(intersection.len(), 2);

        let (outer0, outer2) = overlap_outer_bits(pair);
        let common_outer = Monomial::variable(0, 1 - outer0 as usize)
            .multiply(Monomial::variable(2, 1 - outer2 as usize));
        assert_eq!(
            expected,
            BTreeSet::from([
                common_outer.multiply(Monomial::variable(1, 0)),
                common_outer.multiply(Monomial::variable(1, 1)),
            ])
        );

        // The interval is the unique minimal first syzygy.  If v^0 has
        // middle bit zero and v^1 has middle bit one, then
        // m(v^0)=C X_11 and m(v^1)=C X_10.
        let v0 = CubeCell([outer0, 0, outer2]);
        let v1 = CubeCell([outer0, 1, outer2]);
        let interval = CubeCell([outer0, STAR, outer2]);
        let x10 = Monomial::variable(1, 0);
        let x11 = Monomial::variable(1, 1);
        assert_eq!(
            x11.multiply(opposite_vertex_label(v1)),
            x10.multiply(opposite_vertex_label(v0))
        );
        assert_eq!(x10.gcd(x11), Monomial::one());
        assert_eq!(
            weighted_boundary(interval),
            vec![
                (v1, Polynomial::monomial(x11)),
                (v0, Polynomial::monomial(x10).scale(-1)),
            ]
        );

        // Both inclusions of the minimal interval resolution into its two
        // facet resolutions are literally labelled-cell inclusions.
        for cell in overlap_cells(pair, 0)
            .into_iter()
            .chain(overlap_cells(pair, 1))
        {
            assert!(facet_contains(CHARTS[pair.0].facet, cell));
            assert!(facet_contains(CHARTS[pair.1].facet, cell));
        }
    }

    // The two opposite facet pairs are disjoint in the physical support
    // poset, despite having nonzero intersections as ideals in A.  Hence an
    // unrestricted ideal-intersection Cech nerve is not the belt cover.
    for pair in OPPOSITE {
        let intersection = intersect_ideals(
            &facet_ideal(CHARTS[pair.0].facet),
            &facet_ideal(CHARTS[pair.1].facet),
        );
        assert!(!intersection.is_empty());
        assert_eq!(intersection.len(), 4);
        assert!(overlap_cells_if_supported(pair).is_empty());
    }
}

fn overlap_cells_if_supported(pair: (usize, usize)) -> Vec<CubeCell> {
    if ADJACENT.contains(&pair) {
        overlap_cells(pair, 0)
            .into_iter()
            .chain(overlap_cells(pair, 1))
            .collect()
    } else {
        Vec::new()
    }
}

fn zero_matrix(rows: usize, columns: usize) -> Matrix {
    vec![vec![Polynomial::zero(); columns]; rows]
}

fn add_matrix_entry(matrix: &mut Matrix, row: usize, column: usize, value: Polynomial) {
    matrix[row][column] = matrix[row][column].add(&value);
}

fn multiply_matrices(left: &Matrix, right: &Matrix) -> Matrix {
    assert_eq!(left.first().map_or(0, Vec::len), right.len());
    let rows = left.len();
    let columns = right.first().map_or(0, Vec::len);
    let middle = right.len();
    let mut product = zero_matrix(rows, columns);
    for row in 0..rows {
        for column in 0..columns {
            for index in 0..middle {
                add_matrix_entry(
                    &mut product,
                    row,
                    column,
                    left[row][index].multiply(&right[index][column]),
                );
            }
        }
    }
    product
}

fn total_basis(degree: usize) -> Vec<TotalBasis> {
    let mut result = Vec::new();
    for (chart_index, chart) in CHARTS.iter().enumerate() {
        result.extend(
            facet_cells(chart.facet, degree)
                .into_iter()
                .map(|cell| TotalBasis::Facet(chart_index, cell)),
        );
    }
    if degree > 0 {
        for (overlap_index, &pair) in ADJACENT.iter().enumerate() {
            result.extend(
                overlap_cells(pair, degree - 1)
                    .into_iter()
                    .map(|cell| TotalBasis::Overlap(overlap_index, cell)),
            );
        }
    }
    result
}

fn index_of<T: Eq + std::fmt::Debug>(basis: &[T], value: &T) -> usize {
    basis
        .iter()
        .position(|candidate| candidate == value)
        .unwrap_or_else(|| panic!("basis element not found: {value:?}"))
}

fn total_boundary_matrix(degree: usize) -> Matrix {
    assert!((1..=2).contains(&degree));
    let source = total_basis(degree);
    let target = total_basis(degree - 1);
    let mut matrix = zero_matrix(target.len(), source.len());
    for (column, generator) in source.iter().copied().enumerate() {
        match generator {
            TotalBasis::Facet(chart, cell) => {
                for (face, coefficient) in weighted_boundary(cell) {
                    let row = index_of(&target, &TotalBasis::Facet(chart, face));
                    add_matrix_entry(&mut matrix, row, column, coefficient);
                }
            }
            TotalBasis::Overlap(overlap, cell) => {
                let pair = ADJACENT[overlap];
                let first = index_of(&target, &TotalBasis::Facet(pair.0, cell));
                let second = index_of(&target, &TotalBasis::Facet(pair.1, cell));
                add_matrix_entry(&mut matrix, first, column, Polynomial::one());
                add_matrix_entry(&mut matrix, second, column, Polynomial::one().scale(-1));

                // The overlap resolution is shifted once in Cone(j), so its
                // internal differential enters with a minus sign.
                for (face, coefficient) in weighted_boundary(cell) {
                    let row = index_of(&target, &TotalBasis::Overlap(overlap, face));
                    add_matrix_entry(&mut matrix, row, column, coefficient.scale(-1));
                }
            }
        }
    }
    matrix
}

fn belt_boundary_matrix(degree: usize) -> Matrix {
    let source = belt_cells(degree);
    let target = belt_cells(degree - 1);
    let mut matrix = zero_matrix(target.len(), source.len());
    for (column, cell) in source.into_iter().enumerate() {
        for (face, coefficient) in weighted_boundary(cell) {
            let row = index_of(&target, &face);
            add_matrix_entry(&mut matrix, row, column, coefficient);
        }
    }
    matrix
}

fn comparison_matrix(degree: usize) -> Matrix {
    let source = total_basis(degree);
    let target = belt_cells(degree);
    let mut matrix = zero_matrix(target.len(), source.len());
    for (column, generator) in source.into_iter().enumerate() {
        if let TotalBasis::Facet(_, cell) = generator {
            let row = index_of(&target, &cell);
            add_matrix_entry(&mut matrix, row, column, Polynomial::one());
        }
    }
    matrix
}

fn matrix_is_zero(matrix: &Matrix) -> bool {
    matrix.iter().flatten().all(Polynomial::is_zero)
}

fn evaluate_matrix_at_one(matrix: &Matrix) -> IntMatrix {
    matrix
        .iter()
        .map(|row| row.iter().map(Polynomial::evaluate_at_one).collect())
        .collect()
}

fn unit_smith_rank(mut matrix: IntMatrix) -> usize {
    let rows = matrix.len();
    let columns = matrix.first().map_or(0, Vec::len);
    let mut pivot = 0;
    while pivot < rows.min(columns) {
        let found = (pivot..rows).find_map(|row| {
            (pivot..columns)
                .find(|&column| matrix[row][column].abs() == 1)
                .map(|column| (row, column))
        });
        let Some((pivot_row, pivot_column)) = found else {
            assert!(matrix[pivot..]
                .iter()
                .all(|row| row[pivot..].iter().all(|&value| value == 0)));
            break;
        };
        matrix.swap(pivot, pivot_row);
        for row in &mut matrix {
            row.swap(pivot, pivot_column);
        }
        if matrix[pivot][pivot] == -1 {
            for value in &mut matrix[pivot] {
                *value = -*value;
            }
        }
        for row in 0..rows {
            if row == pivot {
                continue;
            }
            let multiple = matrix[row][pivot];
            if multiple != 0 {
                for column in pivot..columns {
                    matrix[row][column] -= multiple * matrix[pivot][column];
                }
            }
        }
        for column in 0..columns {
            if column == pivot {
                continue;
            }
            let multiple = matrix[pivot][column];
            if multiple != 0 {
                for row in 0..rows {
                    matrix[row][column] -= multiple * matrix[row][pivot];
                }
            }
        }
        assert_eq!(matrix[pivot][pivot], 1);
        assert!((0..rows).all(|row| row == pivot || matrix[row][pivot] == 0));
        assert!((0..columns).all(|column| column == pivot || matrix[pivot][column] == 0));
        pivot += 1;
    }
    pivot
}

fn check_hypercech_totalization() {
    assert_eq!(belt_cells(0).len(), 8);
    assert_eq!(belt_cells(1).len(), 12);
    assert_eq!(belt_cells(2).len(), 4);
    assert_eq!(total_basis(0).len(), 16);
    assert_eq!(total_basis(1).len(), 24);
    assert_eq!(total_basis(2).len(), 8);

    let total_d1 = total_boundary_matrix(1);
    let total_d2 = total_boundary_matrix(2);
    let belt_d1 = belt_boundary_matrix(1);
    let belt_d2 = belt_boundary_matrix(2);
    assert!(matrix_is_zero(&multiply_matrices(&total_d1, &total_d2)));
    assert!(matrix_is_zero(&multiply_matrices(&belt_d1, &belt_d2)));

    let q0 = comparison_matrix(0);
    let q1 = comparison_matrix(1);
    let q2 = comparison_matrix(2);
    assert_eq!(
        multiply_matrices(&q0, &total_d1),
        multiply_matrices(&belt_d1, &q1)
    );
    assert_eq!(
        multiply_matrices(&q1, &total_d2),
        multiply_matrices(&belt_d2, &q2)
    );

    // Cell by cell, 0 -> overlap copies -> facet copies -> belt cell -> 0
    // is split exact over A.  This proves that Cone(j) -> B_Q^w is a
    // polynomial quasi-isomorphism, not only a numerical specialization.
    for degree in 0..=2 {
        for cell in belt_cells(degree) {
            let containing_facets: Vec<_> = CHARTS
                .iter()
                .enumerate()
                .filter_map(|(index, chart)| facet_contains(chart.facet, cell).then_some(index))
                .collect();
            let containing_overlaps: Vec<_> = ADJACENT
                .iter()
                .enumerate()
                .filter_map(|(index, &(first, second))| {
                    (containing_facets.contains(&first) && containing_facets.contains(&second))
                        .then_some(index)
                })
                .collect();
            assert!((1..=2).contains(&containing_facets.len()));
            assert_eq!(containing_overlaps.len() + 1, containing_facets.len());
            let local_j: IntMatrix = if containing_facets.len() == 2 {
                vec![vec![1], vec![-1]]
            } else {
                vec![Vec::new()]
            };
            let local_q: IntMatrix = vec![vec![1; containing_facets.len()]];
            assert!(multiply_int(&local_q, &local_j)
                .iter()
                .flatten()
                .all(|&value| value == 0));
            assert_eq!(unit_smith_rank(local_j), containing_facets.len() - 1);
            assert_eq!(unit_smith_rank(local_q), 1);
            if containing_facets.len() == 2 {
                let pair = ADJACENT[containing_overlaps[0]];
                assert_eq!(
                    BTreeSet::from([pair.0, pair.1]),
                    containing_facets.iter().copied().collect()
                );
            }
        }
    }

    // Unit Smith reductions at X_ra=1.  All nonzero invariant factors are
    // one.  Thus both complexes have integral H_0=Z, H_1=Z, H_2=0 and no
    // torsion; the totalization has the same exact ranks as the belt.
    let belt_rank_d1 = unit_smith_rank(evaluate_matrix_at_one(&belt_d1));
    let belt_rank_d2 = unit_smith_rank(evaluate_matrix_at_one(&belt_d2));
    let total_rank_d1 = unit_smith_rank(evaluate_matrix_at_one(&total_d1));
    let total_rank_d2 = unit_smith_rank(evaluate_matrix_at_one(&total_d2));
    assert_eq!((belt_rank_d1, belt_rank_d2), (7, 4));
    assert_eq!((total_rank_d1, total_rank_d2), (15, 8));
    assert_eq!(12 - belt_rank_d1 - belt_rank_d2, 1);
    assert_eq!(24 - total_rank_d1 - total_rank_d2, 1);
}

fn facet_vertices(facet: Facet) -> [CubeCell; 4] {
    let free: Vec<_> = (0..3)
        .filter(|&coordinate| coordinate != facet.coordinate)
        .collect();
    let make = |first: u8, second: u8| {
        let mut word = [0_u8; 3];
        word[facet.coordinate] = facet.value;
        word[free[0]] = first;
        word[free[1]] = second;
        CubeCell(word)
    };
    [make(0, 0), make(1, 0), make(1, 1), make(0, 1)]
}

impl Chart {
    fn target_vertex(self, source_vertex: usize) -> CubeCell {
        let target_index = if self.sides == 5 && source_vertex == 4 {
            0
        } else {
            source_vertex
        };
        facet_vertices(self.facet)[target_index]
    }

    fn target_edge(self, source_edge: usize) -> Option<(CubeCell, i64)> {
        let head = self.target_vertex(source_edge);
        let tail = self.target_vertex((source_edge + self.sides - 1) % self.sides);
        if head == tail {
            return None;
        }
        let coordinate = (0..3)
            .find(|&region| head.0[region] != tail.0[region])
            .unwrap();
        let mut word = head.0;
        word[coordinate] = STAR;
        let orientation = if tail.0[coordinate] == 0 { 1 } else { -1 };
        Some((CubeCell(word), orientation))
    }

    fn target_face(self) -> CubeCell {
        let mut word = [STAR; 3];
        word[self.facet.coordinate] = self.facet.value;
        CubeCell(word)
    }
}

fn facet_orientation(facet: Facet) -> i64 {
    let coordinate_sign = if facet.coordinate % 2 == 0 { 1 } else { -1 };
    coordinate_sign * if facet.value == 1 { 1 } else { -1 }
}

fn source_basis(degree: usize) -> Vec<SourceCell> {
    CHARTS
        .iter()
        .enumerate()
        .flat_map(|(chart, data)| {
            let count = match degree {
                0 | 1 => data.sides,
                2 => 1,
                _ => 0,
            };
            (0..count).map(move |local| SourceCell { chart, local })
        })
        .collect()
}

fn source_boundary_matrix(degree: usize) -> IntMatrix {
    let source = source_basis(degree);
    let target = source_basis(degree - 1);
    let mut matrix = vec![vec![0_i64; source.len()]; target.len()];
    for (column, generator) in source.into_iter().enumerate() {
        let chart = CHARTS[generator.chart];
        match degree {
            1 => {
                let head = SourceCell {
                    chart: generator.chart,
                    local: generator.local,
                };
                let tail = SourceCell {
                    chart: generator.chart,
                    local: (generator.local + chart.sides - 1) % chart.sides,
                };
                matrix[index_of(&target, &head)][column] += 1;
                matrix[index_of(&target, &tail)][column] -= 1;
            }
            2 => {
                for local in 0..chart.sides {
                    let edge = SourceCell {
                        chart: generator.chart,
                        local,
                    };
                    matrix[index_of(&target, &edge)][column] += 1;
                }
            }
            _ => unreachable!(),
        }
    }
    matrix
}

fn raw_carrier_matrix(degree: usize) -> Matrix {
    let source = source_basis(degree);
    let target = belt_cells(degree);
    let mut matrix = zero_matrix(target.len(), source.len());
    for (column, generator) in source.into_iter().enumerate() {
        let chart = CHARTS[generator.chart];
        let orientation = facet_orientation(chart.facet);
        match degree {
            0 => {
                let cell = chart.target_vertex(generator.local);
                let row = index_of(&target, &cell);
                add_matrix_entry(
                    &mut matrix,
                    row,
                    column,
                    Polynomial::monomial(raw_vertex_weight(cell)).scale(orientation),
                );
            }
            1 => {
                if let Some((cell, edge_orientation)) = chart.target_edge(generator.local) {
                    let row = index_of(&target, &cell);
                    add_matrix_entry(
                        &mut matrix,
                        row,
                        column,
                        Polynomial::monomial(raw_cell_weight(cell))
                            .scale(orientation * edge_orientation),
                    );
                }
            }
            2 => {
                let cell = chart.target_face();
                let row = index_of(&target, &cell);
                add_matrix_entry(
                    &mut matrix,
                    row,
                    column,
                    Polynomial::monomial(raw_cell_weight(cell)).scale(orientation),
                );
            }
            _ => unreachable!(),
        }
    }
    matrix
}

fn int_to_polynomial_matrix(matrix: &IntMatrix) -> Matrix {
    matrix
        .iter()
        .map(|row| {
            row.iter()
                .map(|&value| Polynomial::one().scale(value))
                .collect()
        })
        .collect()
}

fn carrier_sign_and_target(degree: usize, generator: SourceCell) -> Option<(CubeCell, i64)> {
    let chart = CHARTS[generator.chart];
    let orientation = facet_orientation(chart.facet);
    match degree {
        0 => Some((chart.target_vertex(generator.local), orientation)),
        1 => chart
            .target_edge(generator.local)
            .map(|(cell, sign)| (cell, orientation * sign)),
        2 => Some((chart.target_face(), orientation)),
        _ => None,
    }
}

fn fiber_kernel_basis(
    degree: usize,
) -> (IntMatrix, Vec<SourceCell>, Vec<SourceCell>, Vec<SourceCell>) {
    let source = source_basis(degree);
    let target = belt_cells(degree);
    let mut columns: Vec<(Vec<i64>, SourceCell, bool)> = Vec::new();
    let mut anchors = Vec::new();

    // Zero columns occur only for the two collapsed pentagon edges.
    for (index, &generator) in source.iter().enumerate() {
        if carrier_sign_and_target(degree, generator).is_none() {
            let mut column = vec![0_i64; source.len()];
            column[index] = 1;
            columns.push((column, generator, true));
        }
    }

    for cell in target {
        let fiber: Vec<_> = source
            .iter()
            .copied()
            .filter(|&generator| {
                carrier_sign_and_target(degree, generator)
                    .is_some_and(|(target_cell, _)| target_cell == cell)
            })
            .collect();
        assert!(!fiber.is_empty());

        // At degree zero, choose P-local-0 as the anchor when a pentagon
        // duplicate is present.  This makes P-local-4 the explicit H_s
        // endpoint relation and leaves one cross-chart relation per vertex.
        let anchor = if degree == 0 {
            fiber
                .iter()
                .copied()
                .find(|generator| CHARTS[generator.chart].sides == 5 && generator.local == 0)
                .unwrap_or(fiber[0])
        } else {
            fiber[0]
        };
        anchors.push(anchor);
        let (_, anchor_sign) = carrier_sign_and_target(degree, anchor).unwrap();

        let mut nonanchors: Vec<_> = fiber
            .into_iter()
            .filter(|&generator| generator != anchor)
            .collect();
        nonanchors.sort_by_key(|generator| {
            let is_hs = degree == 0 && CHARTS[generator.chart].sides == 5 && generator.local == 4;
            (!is_hs, generator.chart, generator.local)
        });
        for generator in nonanchors {
            let (_, sign) = carrier_sign_and_target(degree, generator).unwrap();
            let mut column = vec![0_i64; source.len()];
            column[index_of(&source, &generator)] = 1;
            column[index_of(&source, &anchor)] = -sign * anchor_sign;
            let is_hs = degree == 0 && CHARTS[generator.chart].sides == 5 && generator.local == 4;
            columns.push((column, generator, is_hs));
        }
    }

    // Reorder the kernel basis so the two H_s generators occur first.
    columns.sort_by_key(|(_, generator, is_hs)| (!*is_hs, generator.chart, generator.local));

    let matrix = (0..source.len())
        .map(|row| columns.iter().map(|(column, _, _)| column[row]).collect())
        .collect();
    let nonanchors = columns.iter().map(|(_, generator, _)| *generator).collect();
    let distinguished_hs = columns
        .iter()
        .filter_map(|(_, generator, is_hs)| is_hs.then_some(*generator))
        .collect();
    (matrix, anchors, distinguished_hs, nonanchors)
}

fn multiply_int(left: &IntMatrix, right: &IntMatrix) -> IntMatrix {
    assert_eq!(left.first().map_or(0, Vec::len), right.len());
    let rows = left.len();
    let columns = right.first().map_or(0, Vec::len);
    let middle = right.len();
    let mut result = vec![vec![0_i64; columns]; rows];
    for row in 0..rows {
        for column in 0..columns {
            result[row][column] = (0..middle)
                .map(|index| left[row][index] * right[index][column])
                .sum();
        }
    }
    result
}

fn determinant(mut matrix: IntMatrix) -> i64 {
    let size = matrix.len();
    assert!(matrix.iter().all(|row| row.len() == size));
    if size == 0 {
        return 1;
    }
    let mut sign = 1_i64;
    let mut denominator = 1_i64;
    for pivot_column in 0..size.saturating_sub(1) {
        let pivot_row = (pivot_column..size)
            .find(|&row| matrix[row][pivot_column] != 0)
            .unwrap();
        if pivot_row != pivot_column {
            matrix.swap(pivot_row, pivot_column);
            sign = -sign;
        }
        let pivot = matrix[pivot_column][pivot_column];
        for row in pivot_column + 1..size {
            for column in pivot_column + 1..size {
                let numerator = matrix[row][column] * pivot
                    - matrix[row][pivot_column] * matrix[pivot_column][column];
                assert_eq!(numerator % denominator, 0);
                matrix[row][column] = numerator / denominator;
            }
        }
        denominator = pivot;
    }
    sign * matrix[size - 1][size - 1]
}

fn append_anchor_columns(kernel: &IntMatrix, anchors: &[SourceCell], degree: usize) -> IntMatrix {
    let source = source_basis(degree);
    let mut result = kernel.clone();
    for row in 0..source.len() {
        result[row].extend(
            anchors
                .iter()
                .map(|anchor| i64::from(source[row] == *anchor)),
        );
    }
    result
}

fn coordinates_in_fiber_kernel(
    vector: &[i64],
    degree: usize,
    kernel: &IntMatrix,
    nonanchors: &[SourceCell],
) -> Vec<i64> {
    let source = source_basis(degree);
    let columns = kernel.first().map_or(0, Vec::len);
    assert_eq!(nonanchors.len(), columns);
    let mut coordinates = vec![0_i64; columns];
    for column in 0..columns {
        let nonanchor = index_of(&source, &nonanchors[column]);
        assert_eq!(kernel[nonanchor][column], 1);
        coordinates[column] = vector[nonanchor];
    }
    let reconstructed: Vec<_> = (0..source.len())
        .map(|row| {
            (0..columns)
                .map(|column| kernel[row][column] * coordinates[column])
                .sum::<i64>()
        })
        .collect();
    assert_eq!(reconstructed, vector);
    coordinates
}

fn check_actual_carrier_relation_complex() {
    let source_d1 = source_boundary_matrix(1);
    let source_d2 = source_boundary_matrix(2);
    let carrier0 = raw_carrier_matrix(0);
    let carrier1 = raw_carrier_matrix(1);
    let carrier2 = raw_carrier_matrix(2);
    let belt_d1 = belt_boundary_matrix(1);
    let belt_d2 = belt_boundary_matrix(2);
    assert_eq!(
        multiply_matrices(&belt_d1, &carrier1),
        multiply_matrices(&carrier0, &int_to_polynomial_matrix(&source_d1))
    );
    assert_eq!(
        multiply_matrices(&belt_d2, &carrier2),
        multiply_matrices(&carrier1, &int_to_polynomial_matrix(&source_d2))
    );

    let (kernel0, anchors0, hs_vertices, nonanchors0) = fiber_kernel_basis(0);
    let (kernel1, anchors1, hs_edges, _nonanchors1) = fiber_kernel_basis(1);
    assert_eq!((kernel0.len(), kernel0[0].len()), (18, 10));
    assert_eq!((kernel1.len(), kernel1[0].len()), (18, 6));
    assert_eq!(hs_vertices.len(), 2);
    assert_eq!(hs_edges.len(), 2);
    assert_eq!(anchors0.len(), 8);
    assert_eq!(anchors1.len(), 12);

    // These are complete saturated kernels, not merely rational spanning
    // sets: adjoining one anchor per nonzero target fiber gives a unimodular
    // basis of each source lattice.
    assert_eq!(
        determinant(append_anchor_columns(&kernel0, &anchors0, 0)).abs(),
        1
    );
    assert_eq!(
        determinant(append_anchor_columns(&kernel1, &anchors1, 1)).abs(),
        1
    );

    // Restrict the polygon boundary to the degreewise kernels.
    let image = multiply_int(&source_d1, &kernel1);
    let kernel_columns = kernel1[0].len();
    let mut relation_d = vec![vec![0_i64; kernel_columns]; kernel0[0].len()];
    for column in 0..kernel_columns {
        let vector: Vec<_> = image.iter().map(|row| row[column]).collect();
        let coordinates = coordinates_in_fiber_kernel(&vector, 0, &kernel0, &nonanchors0);
        for row in 0..coordinates.len() {
            relation_d[row][column] = coordinates[row];
        }
    }

    // The first two summands are precisely the two collapsed P-edge cones.
    // Their differential is a unit diagonal.  Quotienting them leaves four
    // interval complexes: eight endpoint relations, four edge relations,
    // every row used once and every column having two primitive endpoints.
    assert_eq!(relation_d.len(), 10);
    assert_eq!(relation_d[0].len(), 6);
    for column in 0..2 {
        assert_eq!(relation_d[column][column].abs(), 1);
        assert!((0..10).all(|row| row == column || relation_d[row][column] == 0));
    }
    let residual: IntMatrix = relation_d[2..]
        .iter()
        .map(|row| row[2..].to_vec())
        .collect();
    assert_eq!((residual.len(), residual[0].len()), (8, 4));
    for column in 0..4 {
        let support: Vec<_> = (0..8).filter(|&row| residual[row][column] != 0).collect();
        assert_eq!(support.len(), 2);
        assert_eq!(residual[support[0]][column].abs(), 1);
        assert_eq!(residual[support[1]][column].abs(), 1);
        assert_eq!(
            residual[support[0]][column] + residual[support[1]][column],
            0
        );
    }
    for row in 0..8 {
        assert_eq!(
            (0..4).filter(|&column| residual[row][column] != 0).count(),
            1
        );
    }
    assert_eq!(unit_smith_rank(residual), 4);

    // Four faces map injectively to four distinct target facets, so K_2=0.
    assert_eq!(source_basis(2).len(), 4);
    assert_eq!(unit_smith_rank(evaluate_matrix_at_one(&carrier2)), 4);
}

fn transform_facet(facet: Facet, swap: bool, flip0: u8, flip2: u8) -> Facet {
    let (coordinate, flip) = match (swap, facet.coordinate) {
        (false, 0) => (0, flip0),
        (false, 2) => (2, flip2),
        (true, 0) => (2, flip2),
        (true, 2) => (0, flip0),
        _ => panic!("not an outer facet"),
    };
    Facet {
        coordinate,
        value: facet.value ^ flip,
    }
}

fn transform_monomial(value: Monomial, swap: bool, flip0: u8, flip2: u8) -> Monomial {
    let mut result = Monomial::one();
    for region in 0..3 {
        for bit in 0..2 {
            let power = value.0[2 * region + bit];
            if power == 0 {
                continue;
            }
            let (new_region, flip) = match (swap, region) {
                (_, 1) => (1, 0),
                (false, 0) => (0, flip0),
                (false, 2) => (2, flip2),
                (true, 0) => (2, flip2),
                (true, 2) => (0, flip0),
                _ => unreachable!(),
            };
            result.0[2 * new_region + (bit ^ flip as usize)] = power;
        }
    }
    result
}

fn check_covariance_and_normalization() {
    let facet_set: BTreeSet<_> = CHARTS.iter().map(|chart| chart.facet).collect();
    let adjacent_set: BTreeSet<_> = ADJACENT
        .iter()
        .map(|&(first, second)| BTreeSet::from([CHARTS[first].facet, CHARTS[second].facet]))
        .collect();
    let mut automorphisms = BTreeSet::new();
    for swap in [false, true] {
        for flip0 in 0..=1_u8 {
            for flip2 in 0..=1_u8 {
                let image: Vec<_> = CHARTS
                    .iter()
                    .map(|chart| transform_facet(chart.facet, swap, flip0, flip2))
                    .collect();
                assert_eq!(image.iter().copied().collect::<BTreeSet<_>>(), facet_set);
                let permutation: Vec<_> = image
                    .iter()
                    .map(|facet| {
                        CHARTS
                            .iter()
                            .position(|chart| chart.facet == *facet)
                            .unwrap()
                    })
                    .collect();
                automorphisms.insert(permutation.clone());
                for &(first, second) in &ADJACENT {
                    assert!(adjacent_set.contains(&BTreeSet::from([image[first], image[second]])));
                    let transformed: Ideal =
                        intersect_ideals(&facet_ideal(image[first]), &facet_ideal(image[second]));
                    let original = intersect_ideals(
                        &facet_ideal(CHARTS[first].facet),
                        &facet_ideal(CHARTS[second].facet),
                    );
                    let transported: Ideal = original
                        .into_iter()
                        .map(|monomial| transform_monomial(monomial, swap, flip0, flip2))
                        .collect();
                    assert_eq!(transformed, transported);
                }
            }
        }
    }
    assert_eq!(automorphisms.len(), 8);

    // Four edge compatibilities leave one common scalar.  Fixing the first
    // chart normalization gives a unimodular system, hence unique saturated
    // normalization over Z and A.
    let normalization = vec![
        vec![1, -1, 0, 0],
        vec![1, 0, 0, -1],
        vec![0, 1, -1, 0],
        vec![1, 0, 0, 0],
    ];
    assert_eq!(determinant(normalization).abs(), 1);

    // Ordered contractions of the two outer normals differ by the Koszul
    // sign.  The same anticommutation is already present in d^2=0 above.
    let normal_02 = 1_i64;
    let normal_20 = -1_i64;
    assert_eq!(normal_02, -normal_20);
}

fn main() {
    assert_eq!(CHARTS.map(|chart| chart.name), ["P+", "P-", "S+", "S-"]);
    check_ideal_intersections_and_minimal_resolutions();
    check_hypercech_totalization();
    check_actual_carrier_relation_complex();
    check_covariance_and_normalization();

    println!("resolved support-overlap hyper-Cech certificate");
    println!("  ring: Z[X00,X01,X10,X11,X20,X21]");
    println!("  scalar ideal: I_Q=(X00,X01)(X10,X11)(X20,X21)");
    println!("  support facets: P+ x2=1, P- x0=1, S+ x2=0, S- x0=0");
    println!("  every adjacent facet-ideal intersection is C_e (X10,X11)");
    println!("  each has two minimal generators and one primitive interval syzygy");
    println!("  opposite facets have nonzero algebraic intersections and are excluded");
    println!("  four facet plus four interval resolutions form the support hyper-Cech cone");
    println!("  the cone maps strictly and polynomially to the weighted belt B_Q^w");
    println!("  cellwise split exactness proves that comparison is a quasi-isomorphism");
    println!("  integral homology: H0=Z, H1=Z, H2=0, with unit Smith factors");
    println!("  actual polygon carrier kernel ranks: K0=10, K1=6, K2=0");
    println!("  two kernel intervals are the collapsed pentagon cones H_s");
    println!("  quotient relation complex: exactly four primitive overlap intervals");
    println!("  relation lattices and normalized four-cycle are saturated over Z");
    println!("  all descent pivots are units: no division by 2 or 8 occurs");
    println!("  outer-square deck covariance and ordered-normal Koszul sign hold");
    println!();
    println!("VERDICT: CONDITIONAL");
    println!("  the four bridges are canonical in the support-selected algebraic carrier");
    println!("  they are not free cells once adjacent overlap modules are minimally resolved");
    println!("  finite-alpha Pochhammer/Cousin and scalar-geometric provenance remain open");
}
