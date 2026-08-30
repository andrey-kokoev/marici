// Exact audit of source-defined dashed-edge ports into the common readout.

fn f(x: [i128; 3]) -> i128 {
    x[0] * x[0] * x[1] + 3 * x[1] * x[2] + x[2] * x[2] * x[2]
}

// Edge labels: 0=12, 1=23, 2=31.
fn translate(mut x: [i128; 3], edge: usize, y: i128) -> [i128; 3] {
    let endpoints = [(0, 1), (1, 2), (2, 0)];
    let (a, b) = endpoints[edge];
    x[a] += y;
    x[b] += y;
    x
}

fn apply_order(x: [i128; 3], ys: [i128; 3], order: &[usize]) -> (i128, i128) {
    let mut shifted = x;
    let mut denominator = 1;
    for &edge in order {
        shifted = translate(shifted, edge, ys[edge]);
        denominator *= ys[edge];
    }
    (f(shifted), denominator)
}

fn main() {
    let samples = [
        ([2_i128, 3, 5], [7_i128, 11, 13]),
        ([-4, 7, 3], [5, 13, 17]),
        ([11, -2, 13], [17, 19, 23]),
    ];
    let cyclic_pairs = [(0_usize, 1_usize), (1, 2), (2, 0)];
    let triple_orders = [[0_usize, 1_usize, 2_usize], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]];

    for (x, ys) in samples {
        for (a, b) in cyclic_pairs {
            assert_eq!(apply_order(x, ys, &[a, b]), apply_order(x, ys, &[b, a]));
        }
        let reference = apply_order(x, ys, &triple_orders[0]);
        for order in triple_orders {
            assert_eq!(apply_order(x, ys, &order), reference);
        }
    }

    println!("{{\"status\":\"pass\",\"samples\":3,\"cyclic_pairs\":3,\"triple_orders\":6,\"port_commutators\":0,\"variance\":\"sector_to_common_readout\"}}");
}
