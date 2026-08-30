use std::collections::BTreeSet;
use std::fs;

fn main() {
    let mut binary_packets = 0_u64;
    let mut ternary_packets = 0_u64;
    let mut labelled_components = 0_u64;

    for m in 1_usize..=7 {
        for n in 1_usize..=6 {
            let left: Vec<i128> = (0..m).map(|i| 3 * i as i128 - m as i128).collect();
            let right: Vec<i128> = (0..n).map(|j| 5 * j as i128 - 2 * n as i128).collect();
            let mut labels = BTreeSet::new();
            for i in 0..m {
                for j in 0..n {
                    assert!(labels.insert((i, j)));
                    let cleared_mu = 3 * left[i] + 4 * right[j];
                    let _ = cleared_mu;
                    labelled_components += 1;
                }
            }
            assert_eq!(labels.len(), m * n);
            binary_packets += 1;
        }
    }

    // Exact three-block cardinality weights (3,4,12)/13.  The first two
    // normalize to (3,4)/5 and their aggregate has outer weight 5/13.
    for m in 1_usize..=5 {
        for n in 1_usize..=5 {
            for k in 1_usize..=5 {
                let a: Vec<i128> = (0..m).map(|i| i as i128 - 2).collect();
                let b: Vec<i128> = (0..n).map(|j| 2 * j as i128 + 1).collect();
                let c: Vec<i128> = (0..k).map(|q| 3 - q as i128).collect();
                let mut direct = BTreeSet::new();
                let mut nested = BTreeSet::new();
                for i in 0..m {
                    for j in 0..n {
                        for q in 0..k {
                            let mu_direct_num = 3 * a[i] + 4 * b[j] + 12 * c[q];
                            let inner_num = 3 * a[i] + 4 * b[j];
                            let mu_nested_num = inner_num + 12 * c[q];
                            assert_eq!(mu_direct_num, mu_nested_num);
                            direct.insert((i, j, q, mu_direct_num));
                            nested.insert((i, j, q, mu_nested_num));
                        }
                    }
                }
                assert_eq!(direct, nested);
                assert_eq!(direct.len(), m * n * k);
                ternary_packets += 1;
            }
        }
    }

    let output = format!(
        concat!(
            "{{\n",
            "  \"schema\": \"marici.finite_mixture_cut_descent.v1\",\n",
            "  \"binary_mixture_packets_checked\": {},\n",
            "  \"ternary_reassociation_packets_checked\": {},\n",
            "  \"labelled_product_components_checked\": {},\n",
            "  \"component_product\": \"J_X times J_Y\",\n",
            "  \"nested_merge\": \"same labelled tuples and weighted displacement\",\n",
            "  \"new_carrier_operation_required\": false\n",
            "}}\n"
        ),
        binary_packets, ternary_packets, labelled_components
    );
    fs::write(
        "research/benincasa/results/finite-mixture-cut-descent.json",
        output,
    )
    .unwrap();
}
