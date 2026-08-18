use std::collections::{BTreeMap, HashMap};

const P: i64 = 32_003;
const NV: usize = 3;
type Mon = [u8; NV];
type Row = BTreeMap<usize, i64>;

fn mm(a: i64, b: i64) -> i64 {
    ((a as i128 * b as i128) % P as i128) as i64
}
fn power(mut a: i64, mut n: i64) -> i64 {
    let mut r = 1;
    while n > 0 {
        if n & 1 == 1 {
            r = mm(r, a);
        }
        a = mm(a, a);
        n >>= 1;
    }
    r
}
fn inv(a: i64) -> i64 {
    power(a.rem_euclid(P), P - 2)
}

#[derive(Clone, Default)]
struct Poly(BTreeMap<Mon, i64>);
impl Poly {
    fn term(m: Mon, c: i64) -> Self {
        let mut r = Self::default();
        let c = c.rem_euclid(P);
        if c != 0 {
            r.0.insert(m, c);
        }
        r
    }
    fn con(c: i64) -> Self {
        Self::term([0; NV], c)
    }
    fn var(i: usize) -> Self {
        let mut m = [0; NV];
        m[i] = 1;
        Self::term(m, 1)
    }
    fn add(&self, o: &Self) -> Self {
        let mut r = self.clone();
        for (m, c) in &o.0 {
            let n = (r.0.get(m).copied().unwrap_or(0) + c).rem_euclid(P);
            if n == 0 {
                r.0.remove(m);
            } else {
                r.0.insert(*m, n);
            }
        }
        r
    }
    fn scale(&self, s: i64) -> Self {
        let mut r = Self::default();
        for (m, c) in &self.0 {
            let n = mm(*c, s.rem_euclid(P));
            if n != 0 {
                r.0.insert(*m, n);
            }
        }
        r
    }
    fn mul(&self, o: &Self) -> Self {
        let mut r = Self::default();
        for (lm, lc) in &self.0 {
            for (rm, rc) in &o.0 {
                let m = [lm[0] + rm[0], lm[1] + rm[1], lm[2] + rm[2]];
                let n = (r.0.get(&m).copied().unwrap_or(0) + mm(*lc, *rc)).rem_euclid(P);
                if n == 0 {
                    r.0.remove(&m);
                } else {
                    r.0.insert(m, n);
                }
            }
        }
        r
    }
    fn pow(&self, mut n: u8) -> Self {
        let mut r = Self::con(1);
        let mut b = self.clone();
        while n > 0 {
            if n & 1 == 1 {
                r = r.mul(&b);
            }
            n >>= 1;
            if n > 0 {
                b = b.mul(&b);
            }
        }
        r
    }
    fn der(&self, i: usize) -> Self {
        let mut r = Self::default();
        for (m, c) in &self.0 {
            if m[i] > 0 {
                let mut d = *m;
                let e = d[i];
                d[i] -= 1;
                r = r.add(&Self::term(d, mm(*c, i64::from(e))));
            }
        }
        r
    }
}
fn sum(ps: &[Poly]) -> Poly {
    ps.iter().fold(Poly::default(), |a, b| a.add(b))
}
fn mons(d: usize) -> Vec<Mon> {
    let mut r = Vec::new();
    for total in 0..=d {
        for c in 0..=total {
            for a in 0..=total - c {
                r.push([c as u8, a as u8, (total - c - a) as u8]);
            }
        }
    }
    r
}
fn add_term(row: &mut Row, col: usize, val: i64) {
    let n = (row.get(&col).copied().unwrap_or(0) + val).rem_euclid(P);
    if n == 0 {
        row.remove(&col);
    } else {
        row.insert(col, n);
    }
}
fn pivot(mut row: Row, ps: &mut BTreeMap<usize, Row>) {
    while let Some((&col, &coef)) = row.iter().next_back() {
        if let Some(old) = ps.get(&col) {
            for (&j, &v) in old {
                add_term(&mut row, j, -mm(coef, v));
            }
        } else {
            let s = inv(coef);
            for v in row.values_mut() {
                *v = mm(*v, s);
            }
            ps.insert(col, row);
            return;
        }
    }
}
fn add_poly(
    row: &mut Row,
    cols: &HashMap<(usize, usize, Mon), usize>,
    kp: usize,
    qp: usize,
    base: Mon,
    poly: &Poly,
    scale: i64,
) {
    for (m, c) in &poly.0 {
        let term = [base[0] + m[0], base[1] + m[1], base[2] + m[2]];
        add_term(row, cols[&(kp, qp, term)], mm(*c, scale));
    }
}

