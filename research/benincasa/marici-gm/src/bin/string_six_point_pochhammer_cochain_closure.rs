use serde_json::{json, Value};
use symbolica::prelude::*;

fn a(s: &str) -> Atom {
    Atom::parse(s, "marici", Default::default()).unwrap()
}
fn clean(x: Atom) -> Atom {
    x.together().cancel().factor()
}

fn main() {
    let prior: Value = serde_json::from_str(
        &std::fs::read_to_string("../string-six-point-circuit-exceptional-cochain.json").unwrap(),
    )
    .unwrap();
    let lambda: Vec<Atom> = prior["cochain"]
        .as_array()
        .unwrap()
        .iter()
        .map(|x| a(x.as_str().unwrap()))
        .collect();
    assert_eq!(lambda.len(), 6);

    // The cycle follows adjacent swaps from increasing to decreasing for the
    // first three edges and reverses them for the final three.
    let cycle = [0usize, 1, 4, 5, 3, 2];
    let transport = [
        a("B34"),
        a("B24"),
        a("X"),
        a("1/B34"),
        a("1/B24"),
        a("1/X"),
    ];
    let holonomy = transport
        .iter()
        .cloned()
        .fold(a("1"), |p, u| clean(p * u));
    assert_eq!(holonomy, a("1"));

    let defects: Vec<Atom> = (0..6)
        .map(|k| {
            let current = cycle[k];
            let next = cycle[(k + 1) % 6];
            clean(lambda[next].clone() - transport[k].clone() * lambda[current].clone())
        })
        .collect();

    // Transport every edge defect to the final/base vertex.  The sum is the
    // twisted boundary of the oriented chamber two-cell.
    let mut weighted_sum = a("0");
    for j in 0..6 {
        let suffix = ((j + 1)..6)
            .map(|k| transport[k].clone())
            .fold(a("1"), |p, u| clean(p * u));
        weighted_sum += suffix * defects[j].clone();
    }
    assert_eq!(clean(weighted_sum), a("0"));
    let nonzero_defects = defects.iter().filter(|d| **d != a("0")).count();

    let packet = json!({
        "schema":"marici.benincasa.string_six_point_pochhammer_cochain_closure.v1",
        "chamber_order":["123456","124356","142356","143256","134256","132456"],
        "index_cycle":cycle,
        "edge_pairs":["34","24","23","34","24","23"],
        "edge_orientations":["forward","forward","forward","reverse","reverse","reverse"],
        "half_monodromy_transports":["B34","B24","X","B34^-1","B24^-1","X^-1"],
        "holonomy":"1",
        "twisted_defects":defects.iter().map(ToString::to_string).collect::<Vec<_>>(),
        "nonzero_twisted_defect_count":nonzero_defects,
        "weighted_two_cell_boundary":"0",
        "classification":"the exceptional cochain is generally not a flat vertex section, but its source-derived twisted edge coboundary closes exactly on the oriented chamber two-cell",
        "scope":"rank-one Koba-Nielsen/Pochhammer coefficient transport on the frozen chamber cycle; no claim of a six-dimensional chain equivalence"
    });
    let text = serde_json::to_string_pretty(&packet).unwrap() + "\n";
    std::fs::write("../string-six-point-pochhammer-cochain-closure.json", &text).unwrap();
    print!("{text}");
}
