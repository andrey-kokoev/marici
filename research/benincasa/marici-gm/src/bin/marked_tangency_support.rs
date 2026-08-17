use std::collections::{BTreeMap, BTreeSet};

const P: u64 = 2_305_843_009_213_693_951;

#[derive(Clone, Copy, Debug, PartialEq, Eq)]
struct F(u64);
impl F {
    fn n(v: u64) -> Self {
        Self(v % P)
    }
    fn z() -> Self {
        Self(0)
    }
    fn o() -> Self {
        Self(1)
    }
    fn add(self, b: Self) -> Self {
        Self::n(((self.0 as u128 + b.0 as u128) % P as u128) as u64)
    }
    fn neg(self) -> Self {
        if self.0 == 0 {
            self
        } else {
            Self(P - self.0)
        }
    }
    fn sub(self, b: Self) -> Self {
        self.add(b.neg())
    }
    fn mul(self, b: Self) -> Self {
        Self::n(((self.0 as u128 * b.0 as u128) % P as u128) as u64)
    }
    fn pow(mut self, mut n: u64) -> Self {
        let mut r = Self::o();
        while n > 0 {
            if n & 1 == 1 {
                r = r.mul(self)
            }
            self = self.mul(self);
            n >>= 1;
        }
        r
    }
    fn inv(self) -> Self {
        assert_ne!(self.0, 0);
        self.pow(P - 2)
    }
}

#[derive(Clone, Copy)]
struct D {
    x: F,
    d: F,
}
impl D {
    fn c(x: F) -> Self {
        Self { x, d: F::z() }
    }
    fn var(x: F) -> Self {
        Self { x, d: F::o() }
    }
    fn add(self, b: Self) -> Self {
        Self {
            x: self.x.add(b.x),
            d: self.d.add(b.d),
        }
    }
    fn neg(self) -> Self {
        Self {
            x: self.x.neg(),
            d: self.d.neg(),
        }
    }
    fn sub(self, b: Self) -> Self {
        self.add(b.neg())
    }
    fn mul(self, b: Self) -> Self {
        Self {
            x: self.x.mul(b.x),
            d: self.d.mul(b.x).add(self.x.mul(b.d)),
        }
    }
    fn sq(self) -> Self {
        self.mul(self)
    }
}

type Mon = (u8, u8);
#[derive(Clone, Debug)]
struct Poly(BTreeMap<Mon, F>);
impl Poly {
    fn zero() -> Self {
        Self(BTreeMap::new())
    }
    fn mon(i: u8, j: u8, c: F) -> Self {
        let mut q = Self::zero();
        if c.0 != 0 {
            q.0.insert((i, j), c);
        }
        q
    }
    fn c(c: F) -> Self {
        Self::mon(0, 0, c)
    }
    fn add(&self, b: &Self) -> Self {
        let mut r = self.clone();
        for (m, c) in &b.0 {
            let v = r.0.get(m).copied().unwrap_or(F::z()).add(*c);
            if v.0 == 0 {
                r.0.remove(m);
            } else {
                r.0.insert(*m, v);
            }
        }
        r
    }
    fn neg(&self) -> Self {
        Self(self.0.iter().map(|(m, c)| (*m, c.neg())).collect())
    }
    fn sub(&self, b: &Self) -> Self {
        self.add(&b.neg())
    }
    fn scale(&self, c: F) -> Self {
        if c.0 == 0 {
            return Self::zero();
        }
        Self(self.0.iter().map(|(m, v)| (*m, v.mul(c))).collect())
    }
    fn mul(&self, b: &Self) -> Self {
        let mut r = Self::zero();
        for ((i, j), c) in &self.0 {
            for ((k, l), d) in &b.0 {
                let m = (i + k, j + l);
                let v = r.0.get(&m).copied().unwrap_or(F::z()).add(c.mul(*d));
                if v.0 == 0 {
                    r.0.remove(&m);
                } else {
                    r.0.insert(m, v);
                }
            }
        }
        r
    }
    fn pow(&self, n: u8) -> Self {
        let mut r = Self::c(F::o());
        for _ in 0..n {
            r = r.mul(self)
        }
        r
    }
    fn da(&self) -> Self {
        let mut r = Self::zero();
        for ((i, j), c) in &self.0 {
            if *i > 0 {
                r.0.insert((i - 1, *j), c.mul(F::n(*i as u64)));
            }
        }
        r
    }
    fn db(&self) -> Self {
        let mut r = Self::zero();
        for ((i, j), c) in &self.0 {
            if *j > 0 {
                r.0.insert((*i, j - 1), c.mul(F::n(*j as u64)));
            }
        }
        r
    }
    fn eval(&self, a: F, b: F) -> F {
        self.0.iter().fold(F::z(), |z,((i,j),c)| {
            z.add(c.mul(a.pow(*i as u64)).mul(b.pow(*j as u64)))
        })
    }
}

struct Geometry {
    k: Poly,
    kp: Poly,
    k1: Poly,
    k1p: Poly,
    l1: Poly,
    l2: Poly,
    l1p: F,
    l2p: F,
}

fn geometry(uu: u64, vv: u64, axis: char) -> Geometry {
    let two = F::n(2);
    let half = two.inv();
    let one = F::o();
    let u = if axis == 'u' {
        D::var(F::n(uu))
    } else {
        D::c(F::n(uu))
    };
    let v = if axis == 'v' {
        D::var(F::n(vv))
    } else {
        D::c(F::n(vv))
    };
    let x = D::c(one);
    let y = u.add(v).mul(D::c(half)).sub(x);
    let z = u.sub(v).mul(D::c(half));
    let c = u.neg();
    let h = x.sq().add(y.sq()).sub(z.sq());
    let ga = x
        .sq()
        .sub(c.sq())
        .mul(x.sq().sub(y.sq()).sub(z.sq()))
        .sub(c.sq().mul(z.sq()).mul(D::c(two)));
    let gb = y
        .sq()
        .sub(c.sq())
        .mul(y.sq().sub(x.sq()).sub(z.sq()))
        .sub(c.sq().mul(z.sq()).mul(D::c(two)));
    let hh = z.sq().mul(
        c.sq()
            .sub(y.sq())
            .mul(c.sq().sub(x.sq()))
            .add(c.sq().mul(z.sq())),
    );
    let mut k = Poly::zero();
    let mut kp = Poly::zero();
    for (m, q) in [
        ((4, 0), x.sq()),
        ((2, 2), h.neg()),
        ((0, 4), y.sq()),
        ((2, 0), ga),
        ((0, 2), gb),
        ((0, 0), hh),
    ] {
        if q.x.0 != 0 {
            k.0.insert(m, q.x);
        }
        if q.d.0 != 0 {
            kp.0.insert(m, q.d);
        }
    }
    let k1a = c.mul(D::c(two.neg())).mul(x.sq().sub(y.sq()).add(z.sq()));
    let k1b = c.mul(D::c(two.neg())).mul(y.sq().sub(x.sq()).add(z.sq()));
    let k1h = c
        .mul(D::c(two))
        .mul(z.sq())
        .mul(c.sq().mul(D::c(two)).sub(x.sq()).sub(y.sq()).add(z.sq()));
    let mut k1 = Poly::zero();
    let mut k1p = Poly::zero();
    for (m, q) in [((2, 0), k1a), ((0, 2), k1b), ((0, 0), k1h)] {
        if q.x.0 != 0 {
            k1.0.insert(m, q.x);
        }
        if q.d.0 != 0 {
            k1p.0.insert(m, q.d);
        }
    }
    let l1 = Poly::mon(0, 1, one).add(&Poly::c(one.sub(u.x)));
    let l2 = Poly::mon(1, 0, one).add(&Poly::c(v.x.sub(u.x).mul(half).sub(one)));
    Geometry {
        k,
        kp,
        k1,
        k1p,
        l1,
        l2,
        l1p: u.d.neg(),
        l2p: v.d.sub(u.d).mul(half),
    }
}

