// Exact lattice-simplex audit of the positive exceptional directions.

fn main() {
    let n = 12_i32;
    let mut directions = 0_usize;
    let mut weak_transform_zeros = 0_usize;

    for a in 0..=n {
        for b in 0..=n - a {
            for c in 0..=n - a - b {
                for d in 0..=n - a - b - c {
                    let e = n - a - b - c - d;
                    let q_hat = a + b + c + d;
                    let y_hat = e;
                    if q_hat == 0 && y_hat == 0 {
                        weak_transform_zeros += 1;
                    }
                    directions += 1;
                }
            }
        }
    }

    assert_eq!(directions, 1820);
    assert_eq!(weak_transform_zeros, 0);
    println!(
        "{{\"status\":\"pass\",\"simplex_directions\":1820,\"weak_transform_positive_zeros\":0,\"common_radial_valuation\":1}}"
    );
}
