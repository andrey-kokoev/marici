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

fn parameter_derivative_unreduced(row: &Row, explicit_dot: &Row, r: &Reduction, kd: &Poly, qd: &[Poly; 3]) -> Row {
    let mut out = explicit_dot.clone();
    for (&col, &coef) in row {
        let (kp, qps, mon) = r.labels[col];
        if r.cols.contains_key(&(kp + 1, qps, mon)) {
            add_poly(&mut out, &r.cols, kp + 1, qps, mon, kd, mm(coef, 5 - kp as i64));
        }
        for qi in 0..3 {
            if qps[qi] > 0 {
                let mut next = qps;
                next[qi] += 1;
                if r.cols.contains_key(&(kp, next, mon)) {
                    add_poly(&mut out, &r.cols, kp, next, mon, &qd[qi], -mm(coef, qps[qi] as i64));
                }
            }
        }
    }
    out
}

fn parameter_derivative(row: &Row, explicit_dot: &Row, r: &Reduction, kd: &Poly, qd: &[Poly; 3]) -> Row {
    reduce(parameter_derivative_unreduced(row, explicit_dot, r, kd, qd), &r.pivots)
}

fn mixed_explicit_derivative(row: &Row, r: &Reduction, kxy: &Poly, qxy: &[Poly; 3]) -> Row {
    let mut out = Row::new();
    for (&col, &coef) in row {
        let (kp, qps, mon) = r.labels[col];
        if r.cols.contains_key(&(kp + 1, qps, mon)) {
            add_poly(&mut out, &r.cols, kp + 1, qps, mon, kxy, mm(coef, 5 - kp as i64));
        }
        for qi in 0..3 {
            if qps[qi] > 0 {
                let mut next = qps;
                next[qi] += 1;
                if r.cols.contains_key(&(kp, next, mon)) {
                    add_poly(&mut out, &r.cols, kp, next, mon, &qxy[qi], -mm(coef, qps[qi] as i64));
                }
            }
        }
    }
    out
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

fn parameter_k_mixed_derivative(x: i64, y: i64, z: i64, first: usize, second: usize) -> Poly {
    let mut out = Poly::default();
    for (first_offset, first_weight) in [(-2_i64, 1_i64), (-1, -8), (1, 8), (2, -1)] {
        for (second_offset, second_weight) in [(-2_i64, 1_i64), (-1, -8), (1, 8), (2, -1)] {
            let mut point = [x, y, z];
            point[first] += first_offset;
            point[second] += second_offset;
            out = out.add(
                &cayley_menger(point[0], point[1], point[2])
                    .scale(mm(first_weight, second_weight)),
            );
        }
    }
    out.scale(mm(inv(12), inv(12)))
}

fn localize_to_top(mut row: Row, mut mask: u8, reductions: &BTreeMap<u8, Reduction>, qs: &[Poly; 3]) -> Row {
    for bit in 0..3 {
        if mask & (1 << bit) == 0 {
            let next = mask | (1 << bit);
            row = localization_map(&row, &reductions[&mask], &reductions[&next], bit, &qs[bit]);
            mask = next;
        }
    }
    row
}

fn quotient_scalar(vector: Row, generator: &Row, boundary: &BTreeMap<usize, Row>) -> Option<i64> {
    let v = reduce(vector, boundary);
    let g = reduce(generator.clone(), boundary);
    let (&pivot_col, &gcoef) = g.iter().next_back()?;
    let scalar = mm(v.get(&pivot_col).copied().unwrap_or(0), inv(gcoef));
    let mut difference = v;
    for (&col, &coef) in &g {
        add_term(&mut difference, col, -mm(scalar, coef));
    }
    if difference.is_empty() { Some(scalar) } else { None }
}

fn signed_quartic(x: i64, y: i64, z: i64) -> i64 {
    let e = (x + y + z).rem_euclid(P);
    let a = mm((x - y - z).rem_euclid(P), (x - y + z).rem_euclid(P));
    let b = mm((x + y - z).rem_euclid(P), e);
    (4 * mm(a, b) - mm((a + b - mm(e, e)).rem_euclid(P), (a + b - mm(e, e)).rem_euclid(P))).rem_euclid(P)
}

fn scalar_parameter_derivative(f: fn(i64, i64, i64) -> i64, x: i64, y: i64, z: i64, axis: usize) -> i64 {
    let mut out = 0_i64;
    for (offset, weight) in [(-2_i64, 1_i64), (-1, -8), (1, 8), (2, -1)] {
        let mut point = [x, y, z];
        point[axis] += offset;
        out = (out + mm(weight, f(point[0], point[1], point[2]))).rem_euclid(P);
    }
    mm(out, inv(12))
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
    let (x, y, z) = if let Ok(raw) = std::env::var("KINEMATIC_XYZ") {
        let values: Vec<i64> = raw.split(',').map(|value| value.parse().unwrap()).collect();
        assert_eq!(values.len(), 3, "KINEMATIC_XYZ must contain x,y,z");
        (values[0], values[1], values[2])
    } else {
        match point.as_str() {
            "A" => (2_i64, 3_i64, 4_i64),
            "B" => (3_i64, 5_i64, 6_i64),
            _ => panic!("KINEMATIC_POINT must be A or B"),
        }
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

    // The boundary of the top mask is generated by its three codimension-one
    // deletion faces.  Reduce the literal constant-numerator top form and its
    // two derivatives modulo that boundary to obtain the descended line
    // connection without choosing a complement in the 21-dimensional space.
    let top = &final_reductions[&0b111];
    let mut boundary_pivots = BTreeMap::new();
    for (face, bit) in [(0b011_u8, 2_usize), (0b101, 1), (0b110, 0)] {
        let lower = &final_reductions[&face];
        for &monomial in &lower.survivors {
            let source = Row::from([(lower.cols[&(0, lower.target_q, monomial)], 1)]);
            pivot(localization_map(&source, lower, top, bit, &qs[bit]), &mut boundary_pivots);
        }
    }
    let omega = Row::from([(top.cols[&(0, [1, 1, 1], [0, 0, 0])], 1)]);
    let omega_mod_boundary = reduce(omega.clone(), &boundary_pivots);
    let (&quotient_pivot, &omega_pivot_coefficient) = omega_mod_boundary
        .iter()
        .next_back()
        .expect("literal top form must survive the boundary span");
    println!(
        "top_boundary_rank={} top_quotient_rank={} omega_survives={}",
        boundary_pivots.len(),
        top.rank - boundary_pivots.len(),
        !omega_mod_boundary.is_empty()
    );
    let mut boundary_derivatives = Vec::new();
    for (direction, kd, qd) in &directions {
        let derivative = parameter_derivative(&omega, &Row::new(), top, kd, qd);
        let derivative_mod_boundary = reduce(derivative.clone(), &boundary_pivots);
        let scalar = mm(
            derivative_mod_boundary.get(&quotient_pivot).copied().unwrap_or(0),
            inv(omega_pivot_coefficient),
        );
        let mut boundary_part = derivative;
        for (&column, &coefficient) in &omega {
            add_term(&mut boundary_part, column, -mm(scalar, coefficient));
        }
        let quotient_error = reduce(boundary_part.clone(), &boundary_pivots);
        let boundary_normal_form = reduce(boundary_part, &top.pivots);
        println!(
            "top_connection_direction={direction} quotient_scalar={scalar} descends={} boundary_part_nonzero={}",
            quotient_error.is_empty(),
            !boundary_normal_form.is_empty()
        );
        boundary_derivatives.push(boundary_normal_form);
    }
    let mut extension_rank_pivots = BTreeMap::new();
    for row in boundary_derivatives {
        pivot(row, &mut extension_rank_pivots);
    }
    println!("top_two_direction_boundary_extension_rank={}", extension_rank_pivots.len());

    if qmax >= 3 {
        let kxy = parameter_k_mixed_derivative(x, y, z, 0, 1);
        let qxy = [Poly::default(), Poly::default(), Poly::default()];
        let (_, kx, qx) = &directions[0];
        let (_, ky, qy) = &directions[1];
        let mut nonzero_curvatures = 0_usize;
        for &monomial in &top.survivors {
            let source = Row::from([(top.cols[&(0, top.target_q, monomial)], 1)]);
            let dx = parameter_derivative_unreduced(&source, &Row::new(), top, kx, qx);
            let dy = parameter_derivative_unreduced(&source, &Row::new(), top, ky, qy);
            let mixed_explicit = mixed_explicit_derivative(&source, top, &kxy, &qxy);
            let dy_dx = parameter_derivative(&dx, &mixed_explicit, top, ky, qy);
            let dx_dy = parameter_derivative(&dy, &mixed_explicit, top, kx, qx);
            let mut curvature = dy_dx;
            for (column, coefficient) in dx_dy {
                add_term(&mut curvature, column, -coefficient);
            }
            if !reduce(curvature, &top.pivots).is_empty() {
                nonzero_curvatures += 1;
            }
        }
        println!(
            "top_mixed_jet_generators_tested={} top_mixed_jet_nonzero_curvatures={} top_connection_flat={}",
            top.survivors.len(),
            nonzero_curvatures,
            nonzero_curvatures == 0
        );
    } else {
        println!("top_mixed_jet_skipped=true required_q_pole_depth=3 actual_q_pole_depth={qmax}");
    }

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
    let top = &final_reductions[&0b111];
    let mut boundary = BTreeMap::new();
    for face in [0b011_u8, 0b101, 0b110] {
        let reduction = &final_reductions[&face];
        for &mon in &reduction.survivors {
            let source = Row::from([(reduction.cols[&(0, reduction.target_q, mon)], 1)]);
            pivot(localize_to_top(source, face, &final_reductions, &qs), &mut boundary);
        }
    }
    let omega = Row::from([(top.cols[&(0, top.target_q, [0, 0, 0])], 1)]);
    println!("proper_top boundary_rank={} quotient_rank={}", boundary.len(), top.rank - boundary.len());
    let q_value = signed_quartic(x, y, z);
    for (axis, (direction, kd, qd)) in directions.iter().enumerate() {
        let connection = parameter_derivative(&omega, &Row::new(), top, kd, qd);
        let scalar = quotient_scalar(connection, &omega, &boundary);
        let q_dot = scalar_parameter_derivative(signed_quartic, x, y, z, axis);
        let half_dlog_q = mm(q_dot, mm(inv(2), inv(q_value)));
        println!(
            "proper_top direction={direction} connection_scalar={scalar:?} half_dlog_Q={half_dlog_q} matches_plus={} matches_minus={}",
            scalar == Some(half_dlog_q),
            scalar == Some((-half_dlog_q).rem_euclid(P))
        );
    }
}
