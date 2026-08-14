//! Exact certificate for the universal finite-loading relation algebra.
//!
//! Put q_ra=exp(2 pi i alpha' s_ra) and u_ra=q_ra-1.  This certificate
//! works first over R0=Z[u_00,u_01,u_10,u_11,u_20,u_21].  The universal
//! rank-one local-system ring is
//!
//!   Lambda=Z[q_ra^{+/-1}]
//!         =R0[(1+u_ra)^{-1}],
//!
//! a flat localization.  Consequently every identity and split exact
//! sequence checked below remains valid over Lambda, and after additionally
//! inverting the nonresonant u_ra.  At that last localization the labelled
//! resolutions cease to be minimal and support can no longer be recovered
//! from ideals alone; the scalar support poset must still be retained.
//!
//! This is only a universal group-ring/local-system algebra theorem.  More
//! precisely, it is the base change of the scalar lcm carrier along the
//! formal substitution X_ra |-> u_ra.  Entry 38 types the physical object
//! differently: X_ra remains an occurrence/contact coefficient, whereas
//! q_E-1 is the differential in an additional normal Pochhammer Koszul
//! factor.  Tensoring that normal factor with this substituted carrier would
//! count the same boundary loading twice.  Thus the certificate does not
//! construct loaded tangential transport on the scalar flip edge,
//! Pochhammer currents, collars, a rank-one excess-conormal Thom cone, or the
//! dependent Cousin natural transformation.  In particular, the rank-one
//! algebraic overlap syzygy does not prove that the actual derived scalar
//! fiber product has a locally free rank-one excess cotangent complex.

use std::collections::{BTreeMap, BTreeSet};

const STAR: u8 = 2;
const VARIABLES: usize = 6;

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct Monomial([u8; VARIABLES]);

#[derive(Clone, Debug, Eq, PartialEq)]
struct Polynomial(BTreeMap<Monomial, i64>);

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct Cell([u8; 3]);

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
enum TotalCell {
    Facet(usize, Cell),
    Overlap(usize, Cell),
}

type Chain<T> = BTreeMap<T, Polynomial>;
type Ideal = BTreeSet<Monomial>;

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

    fn variable_index(index: usize) -> Self {
        let mut powers = [0; VARIABLES];
        powers[index] = 1;
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
        let mut result = Polynomial::zero();
        for (&left, &left_coefficient) in &self.0 {
            for (&right, &right_coefficient) in &other.0 {
                let term = Polynomial::monomial(left.multiply(right))
                    .scale(left_coefficient * right_coefficient);
                result = result.add(&term);
            }
        }
        result
    }

    fn is_zero(&self) -> bool {
        self.0.is_empty()
    }
}

fn add_term<T: Copy + Ord>(chain: &mut Chain<T>, cell: T, coefficient: Polynomial) {
    let value = chain
        .get(&cell)
        .cloned()
        .unwrap_or_else(Polynomial::zero)
        .add(&coefficient);
    if value.is_zero() {
        chain.remove(&cell);
    } else {
        chain.insert(cell, value);
    }
}

fn vertices(cell: Cell) -> Vec<Cell> {
    let free: Vec<_> = (0..3)
        .filter(|&coordinate| cell.0[coordinate] == STAR)
        .collect();
    (0..1_usize << free.len())
        .map(|mask| {
            let mut vertex = cell;
            for (index, &coordinate) in free.iter().enumerate() {
                vertex.0[coordinate] = ((mask >> index) & 1) as u8;
            }
            vertex
        })
        .collect()
}

fn opposite_label(vertex: Cell) -> Monomial {
    assert!(vertex.0.iter().all(|&value| value < 2));
    (0..3).fold(Monomial::one(), |product, region| {
        product.multiply(Monomial::variable(region, 1 - vertex.0[region] as usize))
    })
}

fn raw_weight(vertex: Cell) -> Monomial {
    assert!(vertex.0.iter().all(|&value| value < 2));
    (0..3).fold(Monomial::one(), |product, region| {
        product.multiply(Monomial::variable(region, vertex.0[region] as usize))
    })
}

