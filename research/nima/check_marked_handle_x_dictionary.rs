//! Open-path -> surface-X dictionary and complete five-vertex YM LS audit.
//!
//! The graph is the marked theta handle of entry 50, with one external gluon
//! on each theta road.  Attaching the three scalar-scaffold vertices gives an
//! eight-vertex trivalent ribbon graph with six scalar boundary legs.
//!
//! This certificate performs three logically separate constructions:
//!
//! 1. It expands every open polarization-contraction path by the literal
//!    Carrôlo--Figueiredo endpoint rule
//!
//!      C -> X_(b,d) + X_(a,c) - X_(b,c) - X_(a,d),
//!
//!    generating the endpoint extensions by "left forever" or "right once,
//!    then left forever" on the ribbon graph.  Curve variables are keyed by
//!    their boundary endpoints and reduced signed edge word, so homotopically
//!    distinct handle curves remain distinct.
//!
//! 2. It retains every extension origin and its (-1)^N_e sign, sums equal
//!    monomials, and records exact cancellations.  The same implementation is
//!    first calibrated on the scalar-scaffolded three-gluon vertex, where it
//!    must reproduce the documented six-term X polynomial.
//!
//! 3. Independently, it contracts the five ordinary three-gluon tensors at an
//!    exact rational six-dimensional split-signature point.  The all-metric
//!    network is resolved into all 243 local sectors, while the physical loop
//!    state sum inserts transverse projectors on the two closing edges for all
//!    twelve spanning-tree presentations.  The presentation-independent
//!    physical answer is compared with the full X polynomial after the
//!    resolved circuit value nu-Delta=D and the four-path normalization.

use std::collections::{BTreeMap, BTreeSet, VecDeque};

type Int = i128;
const DIM: usize = 6;

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct HalfEdge {
    vertex: usize,
    position: usize,
}

impl HalfEdge {
    fn new(vertex: usize, position: usize) -> Self {
        assert!(position < 3);
        Self { vertex, position }
    }

    fn id(self) -> usize {
        3 * self.vertex + self.position
    }
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct Edge {
    first: HalfEdge,
    second: HalfEdge,
    scaffold: bool,
}

#[derive(Clone, Debug)]
struct RibbonGraph {
    ym_vertices: usize,
    vertices: usize,
    edges: Vec<Edge>,
    edge_at: Vec<Option<(usize, HalfEdge)>>,
    external_labels: BTreeMap<HalfEdge, usize>,
}

impl RibbonGraph {
    fn from_edges(ym_vertices: usize, vertices: usize, edges: Vec<Edge>) -> Self {
        let mut edge_at = vec![None; 3 * vertices];
        for (edge_index, edge) in edges.iter().enumerate() {
            assert!(edge.first.vertex < vertices && edge.second.vertex < vertices);
            assert!(edge_at[edge.first.id()].is_none());
            assert!(edge_at[edge.second.id()].is_none());
            edge_at[edge.first.id()] = Some((edge_index, edge.second));
            edge_at[edge.second.id()] = Some((edge_index, edge.first));
        }

        let external: Vec<_> = (0..vertices)
            .flat_map(|vertex| (0..3).map(move |position| HalfEdge::new(vertex, position)))
            .filter(|half| edge_at[half.id()].is_none())
            .collect();
        assert!(!external.is_empty());

        let sigma = |half: HalfEdge| HalfEdge::new(half.vertex, (half.position + 1) % 3);
        let alpha = |half: HalfEdge| edge_at[half.id()].map(|(_, other)| other).unwrap_or(half);
        let phi = |half: HalfEdge| sigma(alpha(half));

        let start = *external.iter().min().unwrap();
        let mut boundary = Vec::new();
        let mut seen = BTreeSet::new();
        let mut current = start;
        while seen.insert(current) {
            if edge_at[current.id()].is_none() {
                boundary.push(current);
            }
            current = phi(current);
        }
        assert_eq!(current, start);
        assert_eq!(seen.len(), 3 * vertices);
        assert_eq!(boundary.len(), external.len());

        let external_labels = boundary
            .into_iter()
            .enumerate()
            .map(|(index, half)| (half, index + 1))
            .collect();
        Self {
            ym_vertices,
            vertices,
            edges,
            edge_at,
            external_labels,
        }
    }

    fn three_point() -> Self {
        // Vertex 0 is the gluon cubic vertex.  Vertices 1,2,3 are the
        // scalar-scaffold vertices; their positions 1,2 are boundary scalars.
        let edges = (0..3)
            .map(|leg| Edge {
                first: HalfEdge::new(0, leg),
                second: HalfEdge::new(1 + leg, 0),
                scaffold: true,
            })
            .collect();
        Self::from_edges(1, 4, edges)
    }

    fn marked_theta() -> Self {
        // YM vertices: left core 0, right core 1, marked road vertices 2..=4.
        // Scaffold vertices are 5..=7.
        let mut edges = Vec::new();
        for road in 0..3 {
            let middle = 2 + road;
            edges.push(Edge {
                first: HalfEdge::new(0, road),
                second: HalfEdge::new(middle, 0),
                scaffold: false,
            });
            edges.push(Edge {
                first: HalfEdge::new(1, road),
                second: HalfEdge::new(middle, 2),
                scaffold: false,
            });
            edges.push(Edge {
                first: HalfEdge::new(middle, 1),
                second: HalfEdge::new(5 + road, 0),
                scaffold: true,
            });
        }
        Self::from_edges(5, 8, edges)
    }

    fn other_end(&self, half: HalfEdge) -> Option<(usize, HalfEdge, i16)> {
        self.edge_at[half.id()].map(|(edge_index, other)| {
            let edge = self.edges[edge_index];
            let direction = if half == edge.first { 1 } else { -1 };
            (edge_index, other, direction * (edge_index as i16 + 1))
        })
    }

    fn patterns(&self) -> Vec<Vec<usize>> {
        let total = 3_usize.pow(self.ym_vertices as u32);
        (0..total)
            .map(|mut code| {
                let mut pattern = Vec::with_capacity(self.ym_vertices);
                for _ in 0..self.ym_vertices {
                    pattern.push(code % 3);
                    code /= 3;
                }
                pattern
            })
            .collect()
    }
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum EndpointChoice {
    // This endpoint choice leaves the full contraction as the core.
    RightThenLeft,
    // This endpoint choice trims one extension from the core.
    LeftForever,
}

impl EndpointChoice {
    const BOTH: [Self; 2] = [Self::RightThenLeft, Self::LeftForever];

