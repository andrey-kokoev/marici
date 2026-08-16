use std::{collections::BTreeMap, env, fs};

const TMAX: i32 = 10;
const RMIN: i32 = -6;
const RMAX: i32 = 8;

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct Rat {
    n: i128,
    d: i128,
}

impl Rat {
    const Z: Self = Self { n: 0, d: 1 };
    const O: Self = Self { n: 1, d: 1 };
    fn new(mut n: i128, mut d: i128) -> Self {
        assert_ne!(d, 0);
        if d < 0 {
            n = -n;
            d = -d;
        }
        let g = gcd(n.abs(), d);
        Self { n: n / g, d: d / g }
    }
    fn add(self, q: Self) -> Self {
        Self::new(self.n * q.d + q.n * self.d, self.d * q.d)
    }
    fn mul(self, q: Self) -> Self {
        Self::new(self.n * q.n, self.d * q.d)
    }
    fn neg(self) -> Self {
        Self::new(-self.n, self.d)
    }
    fn scale(self, n: i128, d: i128) -> Self {
        self.mul(Self::new(n, d))
    }
}

fn factorial(n: usize) -> i128 {
    (1..=n as i128).product()
}

fn polynomial_from_values(start: i128, values: &[Rat]) -> Vec<Rat> {
    let mut differences = values.to_vec();
    let mut newton = Vec::new();
    while !differences.is_empty() {
        newton.push(differences[0]);
        differences = differences
            .windows(2)
            .map(|w| w[1].add(w[0].neg()))
            .collect();
    }
    let mut result = vec![Rat::Z; values.len()];
    let mut falling = vec![Rat::O];
    for (k, &delta) in newton.iter().enumerate() {
        let factor = delta.scale(1, factorial(k));
        for (i, &c) in falling.iter().enumerate() {
            result[i] = result[i].add(c.mul(factor));
        }
        let root = start + k as i128;
        let mut next = vec![Rat::Z; falling.len() + 1];
        for (i, &c) in falling.iter().enumerate() {
            next[i] = next[i].add(c.scale(-root, 1));
            next[i + 1] = next[i + 1].add(c);
        }
        falling = next;
    }
    while result.last() == Some(&Rat::Z) {
        result.pop();
    }
    result
}

fn choose(n: usize, k: usize) -> i128 {
    if k > n {
        return 0;
    }
    (0..k).fold(1_i128, |z, i| z * (n - i) as i128 / (i + 1) as i128)
}

fn infinity_n2_coefficient(x: i128, y: i128, which_31: bool) -> Rat {
    let a = x * y;
    let s = x + y;
    for p in 2_usize..=10 {
        let start = 11_i128;
        let count = 2 * p + 14;
        let values: Vec<_> = (0..count)
            .map(|i| {
                let n = start + i as i128;
                let v = a * n * n - 2 * s;
                let mut z = residue(x, y, n, which_31);
                for _ in 0..p {
                    z = z.scale(v, 1);
                }
                z
            })
            .collect();
        let poly = polynomial_from_values(start, &values);
        // Validate beyond the interpolation set.
        let test_n = start + count as i128 + 3;
        let mut eval = Rat::Z;
        for &c in poly.iter().rev() {
            eval = eval.scale(test_n, 1).add(c);
        }
        let mut expected = residue(x, y, test_n, which_31);
        let vv = a * test_n * test_n - 2 * s;
        for _ in 0..p {
            expected = expected.scale(vv, 1);
        }
        if eval != expected {
            continue;
        }
        let mut coefficient = Rat::Z;
        for j in 0.. {
            let degree = 2 * p + 2 + 2 * j;
            if degree >= poly.len() {
                break;
            }
            let multiplier = choose(p + j - 1, j);
            let mut term = poly[degree].scale(multiplier, 1);
            for _ in 0..j {
                term = term.scale(2 * s, a);
            }
            coefficient = coefficient.add(term);
        }
        for _ in 0..p {
            coefficient = coefficient.scale(1, a);
        }
        assert_eq!(p, 4);
        return coefficient;
    }
    panic!("no rational denominator power found")
}

fn gcd(mut a: i128, mut b: i128) -> i128 {
    while b != 0 {
        let c = a % b;
        a = b;
        b = c;
    }
    a.max(1)
}

#[derive(Clone, Debug)]
struct S(BTreeMap<(i32, i32), Rat>);

