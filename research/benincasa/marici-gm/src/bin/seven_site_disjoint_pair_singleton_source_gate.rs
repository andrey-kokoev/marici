use serde_json::json;
use std::{
    collections::{BTreeMap, BTreeSet},
    fs,
};

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct Rat {
    n: i128,
    d: i128,
}

fn gcd(mut left: i128, mut right: i128) -> i128 {
    while right != 0 {
        let remainder = left % right;
        left = right;
        right = remainder;
    }
    left.abs()
}

impl Rat {
    fn new(mut n: i128, mut d: i128) -> Self {
        if n == 0 {
            return Self { n: 0, d: 1 };
        }
        if d < 0 {
            n = -n;
            d = -d;
        }
        let divisor = gcd(n.abs(), d);
        Self {
            n: n / divisor,
            d: d / divisor,
        }
    }
    fn add(self, other: Self) -> Self {
        Self::new(self.n * other.d + other.n * self.d, self.d * other.d)
    }
    fn multiply(self, other: Self) -> Self {
        Self::new(self.n * other.n, self.d * other.d)
    }
    fn inverse(self) -> Self {
        Self::new(self.d, self.n)
    }
    fn negate(self) -> Self {
        Self::new(-self.n, self.d)
    }
    fn display(self) -> String {
        if self.d == 1 {
            self.n.to_string()
        } else {
            format!("{}/{}", self.n, self.d)
        }
    }
}

fn exact_row_relation(labels: &[String], facets: &BTreeMap<String, Vec<i64>>) -> Vec<String> {
    let rows = facets[&labels[0]].len();
    let columns = labels.len();
    let mut matrix = (0..rows)
        .map(|row| {
            labels
                .iter()
                .map(|label| Rat::new(facets[label][row] as i128, 1))
                .collect::<Vec<_>>()
        })
        .collect::<Vec<_>>();
    let mut pivot_row = 0usize;
    let mut pivots = Vec::new();
    for column in 0..columns {
        let Some(found) = (pivot_row..rows).find(|row| matrix[*row][column].n != 0) else {
            continue;
        };
        matrix.swap(pivot_row, found);
        let inverse = matrix[pivot_row][column].inverse();
        for entry in column..columns {
            matrix[pivot_row][entry] = matrix[pivot_row][entry].multiply(inverse);
        }
        for row in 0..rows {
            if row == pivot_row || matrix[row][column].n == 0 {
                continue;
            }
            let scale = matrix[row][column].negate();
            for entry in column..columns {
                matrix[row][entry] =
                    matrix[row][entry].add(matrix[pivot_row][entry].multiply(scale));
            }
        }
        pivots.push(column);
        pivot_row += 1;
        if pivot_row == rows {
            break;
        }
    }
    let free = (0..columns)
        .find(|column| !pivots.contains(column))
        .unwrap();
    let mut relation = vec![Rat::new(0, 1); columns];
    relation[free] = Rat::new(1, 1);
    for (row, pivot) in pivots.iter().enumerate() {
        relation[*pivot] = matrix[row][free].negate();
    }
    relation.into_iter().map(Rat::display).collect()
}

fn rank(mut matrix: Vec<Vec<i64>>) -> usize {
    matrix.retain(|row| row.iter().any(|entry| *entry != 0));
    if matrix.is_empty() {
        return 0;
    }
    let columns = matrix[0].len();
    let mut row = 0;
    for column in 0..columns {
        let Some(pivot) = (row..matrix.len()).find(|index| matrix[*index][column] != 0) else {
            continue;
        };
        matrix.swap(row, pivot);
        for target in row + 1..matrix.len() {
            let x = matrix[target][column];
            if x == 0 {
                continue;
            }
            let y = matrix[row][column];
            for index in column..columns {
                matrix[target][index] = y * matrix[target][index] - x * matrix[row][index];
            }
        }
        row += 1;
    }
    row
}

fn label(sites: &BTreeSet<usize>) -> String {
    format!(
        "g_{}",
        sites
            .iter()
            .map(|site| (site + 1).to_string())
            .collect::<String>()
    )
}

fn rotate(label: &str, shift: usize, n: usize) -> String {
    let mut sites = label
        .strip_prefix("g_")
        .unwrap()
        .chars()
        .map(|character| (character.to_digit(10).unwrap() as usize - 1 + shift) % n)
        .collect::<Vec<_>>();
    sites.sort();
    format!(
        "g_{}",
        sites
            .iter()
            .map(|site| (site + 1).to_string())
            .collect::<String>()
    )
}

