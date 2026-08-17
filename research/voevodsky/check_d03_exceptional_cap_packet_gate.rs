//! Rank, degree, and support gate for Entry 176 versus Entry 369.

use std::collections::BTreeSet;

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
enum Support {
    Center,
    X3Branch,
    X4Branch,
}

fn rank_mod_prime(mut matrix: Vec<Vec<i64>>, prime: i64) -> usize {
    if matrix.is_empty() || matrix[0].is_empty() {
        return 0;
    }
    let rows = matrix.len();
    let columns = matrix[0].len();
    let mut rank = 0;
    for column in 0..columns {
        let Some(pivot) = (rank..rows).find(|row| matrix[*row][column].rem_euclid(prime) != 0)
        else {
            continue;
        };
        matrix.swap(rank, pivot);
        let value = matrix[rank][column].rem_euclid(prime);
        let inverse = (1..prime)
            .find(|candidate| candidate * value % prime == 1)
            .unwrap();
        for entry in &mut matrix[rank] {
            *entry = entry.rem_euclid(prime) * inverse % prime;
        }
        for row in 0..rows {
            if row == rank {
                continue;
            }
            let factor = matrix[row][column].rem_euclid(prime);
            for entry in column..columns {
                matrix[row][entry] =
                    (matrix[row][entry] - factor * matrix[rank][entry]).rem_euclid(prime);
            }
        }
        rank += 1;
    }
    rank
}

fn main() {
    // Entry 369: two degree-zero branch classes and one degree-one center
    // class.  Entry 176 is local to the x3 road and has degree -1.
    let degree_zero = [Support::X3Branch, Support::X4Branch];
    let degree_one = [Support::Center];
    let literal_cap_support = BTreeSet::from([Support::X3Branch, Support::Center]);
    assert!(!literal_cap_support.contains(&Support::X4Branch));

    // The strongest differential allowed by the literal support is
    // [unit, 0]: X3Branch + X4Branch -> Center.  Its cone/homology still has
    // the x4 line.  Signs and nonzero unit choices do not change this rank.
    let strongest_literal_differential = vec![vec![1_i64, 0_i64]];
    let literal_rank = rank_mod_prime(strongest_literal_differential, 101);
    let literal_h0_rank = degree_zero.len() - literal_rank;
    let literal_h1_rank = degree_one.len() - literal_rank;
    assert_eq!((literal_h0_rank, literal_h1_rank), (1, 0));

    // After the nonphysical x4 branch is removed, a primitive x3-to-center
    // coefficient would make the remaining two-term packet acyclic.  Entry
    // 176 proves primitive k=1 in its labelled relative model, but does not
    // yet type this coefficient as the localization-dual module map below.
    let physical_quotient_differential = vec![vec![1_i64]];
    let quotient_rank = rank_mod_prime(physical_quotient_differential, 101);
    assert_eq!((1 - quotient_rank, 1 - quotient_rank), (0, 0));

    println!(
        "{{\"claim\":\"The literal Entry-176 x3-supported rank-one cap cannot kill the full three-class exceptional obstruction packet; after quotienting the nonphysical x4 branch, a primitive x3-to-center map would be rank-compatible with an acyclic cone, but the required localization-dual module map remains unconstructed\",\"status\":\"literal_cap_insufficient_reduced_gate_open\",\"packet_ranks_degree_0_1\":[2,1],\"literal_cap_support\":[\"center\",\"x3_branch\"],\"unsupported_survivor\":\"x4_branch\",\"literal_cone_homology_ranks_degree_0_1\":[{literal_h0_rank},{literal_h1_rank}],\"after_x4_quotient_unit_map_homology_ranks_degree_0_1\":[0,0],\"missing\":\"support-typed map on multi-localization dual coefficients\"}}"
    );
}
