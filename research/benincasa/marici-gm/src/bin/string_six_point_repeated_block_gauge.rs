use serde_json::json;

fn det(m: [[i64; 2]; 2]) -> i64 {
    m[0][0] * m[1][1] - m[0][1] * m[1][0]
}
fn mul(a: [[i64; 2]; 2], b: [[i64; 2]; 2]) -> [[i64; 2]; 2] {
    let mut c = [[0; 2]; 2];
    for i in 0..2 {
        for j in 0..2 {
            c[i][j] = (0..2).map(|k| a[i][k] * b[k][j]).sum();
        }
    }
    c
}

fn main() {
    let swap = [[0i64, 1], [1, 0]];
    let mut commuting = Vec::new();
    for a in -4..=4 {
        for b in -4..=4 {
            for c in -4..=4 {
                for d in -4..=4 {
                    let m = [[a, b], [c, d]];
                    if det(m).abs() == 1 && mul(m, swap) == mul(swap, m) {
                        commuting.push(m);
                    }
                }
            }
        }
    }
    commuting.sort();
    commuting.dedup();
    let expected = vec![
        [[-1, 0], [0, -1]],
        [[0, -1], [-1, 0]],
        [[0, 1], [1, 0]],
        [[1, 0], [0, 1]],
    ];
    assert_eq!(commuting, expected);

    let packet = json!({
        "schema":"marici.benincasa.string_six_point_repeated_block_gauge.v1",
        "occurrence_transport":"simultaneous swap J on sparse and dense rank-two bases",
        "intertwining_equation":"P*J=J*P",
        "integral_unimodular_solutions":commuting,
        "solutions_up_to_overall_orientation":["I","J"],
        "independent_repeated_blocks":2,
        "residual_unsigned_gauge":"(Z/2)^2",
        "cyclic_composition_for_every_solution":1,
        "classification":"cyclic and reflection covariance preserve but do not select the internal ordering of either repeated wall block"
    });
    let text = serde_json::to_string_pretty(&packet).unwrap() + "\n";
    std::fs::write("../string-six-point-repeated-block-gauge.json", &text).unwrap();
    print!("{text}");
}
