//! Exact combinatorial audit of the six-point barycentric tripods against
//! the codimension-one Cousin filtration used by the facewise PC complex.
//!
//! Entry 21 uses a final barycentric edge [T,b(F_D)] from a triangulation
//! vertex directly to the barycenter of a square physical facet.  That is a
//! valid edge of sd(K), but it skips one face dimension.  Consequently its
//! top-stratum boundary is not a single codimension-one Cousin incidence.
//!
//! For the tripod one can repair the jump without a cellular collapse.  A
//! corner T of the square F_D has exactly two incident scalar edges inside
//! F_D.  Replace [T,b(F_D)] by the half-sum of the two saturated flags
//!
//!   T < e_0 < F_D,  T < e_1 < F_D.
//!
//! Reflection in the corner/facet pair exchanges e_0 and e_1.  Invariance
//! and the required boundary force both weights to be 1/2.  The certificate
//! works with doubled integral chains.  It checks the two tripods, all D_6
//! images, every cover relation, and the resulting boundary.  It also
//! records that the saturated tail has nonzero support inside F_D.  Thus
//! residue-freeness does not follow from subdivision or support alone; it
//! still requires the occurrence/Gysin coefficient map.

use std::collections::{BTreeMap, BTreeSet};

const N: u8 = 6;

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct Diagonal(u8, u8);

type Triangulation = Vec<Diagonal>;

#[derive(Clone, Debug, Eq, Ord, PartialEq, PartialOrd)]
enum Node {
    Vertex(Triangulation),
    Edge(Triangulation, Triangulation),
    Facet(Diagonal),
}

type Chain = BTreeMap<(Node, Node), i64>;
type TwoChain = BTreeMap<(Node, Node, Node), i64>;

fn diagonal(first: u8, second: u8) -> Diagonal {
    if first < second {
        Diagonal(first, second)
    } else {
        Diagonal(second, first)
    }
}

fn boundary(value: Diagonal) -> bool {
    value.1 - value.0 == 1 || value == Diagonal(0, N - 1)
}

fn physical(value: Diagonal) -> bool {
    value.0 % 2 != value.1 % 2
}

fn between(vertex: u8, first: u8, second: u8) -> bool {
    let span = (second + N - first) % N;
    let position = (vertex + N - first) % N;
    position > 0 && position < span
}

fn crosses(first: Diagonal, second: Diagonal) -> bool {
    if [first.0, first.1]
        .iter()
        .any(|endpoint| *endpoint == second.0 || *endpoint == second.1)
    {
        return false;
    }
    between(second.0, first.0, first.1) != between(second.1, first.0, first.1)
        && between(first.0, second.0, second.1) != between(first.1, second.0, second.1)
}

fn all_diagonals() -> Vec<Diagonal> {
    let mut result = Vec::new();
    for first in 0..N {
        for second in first + 1..N {
            let value = Diagonal(first, second);
            if !boundary(value) {
                result.push(value);
            }
        }
    }
    result
}

fn triangulations() -> Vec<Triangulation> {
    let values = all_diagonals();
    let mut result = Vec::new();
    for first in 0..values.len() {
        for second in first + 1..values.len() {
            for third in second + 1..values.len() {
                let mut current = vec![values[first], values[second], values[third]];
                if current.iter().enumerate().all(|(index, &left)| {
                    current[index + 1..]
                        .iter()
                        .all(|&right| !crosses(left, right))
                }) {
                    current.sort();
                    result.push(current);
                }
            }
        }
    }
    result.sort();
    result.dedup();
    assert_eq!(result.len(), 14);
    result
}

fn common_count(first: &Triangulation, second: &Triangulation) -> usize {
    first.iter().filter(|value| second.contains(value)).count()
}

fn adjacent(first: &Triangulation, second: &Triangulation) -> bool {
    common_count(first, second) == 2
}

fn core(value: &Triangulation) -> Vec<Diagonal> {
    value
        .iter()
        .copied()
        .filter(|&item| physical(item))
        .collect()
}

