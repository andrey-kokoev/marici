use std::fs;

type V2 = [i128; 2];
type M2 = [[i128; 2]; 2];

fn outer(a: V2, b: V2) -> M2 {
    [[a[0]*b[0], a[0]*b[1]], [a[1]*b[0], a[1]*b[1]]]
}

fn add(a: M2, b: M2) -> M2 {
    [[a[0][0]+b[0][0], a[0][1]+b[0][1]], [a[1][0]+b[1][0], a[1][1]+b[1][1]]]
}

fn scale(c: i128, a: M2) -> M2 {
    [[c*a[0][0], c*a[0][1]], [c*a[1][0], c*a[1][1]]]
}

fn main() {
    let mut checks = 0_u64;
    let mut phase_pairs = 0_u64;

    for u0 in 1_i128..=7 { for u1 in 1_i128..=8 {
        for v0 in 1_i128..=9 { for v1 in 1_i128..=10 {
            let u = [u0,u1];
            let v = [v0,v1];
            let uu = outer(u,u);
            let vv = outer(v,v);
            let mixed = add(outer(u,v), outer(v,u));
            for epsilon in 1_i128..=4 { for eta in 1_i128..=4 {
                let chi = [epsilon*u0 + eta*v0, epsilon*u1 + eta*v1];
                let direct = outer(chi,chi);
                let expanded = add(add(scale(epsilon*epsilon,uu), scale(epsilon*eta,mixed)), scale(eta*eta,vv));
                assert_eq!(direct, expanded);
                checks += 1;
            }}

            // v and -v have the same separate PSD ray vv^T, but opposite
            // mixed coefficient.  Relative phase is therefore visible in
            // bidegree (1,1), not in a higher normal grade.
            let minus_v = [-v0,-v1];
            assert_eq!(outer(v,v), outer(minus_v,minus_v));
            let minus_mixed = add(outer(u,minus_v),outer(minus_v,u));
            assert_eq!(minus_mixed, scale(-1,mixed));
            assert_ne!(mixed, [[0,0],[0,0]]);
            checks += 3;
            phase_pairs += 1;
        }
    }}}

    let output = format!(concat!(
        "{{\n",
        "  \"schema\": \"marici.two_amplitude_jet_hermitian_square.v1\",\n",
        "  \"exact_checks\": {},\n",
        "  \"phase_sensitive_pairs\": {},\n",
        "  \"bidegrees\": [\"(2,0)\", \"(1,1)\", \"(0,2)\"],\n",
        "  \"mixed_grade\": \"|u><v|+|v><u|\",\n",
        "  \"relative_phase_visible_at_total_grade\": 2,\n",
        "  \"higher_flag_required\": false,\n",
        "  \"new_cut_carrier_stratum\": false\n",
        "}}\n"), checks, phase_pairs);
    fs::write("research/benincasa/results/two-amplitude-jet-hermitian-square.json", output).unwrap();
}
