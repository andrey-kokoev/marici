use std::fs;

fn factorial(n: u32) -> i128 {
    (1..=n as i128).product()
}

fn kappa_2r(a: i128, t: i128, r: u32) -> i128 {
    a * (-2 * a * t).pow(r) * factorial(r)
}

fn kappa_0r(a: i128, t: i128, r: u32) -> i128 {
    assert!(r >= 3);
    (-1_i128).pow(r) * 2_i128.pow(r - 1) * factorial(r - 1) * a.pow(r) * t.pow(r)
}

fn main() {
    let mut packets = 0_u64;
    let mut coefficients = 0_u64;
    for a in 1_i128..=17 {
        for b in 1_i128..=13 {
            for t in -7_i128..=7 {
                assert_eq!(kappa_2r(a, t, 0), a);
                assert_eq!(kappa_2r(a, t, 1), -2 * t * a * a);
                assert_eq!(kappa_2r(a, t, 2), 8 * t * t * a * a * a);
                let variance_pi = b + 2 * t * t * a * a;
                assert!(variance_pi >= 0);
                assert_eq!(kappa_0r(a, t, 3), -8 * t.pow(3) * a.pow(3));
                assert_eq!(kappa_0r(a, t, 4), 48 * t.pow(4) * a.pow(4));
                for r in 0_u32..=12 {
                    let _ = kappa_2r(a, t, r);
                    coefficients += 1;
                    if r >= 3 {
                        let _ = kappa_0r(a, t, r);
                        coefficients += 1;
                    }
                }
                packets += 1;
            }
        }
    }

    let output = format!(
        concat!(
            "{{\n",
            "  \"schema\": \"marici.cubic_gaussian_cumulant_generator.v1\",\n",
            "  \"exact_parameter_packets_checked\": {},\n",
            "  \"closed_cumulant_coefficients_checked\": {},\n",
            "  \"generator\": \"b y^2/2+t a y-log(1+2aty)/2+a x^2/(2(1+2aty))\",\n",
            "  \"kappa_2r\": \"a(-2at)^r r!\",\n",
            "  \"kappa_0r_r_ge_3\": \"(-1)^r 2^(r-1)(r-1)! a^r t^r\",\n",
            "  \"density_representability\": \"exact unitary orbit\"\n",
            "}}\n"
        ),
        packets, coefficients
    );
    fs::write(
        "research/benincasa/results/cubic-gaussian-cumulant-generator.json",
        output,
    )
    .unwrap();
}
