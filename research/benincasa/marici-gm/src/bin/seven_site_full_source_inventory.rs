use serde_json::json;
use std::{
    collections::{BTreeMap, BTreeSet},
    fs,
    sync::OnceLock,
};

const N: usize = 7;

fn prime() -> i64 {
    static PRIME: OnceLock<i64> = OnceLock::new();
    *PRIME.get_or_init(|| {
        std::env::var("PRIME")
            .ok()
            .map(|raw| raw.parse().expect("PRIME must be an integer"))
            .unwrap_or(1_000_003)
    })
}

#[derive(Clone)]
struct Facet {
    name: String,
    row: Vec<i64>,
    zero_mask: u32,
}

fn inverse_mod(mut value: i64) -> i64 {
    value = value.rem_euclid(prime());
    let mut exponent = prime() - 2;
    let mut result = 1i64;
    while exponent > 0 {
        if exponent & 1 == 1 {
            result = ((result as i128 * value as i128) % prime() as i128) as i64;
        }
        value = ((value as i128 * value as i128) % prime() as i128) as i64;
        exponent >>= 1;
    }
    result
}

fn rank_mod(mut matrix: Vec<Vec<i64>>) -> usize {
    if matrix.is_empty() {
        return 0;
    }
    let columns = matrix[0].len();
    let mut row = 0usize;
    for column in 0..columns {
        let Some(pivot) = (row..matrix.len())
            .find(|candidate| matrix[*candidate][column].rem_euclid(prime()) != 0)
        else {
            continue;
        };
        matrix.swap(row, pivot);
        let inverse = inverse_mod(matrix[row][column]);
        for entry in column..columns {
            matrix[row][entry] = ((matrix[row][entry].rem_euclid(prime()) as i128
                * inverse as i128)
                % prime() as i128) as i64;
        }
        for target in 0..matrix.len() {
            if target == row {
                continue;
            }
            let scale = matrix[target][column].rem_euclid(prime());
            if scale == 0 {
                continue;
            }
            for entry in column..columns {
                matrix[target][entry] = (matrix[target][entry]
                    - ((scale as i128 * matrix[row][entry] as i128) % prime() as i128) as i64)
                    .rem_euclid(prime());
            }
        }
        row += 1;
        if row == matrix.len() {
            break;
        }
    }
    row
}

