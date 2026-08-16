use std::collections::BTreeMap;

#[derive(Clone, Debug, Default, Eq, PartialEq)]
struct Poly<const N: usize>(BTreeMap<[u8; N], i128>);

impl<const N: usize> Poly<N> {
    fn constant(value: i128) -> Self {
        let mut out = Self::default();
        if value != 0 {
            out.0.insert([0; N], value);
        }
        out
    }
    fn variable(index: usize) -> Self {
        let mut exponent = [0; N];
        exponent[index] = 1;
        let mut out = Self::default();
        out.0.insert(exponent, 1);
        out
    }
    fn add(&self, other: &Self) -> Self {
        let mut out = self.clone();
        for (m, c) in &other.0 {
            let next = out.0.get(m).copied().unwrap_or(0) + c;
            if next == 0 {
                out.0.remove(m);
            } else {
                out.0.insert(*m, next);
            }
        }
        out
    }
    fn scale(&self, scalar: i128) -> Self {
        let mut out = Self::default();
        for (m, c) in &self.0 {
            let next = c * scalar;
            if next != 0 {
                out.0.insert(*m, next);
            }
        }
        out
    }
    fn sub(&self, other: &Self) -> Self {
        self.add(&other.scale(-1))
    }
    fn mul(&self, other: &Self) -> Self {
        let mut out = Self::default();
        for (lm, lc) in &self.0 {
            for (rm, rc) in &other.0 {
                let mut m = [0; N];
                for i in 0..N {
                    m[i] = lm[i] + rm[i];
                }
                let next = out.0.get(&m).copied().unwrap_or(0) + lc * rc;
                if next == 0 {
                    out.0.remove(&m);
                } else {
                    out.0.insert(m, next);
                }
            }
        }
        out
    }
    fn pow(&self, mut exponent: u8) -> Self {
        let mut out = Self::constant(1);
        let mut base = self.clone();
        while exponent > 0 {
            if exponent & 1 == 1 {
                out = out.mul(&base);
            }
            exponent >>= 1;
            if exponent > 0 {
                base = base.mul(&base);
            }
        }
        out
    }
    fn evaluate(&self, point: [i128; N]) -> i128 {
        self.0
            .iter()
            .map(|(m, c)| {
                let mut term = *c;
                for i in 0..N {
                    term *= point[i].pow(u32::from(m[i]));
                }
                term
            })
            .sum()
    }
    fn format(&self, names: [&str; N]) -> String {
        if self.0.is_empty() {
            return "0".to_owned();
        }
        let mut terms: Vec<_> = self.0.iter().collect();
        terms.sort_by_key(|(m, _)| std::cmp::Reverse(m.iter().copied().sum::<u8>()));
        terms
            .into_iter()
            .map(|(m, c)| {
                let factors: Vec<_> = m
                    .iter()
                    .enumerate()
                    .filter(|(_, e)| **e > 0)
                    .map(|(i, e)| {
                        if *e == 1 {
                            names[i].to_owned()
                        } else {
                            format!("{}^{}", names[i], e)
                        }
                    })
                    .collect();
                if factors.is_empty() {
                    c.to_string()
                } else if *c == 1 {
                    factors.join("*")
                } else if *c == -1 {
                    format!("-{}", factors.join("*"))
                } else {
                    format!("{}*{}", c, factors.join("*"))
                }
            })
            .collect::<Vec<_>>()
            .join(" + ")
            .replace("+ -", "- ")
    }
}

fn sum<const N: usize>(terms: &[Poly<N>]) -> Poly<N> {
    terms.iter().fold(Poly::default(), |a, b| a.add(b))
}

fn cayley_menger<const N: usize>(
    x: &Poly<N>,
    y: &Poly<N>,
    z: &Poly<N>,
    c: &Poly<N>,
    a: &Poly<N>,
    b: &Poly<N>,
) -> Poly<N> {
    let x2 = x.pow(2);
    let y2 = y.pow(2);
    let z2 = z.pow(2);
    let c2 = c.pow(2);
    let a2 = a.pow(2);
    let b2 = b.pow(2);
    let h = x2.add(&y2).sub(&z2);
    let ga0 = x2.mul(&x2.sub(&y2).sub(&z2));
    let gac = y2.sub(&x2).sub(&z2);
    let gb0 = y2.mul(&y2.sub(&x2).sub(&z2));
    let gbc = x2.sub(&y2).sub(&z2);
    let hc = z2.sub(&x2).sub(&y2);
    sum(&[
        x2.mul(&a.pow(4)),
        a2.mul(&b2).mul(&h).scale(-1),
        y2.mul(&b.pow(4)),
        a2.mul(&ga0),
        c2.mul(&a2).mul(&gac),
        b2.mul(&gb0),
        c2.mul(&b2).mul(&gbc),
        z2.mul(&c.pow(4)),
        c2.mul(&z2).mul(&hc),
        z2.mul(&x2).mul(&y2),
    ])
}

fn main() {
    let x = Poly::<3>::variable(0);
    let y = Poly::<3>::variable(1);
    let z = Poly::<3>::variable(2);
    let e = sum(&[x.clone(), y.clone(), z.clone()]);
    let top = cayley_menger(&x, &y, &z, &e.scale(-1), &x.add(&z), &y.add(&z));
    let signed_left = y.add(&z).sub(&x);
    let signed_right = x.add(&z).sub(&y);
    let expected_top = e.mul(&signed_left).mul(&signed_right).pow(2);
    assert_eq!(top, expected_top);
    println!("K_TRIPLE={}", top.format(["x", "y", "z"]));
    println!("K_TRIPLE_FACTORED=[(x+y+z)(-x+y+z)(x-y+z)]^2");
    println!("K_TRIPLE_A={}", top.evaluate([2, 3, 4]));
    println!("K_TRIPLE_B={}", top.evaluate([3, 5, 6]));

    let x = Poly::<4>::variable(0);
    let y = Poly::<4>::variable(1);
    let z = Poly::<4>::variable(2);
    let t = Poly::<4>::variable(3);
    let e = sum(&[x.clone(), y.clone(), z.clone()]);
    let kg1g2 = cayley_menger(&x, &y, &z, &t, &y.add(&t).scale(-1), &x.add(&t).scale(-1));
    let kg1g = cayley_menger(&x, &y, &z, &e.scale(-1), &t, &y.add(&z));
    let kg2g = cayley_menger(&x, &y, &z, &e.scale(-1), &x.add(&z), &t);
    println!("K_FACE_011={}", kg1g2.format(["x", "y", "z", "t"]));
    println!("K_FACE_101={}", kg1g.format(["x", "y", "z", "t"]));
    println!("K_FACE_110={}", kg2g.format(["x", "y", "z", "t"]));

    let jacobian = -1_i128;
    let expected_011 = t.mul(&y.add(&z).sub(&x)).mul(&x.add(&z).sub(&y)).pow(2);
    assert_eq!(kg1g2, expected_011);
    assert_eq!(jacobian.abs(), 1);
    assert_eq!(top.evaluate([2, 3, 4]), 18_225);
    println!("INCIDENCE_JACOBIAN={jacobian}");
    println!("TOP_RESIDUE_BOUNDARY_SIGNS=[1,-1,1]");
}