    fn extension_count(self) -> usize {
        usize::from(self == Self::LeftForever)
    }
}

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct RedEndpoint {
    vertex: usize,
    incoming_position: usize,
}

#[derive(Clone, Debug, Eq, PartialEq)]
struct OpenComponent {
    first: RedEndpoint,
    second: RedEndpoint,
    // Signed graph-edge word from the first red endpoint to the second.
    interior: Vec<i16>,
}

#[derive(Clone, Debug, Eq, PartialEq)]
struct StatePattern {
    open: Vec<OpenComponent>,
    circuits: usize,
}

#[derive(Clone, Copy, Debug)]
enum LinkKind {
    Local,
    Graph(i16),
}

fn add_link(adjacency: &mut [Vec<(usize, LinkKind)>], a: usize, b: usize, kind: LinkKind) {
    adjacency[a].push((b, kind));
    let reverse = match kind {
        LinkKind::Local => LinkKind::Local,
        LinkKind::Graph(token) => LinkKind::Graph(-token),
    };
    adjacency[b].push((a, reverse));
}

fn state_pattern(graph: &RibbonGraph, pattern: &[usize]) -> StatePattern {
    assert_eq!(pattern.len(), graph.ym_vertices);
    let half_count = 3 * graph.vertices;
    let red_count = graph.vertices;
    let total_nodes = half_count + red_count;
    let red_node = |vertex: usize| half_count + vertex;
    let mut adjacency = vec![Vec::new(); total_nodes];
    let mut active = BTreeSet::new();

    for (vertex, &singleton) in pattern.iter().enumerate() {
        let red = red_node(vertex);
        let single = HalfEdge::new(vertex, singleton).id();
        add_link(&mut adjacency, red, single, LinkKind::Local);
        active.insert(red);
        active.insert(single);
        let paired: Vec<_> = (0..3).filter(|&position| position != singleton).collect();
        let a = HalfEdge::new(vertex, paired[0]).id();
        let b = HalfEdge::new(vertex, paired[1]).id();
        add_link(&mut adjacency, a, b, LinkKind::Local);
        active.insert(a);
        active.insert(b);
    }

    // A scalar-scaffold vertex terminates the gluon polarization on its red
    // momentum handle.  Its two scalar flags remain boundary exits.
    for vertex in graph.ym_vertices..graph.vertices {
        let red = red_node(vertex);
        let gluon = HalfEdge::new(vertex, 0).id();
        add_link(&mut adjacency, red, gluon, LinkKind::Local);
        active.insert(red);
        active.insert(gluon);
    }

    for (edge_index, edge) in graph.edges.iter().enumerate() {
        let token = edge_index as i16 + 1;
        add_link(
            &mut adjacency,
            edge.first.id(),
            edge.second.id(),
            LinkKind::Graph(token),
        );
        active.insert(edge.first.id());
        active.insert(edge.second.id());
    }

    for &node in &active {
        let degree = adjacency[node].len();
        if node >= half_count {
            assert_eq!(degree, 1);
        } else {
            assert_eq!(degree, 2);
        }
    }

    let mut seen = BTreeSet::new();
    let mut open = Vec::new();
    let mut circuits = 0;
    for &start in &active {
        if seen.contains(&start) {
            continue;
        }
        let mut queue = VecDeque::from([start]);
        seen.insert(start);
        let mut nodes = Vec::new();
        let mut reds = Vec::new();
        while let Some(node) = queue.pop_front() {
            nodes.push(node);
            if node >= half_count {
                reds.push(node - half_count);
            }
            for &(next, _) in &adjacency[node] {
                if seen.insert(next) {
                    queue.push_back(next);
                }
            }
        }
        match reds.len() {
            0 => circuits += 1,
            2 => {
                reds.sort_unstable();
                let first_vertex = reds[0];
                let second_vertex = reds[1];
                let mut current = red_node(first_vertex);
                let target = red_node(second_vertex);
                let mut previous = None;
                let mut interior = Vec::new();
                while current != target {
                    let &(next, kind) = adjacency[current]
                        .iter()
                        .find(|(next, _)| Some(*next) != previous)
                        .unwrap();
                    if let LinkKind::Graph(token) = kind {
                        interior.push(token);
                    }
                    previous = Some(current);
                    current = next;
                }
                let incoming = |vertex: usize| {
                    if vertex < graph.ym_vertices {
                        pattern[vertex]
                    } else {
                        0
                    }
                };
                open.push(OpenComponent {
                    first: RedEndpoint {
                        vertex: first_vertex,
                        incoming_position: incoming(first_vertex),
                    },
                    second: RedEndpoint {
                        vertex: second_vertex,
                        incoming_position: incoming(second_vertex),
                    },
                    interior,
                });
            }
            count => panic!("state component has {count} red endpoints"),
        }
    }
    open.sort_by_key(|component| (component.first, component.second));
    assert_eq!(open.len(), graph.vertices / 2);
    StatePattern { open, circuits }
}

#[derive(Clone, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct CurveLabel {
    first_boundary: usize,
    second_boundary: usize,
    edge_word: Vec<i16>,
}

fn invert_word(word: &[i16]) -> Vec<i16> {
    word.iter().rev().map(|token| -*token).collect()
}

fn reduce_word(word: Vec<i16>) -> Vec<i16> {
    let mut reduced = Vec::new();
    for token in word {
        if reduced.last().copied() == Some(-token) {
            reduced.pop();
        } else {
            reduced.push(token);
        }
    }
    reduced
}

impl CurveLabel {
    fn canonical(first_boundary: usize, edge_word: Vec<i16>, second_boundary: usize) -> Self {
        let edge_word = reduce_word(edge_word);
        let forward = (first_boundary, edge_word.clone(), second_boundary);
        let reverse = (second_boundary, invert_word(&edge_word), first_boundary);
        let (first_boundary, edge_word, second_boundary) =
            if forward <= reverse { forward } else { reverse };
        Self {
            first_boundary,
            second_boundary,
            edge_word,
        }
    }