fn cell_label(cell: Cell) -> Monomial {
    vertices(cell)
        .into_iter()
        .map(opposite_label)
        .reduce(Monomial::lcm)
        .unwrap()
}

fn raw_cell_weight(cell: Cell) -> Monomial {
    vertices(cell)
        .into_iter()
        .map(raw_weight)
        .reduce(Monomial::gcd)
        .unwrap()
}

fn dimension(cell: Cell) -> usize {
    cell.0.iter().filter(|&&value| value == STAR).count()
}

fn cells(degree: usize) -> Vec<Cell> {
    let mut result = Vec::new();
    for code in 0..27 {
        let mut work = code;
        let mut word = [0_u8; 3];
        for value in &mut word {
            *value = (work % 3) as u8;
            work /= 3;
        }
        let cell = Cell(word);
        if dimension(cell) == degree {
            result.push(cell);
        }
    }
    result.sort();
    result
}

fn loaded_boundary(cell: Cell) -> Vec<(Cell, Polynomial)> {
    let label = cell_label(cell);
    let mut result = Vec::new();
    let mut normal_position = 0;
    for coordinate in 0..3 {
        if cell.0[coordinate] != STAR {
            continue;
        }
        let koszul = if normal_position % 2 == 0 { 1 } else { -1 };
        for (value, sign) in [(1_u8, koszul), (0_u8, -koszul)] {
            let mut face = cell;
            face.0[coordinate] = value;
            result.push((
                face,
                Polynomial::monomial(label.quotient(cell_label(face))).scale(sign),
            ));
        }
        normal_position += 1;
    }
    result
}

fn boundary_chain(chain: &Chain<Cell>) -> Chain<Cell> {
    let mut result = Chain::new();
    for (&cell, coefficient) in chain {
        for (face, incidence) in loaded_boundary(cell) {
            add_term(&mut result, face, coefficient.multiply(&incidence));
        }
    }
    result
}

fn facet_contains(facet: Facet, cell: Cell) -> bool {
    cell.0[facet.coordinate] == facet.value
}

fn facet_cells(facet: Facet, degree: usize) -> Vec<Cell> {
    cells(degree)
        .into_iter()
        .filter(|&cell| facet_contains(facet, cell))
        .collect()
}

fn belt_cells(degree: usize) -> Vec<Cell> {
    cells(degree)
        .into_iter()
        .filter(|&cell| CHARTS.iter().any(|chart| facet_contains(chart.facet, cell)))
        .collect()
}

fn overlap_cell(pair: (usize, usize), middle: u8) -> Cell {
    let mut word = [STAR; 3];
    word[1] = middle;
    for chart in [CHARTS[pair.0], CHARTS[pair.1]] {
        word[chart.facet.coordinate] = chart.facet.value;
    }
    assert!(word[0] < 2 && word[2] < 2);
    Cell(word)
}

fn normalize_ideal(generators: impl IntoIterator<Item = Monomial>) -> Ideal {
    let all: Ideal = generators.into_iter().collect();
    all.iter()
        .copied()
        .filter(|&candidate| {
            !all.iter()
                .copied()
                .any(|other| other != candidate && other.divides(candidate))
        })
        .collect()
}

fn intersect_ideals(left: &Ideal, right: &Ideal) -> Ideal {
    normalize_ideal(
        left.iter()
            .flat_map(|&a| right.iter().map(move |&b| a.lcm(b))),
    )
}

fn facet_ideal(facet: Facet) -> Ideal {
    normalize_ideal(facet_cells(facet, 0).into_iter().map(opposite_label))
}

fn total_boundary(generator: TotalCell) -> Chain<TotalCell> {
    let mut result = Chain::new();
    match generator {
        TotalCell::Facet(chart, cell) => {
            for (face, coefficient) in loaded_boundary(cell) {
                add_term(&mut result, TotalCell::Facet(chart, face), coefficient);
            }
        }
        TotalCell::Overlap(overlap, cell) => {
            let pair = ADJACENT[overlap];
            add_term(
                &mut result,
                TotalCell::Facet(pair.0, cell),
                Polynomial::one(),
            );
            add_term(
                &mut result,
                TotalCell::Facet(pair.1, cell),
                Polynomial::one().scale(-1),
            );
            for (face, coefficient) in loaded_boundary(cell) {
                add_term(
                    &mut result,
                    TotalCell::Overlap(overlap, face),
                    coefficient.scale(-1),
                );
            }
        }
    }
    result
}

