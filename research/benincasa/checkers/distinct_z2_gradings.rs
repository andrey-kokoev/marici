use std::fs;

fn main() {
    let mut checks = 0_u64;
    for t in -31_i128..=31 {
        for a in 1_i128..=29 {
            let k3 = -2 * t * a * a;
            let k3_deck = -2 * (-t) * a * a;
            let k4 = 8 * t * t * a * a * a;
            let k4_deck = 8 * (-t) * (-t) * a * a * a;
            assert_eq!(k3_deck, -k3);
            assert_eq!(k4_deck, k4);
            checks += 2;
        }
    }

    for u in -37_i128..=37 {
        for v in -23_i128..=23 {
            let xi = u * v;
            let xi_deck = (-u) * (-v);
            assert_eq!(xi_deck, xi);
            checks += 1;
        }
    }

    let output = format!(
        concat!(
            "{{\n",
            "  \"schema\": \"marici.distinct_z2_gradings.v1\",\n",
            "  \"exact_parity_checks\": {},\n",
            "  \"cubic_flow_action\": \"t maps to -t; kappa3 odd; kappa4 even\",\n",
            "  \"conditioning_action\": \"u maps to -u; Sym2(u) even\",\n",
            "  \"canonical_identification_between_actions\": false,\n",
            "  \"identification_with_cosmological_time_root\": \"unconstructed\"\n",
            "}}\n"
        ),
        checks
    );
    fs::write(
        "research/benincasa/results/distinct-z2-gradings.json",
        output,
    )
    .unwrap();
}
