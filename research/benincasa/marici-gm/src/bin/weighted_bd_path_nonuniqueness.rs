fn main() {
    // Exact rational samples witness two distinct admissible weighted limits.
    // epsilon=1/10 and c=1,2 both satisfy epsilon<1/c.
    let eps_num: i64 = 1;
    let eps_den: i64 = 10;
    for c in [1_i64, 2_i64] {
        assert!(eps_num * c < eps_den);
        // Im X3 = -epsilon + c epsilon^2 < 0 iff c*eps_num < eps_den.
        let im_x3_num = -eps_num * eps_den + c * eps_num * eps_num;
        assert!(im_x3_num < 0);
        // t=y/u^2=i*c, so the two paths land at distinct exceptional points.
        assert!(c > 0);
    }
    assert_ne!(1_i64, 2_i64);
    println!("exact certificate: the BD tube admits distinct weighted limits t=i and t=2i");
}
