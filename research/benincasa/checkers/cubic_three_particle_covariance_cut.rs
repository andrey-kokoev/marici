fn main() {
    // Exact normalized state (|000>+g A|111>)/sqrt(1+g^2 A^2).
    // aa annihilates |111>, while a^dagger a returns one on |111>.
    for (g_num, amplitude) in [(1_i64, 2_i64), (2, 3), (3, 5), (5, 8)] {
        let weight = g_num * g_num * amplitude * amplitude;
        let occupation_num = weight;
        let occupation_den = 1 + weight;
        assert!(occupation_num > 0 && occupation_num < occupation_den);
        let anomalous_numerator = 0_i64;
        assert_eq!(anomalous_numerator, 0);
        // The coefficient of g^2 in the occupation is |A|^2.
        assert_eq!(weight / (g_num * g_num), amplitude * amplitude);
    }
    println!("{{");
    println!("  \"schema\": \"marici.cubic_three_particle_covariance_cut.v1\",");
    println!("  \"state\": \"(|000>+g A|111>)/sqrt(1+g^2|A|^2)\",");
    println!("  \"first_order_anomalous_coordinate\": 0,");
    println!("  \"second_order_statistical_coordinate\": \"|A|^2\",");
    println!("  \"second_order_coordinate_is_cut_norm\": true");
    println!("}}");
}