    fn endpoint_pair(&self) -> (usize, usize) {
        if self.first_boundary <= self.second_boundary {
            (self.first_boundary, self.second_boundary)
        } else {
            (self.second_boundary, self.first_boundary)
        }
    }
}

#[derive(Clone, Debug)]
struct Extension {
    boundary: usize,
    word_from_endpoint: Vec<i16>,
}

fn endpoint_extension(
    graph: &RibbonGraph,
    endpoint: RedEndpoint,
    choice: EndpointChoice,
) -> Extension {
    let mut current = HalfEdge::new(
        endpoint.vertex,
        match choice {
            EndpointChoice::LeftForever => (endpoint.incoming_position + 1) % 3,
            EndpointChoice::RightThenLeft => (endpoint.incoming_position + 2) % 3,
        },
    );
    let mut word = Vec::new();
    let mut seen = BTreeSet::new();
    loop {
        if let Some(&boundary) = graph.external_labels.get(&current) {
            return Extension {
                boundary,
                word_from_endpoint: word,
            };
        }
        assert!(
            seen.insert(current),
            "left-turn extension entered a closed orbit"
        );
        let (_, other, token) = graph.other_end(current).unwrap();
        word.push(token);
        current = HalfEdge::new(other.vertex, (other.position + 1) % 3);
    }
}

fn component_curve(
    graph: &RibbonGraph,
    component: &OpenComponent,
    first_choice: EndpointChoice,
    second_choice: EndpointChoice,
) -> CurveLabel {
    let first = endpoint_extension(graph, component.first, first_choice);
    let second = endpoint_extension(graph, component.second, second_choice);
    let mut word = invert_word(&first.word_from_endpoint);
    word.extend(component.interior.iter().copied());
    word.extend(second.word_from_endpoint.iter().copied());
    CurveLabel::canonical(first.boundary, word, second.boundary)
}

fn boundary_arc_curve(graph: &RibbonGraph, start_label: usize, end_label: usize) -> CurveLabel {
    let external_by_label: BTreeMap<_, _> = graph
        .external_labels
        .iter()
        .map(|(&half, &label)| (label, half))
        .collect();
    let start = external_by_label[&start_label];
    let end = external_by_label[&end_label];
    let mut current = start;
    let mut word = Vec::new();
    let mut seen = BTreeSet::new();
    while current != end {
        assert!(
            seen.insert(current),
            "boundary arc failed to reach its endpoint"
        );
        if graph.external_labels.contains_key(&current) {
            current = HalfEdge::new(current.vertex, (current.position + 1) % 3);
        } else {
            let (_, other, token) = graph.other_end(current).unwrap();
            word.push(token);
            current = HalfEdge::new(other.vertex, (other.position + 1) % 3);
        }
    }
    CurveLabel::canonical(start_label, word, end_label)
}

fn forced_zero_curve_labels(graph: &RibbonGraph) -> BTreeSet<CurveLabel> {
    let boundary_count = graph.external_labels.len();
    assert_eq!(boundary_count, 6);
    let mut result = BTreeSet::new();

    // Boundary-edge invariants X_{i,i+1}=p_i^2 vanish.  We use the
    // all-left boundary representative, which distinguishes these curves from
    // winding curves with the same endpoints on a surface with handles.
    for start in 1..=boundary_count {
        let end = start % boundary_count + 1;
        result.insert(boundary_arc_curve(graph, start, end));
    }

    // The three scalar-scaffolding chords are the short boundary-parallel
    // arcs X_{1,3}, X_{3,5}, and X_{5,1}.  These, rather than the curves whose
    // cores run along an individual scaffold graph edge, are put on shell.
    for (start, end) in [(1, 3), (3, 5), (5, 1)] {
        result.insert(boundary_arc_curve(graph, start, end));
    }
    result
}

#[derive(Clone, Debug)]
struct FactorTerm {
    curve: CurveLabel,
    extensions: usize,
}

fn component_factor(graph: &RibbonGraph, component: &OpenComponent) -> Vec<FactorTerm> {
    let mut terms = Vec::new();
    for first_choice in EndpointChoice::BOTH {
        for second_choice in EndpointChoice::BOTH {
            terms.push(FactorTerm {
                curve: component_curve(graph, component, first_choice, second_choice),
                extensions: first_choice.extension_count() + second_choice.extension_count(),
            });
        }
    }
    terms
}

#[derive(Clone, Copy, Debug, Default, Eq, PartialEq)]
struct Coefficient {
    constant: Int,
    dimension: Int,
}

impl Coefficient {
    fn is_zero(self) -> bool {
        self.constant == 0 && self.dimension == 0
    }
}

#[derive(Clone, Copy, Debug, Default)]
struct OriginTally {
    constant_even: usize,
    constant_odd: usize,
    dimension_even: usize,
    dimension_odd: usize,
}

impl OriginTally {
    fn origins(self) -> usize {
        self.constant_even + self.constant_odd + self.dimension_even + self.dimension_odd
    }
}

type Monomial = Vec<CurveLabel>;

#[derive(Clone, Debug)]
struct Expansion {
    coefficients: BTreeMap<Monomial, Coefficient>,
    origins: BTreeMap<Monomial, OriginTally>,
    raw_origins: usize,
    on_shell_zero_origins: usize,
    extension_histogram: BTreeMap<usize, usize>,
}

fn expand_x_dictionary(graph: &RibbonGraph) -> Expansion {
    let forced_zero = forced_zero_curve_labels(graph);
    let mut coefficients = BTreeMap::<Monomial, Coefficient>::new();
    let mut origins = BTreeMap::<Monomial, OriginTally>::new();
    let mut raw_origins = 0;
    let mut on_shell_zero_origins = 0;
    let mut extension_histogram = BTreeMap::new();

    for pattern in graph.patterns() {
        let state = state_pattern(graph, &pattern);
        assert!(state.circuits <= 1);
        let factors: Vec<_> = state
            .open
            .iter()
            .map(|component| component_factor(graph, component))
            .collect();

        fn recurse(
            index: usize,
            factors: &[Vec<FactorTerm>],
            forced_zero: &BTreeSet<CurveLabel>,
            selected: &mut Vec<CurveLabel>,
            extensions: usize,
            circuits: usize,
            coefficients: &mut BTreeMap<Monomial, Coefficient>,
            origins: &mut BTreeMap<Monomial, OriginTally>,
            raw_origins: &mut usize,
            on_shell_zero_origins: &mut usize,
            extension_histogram: &mut BTreeMap<usize, usize>,
        ) {
            if index == factors.len() {
                *raw_origins += 1;
                *extension_histogram.entry(extensions).or_insert(0) += 1;
                if selected.iter().any(|curve| forced_zero.contains(curve)) {
                    *on_shell_zero_origins += 1;
                    return;
                }
                let mut monomial = selected.clone();
                monomial.sort();
                let odd = extensions % 2 == 1;
                let sign: Int = if odd { -1 } else { 1 };
                let coefficient = coefficients.entry(monomial.clone()).or_default();
                let tally = origins.entry(monomial).or_default();
                if circuits == 0 {
                    coefficient.constant += sign;
                    if odd {
                        tally.constant_odd += 1;
                    } else {
                        tally.constant_even += 1;
                    }
                } else {
                    // The resolved circuit carrier is nu-Delta=D in either
                    // physical class: (nu,Delta)=(0,-D) for a generic closed
                    // curve and (1,1-D) for an internal-boundary curve.  This
                    // is essential because the latter occurs in some nested
                    // physical-projector sewing histories below.
                    coefficient.dimension += sign;
                    if odd {
                        tally.dimension_odd += 1;
                    } else {
                        tally.dimension_even += 1;
                    }
                }
                return;
            }
            for term in &factors[index] {
                selected.push(term.curve.clone());
                recurse(
                    index + 1,
                    factors,
                    forced_zero,
                    selected,
                    extensions + term.extensions,
                    circuits,
                    coefficients,
                    origins,
                    raw_origins,
                    on_shell_zero_origins,
                    extension_histogram,
                );
                selected.pop();
            }
        }

        recurse(
            0,
            &factors,
            &forced_zero,
            &mut Vec::new(),
            0,
            state.circuits,
            &mut coefficients,
            &mut origins,
            &mut raw_origins,
            &mut on_shell_zero_origins,
            &mut extension_histogram,
        );
    }

    Expansion {
        coefficients,
        origins,
        raw_origins,
        on_shell_zero_origins,
        extension_histogram,
    }
}

type EndpointMonomial = Vec<(usize, usize)>;

fn collapse_tree_polynomial(expansion: &Expansion) -> BTreeMap<EndpointMonomial, Int> {
    let mut result = BTreeMap::new();
    for (monomial, coefficient) in &expansion.coefficients {
        assert_eq!(coefficient.dimension, 0);
        let mut collapsed: Vec<_> = monomial.iter().map(CurveLabel::endpoint_pair).collect();
        collapsed.sort_unstable();
        *result.entry(collapsed).or_insert(0) += coefficient.constant;
    }
    result.retain(|_, coefficient| *coefficient != 0);
    result
}

fn known_three_point_polynomial() -> BTreeMap<EndpointMonomial, Int> {
    let mut result = BTreeMap::new();
    let terms = [
        (1, [(1, 4), (2, 6)]),
        (1, [(3, 6), (2, 4)]),
        (1, [(2, 5), (4, 6)]),
        (-1, [(2, 5), (3, 6)]),
        (-1, [(1, 4), (3, 6)]),
        (-1, [(1, 4), (2, 5)]),
    ];
    for (coefficient, pairs) in terms {
        let mut monomial: Vec<_> = pairs
            .into_iter()
            .map(|(a, b)| if a <= b { (a, b) } else { (b, a) })
            .collect();
        monomial.sort_unstable();
        *result.entry(monomial).or_insert(0) += coefficient;
    }
    result
}

fn relabel_tree_polynomial(
    polynomial: &BTreeMap<EndpointMonomial, Int>,
    shift: isize,
    orientation: isize,
) -> BTreeMap<EndpointMonomial, Int> {
    let map = |label: usize| {
        let zero = label as isize - 1;
        (orientation * zero + shift).rem_euclid(6) as usize + 1
    };
    polynomial
        .iter()
        .map(|(monomial, &coefficient)| {
            let mut moved: Vec<_> = monomial
                .iter()
                .map(|&(a, b)| {
                    let x = map(a);
                    let y = map(b);
                    if x <= y {
                        (x, y)
                    } else {
                        (y, x)
                    }
                })
                .collect();
            moved.sort_unstable();
            (moved, coefficient)
        })
        .collect()
}

fn audit_three_point_calibration() -> (isize, isize, Int, Expansion) {
    let graph = RibbonGraph::three_point();
    let expansion = expand_x_dictionary(&graph);
    let observed = collapse_tree_polynomial(&expansion);
    let expected = known_three_point_polynomial();
    for orientation in [1, -1] {
        for shift in 0..6 {
            let moved = relabel_tree_polynomial(&observed, shift, orientation);
            if moved == expected {
                return (shift, orientation, 1, expansion);
            }
            if moved
                .iter()
                .map(|(monomial, coefficient)| (monomial.clone(), -*coefficient))
                .collect::<BTreeMap<_, _>>()
                == expected
            {
                return (shift, orientation, -1, expansion);
            }
        }
    }
    panic!(
        "three-point X dictionary does not reproduce the documented polynomial\nobserved={observed:#?}\nexpected={expected:#?}\nlabels={:#?}\nscaffold={:#?}",
        graph.external_labels,
        forced_zero_curve_labels(&graph)
    );
}

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct Vector([Int; DIM]);

impl Vector {
    const ZERO: Self = Self([0; DIM]);

