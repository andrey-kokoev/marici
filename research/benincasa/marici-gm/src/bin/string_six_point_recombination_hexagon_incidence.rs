use serde_json::json;

fn adjacent(cycle: &[usize], a: usize, b: usize) -> bool {
    (0..cycle.len()).any(|i| {
        let x = cycle[i];
        let y = cycle[(i + 1) % cycle.len()];
        (x == a && y == b) || (x == b && y == a)
    })
}

fn main() {
    // Entry 979's oriented chamber-edge occurrence order.
    let cycle = [0usize, 1, 4, 5, 3, 2];
    let plus = ([0usize], [3usize]);
    let minus = ([1usize, 2], [4usize, 5]);

    let plus_pairs: Vec<_> = plus
        .0
        .iter()
        .flat_map(|a| plus.1.iter().map(move |b| (*a, *b)))
        .filter(|(a, b)| adjacent(&cycle, *a, *b))
        .collect();
    let minus_pairs: Vec<_> = minus
        .0
        .iter()
        .flat_map(|a| minus.1.iter().map(move |b| (*a, *b)))
        .filter(|(a, b)| adjacent(&cycle, *a, *b))
        .collect();

    assert!(plus_pairs.is_empty());
    assert_eq!(minus_pairs, vec![(1, 4)]);

    let packet = json!({
        "schema": "marici.benincasa.string_six_point_recombination_hexagon_incidence.v1",
        "oriented_occurrence_cycle": cycle,
        "wall_occurrence_blocks": {
            "ZA2": [0],
            "ZA2B24": [1,2],
            "A3_over_Z": [3],
            "A3B34_over_Z": [4,5]
        },
        "recombination_loci": {
            "++": {
                "wall_blocks": [[0],[3]],
                "incident_occurrence_pairs": plus_pairs,
                "chamber_vertex_count": 0,
                "classification": "algebraic wall intersection with no vertex in the frozen chamber hexagon"
            },
            "--": {
                "wall_blocks": [[1,2],[4,5]],
                "incident_occurrence_pairs": minus_pairs,
                "oriented_cycle_edges": [[1,4]],
                "chamber_vertex_count": 1,
                "classification": "one labelled chamber vertex realizes the repeated-wall recombination support"
            }
        },
        "consequence": "a chamber Cousin boundary can be sought for the -- modification at one labelled vertex, but no such map can type the ++ modification inside the frozen hexagon",
        "remaining_missing_datum": "source-normalized local units and residue orientations for the -- vertex-to-edge map"
    });
    let text = serde_json::to_string_pretty(&packet).unwrap() + "\n";
    std::fs::write("../string-six-point-recombination-hexagon-incidence.json", &text).unwrap();
    print!("{text}");
}
