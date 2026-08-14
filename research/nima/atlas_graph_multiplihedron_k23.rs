//! Exact combinatorial atlas for the marked-theta graph multiplihedron.
//!
//! The five cubic vertices form `K_{2,3}`.  This program implements
//! Definitions 1, 3, and 5 and Corollary 7 of Devadoss--Forcey,
//! "Marked tubes and the graph multiplihedron" (arXiv:0807.4159): tubes are
//! nonempty connected induced vertex sets, every tubing contains the universal
//! tube, and a marked tubing has thin/thick/broken markings subject to the
//! marked nesting rule.  It also checks the facet products in Propositions 15
//! and 16 and audits all twelve spanning-tree presentations.
//!
//! This is a combinatorial certificate only.  It does not evaluate a Ward
//! differential or identify any Ward coefficient with a cellular boundary.

use std::collections::{BTreeMap, BTreeSet, VecDeque};

const N: usize = 5;
const ALL: u8 = (1 << N) - 1;

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum Mark {
    Thin,
    Thick,
    Broken,
}

#[derive(Clone, Debug)]
struct Graph {
    edges: BTreeSet<(usize, usize)>,
}

impl Graph {
    fn new(edges: &[(usize, usize)]) -> Self {
        Self {
            edges: edges.iter().map(|&(a, b)| ordered(a, b)).collect(),
        }
    }

    fn has_edge(&self, a: usize, b: usize) -> bool {
        self.edges.contains(&ordered(a, b))
    }

    fn connected(&self, mask: u8) -> bool {
        if mask == 0 {
            return false;
        }
        let start = mask.trailing_zeros() as usize;
        let mut seen = 1_u8 << start;
        let mut queue = VecDeque::from([start]);
        while let Some(a) = queue.pop_front() {
            for b in 0..N {
                let bit = 1_u8 << b;
                if mask & bit != 0 && seen & bit == 0 && self.has_edge(a, b) {
                    seen |= bit;
                    queue.push_back(b);
                }
            }
        }
        seen == mask
    }

    fn tubes(&self) -> Vec<u8> {
        (1..=ALL).filter(|&mask| self.connected(mask)).collect()
    }

    fn components(&self, mask: u8) -> Vec<u8> {
        let mut remaining = mask;
        let mut answer = Vec::new();
        while remaining != 0 {
            let start = remaining.trailing_zeros() as usize;
            let mut component = 1_u8 << start;
            let mut queue = VecDeque::from([start]);
            remaining &= !(1_u8 << start);
            while let Some(a) = queue.pop_front() {
                for b in 0..N {
                    let bit = 1_u8 << b;
                    if remaining & bit != 0 && self.has_edge(a, b) {
                        remaining &= !bit;
                        component |= bit;
                        queue.push_back(b);
                    }
                }
            }
            answer.push(component);
        }
        answer
    }

    fn edge_count_in(&self, mask: u8) -> usize {
        self.edges
            .iter()
            .filter(|&&(a, b)| mask & (1 << a) != 0 && mask & (1 << b) != 0)
            .count()
    }

    /// Edge count of Definition 14's reconnected complement G*(t).
    fn reconnected_complement_edges(&self, t: u8) -> usize {
        let outside: Vec<_> = (0..N).filter(|&v| t & (1 << v) == 0).collect();
        let mut count = 0;
        for i in 0..outside.len() {
            for j in i + 1..outside.len() {
                let pair = (1 << outside[i]) | (1 << outside[j]);
                if self.connected(pair) || self.connected(pair | t) {
                    count += 1;
                }
            }
        }
        count
    }
}

fn ordered(a: usize, b: usize) -> (usize, usize) {
    if a < b {
        (a, b)
    } else {
        (b, a)
    }
}

fn subset(a: u8, b: u8) -> bool {
    a & !b == 0
}

fn compatible_unmarked(graph: &Graph, a: u8, b: u8) -> bool {
    if subset(a, b) || subset(b, a) {
        return true;
    }
    if a & b != 0 {
        return false;
    }
    !graph.connected(a | b)
}