fn ordered_edge(first: Triangulation, second: Triangulation) -> Node {
    if first < second {
        Node::Edge(first, second)
    } else {
        Node::Edge(second, first)
    }
}

fn add(chain: &mut Chain, first: Node, second: Node, coefficient: i64) {
    *chain.entry((first, second)).or_default() += coefficient;
    chain.retain(|_, value| *value != 0);
}

fn node_dimension(value: &Node) -> usize {
    match value {
        Node::Vertex(_) => 0,
        Node::Edge(_, _) => 1,
        Node::Facet(_) => 2,
    }
}

fn node_in_facet(value: &Node, facet: Diagonal) -> bool {
    match value {
        Node::Vertex(triangulation) => triangulation.contains(&facet),
        Node::Edge(first, second) => first.contains(&facet) && second.contains(&facet),
        Node::Facet(value) => *value == facet,
    }
}

fn chain_boundary(chain: &Chain) -> BTreeMap<Node, i64> {
    let mut result = BTreeMap::new();
    for ((first, second), coefficient) in chain {
        *result.entry(first.clone()).or_default() -= coefficient;
        *result.entry(second.clone()).or_default() += coefficient;
    }
    result.retain(|_, value| *value != 0);
    result
}

fn two_chain_boundary(chain: &TwoChain) -> Chain {
    let mut result = Chain::new();
    for ((first, second, third), coefficient) in chain {
        add(&mut result, second.clone(), third.clone(), *coefficient);
        add(&mut result, first.clone(), third.clone(), -*coefficient);
        add(&mut result, first.clone(), second.clone(), *coefficient);
    }
    result
}

fn route_homotopies(corner: &Triangulation, facet: Diagonal, triangulations: &[Triangulation]) {
    let fiber: Vec<_> = triangulations
        .iter()
        .filter(|value| core(value) == vec![facet])
        .cloned()
        .collect();
    let neighbors: Vec<_> = fiber
        .iter()
        .filter(|value| adjacent(corner, value))
        .cloned()
        .collect();
    assert_eq!(neighbors.len(), 2);

    let start = Node::Vertex(corner.clone());
    let end = Node::Facet(facet);
    let mut paths = Vec::new();
    let mut triangles = Vec::new();
    for neighbor in neighbors {
        let middle = ordered_edge(corner.clone(), neighbor);
        let mut path = Chain::new();
        add(&mut path, start.clone(), middle.clone(), 1);
        add(&mut path, middle.clone(), end.clone(), 1);
        paths.push(path);
        triangles.push((start.clone(), middle, end.clone()));
    }

    // Each saturated route differs from the nonsaturated radial edge by the
    // boundary of its barycentric two-simplex.
    let mut direct = Chain::new();
    add(&mut direct, start.clone(), end.clone(), 1);
    for (path, triangle) in paths.iter().zip(&triangles) {
        let boundary = two_chain_boundary(&BTreeMap::from([(triangle.clone(), 1)]));
        let mut expected = path.clone();
        add(&mut expected, start.clone(), end.clone(), -1);
        assert_eq!(boundary, expected);
    }

    // The doubled canonical half-sum differs from twice the radial edge by
    // the boundary of the sum of the two triangles.
    let filler: TwoChain = triangles
        .iter()
        .cloned()
        .map(|triangle| (triangle, 1))
        .collect();
    let mut expected = Chain::new();
    for path in &paths {
        for ((first, second), coefficient) in path {
            add(&mut expected, first.clone(), second.clone(), *coefficient);
        }
    }
    add(&mut expected, start.clone(), end.clone(), -2);
    assert_eq!(two_chain_boundary(&filler), expected);

    // The difference of the two route choices is itself an integral
    // boundary.  This is the point-set representative ambiguity which the
    // symmetric half-sum removes.
    let route_difference_filler =
        BTreeMap::from([(triangles[0].clone(), 1), (triangles[1].clone(), -1)]);
    let mut route_difference = paths[0].clone();
    for ((first, second), coefficient) in &paths[1] {
        add(
            &mut route_difference,
            first.clone(),
            second.clone(),
            -*coefficient,
        );
    }
    assert_eq!(
        two_chain_boundary(&route_difference_filler),
        route_difference
    );

    assert_eq!(
        chain_boundary(&direct),
        BTreeMap::from([(start, -1), (end, 1)])
    );
}