fn rank_for(k: &Poly, q: &Poly, kmax: usize, qmax: usize, ambient: usize, cutoff: usize) -> usize {
    let column_degree = ambient + 3;
    let low = mons(cutoff);
    let all = mons(column_degree);
    let mut labels = Vec::new();
    labels.extend(low.iter().map(|m| (0, 1, *m)));
    for kp in 0..=kmax {
        for qp in 0..=qmax {
            for m in &all {
                if !(kp == 0 && qp == 1 && low.contains(m)) {
                    labels.push((kp, qp, *m));
                }
            }
        }
    }
    let cols: HashMap<_, _> = labels.iter().enumerate().map(|(i, x)| (*x, i)).collect();
    let low_count = low.len();
    let mut ps = BTreeMap::new();
    let gamma = 5_i64;

    for kp in 0..kmax {
        for qp in 0..qmax {
            for axis in 0..NV {
                for m in mons(ambient) {
                    let mut row = Row::new();
                    if m[axis] > 0 {
                        let mut d = m;
                        let e = d[axis];
                        d[axis] -= 1;
                        add_term(&mut row, cols[&(kp, qp, d)], i64::from(e));
                    }
                    add_poly(
                        &mut row,
                        &cols,
                        kp + 1,
                        qp,
                        m,
                        &k.der(axis),
                        gamma - kp as i64,
                    );
                    add_poly(&mut row, &cols, kp, qp + 1, m, &q.der(axis), -(qp as i64));
                    pivot(row, &mut ps);
                }
            }
            if ambient >= 4 {
                for m in mons(ambient - 4) {
                    let mut row = Row::new();
                    add_term(&mut row, cols[&(kp, qp, m)], 1);
                    add_poly(&mut row, &cols, kp + 1, qp, m, k, -1);
                    pivot(row, &mut ps);
                }
            }
            if ambient >= 1 {
                for m in mons(ambient - 1) {
                    let mut row = Row::new();
                    add_term(&mut row, cols[&(kp, qp, m)], 1);
                    add_poly(&mut row, &cols, kp, qp + 1, m, q, -1);
                    pivot(row, &mut ps);
                }
            }
        }
    }
    low_count - ps.keys().filter(|&&x| x < low_count).count()
}

fn cayley_menger(x: i64, y: i64, z: i64) -> Poly {
    let c = Poly::var(0);
    let a = Poly::var(1);
    let b = Poly::var(2);
    let c2 = c.pow(2);
    let a2 = a.pow(2);
    let b2 = b.pow(2);
    let (x2, y2, z2) = (x * x, y * y, z * z);
    sum(&[
        a.pow(4).scale(x2),
        a2.mul(&b2).scale(-(x2 + y2 - z2)),
        b.pow(4).scale(y2),
        a2.scale(x2 * (x2 - y2 - z2)),
        c2.mul(&a2).scale(-x2 + y2 - z2),
        b2.scale(y2 * (y2 - x2 - z2)),
        c2.mul(&b2).scale(-y2 + x2 - z2),
        c.pow(4).scale(z2),
        c2.scale(z2 * (-x2 - y2 + z2)),
        Poly::con(z2 * x2 * y2),
    ])
}

fn main() {
    let c = Poly::var(0);
    let a = Poly::var(1);
    let b = Poly::var(2);
    let point = std::env::var("KINEMATIC_POINT").unwrap_or_else(|_| "A".to_owned());
    let (x, y, z) = match point.as_str() {
        "A" => (2_i64, 3_i64, 4_i64),
        "B" => (3_i64, 5_i64, 6_i64),
        _ => panic!("KINEMATIC_POINT must be A or B"),
    };
    let k = cayley_menger(x, y, z);
    let families = [
        ("q_g1", sum(&[c.clone(), b, Poly::con(x)]), 8_usize),
        ("q_g2", sum(&[c.clone(), a, Poly::con(y)]), 8_usize),
        ("q_G12", c.add(&Poly::con(x + y + z)), 16_usize),
    ];
    let kmax: usize = std::env::var("K_POLE")
        .ok()
        .map_or(2, |x| x.parse().unwrap());
    let qmax: usize = std::env::var("Q_POLE")
        .ok()
        .map_or(2, |x| x.parse().unwrap());
    let max_ambient: usize = std::env::var("MAX_AMBIENT")
        .ok()
        .map_or(12, |x| x.parse().unwrap());
    println!("schema=generic-q-pole-twisted-derham-rank-v1 gamma=5 point={point} xyz=({x},{y},{z}) k_pole={kmax} q_pole={qmax}");
    for ambient in 7..=max_ambient {
        for (name, q, target) in &families {
            let rank = rank_for(&k, q, kmax, qmax, ambient, 5);
            println!("ambient={ambient} family={name} filtered_rank={rank} target={target}");
        }
    }
}
