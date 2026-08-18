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

fn reduce(mut row: Row, ps: &BTreeMap<usize, Row>) -> Row {
    let mut remainder = Row::new();
    loop {
        let Some((&col, &coefficient)) = row.iter().next_back() else {
            return remainder;
        };
        if let Some(existing) = ps.get(&col) {
            for (&column, &value) in existing {
                add_term(&mut row, column, -mm(coefficient, value));
            }
        } else {
            row.remove(&col);
            remainder.insert(col, coefficient);
        }
    }
}
fn add_poly(
    row: &mut Row,
    cols: &HashMap<(usize, [usize; 3], Mon), usize>,
    kp: usize,
    qps: [usize; 3],
    base: Mon,
    poly: &Poly,
    scale: i64,
) {
    for (m, c) in &poly.0 {
        let term = [base[0] + m[0], base[1] + m[1], base[2] + m[2]];
        add_term(row, cols[&(kp, qps, term)], mm(*c, scale));
    }
}

fn q_states(mask: u8, qmax: usize, include_boundary: bool) -> Vec<[usize; 3]> {
    let stop = if include_boundary { qmax } else { qmax - 1 };
    let bounds = [
        if mask & 1 != 0 { stop } else { 0 },
        if mask & 2 != 0 { stop } else { 0 },
        if mask & 4 != 0 { stop } else { 0 },
    ];
    let mut states = Vec::new();
    for q0 in 0..=bounds[0] {
        for q1 in 0..=bounds[1] {
            for q2 in 0..=bounds[2] {
                states.push([q0, q1, q2]);
            }
        }
    }
    states
}

struct Reduction {
    rank: usize,
    survivors: Vec<Mon>,
    labels: Vec<(usize, [usize; 3], Mon)>,
    cols: HashMap<(usize, [usize; 3], Mon), usize>,
    pivots: BTreeMap<usize, Row>,
    target_q: [usize; 3],
}

fn rank_for(
    k: &Poly,
    qs: &[Poly; 3],
    mask: u8,
    kmax: usize,
    qmax: usize,
    ambient: usize,
    cutoff: usize,
) -> Reduction {
    let column_degree = ambient + 3;
    let low = mons(cutoff);
    let all = mons(column_degree);
    let target_q = [
        usize::from(mask & 1 != 0),
        usize::from(mask & 2 != 0),
        usize::from(mask & 4 != 0),
    ];
    let mut labels = Vec::new();
    labels.extend(low.iter().map(|m| (0, target_q, *m)));
    for kp in 0..=kmax {
        for qps in q_states(mask, qmax, true) {
            for m in &all {
                if !(kp == 0 && qps == target_q && low.contains(m)) {
                    labels.push((kp, qps, *m));
                }
            }
        }
    }
    let cols: HashMap<_, _> = labels.iter().enumerate().map(|(i, x)| (*x, i)).collect();
    let mut ps = BTreeMap::new();
    let gamma = 5_i64;

    for kp in 0..kmax {
        for qps in q_states(mask, qmax, false) {
            for axis in 0..NV {
                for m in mons(ambient) {
                    let mut row = Row::new();
                    if m[axis] > 0 {
                        let mut d = m;
                        let e = d[axis];
                        d[axis] -= 1;
                        add_term(&mut row, cols[&(kp, qps, d)], i64::from(e));
                    }
                    add_poly(
                        &mut row,
                        &cols,
                        kp + 1,
                        qps,
                        m,
                        &k.der(axis),
                        gamma - kp as i64,
                    );
                    for qi in 0..3 {
                        if mask & (1 << qi) != 0 {
                            let mut next = qps;
                            next[qi] += 1;
                            add_poly(
                                &mut row,
                                &cols,
                                kp,
                                next,
                                m,
                                &qs[qi].der(axis),
                                -(qps[qi] as i64),
                            );
                        }
                    }
                    pivot(row, &mut ps);
                }
            }
            if ambient >= 4 {
                for m in mons(ambient - 4) {
                    let mut row = Row::new();
                    add_term(&mut row, cols[&(kp, qps, m)], 1);
                    add_poly(&mut row, &cols, kp + 1, qps, m, k, -1);
                    pivot(row, &mut ps);
                }
            }
            if ambient >= 1 {
                for qi in 0..3 {
                    if mask & (1 << qi) == 0 {
                        continue;
                    }
                    for m in mons(ambient - 1) {
                        let mut row = Row::new();
                        add_term(&mut row, cols[&(kp, qps, m)], 1);
                        let mut next = qps;
                        next[qi] += 1;
                        add_poly(&mut row, &cols, kp, next, m, &qs[qi], -1);
                        pivot(row, &mut ps);
                    }
                }
            }
        }
    }
    let survivors: Vec<_> = low
        .iter()
        .enumerate()
        .filter(|(column, _)| !ps.contains_key(column))
        .map(|(_, monomial)| *monomial)
        .collect();
    Reduction {
        rank: survivors.len(),
        survivors,
        labels,
        cols,
        pivots: ps,
        target_q,
    }
}

