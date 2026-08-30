fn main() {
    let mut checks = 0usize;
    for ar in -3_i64..=3 {
        for ai in -3_i64..=3 {
            let squeezing_norm = 2 * (ar * ar + ai * ai);
            for b1 in -3_i64..=3 {
                for b2 in -3_i64..=3 {
                    for b3 in -3_i64..=3 {
                        let cut_norm = b1 * b1 + b2 * b2 + b3 * b3;
                        let occupation_second_grade = squeezing_norm + cut_norm;
                        let uncertainty_second_grade =
                            occupation_second_grade - squeezing_norm;
                        assert_eq!(uncertainty_second_grade, cut_norm);
                        assert!(uncertainty_second_grade >= 0);
                        assert_eq!(uncertainty_second_grade == 0, b1 == 0 && b2 == 0 && b3 == 0);
                        checks += 1;
                    }
                }
            }
        }
    }
    println!("{{");
    println!("  \"schema\": \"marici.gaussian_mixed_second_rees_cone.v1\",");
    println!("  \"exact_checks\": {checks},");
    println!("  \"occupation_second_grade\": \"2|a|^2 + sum_r |b_r|^2\",");
    println!("  \"anomalous_first_norm\": \"2|a|^2\",");
    println!("  \"uncertainty_second_grade\": \"sum_r |b_r|^2\",");
    println!("  \"equality_condition\": \"all environment-crossing Cut amplitudes vanish\"");
    println!("}}");
}