fn saturated_tripod_leg(
    center: &Triangulation,
    facet: Diagonal,
    triangulations: &[Triangulation],
) -> (Chain, Triangulation) {
    let fiber: Vec<_> = triangulations
        .iter()
        .filter(|value| core(value) == vec![facet])
        .cloned()
        .collect();
    assert_eq!(fiber.len(), 4);
    let corners: Vec<_> = fiber
        .iter()
        .filter(|value| adjacent(center, value))
        .cloned()
        .collect();
    assert_eq!(corners.len(), 1);
    let corner = corners[0].clone();
    let bridge = ordered_edge(center.clone(), corner.clone());

    let internal_neighbors: Vec<_> = fiber
        .iter()
        .filter(|value| adjacent(&corner, value))
        .cloned()
        .collect();
    assert_eq!(internal_neighbors.len(), 2);

    // Doubled chain: the first two segments have coefficient two; the two
    // saturated tails have coefficient one each.
    let mut result = Chain::new();
    add(&mut result, Node::Vertex(center.clone()), bridge.clone(), 2);
    add(&mut result, bridge, Node::Vertex(corner.clone()), 2);
    for neighbor in internal_neighbors {
        let edge = ordered_edge(corner.clone(), neighbor);
        add(&mut result, Node::Vertex(corner.clone()), edge.clone(), 1);
        add(&mut result, edge, Node::Facet(facet), 1);
    }

    assert_eq!(
        chain_boundary(&result),
        BTreeMap::from([(Node::Vertex(center.clone()), -2), (Node::Facet(facet), 2),])
    );
    assert!(result
        .keys()
        .all(|(first, second)| { node_dimension(first).abs_diff(node_dimension(second)) == 1 }));
    (result, corner)
}

fn rotate_diagonal(value: Diagonal, amount: u8, reflect: bool) -> Diagonal {
    let transform = |vertex: u8| {
        let reflected = if reflect { (N - vertex) % N } else { vertex };
        (reflected + amount) % N
    };
    diagonal(transform(value.0), transform(value.1))
}

fn transform_triangulation(value: &Triangulation, amount: u8, reflect: bool) -> Triangulation {
    let mut result: Vec<_> = value
        .iter()
        .copied()
        .map(|item| rotate_diagonal(item, amount, reflect))
        .collect();
    result.sort();
    result
}

fn transform_node(value: &Node, amount: u8, reflect: bool) -> Node {
    match value {
        Node::Vertex(triangulation) => {
            Node::Vertex(transform_triangulation(triangulation, amount, reflect))
        }
        Node::Edge(first, second) => ordered_edge(
            transform_triangulation(first, amount, reflect),
            transform_triangulation(second, amount, reflect),
        ),
        Node::Facet(value) => Node::Facet(rotate_diagonal(*value, amount, reflect)),
    }
}

fn transform_chain(value: &Chain, amount: u8, reflect: bool) -> Chain {
    value
        .iter()
        .map(|((first, second), coefficient)| {
            (
                (
                    transform_node(first, amount, reflect),
                    transform_node(second, amount, reflect),
                ),
                *coefficient,
            )
        })
        .collect()
}

