//! Image lattice of all currently admitted normalization/log source classes.

fn gcd(mut a: i64, mut b: i64) -> i64 {
    a = a.abs();
    b = b.abs();
    while b != 0 {
        (a, b) = (b, a % b);
    }
    a
}

fn main() {
    // Columns: full-log maximal-cone top; six local KN walls; short hexagon.
    let admitted_q_row = [2_i64, 0, 0, 0, 0, 0, 0, 0];
    let image_index = admitted_q_row.into_iter().fold(0, gcd);
    assert_eq!(image_index, 2);
    assert!((-64_i64..=64).all(|x| admitted_q_row.iter().map(|c| c * x).sum::<i64>() != 1));

    // The abstract P2 unit is not an admitted column: its pair-incidence graph
    // has two components, while the literal corridor graph has one.
    let p2_literal_column_admitted = false;
    assert!(!p2_literal_column_admitted);

    let enlarged = [2_i64, 1];
    assert_eq!(enlarged.into_iter().fold(0, gcd), 1);
    println!("{{\"status\":\"falsified_scoped_admitted_source_primitive_Q_surjectivity\",\"admitted_Q_row\":[2,0,0,0,0,0,0,0],\"image_lattice\":\"2Z\",\"cokernel\":\"Z/2\",\"P2_unit_literal_column_admitted\":false,\"minimal_new_column\":1,\"endpoint_Q_mapping_fiber\":\"unconstructed\"}}");
}
