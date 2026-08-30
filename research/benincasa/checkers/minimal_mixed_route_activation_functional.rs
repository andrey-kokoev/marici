// Exact quotient of 2x2 mixed route operators visible on p=(1,-1).

fn activation(h: [[i128; 2]; 2]) -> i128 {
    h[0][0] - h[0][1] + h[1][0] - h[1][1]
}

fn swap_conjugate(h: [[i128; 2]; 2]) -> [[i128; 2]; 2] {
    [[h[1][1], h[1][0]], [h[0][1], h[0][0]]]
}

fn main() {
    let kernel_basis = [
        [[1_i128, 1], [0, 0]],
        [[0, 0], [1, 1]],
        [[1, 0], [-1, 0]],
    ];
    for h in kernel_basis {
        assert_eq!(activation(h), 0);
    }

    let witness = [[1_i128, 0], [0, 0]];
    assert_eq!(activation(witness), 1);
    assert_eq!(activation(swap_conjugate(witness)), -1);

    println!(
        "{{\"status\":\"pass\",\"operator_space_dimension\":4,\"invisible_kernel_dimension\":3,\"activation_quotient_dimension\":1,\"functional\":\"h11-h12+h21-h22\",\"route_swap_character\":-1,\"orientation_required\":true}}"
    );
}
