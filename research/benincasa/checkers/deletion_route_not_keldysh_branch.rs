// Exact label-typing audit: deletion route and SK branch are independent C2 actions.

fn route_swap(i: (u8, u8)) -> (u8, u8) {
    (1 - i.0, i.1)
}

fn branch_swap(i: (u8, u8)) -> (u8, u8) {
    (i.0, 1 - i.1)
}

fn main() {
    let labels = [(0_u8, 0_u8), (0, 1), (1, 0), (1, 1)];
    for x in labels {
        assert_eq!(route_swap(branch_swap(x)), branch_swap(route_swap(x)));
        assert_eq!(route_swap(route_swap(x)), x);
        assert_eq!(branch_swap(branch_swap(x)), x);
    }

    // Identifying route with branch retains only the diagonal and discards
    // two legitimate independently labelled occurrences.
    let diagonal_count = labels.iter().filter(|(r, b)| r == b).count();
    assert_eq!(diagonal_count, 2);
    assert_eq!(labels.len(), 4);

    println!(
        "{{\"status\":\"pass\",\"route_labels\":[\"grade2\",\"grade3\"],\"branch_labels\":[\"plus\",\"minus\"],\"combined_occurrences\":4,\"independent_C2_actions_commute\":true,\"identification_retains\":2,\"identification_discards\":2,\"route_branch_identification_typed\":false}}"
    );
}