fn localization_map(row: &Row, lower: &Reduction, higher: &Reduction, bit: usize, q: &Poly) -> Row {
    let mut image = Row::new();
    for (&column, &coefficient) in row {
        let (kp, mut qps, monomial) = lower.labels[column];
        qps[bit] = 1;
        for (factor_monomial, factor_coefficient) in &q.0 {
            let term = [
                monomial[0] + factor_monomial[0],
                monomial[1] + factor_monomial[1],
                monomial[2] + factor_monomial[2],
            ];
            add_term(
                &mut image,
                higher.cols[&(kp, qps, term)],
                mm(coefficient, *factor_coefficient),
            );
        }
    }
    reduce(image, &higher.pivots)
}

fn parameter_derivative(row: &Row, explicit_dot: &Row, r: &Reduction, kd: &Poly, qd: &[Poly; 3]) -> Row {
    let mut out = explicit_dot.clone();
    for (&col, &coef) in row {
        let (kp, qps, mon) = r.labels[col];
        if kp < 2 {
            add_poly(&mut out, &r.cols, kp + 1, qps, mon, kd, mm(coef, 5 - kp as i64));
        }
        for qi in 0..3 {
            if qps[qi] > 0 && qps[qi] < 2 {
                let mut next = qps;
                next[qi] += 1;
                add_poly(&mut out, &r.cols, kp, next, mon, &qd[qi], -mm(coef, qps[qi] as i64));
            }
        }
    }
    reduce(out, &r.pivots)
}

fn localized_jet(row: &Row, lower: &Reduction, higher: &Reduction, bit: usize, q: &Poly, qd: &Poly) -> (Row, Row) {
    let (mut value, mut dot) = (Row::new(), Row::new());
    for (&col, &coef) in row {
        let (kp, mut qps, mon) = lower.labels[col];
        qps[bit] = 1;
        add_poly(&mut value, &higher.cols, kp, qps, mon, q, coef);
        add_poly(&mut dot, &higher.cols, kp, qps, mon, qd, coef);
    }
    (value, dot)
}