#[derive(Clone)]
struct Class {
    a: u8,
    b: u8,
    h: u8,
    n: Poly,
    np: Poly,
}
fn classes(g: &Geometry) -> Vec<Class> {
    let one = Poly::c(F::o());
    let aa = Poly::mon(1, 0, F::o());
    let bb = Poly::mon(0, 1, F::o());
    let half = F::n(2).inv();
    let double = |m: &Poly| Class {
        a: 0,
        b: 0,
        h: 3,
        n: m.mul(&g.k1).scale(half.neg()),
        np: m.mul(&g.k1p).scale(half.neg()),
    };
    vec![
        Class {
            a: 1,
            b: 1,
            h: 1,
            n: one.clone(),
            np: Poly::zero(),
        },
        Class {
            a: 1,
            b: 0,
            h: 1,
            n: one.clone(),
            np: Poly::zero(),
        },
        Class {
            a: 0,
            b: 1,
            h: 1,
            n: one.clone(),
            np: Poly::zero(),
        },
        Class {
            a: 0,
            b: 0,
            h: 1,
            n: aa.mul(&bb),
            np: Poly::zero(),
        },
        Class {
            a: 0,
            b: 0,
            h: 1,
            n: aa.clone(),
            np: Poly::zero(),
        },
        double(&aa),
        Class {
            a: 0,
            b: 0,
            h: 1,
            n: bb.clone(),
            np: Poly::zero(),
        },
        double(&bb),
        double(&one),
        Class {
            a: 0,
            b: 0,
            h: 1,
            n: one.clone(),
            np: Poly::zero(),
        },
        Class {
            a: 0,
            b: 0,
            h: 1,
            n: aa.pow(2),
            np: Poly::zero(),
        },
        Class {
            a: 0,
            b: 0,
            h: 1,
            n: bb.pow(2),
            np: Poly::zero(),
        },
    ]
}
fn common(g: &Geometry, q: &Class) -> Poly {
    q.n.mul(&g.l1.pow(2 - q.a))
        .mul(&g.l2.pow(2 - q.b))
        .mul(&g.k.pow((5 - q.h) / 2))
}
fn target(g: &Geometry, q: &Class) -> Poly {
    let ea = 2 - q.a;
    let eb = 2 - q.b;
    let ek = (5 - q.h) / 2;
    let mut r = q.np.mul(&g.l1.pow(ea)).mul(&g.l2.pow(eb)).mul(&g.k.pow(ek));
    if q.a > 0 {
        r = r.sub(
            &q.n.mul(&g.l1.pow(ea - 1))
                .mul(&g.l2.pow(eb))
                .mul(&g.k.pow(ek))
                .scale(g.l1p.mul(F::n(q.a as u64))),
        )
    }
    if q.b > 0 {
        r = r.sub(
            &q.n.mul(&g.l1.pow(ea))
                .mul(&g.l2.pow(eb - 1))
                .mul(&g.k.pow(ek))
                .scale(g.l2p.mul(F::n(q.b as u64))),
        )
    }
    r.sub(
        &q.n.mul(&g.l1.pow(ea))
            .mul(&g.l2.pow(eb))
            .mul(&g.kp)
            .mul(&g.k.pow(ek - 1))
            .scale(F::n(q.h as u64).mul(F::n(2).inv())),
    )
}
fn monomials(d: u8) -> Vec<Mon> {
    let mut z = Vec::new();
    for s in 0..=d {
        for i in 0..=s {
            z.push((i, s - i));
        }
    }
    z
}
fn exact(g: &Geometry, sa: u8, sb: u8, m: Mon, is_q: bool) -> Poly {
    let f = Poly::mon(m.0, m.1, F::o());
    let ea = 2 - sa;
    let eb = 2 - sb;
    let base = g.l1.pow(ea).mul(&g.l2.pow(eb));
    let k1 = g.k.clone();
    let half = F::n(2).inv();
    if !is_q {
        let mut z = f.db().neg().mul(&base).mul(&k1);
        if sa > 0 {
            z = z.add(
                &f.mul(&g.l1.pow(ea - 1))
                    .mul(&g.l2.pow(eb))
                    .mul(&k1)
                    .scale(F::n(sa as u64)),
            )
        }
        z.add(&f.mul(&base).mul(&g.k.db()).scale(F::n(3).mul(half)))
    } else {
        let mut z = f.da().mul(&base).mul(&k1);
        if sb > 0 {
            z = z.sub(
                &f.mul(&g.l1.pow(ea))
                    .mul(&g.l2.pow(eb - 1))
                    .mul(&k1)
                    .scale(F::n(sb as u64)),
            )
        }
        z.sub(&f.mul(&base).mul(&g.k.da()).scale(F::n(3).mul(half)))
    }
}

#[allow(dead_code)]
struct Sol {
    rank: usize,
    fixed: Vec<bool>,
    values: Vec<F>,
    residual_zero: bool,
    equations: usize,
    unknowns: usize,
    gauge_rank: usize,
    gauge_pivot_mask: u16,
    gauge_rref: Vec<Vec<F>>,
}
fn solve(g: &Geometry, master: usize, degree: u8) -> Sol {
    let cs = classes(g);
    let mut cols: Vec<Poly> = cs.iter().map(|q| common(g, q)).collect();
    for (sa, sb) in [(1, 1), (1, 0), (0, 1), (0, 0)] {
        for m in monomials(degree) {
            cols.push(exact(g, sa, sb, m, false));
            cols.push(exact(g, sa, sb, m, true));
        }
    }
    let rhs = target(g, &cs[master]);
    let mut mons = BTreeSet::new();
    for q in &cols {
        mons.extend(q.0.keys().copied())
    }
    mons.extend(rhs.0.keys().copied());
    let n = cols.len();
    let mut a: Vec<Vec<F>> = mons
        .iter()
        .map(|m| {
            let mut r: Vec<F> = cols
                .iter()
                .map(|q| q.0.get(m).copied().unwrap_or(F::z()))
                .collect();
            r.push(rhs.0.get(m).copied().unwrap_or(F::z()));
            r
        })
        .collect();
    let rows = a.len();
    let mut piv = Vec::new();
    let mut rr = 0;
    for c in 0..n {
        let Some(p) = (rr..rows).find(|&i| a[i][c].0 != 0) else {
            continue;
        };
        a.swap(rr, p);
        let inv = a[rr][c].inv();
        for j in c..=n {
            a[rr][j] = a[rr][j].mul(inv)
        }
        for i in 0..rows {
            if i != rr && a[i][c].0 != 0 {
                let f = a[i][c];
                for j in c..=n {
                    a[i][j] = a[i][j].sub(f.mul(a[rr][j]));
                }
            }
        }
        piv.push((rr, c));
        rr += 1;
        if rr == rows {
            break;
        }
    }
    assert!(
        (0..rows).all(|i| !(0..n).all(|j| a[i][j].0 == 0) || a[i][n].0 == 0),
        "inconsistent master={master} degree={degree} equations={rows} unknowns={n}"
    );
    let pivot_cols: BTreeSet<usize> = piv.iter().map(|(_, c)| *c).collect();
    let free: Vec<usize> = (0..n).filter(|c| !pivot_cols.contains(c)).collect();
    let mut fixed = vec![false; 12];
    let mut values = vec![F::z(); 12];
    for (row, col) in &piv {
        if *col < 12 {
            fixed[*col] = free.iter().all(|j| a[*row][*j].0 == 0);
            values[*col] = a[*row][n];
        }
    }
    let mut x = vec![F::z(); n];
    for (row, col) in &piv {
        x[*col] = a[*row][n]
    }
    let mut check = Poly::zero();
    for (q, c) in cols.iter().zip(x) {
        check = check.add(&q.scale(c))
    }
    // Project the homogeneous solution space to the twelve master
    // coordinates.  Its row space is independent of a choice of affine
    // section, so rank and pivot columns are gauge-invariant Pluecker data.
    let mut gauge = Vec::<Vec<F>>::new();
    for j in &free {
        let mut v = vec![F::z(); 12];
        if *j < 12 {
            v[*j] = F::o();
        }
        for (row, col) in &piv {
            if *col < 12 {
                v[*col] = a[*row][*j].neg();
            }
        }
        if v.iter().any(|q| q.0 != 0) {
            gauge.push(v);
        }
    }
    let mut gr = 0usize;
    let mut gauge_pivot_mask = 0u16;
    for c in 0..12 {
        let Some(p) = (gr..gauge.len()).find(|&i| gauge[i][c].0 != 0) else {
            continue;
        };
        gauge.swap(gr, p);
        let inv = gauge[gr][c].inv();
        for k in c..12 {
            gauge[gr][k] = gauge[gr][k].mul(inv);
        }
        for i in 0..gauge.len() {
            if i != gr && gauge[i][c].0 != 0 {
                let f = gauge[i][c];
                for k in c..12 {
                    gauge[i][k] = gauge[i][k].sub(f.mul(gauge[gr][k]));
                }
            }
        }
        gauge_pivot_mask |= 1u16 << c;
        gr += 1;
        if gr == gauge.len() {
            break;
        }
    }
    Sol {
        rank: rr,
        fixed,
        values,
        residual_zero: check.sub(&rhs).0.is_empty(),
        equations: rows,
        unknowns: n,
        gauge_rank: gr,
        gauge_pivot_mask,
        gauge_rref: gauge[..gr].to_vec(),
    }
}

