fn rank(mut a: Vec<Vec<f64>>) -> usize {
    let (m, n) = (a.len(), a[0].len());
    let mut r = 0;
    for c in 0..n {
        if let Some(p) = (r..m).find(|&i| a[i][c].abs() > 1e-9) {
            a.swap(r, p);
            let q = a[r][c];
            for j in c..n { a[r][j] /= q; }
            for i in 0..m {
                if i != r {
                    let q = a[i][c];
                    for j in c..n { a[i][j] -= q * a[r][j]; }
                }
            }
            r += 1;
        }
    }
    r
}

fn main() {
    // Columns are the grade-two and grade-three contact routes for edges
    // 12, 23, 31. Rows retain the three independent contact letters.
    let e = vec![
        vec![8., -8., 0., 0., 0., 0.],
        vec![0., 0., 8., -8., 0., 0.],
        vec![0., 0., 0., 0., 8., -8.],
    ];
    assert_eq!(rank(e.clone()), 3);
    for edge in 0..3 {
        let mut p = vec![0.; 6];
        p[2 * edge] = 1.;
        p[2 * edge + 1] = 1.;
        for row in &e {
            let value: f64 = row.iter().zip(&p).map(|(x, y)| x * y).sum();
            assert!(value.abs() < 1e-9);
        }
    }
    println!("{{\"status\":\"pass\",\"source_dimension\":6,\"augmentation_rank\":3,\"kernel_rank\":3,\"kernel_basis\":[\"p12\",\"p23\",\"p31\"]}}");
}