impl S {
    fn mono(t: i32, r: i32, c: i128) -> Self {
        let mut m = BTreeMap::new();
        if c != 0 {
            m.insert((t, r), Rat::new(c, 1));
        }
        Self(m)
    }
    fn rat(t: i32, r: i32, c: Rat) -> Self {
        let mut m = BTreeMap::new();
        if c != Rat::Z {
            m.insert((t, r), c);
        }
        Self(m)
    }
    fn add(&self, q: &Self) -> Self {
        let mut out = self.0.clone();
        for (&k, &v) in &q.0 {
            let z = out.get(&k).copied().unwrap_or(Rat::Z).add(v);
            if z == Rat::Z {
                out.remove(&k);
            } else {
                out.insert(k, z);
            }
        }
        Self(out)
    }
    fn scale(&self, n: i128, d: i128) -> Self {
        Self(
            self.0
                .iter()
                .filter_map(|(&k, &v)| {
                    let z = v.scale(n, d);
                    (z != Rat::Z).then_some((k, z))
                })
                .collect(),
        )
    }
    fn mul(&self, q: &Self) -> Self {
        let mut out = S(BTreeMap::new());
        for (&(ta, ra), &a) in &self.0 {
            for (&(tb, rb), &b) in &q.0 {
                let (t, r) = (ta + tb, ra + rb);
                if (0..=TMAX).contains(&t) && (RMIN..=RMAX).contains(&r) {
                    out = out.add(&S::rat(t, r, a.mul(b)));
                }
            }
        }
        out
    }
    fn pow(&self, mut p: usize) -> Self {
        let mut a = self.clone();
        let mut z = S::mono(0, 0, 1);
        while p > 0 {
            if p & 1 == 1 {
                z = z.mul(&a);
            }
            p >>= 1;
            if p > 0 {
                a = a.mul(&a);
            }
        }
        z
    }
    fn coeff(&self, t: i32, r: i32) -> Rat {
        self.0.get(&(t, r)).copied().unwrap_or(Rat::Z)
    }
}

fn binomial_minus_three_halves(j: usize) -> Rat {
    let mut z = Rat::O;
    for k in 0..j {
        z = z.mul(Rat::new(-3 - 2 * k as i128, 2 * (k as i128 + 1)));
    }
    z
}

fn geometric_inverse(unit: &S, terms: usize) -> S {
    // unit must have constant coefficient one.
    assert_eq!(unit.coeff(0, 0), Rat::O);
    let u = unit.add(&S::mono(0, 0, -1));
    let mut out = S::mono(0, 0, 1);
    let mut power = S::mono(0, 0, 1);
    for j in 1..=terms {
        power = power.mul(&u);
        out = out.add(&power.scale(if j % 2 == 0 { 1 } else { -1 }, 1));
    }
    out
}

fn minus_three_halves(unit: &S, terms: usize) -> S {
    assert_eq!(unit.coeff(0, 0), Rat::O);
    let u = unit.add(&S::mono(0, 0, -1));
    let mut out = S::mono(0, 0, 1);
    let mut power = S::mono(0, 0, 1);
    for j in 1..=terms {
        power = power.mul(&u);
        let b = binomial_minus_three_halves(j);
        out = out.add(&power.scale(b.n, b.d));
    }
    out
}

fn weighted_k_l(x: i128, y: i128, n: i128) -> (S, S) {
    let one = S::mono(0, 0, 1);
    let tau2 = S::mono(2, 0, 1);
    let total = tau2.clone();
    let z = tau2.add(&S::mono(0, 0, -(x + y)));
    let cut = tau2.scale(-1, 1);
    let aa = S::mono(0, 0, y).add(&S::mono(2, 1, 1));
    let bb = S::mono(0, 0, x)
        .add(&S::mono(2, 1, -1))
        .add(&S::mono(3, 0, n));
    let x2 = S::mono(0, 0, x * x);
    let y2 = S::mono(0, 0, y * y);
    let a2 = aa.pow(2);
    let b2 = bb.pow(2);
    let z2 = z.pow(2);
    let c2 = cut.pow(2);
    let h = x2.add(&y2).add(&z2.scale(-1, 1));
    let f = x2
        .mul(&a2.pow(2))
        .add(&h.mul(&a2).mul(&b2).scale(-1, 1))
        .add(&y2.mul(&b2.pow(2)));
    let ga = x2
        .add(&c2.scale(-1, 1))
        .mul(&x2.add(&y2.scale(-1, 1)).add(&z2.scale(-1, 1)))
        .add(&c2.mul(&z2).scale(-2, 1));
    let gb = y2
        .add(&c2.scale(-1, 1))
        .mul(&y2.add(&x2.scale(-1, 1)).add(&z2.scale(-1, 1)))
        .add(&c2.mul(&z2).scale(-2, 1));
    let hh = z2.mul(
        &c2.add(&y2.scale(-1, 1))
            .mul(&c2.add(&x2.scale(-1, 1)))
            .add(&c2.mul(&z2)),
    );
    let k = f.add(&ga.mul(&a2)).add(&gb.mul(&b2)).add(&hh);
    let bracket = x2
        .add(&y2.scale(-1, 1))
        .add(&z2)
        .mul(&a2)
        .add(&y2.add(&x2.scale(-1, 1)).add(&z2).mul(&b2))
        .add(
            &z2.mul(
                &total
                    .pow(2)
                    .scale(2, 1)
                    .add(&x2.scale(-1, 1))
                    .add(&y2.scale(-1, 1))
                    .add(&z2),
            )
            .scale(-1, 1),
        );
    let l = total.mul(&bracket).scale(2, 1);
    // Shift K/tau^6 and L/tau^4.
    let ks = S(k
        .0
        .into_iter()
        .filter_map(|((t, r), c)| (t >= 6).then_some(((t - 6, r), c)))
        .collect());
    let ls = S(l
        .0
        .into_iter()
        .filter_map(|((t, r), c)| (t >= 4).then_some(((t - 4, r), c)))
        .collect());
    assert_eq!(one.coeff(0, 0), Rat::O);
    (ks, ls)
}

