use std::{env, fs};

const DEG: usize = 12;

#[derive(Clone, Copy)]
struct P([i128; DEG]);

impl P {
    fn c(x: i128) -> Self {
        let mut a = [0; DEG];
        a[0] = x;
        Self(a)
    }
    fn e() -> Self {
        let mut a = [0; DEG];
        a[1] = 1;
        Self(a)
    }
    fn add(self, o: Self) -> Self {
        let mut a = [0; DEG];
        for i in 0..DEG {
            a[i] = self.0[i] + o.0[i];
        }
        Self(a)
    }
    fn sub(self, o: Self) -> Self {
        self.add(o.scale(-1))
    }
    fn scale(self, n: i128) -> Self {
        let mut a = [0; DEG];
        for i in 0..DEG {
            a[i] = self.0[i] * n;
        }
        Self(a)
    }
    fn mul(self, o: Self) -> Self {
        let mut a = [0; DEG];
        for i in 0..DEG {
            for j in 0..DEG - i {
                a[i + j] += self.0[i] * o.0[j];
            }
        }
        Self(a)
    }
    fn sq(self) -> Self {
        self.mul(self)
    }
}

fn k_family(x: i128, y: i128, a: i128, b: i128) -> P {
    let e = P::e();
    let s = P::c(x + y);
    let z = e.sub(s);
    let c = e.scale(-1);
    let x2 = P::c(x * x);
    let y2 = P::c(y * y);
    let a2 = P::c(a * a);
    let b2 = P::c(b * b);
    let z2 = z.sq();
    let c2 = c.sq();
    let h = x2.add(y2).sub(z2);
    let f = x2.mul(a2.sq()).sub(h.mul(a2).mul(b2)).add(y2.mul(b2.sq()));
    let ga = x2.sub(c2).mul(x2.sub(y2).sub(z2)).sub(c2.mul(z2).scale(2));
    let gb = y2.sub(c2).mul(y2.sub(x2).sub(z2)).sub(c2.mul(z2).scale(2));
    let hh = z2.mul(c2.sub(y2).mul(c2.sub(x2)).add(c2.mul(z2)));
    f.add(ga.mul(a2)).add(gb.mul(b2)).add(hh)
}

fn main() {
    let out = env::args().nth(1).expect("output path");
    let mut points = 0usize;
    for x in 1i128..=5 {
        for y in 1i128..=5 {
            for a in -6i128..=6 {
                for b in -6i128..=6 {
                    let k = k_family(x, y, a, b);
                    let s = x + y;
                    let r = x * a * a + y * b * b - x * y * s;
                    let k1 = -2 * s * (a * a - y * y) * (b * b - x * x);
                    assert_eq!(k.0[0], r * r, "central square");
                    assert_eq!(k.0[1], k1, "first normal factorization");
                    if a * a == y * y && b * b == x * x {
                        assert_eq!(k.0[2], 0, "corner second coefficient");
                        assert_eq!(k.0[3], -8 * x * y * s, "corner third coefficient");
                        assert_eq!(
                            k.0[4],
                            5 * x * x + 14 * x * y + 5 * y * y,
                            "corner fourth coefficient"
                        );
                        assert_eq!(k.0[5], -6 * s, "corner fifth coefficient");
                        assert_eq!(k.0[6], 2, "corner sixth coefficient");
                        assert!(k.0[7..].iter().all(|c| *c == 0), "corner degree six");
                    }
                    points += 1;
                }
            }
        }
    }
    let json = format!(
        concat!(
        "{{\n",
        "  \"schema\": \"marici.et_cut_nearby_normal_form.v1\",\n",
        "  \"exact_integer_points\": {},\n",
        "  \"central_fiber\": \"K_0=R^2; R=x*a^2+y*b^2-x*y*(x+y)\",\n",
        "  \"first_normal\": \"[E]K_E=-2*(x+y)*(a^2-y^2)*(b^2-x^2)\",\n",
        "  \"generic_local_model\": \"U*V=E*unit+O(E^2) away from the four axial marked lines\",\n",
        "  \"excess_support\": [\"a=y\",\"a=-y\",\"b=x\",\"b=-x\"],\n",
        "  \"corner_second_coefficient\": 0,\n",
        "  \"corner_first_nonzero_normal_order\": 3,\n",
        "  \"corner_third_coefficient\": \"-8*x*y*(x+y)\",\n",
        "  \"corner_exact_tail\": \"E^3*(-8*x*y*(x+y)+(5*x^2+14*x*y+5*y^2)*E-6*(x+y)*E^2+2*E^3)\",\n",
        "  \"depth_two_comparison_sufficient_at_marked_corners\": false,\n",
        "  \"new_carrier_divisor\": false\n",
        "}}\n"),
        points
    );
    fs::write(out, json).expect("write certificate");
}
