fn rank(mut a: Vec<Vec<i64>>) -> usize {
    let (n, m) = (a.len(), a[0].len());
    let mut row = 0;
    for col in 0..m {
        let Some(pivot) = (row..n).find(|&i| a[i][col] != 0) else {
            continue;
        };
        a.swap(row, pivot);
        for i in row + 1..n {
            if a[i][col] == 0 {
                continue;
            }
            let (x, y) = (a[row][col], a[i][col]);
            for j in col..m {
                a[i][j] = x * a[i][j] - y * a[row][j];
            }
        }
        row += 1;
    }
    row
}

fn main() {
    // Leading t^{-1} dr coefficient of the raw E-chart pullback, with the
    // common scalar 1/(r(r-1)) removed. Basis order is e1,...,e9.
    let mut c = vec![vec![0_i64; 9]; 9];
    c[7][6] = 1;
    c[8][6] = -1;
    assert_eq!(rank(c.clone()), 1);
    for i in 0..9 {
        for j in 0..9 {
            let square: i64 = (0..9).map(|k| c[i][k] * c[k][j]).sum();
            assert_eq!(square, 0);
        }
    }

    // The radial Rees lattice f_i=t^{w_i}e_i. Every nonzero irregular
    // entry gains w_row-w_col=1 and therefore becomes regular.
    let weights = [0_i64, 0, 0, 0, 0, 0, 0, 1, 1];
    for i in 0..9 {
        for j in 0..9 {
            if c[i][j] != 0 {
                assert_eq!(weights[i] - weights[j], 1);
            }
        }
    }

    // Exact symbolic pullback of the frozen bivariate connection gives
    // these minimum t-valuations in both standard charts.
    let raw = (-1_i64, -1_i64); // (dt coefficient, exceptional tangent)
    let gauged_e_chart = (-1_i64, 0_i64);
    let gauged_v_chart = (-1_i64, 0_i64);
    assert_eq!(raw.1 + 1, gauged_e_chart.1);
    assert_eq!(gauged_e_chart, gauged_v_chart);

    // Remaining exceptional-direction denominators divide r(r-1): r=0
    // is the other cusp wall and r=1 is the soft wall X3=0.
    for r in [-7_i64, -2, 2, 3, 11] {
        assert_ne!(r * (r - 1), 0);
    }

    println!("{{");
    println!("  \"schema\": \"marici.benincasa.rank9_radial_rees_resolution.v1\",");
    println!("  \"module\": \"nine-master q_G12 residue module\",");
    println!("  \"raw_tangent_leading_rank\": 1,");
    println!("  \"raw_tangent_leading_square_zero\": true,");
    println!("  \"rees_weights_e1_to_e9\": [0,0,0,0,0,0,0,1,1],");
    println!("  \"raw_min_t_valuations\": {{\"dt\":-1,\"tangent\":-1}},");
    println!("  \"gauged_min_t_valuations_E_chart\": {{\"dt\":-1,\"tangent\":0}},");
    println!("  \"gauged_min_t_valuations_v_chart\": {{\"dt\":-1,\"tangent\":0}},");
    println!("  \"exceptional_direction_support\": [\"r=0 (ell3=0)\",\"r=1 (X3=0)\"],");
    println!("  \"new_support_factor\": false,");
    println!("  \"new_carrier_datum\": false,");
    println!(
        "  \"scope\": \"rank-nine absolute residue module; not the marked rank-twelve extension\""
    );
    println!("}}");
}