fn residue(x: i128, y: i128, n: i128, which_31: bool) -> Rat {
    let (k, l) = weighted_k_l(x, y, n);
    let k00 = 4 * x * y * (n * n * x * y - 2 * (x + y));
    if k00 == 0 {
        return Rat::Z;
    }
    let ku = k.scale(1, k00);
    let km32 = minus_three_halves(&ku, 10);

    let q1u = S::mono(0, 0, 1).add(
        &S::mono(2, 1, -1)
            .add(&S::mono(2, 0, -1))
            .add(&S::mono(3, 0, n))
            .scale(1, 2 * x),
    );
    let q2u = S::mono(0, 0, 1).add(&S::mono(2, 1, 1).add(&S::mono(2, 0, -1)).scale(1, 2 * y));
    let q3u = S::mono(0, 0, 1).add(&S::mono(1, 0, n));
    let mut d = geometric_inverse(&q1u, 10)
        .mul(&geometric_inverse(&q2u, 10))
        .mul(&geometric_inverse(&q3u, 10))
        .scale(1, 4 * x * y);
    let occ = if which_31 {
        S::mono(0, -1, 1)
    } else {
        // 1/(-r+tau*n)=-sum_{j>=0} tau^j*n^j/r^(j+1).
        let mut z = S(BTreeMap::new());
        for j in 0..=4 {
            z = z.add(&S::mono(j, -(j + 1), -n.pow(j as u32)));
        }
        z
    };
    d = d.mul(&occ);
    let form = d.mul(&l).mul(&km32).scale(-1, 2);
    form.coeff(4, -1)
}

fn main() {
    let output = env::args().nth(1).expect("output path");
    let mut sum_checks = 0_u64;
    let mut infinity_checks = 0_u64;
    for x in 1_i128..=4 {
        for y in 1_i128..=4 {
            for n in -3_i128..=3 {
                let s = x + y;
                let u = n * n;
                let v = x * y * u - 2 * s;
                if v == 0 {
                    continue;
                }
                let r31 = residue(x, y, n, true);
                let r23 = residue(x, y, n, false);
                let bracket = (x * y).pow(2) * u.pow(2) - 7 * x * y * s * u + 5 * s.pow(2);
                let expected = Rat::new(3 * u * (x - y) * s * bracket, 2 * x * y * v.pow(2));
                assert_eq!(r31.add(r23), expected);
                sum_checks += 1;
            }
        }
    }
    for &(x, y) in &[(1, 2), (1, 3), (2, 3), (2, 5), (3, 4), (3, 5)] {
        let l31 = infinity_n2_coefficient(x, y, true);
        let l23 = infinity_n2_coefficient(x, y, false);
        let expected31 = Rat::new(3 * x + 5 * y, 2 * y);
        let expected23 = Rat::new(-(5 * x + 3 * y), 2 * x);
        let total = Rat::new(3 * (x - y) * (x + y), 2 * x * y);
        assert_eq!(l31, expected31);
        assert_eq!(l23, expected23);
        assert_eq!(l31.add(l23), total);
        infinity_checks += 1;
    }
    let json = format!(
        concat!(
            "{{\n",
            "  \"schema\": \"marici.split-occurrence-weight-zero.v1\",\n",
            "  \"exact_unsplit_sum_checks\": {},\n",
            "  \"exact_projective_infinity_checks\": {},\n",
            "  \"individual_denominator_power\": 4,\n",
            "  \"L31\": \"(3*x+5*y)/(2*y)\",\n",
            "  \"L23\": \"-(5*x+3*y)/(2*x)\",\n",
            "  \"kummer_coefficient_rule\": \"c_i=L_i/(8*(x*y)^(5/2))\",\n",
            "  \"sum_L\": \"3*(x-y)*(x+y)/(2*x*y)\",\n",
            "  \"sum_kummer_coefficient\": \"3*(x-y)*(x+y)/(16*(x*y)^(7/2))\",\n",
            "  \"occurrence_forgetting\": \"additive_not_multiplicity_two\",\n",
            "  \"individual_endpoint_jets\": \"uncomputed\",\n",
            "  \"individual_physical_currents\": \"not_canonical_without_regulator_hierarchy\",\n",
            "  \"new_carrier_incidence\": false\n",
            "}}\n"
        ),
        sum_checks, infinity_checks
    );
    fs::write(output, json).expect("write certificate");
}
