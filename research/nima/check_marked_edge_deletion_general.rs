//! Exhaustive finite audit of marked-tubing edge-deletion carriers.
//!
//! For every labeled connected simple graph on one through five vertices, this
//! certificate audits every edge deletion whose target remains connected.  It
//! implements the marked-tubing face poset of Devadoss--Forcey and compares
//! three contravariant carriers: component splitting with the innermost mark,
//! component splitting with the outermost mark, and forget-only deletion.
//!
//! The audit is finite evidence, not an all-graph proof.  Relabeling covariance
//! is checked on every permutation in the full symmetric group.  The expensive
//! face-poset calculations are deduplicated by isomorphism class only after all
//! labeled graphs and deletion diagrams have been enumerated.

use std::collections::{BTreeMap, BTreeSet, HashMap, VecDeque};
use std::time::Instant;

#[derive(Clone, Copy, Debug, Eq, Hash, Ord, PartialEq, PartialOrd)]
enum Mark {
    Thin,
    Thick,
    Broken,
}

impl Mark {
    fn letter(self) -> char {
        match self {
            Self::Thin => 'n',
            Self::Thick => 'k',
            Self::Broken => 'b',
        }
    }
}

#[derive(Clone, Copy, Debug, Eq, Hash, Ord, PartialEq, PartialOrd)]
struct MarkedTube {
    vertices: u8,
    mark: Mark,
}

#[derive(Clone, Debug, Eq, Hash, Ord, PartialEq, PartialOrd)]
struct Face(Vec<MarkedTube>);

impl Face {
    fn codimension(&self) -> usize {
        self.0
            .iter()
            .filter(|tube| tube.mark != Mark::Broken)
            .count()
    }

    fn mark_of(&self, vertices: u8) -> Option<Mark> {
        self.0
            .binary_search_by_key(&vertices, |tube| tube.vertices)
            .ok()
            .map(|index| self.0[index].mark)
    }

    fn contains(&self, vertices: u8) -> bool {
        self.mark_of(vertices).is_some()
    }

    fn underlying(&self) -> Vec<u8> {
        self.0.iter().map(|tube| tube.vertices).collect()
    }
}

#[derive(Clone, Copy, Debug, Eq, Hash, Ord, PartialEq, PartialOrd)]
struct Graph {
    n: usize,
    edges: u16,
}

impl Graph {
    fn all(self) -> u8 {
        ((1_u16 << self.n) - 1) as u8
    }

    fn edge_capacity(self) -> usize {
        self.n * (self.n - 1) / 2
    }

    fn has_edge(self, a: usize, b: usize) -> bool {
        self.edges & (1 << edge_slot(a, b)) != 0
    }

    fn connected(self, vertices: u8) -> bool {
        if vertices == 0 {
            return false;
        }
        let start = vertices.trailing_zeros() as usize;
        let mut seen = 1_u8 << start;
        let mut queue = VecDeque::from([start]);
        while let Some(a) = queue.pop_front() {
            for b in 0..self.n {
                let bit = 1_u8 << b;
                if vertices & bit != 0 && seen & bit == 0 && self.has_edge(a, b) {
                    seen |= bit;
                    queue.push_back(b);
                }
            }
        }
        seen == vertices
    }

    fn tubes(self) -> Vec<u8> {
        (1..=self.all())
            .filter(|&vertices| self.connected(vertices))
            .collect()
    }

