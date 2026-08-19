use serde_json::json;

fn rank(mut a: Vec<Vec<i64>>) -> usize {
    let rows = a.len();
    let cols = a[0].len();
    let mut r = 0;
    for c in 0..cols {
        let Some(p) = (r..rows).find(|&i| a[i][c] != 0) else {
            continue;
        };
        a.swap(r, p);
        for i in 0..rows {
            if i == r || a[i][c] == 0 {
                continue;
            }
            let x = a[i][c];
            let y = a[r][c];
            for j in c..cols {
                a[i][j] = y * a[i][j] - x * a[r][j];
            }
        }
        r += 1;
    }
    r
}

fn main() {
    let chambers = ["123456", "124356", "132456", "134256", "142356", "143256"];
    let occurrences = [
        ("12|35", "124356", "Z*A2"),
        ("124|35", "124356", "Z*A2*B24"),
        ("124|35", "142356", "Z*A2*B24"),
        ("13|25", "134256", "A3/Z"),
        ("134|25", "134256", "A3*B34/Z"),
        ("134|25", "143256", "A3*B34/Z"),
    ];
    let host_rows: Vec<usize> = occurrences
        .iter()
        .map(|(_, host, _)| chambers.iter().position(|x| x == host).unwrap())
        .collect();

    let mut orientation_ranks = Vec::new();
    for mask in 0u8..64 {
        let mut matrix = vec![vec![0i64; 6]; 6];
        for (column, &row) in host_rows.iter().enumerate() {
            matrix[row][column] = if mask & (1 << column) == 0 { 1 } else { -1 };
        }
        orientation_ranks.push(rank(matrix));
    }
    assert!(orientation_ranks.iter().all(|&r| r == 4));

    let canonical_matrix = vec![
        vec![0, 0, 0, 0, 0, 0],
        vec![1, 1, 0, 0, 0, 0],
        vec![0, 0, 0, 0, 0, 0],
        vec![0, 0, 0, 1, 1, 0],
        vec![0, 0, 1, 0, 0, 0],
        vec![0, 0, 0, 0, 0, 1],
    ];
    assert_eq!(rank(canonical_matrix.clone()), 4);

    let packet = json!({
        "schema":"marici.benincasa.string_six_point_corner_to_chamber.v1",
        "source_basis":occurrences.iter().enumerate().map(|(i,(corner,host,factor))|json!({"index":i,"corner":corner,"host_chamber":host,"factor":factor})).collect::<Vec<_>>(),
        "target_basis":chambers,
        "canonical_matrix":canonical_matrix,
        "orientation_cases_checked":64,
        "rank_in_every_orientation":4,
        "kernel_rank":2,
        "kernel_generators_canonical":[[1,-1,0,0,0,0],[0,0,0,1,-1,0]],
        "cokernel_rank":2,
        "cokernel_generators_canonical":["123456","132456"],
        "nonzero_smith_invariants":[1,1,1,1],
        "classification":"the host-chamber forget-support map is not an integral identification with the six-word lattice"
    });
    let text = serde_json::to_string_pretty(&packet).unwrap() + "\n";
    std::fs::write("../string-six-point-corner-to-chamber.json", &text).unwrap();
    print!("{text}");
}
