fn det3(m: [[f64; 3]; 3]) -> f64 {
    m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
        - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
        + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0])
}

fn main() {
    let mut maximum_defect = 0.0_f64;
    for j in 0..64 {
        let theta = 0.137 * j as f64;
        let (s, c) = theta.sin_cos();
        // Columns: Re beta, Im beta, statistical occupation.
        // Rows: delta<qq>, delta<pp>, delta<{q,p}/2>, after harmless
        // oscillator-frequency rescalings.
        let projection = [[c, -s, 1.0], [-c, s, 1.0], [s, c, 0.0]];
        maximum_defect = maximum_defect.max((det3(projection) + 2.0).abs());
    }
    assert!(maximum_defect < 2e-14);
    println!("{{");
    println!("  \"schema\": \"marici.gaussian_phase_space_jet_projection.v1\",");
    println!("  \"equal_time_value_rank\": 1,");
    println!("  \"phase_space_first_jet_rank\": 3,");
    println!("  \"projection_determinant\": \"-2\",");
    println!("  \"time_samples\": 64,");
    println!("  \"maximum_identity_defect\": {:.17e},", maximum_defect);
    println!("  \"marked_initial_slice_makes_projection_canonical\": true");
    println!("}}");
}
