use serde_json::json;

fn gcd(mut a: i64, mut b: i64) -> i64 {
    a = a.abs();
    b = b.abs();
    while b != 0 {
        let r = a % b;
        a = b;
        b = r;
    }
    a
}

fn determinant(mut a: Vec<Vec<i64>>) -> i64 {
    let n = a.len();
    let mut den = 1i64;
    let mut sign = 1i64;
    for k in 0..n - 1 {
        let Some(p) = (k..n).find(|&i| a[i][k] != 0) else {
            return 0;
        };
        if p != k {
            a.swap(p, k);
            sign = -sign;
        }
        let pivot = a[k][k];
        for i in k + 1..n {
            for j in k + 1..n {
                a[i][j] = (a[i][j] * pivot - a[i][k] * a[k][j]) / den;
            }
        }
        den = pivot;
    }
    sign * a[n - 1][n - 1]
}

fn combinations(n: usize, k: usize) -> Vec<Vec<usize>> {
    fn go(start: usize, n: usize, k: usize, cur: &mut Vec<usize>, out: &mut Vec<Vec<usize>>) {
        if cur.len() == k {
            out.push(cur.clone());
            return;
        }
        for i in start..n {
            cur.push(i);
            go(i + 1, n, k, cur, out);
            cur.pop();
        }
    }
    let mut out = Vec::new();
    go(0, n, k, &mut Vec::new(), &mut out);
    out
}

fn main() {
    let chambers = ["123456", "124356", "132456", "134256", "142356", "143256"];
    let permutations = [
        [2, 3, 4],
        [2, 4, 3],
        [3, 2, 4],
        [3, 4, 2],
        [4, 2, 3],
        [4, 3, 2],
    ];
    let mut edges = Vec::new();
    for (i, p) in permutations.iter().enumerate() {
        for swap in [0usize, 1] {
            let mut q = *p;
            q.swap(swap, swap + 1);
            let j = permutations.iter().position(|x| *x == q).unwrap();
            if i < j {
                edges.push((i, j));
            }
        }
    }
    edges.sort();
    edges.dedup();
    assert_eq!(edges.len(), 6);

    // Four independent columns spanning Entry 963's host image.
    let host_rows = [1usize, 3, 4, 5];
    let mut saturating_pairs = Vec::new();
    for pair in combinations(edges.len(), 2) {
        let mut matrix = vec![vec![0i64; 6]; 6];
        for (col, &row) in host_rows.iter().enumerate() {
            matrix[row][col] = 1;
        }
        for (offset, &edge_index) in pair.iter().enumerate() {
            let (a, b) = edges[edge_index];
            matrix[a][4 + offset] = -1;
            matrix[b][4 + offset] = 1;
        }
        let det = determinant(matrix);
        if det.abs() == 1 {
            saturating_pairs.push(json!({
                "edges":[
                    format!("{}->{}",chambers[edges[pair[0]].0],chambers[edges[pair[0]].1]),
                    format!("{}->{}",chambers[edges[pair[1]].0],chambers[edges[pair[1]].1])
                ],
                "determinant":det
            }));
        }
    }
    assert!(!saturating_pairs.is_empty());

    let mut all_minors_gcd = 0i64;
    for item in &saturating_pairs {
        all_minors_gcd = gcd(all_minors_gcd, item["determinant"].as_i64().unwrap());
    }
    assert_eq!(all_minors_gcd, 1);

    let packet = json!({
        "schema":"marici.benincasa.string_six_point_chamber_transition_saturation.v1",
        "chamber_basis":chambers,
        "adjacency_rule":"adjacent transposition in the ordered labels (2,3,4)",
        "edges":edges.iter().map(|&(a,b)|format!("{}--{}",chambers[a],chambers[b])).collect::<Vec<_>>(),
        "edge_count":edges.len(),
        "host_image_basis_rows":["124356","134256","142356","143256"],
        "minimum_transition_columns_needed":2,
        "saturating_edge_pairs":saturating_pairs,
        "saturating_pair_count":saturating_pairs.len(),
        "integral_saturation":all_minors_gcd==1,
        "classification":"existing chamber adjacency can integrally fill the two missing host directions; twisted loading remains absent"
    });
    let text = serde_json::to_string_pretty(&packet).unwrap() + "\n";
    std::fs::write(
        "../string-six-point-chamber-transition-saturation.json",
        &text,
    )
    .unwrap();
    print!("{text}");
}
