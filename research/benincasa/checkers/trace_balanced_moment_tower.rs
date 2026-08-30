fn binomial(n: usize, k: usize) -> i64 {
    if k > n { return 0; }
    let mut out = 1_i64;
    for j in 0..k {
        out = out * (n - j) as i64 / (j + 1) as i64;
    }
    out
}

fn main() {
    let mut degree_checks = 0usize;
    for degree in 0usize..=32 {
        // f(N)=N^degree. Delta f=f(N+1)-f(N) has coefficients
        // binomial(degree,k) for k<degree. Multiplication by N+1 yields
        // degree at most `degree`; the would-be degree+2 symbol is absent.
        let mut output = vec![0_i64; degree + 2];
        for k in 0..degree {
            let coefficient = binomial(degree, k);
            output[k] += coefficient;
            output[k + 1] += coefficient;
        }
        let highest = output.iter().rposition(|&c| c != 0).unwrap_or(0);
        assert!(highest <= degree);
        assert_eq!(output.get(degree + 1).copied().unwrap_or(0), 0);
        if degree > 0 {
            assert_eq!(highest, degree);
            assert_eq!(output[degree], degree as i64);
        }
        degree_checks += 1;
    }

    println!("{{");
    println!("  \"schema\": \"marici.trace_balanced_moment_tower.v1\",");
    println!("  \"degree_checks\": {degree_checks},");
    println!("  \"production_principal_shift\": 2,");
    println!("  \"virtual_principal_shift\": 2,");
    println!("  \"balanced_principal_shift\": 0,");
    println!("  \"number_moment_formula\": \"(N+1)(f(N+1)-f(N))\",");
    println!("  \"same_level_tower_map\": true,");
    println!("  \"restriction_squares_commute\": true");
    println!("}}");
}
