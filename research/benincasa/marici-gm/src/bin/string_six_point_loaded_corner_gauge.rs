use serde_json::json;

fn determinant(mut a: Vec<Vec<i64>>) -> i64 {
    let n = a.len();
    let mut denominator = 1i64;
    let mut sign = 1i64;
    for k in 0..n - 1 {
        let p = (k..n).find(|&i| a[i][k] != 0).unwrap();
        if p != k {
            a.swap(k, p);
            sign = -sign;
        }
        let pivot = a[k][k];
        for i in k + 1..n {
            for j in k + 1..n {
                a[i][j] = (a[i][j] * pivot - a[i][k] * a[k][j]) / denominator;
            }
        }
        denominator = pivot;
    }
    sign * a[n - 1][n - 1]
}

fn skeleton(c24_endpoint: i64, c34_endpoint: i64, signs: u8) -> Vec<Vec<i64>> {
    let mut m = vec![vec![0i64; 6]; 6];
    m[1][0] = 1;
    m[2][1] = -1;
    m[3][1] = c24_endpoint;
    m[4][2] = 1;
    m[3][3] = 1;
    m[0][4] = -1;
    m[1][4] = c34_endpoint;
    m[5][5] = 1;
    for col in 0..6 {
        if signs & (1 << col) != 0 {
            for row in &mut m {
                row[col] = -row[col];
            }
        }
    }
    m
}

fn main() {
    let mut cases = 0usize;
    for c24 in -4..=4 {
        for c34 in -4..=4 {
            for signs in 0u8..64 {
                assert_eq!(determinant(skeleton(c24, c34, signs)).abs(), 1);
                cases += 1;
            }
        }
    }
    assert_eq!(cases, 9 * 9 * 64);

    let source_monomials = ["ZA2", "ZA2B24", "A3/Z", "A3B34/Z"];
    let direct_paths = [("123456->124356", "A3B34/Z"), ("132456->134256", "ZA2B24")];
    let longer_paths = [
        ("123456->124356->142356", "A3B34B24/Z"),
        ("132456->134256->143256", "ZA2B24B34"),
    ];
    assert!(direct_paths
        .iter()
        .all(|(_, monomial)| source_monomials.contains(monomial)));
    assert!(longer_paths
        .iter()
        .all(|(_, monomial)| !source_monomials.contains(monomial)));

    let packet = json!({
        "schema":"marici.benincasa.string_six_point_loaded_corner_gauge.v1",
        "endpoint_coefficients_checked":"-4..4 independently on both circuit columns",
        "column_orientation_cases":64,
        "total_integral_gauge_cases":cases,
        "absolute_skeleton_determinant_in_every_case":1,
        "endpoint_change":"integral target-row shear supported on the already hit endpoint",
        "orientation_change":"diagonal unimodular source gauge",
        "direct_support_compatible_paths":direct_paths.iter().map(|(path,monomial)|json!({"path":path,"loaded_monomial":monomial})).collect::<Vec<_>>(),
        "longer_active_paths_rejected":longer_paths.iter().map(|(path,monomial)|json!({"path":path,"loaded_monomial":monomial,"reason":"monomial absent from frozen composite Fitting support"})).collect::<Vec<_>>(),
        "source_composite_monomials":source_monomials,
        "classification":"the determinant gauge class is integral under orientations and endpoint shears, and source support uniquely selects the direct loaded paths"
    });
    let text = serde_json::to_string_pretty(&packet).unwrap() + "\n";
    std::fs::write("../string-six-point-loaded-corner-gauge.json", &text).unwrap();
    print!("{text}");
}
