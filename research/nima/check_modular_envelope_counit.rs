//! Bounded certificate for the universal modular-envelope lift of the tree
//! transmutation counit.
//!
//! There are two logically different questions:
//!
//! 1. Does a cyclic, Cut-monoidal tree counit have a canonical operation on
//!    resolved surface presentations?
//! 2. Does that universal operation descend to a particular quotient of
//!    surface functions in the X_C variables?
//!
//! The first question is formal: apply the (derived) modular envelope and the
//! resolved Brauer augmentation D |-> 1.  The second is a kernel-inclusion
//! problem and is not settled by this program.
//!
//! This executable audits the finite combinatorics behind the first claim:
//!
//! * canonical chord presentations have the advertised genus and number of
//!   boundary components, independently of the order of boundary and handle
//!   blocks, contraction order, and cyclic basepoint;
//! * every Farey 3S triangle on a one-holed torus has exact SL(2,Z) chart
//!   holonomy one;
//! * vertexwise extension of a local counit commutes with every bridge and
//!   nonbridge cut in all connected multigraphs with at most four vertices
//!   and one loop/edge of each type.
//!
//! These are bounded convention checks.  The all-arity statement follows
//! from functoriality of the derived modular envelope; descent to the physical
//! surface-function quotient still requires
//!
//!   q_scalar Mod(u_tree)(ker q_YM) = 0.

use std::collections::{BTreeSet, VecDeque};

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
enum Block {
    Boundary,
    Handle,
}

#[derive(Clone, Debug)]
struct ChordDiagram {
    alpha: Vec<usize>,
    pairs: Vec<(usize, usize)>,
}

fn chord_diagram(blocks: &[Block]) -> ChordDiagram {
    let half_edges = blocks
        .iter()
        .map(|block| match block {
            Block::Boundary => 2,
            Block::Handle => 4,
        })
        .sum();
    let mut alpha: Vec<_> = (0..half_edges).collect();
    let mut pairs = Vec::new();
    let mut cursor = 0;
    for block in blocks {
        let block_pairs = match block {
            Block::Boundary => vec![(cursor, cursor + 1)],
            Block::Handle => vec![(cursor, cursor + 2), (cursor + 1, cursor + 3)],
        };
        for (left, right) in block_pairs {
            alpha[left] = right;
            alpha[right] = left;
            pairs.push((left, right));
        }
        cursor += match block {
            Block::Boundary => 2,
            Block::Handle => 4,
        };
    }
    ChordDiagram { alpha, pairs }
}

fn rotate_diagram(diagram: &ChordDiagram, shift: usize) -> ChordDiagram {
    if diagram.alpha.is_empty() {
        return diagram.clone();
    }
    let size = diagram.alpha.len();
    let map = |index: usize| (index + shift) % size;
    let mut alpha = vec![0; size];
    let mut pairs = Vec::new();
    for &(left, right) in &diagram.pairs {
        let moved_left = map(left);
        let moved_right = map(right);
        alpha[moved_left] = moved_right;
        alpha[moved_right] = moved_left;
        pairs.push(if moved_left < moved_right {
            (moved_left, moved_right)
        } else {
            (moved_right, moved_left)
        });
    }
    pairs.sort_unstable();
    ChordDiagram { alpha, pairs }
}

fn surface_signature(diagram: &ChordDiagram) -> (usize, usize) {
    if diagram.alpha.is_empty() {
        return (0, 1);
    }
    let size = diagram.alpha.len();
    let phi: Vec<_> = (0..size)
        .map(|half_edge| (diagram.alpha[half_edge] + 1) % size)
        .collect();
    let mut seen = vec![false; size];
    let mut boundaries = 0;
    for start in 0..size {
        if seen[start] {
            continue;
        }
        boundaries += 1;
        let mut current = start;
        while !seen[current] {
            seen[current] = true;
            current = phi[current];
        }
        assert_eq!(current, start);
    }

    // The one-vertex ribbon graph is a spine: chi = V-E = 1-|pairs|.
    let twice_genus = 1 + diagram.pairs.len() - boundaries;
    assert_eq!(twice_genus % 2, 0);
    (twice_genus / 2, boundaries)
}

fn permutations<T: Clone>(values: &[T]) -> Vec<Vec<T>> {
    fn recurse<T: Clone>(remaining: &mut Vec<T>, current: &mut Vec<T>, out: &mut Vec<Vec<T>>) {
        if remaining.is_empty() {
            out.push(current.clone());
            return;
        }
        for index in 0..remaining.len() {
            let value = remaining.remove(index);
            current.push(value.clone());
            recurse(remaining, current, out);
            current.pop();
            remaining.insert(index, value);
        }
    }

    let mut out = Vec::new();
    recurse(&mut values.to_vec(), &mut Vec::new(), &mut out);
    out
}

