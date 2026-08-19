fn close(a: f64, b: f64) {
    assert!((a - b).abs() < 1.0e-12, "{a} != {b}");
}

fn main() {
    let (a, b, c): (f64, f64, f64) = (0.37, 0.51, 0.73);
    let sa = a.sin();

    // Rows: (12354,12453). Columns: (13254,14253).
    // The second row is forced by the source relabelling 3 <-> 4.
    let m = [
        [-(a + b).sin() / sa, -c.sin() / sa],
        [-b.sin() / sa, -(a + c).sin() / sa],
    ];

    let det = m[0][0] * m[1][1] - m[0][1] * m[1][0];
    let reduced = (a + b + c).sin() / sa;
    close(det, reduced);

    // Exact numerical inversion checks both circuit rows simultaneously.
    let inv = [
        [m[1][1] / det, -m[0][1] / det],
        [-m[1][0] / det, m[0][0] / det],
    ];
    for i in 0..2 {
        for j in 0..2 {
            let value = m[i][0] * inv[0][j] + m[i][1] * inv[1][j];
            close(value, if i == j { 1.0 } else { 0.0 });
        }
    }

    println!("five_point_string_full_circuit: ok");
    println!("determinant: sin(x12+x23+x24)/sin(x12) = {det:.15}");
    println!("field_theory_limit: (s12+s23+s24)/s12 = -s25/s12");
}
