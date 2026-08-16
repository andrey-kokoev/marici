//! Canonical augmented SNC/Tate can-var carrier bridge.
//!
//! The projective-conductor SNC incidence complex
//!
//!   Z_or --N--> P_facet --(R-I)--> P_pair --epsilon--> Z
//!
//! and entry113's integral Tate carrier
//!
//!   Z_or --N--> P_tag --(I-R)--> P_road --epsilon--> Z
//!
//! are canonically isomorphic after the forced orientation changes
//! F=(+1,+I,-I,-1).  The bridge is integral, exact, D3-equivariant, and
//! unimodular.  It identifies the two endpoint weight lines and the A2 middle
//! extension without a 1/3 splitting.
//!
//! This is a coefficient/log carrier theorem.  It does not realize the
//! bridge as a nearby-cycle six-functor morphism, does not identify the pair
//! strata with literal entry143 costalks, and derives none of the 24 rows.

type Int = i64;
type Matrix = Vec<Vec<Int>>;

fn multiply(a: &Matrix, b: &Matrix) -> Matrix {
    assert!(!a.is_empty() && !b.is_empty());
    assert_eq!(a[0].len(), b.len());
    (0..a.len())
        .map(|i| {
            (0..b[0].len())
                .map(|j| (0..b.len()).map(|k| a[i][k] * b[k][j]).sum())
                .collect()
        })
        .collect()
}

fn apply(a: &Matrix, v: &[Int]) -> Vec<Int> {
    a.iter()
        .map(|row| row.iter().zip(v).map(|(x, y)| x * y).sum())
        .collect()
}

fn transpose(a: &Matrix) -> Matrix {
    (0..a[0].len())
        .map(|j| (0..a.len()).map(|i| a[i][j]).collect())
        .collect()
}

fn determinant_2(a: &Matrix, rows: [usize; 2], cols: [usize; 2]) -> Int {
    a[rows[0]][cols[0]] * a[rows[1]][cols[1]] - a[rows[0]][cols[1]] * a[rows[1]][cols[0]]
}

fn rank_3(a: &Matrix) -> usize {
    assert_eq!(a.len(), 3);
    assert_eq!(a[0].len(), 3);
    let det = a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
        - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
        + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0]);
    if det != 0 {
        return 3;
    }
    for i in 0..3 {
        for j in i + 1..3 {
            for k in 0..3 {
                for l in k + 1..3 {
                    if determinant_2(a, [i, j], [k, l]) != 0 {
                        return 2;
                    }
                }
            }
        }
    }
    usize::from(a.iter().flatten().any(|x| *x != 0))
}

fn unit_rank_two_minor(a: &Matrix) -> bool {
    (0..3).any(|i| {
        (i + 1..3).any(|j| {
            (0..3).any(|k| (k + 1..3).any(|l| determinant_2(a, [i, j], [k, l]).abs() == 1))
        })
    })
}

fn identity(n: usize) -> Matrix {
    (0..n)
        .map(|i| (0..n).map(|j| Int::from(i == j)).collect())
        .collect()
}

fn scalar(value: Int) -> Matrix {
    vec![vec![value]]
}

fn negate(a: &Matrix) -> Matrix {
    a.iter()
        .map(|row| row.iter().map(|value| -*value).collect())
        .collect()
}

