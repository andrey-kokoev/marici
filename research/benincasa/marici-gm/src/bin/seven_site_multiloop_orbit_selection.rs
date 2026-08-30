use serde_json::{json, Value};
use std::{collections::BTreeSet, fs};

const N: usize = 7;

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

fn parse_region(name: &str) -> Option<BTreeSet<usize>> {
    name.strip_prefix("g_").map(|digits| {
        digits
            .chars()
            .map(|character| character.to_digit(10).unwrap() as usize - 1)
            .collect()
    })
}

fn wall_row(name: &str) -> Vec<i128> {
    let mut row = vec![0; N];
    if let Some(region) = parse_region(name) {
        for edge in 0..N {
            if region.contains(&edge) != region.contains(&((edge + 1) % N)) {
                row[edge] = 1;
            }
        }
        return row;
    }
    let edge = name
        .strip_prefix("G_minus_e")
        .expect("only frozen source walls are admitted")
        .chars()
        .next()
        .unwrap()
        .to_digit(10)
        .unwrap() as usize
        - 1;
    row[edge] = 2;
    row
}

fn site_energy_coefficient(name: &str) -> i128 {
    parse_region(name)
        .map(|region| region.len() as i128)
        .unwrap_or(N as i128)
}

fn is_five_region_total_chain(labels: &[String]) -> bool {
    let regions = labels
        .iter()
        .filter_map(|label| parse_region(label))
        .collect::<Vec<_>>();
    regions.len() == 5
        && (0..regions.len()).all(|left| {
            (0..regions.len()).all(|right| {
                left == right
                    || regions[left].is_subset(&regions[right])
                    || regions[right].is_subset(&regions[left])
            })
        })
}

fn rotate_label(name: &str, shift: usize) -> String {
    if let Some(region) = parse_region(name) {
        let rotated = region
            .iter()
            .map(|site| (site + shift) % N)
            .collect::<BTreeSet<_>>();
        return format!(
            "g_{}",
            rotated
                .iter()
                .map(|site| (site + 1).to_string())
                .collect::<String>()
        );
    }
    let digits = name
        .strip_prefix("G_minus_e")
        .unwrap()
        .chars()
        .map(|character| character.to_digit(10).unwrap() as usize - 1)
        .collect::<Vec<_>>();
    format!(
        "G_minus_e{}{}",
        (digits[0] + shift) % N + 1,
        (digits[1] + shift) % N + 1
    )
}

fn sorting_sign(words: &[String]) -> i32 {
    let inversions = (0..words.len())
        .flat_map(|left| ((left + 1)..words.len()).map(move |right| (left, right)))
        .filter(|(left, right)| words[*left] > words[*right])
        .count();
    if inversions % 2 == 0 {
        1
    } else {
        -1
    }
}

fn score(packet: &Value) -> (usize, usize, usize, usize) {
    let score = &packet["score"];
    (
        score["wall_count"].as_u64().unwrap() as usize,
        score["nesting_depth"].as_u64().unwrap() as usize,
        score["separated_region_pairs"].as_u64().unwrap() as usize,
        score["labelled_orbit_size"].as_u64().unwrap() as usize,
    )
}

fn main() {
    let inventory: Value = serde_json::from_str(
        &fs::read_to_string("../results/seven-site-full-source-inventory.json").unwrap(),
    )
    .unwrap();
    let mut eligible = inventory["all_orbits"]
        .as_array()
        .unwrap()
        .iter()
        .filter_map(|packet| {
            let labels = packet["representative"]
                .as_array()
                .unwrap()
                .iter()
                .map(|label| label.as_str().unwrap().to_string())
                .collect::<Vec<_>>();
            let wall_rank = rank_integer(labels.iter().map(|label| wall_row(label)).collect());
            let augmented_rank = rank_integer(
                labels
                    .iter()
                    .map(|label| {
                        let mut row = wall_row(label);
                        row.push(site_energy_coefficient(label));
                        row
                    })
                    .collect(),
            );
            let free_signed_energies = N - wall_rank;
            (!is_five_region_total_chain(&labels) && free_signed_energies >= 2).then(|| {
                let mut enriched = packet.clone();
                enriched["homogeneous_wall_rank"] = json!(wall_rank);
                enriched["homogeneous_augmented_rank"] = json!(augmented_rank);
                enriched["free_signed_loop_energies"] = json!(free_signed_energies);
                enriched
            })
        })
        .collect::<Vec<_>>();
    assert!(!eligible.is_empty());
    eligible.sort_by(|left, right| {
        score(right).cmp(&score(left)).then_with(|| {
            left["canonical_key"]
                .as_str()
                .unwrap()
                .cmp(right["canonical_key"].as_str().unwrap())
        })
    });
    let top_score = score(&eligible[0]);
    let tied = eligible
        .iter()
        .filter(|packet| score(packet) == top_score)
        .cloned()
        .collect::<Vec<_>>();
    let selected = tied
        .iter()
        .min_by_key(|packet| packet["canonical_key"].as_str().unwrap())
        .unwrap()
        .clone();
    let labels = selected["representative"]
        .as_array()
        .unwrap()
        .iter()
        .map(|label| label.as_str().unwrap().to_string())
        .collect::<Vec<_>>();
    let charts = (0..N)
        .map(|shift| {
            let transported = labels
                .iter()
                .map(|label| rotate_label(label, shift))
                .collect::<Vec<_>>();
            let sign = sorting_sign(&transported);
            let mut sorted = transported.clone();
            sorted.sort();
            json!({"shift":shift,"transported_order":transported,"canonical_order":sorted,"residue_wedge_sorting_sign":sign})
        })
        .collect::<Vec<_>>();
    let packet = json!({
        "schema":"marici.seven_site_multiloop_orbit_selection.v1",
        "source_inventory":"seven-site-full-source-inventory.json",
        "predeclared_filter":{
            "compatibility_type":"exclude exactly the five-region pairwise-comparable total-chain type used in Entry 1900",
            "multiloop_gate":"rank of the six signed-energy wall rows is at most five, leaving at least two free signed loop energies over the generic labelled X_i base",
            "homogeneous_diagonal_diagnostic":"the augmented rank is retained separately; if it exceeds the signed-energy rank, the orbit meets X_i=t only at t=0 but remains admitted over the generic labelled base",
            "discriminant_blind":true
        },
        "priority_rule":"inherit the Entry 1898 lexicographic score (wall_count,nesting_depth,separated_nonadjacent_region_pairs,labelled_orbit_size), then use the lexicographically least canonical labelled key as a neutral tie-break",
        "eligible_orbit_count":eligible.len(),
        "top_score":{"wall_count":top_score.0,"nesting_depth":top_score.1,"separated_region_pairs":top_score.2,"labelled_orbit_size":top_score.3},
        "top_tie_count":tied.len(),
        "selected_orbit":selected,
        "labelled_C7_charts":charts,
        "orientation_convention":"source representative order transported first; canonical display order carries the recorded wedge sorting sign",
        "stabilizer_preserved":true
    });
    fs::write(
        "../results/seven-site-multiloop-orbit-selection.json",
        serde_json::to_string_pretty(&packet).unwrap() + "\n",
    )
    .unwrap();
    println!(
        "{}",
        json!({"eligible":eligible.len(),"top_score":top_score,"top_ties":tied.len(),"selected":selected["canonical_key"],"wall_rank":selected["homogeneous_wall_rank"],"augmented_rank":selected["homogeneous_augmented_rank"],"free_signed_energies":selected["free_signed_loop_energies"]})
    );
}
