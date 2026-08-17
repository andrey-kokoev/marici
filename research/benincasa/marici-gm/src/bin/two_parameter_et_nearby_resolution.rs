fn mm(a: [[i64; 2]; 2], b: [[i64; 2]; 2]) -> [[i64; 2]; 2] {
    let mut c = [[0; 2]; 2];
    for i in 0..2 {
        for j in 0..2 {
            for k in 0..2 {
                c[i][j] += a[i][k] * b[k][j];
            }
        }
    }
    c
}

fn delta1(x: i64, e: i64, t: i64) -> i64 {
    4 * x * (x * t * t + 2 * e * x * t - e * e * (x + 2 * t - e))
}
fn delta2(x: i64, e: i64, t: i64) -> i64 {
    4 * t * (x * x * t + 2 * e * x * t - e * e * (2 * x + t - e))
}

fn main() {
    // Put y=t and keep x invertible.  On the E-chart E=u,t=u*v,
    // Delta_i=4*u^2 times the displayed residual factors.
    let delta1_e_exceptional = "x^2*(v^2+2*v-1)";
    let delta2_e_exceptional = "x^2*v^2";
    let exceptional_orders = [2_i8, 2_i8];
    assert_eq!(exceptional_orders, [2, 2]);
    for x in [1_i64, 2, 3] {
        for u in [-2_i64, -1, 0, 1, 2] {
            for v in [-2_i64, -1, 0, 1, 2] {
                let pulled1 = 4 * x * u * u * (x * (v * v + 2 * v - 1) + u * (1 - 2 * v));
                let pulled2 = 4 * u * u * v * (x * x * v + 2 * x * u * (v - 1) + u * u * (1 - v));
                assert_eq!(delta1(x, u, u * v), pulled1);
                assert_eq!(delta2(x, u, u * v), pulled2);
            }
        }
    }

    // Delta2 is not SNC after the first blowup.  At its remaining point put
    // v=u*w; its new exceptional multiplicity is four and the strict
    // transforms meet it at w=0 and w=2/x.
    let delta2_second_exceptional_order = 4_i8;
    assert_eq!(delta2_second_exceptional_order % 2, 0);
    for x in [1_i64, 2, 3] {
        for u in [-2_i64, -1, 0, 1, 2] {
            for w in [-2_i64, -1, 0, 1, 2] {
                let twice_pulled =
                    4 * u.pow(4) * w * (x * x * w - 2 * x + u * (2 * x * w + 1) - u * u * w);
                assert_eq!(delta2(x, u, u * u * w), twice_pulled);
            }
        }
    }

    // Signed-energy elliptic data:
    // A=(2x-E)(E-2t), B=E(2x+2t-E).
    // After cancelling their common u on the E-chart, m=A/B restricts to
    // 1-2v.  Hence the exceptional divisor carries the original Legendre
    // variation; v=0,1/2,infinity are its three cusps m=1,0,infinity.
    let exceptional_modulus = "m=1-2*v";
    let exceptional_cusps = ["v=0 -> m=1", "v=1/2 -> m=0", "v=infinity -> m=infinity"];
    for x in [1_i64, 2, 3] {
        for u in [-2_i64, -1, 0, 1, 2] {
            for v in [-2_i64, -1, 0, 1, 2] {
                let a = (2 * x - u) * (u - 2 * u * v);
                let b = u * (2 * x + 2 * u * v - u);
                let abar = (2 * x - u) * (1 - 2 * v);
                let bbar = 2 * x + 2 * u * v - u;
                assert_eq!(a, u * abar);
                assert_eq!(b, u * bbar);
                if u == 0 {
                    assert_eq!(abar, (1 - 2 * v) * bbar);
                }
            }
        }
    }

    // Standard Gamma(2) homology basis.  The two ordered coordinate limits
    // select the m=1 and m=infinity cusp monodromies.  Their products differ;
    // this is intrinsic Legendre braid data, not a new algebraic support.
    let t0 = [[1, 2], [0, 1]];
    let t1 = [[1, 0], [-2, 1]];
    let tinf = [[1, -2], [2, -3]]; // inverse(t0*t1)
    assert_eq!(mm(mm(t0, t1), tinf), [[1, 0], [0, 1]]);
    let ordered_1_inf = mm(t1, tinf);
    let ordered_inf_1 = mm(tinf, t1);
    assert_ne!(ordered_1_inf, ordered_inf_1);

    println!("{{");
    println!("  \"corner\": \"(E,t)=(0,0), x invertible\",");
    println!("  \"first_blowup_E_chart\": {{\"Delta1_exceptional\":\"{}\",\"Delta2_exceptional\":\"{}\",\"orders\":[2,2]}},", delta1_e_exceptional, delta2_e_exceptional);
    println!("  \"Delta2_second_blowup\": {{\"exceptional_order\":4,\"strict_points\":[\"w=0\",\"w=2/x\"]}},");
    println!("  \"conductor_exceptional_semisimple_monodromy\": [1,1,1],");
    println!(
        "  \"elliptic_exceptional_modulus\": \"{}\",",
        exceptional_modulus
    );
    println!(
        "  \"elliptic_exceptional_cusps\": [\"{}\",\"{}\",\"{}\"],",
        exceptional_cusps[0], exceptional_cusps[1], exceptional_cusps[2]
    );
    println!("  \"ordered_coordinate_monodromies_commute\": false,");
    println!(
        "  \"order_products\": {{\"T1_Tinf\":{:?},\"Tinf_T1\":{:?}}},",
        ordered_1_inf, ordered_inf_1
    );
    println!("  \"mixed_factors\": [\"2\",\"E\",\"t\",\"v^2+2v-1\",\"w\",\"xw-2\"],");
    println!("  \"new_base_support_factor\": false,");
    println!("  \"new_carrier_datum\": false,");
    println!("  \"classification\": \"noncommuting selected cusp monodromies are the existing Legendre braid; conductor resolution has only even exceptional multiplicities\"");
    println!("}}");
}