fn parameter_k_derivative(x: i64, y: i64, z: i64, axis: usize) -> Poly {
    let mut out = Poly::default();
    for (offset, weight) in [(-2_i64, 1_i64), (-1, -8), (1, 8), (2, -1)] {
        let mut point = [x, y, z];
        point[axis] += offset;
        out = out.add(&cayley_menger(point[0], point[1], point[2]).scale(weight));
    }
    out.scale(inv(12))
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
    let qs = [
        sum(&[c.clone(), b, Poly::con(x)]),
        sum(&[c.clone(), a, Poly::con(y)]),
        c.add(&Poly::con(x + y + z)),
    ];
    let families = [
        ("empty", 0b000_u8, 7_usize),
        ("q_g1", 0b001_u8, 8_usize),
        ("q_g2", 0b010_u8, 8_usize),
        ("q_g1_q_g2", 0b011_u8, 9_usize),
        ("q_G12", 0b100_u8, 16_usize),
        ("q_g1_q_G12", 0b101_u8, 18_usize),
        ("q_g2_q_G12", 0b110_u8, 18_usize),
        ("q_g1_q_g2_q_G12", 0b111_u8, 21_usize),
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
    let mut final_reductions = BTreeMap::new();
    for ambient in 7..=max_ambient {
        for (name, mask, target) in &families {
            let reduction = rank_for(&k, &qs, *mask, kmax, qmax, ambient, 5);
            println!(
                "ambient={ambient} mask={mask:03b} family={name} filtered_rank={} target={target}",
                reduction.rank
            );
            if ambient == max_ambient {
                println!("basis mask={mask:03b} monomials={:?}", reduction.survivors);
                final_reductions.insert(*mask, reduction);
            }
        }
    }
    for lower_mask in 0_u8..8 {
        for bit in 0..3 {
            if lower_mask & (1 << bit) != 0 {
                continue;
            }
            let higher_mask = lower_mask | (1 << bit);
            let lower = &final_reductions[&lower_mask];
            let higher = &final_reductions[&higher_mask];
            let mut image_pivots = BTreeMap::new();
            for &monomial in &lower.survivors {
                let source = Row::from([(lower.cols[&(0, lower.target_q, monomial)], 1)]);
                let image = localization_map(&source, lower, higher, bit, &qs[bit]);
                pivot(image, &mut image_pivots);
            }
            println!(
                "edge={lower_mask:03b}->{higher_mask:03b} image_rank={} source_rank={} injective={}",
                image_pivots.len(),
                lower.rank,
                image_pivots.len() == lower.rank
            );
        }
    }
    for base in 0_u8..8 {
        let missing: Vec<_> = (0..3).filter(|bit| base & (1 << bit) == 0).collect();
        for left_index in 0..missing.len() {
            for right_index in left_index + 1..missing.len() {
                let i = missing[left_index];
                let j = missing[right_index];
                let left_mask = base | (1 << i);
                let right_mask = base | (1 << j);
                let top_mask = base | (1 << i) | (1 << j);
                let source_reduction = &final_reductions[&base];
                let mut equal = true;
                for &monomial in &source_reduction.survivors {
                    let source = Row::from([(
                        source_reduction.cols[&(0, source_reduction.target_q, monomial)],
                        1,
                    )]);
                    let left = localization_map(
                        &source,
                        source_reduction,
                        &final_reductions[&left_mask],
                        i,
                        &qs[i],
                    );
                    let left_top = localization_map(
                        &left,
                        &final_reductions[&left_mask],
                        &final_reductions[&top_mask],
                        j,
                        &qs[j],
                    );
                    let right = localization_map(
                        &source,
                        source_reduction,
                        &final_reductions[&right_mask],
                        j,
                        &qs[j],
                    );
                    let right_top = localization_map(
                        &right,
                        &final_reductions[&right_mask],
                        &final_reductions[&top_mask],
                        i,
                        &qs[i],
                    );
                    equal &= left_top == right_top;
                }
                println!("square={base:03b} bits={i},{j} path_independent={equal}");
            }
        }
    }
    let directions = [
        ("x", parameter_k_derivative(x, y, z, 0), [Poly::con(1), Poly::default(), Poly::con(1)]),
        ("y", parameter_k_derivative(x, y, z, 1), [Poly::default(), Poly::con(1), Poly::con(1)]),
    ];
    for (direction, kd, qd) in &directions {
        for lower_mask in 0_u8..8 {
            for bit in 0..3 {
                if lower_mask & (1 << bit) != 0 { continue; }
                let higher_mask = lower_mask | (1 << bit);
                let lower = &final_reductions[&lower_mask];
                let higher = &final_reductions[&higher_mask];
                let mut natural = true;
                for &mon in &lower.survivors {
                    let source = Row::from([(lower.cols[&(0, lower.target_q, mon)], 1)]);
                    let conn = parameter_derivative(&source, &Row::new(), lower, kd, qd);
                    let right = localization_map(&conn, lower, higher, bit, &qs[bit]);
                    let (localized, explicit_dot) = localized_jet(&source, lower, higher, bit, &qs[bit], &qd[bit]);
                    let left = parameter_derivative(&localized, &explicit_dot, higher, kd, qd);
                    natural &= left == right;
                }
                println!("connection_direction={direction} edge={lower_mask:03b}->{higher_mask:03b} natural={natural}");
            }
        }
    }
}
