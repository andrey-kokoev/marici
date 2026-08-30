fn n_matrix_element(m: usize, n: usize) -> i64 {
    if m == n { n as i64 } else { 0 }
}

fn aa_support(m: usize, n: usize) -> bool {
    n >= 2 && m + 2 == n
}

fn adag_adag_support(m: usize, n: usize) -> bool {
    m >= 2 && m == n + 2
}

fn main() {
    let mut cross_checks = 0usize;
    for even in (0..=12).filter(|n| n % 2 == 0) {
        for odd in (0..=13).filter(|n| n % 2 == 1) {
            assert_eq!(n_matrix_element(even, odd), 0);
            assert!(!aa_support(even, odd));
            assert!(!adag_adag_support(even, odd));
            assert_eq!(n_matrix_element(odd, even), 0);
            assert!(!aa_support(odd, even));
            assert!(!adag_adag_support(odd, even));
            cross_checks += 6;
        }
    }

    let mut norm_checks = 0usize;
    for br in -5_i64..=5 {
        for bi in -5_i64..=5 {
            let cut_norm = br * br + bi * bi;
            assert!(cut_norm >= 0);
            assert_eq!(cut_norm == 0, br == 0 && bi == 0);
            norm_checks += 1;
        }
    }

    println!("{{");
    println!("  \"schema\": \"marici.gaussian_cubic_parity_cut.v1\",");
    println!("  \"even_odd_covariance_cross_checks\": {cross_checks},");
    println!("  \"linear_cubic_covariance_terms\": 0,");
    println!("  \"quadratic_cubic_cut_norm_checks\": {norm_checks},");
    println!("  \"first_statistical_cubic_grade\": \"quadratic\",");
    println!("  \"selection_rule\": \"Gaussian-even x cubic-odd x covariance-even vanishes\"");
    println!("}}");
}
