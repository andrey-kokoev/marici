use serde_json::json;
use std::fs;

fn dot(left: &[i64; 3], right: &[i64; 3]) -> i64 {
    (0..3).map(|i| left[i] * right[i]).sum()
}

fn det3(matrix: &[[i64; 3]; 3]) -> i64 {
    matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
}

fn next_permutation(values: &mut [usize]) -> bool {
    let Some(i) = (0..values.len() - 1).rev().find(|&i| values[i] < values[i + 1]) else {
        return false;
    };
    let j = (i + 1..values.len()).rev().find(|&j| values[i] < values[j]).unwrap();
    values.swap(i, j);
    values[i + 1..].reverse();
    true
}

fn main() {
    let p = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [1, 2, 3],
        [-2, -3, -4],
    ];
    let sum = (0..3).map(|i| p.iter().map(|v| v[i]).sum::<i64>()).collect::<Vec<_>>();
    assert_eq!(sum, vec![0, 0, 0]);

    let gram = (0..5)
        .map(|i| (0..5).map(|j| dot(&p[i], &p[j])).collect::<Vec<_>>())
        .collect::<Vec<_>>();
    let q = [
        p[0],
        [p[0][0] + p[1][0], p[0][1] + p[1][1], p[0][2] + p[1][2]],
        [p[0][0] + p[1][0] + p[2][0], p[0][1] + p[1][1] + p[2][1], p[0][2] + p[1][2] + p[2][2]],
    ];
    let h = [
        [dot(&q[0], &q[0]), dot(&q[0], &q[1]), dot(&q[0], &q[2])],
        [dot(&q[1], &q[0]), dot(&q[1], &q[1]), dot(&q[1], &q[2])],
        [dot(&q[2], &q[0]), dot(&q[2], &q[1]), dot(&q[2], &q[2])],
    ];
    assert_eq!(det3(&h), 1);

    let mut permutation = [0, 1, 2, 3, 4];
    let mut stabilizer = Vec::new();
    loop {
        if (0..5).all(|i| (0..5).all(|j| gram[i][j] == gram[permutation[i]][permutation[j]])) {
            stabilizer.push(permutation.to_vec());
        }
        if !next_permutation(&mut permutation) {
            break;
        }
    }
    assert_eq!(stabilizer, vec![vec![0, 1, 2, 3, 4]]);

    let packet = json!({
        "schema":"marici.benincasa.five_site.asymmetric_physical_slice.v1",
        "spatial_resultants":p,
        "momentum_conservation":sum,
        "point_gram":gram,
        "point_gram_rank":3,
        "routing_basis":["q1=P1","q2=P1+P2","q3=P1+P2+P3"],
        "routing_gram":h,
        "routing_gram_determinant":1,
        "q4_coordinates_in_routing_basis":[-1,-1,4],
        "site_energies":"X_1=...=X_5=t",
        "physical_real_domain":"t>=sqrt(29)",
        "realizability":"each Xi>=|Pi|; add an opposite transverse pair at each site without changing Pi",
        "permutation_stabilizer":stabilizer,
        "residual_label_symmetry":"identity only",
        "complex_parameter":"t",
        "total_energy":"E_T=5t",
        "frozen_before_landau_or_period_evaluation":true
    });
    fs::write(
        "../results/five-site-asymmetric-physical-slice.json",
        serde_json::to_string_pretty(&packet).unwrap() + "\n",
    )
    .unwrap();
    println!("{}", serde_json::to_string(&packet).unwrap());
}