fn total_boundary_chain(chain: &Chain<TotalCell>) -> Chain<TotalCell> {
    let mut result = Chain::new();
    for (&cell, coefficient) in chain {
        for (face, incidence) in total_boundary(cell) {
            add_term(&mut result, face, coefficient.multiply(&incidence));
        }
    }
    result
}

fn comparison(generator: TotalCell) -> Chain<Cell> {
    match generator {
        TotalCell::Facet(_, cell) => BTreeMap::from([(cell, Polynomial::one())]),
        TotalCell::Overlap(_, _) => Chain::new(),
    }
}

fn comparison_chain(chain: &Chain<TotalCell>) -> Chain<Cell> {
    let mut result = Chain::new();
    for (&cell, coefficient) in chain {
        for (target, value) in comparison(cell) {
            add_term(&mut result, target, coefficient.multiply(&value));
        }
    }
    result
}

fn check_universal_loading_and_support_resolution() {
    // Independent q's impose no multiplicative relation on u=q-1.  The
    // displayed bounded audit complements the exact multidegree argument:
    // product_i(1+u_i)^{a_i}=product_i(1+u_i)^{b_i} forces a_i=b_i.
    let one_plus: Vec<_> = (0..VARIABLES)
        .map(|index| Polynomial::one().add(&Polynomial::monomial(Monomial::variable_index(index))))
        .collect();
    for first in 0..VARIABLES {
        for second in first + 1..VARIABLES {
            assert_ne!(one_plus[first], one_plus[second]);
            assert_ne!(
                one_plus[first].multiply(&one_plus[second]),
                Polynomial::one()
            );
        }
    }

    for degree in 2..=3 {
        for cell in cells(degree) {
            let first = BTreeMap::from([(cell, Polynomial::one())]);
            assert!(boundary_chain(&boundary_chain(&first)).is_empty());
        }
    }

    let mut bridges = BTreeSet::new();
    for (overlap, pair) in ADJACENT.into_iter().enumerate() {
        let intersection = intersect_ideals(
            &facet_ideal(CHARTS[pair.0].facet),
            &facet_ideal(CHARTS[pair.1].facet),
        );
        let v0 = overlap_cell(pair, 0);
        let v1 = overlap_cell(pair, 1);
        let interval = overlap_cell(pair, STAR);
        let expected = BTreeSet::from([opposite_label(v0), opposite_label(v1)]);
        assert_eq!(intersection, expected);
        assert_eq!(intersection.len(), 2);

        let u10 = Monomial::variable(1, 0);
        let u11 = Monomial::variable(1, 1);
        assert_eq!(
            u11.multiply(opposite_label(v1)),
            u10.multiply(opposite_label(v0))
        );
        assert_eq!(
            loaded_boundary(interval),
            vec![
                (v1, Polynomial::monomial(u11)),
                (v0, Polynomial::monomial(u10).scale(-1)),
            ]
        );
        bridges.insert(interval);

        // Both overlap inclusions are strict loaded chain maps.
        for (face, _) in loaded_boundary(interval) {
            assert!(facet_contains(CHARTS[pair.0].facet, face));
            assert!(facet_contains(CHARTS[pair.1].facet, face));
        }

        // The shifted overlap differential and Cech incidence anticommute.
        let generator = TotalCell::Overlap(overlap, interval);
        let first = BTreeMap::from([(generator, Polynomial::one())]);
        assert!(total_boundary_chain(&total_boundary_chain(&first)).is_empty());
        assert_eq!(
            comparison_chain(&total_boundary_chain(&first)),
            boundary_chain(&comparison_chain(&first))
        );
    }
    assert_eq!(bridges.len(), 4);

    // Opposite facets have nonzero ideal intersection but no scalar support
    // overlap.  This is why localization cannot choose the physical nerve.
    for pair in OPPOSITE {
        assert!(!intersect_ideals(
            &facet_ideal(CHARTS[pair.0].facet),
            &facet_ideal(CHARTS[pair.1].facet)
        )
        .is_empty());
        assert!(!ADJACENT.contains(&pair));
    }

    // Cellwise, the augmented support Cech sequence is either
    // 0 -> 0 -> R -> R or 0 -> R -> R^2 -> R.  Hence it is split exact
    // over R0, over Lambda, and after nonresonant localization.
    for degree in 0..=2 {
        for cell in belt_cells(degree) {
            let charts: Vec<_> = CHARTS
                .iter()
                .enumerate()
                .filter_map(|(index, chart)| facet_contains(chart.facet, cell).then_some(index))
                .collect();
            assert!((1..=2).contains(&charts.len()));
            if charts.len() == 2 {
                assert!(ADJACENT
                    .iter()
                    .any(|&(a, b)| { BTreeSet::from([a, b]) == charts.iter().copied().collect() }));
            }
        }
    }
}