fn main() {
    // Physical cyclic order (14,03,25).
    let rotation = vec![vec![0, 0, 1], vec![1, 0, 0], vec![0, 1, 0]];
    let rotation_inverse = transpose(&rotation);
    let reflection = vec![vec![1, 0, 0], vec![0, 0, 1], vec![0, 1, 0]];
    let i3 = identity(3);
    let n = vec![vec![1], vec![1], vec![1]];
    let epsilon = vec![vec![1, 1, 1]];
    let source_middle = (0..3)
        .map(|i| (0..3).map(|j| rotation[i][j] - i3[i][j]).collect())
        .collect::<Matrix>();
    let target_middle = negate(&source_middle);

    assert_eq!(multiply(&rotation, &rotation_inverse), i3);
    assert_eq!(multiply(&reflection, &reflection), i3);
    assert_eq!(
        multiply(&multiply(&reflection, &rotation), &reflection),
        rotation_inverse
    );

    // Both augmented complexes square to zero.
    assert_eq!(
        multiply(&source_middle, &n),
        vec![vec![0], vec![0], vec![0]]
    );
    assert_eq!(multiply(&epsilon, &source_middle), vec![vec![0, 0, 0]]);
    assert_eq!(
        multiply(&target_middle, &n),
        vec![vec![0], vec![0], vec![0]]
    );
    assert_eq!(multiply(&epsilon, &target_middle), vec![vec![0, 0, 0]]);

    // Exactness and integral saturation.
    assert_eq!(rank_3(&source_middle), 2);
    assert!(unit_rank_two_minor(&source_middle));
    assert_eq!(apply(&source_middle, &[1, 1, 1]), vec![0, 0, 0]);
    assert_eq!(apply(&epsilon, &[1, -1, 0]), vec![0]);
    assert_eq!(apply(&epsilon, &[0, 1, -1]), vec![0]);
    let image_a = apply(&source_middle, &[1, 0, 0]);
    let image_b = apply(&source_middle, &[0, 1, 0]);
    assert_eq!(apply(&epsilon, &image_a), vec![0]);
    assert_eq!(apply(&epsilon, &image_b), vec![0]);
    let middle_smith = [1_i64, 1];
    let top_smith = [1_i64];
    let augmentation_smith = [1_i64];

    // Forced bridge signs: facets/tags agree, pairs/roads and bottom
    // augmentation reverse.  Every component is unimodular.
    let f3 = scalar(1);
    let f2 = i3.clone();
    let f1 = negate(&i3);
    let f0 = scalar(-1);

    assert_eq!(multiply(&f2, &n), multiply(&n, &f3));
    assert_eq!(multiply(&f1, &source_middle), multiply(&target_middle, &f2));
    assert_eq!(multiply(&f0, &epsilon), multiply(&epsilon, &f1));

    // Signed D3 action from the projective SNC orientation conventions.
    let source_reflection_3 = scalar(-1);
    let source_reflection_2 = negate(&reflection);
    let source_reflection_1 = multiply(&reflection, &rotation_inverse);
    let source_reflection_0 = scalar(1);

    assert_eq!(
        multiply(&source_reflection_2, &n),
        multiply(&n, &source_reflection_3)
    );
    assert_eq!(
        multiply(&source_reflection_1, &source_middle),
        multiply(&source_middle, &source_reflection_2)
    );
    assert_eq!(
        multiply(&source_reflection_0, &epsilon),
        multiply(&epsilon, &source_reflection_1)
    );

    // The target actions transported through F are the same signed matrices,
    // and the bridge commutes with rotation and reflection in every degree.
    let actions_rotation = [scalar(1), rotation.clone(), rotation.clone(), scalar(1)];
    let actions_reflection = [
        source_reflection_3,
        source_reflection_2,
        source_reflection_1,
        source_reflection_0,
    ];
    let bridge = [f3, f2, f1, f0];
    for (f, action) in bridge.iter().zip(&actions_rotation) {
        assert_eq!(multiply(f, action), multiply(action, f));
    }
    for (f, action) in bridge.iter().zip(&actions_reflection) {
        assert_eq!(multiply(f, action), multiply(action, f));
    }

    // The norm remains integral: epsilon*N=3.  The bridge never introduces
    // the forbidden projector N*epsilon/3.
    assert_eq!(multiply(&epsilon, &n), vec![vec![3]]);
    let bridge_component_smith = [1_i64, 1, 1, 1];

    println!(
        "{}",
        format!(
            "{{\"claim\":\"The canonical augmented projective-conductor SNC complex is integrally and D3-equivariantly chain-isomorphic to entry113's N/(1-r)/epsilon Tate carrier through the forced unimodular signs (+1,+I,-I,-1).  The complex is exact and saturated, retains epsilon*N=3, and supplies the coefficient/log two-endpoint can-var bridge without division by three.\",\"status\":\"proved_scoped_augmented_snc_tate_can_var_carrier_bridge\",\"source_differentials\":{{\"top\":\"N\",\"middle\":\"R-I\",\"bottom\":\"epsilon\"}},\"target_differentials\":{{\"top\":\"N\",\"middle\":\"I-R\",\"bottom\":\"epsilon\"}},\"bridge_signs\":[1,1,-1,-1],\"bridge_component_smith\":{:?},\"middle_rank\":2,\"middle_smith\":{:?},\"top_smith\":{:?},\"augmentation_smith\":{:?},\"complex_exact\":true,\"d3_equivariant\":true,\"reflection_equivariant\":true,\"epsilon_times_norm\":3,\"division_by_three\":false,\"spatial_nearby_cycle_realization\":\"unconstructed\",\"discrepancy_two_top_assignment\":\"unconstructed\",\"primitive_qSigma_mixed_assignment\":\"unconstructed\",\"literal_entry143_rows_constructed\":0,\"pairwise_log_gysin_correspondences\":\"unconstructed\",\"endpoint_q_mapping_fiber\":\"unconstructed\",\"minimal_next_map\":\"Lift this forced augmented-chain isomorphism to a normalization/conductor nearby-cycle and excess-Gysin morphism, then identify its three pair generators with literal entry143 q_k corridors and derive the 24 corestriction rows.\"}}",
            bridge_component_smith,
            middle_smith,
            top_smith,
            augmentation_smith
        )
    );
}
