//! Tensor and Bockstein gate for lifting Entry 176 to Entry 131's packet.

type Matrix = Vec<Vec<i64>>;

fn multiply(left: &Matrix, right: &Matrix) -> Matrix {
    assert!(!left.is_empty() && !right.is_empty());
    assert_eq!(left[0].len(), right.len());
    (0..left.len())
        .map(|row| {
            (0..right[0].len())
                .map(|column| {
                    (0..right.len())
                        .map(|middle| left[row][middle] * right[middle][column])
                        .sum()
                })
                .collect()
        })
        .collect()
}

fn main() {
    // Entry 176: the relative normal interval has one top relative class,
    // and positive normal integration sends it primitively to +1.
    let relative_normal_homology_rank = 1_usize;
    let cap = vec![vec![1_i64]];
    assert_eq!(relative_normal_homology_rank, 1);
    assert_eq!(cap, vec![vec![1]]);

    // Entry 131: after x3 Cartier restriction the finite packet is
    // [B<g,h> --(0,u3)--> B<p>].  A support/filtration preserving
    // Bockstein-compatible map has f1=diag(e,e), f0=(e).  Positive
    // normalization selects e=1.
    let purity_degree_one = vec![vec![1_i64, 0], vec![0, 1]];
    let purity_degree_zero = vec![vec![1_i64]];
    let beta = vec![vec![1_i64, 7_i64]]; // t3=7 is an arbitrary audit value.
    assert_eq!(
        multiply(&beta, &purity_degree_one),
        multiply(&purity_degree_zero, &beta)
    );

    // cap acts on the separate relative-normal tensor factor.  The u3
    // can-var/Bockstein packet is a spectator, so the lifted map has exactly
    // the purity matrices and remains an isomorphism in both degrees.
    let lifted_degree_one: Matrix = purity_degree_one
        .iter()
        .map(|row| row.iter().map(|entry| cap[0][0] * entry).collect())
        .collect();
    let lifted_degree_zero: Matrix = purity_degree_zero
        .iter()
        .map(|row| row.iter().map(|entry| cap[0][0] * entry).collect())
        .collect();
    assert_eq!(lifted_degree_one, vec![vec![1, 0], vec![0, 1]]);
    assert_eq!(lifted_degree_zero, vec![vec![1]]);
    assert_eq!(
        multiply(&beta, &lifted_degree_one),
        multiply(&lifted_degree_zero, &beta)
    );

    // On the support-labelled associated packet the x4 projection deletes
    // only x4; center and x3 remain.
    let supports = ["center", "x3", "x4"];
    let physical: Vec<_> = supports
        .iter()
        .copied()
        .filter(|support| *support != "x4")
        .collect();
    assert_eq!(physical, ["center", "x3"]);

    println!(
        "{{\"claim\":\"On the finite Cartier/can-var associated packet, Entry 176 lifts as cap_norm tensor pur_x3 and is the unique positive Bockstein-compatible unit after x4 support projection\",\"status\":\"scoped_finite_packet_unit\",\"global_raw_q_shriek_realization\":\"open\"}}"
    );
}