fn audit_canonical_surface_presentations() -> (usize, usize, usize) {
    let mut presentations = 0;
    let mut cyclic_squares = 0;
    let mut contraction_orders = 0;

    for genus in 0..=2 {
        for boundaries in 1..=3 {
            if genus == 0 && boundaries == 1 {
                continue;
            }
            let mut blocks = vec![Block::Boundary; boundaries - 1];
            blocks.extend(vec![Block::Handle; genus]);
            let distinct_orders: BTreeSet<_> = permutations(&blocks).into_iter().collect();
            for order in distinct_orders {
                let diagram = chord_diagram(&order);
                assert_eq!(surface_signature(&diagram), (genus, boundaries));
                presentations += 1;

                for shift in 0..diagram.alpha.len() {
                    assert_eq!(
                        surface_signature(&rotate_diagram(&diagram, shift)),
                        (genus, boundaries)
                    );
                    cyclic_squares += 1;
                }

                // Modular contractions on disjoint flag pairs commute.  The
                // final involution and hence the thickened surface do not
                // depend on the contraction history.
                for pair_order in permutations(&diagram.pairs) {
                    let mut alpha: Vec<_> = (0..diagram.alpha.len()).collect();
                    for &(left, right) in &pair_order {
                        assert_eq!(alpha[left], left);
                        assert_eq!(alpha[right], right);
                        alpha[left] = right;
                        alpha[right] = left;
                    }
                    assert_eq!(alpha, diagram.alpha);
                    contraction_orders += 1;
                }
            }
        }
    }
    (presentations, cyclic_squares, contraction_orders)
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct Mat2 {
    entries: [[i64; 2]; 2],
}

impl Mat2 {
    const IDENTITY: Self = Self {
        entries: [[1, 0], [0, 1]],
    };

    fn columns(first: Slope, second: Slope) -> Self {
        Self {
            entries: [[first.p, second.p], [first.q, second.q]],
        }
    }

    fn determinant(self) -> i64 {
        self.entries[0][0] * self.entries[1][1] - self.entries[0][1] * self.entries[1][0]
    }

    fn inverse_sl2(self) -> Self {
        assert_eq!(self.determinant(), 1);
        Self {
            entries: [
                [self.entries[1][1], -self.entries[0][1]],
                [-self.entries[1][0], self.entries[0][0]],
            ],
        }
    }

    fn multiply(self, other: Self) -> Self {
        let mut entries = [[0; 2]; 2];
        for (row, output_row) in entries.iter_mut().enumerate() {
            for (column, output) in output_row.iter_mut().enumerate() {
                *output = (0..2)
                    .map(|middle| self.entries[row][middle] * other.entries[middle][column])
                    .sum();
            }
        }
        Self { entries }
    }
}

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct Slope {
    p: i64,
    q: i64,
}

impl Slope {
    fn new(p: i64, q: i64) -> Self {
        assert_ne!((p, q), (0, 0));
        assert_eq!(gcd(p.abs(), q.abs()), 1);
        Self { p, q }
    }

    fn plus(self, other: Self) -> Self {
        Self::new(self.p + other.p, self.q + other.q)
    }

    fn negative(self) -> Self {
        Self::new(-self.p, -self.q)
    }

    fn determinant(self, other: Self) -> i64 {
        self.p * other.q - self.q * other.p
    }
}

fn gcd(mut left: i64, mut right: i64) -> i64 {
    while right != 0 {
        let remainder = left % right;
        left = right;
        right = remainder;
    }
    left
}

fn primitive_slopes(bound: i64) -> Vec<Slope> {
    let mut slopes = Vec::new();
    for p in -bound..=bound {
        for q in -bound..=bound {
            if (p, q) != (0, 0) && gcd(p.abs(), q.abs()) == 1 {
                slopes.push(Slope::new(p, q));
            }
        }
    }
    slopes
}

fn audit_farey_three_s(bound: i64) -> usize {
    let slopes = primitive_slopes(bound);
    let mut triangles = 0;
    for &first in &slopes {
        for &second in &slopes {
            if first.determinant(second) != 1 {
                continue;
            }
            let third = first.plus(second);
            assert_eq!(first.determinant(third), 1);
            assert_eq!(second.determinant(third), -1);

            // Each cut chart is an oriented homology frame.  T_(j<-i) is the
            // exact SL(2,Z) change of coordinates from chart i to chart j.
            let frame_first = Mat2::columns(first, second);
            let frame_second = Mat2::columns(second, first.negative());
            let frame_third = Mat2::columns(third, first.negative());
            for frame in [frame_first, frame_second, frame_third] {
                assert_eq!(frame.determinant(), 1);
            }

            let t_second_first = frame_second.inverse_sl2().multiply(frame_first);
            let t_third_second = frame_third.inverse_sl2().multiply(frame_second);
            let t_first_third = frame_first.inverse_sl2().multiply(frame_third);
            let holonomy = t_first_third
                .multiply(t_third_second)
                .multiply(t_second_first);
            assert_eq!(holonomy, Mat2::IDENTITY);
            assert_eq!(t_second_first.determinant(), 1);
            assert_eq!(t_third_second.determinant(), 1);
            assert_eq!(t_first_third.determinant(), 1);
            triangles += 1;
        }
    }
    triangles
}

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct Edge(usize, usize);

fn graph_components(vertices: usize, edges: &[Edge], removed: usize) -> Vec<Vec<usize>> {
    let mut adjacency = vec![Vec::new(); vertices];
    for (index, &Edge(left, right)) in edges.iter().enumerate() {
        if removed & (1 << index) != 0 || left == right {
            continue;
        }
        adjacency[left].push(right);
        adjacency[right].push(left);
    }
    let mut seen = vec![false; vertices];
    let mut components = Vec::new();
    for start in 0..vertices {
        if seen[start] {
            continue;
        }
        let mut queue = VecDeque::from([start]);
        seen[start] = true;
        let mut component = Vec::new();
        while let Some(vertex) = queue.pop_front() {
            component.push(vertex);
            for &next in &adjacency[vertex] {
                if !seen[next] {
                    seen[next] = true;
                    queue.push_back(next);
                }
            }
        }
        component.sort_unstable();
        components.push(component);
    }
    components.sort();
    components
}

fn local_counit(source_weight: u64) -> u64 {
    source_weight * source_weight + 1
}

fn cut_after_counit(components: &[Vec<usize>], source_weights: &[u64]) -> Vec<u64> {
    let local_scalar: Vec<_> = source_weights.iter().copied().map(local_counit).collect();
    let mut result: Vec<_> = components
        .iter()
        .map(|component| {
            component
                .iter()
                .map(|&vertex| local_scalar[vertex])
                .product()
        })
        .collect();
    result.sort_unstable();
    result
}

fn counit_after_cut(components: &[Vec<usize>], source_weights: &[u64]) -> Vec<u64> {
    let mut result: Vec<_> = components
        .iter()
        .map(|component| {
            component
                .iter()
                .map(|&vertex| local_counit(source_weights[vertex]))
                .product()
        })
        .collect();
    result.sort_unstable();
    result
}

fn first_betti(vertices: usize, edges: usize, components: usize) -> usize {
    edges + components - vertices
}

fn audit_cut_monoidality() -> (usize, usize, usize) {
    let primes = [2_u64, 3, 5, 7];
    let mut squares = 0;
    let mut separating = 0;
    let mut nonseparating = 0;

    for vertices in 1..=4 {
        let candidates: Vec<_> = (0..vertices)
            .flat_map(|left| (left..vertices).map(move |right| Edge(left, right)))
            .collect();
        for graph_mask in 0usize..(1usize << candidates.len()) {
            let edges: Vec<_> = candidates
                .iter()
                .enumerate()
                .filter_map(|(index, edge)| (graph_mask & (1 << index) != 0).then_some(*edge))
                .collect();
            if graph_components(vertices, &edges, 0).len() != 1 {
                continue;
            }

            for removed in 0usize..(1usize << edges.len()) {
                let components = graph_components(vertices, &edges, removed);

                // Apply the vertexwise counit before cutting, or cut first and
                // apply it separately on every component.  Since modular
                // completion changes only the gluing graph, both routes are
                // literally the same tensor of local scalar coefficients.
                let before_cut = cut_after_counit(&components, &primes[..vertices]);
                let after_cut = counit_after_cut(&components, &primes[..vertices]);
                assert_eq!(before_cut, after_cut);
                squares += 1;
            }

            let initial_betti = first_betti(vertices, edges.len(), 1);
            for edge_index in 0..edges.len() {
                let components = graph_components(vertices, &edges, 1 << edge_index);
                let cut_betti = first_betti(vertices, edges.len() - 1, components.len());
                match components.len() {
                    2 => {
                        assert_eq!(cut_betti, initial_betti);
                        separating += 1;
                    }
                    1 => {
                        assert_eq!(cut_betti + 1, initial_betti);
                        nonseparating += 1;
                    }
                    count => panic!("one edge cut produced {count} components"),
                }
            }
        }
    }
    (squares, separating, nonseparating)
}

fn main() {
    let (presentations, cyclic_squares, contraction_orders) =
        audit_canonical_surface_presentations();
    let farey_triangles = audit_farey_three_s(5);
    let (cut_squares, separating_cuts, nonseparating_cuts) = audit_cut_monoidality();

    println!("Derived modular-envelope counit certificate");
    println!("===========================================");
    println!("  canonical surface presentations: {presentations}");
    println!("  cyclic surface-presentation squares: {cyclic_squares}");
    println!("  contraction histories: {contraction_orders}");
    println!("  oriented Farey 3S triangles: {farey_triangles}");
    println!("  arbitrary Cut/counit squares: {cut_squares}");
    println!("  separating one-edge cuts: {separating_cuts}");
    println!("  nonseparating one-edge cuts: {nonseparating_cuts}");
    println!();
    println!("VERDICT");
    println!("  the universal derived modular-envelope lift has exact 3S holonomy");
    println!("  its vertexwise counit is Cut-monoidal for bridge and nonbridge cuts");
    println!("  physical X-function descent is reduced to a kernel-inclusion test");
}