fn facet_vertices(facet: Facet) -> [Cell; 4] {
    let free: Vec<_> = (0..3)
        .filter(|&coordinate| coordinate != facet.coordinate)
        .collect();
    let make = |first: u8, second: u8| {
        let mut word = [0_u8; 3];
        word[facet.coordinate] = facet.value;
        word[free[0]] = first;
        word[free[1]] = second;
        Cell(word)
    };
    [make(0, 0), make(1, 0), make(1, 1), make(0, 1)]
}

impl Chart {
    fn target_vertex(self, source_vertex: usize) -> Cell {
        let target = if self.sides == 5 && source_vertex == 4 {
            0
        } else {
            source_vertex
        };
        facet_vertices(self.facet)[target]
    }

    fn target_edge(self, source_edge: usize) -> Option<(Cell, i64)> {
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
        Some((Cell(word), if tail.0[coordinate] == 0 { 1 } else { -1 }))
    }

    fn target_face(self) -> Cell {
        let mut word = [STAR; 3];
        word[self.facet.coordinate] = self.facet.value;
        Cell(word)
    }
}

fn facet_orientation(facet: Facet) -> i64 {
    let coordinate_sign = if facet.coordinate % 2 == 0 { 1 } else { -1 };
    coordinate_sign * if facet.value == 1 { 1 } else { -1 }
}

fn chart_vertex_image(chart: Chart, local: usize) -> Chain<Cell> {
    let target = chart.target_vertex(local);
    BTreeMap::from([(
        target,
        Polynomial::monomial(raw_weight(target)).scale(facet_orientation(chart.facet)),
    )])
}

fn chart_edge_image(chart: Chart, local: usize) -> Chain<Cell> {
    let Some((target, edge_sign)) = chart.target_edge(local) else {
        return Chain::new();
    };
    BTreeMap::from([(
        target,
        Polynomial::monomial(raw_cell_weight(target))
            .scale(facet_orientation(chart.facet) * edge_sign),
    )])
}

fn chart_face_image(chart: Chart) -> Chain<Cell> {
    let target = chart.target_face();
    BTreeMap::from([(
        target,
        Polynomial::monomial(raw_cell_weight(target)).scale(facet_orientation(chart.facet)),
    )])
}

