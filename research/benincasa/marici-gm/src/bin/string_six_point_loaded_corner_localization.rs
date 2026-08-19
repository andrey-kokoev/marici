use serde_json::json;

fn inverse_unimodular(m: &[Vec<i64>]) -> Vec<Vec<i64>> {
    let n = m.len();
    let mut a = vec![vec![0i64; 2 * n]; n];
    for i in 0..n {
        for j in 0..n {
            a[i][j] = m[i][j];
        }
        a[i][n + i] = 1;
    }
    for c in 0..n {
        let p = (c..n).find(|&i| a[i][c].abs() == 1).unwrap();
        a.swap(c, p);
        if a[c][c] == -1 {
            for x in &mut a[c] {
                *x = -*x;
            }
        }
        for i in 0..n {
            if i == c {
                continue;
            }
            let q = a[i][c];
            for j in 0..2 * n {
                a[i][j] -= q * a[c][j];
            }
        }
    }
    a.into_iter().map(|row| row[n..].to_vec()).collect()
}

fn main() {
    // C = S diag(f1,f2,f2,f3,f4,f4), in the conventions of Entry 967.
    let s = vec![
        vec![0, 0, 0, 0, -1, 0],
        vec![1, 0, 0, 0, 1, 0],
        vec![0, -1, 0, 0, 0, 0],
        vec![0, 1, 0, 1, 0, 0],
        vec![0, 0, 1, 0, 0, 0],
        vec![0, 0, 0, 0, 0, 1],
    ];
    let inv = inverse_unimodular(&s);
    let mut product = vec![vec![0i64; 6]; 6];
    for i in 0..6 {
        for j in 0..6 {
            product[i][j] = (0..6).map(|k| inv[i][k] * s[k][j]).sum();
        }
    }
    assert_eq!(
        product,
        (0..6)
            .map(|i| (0..6).map(|j| if i == j { 1 } else { 0 }).collect())
            .collect::<Vec<Vec<i64>>>()
    );

    let factors = [
        ("(ZA2)^2-1", vec![0usize]),
        ("(ZA2B24)^2-1", vec![1usize, 2]),
        ("(A3/Z)^2-1", vec![3usize]),
        ("(A3B34/Z)^2-1", vec![4usize, 5]),
    ];
    let local = factors
        .iter()
        .map(|(factor, columns)| {
            json!({
                "factor":factor,
                "generic_corank":columns.len(),
                "kernel_source_columns":columns,
                "cokernel_dual_rows":columns.iter().map(|&j|inv[j].clone()).collect::<Vec<_>>(),
                "local_elementary_divisors":vec![factor.to_string();columns.len()]
            })
        })
        .collect::<Vec<_>>();

    let packet = json!({
        "schema":"marici.benincasa.string_six_point_loaded_corner_localization.v1",
        "factorization":"C=S*diag(f1,f2,f2,f3,f4,f4)",
        "integral_skeleton":s,
        "integral_skeleton_inverse":inv,
        "skeleton_unimodular":true,
        "localizations":local,
        "corank_pattern":[1,2,1,2],
        "fitting_valuation_pattern":[1,2,1,2],
        "classification":"every composite wall defect is a labelled source kernel and target costalk cokernel of the loaded comparison; no hidden local elementary divisor occurs"
    });
    let text = serde_json::to_string_pretty(&packet).unwrap() + "\n";
    std::fs::write("../string-six-point-loaded-corner-localization.json", &text).unwrap();
    print!("{text}");
}
