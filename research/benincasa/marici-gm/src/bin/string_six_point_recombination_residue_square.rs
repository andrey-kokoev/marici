use serde_json::{json, Value};

fn rank_two(rows: [&[i32]; 2]) -> bool {
    for i in 0..rows[0].len() {
        for j in i + 1..rows[0].len() {
            if rows[0][i] * rows[1][j] - rows[0][j] * rows[1][i] != 0 {
                return true;
            }
        }
    }
    false
}

fn main() {
    let packet: Value = serde_json::from_str(
        &std::fs::read_to_string("../string-six-point-character-plane-reflection.json").unwrap(),
    )
    .unwrap();
    let cases = [
        (
            "++",
            "ZA2 & A3/Z",
            vec![1, 1, 0, 0, 0],
            vec![-1, 0, 1, 0, 0],
        ),
        (
            "--",
            "ZA2B24 & A3B34/Z",
            vec![1, 1, 0, 1, 0],
            vec![-1, 0, 1, 0, 1],
        ),
    ];
    let mut records = Vec::new();
    for (character, intersection, g1, g2) in cases {
        assert!(rank_two([&g1, &g2]));
        let plane = packet["rank_two_character_planes"]
            .as_array()
            .unwrap()
            .iter()
            .find(|x| x["character"] == character)
            .unwrap();
        let collapsed: Vec<_> = plane["generic_pairwise_intersections"]
            .as_array()
            .unwrap()
            .iter()
            .filter(|x| x["intersection"] == intersection && x["specialized_rank"] == 1)
            .collect();
        assert_eq!(collapsed.len(), 4);
        let scalar = collapsed[0]["collapse_scalar_corrected_over_normal"]
            .as_str()
            .unwrap();
        assert!(collapsed
            .iter()
            .all(|x| x["collapse_scalar_corrected_over_normal"] == scalar));
        records.push(json!({
            "character": character,
            "intersection": intersection,
            "log_gradient_order_12": [g1,g2],
            "normal_crossing_rank": 2,
            "common_fiber_row_order_12": ["1",scalar],
            "common_fiber_row_order_21": ["-1",format!("-({scalar})")],
            "signed_koszul_sum": ["0","0"],
            "carrier_regular_sequence": true,
            "carrier_excess_tor": 0
        }));
    }
    let out = json!({
        "schema":"marici.benincasa.string_six_point_recombination_residue_square.v1",
        "log_coordinate_order":["Z","A2","A3","B24","B34"],
        "cases":records,
        "classification":"both recombination loci are ordinary normal crossings; the two Poincare-residue orders differ by the forced Koszul sign and have zero signed commutator",
        "scope":"ordinary logarithmic carrier residue square and its induced common-fiber row; no claim about a separate degree-one exceptional cell"
    });
    let text = serde_json::to_string_pretty(&out).unwrap() + "\n";
    std::fs::write(
        "../string-six-point-recombination-residue-square.json",
        &text,
    )
    .unwrap();
    print!("{text}");
}