    fn plus(self, other: Self) -> Self {
        Self(std::array::from_fn(|index| self.0[index] + other.0[index]))
    }

    fn minus(self, other: Self) -> Self {
        Self(std::array::from_fn(|index| self.0[index] - other.0[index]))
    }

    fn scale(self, scalar: Int) -> Self {
        Self(std::array::from_fn(|index| scalar * self.0[index]))
    }
}

fn from_xy(x: [Int; 3], y: [Int; 3]) -> Vector {
    Vector([x[0], x[1], x[2], y[0], y[1], y[2]])
}

fn metric_entry(first: usize, second: usize) -> Int {
    match (first, second) {
        (0, 3) | (3, 0) | (1, 4) | (4, 1) | (2, 5) | (5, 2) => 1,
        _ => 0,
    }
}

fn dual_index(index: usize) -> usize {
    match index {
        0 => 3,
        1 => 4,
        2 => 5,
        3 => 0,
        4 => 1,
        5 => 2,
        _ => unreachable!(),
    }
}

fn dot(first: Vector, second: Vector) -> Int {
    (0..DIM)
        .flat_map(|i| (0..DIM).map(move |j| first.0[i] * metric_entry(i, j) * second.0[j]))
        .sum()
}

fn covector(vector: Vector, index: usize) -> Int {
    (0..DIM)
        .map(|component| metric_entry(index, component) * vector.0[component])
        .sum()
}

fn vertex_tensor(momenta: [Vector; 3], indices: [usize; 3]) -> Int {
    metric_entry(indices[0], indices[1]) * covector(momenta[0].minus(momenta[1]), indices[2])
        + metric_entry(indices[1], indices[2]) * covector(momenta[1].minus(momenta[2]), indices[0])
        + metric_entry(indices[0], indices[2]) * covector(momenta[2].minus(momenta[0]), indices[1])
}

fn sector_tensor(momenta: [Vector; 3], indices: [usize; 3], singleton: usize) -> Int {
    let first_paired = (singleton + 1) % 3;
    let second_paired = (singleton + 2) % 3;
    metric_entry(indices[first_paired], indices[second_paired])
        * covector(
            momenta[first_paired].minus(momenta[second_paired]),
            indices[singleton],
        )
}

fn contract_three_vertex(momenta: [Vector; 3], polarizations: [Vector; 3]) -> Int {
    let mut total = 0;
    for first in 0..DIM {
        for second in 0..DIM {
            for third in 0..DIM {
                total += vertex_tensor(momenta, [first, second, third])
                    * polarizations[0].0[first]
                    * polarizations[1].0[second]
                    * polarizations[2].0[third];
            }
        }
    }
    total
}

fn polarization_candidates(momentum: Vector) -> Vec<Vector> {
    let mut candidates = BTreeSet::new();
    for u0 in -2..=2 {
        for u1 in -2..=2 {
            for u2 in -2..=2 {
                for v0 in -2..=2 {
                    for v1 in -2..=2 {
                        for v2 in -2..=2 {
                            let candidate = from_xy([u0, u1, u2], [v0, v1, v2]);
                            if candidate == Vector::ZERO || dot(candidate, candidate) != 0 {
                                continue;
                            }
                            if dot(momentum, candidate) == 0 {
                                candidates.insert(candidate);
                            }
                        }
                    }
                }
            }
        }
    }
    candidates.into_iter().collect()
}

#[derive(Clone, Debug)]
struct OnShellPoint {
    momenta: [[Vector; 3]; 5],
    external_polarizations: [Vector; 3],
}

fn on_shell_point(parameters: [Int; 3]) -> OnShellPoint {
    let [a, b, d] = parameters;
    assert_ne!(a, 0);
    let xs = [[1, 0, 0], [0, 1, 0], [-1, -1, 0]];
    let ys = [[0, a, b], [-a, 0, d], [a, -a, -b - d]];
    let p: [Vector; 3] = std::array::from_fn(|road| from_xy(xs[road], [0; 3]));
    let k: [Vector; 3] = std::array::from_fn(|road| from_xy([0; 3], ys[road]));
    let external: [Vector; 3] = std::array::from_fn(|road| p[road].minus(k[road]));
    // Pick the first small-integer null/transverse triple for which the
    // scalar-scaffolded three-point amplitude is nonzero.  This avoids an
    // accidental helicity/kinematic zero while keeping the sample completely
    // deterministic and exactly reproducible.
    let candidate_sets = external.map(polarization_candidates);
    let mut selected = None;
    'search: for &first in candidate_sets[0].iter().take(32) {
        for &second in candidate_sets[1].iter().take(32) {
            for &third in candidate_sets[2].iter().take(32) {
                let polarizations = [first, second, third];
                if contract_three_vertex(external, polarizations) != 0 {
                    selected = Some(polarizations);
                    break 'search;
                }
            }
        }
    }
    let external_polarizations =
        selected.expect("failed to find a nondegenerate polarization triple");