fn gauge_plucker(sol: &Sol) -> Vec<F> {
    assert_eq!(sol.gauge_rank, 2);
    let cols = [3usize, 4, 5, 6, 7];
    let mut out = Vec::new();
    for i in 0..cols.len() {
        for j in i + 1..cols.len() {
            out.push(
                sol.gauge_rref[0][cols[i]]
                    .mul(sol.gauge_rref[1][cols[j]])
                    .sub(sol.gauge_rref[0][cols[j]].mul(sol.gauge_rref[1][cols[i]])),
            );
        }
    }
    assert_eq!(out[0], F::o());
    out
}

fn rational_jet(samples: &[(F, F)], max_degree: usize) -> Option<(F, F, usize, usize)> {
    for total in 0..=2 * max_degree {
        for nd in 0..=max_degree.min(total) {
            let dd = total - nd;
            if dd > max_degree {
                continue;
            }
            let nv = nd + 1 + dd;
            if samples.len() < nv + 4 {
                continue;
            }
            let mut a = Vec::new();
            for (t, y) in samples {
                let mut row = Vec::with_capacity(nv + 1);
                let mut q = F::o();
                for _ in 0..=nd {
                    row.push(q);
                    q = q.mul(*t)
                }
                q = *t;
                for _ in 1..=dd {
                    row.push(y.neg().mul(q));
                    q = q.mul(*t)
                }
                row.push(*y);
                a.push(row);
            }
            let rows = a.len();
            let mut rr = 0;
            let mut piv = Vec::new();
            for c in 0..nv {
                let Some(p) = (rr..rows).find(|&i| a[i][c].0 != 0) else {
                    continue;
                };
                a.swap(rr, p);
                let z = a[rr][c].inv();
                for j in c..=nv {
                    a[rr][j] = a[rr][j].mul(z)
                }
                for i in 0..rows {
                    if i != rr && a[i][c].0 != 0 {
                        let f = a[i][c];
                        for j in c..=nv {
                            a[i][j] = a[i][j].sub(f.mul(a[rr][j]));
                        }
                    }
                }
                piv.push((rr, c));
                rr += 1;
                if rr == rows {
                    break;
                }
            }
            if (0..rows).any(|i| (0..nv).all(|j| a[i][j].0 == 0) && a[i][nv].0 != 0)
                || piv.len() != nv
            {
                continue;
            }
            let mut x = vec![F::z(); nv];
            for (r, c) in piv {
                x[c] = a[r][nv]
            }
            let n0 = x[0];
            let n1 = if nd >= 1 { x[1] } else { F::z() };
            let d1 = if dd >= 1 { x[nd + 1] } else { F::z() };
            return Some((n0, n1.sub(n0.mul(d1)), nd, dd));
        }
    }
    None
}

fn shifted_rational_jet(samples: &[(F, F)], max_degree: usize, max_shift: usize) -> (usize, (F, F, usize, usize)) {
    for shift in 0..=max_shift {
        let shifted = samples.iter().map(|(t,y)| (*t, y.mul(t.pow(shift as u64)))).collect::<Vec<_>>();
        if let Some(jet) = rational_jet(&shifted, max_degree) {
            return (shift, jet);
        }
    }
    panic!("no bounded shifted rational jet through shift {max_shift}")
}

fn rational_fit(samples: &[(F, F)], max_degree: usize) -> (Vec<F>, Vec<F>) {
    for total in 0..=2 * max_degree {
        for nd in 0..=max_degree.min(total) {
            let dd = total - nd;
            if dd > max_degree {
                continue;
            }
            let nv = nd + 1 + dd;
            if samples.len() < nv + 4 {
                continue;
            }
            let mut a = Vec::new();
            for (q, y) in samples {
                let mut row = Vec::with_capacity(nv + 1);
                let mut z = F::o();
                for _ in 0..=nd {
                    row.push(z);
                    z = z.mul(*q)
                }
                z = *q;
                for _ in 1..=dd {
                    row.push(y.neg().mul(z));
                    z = z.mul(*q)
                }
                row.push(*y);
                a.push(row);
            }
            let rows = a.len();
            let mut rr = 0;
            let mut piv = Vec::new();
            for c in 0..nv {
                let Some(p) = (rr..rows).find(|&j| a[j][c].0 != 0) else {
                    continue;
                };
                a.swap(rr, p);
                let inv = a[rr][c].inv();
                for j in c..=nv {
                    a[rr][j] = a[rr][j].mul(inv)
                }
                for j in 0..rows {
                    if j != rr && a[j][c].0 != 0 {
                        let f = a[j][c];
                        for k in c..=nv {
                            a[j][k] = a[j][k].sub(f.mul(a[rr][k]))
                        }
                    }
                }
                piv.push((rr, c));
                rr += 1;
                if rr == rows {
                    break;
                }
            }
            if (0..rows).any(|j| (0..nv).all(|k| a[j][k].0 == 0) && a[j][nv].0 != 0)
                || piv.len() != nv
            {
                continue;
            }
            let mut x = vec![F::z(); nv];
            for (j, c) in piv {
                x[c] = a[j][nv]
            }
            let num = x[..=nd].to_vec();
            let mut den = vec![F::o()];
            den.extend_from_slice(&x[nd + 1..]);
            return (num, den);
        }
    }
    panic!("no bounded rational fit")
}
fn peval(p: &[F], x: F) -> F {
    p.iter().rev().fold(F::z(), |a, c| a.mul(x).add(*c))
}

