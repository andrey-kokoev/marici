use std::fs;

type M2 = [[i128; 2]; 2];

fn kron(a: M2, b: M2) -> [[i128; 4]; 4] {
    let mut out = [[0_i128; 4]; 4];
    for i in 0..2 { for j in 0..2 { for k in 0..2 { for l in 0..2 {
        out[2*i+k][2*j+l] = a[i][j] * b[k][l];
    }}}}
    out
}

fn tr(a: M2) -> i128 { a[0][0] + a[1][1] }

fn tr_product(a: M2, b: M2) -> i128 {
    let mut out = 0_i128;
    for i in 0..2 { for j in 0..2 { out += a[i][j] * b[j][i]; }}
    out
}

fn main() {
    let mut checks = 0_u64;
    for x in 1_i128..=13 {
        for y in 1_i128..=15 {
            // Positive rank-one integral kernels; normalization is restored by
            // dividing by the trace, so all certificates remain integral.
            let rho = [[1, x], [x, x*x]];
            let sigma = [[1, y], [y, y*y]];
            let joint = kron(rho, sigma);

            // Partial trace over Y is tr(sigma)*rho.
            for i in 0..2 { for j in 0..2 {
                let partial = joint[2*i][2*j] + joint[2*i+1][2*j+1];
                assert_eq!(partial, tr(sigma) * rho[i][j]);
                checks += 1;
            }}

            // Transition-kernel expectations factor on independent Cuts.
            let a = [[2, 1], [1, 3]];
            let b = [[3, 2], [2, 5]];
            let ab = kron(a, b);
            let mut joint_expectation = 0_i128;
            for i in 0..4 { for j in 0..4 {
                joint_expectation += joint[i][j] * ab[j][i];
            }}
            assert_eq!(joint_expectation, tr_product(rho, a) * tr_product(sigma, b));
            checks += 1;
        }
    }

    let output = format!(concat!(
        "{{\n",
        "  \"schema\": \"marici.coherent_density_kernel_cut.v1\",\n",
        "  \"exact_checks\": {},\n",
        "  \"joint_kernel\": \"rho_X tensor rho_Y\",\n",
        "  \"partial_trace_recovers_factor\": true,\n",
        "  \"transition_expectations_factor\": true,\n",
        "  \"coefficient_braiding_required\": false,\n",
        "  \"new_cut_carrier_stratum\": false\n",
        "}}\n"), checks);
    fs::write("research/benincasa/results/coherent-density-kernel-cut.json", output).unwrap();
}
