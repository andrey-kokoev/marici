//! Scoped incidence falsifier for the naive two-sheet P2 pair-vertex lift.

use std::collections::VecDeque;

fn components(adjacency: &[Vec<usize>]) -> usize {
    let mut seen = vec![false; adjacency.len()];
    let mut count = 0;
    for start in 0..adjacency.len() {
        if seen[start] {
            continue;
        }
        count += 1;
        seen[start] = true;
        let mut queue = VecDeque::from([start]);
        while let Some(vertex) = queue.pop_front() {
            for &next in &adjacency[vertex] {
                if !seen[next] {
                    seen[next] = true;
                    queue.push_back(next);
                }
            }
        }
    }
    count
}

fn main() {
    // Two normalization sheets, each with the P2 coordinate-boundary triangle.
    let mut p2 = vec![Vec::new(); 6];
    for sheet in 0..2 {
        for axis in 0..3 {
            let left = 3 * sheet + axis;
            let right = 3 * sheet + (axis + 1) % 3;
            p2[left].push(right);
            p2[right].push(left);
        }
    }
    assert!(p2.iter().all(|neighbors| neighbors.len() == 2));
    assert_eq!(components(&p2), 2);

    // Literal cross-sheet corridors: (i,sigma) is joined to (j,-sigma)
    // exactly when i != j.  Encode + as 0..2 and - as 3..5.
    let mut literal = vec![Vec::new(); 6];
    let mut edges = 0;
    for plus_axis in 0..3 {
        for minus_axis in 0..3 {
            if plus_axis == minus_axis {
                continue;
            }
            let plus = plus_axis;
            let minus = 3 + minus_axis;
            literal[plus].push(minus);
            literal[minus].push(plus);
            edges += 1;
        }
    }
    assert_eq!(edges, 6);
    assert!(literal.iter().all(|neighbors| neighbors.len() == 2));
    assert_eq!(components(&literal), 1);

    // Connected-component count is invariant under every graph isomorphism.
    let incidence_preserving_bijection_exists = components(&p2) == components(&literal);
    assert!(!incidence_preserving_bijection_exists);

    // D3 rotation preserves axes and reflection exchanges the two signs.
    for axis in 0..3 {
        assert!(literal[axis].contains(&(3 + (axis + 1) % 3)));
        assert!(literal[(axis + 1) % 3].contains(&(3 + axis)));
    }

    println!(
        "{{\"status\":\"falsified_scoped_naive_two_sheet_P2_pair_vertex_lift\",\"P2_vertices\":6,\"P2_components\":2,\"P2_graph\":\"C3_disjoint_C3\",\"literal_corridors\":6,\"literal_components\":1,\"literal_graph\":\"C6\",\"incidence_preserving_bijection\":false,\"earliest_obstruction\":\"connectedness_before_sign_Tor_Cech\",\"minimal_repair\":\"connected_hexagonal_or_prismatic_conductor_carrier_plus_independent_odd_relative_interior\",\"physical_mapping_fiber\":\"unconstructed\"}}"
    );
}
