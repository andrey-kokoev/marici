type V = [i64; 3]; // coefficients of (I0, I2, I4)

fn add(a: V, b: V) -> V {
    [a[0] + b[0], a[1] + b[1], a[2] + b[2]]
}
fn scale(q: i64, a: V) -> V {
    [q * a[0], q * a[1], q * a[2]]
}

fn main() {
    // All coefficients are multiplied by four relative to the common
    // A H^4/(256 epsilon^2 M^4 p^3) normalization.
    let x_c1: V = [-1, 3, -5];
    let y_c2: V = [1, 1, -5];

    let constant = add(add(add([4, 0, 0], x_c1), scale(-3, y_c2)), [0, 0, -10]);
    let eta2 = add(add(add([0, 4, 0], scale(-1, x_c1)), scale(-1, y_c2)), [0, 0, -10]);
    let eta4 = add([0, 0, 4], [0, 0, -4]);

    assert_eq!(constant, [0, 0, 0]);
    assert_eq!(eta2, [0, 0, 0]);
    assert_eq!(eta4, [0, 0, 0]);

    println!("{{");
    println!("  \"schema\": \"marici.counterterm_label_contract.v1\",");
    println!("  \"forced_third_label\": \"c1\",");
    println!("  \"c1_integral_combination\": \"3*I2-5*I4-I0\",");
    println!("  \"c2_integral_combination\": \"I0+I2-5*I4\",");
    println!("  \"c3_integral_combination\": \"I4\",");
    println!("  \"constant_cancellation\": true,");
    println!("  \"eta2_cancellation\": true,");
    println!("  \"eta4_cancellation\": true");
    println!("}}");
}

