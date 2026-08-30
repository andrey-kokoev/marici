use std::fs;

type Mat = [[i128; 2]; 2];

fn mul(a: Mat, b: Mat) -> Mat {
    [
        [a[0][0] * b[0][0] + a[0][1] * b[1][0], a[0][0] * b[0][1] + a[0][1] * b[1][1]],
        [a[1][0] * b[0][0] + a[1][1] * b[1][0], a[1][0] * b[0][1] + a[1][1] * b[1][1]],
    ]
}

fn sub(a: Mat, b: Mat) -> Mat {
    [[a[0][0]-b[0][0], a[0][1]-b[0][1]], [a[1][0]-b[1][0], a[1][1]-b[1][1]]]
}

fn main() {
    let mut checks = 0_u64;
    let mut nonzero_defects = 0_u64;

    for x in 1_i128..=17 {
        for y in 1_i128..=19 {
            let u = [[1, x], [0, 1]];
            let v = [[1, 0], [y, 1]];
            let a = [[x + 1, 1], [2, y + 1]];
            let uv_a = mul(mul(u, v), a);
            let vu_a = mul(mul(v, u), a);
            let comm_a = mul(sub(mul(u, v), mul(v, u)), a);
            assert_eq!(sub(uv_a, vu_a), comm_a);
            checks += 1;
            if comm_a != [[0, 0], [0, 0]] {
                nonzero_defects += 1;
            }

            // Commuting scalar/diagonal transports recover Entry 1718.
            let d1 = [[x, 0], [0, x]];
            let d2 = [[y, 0], [0, y]];
            assert_eq!(mul(mul(d1, d2), a), mul(mul(d2, d1), a));
            checks += 1;
        }
    }
    assert_eq!(nonzero_defects, 17 * 19);

    let output = format!(
        concat!(
            "{{\n",
            "  \"schema\": \"marici.matrix_mixture_interchange.v1\",\n",
            "  \"exact_checks\": {},\n",
            "  \"nonzero_generic_defects\": {},\n",
            "  \"interchange_defect\": \"[U,V]A\",\n",
            "  \"commuting_specialization_closes\": true,\n",
            "  \"classification\": \"coefficient-level braiding/coherence datum\",\n",
            "  \"physical_cosmology_source_derived\": false,\n",
            "  \"new_cut_carrier_stratum\": false\n",
            "}}\n"
        ), checks, nonzero_defects
    );
    fs::write("research/benincasa/results/matrix-mixture-interchange.json", output).unwrap();
}