fn permutation_sign(source_order: &[String], canonical_order: &[String]) -> i64 {
    let permutation = source_order
        .iter()
        .map(|label| {
            canonical_order
                .iter()
                .position(|candidate| candidate == label)
                .unwrap()
        })
        .collect::<Vec<_>>();
    let inversions = (0..permutation.len())
        .flat_map(|left| ((left + 1)..permutation.len()).map(move |right| (left, right)))
        .filter(|(left, right)| permutation[*left] > permutation[*right])
        .count();
    if inversions % 2 == 0 {
        1
    } else {
        -1
    }
}

fn main() {
    const N: usize = 7;
    let mut vertices = Vec::new();
    for site in 0..N {
        let next = (site + 1) % N;
        for (left, right, edge) in [(1, 1, -1), (1, -1, 1), (-1, 1, 1)] {
            let mut vertex = vec![0; 2 * N];
            vertex[site] = left;
            vertex[next] = right;
            vertex[N + site] = edge;
            vertices.push(vertex);
        }
    }

    let mut facets = BTreeMap::<String, Vec<i64>>::new();
    for length in 1..N {
        for start in 0..N {
            let sites = (0..length)
                .map(|offset| (start + offset) % N)
                .collect::<BTreeSet<_>>();
            let mut facet = vec![0; 2 * N];
            for site in &sites {
                facet[*site] = 1;
            }
            for edge in 0..N {
                if sites.contains(&edge) != sites.contains(&((edge + 1) % N)) {
                    facet[N + edge] = 1;
                }
            }
            facets.insert(label(&sites), facet);
        }
    }
    for edge in 0..N {
        let mut facet = vec![1; N];
        facet.extend(vec![0; N]);
        facet[N + edge] = 2;
        facets.insert(
            format!("G_minus_e{}{}", edge + 1, (edge + 1) % N + 1),
            facet,
        );
    }
    facets.insert(
        "G".into(),
        vec![1; N].into_iter().chain(vec![0; N]).collect(),
    );

    let common = (0..N)
        .map(|site| format!("g_{}", site + 1))
        .chain(std::iter::once("G".into()))
        .collect::<BTreeSet<_>>();
    let active = ["g_12", "g_34", "g_56", "g_7"];
    let remaining = facets
        .keys()
        .filter(|name| !common.contains(*name) && !active.contains(&name.as_str()))
        .cloned()
        .collect::<Vec<_>>();

    let active_zero_vertices = vertices
        .iter()
        .filter(|vertex| {
            active.iter().all(|name| {
                facets[*name]
                    .iter()
                    .zip(vertex.iter())
                    .map(|(a, b)| a * b)
                    .sum::<i64>()
                    == 0
            })
        })
        .collect::<Vec<_>>();
    let active_affine_rank = if active_zero_vertices.is_empty() {
        0
    } else {
        let base = active_zero_vertices[0];
        rank(
            active_zero_vertices
                .iter()
                .skip(1)
                .map(|vertex| vertex.iter().zip(base.iter()).map(|(x, y)| x - y).collect())
                .collect(),
        )
    };
    let common_active_names = common
        .iter()
        .cloned()
        .chain(active.iter().map(|name| name.to_string()))
        .collect::<Vec<_>>();
    let common_active_rank = rank(
        common_active_names
            .iter()
            .map(|name| facets[name].clone())
            .collect(),
    );

    let mut completions = Vec::new();
    let mut completion_census = BTreeMap::<String, usize>::new();
    let mut maximum_affine_rank = 0usize;
    let mut maximum_denominator_rank = 0usize;
    let mut affine_rank_seven_near_misses = Vec::new();
    let mut affine_rank_seven_label_sets = Vec::new();
    let mut denominator_rank_fourteen_near_misses = Vec::new();
    for left in 0..remaining.len() {
        for middle in left + 1..remaining.len() {
            for right in middle + 1..remaining.len() {
                let names = active
                    .iter()
                    .map(|name| name.to_string())
                    .chain([
                        remaining[left].clone(),
                        remaining[middle].clone(),
                        remaining[right].clone(),
                    ])
                    .collect::<Vec<_>>();
                let zeros = vertices
                    .iter()
                    .filter(|vertex| {
                        names.iter().all(|name| {
                            facets[name]
                                .iter()
                                .zip(vertex.iter())
                                .map(|(a, b)| a * b)
                                .sum::<i64>()
                                == 0
                        })
                    })
                    .collect::<Vec<_>>();
                if zeros.is_empty() {
                    *completion_census
                        .entry("empty_zero_set".into())
                        .or_default() += 1;
                    continue;
                }
                let base = zeros[0];
                let affine_rank = rank(
                    zeros
                        .iter()
                        .skip(1)
                        .map(|vertex| vertex.iter().zip(base.iter()).map(|(x, y)| x - y).collect())
                        .collect(),
                );
                let rows = common
                    .iter()
                    .chain(names.iter())
                    .map(|name| facets[name].clone())
                    .collect::<Vec<_>>();
                let denominator_rank = rank(rows);
                maximum_affine_rank = maximum_affine_rank.max(affine_rank);
                maximum_denominator_rank = maximum_denominator_rank.max(denominator_rank);
                let completion_labels = vec![
                    remaining[left].clone(),
                    remaining[middle].clone(),
                    remaining[right].clone(),
                ];
                if affine_rank == N {
                    affine_rank_seven_near_misses.push(json!({"labels":completion_labels.clone(),"denominator_rank":denominator_rank}));
                    affine_rank_seven_label_sets.push(completion_labels.clone());
                }
                if denominator_rank == 2 * N {
                    denominator_rank_fourteen_near_misses
                        .push(json!({"labels":completion_labels,"affine_rank":affine_rank}));
                }
                if affine_rank != N {
                    *completion_census
                        .entry(format!("affine_rank_{affine_rank}"))
                        .or_default() += 1;
                    continue;
                }
                if denominator_rank == 2 * N {
                    completions.push(vec![
                        remaining[left].clone(),
                        remaining[middle].clone(),
                        remaining[right].clone(),
                    ]);
                    *completion_census.entry("accepted".into()).or_default() += 1;
                } else {
                    *completion_census
                        .entry(format!("denominator_rank_{denominator_rank}"))
                        .or_default() += 1;
                }
            }
        }
    }

    let mut orbit = Vec::new();
    for shift in 0..N {
        let source_order = active
            .iter()
            .map(|label| rotate(label, shift, N))
            .collect::<Vec<_>>();
        let mut canonical_order = source_order.clone();
        canonical_order.sort();
        orbit.push(json!({
            "shift":shift,
            "source_order":source_order,
            "canonical_order":canonical_order,
            "source_to_canonical_orientation":permutation_sign(&source_order,&canonical_order)
        }));
    }
    let distinct_occurrences = orbit
        .iter()
        .map(|entry| entry["canonical_order"].to_string())
        .collect::<BTreeSet<_>>();
    assert_eq!(distinct_occurrences.len(), 7);

    let rank_thirteen_relations = affine_rank_seven_label_sets
        .iter()
        .map(|completion| {
            let distinct_labels = common
                .iter()
                .cloned()
                .chain(active.iter().map(|name| name.to_string()))
                .chain(completion.iter().cloned())
                .collect::<BTreeSet<_>>()
                .into_iter()
                .collect::<Vec<_>>();
            let coefficients = exact_row_relation(&distinct_labels, &facets);
            json!({"completion":completion,"ordered_distinct_denominators":distinct_labels,"relation_coefficients":coefficients})
        })
        .collect::<Vec<_>>();

    let packet = json!({
        "schema":"marici.seven_site_disjoint_pair_singleton_source_gate.v1",
        "n":N,
        "active_incidence":active,
        "source_term_denominator_count":2*N,
        "common_denominator_count":common.len(),
        "additional_completion_count_per_term":3,
        "active_face_audit":{"zero_vertex_count":active_zero_vertices.len(),"affine_rank":active_affine_rank,"common_plus_active_rank":common_active_rank},
        "completion_triple_census":completion_census,
        "maximum_completion_affine_rank":maximum_affine_rank,
        "maximum_completion_denominator_rank":maximum_denominator_rank,
        "affine_rank_seven_candidates":affine_rank_seven_near_misses,
        "denominator_rank_fourteen_candidates":denominator_rank_fourteen_near_misses,
        "affine_rank_seven_exact_relations":rank_thirteen_relations,
        "compatible_source_term_completions":completions,
        "containing_source_term_count":completions.len(),
        "gate_passes":!completions.is_empty(),
        "cyclic_orbit":orbit,
        "cyclic_orbit_size":distinct_occurrences.len(),
        "stabilizer_order":1,
        "occurrence_representation":{"group":"C7","module":"Q[C7]","character":[7,0,0,0,0,0,0]},
        "orientation_convention":"source order is transported strictly; the reported signs only compare it with lexical canonical order",
        "scope":"frozen source incidence, full rank, orbit, and orientation only; no seven-site Landau claim"
    });
    fs::write(
        "../results/seven-site-disjoint-pair-singleton-source-gate.json",
        serde_json::to_string_pretty(&packet).unwrap() + "\n",
    )
    .unwrap();
    println!(
        "{}",
        json!({"orbit_size":7,"completions":completions.len(),"gate_passes":!completions.is_empty()})
    );
}
