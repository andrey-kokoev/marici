//! Exact weighted-cellular certificate for the geometric D=03 relation
//! target supplied by the full six-point associahedron.
//!
//! A cell is a noncrossing dissection S of a labelled hexagon.  Its weighted
//! boundary is
//!
//!   d[S] = sum_{a addable} (-1)^#{s in S | s<a} X_a [S union {a}].
//!
//! The sign is the ordered normal-orientation sign.  The two orders of adding
//! compatible diagonals cancel, so d^2=0.  Multiplying [S] by the product of
//! its diagonal variables conjugates this differential to the ordinary
//! cellular boundary.  Hence the reciprocal vertex functional
//!
//!   lambda(T) = 1 / product_{a in T} X_a
//!
//! is the unique endpoint-normalized H^0 class.
//!
//! The three long-diagonal facets are disjoint squares.  Restricting lambda
//! and removing their common physical X_D/[dX_D] factor gives precisely the
//! three rotated entry-97 occurrence weights.  The other six facets are the
//! short-diagonal pentagons.  Relative to their union, every edge and vertex
//! vanishes and the only surviving cellular differential is
//!
//!   C3=Z<K_rel> -> C2=Z<T0,T1,T2>,  d K_rel=T0+T1+T2.
//!
//! Thus the target relation object and its differential are relative
//! associahedral geometry, not a formal cone.  This certificate does not
//! construct the excess Beck--Chevalley maps from the two conductor normal-
//! link source triangles; that separate obstruction is audited by
//! check_d03_three_pair_pc_extension.rs.

use std::collections::{BTreeMap, BTreeSet, VecDeque};

const N: u8 = 6;
const DIMENSION: usize = 3;

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct Diagonal(u8, u8);

type Dissection = BTreeSet<Diagonal>;

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct Laurent([i8; 9]);

impl Laurent {
    fn one() -> Self {
        Self([0; 9])
    }

    fn variable(index: usize) -> Self {
        let mut result = [0; 9];
        result[index] = 1;
        Self(result)
    }

    fn multiply(self, other: Self) -> Self {
        Self(std::array::from_fn(|index| self.0[index] + other.0[index]))
    }

    fn inverse(self) -> Self {
        Self(self.0.map(|entry| -entry))
    }
}

fn diagonal(first: u8, second: u8) -> Diagonal {
    if first < second {
        Diagonal(first, second)
    } else {
        Diagonal(second, first)
    }
}

fn boundary_edge(value: Diagonal) -> bool {
    value.1 - value.0 == 1 || value == Diagonal(0, N - 1)
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
            if !boundary_edge(value) {
                result.push(value);
            }
        }
    }
    result
}

fn short_index(value: Diagonal) -> Option<usize> {
    (0..6).find(|&index| diagonal(index as u8, (index as u8 + 2) % N) == value)
}

fn long_index(value: Diagonal) -> Option<usize> {
    (0..3).find(|&index| diagonal(index as u8, index as u8 + 3) == value)
}

fn variable_index(value: Diagonal) -> usize {
    if let Some(index) = short_index(value) {
        index
    } else {
        6 + long_index(value).expect("every hexagon diagonal is short or long")
    }
}

fn noncrossing(value: &Dissection) -> bool {
    value.iter().enumerate().all(|(position, first)| {
        value
            .iter()
            .skip(position + 1)
            .all(|second| !crosses(*first, *second))
    })
}

fn dissections() -> Vec<Vec<Dissection>> {
    let diagonals = all_diagonals();
    assert_eq!(diagonals.len(), 9);
    let mut by_size = vec![Vec::new(); DIMENSION + 1];
    for subset in 0_u16..(1_u16 << diagonals.len()) {
        if subset.count_ones() as usize > DIMENSION {
            continue;
        }
        let current: Dissection = diagonals
            .iter()
            .enumerate()
            .filter(|(index, _)| subset & (1 << index) != 0)
            .map(|(_, &value)| value)
            .collect();
        if noncrossing(&current) {
            by_size[current.len()].push(current);
        }
    }
    for values in &mut by_size {
        values.sort();
    }
    assert_eq!(
        by_size.iter().map(Vec::len).collect::<Vec<_>>(),
        [1, 9, 21, 14]
    );
    by_size
}

fn addable(dissection: &Dissection, value: Diagonal) -> bool {
    !dissection.contains(&value)
        && dissection.len() < DIMENSION
        && dissection.iter().all(|&present| !crosses(present, value))
}

fn raw_incidence_sign(dissection: &Dissection, added: Diagonal) -> i64 {
    if dissection.iter().filter(|&&value| value < added).count() % 2 == 0 {
        1
    } else {
        -1
    }
}

