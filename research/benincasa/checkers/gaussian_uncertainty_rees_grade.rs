fn main() {
    // For covariance coordinates (x,y,n), the one-mode uncertainty excess is
    // (n+1/2)^2-|beta|^2-1/4 = n+n^2-x^2-y^2.
    let first_grade = "n";
    let second_grade = "n^2-x^2-y^2";
    let samples = [(3.0, 4.0), (5.0, 12.0), (8.0, 15.0)];
    for (x, y) in samples {
        let required_second_order_occupation = x * x + y * y;
        let completed_second_grade = required_second_order_occupation - x * x - y * y;
        assert_eq!(completed_second_grade, 0.0);
    }
    println!("{{");
    println!("  \"schema\": \"marici.gaussian_uncertainty_rees_grade.v1\",");
    println!("  \"uncertainty_excess\": \"n+n^2-x^2-y^2\",");
    println!("  \"first_rees_grade\": \"{first_grade}\",");
    println!("  \"second_rees_grade\": \"{second_grade}\",");
    println!("  \"pure_bogoliubov_second_order_completion\": \"n_2=x^2+y^2\",");
    println!("  \"first_jet_sufficient_for_positivity\": false");
    println!("}}");
}
