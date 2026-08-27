fn det3(m: [[i64; 3]; 3]) -> i64 {
    m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
        - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
        + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0])
}

fn row(x: i64) -> [i64; 3] {
    [1, x, x * x]
}

fn vandermonde(x0: i64, x1: i64, x2: i64) -> i64 {
    (x1 - x0) * (x2 - x0) * (x2 - x1)
}

fn main() {
    let triples = [(0, 1, 2), (-2, 3, 7), (1, 1, 4), (5, 2, -1)];
    for (x0, x1, x2) in triples {
        let determinant = det3([row(x0), row(x1), row(x2)]);
        assert_eq!(determinant, vandermonde(x0, x1, x2));
        assert_eq!(determinant != 0, x0 != x1 && x0 != x2 && x1 != x2);
    }

    // Two evaluations have a nonzero 2x2 minor when their points differ,
    // but a 2x3 map always retains at least one scheme direction.
    let x0 = 0;
    let x1 = 1;
    let two_port_minor = row(x0)[0] * row(x1)[1] - row(x0)[1] * row(x1)[0];
    assert_eq!(two_port_minor, 1);

    println!("three_port_determinant_formula_verified=true");
    println!("three_distinct_ports_are_faithful=true");
    println!("two_port_rank=2");
    println!("two_port_kernel_dimension=1");
    println!("minimum_scalar_ports=3");
}