fn orientation_gauges() -> BTreeMap<Dissection, i64> {
    // The ordered-normal signs already make every codimension-two diamond
    // anticommute.  Orient the vertices coherently so that the two endpoints
    // of every one-cell have opposite signs.  This is only an orientation
    // gauge; it does not change any weighted coefficient.
    let by_size = dissections();
    let mut gauges = BTreeMap::from([(by_size[3][0].clone(), 1_i64)]);
    let mut changed = true;
    while changed {
        changed = false;
        for edge in &by_size[2] {
            let endpoints: Vec<_> = all_diagonals()
                .into_iter()
                .filter(|&value| addable(edge, value))
                .map(|value| {
                    let mut target = edge.clone();
                    target.insert(value);
                    (target, raw_incidence_sign(edge, value))
                })
                .collect();
            assert_eq!(endpoints.len(), 2);
            let relation = -endpoints[0].1 * endpoints[1].1;
            match (
                gauges.get(&endpoints[0].0).copied(),
                gauges.get(&endpoints[1].0).copied(),
            ) {
                (Some(first), Some(second)) => assert_eq!(second, relation * first),
                (Some(first), None) => {
                    gauges.insert(endpoints[1].0.clone(), relation * first);
                    changed = true;
                }
                (None, Some(second)) => {
                    gauges.insert(endpoints[0].0.clone(), relation * second);
                    changed = true;
                }
                (None, None) => {}
            }
        }
    }
    assert_eq!(gauges.len(), 14);
    gauges
}

fn incidence_sign(dissection: &Dissection, added: Diagonal) -> i64 {
    let mut target = dissection.clone();
    target.insert(added);
    let gauges = orientation_gauges();
    let source_gauge = gauges.get(dissection).copied().unwrap_or(1);
    let target_gauge = gauges.get(&target).copied().unwrap_or(1);
    raw_incidence_sign(dissection, added) * source_gauge * target_gauge
}

fn weight(dissection: &Dissection) -> Laurent {
    dissection.iter().fold(Laurent::one(), |result, &value| {
        result.multiply(Laurent::variable(variable_index(value)))
    })
}

fn weighted_boundary(dissection: &Dissection) -> BTreeMap<Dissection, (i64, Laurent)> {
    all_diagonals()
        .into_iter()
        .filter(|&value| addable(dissection, value))
        .map(|value| {
            let mut target = dissection.clone();
            target.insert(value);
            (
                target,
                (
                    incidence_sign(dissection, value),
                    Laurent::variable(variable_index(value)),
                ),
            )
        })
        .collect()
}

fn check_weighted_complex(by_size: &[Vec<Dissection>]) {
    // Every codimension-two target is reached by two addable diagonals.  The
    // Laurent monomial is the same in both orders and the ordered-normal
    // incidence signs are opposite.
    for size in 0..=1 {
        for source in &by_size[size] {
            let first_boundary = weighted_boundary(source);
            let mut square = BTreeMap::<Dissection, BTreeMap<Laurent, i64>>::new();
            for (middle, (first_sign, first_weight)) in first_boundary {
                for (target, (second_sign, second_weight)) in weighted_boundary(&middle) {
                    *square
                        .entry(target)
                        .or_default()
                        .entry(first_weight.multiply(second_weight))
                        .or_default() += first_sign * second_sign;
                }
            }
            for coefficients in square.values() {
                assert!(coefficients.values().all(|&coefficient| coefficient == 0));
            }
        }
    }

    // Multiplication by the cell weight conjugates the weighted boundary to
    // unit cellular incidence: w(S)*X_a=w(S union {a}).
    for size in 0..DIMENSION {
        for source in &by_size[size] {
            for (target, (_, coefficient)) in weighted_boundary(source) {
                assert_eq!(weight(source).multiply(coefficient), weight(&target));
            }
        }
    }

    // The reciprocal functional on raw vertex generators kills every
    // weighted edge boundary occurrence by occurrence.
    for edge in &by_size[2] {
        let endpoints = weighted_boundary(edge);
        assert_eq!(endpoints.len(), 2);
        let evaluations: Vec<_> = endpoints
            .iter()
            .map(|(vertex, (sign, coefficient))| {
                (*sign, coefficient.multiply(weight(vertex).inverse()))
            })
            .collect();
        assert_eq!(evaluations[0].1, evaluations[1].1);
        assert_eq!(evaluations[0].0 + evaluations[1].0, 0);
    }
}

fn triangulation_neighbors(
    triangulation: &Dissection,
    by_size: &[Vec<Dissection>],
) -> Vec<Dissection> {
    by_size[2]
        .iter()
        .filter(|edge| edge.is_subset(triangulation))
        .flat_map(|edge| weighted_boundary(edge).into_keys())
        .filter(|other| other != triangulation)
        .collect()
}

