use serde_json::{json, Value};
use std::{
    collections::{BTreeMap, BTreeSet},
    fs,
};

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
            .map(|c| c.to_digit(10).unwrap() as usize - 1)
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
    } else {
        let edge = name
            .strip_prefix("G_minus_e")
            .unwrap()
            .chars()
            .next()
            .unwrap()
            .to_digit(10)
            .unwrap() as usize
            - 1;
        row[edge] = 2;
    }
    row
}

fn site_coefficient(name: &str) -> i128 {
    parse_region(name)
        .map(|r| r.len() as i128)
        .unwrap_or(N as i128)
}

fn relation(left: &str, right: &str) -> char {
    match (parse_region(left), parse_region(right)) {
        (Some(a), Some(b)) if a == b => '=',
        (Some(a), Some(b)) if a.is_subset(&b) => '<',
        (Some(a), Some(b)) if b.is_subset(&a) => '>',
        (Some(a), Some(b)) if a.is_disjoint(&b) => 'd',
        (Some(_), Some(_)) => 'o',
        (None, None) => 'G',
        _ => 'm',
    }
}

// Canonicalize the six-object relational structure by all 6! permutations.
// This is deliberately independent of source labels and cyclic representatives.
fn poset_signature(labels: &[String]) -> String {
    fn visit(
        prefix: &mut Vec<usize>,
        remaining: &mut Vec<usize>,
        labels: &[String],
        best: &mut Option<String>,
    ) {
        if remaining.is_empty() {
            let mut word = String::new();
            for &i in prefix.iter() {
                word.push(if parse_region(&labels[i]).is_some() {
                    'r'
                } else {
                    'G'
                });
                word.push(
                    char::from_digit(
                        parse_region(&labels[i]).map(|r| r.len()).unwrap_or(N) as u32,
                        10,
                    )
                    .unwrap(),
                );
            }
            word.push(':');
            for i in 0..prefix.len() {
                for j in i + 1..prefix.len() {
                    word.push(relation(&labels[prefix[i]], &labels[prefix[j]]));
                }
            }
            if best.as_ref().map(|old| &word < old).unwrap_or(true) {
                *best = Some(word);
            }
            return;
        }
        for index in 0..remaining.len() {
            let value = remaining.remove(index);
            prefix.push(value);
            visit(prefix, remaining, labels, best);
            prefix.pop();
            remaining.insert(index, value);
        }
    }
    let mut best = None;
    visit(
        &mut Vec::new(),
        &mut (0..labels.len()).collect(),
        labels,
        &mut best,
    );
    best.unwrap()
}

fn score(packet: &Value) -> (usize, usize, usize, usize) {
    let s = &packet["score"];
    (
        s["wall_count"].as_u64().unwrap() as usize,
        s["nesting_depth"].as_u64().unwrap() as usize,
        s["separated_region_pairs"].as_u64().unwrap() as usize,
        s["labelled_orbit_size"].as_u64().unwrap() as usize,
    )
}

fn main() {
    let inventory: Value = serde_json::from_str(
        &fs::read_to_string("../results/seven-site-full-source-inventory.json").unwrap(),
    )
    .unwrap();
    let mut classes = BTreeMap::<String, Vec<Value>>::new();
    for orbit in inventory["all_orbits"].as_array().unwrap() {
        let labels = orbit["representative"]
            .as_array()
            .unwrap()
            .iter()
            .map(|v| v.as_str().unwrap().to_string())
            .collect::<Vec<_>>();
        let rows = labels
            .iter()
            .map(|label| wall_row(label))
            .collect::<Vec<_>>();
        let rank = rank_integer(rows.clone());
        let augmented_rank = rank_integer(
            labels
                .iter()
                .zip(rows.iter())
                .map(|(label, row)| {
                    let mut out = row.clone();
                    out.push(site_coefficient(label));
                    out
                })
                .collect(),
        );
        let diagonal = if augmented_rank == rank {
            "generic_homogeneous_line"
        } else {
            "origin_only"
        };
        let signature = poset_signature(&labels);
        let key = format!(
            "r{rank}-a{augmented_rank}-f{}-{diagonal}-{signature}",
            N - rank
        );
        let mut enriched = orbit.clone();
        enriched["wall_rank"] = json!(rank);
        enriched["augmented_rank"] = json!(augmented_rank);
        enriched["free_signed_energies"] = json!(N - rank);
        enriched["homogeneous_diagonal_behavior"] = json!(diagonal);
        enriched["compatibility_poset_signature"] = json!(signature);
        classes.entry(key).or_default().push(enriched);
    }
    let mut packets = classes.into_iter().map(|(key, mut members)| {
        members.sort_by(|l,r| score(r).cmp(&score(l)).then_with(|| l["canonical_key"].as_str().unwrap().cmp(r["canonical_key"].as_str().unwrap())));
        let maximal_score = score(&members[0]);
        let ties = members.iter().take_while(|m| score(m)==maximal_score).count();
        json!({
            "class_key":key,
            "orbit_count":members.len(),
            "wall_rank":members[0]["wall_rank"],
            "augmented_rank":members[0]["augmented_rank"],
            "free_signed_energies":members[0]["free_signed_energies"],
            "homogeneous_diagonal_behavior":members[0]["homogeneous_diagonal_behavior"],
            "compatibility_poset_signature":members[0]["compatibility_poset_signature"],
            "maximal_score":{"wall_count":maximal_score.0,"nesting_depth":maximal_score.1,"separated_region_pairs":maximal_score.2,"labelled_orbit_size":maximal_score.3},
            "maximal_tie_count":ties,
            "neutral_representative":members[0],
            "member_keys":members.iter().map(|m|m["canonical_key"].clone()).collect::<Vec<_>>()
        })
    }).collect::<Vec<_>>();
    packets.sort_by(|l, r| {
        l["wall_rank"]
            .as_u64()
            .cmp(&r["wall_rank"].as_u64())
            .then_with(|| {
                l["class_key"]
                    .as_str()
                    .unwrap()
                    .cmp(r["class_key"].as_str().unwrap())
            })
    });
    let counts = packets
        .iter()
        .fold(BTreeMap::<String, usize>::new(), |mut acc, p| {
            let k = format!(
                "rank{}_{}",
                p["wall_rank"].as_u64().unwrap(),
                p["homogeneous_diagonal_behavior"].as_str().unwrap()
            );
            *acc.entry(k).or_default() += p["orbit_count"].as_u64().unwrap() as usize;
            acc
        });
    let packet = json!({
        "schema":"marici.seven_site_inventory_partition.v1",
        "source_inventory":"seven-site-full-source-inventory.json",
        "predeclared_partition":["signed-energy wall rank","compatibility-poset isomorphism type with region/cardinality colors","number of free signed energies (hence generic free loop-square variables)","homogeneous diagonal behavior from augmented rank"],
        "predeclared_ranking":"within each class, maximize the frozen Entry 1898 score, then choose the lexicographically least canonical labelled key; no cover or discriminant data enter",
        "orbit_count":inventory["cyclic_orbit_count"],
        "class_count":packets.len(),
        "orbit_counts_by_rank_and_diagonal":counts,
        "classes":packets
    });
    fs::write(
        "../results/seven-site-inventory-partition.json",
        serde_json::to_string_pretty(&packet).unwrap() + "\n",
    )
    .unwrap();
    println!(
        "{}",
        json!({"orbits":inventory["cyclic_orbit_count"],"classes":packet["class_count"],"counts":packet["orbit_counts_by_rank_and_diagonal"]})
    );
}
