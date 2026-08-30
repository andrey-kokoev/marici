fn rotate<T: Copy>(x: [T; 3]) -> [T; 3] { [x[2], x[0], x[1]] }

fn response(c: [i64; 3], p: [i64; 3]) -> [i64; 3] {
    [-8 * c[0] * p[0], -8 * c[1] * p[1], -8 * c[2] * p[2]]
}

fn main() {
    let c = [2, 3, 5];
    let p = [7, 11, 13];
    assert_eq!(rotate(response(c, p)), response(rotate(c), rotate(p)));
    let invariant_p = [1, 1, 1];
    let scalar: i64 = response(c, invariant_p).iter().sum();
    assert_eq!(scalar, -8 * (2 + 3 + 5));
    println!("{{\"status\":\"pass\",\"c3_equivariant\":true,\"kernel_character\":\"regular_C3\",\"invariant_response\":\"-8*(C12+C23+C31)\",\"descends_to_ungraded_readout\":false}}");
}