fn check_unique_global_augmentation(by_size: &[Vec<Dissection>]) {
    let vertices = &by_size[3];
    let mut reached = BTreeSet::new();
    let mut queue = VecDeque::from([vertices[0].clone()]);
    while let Some(current) = queue.pop_front() {
        if !reached.insert(current.clone()) {
            continue;
        }
        queue.extend(triangulation_neighbors(&current, by_size));
    }
    assert_eq!(reached.len(), 14);

    // After the canonical Laurent diagonal normalization, every edge equation
    // says that its two endpoint values agree.  Connectivity therefore makes
    // H^0 rank one, and value +1 at one normalized endpoint fixes its generator.
    let mut normalized_values = BTreeMap::from([(vertices[0].clone(), 1_i64)]);
    let mut queue = VecDeque::from([vertices[0].clone()]);
    while let Some(current) = queue.pop_front() {
        let value = normalized_values[&current];
        for neighbor in triangulation_neighbors(&current, by_size) {
            match normalized_values.get(&neighbor) {
                Some(&known) => assert_eq!(known, value),
                None => {
                    normalized_values.insert(neighbor.clone(), value);
                    queue.push_back(neighbor);
                }
            }
        }
    }
    assert_eq!(normalized_values.len(), 14);
    assert!(normalized_values.values().all(|&value| value == 1));

    // The two triangulations with no long road are the alternating central /
    // contact endpoints.  Their values are forced by the same global edge
    // equations rather than added as a free road-invisible generator.
    let zero_road: Vec<_> = vertices
        .iter()
        .filter(|triangulation| {
            triangulation
                .iter()
                .all(|&value| long_index(value).is_none())
        })
        .collect();
    assert_eq!(zero_road.len(), 2);
    let zero_road_short_indices: BTreeSet<Vec<_>> = zero_road
        .iter()
        .map(|triangulation| {
            let mut result: Vec<_> = triangulation
                .iter()
                .map(|&value| short_index(value).unwrap())
                .collect();
            result.sort();
            result
        })
        .collect();
    assert_eq!(
        zero_road_short_indices,
        BTreeSet::from([vec![0, 2, 4], vec![1, 3, 5]])
    );
    for triangulation in zero_road {
        assert_eq!(normalized_values[triangulation], 1);
        assert_eq!(
            weight(triangulation)
                .0
                .iter()
                .filter(|&&entry| entry == 1)
                .count(),
            3
        );
    }
}

fn check_three_road_restrictions(by_size: &[Vec<Dissection>]) {
    let mut all_road_vertices = BTreeSet::new();
    for road in 0..3 {
        let physical = diagonal(road as u8, road as u8 + 3);
        let vertices: Vec<_> = by_size[3]
            .iter()
            .filter(|triangulation| triangulation.contains(&physical))
            .collect();
        assert_eq!(vertices.len(), 4);
        for vertex in &vertices {
            assert!(all_road_vertices.insert((*vertex).clone()));
        }

        let left_slots = [road, (road + 1) % 6];
        let right_slots = [(road + 3) % 6, (road + 4) % 6];
        let expected: BTreeSet<(usize, usize)> = left_slots
            .into_iter()
            .flat_map(|left| right_slots.into_iter().map(move |right| (left, right)))
            .collect();
        let actual: BTreeSet<(usize, usize)> = vertices
            .iter()
            .map(|triangulation| {
                let shorts: Vec<_> = triangulation
                    .iter()
                    .filter_map(|&value| short_index(value))
                    .collect();
                assert_eq!(shorts.len(), 2);
                let left = *shorts
                    .iter()
                    .find(|value| left_slots.contains(value))
                    .unwrap();
                let right = *shorts
                    .iter()
                    .find(|value| right_slots.contains(value))
                    .unwrap();
                (left, right)
            })
            .collect();
        assert_eq!(actual, expected);

        // Raw lambda includes the common long-channel inverse.  Multiplying
        // it by X_D (and pairing [dX_D] positively) leaves entry 97's
        // 1/(x_left*x_right) at all four rotated occurrences.
        for triangulation in vertices {
            let raw_lambda = weight(triangulation).inverse();
            let stripped = raw_lambda.multiply(Laurent::variable(6 + road));
            let (left, right) = actual
                .iter()
                .copied()
                .find(|&(left, right)| {
                    triangulation.contains(&diagonal(left as u8, (left as u8 + 2) % N))
                        && triangulation.contains(&diagonal(right as u8, (right as u8 + 2) % N))
                })
                .unwrap();
            let expected_weight = Laurent::variable(left)
                .multiply(Laurent::variable(right))
                .inverse();
            assert_eq!(stripped, expected_weight);
        }
    }
    assert_eq!(all_road_vertices.len(), 12);
}