    fn components(self, vertices: u8) -> Vec<u8> {
        let mut remaining = vertices;
        let mut answer = Vec::new();
        while remaining != 0 {
            let start = remaining.trailing_zeros() as usize;
            let mut component = 1_u8 << start;
            remaining &= !(1 << start);
            let mut queue = VecDeque::from([start]);
            while let Some(a) = queue.pop_front() {
                for b in 0..self.n {
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
        answer.sort_unstable();
        answer
    }
}

fn edge_slot(a: usize, b: usize) -> usize {
    let (left, right) = if a < b { (a, b) } else { (b, a) };
    right * (right - 1) / 2 + left
}

fn endpoints(n: usize, slot: usize) -> (usize, usize) {
    for right in 1..n {
        for left in 0..right {
            if edge_slot(left, right) == slot {
                return (left, right);
            }
        }
    }
    panic!("edge slot {slot} is outside K_{n}");
}

fn subset(a: u8, b: u8) -> bool {
    a & !b == 0
}

fn proper_subset(a: u8, b: u8) -> bool {
    a != b && subset(a, b)
}

fn unmarked_compatible(graph: Graph, a: u8, b: u8) -> bool {
    if subset(a, b) || subset(b, a) {
        return true;
    }
    a & b == 0 && !graph.connected(a | b)
}

fn marked_compatible(a: MarkedTube, b: MarkedTube) -> bool {
    if proper_subset(a.vertices, b.vertices) {
        b.mark == Mark::Thick || a.mark == Mark::Thin
    } else if proper_subset(b.vertices, a.vertices) {
        a.mark == Mark::Thick || b.mark == Mark::Thin
    } else {
        true
    }
}

fn valid_face(graph: Graph, face: &Face) -> bool {
    if face.mark_of(graph.all()).is_none() {
        return false;
    }
    for i in 0..face.0.len() {
        if !graph.connected(face.0[i].vertices) {
            return false;
        }
        if i > 0 && face.0[i - 1].vertices >= face.0[i].vertices {
            return false;
        }
        for j in i + 1..face.0.len() {
            if !unmarked_compatible(graph, face.0[i].vertices, face.0[j].vertices)
                || !marked_compatible(face.0[i], face.0[j])
            {
                return false;
            }
        }
    }
    true
}

fn enumerate_unmarked_tubings(graph: Graph) -> Vec<Vec<u8>> {
    let proper: Vec<_> = graph
        .tubes()
        .into_iter()
        .filter(|&tube| tube != graph.all())
        .collect();
    let mut answer = Vec::new();
    fn visit(
        graph: Graph,
        proper: &[u8],
        start: usize,
        chosen: &mut Vec<u8>,
        answer: &mut Vec<Vec<u8>>,
    ) {
        let mut tubing = chosen.clone();
        tubing.push(graph.all());
        tubing.sort_unstable();
        answer.push(tubing);
        for index in start..proper.len() {
            let candidate = proper[index];
            if chosen
                .iter()
                .all(|&old| unmarked_compatible(graph, old, candidate))
            {
                chosen.push(candidate);
                visit(graph, proper, index + 1, chosen, answer);
                chosen.pop();
            }
        }
    }
    visit(graph, &proper, 0, &mut Vec::new(), &mut answer);
    answer
}

fn enumerate_faces(graph: Graph) -> Vec<Face> {
    let mut answer = Vec::new();
    for tubing in enumerate_unmarked_tubings(graph) {
        fn mark(
            graph: Graph,
            tubing: &[u8],
            index: usize,
            chosen: &mut Vec<MarkedTube>,
            answer: &mut Vec<Face>,
        ) {
            if index == tubing.len() {
                let face = Face(chosen.clone());
                debug_assert!(valid_face(graph, &face));
                answer.push(face);
                return;
            }
            for marking in [Mark::Thin, Mark::Thick, Mark::Broken] {
                let candidate = MarkedTube {
                    vertices: tubing[index],
                    mark: marking,
                };
                if chosen.iter().all(|&old| marked_compatible(old, candidate)) {
                    chosen.push(candidate);
                    mark(graph, tubing, index + 1, chosen, answer);
                    chosen.pop();
                }
            }
        }
        mark(graph, &tubing, 0, &mut Vec::new(), &mut answer);
    }
    answer.sort();
    answer.dedup();
    answer
}

struct Poset {
    graph: Graph,
    faces: Vec<Face>,
    indices: HashMap<Face, usize>,
    covers: Vec<Vec<usize>>,
    down: Option<Vec<Vec<u64>>>,
}

impl Poset {
    fn new(graph: Graph, compute_closure: bool) -> Self {
        let faces = enumerate_faces(graph);
        let indices: HashMap<_, _> = faces
            .iter()
            .cloned()
            .enumerate()
            .map(|(index, face)| (face, index))
            .collect();
        let mut covers = vec![Vec::new(); faces.len()];
        let tubes = graph.tubes();
        let add = |face: Face, from: usize, covers: &mut Vec<Vec<usize>>| {
            let to = *indices.get(&face).expect("valid refinement was enumerated");
            assert_eq!(faces[to].codimension(), faces[from].codimension() + 1);
            covers[from].push(to);
        };

        for (from, coarse) in faces.iter().enumerate() {
            // Definition 5(1): resolve one broken mark.
            for index in 0..coarse.0.len() {
                if coarse.0[index].mark != Mark::Broken {
                    continue;
                }
                for marking in [Mark::Thin, Mark::Thick] {
                    let mut refined = coarse.clone();
                    refined.0[index].mark = marking;
                    if valid_face(graph, &refined) {
                        add(refined, from, &mut covers);
                    }
                }
            }

            // Definition 5(2),(3): add a thin or thick tube in its permitted
            // paint region.
            for &vertices in &tubes {
                if coarse.contains(vertices) {
                    continue;
                }
                for marking in [Mark::Thin, Mark::Thick] {
                    let permitted_outer = coarse.0.iter().any(|outer| {
                        proper_subset(vertices, outer.vertices)
                            && match marking {
                                Mark::Thin => {
                                    outer.mark == Mark::Thin || outer.mark == Mark::Broken
                                }
                                Mark::Thick => outer.mark == Mark::Thick,
                                Mark::Broken => unreachable!(),
                            }
                    });
                    if !permitted_outer {
                        continue;
                    }
                    let mut entries = coarse.0.clone();
                    entries.push(MarkedTube {
                        vertices,
                        mark: marking,
                    });
                    entries.sort();
                    let refined = Face(entries);
                    if valid_face(graph, &refined) {
                        add(refined, from, &mut covers);
                    }
                }
            }

            // Definition 5(4): thicken broken v and add a nonempty compatible
            // collection of closely nested broken tubes.
            for v_index in 0..coarse.0.len() {
                let v = coarse.0[v_index];
                if v.mark != Mark::Broken {
                    continue;
                }
                let candidates: Vec<_> = tubes
                    .iter()
                    .copied()
                    .filter(|&u| {
                        !coarse.contains(u)
                            && proper_subset(u, v.vertices)
                            && !coarse.0.iter().any(|w| {
                                proper_subset(u, w.vertices)
                                    && proper_subset(w.vertices, v.vertices)
                            })
                    })
                    .collect();
                fn collections(
                    graph: Graph,
                    candidates: &[u8],
                    start: usize,
                    chosen: &mut Vec<u8>,
                    visit: &mut impl FnMut(&[u8]),
                ) {
                    for index in start..candidates.len() {
                        let candidate = candidates[index];
                        if chosen
                            .iter()
                            .all(|&old| unmarked_compatible(graph, old, candidate))
                        {
                            chosen.push(candidate);
                            visit(chosen);
                            collections(graph, candidates, index + 1, chosen, visit);
                            chosen.pop();
                        }
                    }
                }
                let mut visit = |new_broken: &[u8]| {
                    let mut entries = coarse.0.clone();
                    entries[v_index].mark = Mark::Thick;
                    entries.extend(new_broken.iter().map(|&vertices| MarkedTube {
                        vertices,
                        mark: Mark::Broken,
                    }));
                    entries.sort();
                    let refined = Face(entries);
                    if valid_face(graph, &refined) {
                        add(refined, from, &mut covers);
                    }
                };
                collections(graph, &candidates, 0, &mut Vec::new(), &mut visit);
            }
            covers[from].sort_unstable();
            covers[from].dedup();
        }

        let down = if compute_closure {
            let words = faces.len().div_ceil(64);
            let mut closure = vec![vec![0_u64; words]; faces.len()];
            let mut order: Vec<_> = (0..faces.len()).collect();
            order.sort_by_key(|&index| std::cmp::Reverse(faces[index].codimension()));
            for coarse in order {
                closure[coarse][coarse / 64] |= 1 << (coarse % 64);
                for &refined in &covers[coarse] {
                    for word in 0..words {
                        closure[coarse][word] |= closure[refined][word];
                    }
                }
            }
            Some(closure)
        } else {
            None
        };

        let top = Face(vec![MarkedTube {
            vertices: graph.all(),
            mark: Mark::Broken,
        }]);
        let top_index = indices[&top];
        if let Some(closure) = &down {
            assert_eq!(
                closure[top_index]
                    .iter()
                    .map(|word| word.count_ones() as usize)
                    .sum::<usize>(),
                faces.len()
            );
        }
        Self {
            graph,
            faces,
            indices,
            covers,
            down,
        }
    }

    fn index(&self, face: &Face) -> Option<usize> {
        self.indices.get(face).copied()
    }

    fn refines(&self, refined: usize, coarse: usize) -> bool {
        let down = self.down.as_ref().expect("target closure was requested");
        down[coarse][refined / 64] & (1 << (refined % 64)) != 0
    }
}

#[derive(Clone, Copy, Debug, Eq, Hash, Ord, PartialEq, PartialOrd)]
enum Rule {
    ComponentsInnermost,
    Forget,
    ComponentsOutermost,
}

impl Rule {
    const ALL: [Self; 3] = [
        Self::ComponentsInnermost,
        Self::Forget,
        Self::ComponentsOutermost,
    ];

    fn name(self) -> &'static str {
        match self {
            Self::ComponentsInnermost => "components/innermost",
            Self::Forget => "forget",
            Self::ComponentsOutermost => "components/outermost",
        }
    }
}

#[derive(Clone, Copy, Debug)]
struct Contribution {
    source: u8,
    mark: Mark,
}

fn compare_face(rule: Rule, target: Graph, source: &Face) -> Option<Face> {
    if rule == Rule::Forget {
        let face = Face(
            source
                .0
                .iter()
                .copied()
                .filter(|tube| target.connected(tube.vertices))
                .collect(),
        );
        return valid_face(target, &face).then_some(face);
    }

    let mut by_component: BTreeMap<u8, Vec<Contribution>> = BTreeMap::new();
    for tube in &source.0 {
        for component in target.components(tube.vertices) {
            by_component
                .entry(component)
                .or_default()
                .push(Contribution {
                    source: tube.vertices,
                    mark: tube.mark,
                });
        }
    }
    let mut entries = Vec::new();
    for (vertices, contributions) in by_component {
        let marked = match rule {
            Rule::ComponentsInnermost => {
                contributions
                    .iter()
                    .min_by_key(|entry| entry.source.count_ones())
                    .expect("every component has a source")
                    .mark
            }
            Rule::ComponentsOutermost => {
                contributions
                    .iter()
                    .max_by_key(|entry| entry.source.count_ones())
                    .expect("every component has a source")
                    .mark
            }
            Rule::Forget => unreachable!(),
        };
        entries.push(MarkedTube {
            vertices,
            mark: marked,
        });
    }
    let face = Face(entries);
    valid_face(target, &face).then_some(face)
}

#[derive(Clone, Debug, Eq, PartialEq)]
struct Witness {
    key: (usize, u32, usize, usize, String),
    text: String,
}

#[derive(Clone, Debug, Default)]
struct MapAudit {
    inclusions: usize,
    sources: usize,
    cover_relations: usize,
    covariance_checks: usize,
    undefined: usize,
    order_failures: usize,
    dimension_failures: usize,
    missed_targets: usize,
    covariance_failures: usize,
    first_undefined: Option<Witness>,
    first_order_failure: Option<Witness>,
    first_dimension_failure: Option<Witness>,
    first_missed: Option<Witness>,
    first_covariance_failure: Option<Witness>,
}

#[derive(Clone, Debug, Default)]
struct TwoPathAudit {
    diagrams: usize,
    sources: usize,
    path_failures: usize,
    direct_failures: usize,
    first_path_failure: Option<Witness>,
    first_direct_failure: Option<Witness>,
}

fn mask_name(n: usize, vertices: u8) -> String {
    let labels: Vec<_> = (0..n)
        .filter(|&vertex| vertices & (1 << vertex) != 0)
        .map(|vertex| vertex.to_string())
        .collect();
    format!("{{{}}}", labels.join(","))
}

fn face_name(n: usize, face: &Face) -> String {
    let entries: Vec<_> = face
        .0
        .iter()
        .map(|tube| format!("{}:{}", mask_name(n, tube.vertices), tube.mark.letter()))
        .collect();
    format!("[{}]", entries.join(" "))
}

fn graph_name(graph: Graph) -> String {
    let edges: Vec<_> = (0..graph.edge_capacity())
        .filter(|&slot| graph.edges & (1 << slot) != 0)
        .map(|slot| {
            let (a, b) = endpoints(graph.n, slot);
            format!("{a}-{b}")
        })
        .collect();
    format!("n={} {{{}}}", graph.n, edges.join(","))
}

fn keep_smallest(slot: &mut Option<Witness>, graph: Graph, grading_face: &Face, text: String) {
    let key = (
        graph.n,
        graph.edges.count_ones(),
        grading_face.codimension(),
        grading_face.0.len(),
        text.clone(),
    );
    let replace = slot.as_ref().map(|old| key < old.key).unwrap_or(true);
    if replace {
        *slot = Some(Witness { key, text });
    }
}

fn merge_witness(target: &mut Option<Witness>, source: Option<Witness>) {
    if let Some(source) = source {
        if target
            .as_ref()
            .map(|current| source.key < current.key)
            .unwrap_or(true)
        {
            *target = Some(source);
        }
    }
}

fn permute_mask(n: usize, vertices: u8, permutation: &[usize]) -> u8 {
    let mut answer = 0;
    for vertex in 0..n {
        if vertices & (1 << vertex) != 0 {
            answer |= 1 << permutation[vertex];
        }
    }
    answer
}

fn permute_graph(graph: Graph, permutation: &[usize]) -> Graph {
    let mut edges = 0;
    for slot in 0..graph.edge_capacity() {
        if graph.edges & (1 << slot) == 0 {
            continue;
        }
        let (a, b) = endpoints(graph.n, slot);
        edges |= 1 << edge_slot(permutation[a], permutation[b]);
    }
    Graph { n: graph.n, edges }
}

fn permute_face(n: usize, face: &Face, permutation: &[usize]) -> Face {
    let mut entries: Vec<_> = face
        .0
        .iter()
        .map(|tube| MarkedTube {
            vertices: permute_mask(n, tube.vertices, permutation),
            mark: tube.mark,
        })
        .collect();
    entries.sort();
    Face(entries)
}

fn permutations(n: usize) -> Vec<Vec<usize>> {
    fn visit(n: usize, used: &mut [bool], chosen: &mut Vec<usize>, answer: &mut Vec<Vec<usize>>) {
        if chosen.len() == n {
            answer.push(chosen.clone());
            return;
        }
        for value in 0..n {
            if used[value] {
                continue;
            }
            used[value] = true;
            chosen.push(value);
            visit(n, used, chosen, answer);
            chosen.pop();
            used[value] = false;
        }
    }
    let mut answer = Vec::new();
    visit(n, &mut vec![false; n], &mut Vec::new(), &mut answer);
    answer
}

fn canonical_diagram(source: Graph, target: Graph) -> (Graph, Graph) {
    assert_eq!(source.n, target.n);
    permutations(source.n)
        .into_iter()
        .map(|permutation| {
            (
                permute_graph(source, &permutation),
                permute_graph(target, &permutation),
            )
        })
        .min_by_key(|(permuted_source, permuted_target)| {
            (permuted_source.edges, permuted_target.edges)
        })
        .expect("every finite vertex set has a permutation")
}

fn audit_one_inclusion(rule: Rule, source: &Poset, target: &Poset) -> MapAudit {
    assert_eq!(source.graph.n, target.graph.n);
    assert_eq!(source.graph.edges & target.graph.edges, target.graph.edges);
    let mut audit = MapAudit {
        inclusions: 1,
        sources: source.faces.len(),
        ..MapAudit::default()
    };
    let mut values = Vec::with_capacity(source.faces.len());
    let mut hit = vec![false; target.faces.len()];
    let permutations = permutations(source.graph.n);

    for face in &source.faces {
        let image = compare_face(rule, target.graph, face);
        let value = image.as_ref().and_then(|candidate| target.index(candidate));
        match value {
            Some(index) => {
                hit[index] = true;
                if target.faces[index].codimension() < face.codimension() {
                    audit.dimension_failures += 1;
                    keep_smallest(
                        &mut audit.first_dimension_failure,
                        source.graph,
                        face,
                        format!(
                            "{} -> {}: {} codim {} maps to {} codim {}",
                            graph_name(source.graph),
                            graph_name(target.graph),
                            face_name(source.graph.n, face),
                            face.codimension(),
                            face_name(target.graph.n, &target.faces[index]),
                            target.faces[index].codimension()
                        ),
                    );
                }
            }
            None => {
                audit.undefined += 1;
                keep_smallest(
                    &mut audit.first_undefined,
                    source.graph,
                    face,
                    format!(
                        "{} -> {} is undefined on {}",
                        graph_name(source.graph),
                        graph_name(target.graph),
                        face_name(source.graph.n, face)
                    ),
                );
            }
        }

        for permutation in &permutations {
            audit.covariance_checks += 1;
            let permuted_target = permute_graph(target.graph, permutation);
            let left = image
                .as_ref()
                .map(|candidate| permute_face(source.graph.n, candidate, permutation));
            let permuted_source = permute_face(source.graph.n, face, permutation);
            debug_assert!(valid_face(
                permute_graph(source.graph, permutation),
                &permuted_source
            ));
            let right = compare_face(rule, permuted_target, &permuted_source);
            if left != right {
                audit.covariance_failures += 1;
                keep_smallest(
                    &mut audit.first_covariance_failure,
                    source.graph,
                    face,
                    format!(
                        "{} -> {} fails permutation covariance on {}",
                        graph_name(source.graph),
                        graph_name(target.graph),
                        face_name(source.graph.n, face)
                    ),
                );
            }
        }
        values.push(value);
    }

    for (coarse, refinements) in source.covers.iter().enumerate() {
        for &refined in refinements {
            audit.cover_relations += 1;
            if let (Some(image_coarse), Some(image_refined)) = (values[coarse], values[refined]) {
                if !target.refines(image_refined, image_coarse) {
                    audit.order_failures += 1;
                    keep_smallest(
                        &mut audit.first_order_failure,
                        source.graph,
                        &source.faces[coarse],
                        format!(
                            "{} -> {}: {} refines {}, but {} does not refine {}",
                            graph_name(source.graph),
                            graph_name(target.graph),
                            face_name(source.graph.n, &source.faces[refined]),
                            face_name(source.graph.n, &source.faces[coarse]),
                            face_name(target.graph.n, &target.faces[image_refined]),
                            face_name(target.graph.n, &target.faces[image_coarse])
                        ),
                    );
                }
            }
        }
    }

    audit.missed_targets = hit.iter().filter(|&&seen| !seen).count();
    for (index, seen) in hit.iter().enumerate() {
        if !seen {
            keep_smallest(
                &mut audit.first_missed,
                target.graph,
                &target.faces[index],
                format!(
                    "{} is not hit from {}",
                    face_name(target.graph.n, &target.faces[index]),
                    graph_name(source.graph)
                ),
            );
        }
    }
    audit
}

fn accumulate_map(total: &mut MapAudit, part: MapAudit) {
    total.inclusions += part.inclusions;
    total.sources += part.sources;
    total.cover_relations += part.cover_relations;
    total.covariance_checks += part.covariance_checks;
    total.undefined += part.undefined;
    total.order_failures += part.order_failures;
    total.dimension_failures += part.dimension_failures;
    total.missed_targets += part.missed_targets;
    total.covariance_failures += part.covariance_failures;
    merge_witness(&mut total.first_undefined, part.first_undefined);
    merge_witness(&mut total.first_order_failure, part.first_order_failure);
    merge_witness(
        &mut total.first_dimension_failure,
        part.first_dimension_failure,
    );
    merge_witness(&mut total.first_missed, part.first_missed);
    merge_witness(
        &mut total.first_covariance_failure,
        part.first_covariance_failure,
    );
}

fn connected_graphs(n: usize) -> Vec<Graph> {
    let capacity = n * (n - 1) / 2;
    (0..(1_u16 << capacity))
        .map(|edges| Graph { n, edges })
        .filter(|graph| graph.connected(graph.all()))
        .collect()
}

fn audit_two_paths(
    final_graph: Graph,
    edge_a: usize,
    edge_b: usize,
    totals: &mut BTreeMap<Rule, TwoPathAudit>,
) {
    let middle_a = Graph {
        n: final_graph.n,
        edges: final_graph.edges | (1 << edge_a),
    };
    let middle_b = Graph {
        n: final_graph.n,
        edges: final_graph.edges | (1 << edge_b),
    };
    let source_graph = Graph {
        n: final_graph.n,
        edges: final_graph.edges | (1 << edge_a) | (1 << edge_b),
    };
    assert!(middle_a.connected(middle_a.all()));
    assert!(middle_b.connected(middle_b.all()));
    assert!(source_graph.connected(source_graph.all()));
    let faces = enumerate_faces(source_graph);
    for rule in Rule::ALL {
        let total = totals.entry(rule).or_default();
        total.diagrams += 1;
        total.sources += faces.len();
        for face in &faces {
            let through_a = compare_face(rule, middle_a, face)
                .and_then(|middle| compare_face(rule, final_graph, &middle));
            let through_b = compare_face(rule, middle_b, face)
                .and_then(|middle| compare_face(rule, final_graph, &middle));
            let direct = compare_face(rule, final_graph, face);
            if through_a != through_b {
                total.path_failures += 1;
                keep_smallest(
                    &mut total.first_path_failure,
                    source_graph,
                    face,
                    format!(
                        "{} -> {}: deletion orders disagree on {}; via first={:?}, via second={:?}",
                        graph_name(source_graph),
                        graph_name(final_graph),
                        face_name(source_graph.n, face),
                        through_a
                            .as_ref()
                            .map(|value| face_name(source_graph.n, value)),
                        through_b
                            .as_ref()
                            .map(|value| face_name(source_graph.n, value))
                    ),
                );
            }
            if through_a != direct || through_b != direct {
                total.direct_failures += 1;
                keep_smallest(
                    &mut total.first_direct_failure,
                    source_graph,
                    face,
                    format!(
                        "{} -> {}: a two-step carrier differs from direct on {}; direct={:?}",
                        graph_name(source_graph),
                        graph_name(final_graph),
                        face_name(source_graph.n, face),
                        direct
                            .as_ref()
                            .map(|value| face_name(source_graph.n, value))
                    ),
                );
            }
        }
    }
}

fn unmarked_component_image(target: Graph, tubing: &[u8]) -> Vec<u8> {
    let mut answer = BTreeSet::new();
    for &tube in tubing {
        answer.extend(target.components(tube));
    }
    answer.into_iter().collect()
}

fn theta_graph() -> Graph {
    let mut edges = 0;
    for left in 0..2 {
        for right in 2..5 {
            edges |= 1 << edge_slot(left, right);
        }
    }
    Graph { n: 5, edges }
}

fn audit_theta_unmarked_agreement() -> (usize, usize, usize) {
    let theta = theta_graph();
    let marked_faces = enumerate_faces(theta);
    let unmarked_tubings = enumerate_unmarked_tubings(theta);
    assert_eq!(marked_faces.len(), 3_847);
    assert_eq!(unmarked_tubings.len(), 419);
    let mut marked_checks = 0;
    let mut unmarked_checks = 0;
    let mut failures = 0;
    for slot in 0..theta.edge_capacity() {
        if theta.edges & (1 << slot) == 0 {
            continue;
        }
        let target = Graph {
            n: theta.n,
            edges: theta.edges & !(1 << slot),
        };
        assert!(target.connected(target.all()));
        for face in &marked_faces {
            marked_checks += 1;
            let expected = unmarked_component_image(target, &face.underlying());
            let actual = compare_face(Rule::ComponentsInnermost, target, face)
                .expect("the innermost carrier is total on Theta")
                .underlying();
            if actual != expected {
                failures += 1;
            }
        }
        for tubing in &unmarked_tubings {
            unmarked_checks += 1;
            let image = unmarked_component_image(target, tubing);
            let valid = image.contains(&target.all())
                && image.iter().all(|&tube| target.connected(tube))
                && (0..image.len()).all(|i| {
                    (i + 1..image.len()).all(|j| unmarked_compatible(target, image[i], image[j]))
                });
            if !valid {
                failures += 1;
            }
        }
    }
    (marked_checks, unmarked_checks, failures)
}

fn print_witness(label: &str, witness: &Option<Witness>) {
    if let Some(witness) = witness {
        println!("  {label}: {}", witness.text);
    }
}

fn main() {
    let started = Instant::now();
    let mut graph_counts = Vec::new();
    let mut one_edge: BTreeMap<Rule, MapAudit> = BTreeMap::new();
    let mut two_edge: BTreeMap<Rule, TwoPathAudit> = BTreeMap::new();
    let mut inclusions_by_n = Vec::new();
    let mut diagrams_by_n = Vec::new();

    for n in 1..=5 {
        let graphs = connected_graphs(n);
        graph_counts.push(graphs.len());
        let mut inclusion_count = 0;
        let mut diagram_count = 0;
        let mut inclusion_classes = BTreeSet::new();
        let mut diagram_classes = BTreeSet::new();
        for &target_graph in &graphs {
            let missing: Vec<_> = (0..target_graph.edge_capacity())
                .filter(|&slot| target_graph.edges & (1 << slot) == 0)
                .collect();
            for &slot in &missing {
                let source_graph = Graph {
                    n,
                    edges: target_graph.edges | (1 << slot),
                };
                inclusion_count += 1;
                inclusion_classes.insert(canonical_diagram(source_graph, target_graph));
            }
            for left in 0..missing.len() {
                for right in left + 1..missing.len() {
                    let source_graph = Graph {
                        n,
                        edges: target_graph.edges | (1 << missing[left]) | (1 << missing[right]),
                    };
                    diagram_classes.insert(canonical_diagram(source_graph, target_graph));
                    diagram_count += 1;
                }
            }
        }
        for &(source_graph, target_graph) in &inclusion_classes {
            let source = Poset::new(source_graph, false);
            let target = Poset::new(target_graph, true);
            for rule in Rule::ALL {
                let part = audit_one_inclusion(rule, &source, &target);
                accumulate_map(one_edge.entry(rule).or_default(), part);
            }
        }
        for &(source_graph, final_graph) in &diagram_classes {
            let deleted: Vec<_> = (0..source_graph.edge_capacity())
                .filter(|&slot| {
                    source_graph.edges & (1 << slot) != 0 && final_graph.edges & (1 << slot) == 0
                })
                .collect();
            assert_eq!(deleted.len(), 2);
            audit_two_paths(final_graph, deleted[0], deleted[1], &mut two_edge);
        }
        inclusions_by_n.push(inclusion_count);
        diagrams_by_n.push(diagram_count);
        println!(
            "SCOPE n={n} connected_labeled_graphs={} one_edge_labeled={inclusion_count} one_edge_isomorphism_classes={} two_edge_labeled={diagram_count} two_edge_isomorphism_classes={}",
            graphs.len(),
            inclusion_classes.len(),
            diagram_classes.len()
        );
    }

    assert_eq!(graph_counts, vec![1, 1, 4, 38, 728]);

    println!("\nONE-EDGE MARKED FACE-POSET AUDIT");
    for rule in Rule::ALL {
        let audit = &one_edge[&rule];
        println!(
            "  {} inclusions={} sources={} covers={} covariance_generators={} undefined={} order_failures={} dimension_failures={} missed_targets={} covariance_failures={}",
            rule.name(),
            audit.inclusions,
            audit.sources,
            audit.cover_relations,
            audit.covariance_checks,
            audit.undefined,
            audit.order_failures,
            audit.dimension_failures,
            audit.missed_targets,
            audit.covariance_failures
        );
        print_witness("undefined witness", &audit.first_undefined);
        print_witness("order witness", &audit.first_order_failure);
        print_witness("dimension witness", &audit.first_dimension_failure);
        print_witness("surjectivity witness", &audit.first_missed);
        print_witness("covariance witness", &audit.first_covariance_failure);
    }

    println!("\nTWO-EDGE DELETION AUDIT");
    for rule in Rule::ALL {
        let audit = &two_edge[&rule];
        println!(
            "  {} diagrams={} sources={} path_failures={} direct_failures={}",
            rule.name(),
            audit.diagrams,
            audit.sources,
            audit.path_failures,
            audit.direct_failures
        );
        print_witness("path witness", &audit.first_path_failure);
        print_witness("direct witness", &audit.first_direct_failure);
    }

    let (theta_marked, theta_unmarked, theta_failures) = audit_theta_unmarked_agreement();
    println!("\nTHETA UNMARKED BASELINE");
    println!(
        "  marked_forgetful_checks={theta_marked} unmarked_projection_checks={theta_unmarked} failures={theta_failures}"
    );

    let inner = &one_edge[&Rule::ComponentsInnermost];
    assert_eq!(inner.undefined, 0);
    assert_eq!(inner.order_failures, 0);
    assert_eq!(inner.dimension_failures, 0);
    assert_eq!(inner.missed_targets, 0);
    assert_eq!(inner.covariance_failures, 0);
    let inner_two = &two_edge[&Rule::ComponentsInnermost];
    assert_eq!(inner_two.path_failures, 0);
    assert_eq!(inner_two.direct_failures, 0);
    assert_eq!(theta_failures, 0);

    let forget = &one_edge[&Rule::Forget];
    let outer = &one_edge[&Rule::ComponentsOutermost];
    assert!(forget.order_failures + forget.dimension_failures + forget.missed_targets > 0);
    assert!(
        outer.undefined
            + outer.order_failures
            + outer.dimension_failures
            + outer.missed_targets
            + two_edge[&Rule::ComponentsOutermost].path_failures
            + two_edge[&Rule::ComponentsOutermost].direct_failures
            > 0
    );

    println!("\nVERDICT");
    println!(
        "  component/innermost passed every finite test on all {} labeled connected graphs through n=5",
        graph_counts.iter().sum::<usize>()
    );
    println!(
        "  scope one_edge_by_n={inclusions_by_n:?} two_edge_by_n={diagrams_by_n:?}; this is finite evidence, not an all-graph proof"
    );
    println!("  elapsed_seconds={:.3}", started.elapsed().as_secs_f64());
}
