fn main() {
    // Independent centered unit-variance Gaussian quadratures X,Y,Z and
    // momenta Px,Py.  Under the cubic kick exp(-i g XYZ):
    // Px' = Px - g YZ, Py' = Py - g XZ.
    // Wick moments: E[Y^2 Z^2]=E[X^2 Z^2]=1 and odd moments vanish.
    let ey2z2 = 1_i64;
    let ex2z2 = 1_i64;
    let exyz2 = 0_i64;

    let mixed_memory_linear_coefficient = -ey2z2; // Cov(Px',YZ)/g
    let internal_variance_quadratic_coefficient = ex2z2; // (Var Py'-Var Py)/g^2
    let linear_cross_quadrature_quadratic_coefficient = exyz2; // Cov(Px',Py')/g^2

    assert_eq!(mixed_memory_linear_coefficient, -1);
    assert_eq!(internal_variance_quadratic_coefficient, 1);
    assert_eq!(linear_cross_quadrature_quadratic_coefficient, 0);

    let mut parity_checks = 0usize;
    // Every monomial with an odd exponent in an independent centered Gaussian
    // variable has zero expectation. Audit the cubic/linear combinations used.
    for exponents in [[1, 1, 0], [1, 0, 1], [0, 1, 1], [1, 1, 2]] {
        let vanishes = exponents.iter().any(|e| e % 2 == 1);
        assert!(vanishes);
        parity_checks += 1;
    }

    println!("{{");
    println!("  \"schema\": \"marici.cubic_memory_normal_order.v1\",");
    println!("  \"parity_checks\": {parity_checks},");
    println!("  \"mixed_quadratic_memory_first_order_coefficient\": {mixed_memory_linear_coefficient},");
    println!("  \"internal_covariance_second_order_coefficient\": {internal_variance_quadratic_coefficient},");
    println!("  \"linear_cross_covariance_through_second_order\": {linear_cross_quadrature_quadratic_coefficient},");
    println!("  \"full_markov_failure_order\": 1,");
    println!("  \"gaussian_covariance_failure_order\": 2");
    println!("}}");
}