    let sum = |vectors: &[Vector]| vectors.iter().fold(Vector::ZERO, |total, &v| total.plus(v));
    assert_eq!(sum(&p), Vector::ZERO);
    assert_eq!(sum(&k), Vector::ZERO);
    assert_eq!(sum(&external), Vector::ZERO);
    for vector in p
        .iter()
        .chain(k.iter())
        .chain(external.iter())
        .chain(external_polarizations.iter())
    {
        assert_eq!(dot(*vector, *vector), 0);
    }
    for road in 0..3 {
        assert_eq!(dot(external[road], external_polarizations[road]), 0);
    }

    let momenta = [
        p,
        std::array::from_fn(|road| Vector::ZERO.minus(k[road])),
        [Vector::ZERO.minus(p[0]), external[0], k[0]],
        [Vector::ZERO.minus(p[1]), external[1], k[1]],
        [Vector::ZERO.minus(p[2]), external[2], k[2]],
    ];
    // The first entries at marked vertices are -p.  Spell the check rather
    // than relying on the construction above.
    for road in 0..3 {
        assert_eq!(momenta[2 + road][0], Vector::ZERO.minus(p[road]));
    }
    for vertex in &momenta {
        assert_eq!(sum(vertex), Vector::ZERO);
        for momentum in vertex {
            assert_eq!(dot(*momentum, *momentum), 0);
        }
    }
    OnShellPoint {
        momenta,
        external_polarizations,
    }
}

fn direct_five_vertex_leading_singularity(point: &OnShellPoint) -> Int {
    let mut total = 0;
    for code in 0..DIM.pow(6) {
        let mut remaining = code;
        let mut edge_indices = [0; 6];
        for index in &mut edge_indices {
            *index = remaining % DIM;
            remaining /= DIM;
        }
        let mut indices = [[0; 3]; 5];
        let mut sewing_weight = 1;
        for road in 0..3 {
            let left_index = edge_indices[2 * road];
            indices[0][road] = left_index;
            indices[2 + road][0] = dual_index(left_index);
            sewing_weight *= -metric_entry(left_index, dual_index(left_index));

            let right_index = edge_indices[2 * road + 1];
            indices[1][road] = right_index;
            indices[2 + road][2] = dual_index(right_index);
            sewing_weight *= -metric_entry(right_index, dual_index(right_index));
        }
        let mut value = sewing_weight
            * vertex_tensor(point.momenta[0], indices[0])
            * vertex_tensor(point.momenta[1], indices[1]);
        for road in 0..3 {
            let mut contracted = 0;
            for external_index in 0..DIM {
                let local = [indices[2 + road][0], external_index, indices[2 + road][2]];
                contracted += vertex_tensor(point.momenta[2 + road], local)
                    * point.external_polarizations[road].0[external_index];
            }
            value *= contracted;
        }
        total += value;
    }
    total
}

fn direct_pattern_value(point: &OnShellPoint, pattern: &[usize]) -> Int {
    assert_eq!(pattern.len(), 5);
    let mut total = 0;
    for code in 0..DIM.pow(6) {
        let mut remaining = code;
        let mut edge_indices = [0; 6];
        for index in &mut edge_indices {
            *index = remaining % DIM;
            remaining /= DIM;
        }
        let mut indices = [[0; 3]; 5];
        let mut sewing_weight = 1;
        for road in 0..3 {
            let left_index = edge_indices[2 * road];
            indices[0][road] = left_index;
            indices[2 + road][0] = dual_index(left_index);
            sewing_weight *= -metric_entry(left_index, dual_index(left_index));

            let right_index = edge_indices[2 * road + 1];
            indices[1][road] = right_index;
            indices[2 + road][2] = dual_index(right_index);
            sewing_weight *= -metric_entry(right_index, dual_index(right_index));
        }
        let mut value = sewing_weight
            * sector_tensor(point.momenta[0], indices[0], pattern[0])
            * sector_tensor(point.momenta[1], indices[1], pattern[1]);
        for road in 0..3 {
            let mut contracted = 0;
            for external_index in 0..DIM {
                let local = [indices[2 + road][0], external_index, indices[2 + road][2]];
                contracted += sector_tensor(point.momenta[2 + road], local, pattern[2 + road])
                    * point.external_polarizations[road].0[external_index];
            }
            value *= contracted;
        }
        total += value;
    }
    total
}

fn spanning_tree_masks() -> Vec<u8> {
    let mut result = Vec::new();
    for mask in 0_u8..(1 << 6) {
        if mask.count_ones() != 4 {
            continue;
        }
        let mut adjacency = vec![Vec::new(); 5];
        for road in 0..3 {
            let middle = 2 + road;
            if mask & (1 << (2 * road)) != 0 {
                adjacency[0].push(middle);
                adjacency[middle].push(0);
            }
            if mask & (1 << (2 * road + 1)) != 0 {
                adjacency[1].push(middle);
                adjacency[middle].push(1);
            }
        }
        let mut seen = BTreeSet::from([0]);
        let mut queue = VecDeque::from([0]);
        while let Some(vertex) = queue.pop_front() {
            for &next in &adjacency[vertex] {
                if seen.insert(next) {
                    queue.push_back(next);
                }
            }
        }
        if seen.len() == 5 {
            result.push(mask);
        }
    }
    assert_eq!(result.len(), 12);
    result
}

