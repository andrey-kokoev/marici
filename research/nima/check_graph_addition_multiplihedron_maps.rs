//! Exact graph-edge-addition audit for marked-tubing face posets.
//!
//! This program implements Definitions 1, 3, 4, and 5 of
//! Devadoss--Forcey, "Marked tubes and the graph multiplihedron".  It tests
//! proposed contravariant face carriers J(G+e) -> J(G) for every edge in the
//! twelve spanning-tree presentations of K_{2,3}.  This is a finite
//! combinatorial certificate; it does not assert that an order-preserving
//! carrier is induced by a continuous cellular map unless stated separately.

use std::collections::{BTreeMap, BTreeSet, HashMap, VecDeque};

const N: usize = 5;
const ALL: u8 = (1 << N) - 1;

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
}

#[derive(Clone, Copy, Debug, Eq, Hash, Ord, PartialEq, PartialOrd)]
struct Graph(u8);

impl Graph {
    fn has_edge(self, a: usize, b: usize) -> bool {
        edge_slot(a, b)
            .map(|slot| self.0 & (1 << slot) != 0)
            .unwrap_or(false)
    }

    fn connected(self, vertices: u8) -> bool {
        if vertices == 0 {
            return false;
        }
        let start = vertices.trailing_zeros() as usize;
        let mut seen = 1_u8 << start;
        let mut queue = VecDeque::from([start]);
        while let Some(a) = queue.pop_front() {
            for b in 0..N {
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
        (1..=ALL)
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
        answer.sort_unstable();
        answer
    }
}

fn edge_slot(a: usize, b: usize) -> Option<usize> {
    let (left, right) = if a < 2 && b >= 2 {
        (a, b)
    } else if b < 2 && a >= 2 {
        (b, a)
    } else {
        return None;
    };
    Some(2 * (right - 2) + left)
}

fn endpoints(slot: usize) -> (usize, usize) {
    (slot % 2, 2 + slot / 2)
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
    if face.mark_of(ALL).is_none() {
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
        .filter(|&tube| tube != ALL)
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
        tubing.push(ALL);
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
    // `covers[coarse]` lists its one-step refinements.
    covers: Vec<Vec<usize>>,
    // `down[coarse]` contains every refinement of `coarse`, including itself.
    down: Vec<Vec<u64>>,
}

impl Poset {
    fn new(graph: Graph) -> Self {
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
            // Definition 5(1): resolve one broken marking.
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

            // Definition 5(2),(3): add one thin or thick tube inside an
            // existing tube with the same permitted paint region.
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

            // Definition 5(4): thicken a broken v while simultaneously
            // adding a nonempty compatible collection of broken tubes that
            // are closely nested in v (Definition 4).
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

        let words = faces.len().div_ceil(64);
        let mut down = vec![vec![0_u64; words]; faces.len()];
        let mut order: Vec<_> = (0..faces.len()).collect();
        order.sort_by_key(|&index| std::cmp::Reverse(faces[index].codimension()));
        for coarse in order {
            down[coarse][coarse / 64] |= 1 << (coarse % 64);
            for &refined in &covers[coarse] {
                for word in 0..words {
                    down[coarse][word] |= down[refined][word];
                }
            }
        }

        let top = Face(vec![MarkedTube {
            vertices: ALL,
            mark: Mark::Broken,
        }]);
        let top_index = indices[&top];
        assert_eq!(
            down[top_index]
                .iter()
                .map(|word| word.count_ones() as usize)
                .sum::<usize>(),
            faces.len()
        );
        for (coarse, adjacent) in covers.iter().enumerate() {
            for &refined in adjacent {
                assert_eq!(
                    faces[refined].codimension(),
                    faces[coarse].codimension() + 1
                );
            }
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
        self.down[coarse][refined / 64] & (1 << (refined % 64)) != 0
    }
}

#[derive(Clone, Copy, Debug, Eq, Hash, PartialEq)]
enum Rule {
    Forget,
    ComponentsInnermost,
    ComponentsOutermost,
    ComponentsThinPriority,
    ComponentsThickPriority,
    ComponentsBrokenJoin,
    ComponentsUnanimous,
}

impl Rule {
    const ALL: [Self; 7] = [
        Self::Forget,
        Self::ComponentsInnermost,
        Self::ComponentsOutermost,
        Self::ComponentsThinPriority,
        Self::ComponentsThickPriority,
        Self::ComponentsBrokenJoin,
        Self::ComponentsUnanimous,
    ];

    fn name(self) -> &'static str {
        match self {
            Self::Forget => "forget",
            Self::ComponentsInnermost => "components/innermost",
            Self::ComponentsOutermost => "components/outermost",
            Self::ComponentsThinPriority => "components/thin-priority",
            Self::ComponentsThickPriority => "components/thick-priority",
            Self::ComponentsBrokenJoin => "components/broken-join",
            Self::ComponentsUnanimous => "components/unanimous",
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
        let mark = match rule {
            Rule::ComponentsInnermost => {
                contributions
                    .iter()
                    .min_by_key(|entry| entry.source.count_ones())
                    .unwrap()
                    .mark
            }
            Rule::ComponentsOutermost => {
                contributions
                    .iter()
                    .max_by_key(|entry| entry.source.count_ones())
                    .unwrap()
                    .mark
            }
            Rule::ComponentsThinPriority => {
                if contributions.iter().any(|entry| entry.mark == Mark::Thin) {
                    Mark::Thin
                } else if contributions.iter().any(|entry| entry.mark == Mark::Broken) {
                    Mark::Broken
                } else {
                    Mark::Thick
                }
            }
            Rule::ComponentsThickPriority => {
                if contributions.iter().any(|entry| entry.mark == Mark::Thick) {
                    Mark::Thick
                } else if contributions.iter().any(|entry| entry.mark == Mark::Broken) {
                    Mark::Broken
                } else {
                    Mark::Thin
                }
            }
            Rule::ComponentsBrokenJoin => {
                let first = contributions[0].mark;
                if contributions.iter().all(|entry| entry.mark == first) {
                    first
                } else {
                    Mark::Broken
                }
            }
            Rule::ComponentsUnanimous => {
                let first = contributions[0].mark;
                if !contributions.iter().all(|entry| entry.mark == first) {
                    return None;
                }
                first
            }
            Rule::Forget => unreachable!(),
        };
        entries.push(MarkedTube { vertices, mark });
    }
    let face = Face(entries);
    valid_face(target, &face).then_some(face)
}

#[derive(Clone, Debug, Default)]
struct MapAudit {
    sources: usize,
    undefined: usize,
    order_failures: usize,
    dimension_failures: usize,
    missed_targets: usize,
    covariance_failures: usize,
    first_undefined: Option<Witness>,
    first_order_failure: Option<Witness>,
    first_dimension_failure: Option<Witness>,
    first_missed: Option<Witness>,
}

#[derive(Clone, Debug, Eq, PartialEq)]
struct Witness {
    // Lowest source/target codimension, then fewest tubes, then lexical form.
    key: (usize, usize, String),
    text: String,
}

fn face_name(face: &Face) -> String {
    let entries: Vec<_> = face
        .0
        .iter()
        .map(|tube| format!("{}:{}", mask_name(tube.vertices), tube.mark.letter()))
        .collect();
    format!("[{}]", entries.join(" "))
}

fn mask_name(vertices: u8) -> String {
    const LABELS: [&str; N] = ["L0", "L1", "R0", "R1", "R2"];
    let labels: Vec<_> = (0..N)
        .filter(|&vertex| vertices & (1 << vertex) != 0)
        .map(|vertex| LABELS[vertex])
        .collect();
    format!("{{{}}}", labels.join(","))
}

fn graph_name(graph: Graph) -> String {
    let edges: Vec<_> = (0..6)
        .filter(|&slot| graph.0 & (1 << slot) != 0)
        .map(|slot| {
            let (a, b) = endpoints(slot);
            format!("{}-{}", mask_name(1 << a), mask_name(1 << b))
        })
        .collect();
    format!("{{{}}}", edges.join(","))
}

fn audit_map(rule: Rule, source: &Poset, target: &Poset) -> (MapAudit, Vec<Option<usize>>) {
    assert_eq!((source.graph.0 & target.graph.0), target.graph.0);
    let mut audit = MapAudit {
        sources: source.faces.len(),
        ..MapAudit::default()
    };
    let mut values = Vec::with_capacity(source.faces.len());
    let mut hit = vec![false; target.faces.len()];
    for face in &source.faces {
        let value = compare_face(rule, target.graph, face).and_then(|image| target.index(&image));
        match value {
            Some(index) => {
                hit[index] = true;
                // A face carrier for a cellular map must not send a cell to
                // a higher-dimensional carrier face.  Since dim=N-codim,
                // this is codim(image) >= codim(source).
                if target.faces[index].codimension() < face.codimension() {
                    audit.dimension_failures += 1;
                    let witness = format!(
                        "{} (codim {}) maps to {} (codim {})",
                        face_name(face),
                        face.codimension(),
                        face_name(&target.faces[index]),
                        target.faces[index].codimension(),
                    );
                    keep_smallest(&mut audit.first_dimension_failure, witness, face);
                }
            }
            None => {
                audit.undefined += 1;
                let witness = format!(
                    "{} -> {} has no valid image for {}",
                    graph_name(source.graph),
                    graph_name(target.graph),
                    face_name(face)
                );
                keep_smallest(&mut audit.first_undefined, witness, face);
            }
        }
        values.push(value);
    }
    for (coarse, refinements) in source.covers.iter().enumerate() {
        for &refined in refinements {
            if let (Some(image_coarse), Some(image_refined)) = (values[coarse], values[refined]) {
                if !target.refines(image_refined, image_coarse) {
                    audit.order_failures += 1;
                    let witness = format!(
                        "{} -> {}: {} refines {}, but image {} does not refine {}",
                        graph_name(source.graph),
                        graph_name(target.graph),
                        face_name(&source.faces[refined]),
                        face_name(&source.faces[coarse]),
                        face_name(&target.faces[image_refined]),
                        face_name(&target.faces[image_coarse]),
                    );
                    keep_smallest(
                        &mut audit.first_order_failure,
                        witness,
                        &source.faces[coarse],
                    );
                }
            }
        }
    }
    audit.missed_targets = hit.iter().filter(|&&seen| !seen).count();
    for (index, seen) in hit.iter().enumerate() {
        if !seen {
            let witness = format!(
                "{} is not hit from {}",
                face_name(&target.faces[index]),
                graph_name(source.graph)
            );
            keep_smallest(&mut audit.first_missed, witness, &target.faces[index]);
        }
    }
    (audit, values)
}

fn keep_smallest(slot: &mut Option<Witness>, text: String, grading_face: &Face) {
    let key = (
        grading_face.codimension(),
        grading_face.0.len(),
        text.clone(),
    );
    let replace = slot.as_ref().map(|old| key < old.key).unwrap_or(true);
    if replace {
        *slot = Some(Witness { key, text });
    }
}

fn spanning_trees() -> Vec<Graph> {
    (0_u8..64)
        .map(Graph)
        .filter(|graph| graph.0.count_ones() == 4 && graph.connected(ALL))
        .collect()
}

fn unmarked_component_image(target: Graph, tubing: &[u8]) -> Vec<u8> {
    let mut answer = BTreeSet::new();
    for &tube in tubing {
        answer.extend(target.components(tube));
    }
    answer.into_iter().collect()
}

#[derive(Default)]
struct UnmarkedAudit {
    sources: usize,
    invalid: usize,
    dimension_failures: usize,
    missed_targets: usize,
    path_failures: usize,
}

fn audit_unmarked_inclusion(source: Graph, target: Graph, audit: &mut UnmarkedAudit) {
    let source_tubings = enumerate_unmarked_tubings(source);
    let target_tubings = enumerate_unmarked_tubings(target);
    let target_set: BTreeSet<_> = target_tubings.iter().cloned().collect();
    let mut hit = BTreeSet::new();
    for tubing in source_tubings {
        audit.sources += 1;
        let image = unmarked_component_image(target, &tubing);
        let valid = image.contains(&ALL)
            && image.iter().all(|&tube| target.connected(tube))
            && (0..image.len()).all(|i| {
                (i + 1..image.len()).all(|j| unmarked_compatible(target, image[i], image[j]))
            });
        if !valid || !target_set.contains(&image) {
            audit.invalid += 1;
        } else {
            hit.insert(image.clone());
        }
        // Graph-associahedral cell dimension is N-|tubing|.  Thus a
        // dimension-nonincreasing carrier has at least as many target tubes.
        if image.len() < tubing.len() {
            audit.dimension_failures += 1;
        }
    }
    audit.missed_targets += target_tubings
        .iter()
        .filter(|tubing| !hit.contains(*tubing))
        .count();
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

fn permute_mask(vertices: u8, permutation: [usize; N]) -> u8 {
    let mut answer = 0;
    for vertex in 0..N {
        if vertices & (1 << vertex) != 0 {
            answer |= 1 << permutation[vertex];
        }
    }
    answer
}

fn permute_graph(graph: Graph, permutation: [usize; N]) -> Graph {
    let mut answer = 0;
    for slot in 0..6 {
        if graph.0 & (1 << slot) == 0 {
            continue;
        }
        let (a, b) = endpoints(slot);
        answer |= 1 << edge_slot(permutation[a], permutation[b]).unwrap();
    }
    Graph(answer)
}

fn permute_face(face: &Face, permutation: [usize; N]) -> Face {
    let mut entries: Vec<_> = face
        .0
        .iter()
        .map(|tube| MarkedTube {
            vertices: permute_mask(tube.vertices, permutation),
            mark: tube.mark,
        })
        .collect();
    entries.sort();
    Face(entries)
}

fn main() {
    let trees = spanning_trees();
    assert_eq!(trees.len(), 12);
    let full = Graph(0b11_1111);
    let mut graph_masks = BTreeSet::from([full.0]);
    for tree in &trees {
        graph_masks.insert(tree.0);
        for slot in 0..6 {
            if tree.0 & (1 << slot) == 0 {
                graph_masks.insert(tree.0 | (1 << slot));
            }
        }
    }
    let mut posets = BTreeMap::new();
    let mut face_vector_distribution: BTreeMap<Vec<usize>, usize> = BTreeMap::new();
    for mask in graph_masks {
        let poset = Poset::new(Graph(mask));
        let vector: Vec<_> = (0..=N)
            .map(|codimension| {
                poset
                    .faces
                    .iter()
                    .filter(|face| face.codimension() == codimension)
                    .count()
            })
            .collect();
        println!(
            "POSET graph={mask:06b} faces={} codim={vector:?}",
            poset.faces.len()
        );
        *face_vector_distribution.entry(vector).or_default() += 1;
        posets.insert(mask, poset);
    }
    assert_eq!(
        face_vector_distribution,
        BTreeMap::from([
            (vec![1, 46, 313, 788, 841, 322], 6),
            (vec![1, 48, 338, 870, 942, 364], 6),
            (vec![1, 52, 396, 1064, 1180, 462], 6),
            (vec![1, 57, 463, 1289, 1459, 578], 1),
        ])
    );

    // Test every one-edge inclusion occurring in every presentation.
    let mut totals: BTreeMap<&str, MapAudit> = BTreeMap::new();
    let mut map_values: HashMap<(Rule, u8, u8), Vec<Option<usize>>> = HashMap::new();
    for rule in Rule::ALL {
        for tree in &trees {
            for slot in 0..6 {
                if tree.0 & (1 << slot) != 0 {
                    continue;
                }
                let middle = Graph(tree.0 | (1 << slot));
                for (source_graph, target_graph) in [(middle, *tree), (full, middle)] {
                    let key = (rule, source_graph.0, target_graph.0);
                    if map_values.contains_key(&key) {
                        continue;
                    }
                    let (audit, values) =
                        audit_map(rule, &posets[&source_graph.0], &posets[&target_graph.0]);
                    let total = totals.entry(rule.name()).or_default();
                    total.sources += audit.sources;
                    total.undefined += audit.undefined;
                    total.order_failures += audit.order_failures;
                    total.dimension_failures += audit.dimension_failures;
                    total.missed_targets += audit.missed_targets;
                    merge_witness(&mut total.first_undefined, audit.first_undefined);
                    merge_witness(&mut total.first_order_failure, audit.first_order_failure);
                    merge_witness(
                        &mut total.first_dimension_failure,
                        audit.first_dimension_failure,
                    );
                    merge_witness(&mut total.first_missed, audit.first_missed);
                    map_values.insert(key, values);
                }
            }
        }
    }

    // Full S_2 x D_3 covariance: interchange the two central vertices and
    // apply every rotation/reflection of the three roads.
    let mut symmetries = Vec::new();
    for swap_left in [false, true] {
        for road_map in [
            [0, 1, 2],
            [1, 2, 0],
            [2, 0, 1],
            [0, 2, 1],
            [2, 1, 0],
            [1, 0, 2],
        ] {
            symmetries.push([
                usize::from(swap_left),
                usize::from(!swap_left),
                2 + road_map[0],
                2 + road_map[1],
                2 + road_map[2],
            ]);
        }
    }
    assert_eq!(symmetries.len(), 12);
    for rule in Rule::ALL {
        let mut failures = 0;
        let inclusions: BTreeSet<_> = map_values
            .keys()
            .filter(|(candidate, _, _)| *candidate == rule)
            .map(|(_, source, target)| (*source, *target))
            .collect();
        assert_eq!(inclusions.len(), 30);
        for (source_mask, target_mask) in inclusions {
            let source_graph = Graph(source_mask);
            let target_graph = Graph(target_mask);
            for &permutation in &symmetries {
                let ps = permute_graph(source_graph, permutation);
                let pt = permute_graph(target_graph, permutation);
                for source_face in &posets[&source_graph.0].faces {
                    let left = compare_face(rule, target_graph, source_face)
                        .map(|face| permute_face(&face, permutation));
                    let right = compare_face(rule, pt, &permute_face(source_face, permutation));
                    if left != right {
                        failures += 1;
                    }
                }
                assert_eq!(ps.0.count_ones(), source_graph.0.count_ones());
            }
        }
        totals.get_mut(rule.name()).unwrap().covariance_failures = failures;
    }

    // Compare the two composite carriers J(K23) -> J(T+e/f) -> J(T).
    let mut factorization: BTreeMap<&str, (usize, usize, usize, Option<String>)> = BTreeMap::new();
    for rule in Rule::ALL {
        let mut compared = 0;
        let mut failures = 0;
        let mut direct_failures = 0;
        let mut witness = None;
        for tree in &trees {
            let missing: Vec<_> = (0..6).filter(|&slot| tree.0 & (1 << slot) == 0).collect();
            let middle_e = Graph(tree.0 | (1 << missing[0]));
            let middle_f = Graph(tree.0 | (1 << missing[1]));
            for face in &posets[&full.0].faces {
                let e_then_f = compare_face(rule, middle_e, face)
                    .and_then(|middle| compare_face(rule, *tree, &middle));
                let f_then_e = compare_face(rule, middle_f, face)
                    .and_then(|middle| compare_face(rule, *tree, &middle));
                if let (Some(left), Some(right)) = (&e_then_f, &f_then_e) {
                    compared += 1;
                    if left != right {
                        failures += 1;
                        if witness.is_none() {
                            witness = Some(format!(
                                "tree={:06b}, source={}, e/f={}, f/e={}",
                                tree.0,
                                face_name(face),
                                face_name(left),
                                face_name(right)
                            ));
                        }
                    }
                    let direct = compare_face(rule, *tree, face);
                    if direct.as_ref() != Some(left) {
                        direct_failures += 1;
                        if witness.is_none() {
                            witness = Some(format!(
                                "tree={:06b}, source={}, composite={}, direct={}",
                                tree.0,
                                face_name(face),
                                face_name(left),
                                direct
                                    .as_ref()
                                    .map(face_name)
                                    .unwrap_or_else(|| "undefined".to_owned())
                            ));
                        }
                    }
                }
            }
        }
        factorization.insert(rule.name(), (compared, failures, direct_failures, witness));
    }

    // Separate the ordinary graph-associahedral component carrier from its
    // marked graph-multiplihedral extension.  For unmarked tubings, adding a
    // source tube only adds its target components, so order preservation is
    // immediate from set inclusion; validity, skeleton dimension,
    // surjectivity, and two-edge functoriality are audited here.
    let mut unmarked = UnmarkedAudit::default();
    let mut seen_unmarked = BTreeSet::new();
    for tree in &trees {
        let missing: Vec<_> = (0..6).filter(|&slot| tree.0 & (1 << slot) == 0).collect();
        for &slot in &missing {
            let middle = Graph(tree.0 | (1 << slot));
            for (source, target) in [(middle, *tree), (full, middle)] {
                if seen_unmarked.insert((source.0, target.0)) {
                    audit_unmarked_inclusion(source, target, &mut unmarked);
                }
            }
        }
        let middle_e = Graph(tree.0 | (1 << missing[0]));
        let middle_f = Graph(tree.0 | (1 << missing[1]));
        for tubing in enumerate_unmarked_tubings(full) {
            let direct = unmarked_component_image(*tree, &tubing);
            let e_then_f =
                unmarked_component_image(*tree, &unmarked_component_image(middle_e, &tubing));
            let f_then_e =
                unmarked_component_image(*tree, &unmarked_component_image(middle_f, &tubing));
            if direct != e_then_f || direct != f_then_e {
                unmarked.path_failures += 1;
            }
        }
    }
    assert_eq!(seen_unmarked.len(), 30);
    assert_eq!(unmarked.invalid, 0);
    assert_eq!(unmarked.dimension_failures, 0);
    assert_eq!(unmarked.missed_targets, 0);
    assert_eq!(unmarked.path_failures, 0);

    println!("\nONE-EDGE MAP AUDITS (deduplicated graph inclusions)");
    for rule in Rule::ALL {
        let audit = &totals[rule.name()];
        println!(
            "  {:27} sources={} undefined={} order_failures={} dimension_failures={} missed_targets={} covariance_failures={}",
            rule.name(),
            audit.sources,
            audit.undefined,
            audit.order_failures,
            audit.dimension_failures,
            audit.missed_targets,
            audit.covariance_failures,
        );
        if let Some(witness) = &audit.first_undefined {
            println!("    undefined witness: {}", witness.text);
        }
        if let Some(witness) = &audit.first_order_failure {
            println!("    order witness: {}", witness.text);
        }
        if let Some(witness) = &audit.first_dimension_failure {
            println!("    dimension witness: {}", witness.text);
        }
        if let Some(witness) = &audit.first_missed {
            println!("    surjectivity witness: {}", witness.text);
        }
    }

    println!("\nTWO-EDGE FACTORIZATION AUDITS");
    for rule in Rule::ALL {
        let (compared, failures, direct_failures, witness) = &factorization[rule.name()];
        println!(
            "  {:27} jointly_defined={} path_failures={} direct_failures={}",
            rule.name(),
            compared,
            failures,
            direct_failures
        );
        if let Some(witness) = witness {
            println!("    witness: {witness}");
        }
    }

    println!("\nUNMARKED GRAPH-ASSOCIAHEDRAL BASELINE");
    println!(
        "  inclusions={} sources={} invalid={} dimension_failures={} missed_targets={} path_failures={}",
        seen_unmarked.len(),
        unmarked.sources,
        unmarked.invalid,
        unmarked.dimension_failures,
        unmarked.missed_targets,
        unmarked.path_failures,
    );

    // Both missing-edge endpoint pairs fail compatibility in the final graph:
    // they either intersect or are disjoint adjacent tubes.
    let mut intersecting = 0;
    let mut adjacent = 0;
    for tree in &trees {
        let missing: Vec<_> = (0..6).filter(|&slot| tree.0 & (1 << slot) == 0).collect();
        let edge_tubes: Vec<_> = missing
            .iter()
            .map(|&slot| {
                let (a, b) = endpoints(slot);
                (1 << a) | (1 << b)
            })
            .collect();
        assert!(!unmarked_compatible(full, edge_tubes[0], edge_tubes[1]));
        if edge_tubes[0] & edge_tubes[1] != 0 {
            intersecting += 1;
        } else {
            adjacent += 1;
        }
    }
    assert_eq!((intersecting, adjacent), (6, 6));

    // Hard certificate assertions for the successful rule.  The equivalent
    // thin-priority formulation is not an independent choice on valid marked
    // tubings: compatibility forces every innermost contributor to be thin
    // exactly when any contributor is thin.
    for rule in [Rule::ComponentsInnermost, Rule::ComponentsThinPriority] {
        let audit = &totals[rule.name()];
        assert_eq!(audit.sources, 98_802);
        assert_eq!(audit.undefined, 0);
        assert_eq!(audit.order_failures, 0);
        assert_eq!(audit.dimension_failures, 0);
        assert_eq!(audit.missed_targets, 0);
        assert_eq!(audit.covariance_failures, 0);
        let (jointly_defined, path_failures, direct_failures, _) = &factorization[rule.name()];
        assert_eq!(*jointly_defined, 46_164);
        assert_eq!(*path_failures, 0);
        assert_eq!(*direct_failures, 0);
    }
    for ((_rule, source, target), inner_values) in map_values
        .iter()
        .filter(|((rule, _, _), _)| *rule == Rule::ComponentsInnermost)
    {
        assert_eq!(
            inner_values,
            &map_values[&(Rule::ComponentsThinPriority, *source, *target)]
        );
    }
    assert!(totals[Rule::Forget.name()].order_failures > 0);
    assert!(totals[Rule::Forget.name()].missed_targets > 0);

    println!("\nVERDICT INPUTS");
    println!("  presentations=12 intersecting=6 adjacent=6");
    println!("  component/innermost is a total dimension-nonincreasing, order-preserving, face-surjective cellular carrier");
    println!("  it is S2 x D3 covariant and equals both two-edge composites and the direct component carrier");
    println!("  the unmarked component carrier is the graph-associahedral baseline; the innermost-mark lift is the separately audited graph-multiplihedral statement");
    println!("  forget-only and the outermost/thick/broken alternatives are falsified on the marked face poset");
}