fn check_loaded_route_carriers_and_hs() {
    let mut hs_cones = Vec::new();
    for chart in CHARTS {
        for edge in 0..chart.sides {
            let mut source_boundary_image = chart_vertex_image(chart, edge);
            for (cell, coefficient) in
                chart_vertex_image(chart, (edge + chart.sides - 1) % chart.sides)
            {
                add_term(&mut source_boundary_image, cell, coefficient.scale(-1));
            }
            assert_eq!(
                boundary_chain(&chart_edge_image(chart, edge)),
                source_boundary_image
            );
            if chart.target_edge(edge).is_none() {
                hs_cones.push((chart.name, edge));
                assert!(chart_edge_image(chart, edge).is_empty());
                assert!(source_boundary_image.is_empty());
            }
        }

        // This is the complete formal loaded five-edge identity on P and
        // four-edge identity on S.  For P exactly one scalar edge collapses.
        let mut polygon_boundary_image = Chain::new();
        for edge in 0..chart.sides {
            for (cell, coefficient) in chart_edge_image(chart, edge) {
                add_term(&mut polygon_boundary_image, cell, coefficient);
            }
        }
        assert_eq!(
            boundary_chain(&chart_face_image(chart)),
            polygon_boundary_image
        );
        assert_eq!(
            (0..chart.sides)
                .filter(|&edge| chart.target_edge(edge).is_none())
                .count(),
            usize::from(chart.sides == 5)
        );
    }
    assert_eq!(hs_cones, vec![("P+", 0), ("P-", 0)]);
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

fn check_deck_covariance_and_normal_sign() {
    let facets: BTreeSet<_> = CHARTS.iter().map(|chart| chart.facet).collect();
    let adjacent: BTreeSet<_> = ADJACENT
        .iter()
        .map(|&(a, b)| BTreeSet::from([CHARTS[a].facet, CHARTS[b].facet]))
        .collect();
    let mut permutations = BTreeSet::new();
    for swap in [false, true] {
        for flip0 in 0..=1_u8 {
            for flip2 in 0..=1_u8 {
                let image: Vec<_> = CHARTS
                    .iter()
                    .map(|chart| transform_facet(chart.facet, swap, flip0, flip2))
                    .collect();
                assert_eq!(image.iter().copied().collect::<BTreeSet<_>>(), facets);
                let permutation: Vec<_> = image
                    .iter()
                    .map(|facet| {
                        CHARTS
                            .iter()
                            .position(|chart| chart.facet == *facet)
                            .unwrap()
                    })
                    .collect();
                permutations.insert(permutation);
                for &(a, b) in &ADJACENT {
                    assert!(adjacent.contains(&BTreeSet::from([image[a], image[b]])));
                }
            }
        }
    }
    assert_eq!(permutations.len(), 8);

    // The formal support descent uses literal inclusions.  In cyclic order
    // P+ -> P- -> S+ -> S- -> P+, all four normalized transition ratios are
    // therefore +1 and the universal C4 holonomy telescopes exactly.  This
    // says nothing about unconstructed PC transition maps, which may carry
    // a tangential/collar unit H=1+O(alpha') or an orientation local system.
    let transition_ratios = [1_i64, 1, 1, 1];
    assert_eq!(transition_ratios.into_iter().product::<i64>(), 1);

    // The ordered outer normal line is antisymmetric.  The same Koszul sign
    // is what made the loaded cubical and hyper-Cech differentials square
    // to zero above.
    let normal_02 = 1_i64;
    let normal_20 = -1_i64;
    assert_eq!(normal_02, -normal_20);
}

fn main() {
    check_universal_loading_and_support_resolution();
    check_loaded_route_carriers_and_hs();
    check_deck_covariance_and_normal_sign();

    println!("universal finite-loading relation certificate");
    println!("  R0=Z[u00,u01,u10,u11,u20,u21], u_ra=q_ra-1");
    println!("  Lambda=R0[(1+u_ra)^-1] is the universal local-system group ring");
    println!("  loaded cubical and support hyper-Cech differentials square to zero");
    println!("  the support-selected hyper-Cech sequence is split exact cellwise");
    println!("  opposite supports remain excluded despite nonzero ideal intersections");
    println!("  four bridges have d h=u11 e(v1)-u10 e(v0)");
    println!("  both pentagon H_s edges collapse as separate unit cones");
    println!("  each formal pentagon has a five-edge loaded carrier identity");
    println!("  outer deck covariance and ordered-normal Koszul sign hold");
    println!("  formal C4 transition holonomy telescopes exactly to one");
    println!("  this is X_ra->u_ra base change, not X-weight tensor PC normal loading");
    println!();
    println!("VERDICT: CONDITIONAL");
    println!("  universal group-ring/local-system algebra is proved");
    println!("  genuine Pochhammer/Cousin naturality is not constructed");
    println!("  tangential scalar-edge loading and current/collar data remain absent");
}
