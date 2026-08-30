use serde_json::{json, Value};
use std::{
    collections::{BTreeMap, BTreeSet},
    fs,
};

fn rotate(label: &str, shift: usize) -> String {
    if label == "G" {
        return "G".into();
    }
    if let Some(edge) = label.strip_prefix("G_minus_e") {
        let d = edge
            .chars()
            .map(|c| (c.to_digit(10).unwrap() as usize - 1 + shift) % 5 + 1)
            .collect::<Vec<_>>();
        return format!("G_minus_e{}{}", d[0], d[1]);
    }
    let mut s = label
        .strip_prefix("g_")
        .unwrap()
        .chars()
        .map(|c| (c.to_digit(10).unwrap() as usize - 1 + shift) % 5 + 1)
        .collect::<Vec<_>>();
    s.sort();
    format!(
        "g_{}",
        s.into_iter().map(|i| i.to_string()).collect::<String>()
    )
}

fn reflect(label: &str) -> String {
    if label == "G" {
        return "G".into();
    }
    let r = |i: usize| (5 - i) % 5;
    if let Some(edge) = label.strip_prefix("G_minus_e") {
        let d = edge
            .chars()
            .map(|c| c.to_digit(10).unwrap() as usize - 1)
            .collect::<Vec<_>>();
        let (mut l, mut rr) = (r(d[0]), r(d[1]));
        if (l + 1) % 5 != rr {
            std::mem::swap(&mut l, &mut rr);
        }
        return format!("G_minus_e{}{}", l + 1, rr + 1);
    }
    let mut s = label
        .strip_prefix("g_")
        .unwrap()
        .chars()
        .map(|c| r(c.to_digit(10).unwrap() as usize - 1) + 1)
        .collect::<Vec<_>>();
    s.sort();
    format!(
        "g_{}",
        s.into_iter().map(|i| i.to_string()).collect::<String>()
    )
}

fn cyclic_key(labels: &[String]) -> String {
    (0..5)
        .map(|k| {
            let mut x = labels.iter().map(|s| rotate(s, k)).collect::<Vec<_>>();
            x.sort();
            x.join("|")
        })
        .min()
        .unwrap()
}

fn dihedral_key(labels: &[String]) -> String {
    let reflected = labels.iter().map(|s| reflect(s)).collect::<Vec<_>>();
    cyclic_key(labels).min(cyclic_key(&reflected))
}

fn cut_support(label: &str) -> BTreeSet<usize> {
    if let Some(edge) = label.strip_prefix("G_minus_e") {
        return [edge.chars().next().unwrap().to_digit(10).unwrap() as usize - 1]
            .into_iter()
            .collect();
    }
    let sites = label
        .strip_prefix("g_")
        .unwrap()
        .chars()
        .map(|c| c.to_digit(10).unwrap() as usize - 1)
        .collect::<BTreeSet<_>>();
    (0..5)
        .filter(|e| sites.contains(e) != sites.contains(&((e + 1) % 5)))
        .collect()
}

fn has_shared_cut_pair(labels: &[String]) -> bool {
    labels.iter().any(|m| {
        m.starts_with("G_minus_e")
            && labels.iter().any(|a| {
                a.starts_with("g_")
                    && cut_support(a).contains(cut_support(m).iter().next().unwrap())
            })
    })
}

fn main() {
    let source: Value = serde_json::from_str(
        &fs::read_to_string("../results/five-site-compatible-landau-subsets.json").unwrap(),
    )
    .unwrap();
    let triples = source["census"]
        .as_array()
        .unwrap()
        .iter()
        .find(|x| x["active_wall_count"] == 3)
        .unwrap();
    let mut c5 = BTreeMap::<String, (Vec<String>, bool, bool)>::new();
    for record in triples["representative_records"].as_array().unwrap() {
        let labels = record["representative"]
            .as_array()
            .unwrap()
            .iter()
            .map(|x| x.as_str().unwrap().to_owned())
            .collect::<Vec<_>>();
        c5.insert(
            record["canonical_orbit"].as_str().unwrap().to_owned(),
            (labels, record["forces_t_zero"].as_bool().unwrap(), false),
        );
    }
    for value in c5.values_mut() {
        value.2 = has_shared_cut_pair(&value.0);
    }

    let mut c5_classes = BTreeMap::<String, usize>::new();
    for (_, inherited_zero, inherited_one_wall) in c5.values() {
        let disposition = if *inherited_zero {
            "existing total-energy support"
        } else if *inherited_one_wall {
            "existing one-wall threshold support"
        } else {
            "unclassified genuine three-wall candidate"
        };
        *c5_classes.entry(disposition.into()).or_default() += 1;
    }

    let mut d5 = BTreeMap::<String, BTreeSet<String>>::new();
    for (key, (labels, _, _)) in &c5 {
        d5.entry(dihedral_key(labels))
            .or_default()
            .insert(key.clone());
    }
    let mut classes = BTreeMap::<String, usize>::new();
    let records = d5
        .iter()
        .map(|(key, members)| {
            let zero_values = members.iter().map(|m| c5[m].1).collect::<BTreeSet<_>>();
            let one_wall_values = members.iter().map(|m| c5[m].2).collect::<BTreeSet<_>>();
            assert_eq!(
                zero_values.len(),
                1,
                "total-energy disposition must be reflection invariant"
            );
            assert_eq!(
                one_wall_values.len(),
                1,
                "shared-cut disposition must be reflection invariant"
            );
            let inherited_zero = *zero_values.first().unwrap();
            let inherited_one_wall = !inherited_zero && *one_wall_values.first().unwrap();
            let disposition = if inherited_zero {
                "existing total-energy support"
            } else if inherited_one_wall {
                "existing one-wall threshold support"
            } else {
                "unclassified genuine three-wall candidate"
            };
            *classes.entry(disposition.into()).or_default() += 1;
            json!({"D5_representative": key, "C5_members": members, "disposition": disposition})
        })
        .collect::<Vec<_>>();

    assert_eq!(d5.len(), 138);
    assert_eq!(classes.values().sum::<usize>(), 138);
    let packet = json!({
        "schema": "marici.benincasa.five_site.triple_inherited_support_gate.v1",
        "source": "five-site-compatible-landau-subsets.json",
        "admission": "Only labelled triples co-occurring in a frozen OFPT term.",
        "theorem_used": "Entry 1238: a shared-cut M1+A_m pair projects to an existing one-wall threshold.",
        "C5_disposition_counts": c5_classes,
        "D5_disposition_counts": classes,
        "records": records,
        "scope": "An inherited pair support classification; no three-wall stationarity solution is asserted."
    });
    fs::write(
        "../results/five-site-triple-inherited-support-gate.json",
        serde_json::to_string_pretty(&packet).unwrap() + "\n",
    )
    .unwrap();
    println!(
        "{}",
        serde_json::to_string_pretty(&packet["D5_disposition_counts"]).unwrap()
    );
}
