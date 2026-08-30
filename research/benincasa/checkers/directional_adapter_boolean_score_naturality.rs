const N: usize = 5;
const SIZE: usize = 1 << N;
const INCIDENCE: [usize; 3] = [
    (1 << 1) | (1 << 3),
    (1 << 0) | (1 << 4),
    (1 << 0) | (1 << 1) | (1 << 2),
];

fn popcount(mut x: usize) -> usize {
    let mut n = 0;
    while x != 0 { n += x & 1; x >>= 1; }
    n
}

fn depths(present: usize, axis: usize) -> [u8; N] {
    let mut out = [0_u8; N];
    for i in 0..N {
        if present & (1 << i) != 0 {
            out[i] = 2 + u8::from(INCIDENCE[axis] & (1 << i) != 0);
        }
    }
    out
}

fn delete(mut values: [u8; N], deleted: usize) -> [u8; N] {
    for i in 0..N {
        if deleted & (1 << i) != 0 { values[i] = 0; }
    }
    values
}

fn main() {
    let mut naturality_tests = 0_usize;
    for axis in 0..3 {
        for present in 0..SIZE {
            for deleted in 0..SIZE {
                let effective_deleted = deleted & present;
                let deletion_then_adapter = depths(present & !effective_deleted, axis);
                let adapter_then_deletion = delete(depths(present, axis), effective_deleted);
                assert_eq!(deletion_then_adapter, adapter_then_deletion);
                naturality_tests += 1;
            }
        }
    }

    // Boolean zeta scores and their Mobius inverse remain a constant
    // unimodular observer after embedding every route in the common target.
    let mut zeta = [[0_i64; SIZE]; SIZE];
    let mut mobius = [[0_i64; SIZE]; SIZE];
    for t in 0..SIZE {
        for s in 0..SIZE {
            if s & t == t {
                zeta[t][s] = 1;
            }
            if s & t == s {
                mobius[s][t] = if popcount(t ^ s) % 2 == 0 { 1 } else { -1 };
            }
        }
    }
    for i in 0..SIZE {
        for j in 0..SIZE {
            let value: i64 = (0..SIZE).map(|k| mobius[i][k] * zeta[k][j]).sum();
            assert_eq!(value, i64::from(i == j));
        }
    }

    println!(
        "{{\"schema\":\"marici.benincasa.directional-adapter-boolean-score-naturality.v1\",\"status\":\"passed\",\"occurrence_count\":5,\"route_count\":32,\"direction_count\":3,\"deletion_adapter_naturality_tests\":{},\"incidence_masks\":[10,17,7],\"mobius_inverse_exact\":true,\"transported_score_kernel_dimension\":0,\"classification\":\"complete Boolean score tomography remains jointly faithful on the flat labelled adapter staircase\"}}",
        naturality_tests
    );
}
