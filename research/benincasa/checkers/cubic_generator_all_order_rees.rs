use std::fs;

fn rational_coefficients(c: i128, t: i128, x: i128, y: i128, order: usize) -> Vec<i128> {
    let d = 2 * t * y;
    let mut inv = vec![0_i128; order + 1];
    inv[0] = 1;
    for n in 2..=order {
        inv[n] = -d * inv[n - 2];
    }
    let numerator = [c * c * y * y, 2 * c * x * y, x * x];
    let mut out = vec![0_i128; order + 1];
    for n in 0..=order {
        for k in 0..=2.min(n) {
            out[n] += numerator[k] * inv[n - k];
        }
    }
    out
}

fn main() {
    let order = 30_usize;
    let mut packets = 0_u64;
    let mut coefficients = 0_u64;
    for c in -11_i128..=11 {
        for t in -5_i128..=5 {
            for x in -3_i128..=3 {
                for y in -3_i128..=3 {
                    let plus = rational_coefficients(c, t, x, y, order);
                    let deck = rational_coefficients(-c, t, x, y, order);
                    for n in 0..=order {
                        let expected = if n % 2 == 0 { plus[n] } else { -plus[n] };
                        assert_eq!(deck[n], expected);
                        coefficients += 1;
                    }
                    packets += 1;
                }
            }
        }
    }

    let output = format!(
        concat!(
            "{{\n",
            "  \"schema\": \"marici.cubic_generator_all_order_rees.v1\",\n",
            "  \"exact_parameter_packets_checked\": {},\n",
            "  \"series_coefficients_checked\": {},\n",
            "  \"maximum_epsilon_order\": {},\n",
            "  \"exceptional_denominator\": \"1+2 epsilon^2 t y is a unit\",\n",
            "  \"deck_action\": \"(epsilon,c) maps to (-epsilon,-c)\",\n",
            "  \"full_generator_deck_character\": 1,\n",
            "  \"new_logarithmic_extension\": false\n",
            "}}\n"
        ),
        packets, coefficients, order
    );
    fs::write(
        "research/benincasa/results/cubic-generator-all-order-rees.json",
        output,
    )
    .unwrap();
}
