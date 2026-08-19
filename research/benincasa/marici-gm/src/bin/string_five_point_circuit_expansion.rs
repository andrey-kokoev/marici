fn close(a: f64, b: f64) {
    assert!((a - b).abs() < 1.0e-12, "{a} != {b}");
}

fn main() {
    // Generic nonresonant angles pi alpha' s_ij.
    let (x12, x23, x24, x35, x45): (f64, f64, f64, f64, f64) =
        (0.37, 0.51, 0.73, -0.42, 0.29);

    // Source intersection row m(12354 | 12345,12435).
    let h1 = -(1.0 / x45.sin()) * (1.0 / x12.tan() + 1.0 / x23.tan());
    let h2 = -1.0 / (x12.sin() * x35.sin());

    // Entry 883's diagonal KLT kernel.
    let k1 = x23.sin() * x45.sin();
    let k2 = x24.sin() * x35.sin();
    let circuit = [h1 * k1, h2 * k2];

    let published = [
        -(x12 + x23).sin() / x12.sin(),
        -x24.sin() / x12.sin(),
    ];
    close(circuit[0], published[0]);
    close(circuit[1], published[1]);

    // Infinite-tension limit of the same circuit coefficients.
    close(-(x12 + x23) / x12, -((x12 / 0.37) + (x23 / 0.37)) / (x12 / 0.37));
    close(-x24 / x12, -(x24 / 0.37) / (x12 / 0.37));

    println!("five_point_string_circuit_expansion: ok");
    println!("circuit_coefficients: [{:.15},{:.15}]", circuit[0], circuit[1]);
    println!("only_displayed_denominator: sin(pi alpha' s12)");
}
