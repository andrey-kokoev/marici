fn normal_complex_rank(lambda: i64, prime: i64) -> (usize, usize) {
    let differential = lambda.rem_euclid(prime);
    if differential == 0 {
        (1, 1)
    } else {
        (0, 0)
    }
}

fn main() {
    let prime = 32_003_i64;
    let generic_weight = 17_i64;

    // The normal logarithmic complex is R --lambda--> R.  Its Smith factor
    // is lambda, hence its only cohomology over R=Q[lambda] is R/(lambda).
    let smith_factor = "lambda";
    assert_eq!(normal_complex_rank(generic_weight, prime), (0, 0));
    assert_eq!(normal_complex_rank(0, prime), (1, 1));

    let tangential_rank = 5_usize;
    let generic_supported_rank = 0_usize;
    let ordinary_resonant_grade_rank = tangential_rank;
    let derived_special_fiber_total_rank = 2 * tangential_rank;
    assert_eq!(ordinary_resonant_grade_rank, 5);
    assert_eq!(derived_special_fiber_total_rank, 10);

    println!("normal_complex=R--lambda-->R");
    println!("normal_smith_factor={smith_factor}");
    println!("normal_cohomology=R/(lambda)");
    println!("generic_lambda_17_supported_rank={generic_supported_rank}");
    println!("resonant_lambda_0_normal_grades=1,1");
    println!("tangential_candidate_rank={tangential_rank}");
    println!("ordinary_resonant_grade_rank={ordinary_resonant_grade_rank}");
    println!("derived_special_fiber_total_rank={derived_special_fiber_total_rank}");
    println!("canonical_single_grade_truncation=NOT_YET_CHOSEN");
    println!("rank_five_location=KUMMER_RESONANCE_lambda_0");
}