fn rank_integer(mut matrix: Vec<Vec<i128>>) -> usize {
    matrix.retain(|row| row.iter().any(|entry| *entry != 0));
    if matrix.is_empty() {
        return 0;
    }
    let columns = matrix[0].len();
    let mut row = 0usize;
    for column in 0..columns {
        let Some(pivot) = (row..matrix.len()).find(|candidate| matrix[*candidate][column] != 0)
        else {
            continue;
        };
        matrix.swap(row, pivot);
        for target in row + 1..matrix.len() {
            if matrix[target][column] == 0 {
                continue;
            }
            let left = matrix[row][column];
            let right = matrix[target][column];
            for entry in column..columns {
                matrix[target][entry] = left * matrix[target][entry] - right * matrix[row][entry];
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

fn parse_region(name: &str) -> Option<BTreeSet<usize>> {
    name.strip_prefix("g_").map(|digits| {
        digits
            .chars()
            .map(|character| character.to_digit(10).unwrap() as usize - 1)
            .collect()
    })
}

fn rotate_label(name: &str, shift: usize) -> String {
    if let Some(region) = parse_region(name) {
        return label(&region.iter().map(|site| (site + shift) % N).collect());
    }
    if let Some(edge) = name.strip_prefix("G_minus_e") {
        let digits = edge
            .chars()
            .map(|character| character.to_digit(10).unwrap() as usize - 1)
            .collect::<Vec<_>>();
        return format!(
            "G_minus_e{}{}",
            (digits[0] + shift) % N + 1,
            (digits[1] + shift) % N + 1
        );
    }
    name.to_string()
}

fn canonical_orbit(term: &[String]) -> (String, usize) {
    let rotations = (0..N)
        .map(|shift| {
            let mut rotated = term
                .iter()
                .map(|name| rotate_label(name, shift))
                .collect::<Vec<_>>();
            rotated.sort();
            rotated.join("|")
        })
        .collect::<Vec<_>>();
    let canonical = rotations.iter().min().unwrap().clone();
    let stabilizer = rotations
        .iter()
        .filter(|rotation| **rotation == rotations[0])
        .count();
    (canonical, stabilizer)
}

fn strict_nesting_depth(term: &[String]) -> usize {
    let regions = term
        .iter()
        .filter_map(|name| parse_region(name))
        .collect::<Vec<_>>();
    fn depth_from(index: usize, regions: &[BTreeSet<usize>], memo: &mut [usize]) -> usize {
        if memo[index] != 0 {
            return memo[index];
        }
        let depth = 1
            + (0..regions.len())
                .filter(|other| {
                    regions[index].len() < regions[*other].len()
                        && regions[index].is_subset(&regions[*other])
                })
                .map(|other| depth_from(other, regions, memo))
                .max()
                .unwrap_or(0);
        memo[index] = depth;
        depth
    }
    let mut memo = vec![0; regions.len()];
    (0..regions.len())
        .map(|index| depth_from(index, &regions, &mut memo))
        .max()
        .unwrap_or(0)
}

fn separated_region_pairs(term: &[String]) -> usize {
    let regions = term
        .iter()
        .filter_map(|name| parse_region(name))
        .collect::<Vec<_>>();
    (0..regions.len())
        .flat_map(|left| ((left + 1)..regions.len()).map(move |right| (left, right)))
        .filter(|(left, right)| {
            regions[*left].is_disjoint(&regions[*right])
                && !regions[*left].iter().any(|site| {
                    regions[*right].contains(&((site + 1) % N))
                        || regions[*right].contains(&((site + N - 1) % N))
                })
        })
        .count()
}

fn affine_rank(mask: u32, vertices: &[Vec<i64>]) -> usize {
    let selected = (0..vertices.len())
        .filter(|index| mask & (1u32 << index) != 0)
        .collect::<Vec<_>>();
    if selected.len() <= 1 {
        return 0;
    }
    let base = &vertices[selected[0]];
    rank_mod(
        selected
            .iter()
            .skip(1)
            .map(|index| {
                vertices[*index]
                    .iter()
                    .zip(base.iter())
                    .map(|(left, right)| left - right)
                    .collect()
            })
            .collect(),
    )
}

fn enumerate_terms(
    facets: &[Facet],
    vertices: &[Vec<i64>],
    common_rows: &[Vec<i64>],
    start: usize,
    chosen: &mut Vec<usize>,
    zero_mask: u32,
    terms: &mut Vec<Vec<String>>,
) {
    if chosen.len() == 6 {
        if affine_rank(zero_mask, vertices) != N {
            return;
        }
        let rows = common_rows
            .iter()
            .cloned()
            .chain(chosen.iter().map(|index| facets[*index].row.clone()))
            .collect::<Vec<_>>();
        if rank_mod(rows) == 2 * N {
            terms.push(
                chosen
                    .iter()
                    .map(|index| facets[*index].name.clone())
                    .collect(),
            );
        }
        return;
    }
    let needed = 6 - chosen.len();
    if facets.len() - start < needed {
        return;
    }
    for index in start..=facets.len() - needed {
        let next_mask = zero_mask & facets[index].zero_mask;
        if next_mask == 0 {
            continue;
        }
        chosen.push(index);
        enumerate_terms(
            facets,
            vertices,
            common_rows,
            index + 1,
            chosen,
            next_mask,
            terms,
        );
        chosen.pop();
    }
}

fn main() {
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

    let mut facet_rows = BTreeMap::<String, Vec<i64>>::new();
    for length in 1..N {
        for start in 0..N {
            let sites = (0..length)
                .map(|offset| (start + offset) % N)
                .collect::<BTreeSet<_>>();
            let mut row = vec![0; 2 * N];
            for site in &sites {
                row[*site] = 1;
            }
            for edge in 0..N {
                if sites.contains(&edge) != sites.contains(&((edge + 1) % N)) {
                    row[N + edge] = 1;
                }
            }
            facet_rows.insert(label(&sites), row);
        }
    }
    for edge in 0..N {
        let mut row = vec![1; N];
        row.extend(vec![0; N]);
        row[N + edge] = 2;
        facet_rows.insert(format!("G_minus_e{}{}", edge + 1, (edge + 1) % N + 1), row);
    }
    facet_rows.insert(
        "G".into(),
        vec![1; N].into_iter().chain(vec![0; N]).collect(),
    );

    let common_names = (0..N)
        .map(|site| format!("g_{}", site + 1))
        .chain(std::iter::once("G".into()))
        .collect::<BTreeSet<_>>();
    let common_rows = common_names
        .iter()
        .map(|name| facet_rows[name].clone())
        .collect::<Vec<_>>();
    assert_eq!(rank_mod(common_rows.clone()), common_names.len());

    let facets = facet_rows
        .iter()
        .filter(|(name, _)| !common_names.contains(*name))
        .map(|(name, row)| {
            let zero_mask = vertices
                .iter()
                .enumerate()
                .filter(|(_, vertex)| {
                    row.iter()
                        .zip(vertex.iter())
                        .map(|(left, right)| left * right)
                        .sum::<i64>()
                        == 0
                })
                .fold(0u32, |mask, (index, _)| mask | (1u32 << index));
            Facet {
                name: name.clone(),
                row: row.clone(),
                zero_mask,
            }
        })
        .collect::<Vec<_>>();

    let all_vertices_mask = (1u32 << vertices.len()) - 1;
    let mut terms = Vec::new();
    enumerate_terms(
        &facets,
        &vertices,
        &common_rows,
        0,
        &mut Vec::new(),
        all_vertices_mask,
        &mut terms,
    );
    assert!(!terms.is_empty());

    let mut orbits = BTreeMap::<String, (Vec<String>, usize, usize)>::new();
    for term in &terms {
        let (key, stabilizer) = canonical_orbit(term);
        let entry = orbits.entry(key).or_insert((term.clone(), stabilizer, 0));
        entry.2 += 1;
    }

    let mut orbit_packets = orbits
        .iter()
        .map(|(key, (term, stabilizer, multiplicity))| {
            let wall_count = term.len();
            let nesting_depth = strict_nesting_depth(term);
            let separation = separated_region_pairs(term);
            let orbit_size = N / stabilizer;
            (
                (wall_count, nesting_depth, separation, orbit_size),
                json!({
                    "canonical_key":key,
                    "representative":term,
                    "stabilizer_order":stabilizer,
                    "orbit_size":orbit_size,
                    "enumerated_source_multiplicity":multiplicity,
                    "score":{"wall_count":wall_count,"nesting_depth":nesting_depth,"separated_region_pairs":separation,"labelled_orbit_size":orbit_size}
                }),
            )
        })
        .collect::<Vec<_>>();
    orbit_packets.sort_by(|left, right| right.0.cmp(&left.0));
    let top_score = orbit_packets[0].0;
    let top = orbit_packets
        .iter()
        .filter(|(score, _)| *score == top_score)
        .map(|(_, packet)| packet.clone())
        .collect::<Vec<_>>();
    let selected = top
        .iter()
        .min_by_key(|packet| packet["canonical_key"].as_str().unwrap())
        .unwrap()
        .clone();
    let selected_labels = selected["representative"]
        .as_array()
        .unwrap()
        .iter()
        .map(|value| value.as_str().unwrap().to_string())
        .collect::<Vec<_>>();
    let selected_facets = selected_labels
        .iter()
        .map(|name| facets.iter().find(|facet| facet.name == *name).unwrap())
        .collect::<Vec<_>>();
    let selected_zero_mask = selected_facets
        .iter()
        .fold(all_vertices_mask, |mask, facet| mask & facet.zero_mask);
    let selected_rows = common_rows
        .iter()
        .cloned()
        .chain(selected_facets.iter().map(|facet| facet.row.clone()))
        .collect::<Vec<_>>();
    assert_eq!(affine_rank(selected_zero_mask, &vertices), N);
    assert_eq!(
        rank_integer(
            selected_rows
                .iter()
                .map(|row| row.iter().map(|entry| *entry as i128).collect())
                .collect()
        ),
        2 * N
    );
    let output = std::env::var("OUTPUT")
        .unwrap_or_else(|_| "../results/seven-site-full-source-inventory.json".into());

    let packet = json!({
        "schema":"marici.seven_site_full_source_inventory.v1",
        "prime":prime(),
        "facet_count":facet_rows.len(),
        "noncommon_facet_count":facets.len(),
        "source_term_count":terms.len(),
        "cyclic_orbit_count":orbits.len(),
        "selection_rule":"lexicographic maximum of (wall_count,nesting_depth,separated_nonadjacent_region_pairs,labelled_orbit_size); ties are resolved by lexicographically least canonical labelled key without claiming greater complexity",
        "top_score":{"wall_count":top_score.0,"nesting_depth":top_score.1,"separated_region_pairs":top_score.2,"labelled_orbit_size":top_score.3},
        "top_tie_count":top.len(),
        "top_orbits":top,
        "selected_orbit":selected,
        "selected_exact_certificate":{"integer_denominator_rank":14,"affine_face_rank":7},
        "all_orbits":orbit_packets.iter().map(|(_,packet)|packet.clone()).collect::<Vec<_>>(),
        "complexity_selection_status":if orbit_packets.iter().filter(|(score,_)|*score==top_score).count()==1{"unique"}else{"tied"},
        "attack_selection_status":"unique after neutral canonical tie-break",
        "scope":"complete frozen seven-site maximal source-term inventory and pre-geometric orbit ranking"
    });
    fs::write(
        output,
        serde_json::to_string_pretty(&packet).unwrap() + "\n",
    )
    .unwrap();
    println!(
        "{}",
        json!({"terms":terms.len(),"orbits":orbits.len(),"top_score":top_score,"top_ties":top.len()})
    );
}
