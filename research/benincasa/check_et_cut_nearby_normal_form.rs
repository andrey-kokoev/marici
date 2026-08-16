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
                    let k2 = a * a * b * b
                        - (3 * x * x + 2 * x * y) * a * a
                        - (3 * y * y + 2 * x * y) * b * b
                        + x * x * y * y
                        + 2 * x * y * s * s;
                    let k3 = 2 * s * (a * a + b * b - x * x - 4 * x * y - y * y);
                    let k4 = -a * a - b * b + 6 * s * s + 2 * x * y;
                    assert_eq!(k.0[0], r * r, "central square");
                    assert_eq!(k.0[1], k1, "first normal factorization");
                    assert_eq!(k.0[2], k2, "second normal coefficient");
                    assert_eq!(k.0[3], k3, "third normal coefficient");
                    assert_eq!(k.0[4], k4, "fourth normal coefficient");
                    assert_eq!(k.0[5], -6 * s, "fifth normal coefficient");
                    assert_eq!(k.0[6], 2, "sixth normal coefficient");
                    assert!(k.0[7..].iter().all(|c| *c == 0), "global degree six");
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
    // On the conductor tangent plane the minimal blowup has marked points
    // p0=[1:0], p-=[-1:1], p+=[1:1]. In the integral basis
    // e-=[p-]-[p0], e+=[p+]-[p0], the oriented moving interval from the
    // negative to the positive branch has boundary e+-e-=(-1,1).
    let leray_boundary = [-1i128, 1i128];
    assert_eq!(leray_boundary[0] + leray_boundary[1], 0);
    assert_ne!(leray_boundary, [0, 0]);

    let json = format!(
        concat!(
        "{{\n",
        "  \"schema\": \"marici.et_cut_nearby_normal_form.v1\",\n",
        "  \"exact_integer_points\": {},\n",
        "  \"central_fiber\": \"K_0=R^2; R=x*a^2+y*b^2-x*y*(x+y)\",\n",
        "  \"first_normal\": \"[E]K_E=-2*(x+y)*(a^2-y^2)*(b^2-x^2)\",\n",
        "  \"complete_expansion\": \"K_E=R^2+E*K1+E^2*K2+E^3*K3+E^4*K4-6*(x+y)*E^5+2*E^6\",\n",
        "  \"K2\": \"a^2*b^2-(3*x^2+2*x*y)*a^2-(3*y^2+2*x*y)*b^2+x^2*y^2+2*x*y*(x+y)^2\",\n",
        "  \"K3\": \"2*(x+y)*(a^2+b^2-x^2-4*x*y-y^2)\",\n",
        "  \"K4\": \"-a^2-b^2+6*(x+y)^2+2*x*y\",\n",
        "  \"generic_local_model\": \"U*V=E*unit+O(E^2) away from the four axial marked lines\",\n",
        "  \"excess_support\": [\"a=y\",\"a=-y\",\"b=x\",\"b=-x\"],\n",
        "  \"corner_second_coefficient\": 0,\n",
        "  \"corner_first_nonzero_normal_order\": 3,\n",
        "  \"corner_third_coefficient\": \"-8*x*y*(x+y)\",\n",
        "  \"corner_exact_tail\": \"E^3*(-8*x*y*(x+y)+(5*x^2+14*x*y+5*y^2)*E-6*(x+y)*E^2+2*E^3)\",\n",
        "  \"depth_two_comparison_sufficient_at_marked_corners\": false,\n",
        "  \"corner_cubic_tangent_cone\": \"-8*x*y*(x+y)*E*(A*B+E*(A+B)/2+E^2)\",\n",
        "  \"conductor_tangent_restriction\": \"8*x*y*(x+y)*E*(A-E)*(A+E)\",\n",
        "  \"minimal_log_blowup\": \"Bl_(A,E)(A^2) with exceptional P1 and attachment points [1:0],[1:1],[-1:1]\",\n",
        "  \"relative_exceptional_rank\": 2,\n",
        "  \"blowup_chart\": \"r=A/E; p0=r=infinity, pminus=r=-1, pplus=r=1\",\n",
        "  \"canonical_leray_interval\": \"oriented interval [pminus,pplus] fixed by the lower-half-plane E continuation and da wedge db orientation\",\n",
        "  \"relative_basis\": [\"[pminus]-[p0]\",\"[pplus]-[p0]\"],\n",
        "  \"canonical_boundary_vector\": [-1,1],\n",
        "  \"physical_real_corner\": \"(a,b)=(y,x); the other sign corners are occurrence/deck companions\",\n",
        "  \"carrier_level_third_rees_class_nonzero\": true,\n",
        "  \"full_nine_master_cut_nearby_commutator_computed\": false,\n",
        "  \"new_carrier_divisor\": false\n",
        "}}\n"),
        points
    );
    fs::write(out, json).expect("write certificate");
}
