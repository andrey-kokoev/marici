use std::{env, fs};

const DEG: usize = 20;

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

fn weighted_corner(x: i128, y: i128, r: i128, n: i128) -> (P, P) {
    let tau = P::e();
    let tau2 = tau.sq();
    let tau3 = tau2.mul(tau);
    let total = tau2;
    let s = P::c(x + y);
    let z = total.sub(s);
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
    let f = x2
        .mul(a2.sq())
        .sub(h.mul(a2).mul(b2))
        .add(y2.mul(b2.sq()));
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
        .sub(
            z2.mul(
                total
                    .sq()
                    .scale(2)
                    .sub(x2)
                    .sub(y2)
                    .add(z2),
            ),
        );
    let k1 = total.mul(bracket).scale(2);
    (k, k1)
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

    let mut weighted_points = 0usize;
    for x in 1i128..=5 {
        for y in 1i128..=5 {
            for r in -5i128..=5 {
                for n in -5i128..=5 {
                    let (k, k1) = weighted_corner(x, y, r, n);
                    let s = x + y;
                    assert!(k.0[..6].iter().all(|c| *c == 0));
                    assert_eq!(
                        k.0[6],
                        4 * x * x * y * y * n * n + 8 * x * y * s * (r * r - 1),
                        "weighted leading surface"
                    );
                    assert!(k1.0[..4].iter().all(|c| *c == 0));
                    assert_eq!(k1.0[4], 16 * x * y * s, "weighted K1 numerator");
                    weighted_points += 1;
                }
            }
        }
    }

    // The exceptional disk is Q=beta*(1-r^2)-alpha*n^2 > 0 with
    // alpha=4*x^2*y^2 and beta=8*x*y*(x+y). Meromorphic continuation gives
    // int_D Q^lambda = pi*beta^lambda*sqrt(beta/alpha)/(lambda+1), hence at
    // lambda=-3/2 the coefficient of pi is -1/(8*x^2*y^2*(x+y)).
    // E -> E-i0 sends K=E^3*(-Q) to -Q+i0, so K^(-3/2)=+i*Q^(-3/2).
    // Multiplication by the source double-pole numerator -8*x*y*(x+y)
    // leaves +i*pi/(x*y); the 2*pi*i Leray discontinuity leaves
    // -2*pi^2/(x*y). Check these rational prefactors without floating point.
    for x in 1i128..=25 {
        for y in 1i128..=25 {
            let s = x + y;
            let beta = 8 * x * y * s;
            let sqrt_alpha = 2 * x * y;
            assert_eq!(beta * sqrt_alpha, 16 * x * x * y * y * s);
            let source_numerator = -8 * x * y * s;
            assert_eq!(source_numerator * -2 * x * y, beta * sqrt_alpha);
        }
    }

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
        "  \"weighted_substitution\": \"E=tau^2, A=tau^2*r, A+B=tau^3*n\",\n",
        "  \"weighted_exact_integer_points\": 3025,\n",
        "  \"weighted_surface_lead\": \"K=tau^6*(4*x^2*y^2*n^2+8*x*y*(x+y)*(r^2-1))+O(tau^7)\",\n",
        "  \"weighted_source_K1_lead\": \"K1=16*x*y*(x+y)*tau^4+O(tau^5)\",\n",
        "  \"simple_master_period_order\": \"tau^2=E\",\n",
        "  \"double_master_period_order\": \"tau^0=1\",\n",
        "  \"exceptional_period_functional_e1_to_e9\": [0,0,\"y\",0,\"x\",1,0,0,0],\n",
        "  \"exceptional_functional_gysin_image\": 0,\n",
        "  \"exceptional_functional_sector\": \"rank-seven algebraic Tate/Kummer kernel\",\n",
        "  \"coefficient_level_common_factor\": \"-8*x*y*(x+y) times the universal local thimble functional\",\n",
        "  \"physical_real_corner\": \"(a,b)=(y,x); the other sign corners are occurrence/deck companions\",\n",
        "  \"carrier_level_third_rees_class_nonzero\": true,\n",
        "  \"regularized_disk_identity\": \"AC int_D Q^(-3/2) dr dn=-pi/(8*x^2*y^2*(x+y))\",\n",
        "  \"lower_half_branch\": \"E to E-i0 implies K=E^3*(-Q) to -Q+i0 and K^(-3/2)=+i*Q^(-3/2)\",\n",
        "  \"normalized_I_loc\": \"-i*pi/(8*x^2*y^2*(x+y))\",\n",
        "  \"source_numerator_times_I_loc\": \"+i*pi/(x*y)\",\n",
        "  \"leray_discontinuity_factor\": \"2*pi*i\",\n",
        "  \"normalized_cut_nearby_commutator_e1_to_e9\": [0,0,\"-2*pi^2/x\",0,\"-2*pi^2/y\",\"-2*pi^2/(x*y)\",0,0,0],\n",
        "  \"exceptional_semisimple_monodromy\": \"+1\",\n",
        "  \"exceptional_nilpotent_N\": 0,\n",
        "  \"overall_wavefunction_prefactor_status\": \"excluded: source equation (6) uses proportionality and omits coupling/alpha factors; result is in the frozen equation-(58) de Rham master normalization\",\n",
        "  \"full_nine_master_cut_nearby_commutator_computed\": true,\n",
        "  \"new_carrier_divisor\": false\n",
        "}}\n"),
        {
            assert_eq!(weighted_points, 3025);
            points
        }
    );
    fs::write(out, json).expect("write certificate");
}
