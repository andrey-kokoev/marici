use serde_json::json;
use std::collections::BTreeMap;
use std::ops::{Add, Mul, Neg, Sub};

#[derive(Clone, Debug, Eq, PartialEq)]
struct Poly<const N: usize>(BTreeMap<[u8; N], i64>);

impl<const N: usize> Poly<N> {
    fn constant(c: i64) -> Self {
        let mut terms = BTreeMap::new();
        if c != 0 {
            terms.insert([0; N], c);
        }
        Self(terms)
    }

    fn var(i: usize) -> Self {
        let mut exponent = [0; N];
        exponent[i] = 1;
        let mut terms = BTreeMap::new();
        terms.insert(exponent, 1);
        Self(terms)
    }

    fn scale(self, c: i64) -> Self {
        Self(
            self.0
                .into_iter()
                .filter_map(|(e, a)| {
                    let value = a * c;
                    (value != 0).then_some((e, value))
                })
                .collect(),
        )
    }
}

impl<const N: usize> Add for Poly<N> {
    type Output = Self;
    fn add(mut self, rhs: Self) -> Self {
        for (e, a) in rhs.0 {
            let value = self.0.get(&e).copied().unwrap_or(0) + a;
            if value == 0 {
                self.0.remove(&e);
            } else {
                self.0.insert(e, value);
            }
        }
        self
    }
}

impl<const N: usize> Neg for Poly<N> {
    type Output = Self;
    fn neg(self) -> Self {
        self.scale(-1)
    }
}

impl<const N: usize> Sub for Poly<N> {
    type Output = Self;
    fn sub(self, rhs: Self) -> Self {
        self + (-rhs)
    }
}

impl<const N: usize> Mul for Poly<N> {
    type Output = Self;
    fn mul(self, rhs: Self) -> Self {
        let mut out = BTreeMap::new();
        for (e1, a) in self.0 {
            for (e2, b) in &rhs.0 {
                let mut exponent = [0; N];
                for i in 0..N {
                    exponent[i] = e1[i] + e2[i];
                }
                *out.entry(exponent).or_insert(0) += a * b;
            }
        }
        out.retain(|_, a| *a != 0);
        Self(out)
    }
}

fn det2<const N: usize>(m: [[Poly<N>; 2]; 2]) -> Poly<N> {
    m[0][0].clone() * m[1][1].clone() - m[0][1].clone() * m[1][0].clone()
}

fn transpose_mul<const N: usize>(s: [[Poly<N>; 2]; 2], g: [[Poly<N>; 2]; 2]) -> [[Poly<N>; 2]; 2] {
    let mut out = [
        [Poly::constant(0), Poly::constant(0)],
        [Poly::constant(0), Poly::constant(0)],
    ];
    for i in 0..2 {
        for j in 0..2 {
            for k in 0..2 {
                for l in 0..2 {
                    out[i][j] = out[i][j].clone()
                        + s[k][i].clone() * g[k][l].clone() * s[l][j].clone();
                }
            }
        }
    }
    out
}

fn modp(x: i128, p: i128) -> i128 {
    let r = x % p;
    if r < 0 { r + p } else { r }
}

fn main() {
    // Exact determinant identity in Q[A,B,E].
    let a = Poly::<3>::var(0);
    let b = Poly::<3>::var(1);
    let e = Poly::<3>::var(2);
    let c = a.clone() + b.clone() - e.clone() * e.clone();
    let g = [
        [a.clone().scale(2), c.clone()],
        [c.clone(), b.clone().scale(2)],
    ];
    let q = a.clone() * b.clone().scale(4) - c.clone() * c.clone();
    assert_eq!(det2(g), q);

    // Exact regular-gauge covariance in Q[A,B,E,s11,s12,s21,s22].
    let a7 = Poly::<7>::var(0);
    let b7 = Poly::<7>::var(1);
    let e7 = Poly::<7>::var(2);
    let c7 = a7.clone() + b7.clone() - e7.clone() * e7.clone();
    let g7 = [
        [a7.clone().scale(2), c7.clone()],
        [c7.clone(), b7.clone().scale(2)],
    ];
    let s = [
        [Poly::<7>::var(3), Poly::<7>::var(4)],
        [Poly::<7>::var(5), Poly::<7>::var(6)],
    ];
    let det_s = det2(s.clone());
    let transformed = transpose_mul(s, g7.clone());
    assert_eq!(det2(transformed), det_s.clone() * det_s * det2(g7));

    // Exact second-normal expansion after B=E(2s-E), A=B-4p.
    let p = Poly::<3>::var(0);
    let ss = Poly::<3>::var(1);
    let ee = Poly::<3>::var(2);
    let bb = ee.clone() * (ss.clone().scale(2) - ee.clone());
    let aa = bb.clone() - p.clone().scale(4);
    let cc = aa.clone() + bb.clone() - ee.clone() * ee.clone();
    let substituted = aa * bb.scale(4) - cc.clone() * cc;
    let expected = -(p.clone() * p.clone()).scale(16)
        - (p.clone() * ee.clone() * ee.clone()).scale(8)
        + (ss.clone() * ee.clone() * ee.clone() * ee.clone()).scale(8)
        - (ee.clone() * ee.clone() * ee.clone() * ee).scale(5);
    assert_eq!(substituted, expected);

    let samples = [
        (32003_i128, 1_i128, 2_i128, 4182_i128),
        (32003, 1, 2, 5571),
        (32003, 1, 2, 6151),
        (32009, 1, 1, 2199),
        (32009, 1, 1, 4198),
        (32009, 1, 3, 30050),
    ];
    let mut sample_results = Vec::new();
    for (prime, x, y, z) in samples {
        let energy = modp(x + y + z, prime);
        let l1 = modp(x - y - z, prime);
        let l2 = modp(x - y + z, prime);
        let l3 = modp(x + y - z, prime);
        let l4 = modp(x + y + z, prime);
        let av = modp(l1 * l2, prime);
        let bv = modp(l3 * l4, prime);
        let cv = modp(av + bv - energy * energy, prime);
        let determinant = modp(4 * av * bv - cv * cv, prime);
        let matrix_nonzero = av != 0 || bv != 0 || cv != 0;
        assert_eq!(determinant, 0);
        assert!(matrix_nonzero);
        sample_results.push(json!({
            "prime": prime,
            "point": [x, y, z],
            "A": av,
            "B": bv,
            "C": cv,
            "determinant": determinant,
            "toy_pairing_rank": 1
        }));
    }

    let output = json!({
        "schema": "marici.q_pairing_discriminant_toy.v1",
        "status": "pass",
        "identity": "det([[2A,A+B-E^2],[A+B-E^2,2B]]) = Q",
        "regular_gauge_covariance": "det(S^T G S)=det(S)^2 det(G)",
        "second_normal_expansion": "-16p^2-8pE^2+8sE^3-5E^4",
        "generic_Q_samples": sample_results,
        "interpretation": "mechanism witness only; the physical response pairing remains to be source-derived",
        "falsifier": "derive the faithful physical response matrix and test whether its determinant is Q times an existing-carrier unit"
    });
    println!("{}", serde_json::to_string_pretty(&output).unwrap());
}