fn check_relative_relation_target(by_size: &[Vec<Dissection>]) {
    // A cell belongs to the union B_sc of the six short-diagonal pentagon
    // facets exactly when its dissection contains at least one short diagonal.
    let survives =
        |dissection: &Dissection| dissection.iter().all(|&value| short_index(value).is_none());
    let relative_ranks: Vec<_> = by_size
        .iter()
        .map(|cells| cells.iter().filter(|cell| survives(cell)).count())
        .collect();
    // Indexed by number of fixed diagonals: top, facets, edges, vertices.
    assert_eq!(relative_ranks, [1, 3, 0, 0]);

    let top = &by_size[0][0];
    let relative_boundary: Vec<_> = weighted_boundary(top)
        .into_iter()
        .filter(|(facet, _)| survives(facet))
        .collect();
    assert_eq!(relative_boundary.len(), 3);
    for (facet, (sign, coefficient)) in relative_boundary {
        let physical = *facet.iter().next().unwrap();
        let road = long_index(physical).unwrap();
        assert_eq!(sign, 1);
        assert_eq!(coefficient, Laurent::variable(6 + road));
        // In the normalized face basis X_D[F_D], every coefficient is +1.
        assert_eq!(weight(top).multiply(coefficient), weight(&facet));
    }
}

fn main() {
    let by_size = dissections();
    check_weighted_complex(&by_size);
    check_unique_global_augmentation(&by_size);
    check_three_road_restrictions(&by_size);
    check_relative_relation_target(&by_size);

    println!(
        "{}",
        concat!(
            r#"{"claim":"the full weighted six-point associahedron supplies a canonical relative PC relation target: its unique global reciprocal Laurent augmentation restricts to the three rotated entry-97 road weights, and relative to the six short-diagonal pentagon facets its normalized cellular complex is R<K_rel> -> R<T0,T1,T2> with dK_rel=T0+T1+T2","status":"proved","assumptions":["entry 38 is applied to the actual hexagon associahedron face complex with ordered normal orientations","all nine scalar diagonal variables are Laurent units for the occurrence normalization, while the six short-boundary monodromies q_j and u_j=q_j-1 remain a separate PC coefficient layer","the relative subcomplex is the union B_sc of the six short-diagonal pentagon facets"],"evidence_refs":["research/voevodsky/check_d03_relative_associahedron_pc.rs","src/ledger/20260813-38 Finite-Alpha-Prime Normal-Torus Lift and Nearby-Cycle Unit Theorem.md","src/ledger/20260814-86 Occurrence-Conjugated Core-Entry Counit and the Vanishing Residue Scalar.md","src/ledger/20260814-97 Reciprocal-Twist D03 Bivariant Road Trace.md"],"factorization_test":{"cell_census":{"top":1,"facets":9,"edges":21,"vertices":14},"weighted_differential":"PASS: d[S]=sum incidence*X_a[S+a] and d^2=0 exactly","laurent_normalization":"PASS: multiplication by prod_{a in S}X_a conjugates to ordinary cellular incidence","global_counit":"PASS: lambda(T)=(prod_{a in T}X_a)^-1 is a cocycle; connectedness makes its endpoint-normalized H^0 class unique","contact_cells":"PASS in the scalar associahedron: the all-even and all-odd zero-road triangulations have forced normalized value 1 and raw values (x0*x2*x4)^-1 and (x1*x3*x5)^-1","road_restrictions":["F03: (x0,x1) boxtimes (x3,x4)","F14: (x1,x2) boxtimes (x4,x5)","F25: (x2,x3) boxtimes (x5,x0)"],"entry97_match":"PASS: after stripping the common physical X_D/[dX_D] factor, lambda is exactly 1/(x_left*x_right) on all twelve road occurrences","relative_census":{"degree3":1,"degree2":3,"degree1":0,"degree0":0},"relation_differential":"PASS: in normalized oriented facet bases, dK_rel=T0+T1+T2","provenance":"K_rel and its three target attachments are entry-38 relative face tubes of (K6,B_sc), not an adjoined mapping-cone generator"},"counterevidence":["This target theorem does not construct the source maps from the two conductor normal-link triangles to K_rel^PC.","The full PC source-to-target lift still requires the excess-one branch/pair Beck-Chevalley maps isolated in research/voevodsky/check_d03_three_pair_pc_extension.rs.","The uniqueness statement is for the explicit scalar weighted associahedron; it does not declare away an additional contact summand in the larger full PC(J4 boxtimes J6) object."],"next_experiment":"construct the plus-sheet excess Beck-Chevalley comparison from I_+=(u1,u3,u5) to the F03 marked pair I_03=(u0,u3) and verify that its restriction is the entry-97 trace; then rotate and test the f_+ top square before treating f_-"}"#
        )
    );
}
