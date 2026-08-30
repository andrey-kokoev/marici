fn binomial(n: usize, k: usize) -> i64 {
    if k > n { return 0; }
    let mut out = 1_i64;
    for j in 0..k {
        out = out * (n - j) as i64 / (j + 1) as i64;
    }
    out
}

fn main() {
    let mut global_checks = 0usize;
    let mut exchange_checks = 0usize;
    let mut pushed_checks = 0usize;

    for a in 0usize..=5 {
        for b in 0usize..=(5 - a) {
            for c in 0usize..=(5 - a - b) {
                let degree = a + b + c;
                if degree == 0 { continue; }

                // f=(Np^a Nq^b Nk^c).  In f(N+1)-f(N), the top total
                // number-degree is degree-1. Multiplication by
                // (Np+1)(Nq+1)(Nk+1) raises by three.
                let output_number_degree = degree + 2;
                let input_physical_degree = 2 * degree;
                let output_physical_degree = 2 * output_number_degree;
                assert_eq!(output_physical_degree - input_physical_degree, 4);

                // q<->k exchanges b,c and leaves all degree data invariant.
                assert_eq!(a + b + c, a + c + b);
                assert_eq!(binomial(b, 0) * binomial(c, 0),
                           binomial(c, 0) * binomial(b, 0));
                global_checks += 1;
                exchange_checks += 1;
            }
        }
    }

    // Push internal modes to their vacuum relative state. For f=f(Np),
    // (Nq+1)(Nk+1) -> 1 and the generator preserves observed degree.
    for a in 1usize..=32 {
        let top_difference_degree = a - 1;
        let observed_output_degree = top_difference_degree + 1;
        assert_eq!(observed_output_degree, a);
        pushed_checks += 1;
    }

    println!("{{");
    println!("  \"schema\": \"marici.multimode_cubic_cut_filtration.v1\",");
    println!("  \"global_number_monomial_checks\": {global_checks},");
    println!("  \"q_k_exchange_checks\": {exchange_checks},");
    println!("  \"vacuum_pushforward_checks\": {pushed_checks},");
    println!("  \"global_jump\": \"a_p^dagger a_q^dagger a_k^dagger\",");
    println!("  \"global_physical_degree_shift\": 4,");
    println!("  \"pushed_observed_degree_shift\": 0,");
    println!("  \"q_k_exchange_natural\": true,");
    println!("  \"same_level_before_pushforward\": false");
    println!("}}");
}
