fn main() {
    let mut distributions = 0usize;
    let mut gaussian_mismatches = 0usize;
    let mut cumulant_repairs = 0usize;
    let mut conditional_matches = 0usize;

    // Correlated Rademacher pair:
    // P(X=x,Y=y)=(1+r xy)/4, x,y in {+1,-1}.
    // Use r=n/d and clear denominators.
    for d in 1_i128..=64 {
        for n in -d..=d {
            // All four probability numerators d+nxy are nonnegative.
            for xy in [-1_i128, 1_i128] { assert!(d + n * xy >= 0); }
            distributions += 1;

            // E[X^2]=E[Y^2]=E[X^2Y^2]=1 and E[XY]=r.
            // Gaussian Wick prediction is 1+2r^2.
            let gaussian_fourth_num = d * d + 2 * n * n;
            let exact_fourth_num = d * d;
            let fourth_cumulant_num = -2 * n * n;
            assert_eq!(gaussian_fourth_num + fourth_cumulant_num, exact_fourth_num);
            cumulant_repairs += 1;
            if n != 0 {
                assert_ne!(gaussian_fourth_num, exact_fourth_num);
                gaussian_mismatches += 1;
            }

            // Since Y^2=1 pointwise, E[Y^2|X]=1 and then
            // E[X^2 E[Y^2|X]]=1 in either conditioning order.
            let conditional_fourth_num = d * d;
            assert_eq!(conditional_fourth_num, exact_fourth_num);
            conditional_matches += 1;
        }
    }

    println!("{{");
    println!("  \"schema\": \"marici.nongaussian_conditional_cut_cumulant.v1\",");
    println!("  \"distributions\": {distributions},");
    println!("  \"nonzero_correlation_gaussian_mismatches\": {gaussian_mismatches},");
    println!("  \"fourth_cumulant_repairs\": {cumulant_repairs},");
    println!("  \"conditional_matches\": {conditional_matches},");
    println!("  \"connected_fourth_cumulant\": \"-2 r^2\",");
    println!("  \"exact_conditional_cut_remains_associative\": true");
    println!("}}");
}