fn null_reference(momentum: Vector) -> Vector {
    for component in 0..DIM {
        for sign in [-1, 1] {
            let mut entries = [0; DIM];
            entries[component] = sign;
            let candidate = Vector(entries);
            if dot(candidate, candidate) == 0 && dot(momentum, candidate).abs() == 1 {
                return candidate;
            }
        }
    }
    panic!("no unit-denominator null reference for {momentum:?}");
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum SewingMode {
    Metric,
    Physical,
    Longitudinal,
}

fn sewing_options(momentum: Vector, mode: SewingMode) -> Vec<(usize, usize, Int)> {
    let reference = (mode != SewingMode::Metric).then(|| null_reference(momentum));
    let denominator = reference.map(|q| dot(momentum, q)).unwrap_or(1);
    let mut options = Vec::new();
    for first in 0..DIM {
        for second in 0..DIM {
            let mut weight = if mode == SewingMode::Longitudinal {
                0
            } else {
                -metric_entry(first, second)
            };
            if let Some(q) = reference {
                let numerator = momentum.0[first] * q.0[second] + q.0[first] * momentum.0[second];
                assert_eq!(numerator % denominator, 0);
                weight += numerator / denominator;
            }
            if weight != 0 {
                options.push((first, second, weight));
            }
        }
    }
    options
}

fn tensor_network_with_sewings(point: &OnShellPoint, modes: [SewingMode; 6]) -> Int {
    let option_sets: Vec<_> = (0..6)
        .map(|slot| {
            let road = slot / 2;
            let momentum = if slot % 2 == 0 {
                point.momenta[0][road]
            } else {
                point.momenta[1][road]
            };
            sewing_options(momentum, modes[slot])
        })
        .collect();

    fn recurse(
        slot: usize,
        option_sets: &[Vec<(usize, usize, Int)>],
        chosen: &mut [(usize, usize); 6],
        weight: Int,
        point: &OnShellPoint,
        total: &mut Int,
    ) {
        if slot == 6 {
            let mut indices = [[0; 3]; 5];
            for road in 0..3 {
                let (left_core, left_middle) = chosen[2 * road];
                indices[0][road] = left_core;
                indices[2 + road][0] = left_middle;
                let (right_core, right_middle) = chosen[2 * road + 1];
                indices[1][road] = right_core;
                indices[2 + road][2] = right_middle;
            }
            let mut value = weight
                * vertex_tensor(point.momenta[0], indices[0])
                * vertex_tensor(point.momenta[1], indices[1]);
            for road in 0..3 {
                let mut contracted = 0;
                for external_index in 0..DIM {
                    let local = [indices[2 + road][0], external_index, indices[2 + road][2]];
                    contracted += vertex_tensor(point.momenta[2 + road], local)
                        * point.external_polarizations[road].0[external_index];
                }
                value *= contracted;
            }
            *total += value;
            return;
        }
        for &(first, second, local_weight) in &option_sets[slot] {
            chosen[slot] = (first, second);
            recurse(
                slot + 1,
                option_sets,
                chosen,
                weight * local_weight,
                point,
                total,
            );
        }
    }

    let mut total = 0;
    recurse(0, &option_sets, &mut [(0, 0); 6], 1, point, &mut total);
    total
}

fn physical_projector_leading_singularity(point: &OnShellPoint, tree_mask: u8) -> Int {
    let modes = std::array::from_fn(|slot| {
        if tree_mask & (1 << slot) == 0 {
            SewingMode::Physical
        } else {
            SewingMode::Metric
        }
    });
    tensor_network_with_sewings(point, modes)
}

fn projector_correction_decomposition(point: &OnShellPoint, tree_mask: u8) -> [Int; 4] {
    let closures: Vec<_> = (0..6).filter(|slot| tree_mask & (1 << slot) == 0).collect();
    assert_eq!(closures.len(), 2);
    std::array::from_fn(|subset| {
        let mut modes = [SewingMode::Metric; 6];
        for (index, &slot) in closures.iter().enumerate() {
            if subset & (1 << index) != 0 {
                modes[slot] = SewingMode::Longitudinal;
            }
        }
        tensor_network_with_sewings(point, modes)
    })
}

fn full_handle_pattern_value(graph: &RibbonGraph, point: &OnShellPoint, pattern: &[usize]) -> Int {
    let state = state_pattern(graph, pattern);
    let handles = endpoint_vectors(point, pattern);
    let mut value = (DIM as Int).pow(state.circuits as u32);
    for component in state.open {
        value *= dot(
            handles[component.first.vertex],
            handles[component.second.vertex],
        );
    }
    value
}

fn audit_patternwise_tensor_decomposition(graph: &RibbonGraph, point: &OnShellPoint) {
    let mut sector_sum = 0;
    for pattern in graph.patterns() {
        let direct = direct_pattern_value(point, &pattern);
        let paths = full_handle_pattern_value(graph, point, &pattern);
        assert_eq!(
            direct, paths,
            "patternwise tensor/path mismatch: {pattern:?}"
        );
        sector_sum += direct;
    }
    assert_eq!(sector_sum, direct_five_vertex_leading_singularity(point));

    for momenta in point.momenta {
        for first in 0..DIM {
            for second in 0..DIM {
                for third in 0..DIM {
                    let indices = [first, second, third];
                    let sector_sum: Int = (0..3)
                        .map(|singleton| sector_tensor(momenta, indices, singleton))
                        .sum();
                    assert_eq!(sector_sum, vertex_tensor(momenta, indices));
                }
            }
        }
    }
}

fn direct_three_point_amplitude(point: &OnShellPoint) -> Int {
    let momenta = std::array::from_fn(|road| point.momenta[2 + road][1]);
    contract_three_vertex(momenta, point.external_polarizations)
}

fn endpoint_vectors(point: &OnShellPoint, pattern: &[usize]) -> Vec<Vector> {
    let mut vectors = Vec::new();
    for (vertex, &singleton) in pattern.iter().enumerate() {
        let momenta = point.momenta[vertex];
        vectors.push(momenta[(singleton + 1) % 3].minus(momenta[(singleton + 2) % 3]));
    }
    vectors.extend(point.external_polarizations);
    vectors
}

fn open_path_leading_singularity(graph: &RibbonGraph, point: &OnShellPoint) -> Int {
    let mut total = 0;
    for pattern in graph.patterns() {
        let state = state_pattern(graph, &pattern);
        let endpoint_vectors = endpoint_vectors(point, &pattern);
        let mut value = (DIM as Int).pow(state.circuits as u32);
        for component in state.open {
            value *= dot(
                endpoint_vectors[component.first.vertex],
                endpoint_vectors[component.second.vertex],
            );
        }
        // There are six physical -eta internal sewings, so their common sign
        // is positive.  The three scaffold edges are external contractions.
        total += value;
    }
    total
}

fn scaled_vertex_momenta(graph: &RibbonGraph, point: &OnShellPoint) -> Vec<[Vector; 3]> {
    let mut result = Vec::with_capacity(graph.vertices);
    if graph.ym_vertices == 1 {
        // The three-point calibration graph has the three external momenta q_r
        // at its sole YM vertex.
        result.push(std::array::from_fn(|road| {
            point.momenta[2 + road][1].scale(2)
        }));
    } else {
        assert_eq!(graph.ym_vertices, 5);
        result.extend(
            point
                .momenta
                .map(|vertex| vertex.map(|momentum| momentum.scale(2))),
        );
    }

    for road in 0..3 {
        let q = point.momenta[2 + road][1];
        let epsilon = point.external_polarizations[road];
        // These are twice the outgoing momenta (-q,a,b) at the scaffold
        // vertex: (-2q, q+epsilon, q-epsilon).
        result.push([q.scale(-2), q.plus(epsilon), q.minus(epsilon)]);
    }
    assert_eq!(result.len(), graph.vertices);
    for vertex in &result {
        assert_eq!(vertex[0].plus(vertex[1]).plus(vertex[2]), Vector::ZERO);
    }
    for edge in &graph.edges {
        assert_eq!(
            result[edge.first.vertex][edge.first.position]
                .plus(result[edge.second.vertex][edge.second.position]),
            Vector::ZERO
        );
    }
    result
}

fn momentum_after_turn(
    arrival: HalfEdge,
    departure: HalfEdge,
    momenta: &[[Vector; 3]],
    curve_momentum: Vector,
) -> Vector {
    assert_eq!(arrival.vertex, departure.vertex);
    let left = (arrival.position + 1) % 3;
    let right = (arrival.position + 2) % 3;
    if departure.position == right {
        // On a right turn, the unused edge at `left` is the edge entering
        // from the curve's left in the source's momentum rule.
        curve_momentum.plus(momenta[arrival.vertex][left])
    } else {
        assert_eq!(departure.position, left);
        curve_momentum
    }
}

fn curve_scaled_square(graph: &RibbonGraph, momenta: &[[Vector; 3]], curve: &CurveLabel) -> Int {
    let external_by_label: BTreeMap<_, _> = graph
        .external_labels
        .iter()
        .map(|(&half, &label)| (label, half))
        .collect();
    let mut arrival = external_by_label[&curve.first_boundary];
    let end = external_by_label[&curve.second_boundary];
    let mut curve_momentum = momenta[arrival.vertex][arrival.position];

    for &token in &curve.edge_word {
        let edge_index = token.unsigned_abs() as usize - 1;
        let edge = graph.edges[edge_index];
        let (departure, other) = if token > 0 {
            (edge.first, edge.second)
        } else {
            (edge.second, edge.first)
        };
        curve_momentum = momentum_after_turn(arrival, departure, momenta, curve_momentum);
        arrival = other;
    }
    curve_momentum = momentum_after_turn(arrival, end, momenta, curve_momentum);
    dot(curve_momentum, curve_momentum)
}

fn evaluate_x_expansion(graph: &RibbonGraph, point: &OnShellPoint, expansion: &Expansion) -> Int {
    let momenta = scaled_vertex_momenta(graph, point);
    let mut curve_values = BTreeMap::new();
    for monomial in expansion.coefficients.keys() {
        for curve in monomial {
            curve_values
                .entry(curve.clone())
                .or_insert_with(|| curve_scaled_square(graph, &momenta, curve));
        }
    }
    expansion
        .coefficients
        .iter()
        .map(|(monomial, coefficient)| {
            let scalar = coefficient.constant + coefficient.dimension * DIM as Int;
            monomial
                .iter()
                .fold(scalar, |value, curve| value * curve_values[curve])
        })
        .sum()
}

fn component_identity_table(
    graph: &RibbonGraph,
    point: &OnShellPoint,
) -> BTreeMap<(Int, Int), usize> {
    let momenta = scaled_vertex_momenta(graph, point);
    let mut result = BTreeMap::new();
    for pattern in graph.patterns() {
        let state = state_pattern(graph, &pattern);
        let handles: Vec<_> = (0..graph.vertices)
            .map(|vertex| {
                if vertex < graph.ym_vertices {
                    momenta[vertex][(pattern[vertex] + 1) % 3]
                } else {
                    momenta[vertex][1]
                }
            })
            .collect();
        for component in state.open {
            let factor = component_factor(graph, &component)
                .into_iter()
                .map(|term| {
                    let sign = if term.extensions % 2 == 0 { 1 } else { -1 };
                    sign * curve_scaled_square(graph, &momenta, &term.curve)
                })
                .sum();
            let contraction = dot(
                handles[component.first.vertex],
                handles[component.second.vertex],
            );
            *result.entry((factor, contraction)).or_insert(0) += 1;
        }
    }
    result
}

fn graphical_path_sum(graph: &RibbonGraph, point: &OnShellPoint, closed_sign: Int) -> Int {
    let momenta = scaled_vertex_momenta(graph, point);
    let mut total = 0;
    for pattern in graph.patterns() {
        let state = state_pattern(graph, &pattern);
        let handles: Vec<_> = (0..graph.vertices)
            .map(|vertex| {
                if vertex < graph.ym_vertices {
                    momenta[vertex][(pattern[vertex] + 1) % 3]
                } else {
                    momenta[vertex][1]
                }
            })
            .collect();
        let mut value = (closed_sign * DIM as Int).pow(state.circuits as u32);
        for component in state.open {
            value *= dot(
                handles[component.first.vertex],
                handles[component.second.vertex],
            );
        }
        total += value;
    }
    total
}

#[derive(Clone, Debug)]
struct ExpansionStats {
    curve_variables: usize,
    generated_monomials: usize,
    fully_cancelled: usize,
    partially_cancelled: usize,
    surviving: usize,
    constant_survivors: usize,
    dimension_survivors: usize,
    mixed_survivors: usize,
    max_abs_coefficient: Int,
}

fn expansion_stats(expansion: &Expansion) -> ExpansionStats {
    let curve_variables: BTreeSet<_> = expansion
        .coefficients
        .keys()
        .flat_map(|monomial| monomial.iter().cloned())
        .collect();
    let mut fully_cancelled = 0;
    let mut partially_cancelled = 0;
    let mut surviving = 0;
    let mut constant_survivors = 0;
    let mut dimension_survivors = 0;
    let mut mixed_survivors = 0;
    let mut max_abs_coefficient = 0;
    for (monomial, tally) in &expansion.origins {
        let coefficient = expansion.coefficients[monomial];
        if coefficient.is_zero() {
            assert!(tally.origins() > 1);
            fully_cancelled += 1;
            continue;
        }
        surviving += 1;
        let cancellations = tally.constant_even.min(tally.constant_odd)
            + tally.dimension_even.min(tally.dimension_odd);
        if cancellations > 0 {
            partially_cancelled += 1;
        }
        match (coefficient.constant != 0, coefficient.dimension != 0) {
            (true, false) => constant_survivors += 1,
            (false, true) => dimension_survivors += 1,
            (true, true) => mixed_survivors += 1,
            (false, false) => unreachable!(),
        }
        max_abs_coefficient = max_abs_coefficient
            .max(coefficient.constant.abs())
            .max(coefficient.dimension.abs());
    }
    ExpansionStats {
        curve_variables: curve_variables.len(),
        generated_monomials: expansion.origins.len(),
        fully_cancelled,
        partially_cancelled,
        surviving,
        constant_survivors,
        dimension_survivors,
        mixed_survivors,
        max_abs_coefficient,
    }
}

fn main() {
    let (shift, orientation, global_sign, three_point) = audit_three_point_calibration();

    let graph = RibbonGraph::marked_theta();
    assert_eq!(graph.patterns().len(), 243);
    let expansion = expand_x_dictionary(&graph);
    assert_eq!(expansion.raw_origins, 243 * 4_usize.pow(4));
    let stats = expansion_stats(&expansion);

    let point = on_shell_point([1, 2, 3]);
    audit_patternwise_tensor_decomposition(&graph, &point);
    let naive_metric = direct_five_vertex_leading_singularity(&point);
    let full_handle_paths = open_path_leading_singularity(&graph, &point);
    assert_ne!(
        naive_metric, 0,
        "chosen exact on-shell test point is degenerate"
    );
    assert_eq!(full_handle_paths, naive_metric);

    let component_identities = component_identity_table(&graph, &point);
    assert_eq!(component_identities.values().sum::<usize>(), 243 * 4);
    assert!(component_identities
        .keys()
        .all(|&(four_x, contraction)| four_x == -2 * contraction));

    let graphical = graphical_path_sum(&graph, &point, 1);
    let surface = evaluate_x_expansion(&graph, &point, &expansion);
    let projector_values: Vec<_> = spanning_tree_masks()
        .into_iter()
        .map(|mask| (mask, physical_projector_leading_singularity(&point, mask)))
        .collect();
    let physical_values: BTreeSet<_> = projector_values.iter().map(|(_, value)| *value).collect();
    assert_eq!(physical_values.len(), 1);
    let physical = *physical_values.first().unwrap();
    assert_eq!(physical, graphical);
    // Four open contraction paths give one factor -2 each when the polynomial
    // is evaluated on 4 X_C, hence the universal factor 2^4.
    assert_eq!(surface, 16 * physical);

    let projector_components: Vec<_> = spanning_tree_masks()
        .into_iter()
        .map(|mask| (mask, projector_correction_decomposition(&point, mask)))
        .collect();
    let mut correction_classes = BTreeMap::new();
    for (_, pieces) in &projector_components {
        assert_eq!(pieces.iter().sum::<Int>(), physical);
        assert_eq!(pieces[0], naive_metric);
        *correction_classes.entry(*pieces).or_insert(0_usize) += 1;
    }
    assert_eq!(physical - naive_metric, 8);
    assert_eq!(correction_classes.get(&[-2056, 8, 0, 0]), Some(&8));
    assert_eq!(correction_classes.get(&[-2056, 8, 8, -8]), Some(&4));

    let three_graph = RibbonGraph::three_point();
    let three_momenta = scaled_vertex_momenta(&three_graph, &point);
    for curve in forced_zero_curve_labels(&three_graph) {
        assert_eq!(curve_scaled_square(&three_graph, &three_momenta, &curve), 0);
    }
    let three_component_identities = component_identity_table(&three_graph, &point);
    assert_eq!(three_component_identities.values().sum::<usize>(), 6);
    assert!(three_component_identities
        .keys()
        .all(|&(four_x, contraction)| four_x == -2 * contraction));
    let three_surface = evaluate_x_expansion(&three_graph, &point, &three_point);
    let three_direct = direct_three_point_amplitude(&point);
    let three_graphical = graphical_path_sum(&three_graph, &point, 1);
    assert_ne!(three_direct, 0);
    assert_eq!(three_direct, three_graphical);
    assert_eq!(three_surface, 4 * three_direct);

    // Repeat the global comparison at independent exact rational points.
    // The detailed component/cancellation audit above is kinematics
    // independent; these extra points guard against a numerical coincidence
    // in the assembled physical projector and resolved circuit carrier.
    let mut additional_samples = Vec::new();
    for parameters in [[1, -3, 4], [1, 3, -2], [1, 4, 2]] {
        let sample = on_shell_point(parameters);
        let sample_graphical = graphical_path_sum(&graph, &sample, 1);
        let sample_surface = evaluate_x_expansion(&graph, &sample, &expansion);
        let sample_values: BTreeSet<_> = spanning_tree_masks()
            .into_iter()
            .map(|mask| physical_projector_leading_singularity(&sample, mask))
            .collect();
        assert_eq!(sample_values.len(), 1);
        let sample_physical = *sample_values.first().unwrap();
        assert_ne!(sample_physical, 0, "degenerate sample: {parameters:?}");
        assert_eq!(sample_physical, sample_graphical);
        assert_eq!(sample_surface, 16 * sample_physical);
        additional_samples.push((parameters, sample_physical, sample_surface));
    }

    println!("Marked-handle open-path / X-dictionary certificate");
    println!("==================================================");
    println!(
        "  three-point calibration: shift={shift}, orientation={orientation}, sign={global_sign}"
    );
    println!(
        "  three-point raw extension origins: {}",
        three_point.raw_origins
    );
    println!("  five-vertex resolved sectors: 243");
    println!(
        "  raw four-factor extension origins: {}",
        expansion.raw_origins
    );
    println!(
        "  on-shell-zero origins removed: {}",
        expansion.on_shell_zero_origins
    );
    println!(
        "  extension-count histogram: {:?}",
        expansion.extension_histogram
    );
    println!(
        "  distinct surface curve variables: {}",
        stats.curve_variables
    );
    println!("  generated X monomials: {}", stats.generated_monomials);
    println!("  fully cancelled monomials: {}", stats.fully_cancelled);
    println!(
        "  partially cancelled survivors: {}",
        stats.partially_cancelled
    );
    println!("  surviving X monomials: {}", stats.surviving);
    println!(
        "  survivors (constant, D, mixed): ({}, {}, {})",
        stats.constant_survivors, stats.dimension_survivors, stats.mixed_survivors
    );
    println!(
        "  maximum absolute surviving coefficient: {}",
        stats.max_abs_coefficient
    );
    println!("  verified component identities: 972 marked + 6 calibration");
    println!("  naive all-metric five-tensor value: {naive_metric}");
    println!("  physical-projector value (all 12 spanning trees): {physical}");
    println!("  net longitudinal correction: {}", physical - naive_metric);
    println!("  projector correction classes: {correction_classes:?}");
    println!("  marked-handle polynomial at 4 X_C: {surface}");
    println!("  normalized polynomial / 2^4: {}", surface / 16);
    println!("  additional exact samples (parameters, LS, 4X polynomial):");
    for sample in &additional_samples {
        println!("    {sample:?}");
    }
    println!(
        "  A3 calibration (tensor, graphical, 4X polynomial): ({three_direct},{three_graphical},{three_surface})"
    );
    println!();
    println!("VERDICT");
    println!("  the endpoint extension rule reproduces the documented A3(X) polynomial");
    println!("  the handle X dictionary retains homotopy words and exact (-1)^N_e signs");
    println!("  equal-X origins exhibit explicit complete and partial cancellations");
    println!("  the complete physical-projector LS equals the normalized X polynomial");
    println!("  the previous zero-projector-correction claim is falsified on this exact sample");
}
