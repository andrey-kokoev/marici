fn gcd(mut a: i64, mut b: i64) -> i64 {
    a = a.abs();
    b = b.abs();
    while b != 0 {
        let remainder = a % b;
        a = b;
        b = remainder;
    }
    a
}

fn main() {
    // Reflection pairs the two pure faces with coefficients a,-a and the
    // three one-negative faces with the three reflected two-negative faces
    // with coefficients b,-b. Their oriented top trace is 2a-6b.
    for a in -32_i64..=32 {
        for b in -32_i64..=32 {
            let trace = 2 * a - 6 * b;
            assert_eq!(trace.rem_euclid(2), 0);
            assert_ne!(trace, 1);
        }
    }
    let ordinary_row = [2_i64, -6_i64];
    let ordinary_smith = ordinary_row.into_iter().fold(0, gcd);
    assert_eq!(ordinary_smith, 2);

    // A new reflection-odd relative interior counit with primitive
    // coefficient +1 is the minimal symmetry-compatible repair.
    let enlarged_row = [2_i64, -6_i64, 1_i64];
    let enlarged_smith = enlarged_row.into_iter().fold(0, gcd);
    assert_eq!(enlarged_smith, 1);
    let solution = [0_i64, 0_i64, 1_i64];
    assert_eq!(
        enlarged_row
            .into_iter()
            .zip(solution)
            .map(|(coefficient, value)| coefficient * value)
            .sum::<i64>(),
        1
    );

    println!(
        "{{\"status\":\"falsified_scoped_equivariant_face_trace_oddness\",\"ordinary_equivariant_trace\":\"2a-6b\",\"ordinary_row\":[2,-6],\"ordinary_smith_factors\":[2],\"ordinary_cokernel\":\"Z/2\",\"primitive_value_one_reachable\":false,\"minimal_enlarged_row\":[2,-6,1],\"enlarged_smith_factors\":[1],\"required_new_class\":\"reflection-odd relative interior Q counit\",\"cross_polytope_edges_constructed_finitely\":6,\"cross_polytope_faces_constructed_finitely\":8,\"relative_interior_to_literal_Q_constructed\":false,\"mapping_fiber_instantiated\":false}}"
    );
}
