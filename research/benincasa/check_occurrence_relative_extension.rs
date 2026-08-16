use std::{env, fs};

fn gcd(mut a: i128, mut b: i128) -> i128 {
    while b != 0 {
        (a, b) = (b, a % b);
    }
    a.abs().max(1)
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct Rat {
    n: i128,
    d: i128,
}

impl Rat {
    fn new(mut n: i128, mut d: i128) -> Self {
        assert_ne!(d, 0);
        if d < 0 {
            n = -n;
            d = -d;
        }
        let g = gcd(n, d);
        Self { n: n / g, d: d / g }
    }

    fn add(self, rhs: Self) -> Self {
        Self::new(self.n * rhs.d + rhs.n * self.d, self.d * rhs.d)
    }

    fn mul(self, rhs: Self) -> Self {
        Self::new(self.n * rhs.n, self.d * rhs.d)
    }
}

fn pow4(x: i128) -> i128 {
    x * x * x * x
}

fn main() {
    let output = env::args().nth(1).expect("output path");
    let mut period_sewing_checks = 0_u64;
    let mut horizontal_checks = 0_u64;
    let mut cyclic_checks = 0_u64;

    // Remove the common factor i*pi/16. The Kummer interval is
    // int_{-N}^{N} dn/w=-i*pi/sqrt(x*y), and entry 243 gives the two
    // occurrence coefficients. Thus the period numerators over (x*y)^4 are:
    //   p31 = +(3*x^2+7*x*y+6*y^2)
    //   p23 = -(6*x^2+7*x*y+3*y^2).
    for x in 1_i128..=64 {
        for y in 1_i128..=64 {
            let n31 = 3 * x * x + 7 * x * y + 6 * y * y;
            let n23 = -(6 * x * x + 7 * x * y + 3 * y * y);
            let sewn = -3 * (x - y) * (x + y);
            assert_eq!(n31 + n23, sewn);
            period_sewing_checks += 1;

            if x != y {
                // f=-3*(x^2-y^2)/(x*y)^4. Verify df=f*omega exactly for
                // omega_x=2*x/(x^2-y^2)-4/x and
                // omega_y=-2*y/(x^2-y^2)-4/y.
                let delta = x * x - y * y;
                let f = Rat::new(-3 * delta, pow4(x * y));
                let dfx = Rat::new(6 * x * x - 12 * y * y, x * pow4(x * y));
                let dfy = Rat::new(12 * x * x - 6 * y * y, y * pow4(x * y));
                let omega_x = Rat::new(2 * x, delta).add(Rat::new(-4, x));
                let omega_y = Rat::new(-2 * y, delta).add(Rat::new(-4, y));
                assert_eq!(dfx, f.mul(omega_x));
                assert_eq!(dfy, f.mul(omega_y));
                horizontal_checks += 2;
            }
        }
    }

    // Literal cyclic transport acts by ordered substitutions
    // (x,y)=(X1,X2),(X2,X3),(X3,X1); the same sewing identity must hold
    // independently in all three marked sectors.
    for x1 in 1_i128..=16 {
        for x2 in 1_i128..=16 {
            for x3 in 1_i128..=16 {
                for (x, y) in [(x1, x2), (x2, x3), (x3, x1)] {
                    let n31 = 3 * x * x + 7 * x * y + 6 * y * y;
                    let n23 = -(6 * x * x + 7 * x * y + 3 * y * y);
                    assert_eq!(n31 + n23, -3 * (x - y) * (x + y));
                    cyclic_checks += 1;
                }
            }
        }
    }

    let json = format!(
        concat!(
            "{{\n",
            "  \"schema\": \"marici.occurrence-relative-extension.v1\",\n",
            "  \"exact_period_sewing_checks\": {},\n",
            "  \"exact_horizontal_connection_checks\": {},\n",
            "  \"exact_cyclic_sewing_checks\": {},\n",
            "  \"kummer_interval\": \"-i*pi/sqrt(x*y)\",\n",
            "  \"p31_over_i_pi\": \"(3*x^2+7*x*y+6*y^2)/(16*(x*y)^4)\",\n",
            "  \"p23_over_i_pi\": \"-(6*x^2+7*x*y+3*y^2)/(16*(x*y)^4)\",\n",
            "  \"p_sewn_over_i_pi\": \"-3*(x-y)*(x+y)/(16*(x*y)^4)\",\n",
            "  \"sewn_connection_x\": \"2*x/(x^2-y^2)-4/x\",\n",
            "  \"sewn_connection_y\": \"-2*y/(x^2-y^2)-4/y\",\n",
            "  \"relative_model\": \"mapping_cone_with_polar_endpoint_jet_boundary\",\n",
            "  \"individual_evaluation\": \"requires_noncanonical_boundary_functional\",\n",
            "  \"sewn_kummer_period_line_horizontal\": true,\n",
            "  \"full_relative_extension_horizontal\": \"not_claimed\",\n",
            "  \"direct_legendre_gysin_image\": 0,\n",
            "  \"new_carrier_incidence\": false\n",
            "}}\n"
        ),
        period_sewing_checks, horizontal_checks, cyclic_checks
    );
    fs::write(output, json).expect("write certificate");
}
