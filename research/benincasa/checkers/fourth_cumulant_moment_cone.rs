fn det2(a: i64, b: i64, c: i64) -> i64 {
    a * c - b * b
}

fn det3(m: [[i64; 3]; 3]) -> i64 {
    m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
        - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
        + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0])
}

fn audit(name: &str, mu2: i64, mu4: i64, mu6: i64, mu8: i64) -> i64 {
    let m = [[1, mu2, mu4], [mu2, mu4, mu6], [mu4, mu6, mu8]];
    assert!(m[0][0] >= 0 && m[1][1] >= 0 && m[2][2] >= 0);
    assert!(det2(m[0][0], m[0][1], m[1][1]) >= 0);
    assert!(det2(m[0][0], m[0][2], m[2][2]) >= 0);
    assert!(det2(m[1][1], m[1][2], m[2][2]) >= 0);
    assert!(det3(m) >= 0);
    let kappa4 = mu4 - 3 * mu2 * mu2;
    println!("{name}_kappa4={kappa4}");
    println!("{name}_moment_det={}", det3(m));
    kappa4
}

fn main() {
    // Symmetric two-point distribution q=+/-1.
    let negative = audit("two_point", 1, 1, 1, 1);
    // Distribution P(0)=3/4, P(+/-2)=1/8 each.
    let positive = audit("sparse_three_point", 1, 4, 16, 64);
    assert!(negative < 0);
    assert!(positive > 0);

    println!("{{");
    println!("  \"schema\": \"marici.fourth_cumulant_moment_cone.v1\",");
    println!("  \"fixed_variance\": 1,");
    println!("  \"negative_physical_kappa4\": {negative},");
    println!("  \"positive_physical_kappa4\": {positive},");
    println!("  \"moment_basis\": [\"1\",\"q^2\",\"q^4\"],");
    println!("  \"moment_matrices_psd\": true,");
    println!("  \"kappa4_sign_is_physicality_test\": false");
    println!("}}");
}
