// Exact failure of the deletion-Euler response to descend through route summation.

fn ordinary(pair: [i128; 2]) -> i128 {
    pair[0] + pair[1]
}

fn graded(pair: [i128; 2]) -> i128 {
    2 * pair[0] + 3 * pair[1]
}

fn main() {
    let base = [40_i128, -40];
    assert_eq!(ordinary(base), 0);
    assert_eq!(graded(base), -40);

    for k in -32_i128..=32 {
        let redistributed = [base[0] + k, base[1] - k];
        assert_eq!(ordinary(redistributed), ordinary(base));
        assert_eq!(graded(redistributed), graded(base) - k);
    }

    println!(
        "{{\"status\":\"pass\",\"route_redistribution\":\"(A,B)->(A+K,B-K)\",\"ordinary_readout_invariant\":true,\"graded_response_shift\":\"-K\",\"response_determined_by_ungraded_correlator\":false,\"retained_route_presentation_required\":true}}"
    );
}