fn trim(p: &mut Vec<F>) {
    while p.len() > 1 && p.last() == Some(&F::z()) {
        p.pop();
    }
}
fn divide_linear(p: &[F], root: F) -> Vec<F> {
    assert!(p.len() > 1);
    let n = p.len() - 1;
    let mut q = vec![F::z(); n];
    q[n - 1] = p[n];
    for k in (1..n).rev() {
        q[k - 1] = p[k].add(root.mul(q[k]))
    }
    assert_eq!(p[0].add(root.mul(q[0])), F::z());
    q
}

fn vadd(a: &[F], b: &[F]) -> Vec<F> {
    let mut r = vec![F::z(); a.len().max(b.len())];
    for (i,q) in a.iter().enumerate() { r[i] = r[i].add(*q); }
    for (i,q) in b.iter().enumerate() { r[i] = r[i].add(*q); }
    trim(&mut r);
    r
}
fn vscale(a: &[F], c: F) -> Vec<F> {
    let mut r = a.iter().map(|q| q.mul(c)).collect::<Vec<_>>();
    trim(&mut r);
    r
}
fn vmul(a: &[F], b: &[F]) -> Vec<F> {
    let mut r = vec![F::z(); a.len() + b.len() - 1];
    for (i,q) in a.iter().enumerate() {
        for (j,s) in b.iter().enumerate() { r[i+j] = r[i+j].add(q.mul(*s)); }
    }
    trim(&mut r);
    r
}
fn vdivrem(a: &[F], b: &[F]) -> (Vec<F>,Vec<F>) {
    let mut r = a.to_vec(); trim(&mut r);
    let mut d = b.to_vec(); trim(&mut d);
    assert!(d.last().unwrap().0 != 0);
    if r.len() < d.len() { return (vec![F::z()],r); }
    let mut q = vec![F::z();r.len()-d.len()+1];
    while r.len() >= d.len() && !(r.len()==1 && r[0].0==0) {
        let k=r.len()-d.len();
        let c=r[r.len()-1].mul(d[d.len()-1].inv());
        q[k]=c;
        for j in 0..d.len() { r[k+j]=r[k+j].sub(c.mul(d[j])); }
        trim(&mut r);
    }
    trim(&mut q);
    (q,r)
}
fn vgcd(mut a: Vec<F>, mut b: Vec<F>) -> Vec<F> {
    trim(&mut a); trim(&mut b);
    while !(b.len()==1 && b[0].0==0) {
        let (_,r)=vdivrem(&a,&b); a=b; b=r;
    }
    let z=a.last().unwrap().inv();
    vscale(&a,z)
}
fn frozen_support_on_v(u: F) -> Vec<F> {
    let one=vec![F::o()];
    let vv=vec![F::z(),F::o()];
    let half=F::n(2).inv();
    let y=vadd(&vscale(&vadd(&vec![u],&vv),half),&vec![F::o().neg()]);
    let z=vscale(&vadd(&vec![u],&vscale(&vv,F::o().neg())),half);
    let signed=vadd(&vec![u],&vscale(&y,F::o().neg()));
    let e=vec![u];
    let x=one.clone();
    let two=F::n(2);
    let a=vmul(&vadd(&vscale(&x,two),&vscale(&e,F::o().neg())),
               &vadd(&e,&vscale(&y,two.neg())));
    let b=vmul(&e,&vadd(&vadd(&vscale(&x,two),&vscale(&y,two)),&vscale(&e,F::o().neg())));
    let e2=vmul(&e,&e);
    let delta1=vscale(&vmul(&x,&vadd(
        &vadd(&vmul(&x,&vmul(&y,&y)),&vscale(&vmul(&e,&vmul(&x,&y)),two)),
        &vscale(&vmul(&e2,&vadd(&vadd(&x,&vscale(&y,two)),&vscale(&e,F::o().neg()))),F::o().neg())
    )),F::n(4));
    let delta2=vscale(&vmul(&y,&vadd(
        &vadd(&vmul(&vmul(&x,&x),&y),&vscale(&vmul(&e,&vmul(&x,&y)),two)),
        &vscale(&vmul(&e2,&vadd(&vadd(&vscale(&x,two),&y),&vscale(&e,F::o().neg()))),F::o().neg())
    )),F::n(4));
    vmul(&vmul(&vmul(&vmul(&vmul(&vmul(&y,&z),&signed),&a),&b),&delta1),&delta2)
}
fn restricted_even_quartic_discriminant(k: &Poly, fixed: F, vary_a: bool) -> F {
    let mut c=[F::z();5];
    for ((i,j),q) in &k.0 {
        let (vary,fixed_pow)=if vary_a { (*i,*j) } else { (*j,*i) };
        c[vary as usize]=c[vary as usize].add(q.mul(fixed.pow(fixed_pow as u64)));
    }
    assert!(c[1].0==0 && c[3].0==0);
    c[2].pow(2).sub(F::n(4).mul(c[4]).mul(c[0]))
}
fn remove_frozen_factors(mut d: Vec<F>, frozen: &[F]) -> Vec<F> {
    trim(&mut d);
    loop {
        let g=vgcd(d.clone(),frozen.to_vec());
        if g.len()==1 { break; }
        let (q,r)=vdivrem(&d,&g);
        assert!(r.len()==1 && r[0].0==0);
        d=q;
    }
    let z=d.last().unwrap().inv();
    vscale(&d,z)
}
fn divide_by_v_minus_f(p: &Poly, f: &Poly) -> Poly {
    assert!(f.0.keys().all(|(_,j)| *j==0));
    let divisor=Poly::mon(0,1,F::o()).sub(f);
    let mut r=p.clone();
    let mut q=Poly::zero();
    loop {
        let Some(maxj)=r.0.keys().map(|(_,j)|*j).max() else { break; };
        if maxj==0 { break; }
        let mut lead=Poly::zero();
        for ((i,j),c) in &r.0 {
            if *j==maxj { lead=lead.add(&Poly::mon(*i,maxj-1,*c)); }
        }
        q=q.add(&lead);
        r=r.sub(&lead.mul(&divisor));
    }
    assert!(r.0.is_empty(),"nonzero remainder in v-factor division: {:?}",r.0);
    q
}
fn proportional(a:&Poly,b:&Poly)->bool {
    if a.0.is_empty() || b.0.is_empty() { return a.0.is_empty() && b.0.is_empty(); }
    if a.0.keys().collect::<Vec<_>>()!=b.0.keys().collect::<Vec<_>>() { return false; }
    let k=*a.0.keys().next().unwrap();
    let z=a.0[&k].mul(b.0[&k].inv());
    a.0.iter().all(|(m,c)| *c==b.0[m].mul(z))
}
fn symbolic_marked_discriminants() -> (Poly,Poly,Poly,Poly) {
    let one=Poly::c(F::o());
    let u=Poly::mon(1,0,F::o());
    let v=Poly::mon(0,1,F::o());
    let half=F::n(2).inv();
    let two=F::n(2);
    let y=u.add(&v).scale(half).sub(&one);
    let z=u.sub(&v).scale(half);
    let c=u.neg();
    let h=one.add(&y.pow(2)).sub(&z.pow(2));
    let ga=one.sub(&c.pow(2)).mul(&one.sub(&y.pow(2)).sub(&z.pow(2)))
        .sub(&c.pow(2).mul(&z.pow(2)).scale(two));
    let gb=y.pow(2).sub(&c.pow(2)).mul(&y.pow(2).sub(&one).sub(&z.pow(2)))
        .sub(&c.pow(2).mul(&z.pow(2)).scale(two));
    let hh=z.pow(2).mul(&c.pow(2).sub(&y.pow(2)).mul(&c.pow(2).sub(&one)).add(&c.pow(2).mul(&z.pow(2))));
    let bm=u.sub(&one);
    let am=one.add(&u.sub(&v).scale(half));
    let d1=h.neg().mul(&bm.pow(2)).add(&ga).pow(2)
        .sub(&y.pow(2).mul(&bm.pow(4)).add(&gb.mul(&bm.pow(2))).add(&hh).scale(F::n(4)));
    let d2=h.neg().mul(&am.pow(2)).add(&gb).pow(2)
        .sub(&y.pow(2).mul(&am.pow(4).add(&ga.mul(&am.pow(2))).add(&hh)).scale(F::n(4)));
    let e=u.clone();
    let delta1=one.mul(&y.pow(2).add(&e.mul(&y).scale(two)).sub(&e.pow(2).mul(&one.add(&y.scale(two)).sub(&e)))).scale(F::n(4));
    let delta2=y.mul(&y.add(&e.mul(&y).scale(two)).sub(&e.pow(2).mul(&one.scale(two).add(&y).sub(&e)))).scale(F::n(4));
    (d1,d2,delta1,delta2)
}

