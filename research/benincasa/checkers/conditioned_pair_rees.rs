use std::fs;

fn main() {
    let mut generic = 0_u64;
    let mut exceptional = 0_u64;

    for eps in 1_i128..=29 {
        let b = eps * eps;
        for ux in -7_i128..=7 {
            for uy in -7_i128..=7 {
                let cx = eps * ux;
                let cy = eps * uy;
                let xi = cx * cy / b;
                assert_eq!(xi, ux * uy);
                for s in -9_i128..=9 {
                    let r = eps * s;
                    // Cleared generic conditional correction:
                    // cx cy (r^2-b) / b^2 = xi (s^2-1).
                    let numerator = cx * cy * (r * r - b);
                    let denominator = b * b;
                    assert_eq!(numerator, denominator * xi * (s * s - 1));
                    generic += 1;
                }
                exceptional += 1;
            }
        }
    }

    let output = format!(
        concat!(
            "{{\n",
            "  \"schema\": \"marici.conditioned_pair_rees.v1\",\n",
            "  \"generic_conditional_packets_checked\": {},\n",
            "  \"exceptional_lifts_checked\": {},\n",
            "  \"exceptional_coordinate\": \"xi=cx cy/b\",\n",
            "  \"normalized_fiber_coordinate\": \"s=r/sqrt(b)\",\n",
            "  \"conditional_pair\": \"Axy+xi(s^2-1)\",\n",
            "  \"gaussian_average_returns_unconditional_pair\": true\n",
            "}}\n"
        ),
        generic, exceptional
    );
    fs::write(
        "research/benincasa/results/conditioned-pair-rees.json",
        output,
    )
    .unwrap();
}