fn compatible_marked(a: (u8, Mark), b: (u8, Mark)) -> bool {
    let (inner, outer_mark) = if a.0 != b.0 && subset(a.0, b.0) {
        (a.1, b.1)
    } else if a.0 != b.0 && subset(b.0, a.0) {
        (b.1, a.1)
    } else {
        return true;
    };
    outer_mark == Mark::Thick || inner == Mark::Thin
}

fn enumerate_unmarked_tubings(graph: &Graph) -> Vec<Vec<u8>> {
    let proper: Vec<_> = graph.tubes().into_iter().filter(|&t| t != ALL).collect();
    let mut answer = Vec::new();
    fn visit(
        graph: &Graph,
        proper: &[u8],
        start: usize,
        chosen: &mut Vec<u8>,
        answer: &mut Vec<Vec<u8>>,
    ) {
        let mut tubing = vec![ALL];
        tubing.extend(chosen.iter().copied());
        tubing.sort_unstable();
        answer.push(tubing);
        for i in start..proper.len() {
            let candidate = proper[i];
            if chosen
                .iter()
                .all(|&old| compatible_unmarked(graph, old, candidate))
            {
                chosen.push(candidate);
                visit(graph, proper, i + 1, chosen, answer);
                chosen.pop();
            }
        }
    }
    visit(graph, &proper, 0, &mut Vec::new(), &mut answer);
    answer
}

fn face_vector(graph: &Graph) -> ([usize; N + 1], usize) {
    let tubings = enumerate_unmarked_tubings(graph);
    let mut by_dimension = [0_usize; N + 1];
    let mut marked_total = 0;
    for tubes in &tubings {
        let assignments = 3_usize.pow(tubes.len() as u32);
        for code in 0..assignments {
            let mut rest = code;
            let marked: Vec<_> = tubes
                .iter()
                .map(|&tube| {
                    let mark = match rest % 3 {
                        0 => Mark::Thin,
                        1 => Mark::Thick,
                        _ => Mark::Broken,
                    };
                    rest /= 3;
                    (tube, mark)
                })
                .collect();
            let valid = (0..marked.len())
                .all(|i| (i + 1..marked.len()).all(|j| compatible_marked(marked[i], marked[j])));
            if valid {
                let codimension = marked.iter().filter(|tube| tube.1 != Mark::Broken).count();
                assert!(codimension <= N);
                by_dimension[N - codimension] += 1;
                marked_total += 1;
            }
        }
    }
    (by_dimension, marked_total)
}

fn facet_counts(graph: &Graph) -> (usize, usize) {
    let mut upper = 0;
    let mut lower = 0;
    for tubes in enumerate_unmarked_tubings(graph) {
        for code in 0..3_usize.pow(tubes.len() as u32) {
            let mut rest = code;
            let marked: Vec<_> = tubes
                .iter()
                .map(|&tube| {
                    let mark = match rest % 3 {
                        0 => Mark::Thin,
                        1 => Mark::Thick,
                        _ => Mark::Broken,
                    };
                    rest /= 3;
                    (tube, mark)
                })
                .collect();
            if !(0..marked.len())
                .all(|i| (i + 1..marked.len()).all(|j| compatible_marked(marked[i], marked[j])))
            {
                continue;
            }
            let unbroken: Vec<_> = marked
                .iter()
                .filter(|tube| tube.1 != Mark::Broken)
                .collect();
            if unbroken.len() == 1 {
                match unbroken[0].1 {
                    Mark::Thick => {
                        assert_eq!(unbroken[0].0, ALL);
                        upper += 1;
                    }
                    Mark::Thin => lower += 1,
                    Mark::Broken => unreachable!(),
                }
            }
        }
    }
    (upper, lower)
}

fn cube_face_vector() -> [usize; N + 1] {
    let mut answer = [0; N + 1];
    for dimension in 0..=N {
        answer[dimension] = binomial(N, dimension) * (1 << (N - dimension));
    }
    answer
}

fn binomial(n: usize, k: usize) -> usize {
    (0..k).fold(1, |value, i| value * (n - i) / (i + 1))
}

