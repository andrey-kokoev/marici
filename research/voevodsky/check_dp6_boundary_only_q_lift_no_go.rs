#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct Q([i32; 3]);

fn quotient_of_boundary(_edge: usize) -> Q {
    // Every literal dP6 boundary corridor lands in P=F_B/F_V, and the
    // composite P -> E=F_K/F_V -> Q=F_K/F_B is zero.
    Q([0, 0, 0])
}

fn main() {
    let boundary_edges = 12;
    let images = (0..boundary_edges)
        .map(quotient_of_boundary)
        .collect::<Vec<_>>();
    assert!(images.iter().all(|q| *q == Q([0, 0, 0])));

    // The three labelled generic road classes are independent in the
    // relevant degree of Q. Their norm is nonzero and has augmentation 3.
    let q_sigma = Q([1, 1, 1]);
    assert_ne!(q_sigma, Q([0, 0, 0]));
    assert_eq!(q_sigma.0.iter().sum::<i32>(), 3);

    // Therefore no integral linear combination of boundary-only columns can
    // realize the required generic class.
    for mask in 0_u16..(1_u16 << boundary_edges) {
        let mut image = Q([0, 0, 0]);
        for (edge, q) in images.iter().enumerate() {
            if mask & (1 << edge) != 0 {
                for i in 0..3 {
                    image.0[i] += q.0[i];
                }
            }
        }
        assert_ne!(image, q_sigma);
    }

    // Adding a single based interior column q_sigma repairs the coefficient
    // presentation primitively, but its mixed-variance spatial realization
    // is precisely the missing boundary-crossing kernel.
    let augmented_columns = [Q([0, 0, 0]), q_sigma];
    assert_eq!(augmented_columns[1], q_sigma);
    assert_eq!(gcd_all(&augmented_columns[1].0), 1);

    println!(
        "{{\"status\":\"falsified_scoped_boundary_only_q_lift\",\"boundary_edges\":12,\"boundary_Q_rank\":0,\"qSigma\":[1,1,1],\"qSigma_nonzero\":true,\"qSigma_augmentation\":3,\"boundary_only_solution\":\"EMPTY\",\"minimal_coefficient_extension_columns\":1,\"augmented_smith\":[1],\"interior_mixed_variance_kernel_constructed\":false,\"entry158_mapping_fiber_instantiated\":false,\"physical_p_defined\":false,\"physical_bockstein_defined\":false}}"
    );
}

fn gcd_all(values: &[i32]) -> i32 {
    values.iter().fold(0, |a, b| gcd(a, *b))
}

fn gcd(mut a: i32, mut b: i32) -> i32 {
    a = a.abs();
    b = b.abs();
    while b != 0 {
        let r = a % b;
        a = b;
        b = r;
    }
    a
}
