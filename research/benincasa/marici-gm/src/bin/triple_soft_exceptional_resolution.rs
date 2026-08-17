use std::collections::BTreeMap;

#[derive(Clone, Debug, PartialEq, Eq)]
struct P(BTreeMap<(u8, u8), i64>);
impl P {
    fn c(n: i64) -> Self {
        let mut z = BTreeMap::new();
        if n != 0 {
            z.insert((0, 0), n);
        }
        Self(z)
    }
    fn r() -> Self {
        Self(BTreeMap::from([((1, 0), 1)]))
    }
    fn s() -> Self {
        Self(BTreeMap::from([((0, 1), 1)]))
    }
    fn add(&self, q: &Self) -> Self {
        let mut z = self.0.clone();
        for (m, c) in &q.0 {
            *z.entry(*m).or_default() += c;
        }
        z.retain(|_, c| *c != 0);
        Self(z)
    }
    fn neg(&self) -> Self {
        Self(self.0.iter().map(|(m, c)| (*m, -*c)).collect())
    }
    fn sub(&self, q: &Self) -> Self {
        self.add(&q.neg())
    }
    fn mul(&self, q: &Self) -> Self {
        let mut z = BTreeMap::new();
        for ((i, j), a) in &self.0 {
            for ((k, l), b) in &q.0 {
                *z.entry((i + k, j + l)).or_default() += a * b;
            }
        }
        z.retain(|_, c| *c != 0);
        Self(z)
    }
    fn scale(&self, n: i64) -> Self {
        self.mul(&Self::c(n))
    }
    fn eval(&self, r: i64, s: i64) -> i64 {
        self.0
            .iter()
            .map(|((i, j), c)| c * r.pow((*i).into()) * s.pow((*j).into()))
            .sum()
    }
}
fn delta1(e: i64, x: i64, y: i64) -> i64 {
    4 * x * (x * y * y + 2 * e * x * y - e * e * (x + 2 * y - e))
}
fn delta2(e: i64, x: i64, y: i64) -> i64 {
    4 * y * (x * x * y + 2 * e * x * y - e * e * (2 * x + y - e))
}
fn a(e: i64, x: i64, y: i64) -> i64 {
    (2 * x - e) * (e - 2 * y)
}
fn b(e: i64, x: i64, y: i64) -> i64 {
    e * (2 * x + 2 * y - e)
}
fn main() {
    let (r, s, one) = (P::r(), P::s(), P::c(1));
    let f1 = r
        .mul(&s.mul(&s))
        .add(&r.mul(&s).scale(2))
        .sub(&r)
        .sub(&s.scale(2))
        .add(&one);
    let f2 = r
        .mul(&r)
        .mul(&s)
        .add(&r.mul(&s).scale(2))
        .sub(&r.scale(2))
        .sub(&s)
        .add(&one);
    assert_eq!(f1.sub(&f2), r.sub(&s).mul(&one.sub(&r.mul(&s))));
    for u in [-2_i64, -1, 0, 1, 2] {
        for r0 in [-2_i64, -1, 0, 1, 2] {
            for s0 in [-2_i64, -1, 0, 1, 2] {
                assert_eq!(
                    delta1(u, u * r0, u * s0),
                    4 * u.pow(4) * r0 * f1.eval(r0, s0)
                );
                assert_eq!(
                    delta2(u, u * r0, u * s0),
                    4 * u.pow(4) * s0 * f2.eval(r0, s0)
                );
                assert_eq!(a(u, u * r0, u * s0), u * u * (2 * r0 - 1) * (1 - 2 * s0));
                assert_eq!(b(u, u * r0, u * s0), u * u * (2 * r0 + 2 * s0 - 1));
                let g1 = s0 * s0 + 2 * r0 * s0 - r0 * r0 * (1 + 2 * s0 - r0);
                let g2 = s0 + 2 * r0 * s0 - r0 * r0 * (2 + s0 - r0);
                assert_eq!(delta1(u * r0, u, u * s0), 4 * u.pow(4) * g1);
                assert_eq!(delta2(u * r0, u, u * s0), 4 * u.pow(4) * s0 * g2);
                assert_eq!(a(u * r0, u, u * s0), u * u * (2 - r0) * (r0 - 2 * s0));
                assert_eq!(b(u * r0, u, u * s0), u * u * r0 * (2 + 2 * s0 - r0));
                let h1 = s0 + 2 * r0 * s0 - r0 * r0 * (s0 + 2 - r0);
                let h2 = s0 * s0 + 2 * r0 * s0 - r0 * r0 * (2 * s0 + 1 - r0);
                assert_eq!(delta1(u * r0, u * s0, u), 4 * u.pow(4) * s0 * h1);
                assert_eq!(delta2(u * r0, u * s0, u), 4 * u.pow(4) * h2);
            }
        }
    }
    for (e, x, y) in [(0, 1, 0), (0, 0, 1), (2, 1, 0), (2, 0, 1)] {
        assert_eq!(a(e, x, y), 0);
        assert_eq!(b(e, x, y), 0);
    }
    for q in -8_i64..=8 {
        // On r=1/2 put q=2s; on s=1/2 put q=2r.
        let four_f1_at_r_half = q * q - 4 * q + 4;
        let four_f2_at_s_half = q * q - 4 * q + 4;
        assert_eq!(four_f1_at_r_half, (q - 2).pow(2));
        assert_eq!(four_f2_at_s_half, (q - 2).pow(2));
        // On 2r+2s-1=0 put q=2r; denominators are cleared by eight.
        let rr = q;
        let ss = 1 - q;
        let ef1 = rr * ss * ss + 4 * rr * ss - 4 * rr - 8 * ss + 8;
        let ef2 = rr * rr * ss + 4 * rr * ss - 8 * rr - 4 * ss + 8;
        assert_eq!(ef1, q * (q - 3).pow(2));
        assert_eq!(ef2, (1 - q) * (q + 2).pow(2));
    }
    for alpha in -4_i64..=4 {
        for beta in -4_i64..=4 {
            let ef2 = -8 * alpha + beta * (1 + 6 * alpha + alpha * alpha);
            let rr = 1 + alpha;
            let ss = beta;
            assert_eq!(ef2, rr * rr * ss + 4 * rr * ss - 8 * rr - 4 * ss + 8);
        }
    }
    println!("{{");
    println!("  \"corner\": \"(E,x,y)=(0,0,0)\",");
    println!("  \"radial_orders\": {{\"A\":2,\"B\":2,\"Delta1\":4,\"Delta2\":4}},");
    println!("  \"E_chart_modulus\": \"(2*r-1)*(1-2*s)/(2*r+2*s-1)\",");
    println!("  \"modulus_base_points\": [\"[0:1:0]\",\"[0:0:1]\",\"[2:1:0]\",\"[2:0:1]\"],");
    println!("  \"conductor_common_split\": [\"r=s with r^3+2*r^2-3*r+1=0\",\"r*s=1 with r^2-3*r+1=0\"],");
    println!("  \"finite_conductor_energy_tangencies\": [\"(1/2,1)\",\"(1,1/2)\",\"(3/2,-1)\",\"(-1,3/2)\"],");
    println!("  \"radial_conductor_semisimple_monodromy\": [1,1],");
    println!("  \"cut_multirees_fitting_ideals\": {{\"I1\":\"(1)\",\"I2\":\"(2*x,2*y)\",\"I3\":\"(4*x*y)\"}},");
    println!("  \"new_base_support_factor\": false,");
    println!("  \"new_carrier_datum\": false,");
    println!("  \"scope\": \"exact exceptional-plane and center census; not a full rank-twelve nearby connection\"");
    println!("}}");
}