fn mask_name(mask: u8) -> String {
    const LABELS: [&str; N] = ["L0", "L1", "R0", "R1", "R2"];
    let names: Vec<_> = (0..N)
        .filter(|&v| mask & (1 << v) != 0)
        .map(|v| LABELS[v])
        .collect();
    format!("{{{}}}", names.join(","))
}

fn k23_edges() -> Vec<(usize, usize)> {
    let mut edges = Vec::new();
    for left in 0..2 {
        for right in 2..5 {
            edges.push((left, right));
        }
    }
    edges
}

fn print_full_facet_atlas(graph: &Graph) {
    println!("LOWER FACETS (thin tube t; J(G*(t)) x K(G(t)))");
    for t in graph.tubes() {
        let size = t.count_ones() as usize;
        if t == ALL {
            println!("  t={:<18} K(G), dimensions 4", mask_name(t));
        } else {
            println!(
                "  t={:<18} |t|={} E(G(t))={} ; J(G*(t))[n={},E={}] x K(G(t)); dimensions {}+{}=4",
                mask_name(t),
                size,
                graph.edge_count_in(t),
                N - size,
                graph.reconnected_complement_edges(t),
                N - size,
                size - 1,
            );
        }
    }

    println!("UPPER FACETS (nonempty root set A; broken components of V\\A)");
    for root in 1..=ALL {
        let broken_union = ALL & !root;
        let components = graph.components(broken_union);
        let sizes: Vec<_> = components.iter().map(|c| c.count_ones()).collect();
        println!(
            "  A={:<18} broken={:<18} components={:?}; K(G*(broken))[n={},E={}] x prod J(component); dimensions {}+{}=4",
            mask_name(root),
            mask_name(broken_union),
            sizes,
            root.count_ones(),
            graph.reconnected_complement_edges(broken_union),
            root.count_ones() - 1,
            broken_union.count_ones(),
        );
    }
}

fn spanning_tree_audit(full: &Graph, edges: &[(usize, usize)]) {
    let mut presentations = 0;
    let mut shared_endpoint = 0;
    let mut disjoint_endpoint = 0;
    let mut intersecting_tubes = 0;
    let mut adjacent_tubes = 0;
    let mut union_tube_before = 0;
    let mut union_tube_after_one = 0;
    let mut one_edge_factor_edges: BTreeMap<usize, usize> = BTreeMap::new();
    let mut tree_vectors: BTreeMap<[usize; N + 1], usize> = BTreeMap::new();
    let mut one_edge_vectors: BTreeMap<[usize; N + 1], usize> = BTreeMap::new();

    println!("TWELVE SPANNING-TREE PRESENTATIONS");
    for i in 0..edges.len() {
        for j in i + 1..edges.len() {
            let missing = [edges[i], edges[j]];
            let kept: Vec<_> = edges
                .iter()
                .copied()
                .filter(|edge| !missing.contains(edge))
                .collect();
            let tree = Graph::new(&kept);
            if !tree.connected(ALL) {
                continue;
            }
            presentations += 1;
            let a = (1 << missing[0].0) | (1 << missing[0].1);
            let b = (1 << missing[1].0) | (1 << missing[1].1);
            let relation = if a & b != 0 {
                shared_endpoint += 1;
                intersecting_tubes += 1;
                "intersect"
            } else {
                disjoint_endpoint += 1;
                assert!(full.connected(a | b));
                adjacent_tubes += 1;
                "are adjacent"
            };
            assert!(!tree.connected(a) && !tree.connected(b));
            if tree.connected(a | b) {
                union_tube_before += 1;
            }

            let first_edges: Vec<_> = kept.iter().copied().chain([missing[0]]).collect();
            let after_first = Graph::new(&first_edges);
            assert!(after_first.connected(a));
            assert!(!after_first.connected(b));
            if after_first.connected(a | b) {
                union_tube_after_one += 1;
            }
            let factor_edges = after_first.reconnected_complement_edges(a);
            *one_edge_factor_edges.entry(factor_edges).or_default() += 1;

            let tree_f = face_vector(&tree).0;
            let one_f = face_vector(&after_first).0;
            *tree_vectors.entry(tree_f).or_default() += 1;
            *one_edge_vectors.entry(one_f).or_default() += 1;

            println!(
                "  missing {} and {}: not tubes in T, become tubes when sewn, and {} in K23; union tube T={} after-first={} full=true; first lower product J(G1*(e))[n=3,E={}] x K(K2), final E=3",
                mask_name(a),
                mask_name(b),
                relation,
                tree.connected(a | b),
                after_first.connected(a | b),
                factor_edges,
            );
        }
    }
    println!("STAGED FACE VECTORS (dimension 0..5 => multiplicity)");
    println!("  trees: {:?}", tree_vectors);
    println!("  after one sewing: {:?}", one_edge_vectors);
    println!(
        "  one-sewing lower-factor G1*(e) edge counts: {:?}",
        one_edge_factor_edges
    );
    println!(
        "  pair classes: shared={} disjoint={}; final tube relations intersect={} adjacent={}; union tube before={} after chosen first={} after both=12",
        shared_endpoint,
        disjoint_endpoint,
        intersecting_tubes,
        adjacent_tubes,
        union_tube_before,
        union_tube_after_one,
    );

    assert_eq!(presentations, 12);
    assert_eq!((shared_endpoint, disjoint_endpoint), (6, 6));
    assert_eq!((intersecting_tubes, adjacent_tubes), (6, 6));
    assert_eq!(union_tube_before, 0);
    assert_eq!(union_tube_after_one, 6);
    assert_eq!(one_edge_factor_edges, BTreeMap::from([(2, 6), (3, 6)]));
    assert_eq!(
        tree_vectors,
        BTreeMap::from([
            ([322, 841, 788, 313, 46, 1], 6),
            ([364, 942, 870, 338, 48, 1], 6),
        ])
    );
    assert_eq!(
        one_edge_vectors,
        BTreeMap::from([([462, 1180, 1064, 396, 52, 1], 12)])
    );
}