fn small_rational(x: F) -> (i64, i64) {
    if x.0 <= 10_000_000 {
        return (x.0 as i64, 1);
    }
    if P - x.0 <= 10_000_000 {
        return (-((P - x.0) as i64), 1);
    }
    for d in 1i64..=128 {
        let fd = F::n(d as u64);
        for n in -128i64..=128 {
            let fnn = if n < 0 { F::n((-n) as u64).neg() } else { F::n(n as u64) };
            if fnn.mul(fd.inv()) == x {
                return (n, d);
            }
        }
    }
    panic!("residual tangent root has no bounded rational reconstruction: {}", x.0)
}

fn boundary_at(name: &str, r0: u64, center_u: F, center_v: F, marked_weights: [i32;3], full_projection: bool) -> (Vec<F>, Vec<F>, usize, usize, i32, i32, i32, i32, u64, u64, u64, u64) {
    let cols: Vec<usize> = if full_projection { (0usize..12).collect() } else { vec![0,1,2,8,9,10,11] };
    let rw = marked_weights;
    let mut radial = vec![vec![Vec::<(F, F)>::new(); 12]; 3];
    let mut tangent = radial.clone();
    let mut raw_radial = radial.clone();
    let mut raw_tangent = radial.clone();
    for ti in 31u64..=85 {
        let t = F::n(ti);
        let r = F::n(r0);
        let eight = F::n(8);
        let (u, v) = if name == "U" {
            (center_u.add(t), center_v.add(t.mul(r)))
        } else {
            (center_u.add(t.mul(r)), center_v.add(t))
        };
        let gu = geometry(u.0, v.0, 'u');
        let gv = geometry(u.0, v.0, 'v');
        let s6u = solve(&gu, 8, 8);
        let s6v = solve(&gv, 8, 8);
        let g = eight.mul(u).inv();
        let (dgt, dgr) = if name == "U" {
            (eight.mul(u.pow(2)).inv().neg(), F::z())
        } else {
            (
                r.mul(eight.mul(u.pow(2)).inv()).neg(),
                t.mul(eight.mul(u.pow(2)).inv()).neg(),
            )
        };
        for m in 0..3 {
            let su = solve(&gu, m, 8);
            let sv = solve(&gv, m, 8);
            for col in &cols {
                assert!(su.fixed[*col] && sv.fixed[*col] && s6u.fixed[*col] && s6v.fixed[*col],
                    "noncanonical lift coordinate: chart={name} direction={r0} row={m} col={col} fixed=[{},{},{},{}]",
                    su.fixed[*col], sv.fixed[*col], s6u.fixed[*col], s6v.fixed[*col]);
                let au = su.values[*col].neg();
                let av = sv.values[*col].neg();
                let a6u = s6u.values[*col].neg();
                let a6v = s6v.values[*col].neg();
                let (mut at, mut ar, at6, ar6) = if name == "U" {
                    (
                        au.add(r.mul(av)),
                        t.mul(av),
                        a6u.add(r.mul(a6v)),
                        t.mul(a6v),
                    )
                } else {
                    (
                        r.mul(au).add(av),
                        t.mul(au),
                        r.mul(a6u).add(a6v),
                        t.mul(a6u),
                    )
                };
                if m == 0 {
                    at = at.add(g.mul(at6));
                    ar = ar.add(g.mul(ar6));
                    if *col == 8 {
                        let a00 = su.values[0].neg();
                        let b00 = sv.values[0].neg();
                        let (at00, ar00) = if name == "U" {
                            (a00.add(r.mul(b00)), t.mul(b00))
                        } else {
                            (r.mul(a00).add(b00), t.mul(a00))
                        };
                        at = at.add(dgt).sub(g.mul(at00));
                        ar = ar.add(dgr).sub(g.mul(ar00));
                    }
                } else if *col == 8 {
                    let a0u = su.values[0].neg();
                    let a0v = sv.values[0].neg();
                    let (a0t, a0r) = if name == "U" {
                        (a0u.add(r.mul(a0v)), t.mul(a0v))
                    } else {
                        (r.mul(a0u).add(a0v), t.mul(a0u))
                    };
                    at = at.sub(g.mul(a0t));
                    ar = ar.sub(g.mul(a0r));
                }
                raw_radial[m][*col].push((t, at.mul(t.pow(3))));
                raw_tangent[m][*col].push((t, ar.mul(t.pow(2))));
                let col_weight = if *col < 3 { marked_weights[*col] } else { 0 };
                let delta = rw[m] - col_weight;
                let tr = if delta + 1 >= 0 {
                    t.pow((delta + 1) as u64)
                } else {
                    t.pow((-(delta + 1)) as u64).inv()
                };
                let tt = if delta >= 0 {
                    t.pow(delta as u64)
                } else {
                    t.pow((-delta) as u64).inv()
                };
                radial[m][*col].push((t, at.mul(tr)));
                tangent[m][*col].push((t, ar.mul(tt)));
            }
        }
    }
    let mut rv = Vec::new();
    let mut min_radial = 9i32;
    let mut min_tangent = 9i32;
    let mut transformed_min_radial = 9i32;
    let mut transformed_min_tangent = 9i32;
    let mut transformed_max_radial_shift = 0usize;
    let mut transformed_max_tangent_shift = 0usize;
    let mut tv = Vec::new();
    let mut radial_bad_mask = 0u64;
    let mut tangent_bad_mask = 0u64;
    let mut transformed_radial_bad_mask = 0u64;
    let mut transformed_tangent_bad_mask = 0u64;
    let mut entry = 0u64;
    let mut mn = 0;
    let mut md = 0;
    for m in 0..3 {
        for &c in &cols {
            let (ashift, a) = shifted_rational_jet(&radial[m][c], 24, 8);
            let (bshift, b) = shifted_rational_jet(&tangent[m][c], 24, 8);
            let (rashift, ra) = shifted_rational_jet(&raw_radial[m][c], 24, 8);
            let (rbshift, rb) = shifted_rational_jet(&raw_tangent[m][c], 24, 8);
            transformed_max_radial_shift = transformed_max_radial_shift.max(ashift);
            transformed_max_tangent_shift = transformed_max_tangent_shift.max(bshift);
            let tvr = -(ashift as i32) + if a.0 .0 != 0 { -1 } else if a.1 .0 != 0 { 0 } else { 1 };
            let tvt = -(bshift as i32) + if b.0 .0 != 0 { 0 } else if b.1 .0 != 0 { 1 } else { 2 };
            transformed_min_radial = transformed_min_radial.min(tvr);
            transformed_min_tangent = transformed_min_tangent.min(tvt);
            if tvr < -1 {
                transformed_radial_bad_mask |= 1u64 << entry;
            }
            if tvt < 0 {
                transformed_tangent_bad_mask |= 1u64 << entry;
            }
            let vr = -(rashift as i32) + if ra.0 .0 != 0 {
                -3
            } else if ra.1 .0 != 0 {
                -2
            } else {
                -1
            };
            let vt = -(rbshift as i32) + if rb.0 .0 != 0 {
                -2
            } else if rb.1 .0 != 0 {
                -1
            } else {
                0
            };
            min_radial = min_radial.min(vr);
            min_tangent = min_tangent.min(vt);
            if vr < -1 {
                radial_bad_mask |= 1u64 << entry;
            }
            if vt < 0 {
                tangent_bad_mask |= 1u64 << entry;
            }
            entry += 1;
            rv.push(a.0);
            tv.push(b.0);
            mn = mn.max(a.2).max(b.2).max(ra.2).max(rb.2);
            md = md.max(a.3).max(b.3).max(ra.3).max(rb.3);
        }
    }
    assert!(transformed_max_radial_shift <= 8 && transformed_max_tangent_shift <= 8);
    (
        rv,
        tv,
        mn,
        md,
        min_radial,
        min_tangent,
        transformed_min_radial,
        transformed_min_tangent,
        radial_bad_mask,
        tangent_bad_mask,
        transformed_radial_bad_mask,
        transformed_tangent_bad_mask,
    )
}

