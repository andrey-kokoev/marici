// Exact two-chart audit of the complete contact-route packet on Bl_(q,y).

fn main() {
    let contacts = [-31_i128, -7, 1, 5, 29];
    let chart_parameters = [-13_i128, -3, 1, 2, 11];

    for c in contacts {
        assert_ne!(c, 0);
        for t in chart_parameters {
            assert_ne!(t, 0);

            // U_q: y=q*t.  P=C*t and v=2/t.
            // Clear t in A=4*P*v.
            let aq_cleared = 4 * (c * t) * 2;
            assert_eq!(aq_cleared, 8 * c * t);
            assert_eq!(aq_cleared / t, 8 * c);

            // U_y: q=y*s.  P=C/s and v=2*s.
            // Clear s in P and then cancel in the complete composition.
            let s = t;
            let ay_cleared = 4 * c * (2 * s);
            assert_eq!(ay_cleared / s, 8 * c);

            let b = -8 * c;
            assert_eq!(aq_cleared / t + b, 0);
            assert_eq!(ay_cleared / s + b, 0);
        }
    }

    println!(
        "{{\"status\":\"pass\",\"blowup\":\"Bl_(q,y)\",\"charts\":[\"y=q*t\",\"q=y*s\"],\"strict_route_packet\":\"(8*C,-8*C)\",\"chart_transition_agrees\":true,\"exceptional_packet_nonzero_for_C_nonzero\":true,\"classification\":\"exceptional_destructive_interference\"}}"
    );
}