fn main() {
    let edges = k23_edges();
    let graph = Graph::new(&edges);
    let tubes = graph.tubes();
    let proper_tubes = tubes.iter().filter(|&&t| t != ALL).count();
    let (full_faces, marked_total) = face_vector(&graph);
    let (upper_facets, lower_facets) = facet_counts(&graph);
    let cube_faces = cube_face_vector();
    let alternating_sum: isize = full_faces
        .iter()
        .enumerate()
        .map(|(d, &count)| {
            if d % 2 == 0 {
                count as isize
            } else {
                -(count as isize)
            }
        })
        .sum();

    println!("J(K_{{2,3}}) EXACT ATLAS");
    println!("  vertices/nodes: 5; polytope dimension: 5");
    println!(
        "  connected induced tubes: {} ({} proper + universal)",
        tubes.len(),
        proper_tubes
    );
    println!(
        "  unmarked tubings: {}",
        enumerate_unmarked_tubings(&graph).len()
    );
    println!("  marked tubings/faces: {}", marked_total);
    println!("  full J face vector by dimension 0..5: {:?}", full_faces);
    println!("  strict-domain/strict-range cube:       {:?}", cube_faces);
    println!(
        "  facets: full={} (upper={}, lower={}), cube={}",
        full_faces[N - 1],
        upper_facets,
        lower_facets,
        cube_faces[N - 1]
    );
    println!("  Euler alternating sum: {}", alternating_sum);

    assert_eq!(tubes.len(), 26);
    assert_eq!(proper_tubes, 25);
    assert_eq!(full_faces[N], 1);
    assert_eq!(full_faces[N - 1], 57);
    assert_eq!((upper_facets, lower_facets), (31, 26));
    assert_eq!(cube_faces[N - 1], 10);
    assert_eq!(alternating_sum, 1);

    print_full_facet_atlas(&graph);
    spanning_tree_audit(&graph, &edges);

    println!("COMBINATORIAL VERDICT");
    println!("  The 31 nonempty vertex subsets match the 31 upper facets exactly.");
    println!(
        "  The full polytope is sharply distinct from its 5-cube quotient (57 versus 10 facets). "
    );
    println!(
        "  Dimension-five/all-coordinate support alone is shared by both and selects neither."
    );
    println!("  No Ward-to-cell evaluation was performed; matching 31 gauge-tail subsets to the upper-facet incidence remains a test.");
}