fn main() {
    let third = F::n(3).inv();
    let centers = [
        (F::o(), F::n(2), "(1,1/2)", "[1,2]"),
        (F::n(2), F::n(4), "(1/2,1)", "[2,4]"),
        (F::n(2).mul(third), F::z(), "(3/2,-1)", "[2/3,0]"),
        (F::n(1).neg(), F::z(), "(-1,3/2)", "[-1,0]"),
        (F::z(), F::n(2), "[E:x:y]=[0:1:0]", "[0,2]"),
        (F::n(2), F::z(), "[E:x:y]=[2:1:0]", "[2,0]"),
    ];
    let center_index = std::env::args().nth(1).map(|s| s.parse::<usize>().expect("center index must be 0..5")).unwrap_or(0);
    assert!(center_index < centers.len(), "center index must be 0..5");
    let mode = std::env::args().nth(2).unwrap_or_default();
    if mode == "degree" {
        std::panic::set_hook(Box::new(|_| {}));
        let points=[(5u64,47u64,"residual_R"),(7,93,"residual_R"),(5,5,"z_soft"),(5,7,"signed_energy"),(5,41,"generic")];
        let mut out=Vec::<String>::new();
        for (u0,v0,label) in points {
            for degree in [6u8,8,10,12] {
                let outcome=std::panic::catch_unwind(||solve(&geometry(u0,v0,'u'),8,degree));
                match outcome {
                    Err(_)=>out.push(format!("{{\"u\":{u0},\"v\":{v0},\"label\":\"{label}\",\"degree\":{degree},\"status\":\"inconsistent\"}}")),
                    Ok(sol)=>out.push(format!("{{\"u\":{u0},\"v\":{v0},\"label\":\"{label}\",\"degree\":{degree},\"status\":\"ok\",\"gauge_rank\":{},\"pivot_mask\":{}}}",sol.gauge_rank,sol.gauge_pivot_mask)),
                }
            }
        }
        println!("{{\"schema\":\"marici.benincasa.gauge_presentation_degree_stability.v1\",\"results\":[{}]}}",out.join(","));
        return;
    }
    if mode == "factor" {
        let (mut d1,mut d2,delta1,delta2)=symbolic_marked_discriminants();
        let original_d1_terms=d1.0.len();
        let original_d2_terms=d2.0.len();
        let u=Poly::mon(1,0,F::o());
        let factors=[
            u.clone(),
            u.add(&Poly::c(F::n(2))),
            u.pow(2).scale(F::n(2)).sub(&u).add(&Poly::c(F::n(2))),
        ];
        for f in &factors {
            d1=divide_by_v_minus_f(&d1,f);
            d2=divide_by_v_minus_f(&d2,f);
        }
        println!("{{\"schema\":\"marici.benincasa.marked_branch_discriminant_factor_gate.v2\",\"original_d1_terms\":{original_d1_terms},\"original_d2_terms\":{original_d2_terms},\"diagnostic_identically_zero\":{},\"common_linear_factors\":[\"v-u\",\"v-u-2\",\"v-(2u^2-u+2)\"],\"d1_quotient_terms\":{},\"d2_quotient_terms\":{},\"d1_quotient_proportional_delta1\":{},\"d1_quotient_proportional_delta2\":{},\"d2_quotient_proportional_delta1\":{},\"d2_quotient_proportional_delta2\":{}}}",original_d1_terms==0&&original_d2_terms==0,d1.0.len(),d2.0.len(),proportional(&d1,&delta1),proportional(&d1,&delta2),proportional(&d2,&delta1),proportional(&d2,&delta2));
        return;
    }
    if mode == "scan" {
        let mut bad=Vec::<String>::new();
        let mut frozen_bad=0usize;
        let mut residual_bad=0usize;
        std::panic::set_hook(Box::new(|_| {}));
        for u0 in 3u64..=15 {
            let frozen=frozen_support_on_v(F::n(u0));
            for vi in 3u64..=200 {
                let outcome=std::panic::catch_unwind(|| solve(&geometry(u0,vi,'u'),8,8));
                let kind=match outcome {
                    Err(_) => Some("inconsistent"),
                    Ok(sol) if sol.gauge_rank!=2 || sol.gauge_pivot_mask!=24 => Some("rank_or_pivot"),
                    _ => None,
                };
                if let Some(kind)=kind {
                    let on_frozen=peval(&frozen,F::n(vi)).0==0;
                    if on_frozen { frozen_bad+=1; } else { residual_bad+=1; }
                    let guv=geometry(u0,vi,'u');
                    let a_mark=F::o().add(F::n(u0).sub(F::n(vi)).mul(F::n(2).inv()));
                    let b_mark=F::n(u0).sub(F::o());
                    let marked_intersection_on_branch=guv.k.eval(a_mark,b_mark).0==0;
                    let l1_branch_tangency=restricted_even_quartic_discriminant(&guv.k,b_mark,true).0==0;
                    let l2_branch_tangency=restricted_even_quartic_discriminant(&guv.k,a_mark,false).0==0;
                    bad.push(format!("{{\"u\":{u0},\"v\":{vi},\"kind\":\"{kind}\",\"on_frozen_support\":{on_frozen},\"marked_intersection_on_branch\":{marked_intersection_on_branch},\"l1_branch_tangency\":{l1_branch_tangency},\"l2_branch_tangency\":{l2_branch_tangency}}}"));
                }
            }
        }
        println!("{{\"schema\":\"marici.benincasa.gauge_presentation_rank_scan.v1\",\"u_range\":[3,15],\"v_range\":[3,200],\"frozen_bad_count\":{frozen_bad},\"residual_bad_count\":{residual_bad},\"bad_points\":[{}]}}",bad.join(","));
        return;
    }
    if mode == "global" {
        let rows=[0usize,1,2,8];
        let mut max_den_degree=0usize;
        let mut max_residual_degree=0usize;
        let mut residual_mask=0u128;
        let mut entry=0u32;
        let mut rank_or_pivot_failures=0usize;
        let mut inconsistent_sample_count=0usize;
        let mut unexplained_exception_count=0usize;
        let mut exceptions=Vec::<String>::new();
        std::panic::set_hook(Box::new(|_| {}));
        for u0 in [3u64,5,7,11,13] {
            let frozen=frozen_support_on_v(F::n(u0));
            for row in rows {
                for axis in ['u','v'] {
                    let mut samples=vec![Vec::<(F,F)>::new();10];
                    for vi in 31u64..=95 {
                        let Ok(sol)=std::panic::catch_unwind(|| solve(&geometry(u0,vi,axis),row,8)) else {
                            inconsistent_sample_count+=1;
                            let on_frozen=peval(&frozen,F::n(vi)).0==0;
                            if !on_frozen { unexplained_exception_count+=1; }
                            exceptions.push(format!("{{\"u\":{u0},\"v\":{vi},\"row\":{row},\"axis\":\"{axis}\",\"kind\":\"inconsistent\",\"on_frozen_support\":{on_frozen}}}"));
                            continue;
                        };
                        if sol.gauge_rank!=2 || sol.gauge_pivot_mask!=24 {
                            rank_or_pivot_failures+=1;
                            let on_frozen=peval(&frozen,F::n(vi)).0==0;
                            if !on_frozen { unexplained_exception_count+=1; }
                            exceptions.push(format!("{{\"u\":{u0},\"v\":{vi},\"row\":{row},\"axis\":\"{axis}\",\"kind\":\"rank_or_pivot\",\"on_frozen_support\":{on_frozen}}}"));
                            continue;
                        }
                        for (k,q) in gauge_plucker(&sol).into_iter().enumerate() {
                            samples[k].push((F::n(vi),q));
                        }
                    }
                    for s in samples {
                        let (_,d)=rational_fit(&s,20);
                        max_den_degree=max_den_degree.max(d.len()-1);
                        let residual=remove_frozen_factors(d,&frozen);
                        max_residual_degree=max_residual_degree.max(residual.len()-1);
                        if residual.len()>1 { residual_mask|=1u128<<entry; }
                        entry+=1;
                    }
                }
            }
        }
        println!("{{\"schema\":\"marici.benincasa.gauge_plucker_generic_lines.v3\",\"u_slices\":[3,5,7,11,13],\"rows\":[0,1,2,8],\"axes\":[\"u\",\"v\"],\"plucker_order\":[\"p34\",\"p35\",\"p36\",\"p37\",\"p45\",\"p46\",\"p47\",\"p56\",\"p57\",\"p67\"],\"max_denominator_degree\":{max_den_degree},\"max_residual_degree_after_frozen_support\":{max_residual_degree},\"residual_mask\":{residual_mask},\"rank_or_pivot_failures\":{rank_or_pivot_failures},\"inconsistent_sample_count\":{inconsistent_sample_count},\"unexplained_exception_count\":{unexplained_exception_count},\"exceptions\":[{}]}}",exceptions.join(","));
        return;
    }
    let full_projection = mode == "full";
    let (center_u, center_v, source_center, center_uv) = centers[center_index];
    let marked_weights = if center_index >= 4 { [2i32,1,1] } else { [1i32,0,0] };
    if mode == "diag" {
        let mut nonfixed = [0u16;4];
        let mut gauge_ranks = [BTreeSet::<usize>::new(), BTreeSet::new(), BTreeSet::new(), BTreeSet::new()];
        let mut gauge_pivot_masks = [BTreeSet::<u16>::new(), BTreeSet::new(), BTreeSet::new(), BTreeSet::new()];
        let mut gauge_points = [BTreeSet::<Vec<u64>>::new(), BTreeSet::new(), BTreeSet::new(), BTreeSet::new()];
        let mut plucker_min_valuation = [99i32;4];
        let mut plucker_pole_masks = [0u16;4];
        let rows = [0usize,1,2,8];
        for name in ["U","V"] {
            for r0 in [2u64,3,7,13,21] {
                let r = F::n(r0);
                for ti in [31u64,32,47,61,85] {
                    let t = F::n(ti);
                    let (u,v) = if name == "U" {
                        (center_u.add(t), center_v.add(t.mul(r)))
                    } else {
                        (center_u.add(t.mul(r)), center_v.add(t))
                    };
                    let gu = geometry(u.0,v.0,'u');
                    let gv = geometry(u.0,v.0,'v');
                    for (ri,row) in rows.iter().enumerate() {
                        for sol in [solve(&gu,*row,8),solve(&gv,*row,8)] {
                            assert!(sol.residual_zero);
                            gauge_ranks[ri].insert(sol.gauge_rank);
                            gauge_pivot_masks[ri].insert(sol.gauge_pivot_mask);
                            gauge_points[ri].insert(sol.gauge_rref.iter().flatten().map(|q| q.0).collect());
                            for c in 0..12 {
                                if !sol.fixed[c] { nonfixed[ri] |= 1u16 << c; }
                            }
                        }
                    }
                }
            }
        }
        for name in ["U","V"] {
            for r0 in [2u64,3,7,13,21] {
                let r = F::n(r0);
                for (ri,row) in rows.iter().enumerate() {
                    for axis in ['u','v'] {
                        let mut samples = vec![Vec::<(F,F)>::new();10];
                        for ti in 31u64..=55 {
                            let t = F::n(ti);
                            let (u,v) = if name == "U" {
                                (center_u.add(t), center_v.add(t.mul(r)))
                            } else {
                                (center_u.add(t.mul(r)), center_v.add(t))
                            };
                            let sol = solve(&geometry(u.0,v.0,axis),*row,8);
                            for (k,q) in gauge_plucker(&sol).into_iter().enumerate() {
                                samples[k].push((t,q));
                            }
                        }
                        for (k,s) in samples.iter().enumerate() {
                            let (shift,jet) = shifted_rational_jet(s,10,8);
                            let valuation = -(shift as i32)
                                + if jet.0.0 != 0 { 0 } else if jet.1.0 != 0 { 1 } else { 2 };
                            plucker_min_valuation[ri] = plucker_min_valuation[ri].min(valuation);
                            if valuation < 0 { plucker_pole_masks[ri] |= 1u16 << k; }
                        }
                    }
                }
            }
        }
        let gauge_point_counts = gauge_points.map(|q| q.len());
        println!("{{\"schema\":\"marici.benincasa.exact_lift_gauge_diag.v4\",\"center_index\":{center_index},\"rows\":[0,1,2,8],\"nonfixed_column_masks\":{:?},\"gauge_ranks\":{:?},\"gauge_pivot_masks\":{:?},\"gauge_point_counts\":{:?},\"plucker_min_valuation\":{:?},\"plucker_pole_masks\":{:?},\"candidate_exact_lift_columns\":[3,4,5,6,7]}}",nonfixed,gauge_ranks,gauge_pivot_masks,gauge_point_counts,plucker_min_valuation,plucker_pole_masks);
        return;
    }
    let base = F::n(1000);
    let mut handles = Vec::new();
    for name in ["U", "V"] {
        for lane in 0u64..4 {
            handles.push(std::thread::spawn(move || {
                let mut out = Vec::new();
                for r0 in 2u64..=21 {
                    if (r0 - 2) % 4 == lane {
                        out.push((name, r0, boundary_at(name, r0, center_u, center_v, marked_weights, full_projection)));
                    }
                }
                out
            }));
        }
    }
    let mut table = BTreeMap::new();
    for h in handles {
        for (name, r, z) in h.join().expect("worker panicked") {
            table.insert((name, r), z);
        }
    }
    let mut roots = BTreeSet::<i64>::new();
    let mut residual_roots = BTreeSet::<(i64, i64)>::new();
    let mut residual_occurrences = BTreeSet::<(String, usize, i64, i64)>::new();
    let mut residual_polynomials = BTreeSet::<(String, usize, String)>::new();
    let mut maxrn = 0;
    let mut maxrd = 0;
    let mut maxtn = 0;
    let mut maxtd = 0;
    let mut nonzero = 0;
    let mut min_radial = 9i32;
    let mut min_tangent = 9i32;
    let mut transformed_min_radial = 9i32;
    let mut transformed_min_tangent = 9i32;
    let mut radial_bad_mask = 0u64;
    let mut tangent_bad_mask = 0u64;
    let mut transformed_radial_bad_mask = 0u64;
    let mut transformed_tangent_bad_mask = 0u64;
    let projection_columns: Vec<usize> = if full_projection { (0usize..12).collect() } else { vec![0,1,2,8,9,10,11] };
    let entries_per_component = 3 * projection_columns.len();
    for name in ["U", "V"] {
        let mut rs = vec![Vec::<(F, F)>::new(); 2 * entries_per_component];
        for r0 in 2u64..=21 {
            let z = &table[&(name, r0)];
            min_radial = min_radial.min(z.4);
            min_tangent = min_tangent.min(z.5);
            transformed_min_radial = transformed_min_radial.min(z.6);
            transformed_min_tangent = transformed_min_tangent.min(z.7);
            radial_bad_mask |= z.8;
            tangent_bad_mask |= z.9;
            transformed_radial_bad_mask |= z.10;
            transformed_tangent_bad_mask |= z.11;
            for j in 0..entries_per_component {
                let q = F::n(r0).sub(base);
                rs[j].push((q, z.0[j]));
                rs[entries_per_component + j].push((q, z.1[j]));
            }
        }
        for (j, samples) in rs.iter().enumerate() {
            let (n, mut d) = rational_fit(samples, 8);
            if n.iter().any(|x| x.0 != 0) {
                nonzero += 1
            }
            if j < entries_per_component {
                maxrn = maxrn.max(n.len() - 1);
                maxrd = maxrd.max(d.len() - 1)
            } else {
                maxtn = maxtn.max(n.len() - 1);
                maxtd = maxtd.max(d.len() - 1)
            }
            let rq = F::z().sub(base);
            while d.len() > 1 && peval(&d, rq).0 == 0 {
                roots.insert(0);
                d = divide_linear(&d, rq);
                trim(&mut d)
            }
            while d.len() > 1 {
                let mut found = None;
                'search: for den in 1i64..=32 {
                    let fd = F::n(den as u64);
                    for num in -64i64..=64 {
                        let fnn = if num < 0 { F::n((-num) as u64).neg() } else { F::n(num as u64) };
                        let rroot = fnn.mul(fd.inv());
                        let qroot = rroot.sub(base);
                        if peval(&d, qroot).0 == 0 {
                            found = Some((qroot, small_rational(rroot)));
                            break 'search;
                        }
                    }
                }
                let Some((qroot, rr)) = found else { break };
                residual_roots.insert(rr);
                residual_occurrences.insert((name.to_string(), j, rr.0, rr.1));
                d = divide_linear(&d, qroot);
                trim(&mut d);
            }
            trim(&mut d);
            if d.len() > 1 {
                let lead = d[d.len()-1].inv();
                let coeffs = d.iter().map(|c| small_rational(c.mul(lead))).map(|(n,den)| format!("[{n},{den}]")).collect::<Vec<_>>().join(",");
                residual_polynomials.insert((name.to_string(), j, format!("[{coeffs}]")));
            }
        }
    }
    println!("{{");
    println!("  \"schema\": \"marici.benincasa.marked_tangency_support.v4\",");
    println!("  \"center_index\": {center_index},");
    println!("  \"center_uv\": {center_uv},");
    println!("  \"source_center\": \"{source_center}\",");
    println!("  \"charts\": [\"u=u0+t,v=v0+t*r\",\"v=v0+t,u=u0+t*r\"],");
    println!("  \"r_samples_per_chart\": 20,");
    println!("  \"t_samples_per_r\": 55,");
    println!("  \"projection_columns\": {:?},", projection_columns);
    println!("  \"rational_coordinates\": {},", 4 * entries_per_component);
    println!("  \"nonzero_coordinates\": {nonzero},");
    println!("  \"radial_degree_bounds\": [{maxrn},{maxrd}],");
    println!("  \"tangent_degree_bounds\": [{maxtn},{maxtd}],");
    println!("  \"conductor_weights\": [{},{},{},0,0,0,0],", marked_weights[0], marked_weights[1], marked_weights[2]);
    println!("  \"transformed_min_radial_valuation\": {transformed_min_radial},");
    println!("  \"transformed_min_tangent_valuation\": {transformed_min_tangent},");
    println!("  \"raw_min_radial_valuation\": {min_radial},");
    println!("  \"raw_min_tangent_valuation\": {min_tangent},");
    println!("  \"radial_bad_mask_decimal\": {radial_bad_mask},");
    println!("  \"tangent_bad_mask_decimal\": {tangent_bad_mask},");
    println!("  \"transformed_radial_bad_mask_decimal\": {transformed_radial_bad_mask},");
    println!("  \"transformed_tangent_bad_mask_decimal\": {transformed_tangent_bad_mask},");
    let roots_json = if roots.is_empty() { "[]" } else { "[0]" };
    println!("  \"denominator_roots\": {roots_json},");
    let residual_roots_json = residual_roots.iter().map(|(n,d)| format!("[{n},{d}]")).collect::<Vec<_>>().join(",");
    let residual_occurrences_json = residual_occurrences.iter().map(|(chart,j,n,d)| format!("{{\"chart\":\"{chart}\",\"coordinate\":{j},\"root\":[{n},{d}]}}")).collect::<Vec<_>>().join(",");
    let residual_is_existing_cm_branch = center_index == 1 && residual_roots.iter().all(|r| *r == (1,1));
    let basepoint_zero_support = center_index == 4
        && residual_roots.iter().all(|r| *r == (-1,1) || *r == (1,1))
        && residual_polynomials.iter().all(|(_,_,p)| p == "[[1006001,1],[2006,1],[1,1]]");
    let basepoint_two_support = center_index == 5
        && residual_roots.iter().all(|r| *r == (-1,1) || *r == (-9,1) || *r == (-1,9))
        && residual_polynomials.is_empty();
    let residual_is_existing_source_support = residual_roots.is_empty() && residual_polynomials.is_empty()
        || residual_is_existing_cm_branch || basepoint_zero_support || basepoint_two_support;
    let unknown_residual = !residual_is_existing_source_support;
    println!("  \"residual_tangent_roots\": [{residual_roots_json}],");
    println!("  \"residual_occurrences\": [{residual_occurrences_json}],");
    let residual_polynomials_json = residual_polynomials.iter().map(|(chart,j,coeffs)| format!("{{\"chart\":\"{chart}\",\"coordinate\":{j},\"q_coefficients\":{coeffs}}}")).collect::<Vec<_>>().join(",");
    println!("  \"residual_irreducible_polynomials\": [{residual_polynomials_json}],");
    println!("  \"residual_is_existing_cayley_menger_branch\": {residual_is_existing_cm_branch},");
    println!("  \"residual_is_existing_source_support\": {residual_is_existing_source_support},");
    println!("  \"all_denominators_generated_by_frozen_tangent_direction\": {},", residual_roots.is_empty());
    println!("  \"all_denominators_generated_by_frozen_source_support\": {},", !unknown_residual);
    println!("  \"new_support_factor\": {unknown_residual}");
    println!("}}");
}