fn main() {
    let triangulations = triangulations();
    let physical_facets: Vec<_> = all_diagonals()
        .into_iter()
        .filter(|&value| physical(value))
        .collect();
    assert_eq!(
        physical_facets,
        vec![diagonal(0, 3), diagonal(1, 4), diagonal(2, 5)]
    );
    let centers: Vec<_> = triangulations
        .iter()
        .filter(|value| core(value).is_empty())
        .cloned()
        .collect();
    assert_eq!(centers.len(), 2);

    let mut legs = BTreeMap::new();
    let mut original_jump_count = 0;
    let mut nonzero_facet_support = 0;
    for center in &centers {
        for &facet in &physical_facets {
            let (leg, corner) = saturated_tripod_leg(center, facet, &triangulations);
            route_homotopies(&corner, facet, &triangulations);
            // The original last edge [corner,b(F)] skips dimension one.
            assert_eq!(node_dimension(&Node::Vertex(corner)).abs_diff(2), 2);
            original_jump_count += 1;

            let supported: Vec<_> = leg
                .iter()
                .filter(|((first, second), _)| {
                    node_in_facet(first, facet) && node_in_facet(second, facet)
                })
                .collect();
            assert_eq!(supported.len(), 4);
            assert!(supported.iter().all(|(_, coefficient)| **coefficient == 1));
            nonzero_facet_support += supported.len();
            legs.insert((center.clone(), facet), leg);
        }
    }
    assert_eq!(original_jump_count, 6);
    assert_eq!(nonzero_facet_support, 24);

    // Reflection fixing a corner and its square exchanges the two saturated
    // flags.  If their weights are a,b, invariance says a=b and the endpoint
    // boundary says a+b=1.  The unique rational solution is 1/2,1/2.
    let integer_solutions: Vec<_> = (-4..=4)
        .flat_map(|twice_a| (-4..=4).map(move |twice_b| (twice_a, twice_b)))
        .filter(|&(twice_a, twice_b)| twice_a == twice_b && twice_a + twice_b == 2)
        .collect();
    assert_eq!(integer_solutions, vec![(1, 1)]);

    // Exact D_6 covariance of the saturated half-sum rule.
    for ((center, facet), leg) in &legs {
        for reflect in [false, true] {
            for amount in 0..N {
                let transformed_center = transform_triangulation(center, amount, reflect);
                let transformed_facet = rotate_diagonal(*facet, amount, reflect);
                assert_eq!(
                    transform_chain(leg, amount, reflect),
                    legs[&(transformed_center, transformed_facet)]
                );
            }
        }
    }

    // A general sum-zero tripod has exactly the desired doubled boundary.
    let coefficients = [2_i64, -5, 3];
    assert_eq!(coefficients.iter().sum::<i64>(), 0);
    for center in &centers {
        let mut tripod = Chain::new();
        for (&facet, &coefficient) in physical_facets.iter().zip(&coefficients) {
            for ((first, second), value) in &legs[&(center.clone(), facet)] {
                add(
                    &mut tripod,
                    first.clone(),
                    second.clone(),
                    coefficient * value,
                );
            }
        }
        let expected: BTreeMap<_, _> = physical_facets
            .iter()
            .copied()
            .zip(coefficients)
            .map(|(facet, coefficient)| (Node::Facet(facet), 2 * coefficient))
            .collect();
        assert_eq!(chain_boundary(&tripod), expected);
    }

    // One-step rotation exchanges the two parity centers.
    let rotated_centers: BTreeSet<_> = centers
        .iter()
        .map(|center| transform_triangulation(center, 1, false))
        .collect();
    assert_eq!(rotated_centers, centers.iter().cloned().collect());
    assert_ne!(transform_triangulation(&centers[0], 1, false), centers[0]);

    println!("six-point subdivision/PC incidence audit");
    println!("  original tripod tails with codimension-two jumps: 6");
    println!("  each corner/facet pair has exactly two saturated flags");
    println!("  reflection plus unit boundary uniquely forces weights (1/2,1/2)");
    println!("  the doubled saturated tripods have the exact entry-21 boundary");
    println!("  saturated half-sum minus the radial jump has an explicit rational 2-chain filler");
    println!("  the difference of the two integral route choices is also an exact boundary");
    println!("  every refined simplex edge is a codimension-one face incidence");
    println!("  the refinement is equivariant under all twelve D_6 elements");
    println!("  each leg retains four nonzero edge terms inside its physical facet");
    println!();
    println!("VERDICT: PARTIAL");
    println!("  the naive top-stratum map is mistyped on nonsaturated sd(K) edges");
    println!("  the six-point tripod has a unique rational saturated repair");
    println!("  physical residue-freeness still needs an occurrence/Gysin theorem");
}
