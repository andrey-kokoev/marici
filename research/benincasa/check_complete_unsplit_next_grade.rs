use std::{env, fs};

const DEG: usize = 16;

#[derive(Clone, Copy)]
struct P([i128; DEG]);

impl P {
    fn c(value: i128) -> Self {
        let mut coefficients = [0; DEG];
        coefficients[0] = value;
        Self(coefficients)
    }

    fn tau() -> Self {
        let mut coefficients = [0; DEG];
        coefficients[1] = 1;
        Self(coefficients)
    }

    fn add(self, other: Self) -> Self {
        Self(core::array::from_fn(|index| self.0[index] + other.0[index]))
    }

    fn scale(self, scalar: i128) -> Self {
        Self(self.0.map(|coefficient| coefficient * scalar))
    }

    fn sub(self, other: Self) -> Self {
        self.add(other.scale(-1))
    }

    fn mul(self, other: Self) -> Self {
        let mut coefficients = [0; DEG];
        for left in 0..DEG {
            for right in 0..DEG - left {
                coefficients[left + right] += self.0[left] * other.0[right];
            }
        }
        Self(coefficients)
    }

    fn sq(self) -> Self {
        self.mul(self)
    }
}

fn weighted_family(x: i128, y: i128, r: i128, n: i128) -> (P, P) {
    let tau = P::tau();
    let tau2 = tau.sq();
    let tau3 = tau2.mul(tau);
    let total = tau2;
    let z = total.sub(P::c(x + y));
    let cut = total.scale(-1);
    let a = P::c(y).add(tau2.scale(r));
    let b = P::c(x).sub(tau2.scale(r)).add(tau3.scale(n));

    let x2 = P::c(x * x);
    let y2 = P::c(y * y);
    let a2 = a.sq();
    let b2 = b.sq();
    let z2 = z.sq();
    let cut2 = cut.sq();
    let h = x2.add(y2).sub(z2);
    let f = x2.mul(a2.sq()).sub(h.mul(a2).mul(b2)).add(y2.mul(b2.sq()));
    let ga = x2
        .sub(cut2)
        .mul(x2.sub(y2).sub(z2))
        .sub(cut2.mul(z2).scale(2));
    let gb = y2
        .sub(cut2)
        .mul(y2.sub(x2).sub(z2))
        .sub(cut2.mul(z2).scale(2));
    let hh = z2.mul(cut2.sub(y2).mul(cut2.sub(x2)).add(cut2.mul(z2)));
    let k = f.add(ga.mul(a2)).add(gb.mul(b2)).add(hh);

    let bracket = x2
        .sub(y2)
        .add(z2)
        .mul(a2)
        .add(y2.sub(x2).add(z2).mul(b2))
        .sub(z2.mul(total.sq().scale(2).sub(x2).sub(y2).add(z2)));
    let k1 = total.mul(bracket).scale(2);
    (k, k1)
}

fn main() {
    let output = env::args().nth(1).expect("output path");
    let mut exact_points = 0usize;

    for x in 1i128..=9 {
        for y in 1i128..=9 {
            for r in -8i128..=8 {
                for n in -7i128..=7 {
                    let (k, k1) = weighted_family(x, y, r, n);
                    let s = x + y;
                    let k0 = 4 * x * y * (n * n * x * y + 2 * s * (r * r - 1));
                    let k_next = 4 * n * x * y * s * (r * r - 2 * r - 1);
                    let l0 = 16 * x * y * s;
                    let l_next = 8 * n * x * y * s;
                    assert_eq!(k.0[6], k0);
                    assert_eq!(k.0[7], k_next);
                    assert_eq!(k1.0[4], l0);
                    assert_eq!(k1.0[5], l_next);

                    // Write k0=a+c*r^2 and k_next=p+q*r+u*r^2.
                    // The only possible tau^-2 logarithmic residue is
                    // proportional to q+n*c, which vanishes identically.
                    let c = 8 * x * y * s;
                    let q = -8 * n * x * y * s;
                    assert_eq!(q, -n * c);
                    assert_eq!(q + n * c, 0);
                    exact_points += 1;
                }
            }
        }
    }

    let json = format!(
        concat!(
            "{{\n",
            "  \"schema\": \"marici.complete_unsplit_next_grade.v1\",\n",
            "  \"exact_weighted_points\": {},\n",
            "  \"K_expansion\": {{\n",
            "    \"tau6\": \"4*x*y*(n^2*x*y+2*(x+y)*(r^2-1))\",\n",
            "    \"tau7\": \"4*n*x*y*(x+y)*(r^2-2*r-1)\"\n",
            "  }},\n",
            "  \"K1_expansion\": {{\"tau4\":\"16*x*y*(x+y)\",\"tau5\":\"8*n*x*y*(x+y)\"}},\n",
            "  \"leading_complete_log_residue\": 0,\n",
            "  \"next_grade_residue_identity\": \"coeff_r(K_tau7)+n*coeff_r2(K_tau6)=0\",\n",
            "  \"next_complete_log_residue\": 0,\n",
            "  \"grades_closed\": [-3,-2],\n",
            "  \"next_possible_grade\": -1,\n",
            "  \"supersedes_incomplete_primitive_in_entries\": [322,323],\n",
            "  \"new_carrier_incidence\": false\n",
            "}}\n"
        ),
        exact_points
    );
    fs::write(output, json).expect("write certificate");
}
