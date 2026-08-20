use std::collections::{BTreeMap, BTreeSet};

#[cfg(all(not(feature = "replication-prime"), not(feature = "reconstruction-prime-3"), not(feature = "verification-prime-4")))]
const P: u64 = 2_305_843_009_213_693_951;
#[cfg(all(feature = "replication-prime", not(feature = "reconstruction-prime-3"), not(feature = "verification-prime-4")))]
const P: u64 = 2_305_843_009_213_693_921;
#[cfg(all(feature = "reconstruction-prime-3", not(feature = "replication-prime"), not(feature = "verification-prime-4")))]
const P: u64 = 2_305_843_009_213_693_723;
#[cfg(all(feature = "verification-prime-4", not(feature = "replication-prime"), not(feature = "reconstruction-prime-3")))]
const P: u64 = 2_305_843_009_213_693_561;

#[cfg(any(
    all(feature = "replication-prime", feature = "reconstruction-prime-3"),
    all(feature = "replication-prime", feature = "verification-prime-4"),
    all(feature = "reconstruction-prime-3", feature = "verification-prime-4")
))]
compile_error!("select exactly one reconstruction/verification-prime feature");

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

fn exceptional_p_chart_geometry(ss: u64, differentiated: bool) -> Geometry {
    let one = F::o();
    let two = F::n(2);
    let half = two.inv();
    let s = if differentiated {
        D::var(F::n(ss))
    } else {
        D::c(F::n(ss))
    };
    let s2 = s.sq();
    let s3 = s2.mul(s);
    let s4 = s2.sq();

    // K_E = in_J(K)(1,s,A,B), in the fixed fiber coordinates A,B.
    let a2 = D::c(F::n(5).neg().mul(half))
        .sub(s)
        .sub(s2.mul(D::c(half)));
    let a2b = D::c(two).mul(D::c(one).sub(s));
    let b2 = D::c(one).add(s).sq();
    let b1 = D::c(half).mul(
        D::c(F::n(5).neg())
            .add(s.mul(D::c(F::n(3))))
            .add(s2)
            .add(s3),
    );
    let constant = D::c(F::n(16).inv()).mul(
        D::c(F::n(25))
            .sub(s.mul(D::c(F::n(44))))
            .add(s2.mul(D::c(F::n(14))))
            .add(s3.mul(D::c(F::n(4))))
            .add(s4),
    );
    let mut k = Poly::zero();
    let mut kp = Poly::zero();
    for (m, coefficient) in [
        ((4, 0), D::c(one)),
        ((2, 1), a2b),
        ((2, 0), a2),
        ((0, 2), b2),
        ((0, 1), b1),
        ((0, 0), constant),
    ] {
        if coefficient.x.0 != 0 {
            k.0.insert(m, coefficient.x);
        }
        if coefficient.d.0 != 0 {
            kp.0.insert(m, coefficient.d);
        }
    }

    // in_J(K1)(1,s,A,B) = 4A^2 + 4(1-s)B - s^2 + 6s - 5.
    let k1_b = D::c(F::n(4)).mul(D::c(one).sub(s));
    let k1_c = s2.neg().add(s.mul(D::c(F::n(6)))).sub(D::c(F::n(5)));
    let mut k1 = Poly::zero();
    let mut k1p = Poly::zero();
    for (m, coefficient) in [
        ((2, 0), D::c(F::n(4))),
        ((0, 1), k1_b),
        ((0, 0), k1_c),
    ] {
        if coefficient.x.0 != 0 {
            k1.0.insert(m, coefficient.x);
        }
        if coefficient.d.0 != 0 {
            k1p.0.insert(m, coefficient.d);
        }
    }

    Geometry {
        k,
        kp,
        k1,
        k1p,
        l1: Poly::mon(0, 1, one).sub(&Poly::c(one)),
        l2: Poly::mon(1, 0, one).add(&Poly::c(s.x.sub(one).mul(half))),
        l1p: F::z(),
        l2p: s.d.mul(half),
    }
}

fn geometry(uu: u64, vv: u64, axis: char) -> Geometry {
    if std::env::var_os("MARICI_EXCEPTIONAL_P_CHART").is_some() {
        return exceptional_p_chart_geometry(uu, axis == 'u');
    }
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

struct Sol {
    rank: usize,
    fixed: Vec<bool>,
    values: Vec<F>,
    residual_zero: bool,
    equations: usize,
    unknowns: usize,
    pivot_cols: Vec<usize>,
    consistent: bool,
    witness: Vec<F>,
}

fn pivot_hash(columns: &[usize]) -> u64 {
    columns.iter().fold(1_469_598_103_934_665_603u64, |hash, column| {
        (hash ^ (*column as u64 + 1)).wrapping_mul(1_099_511_628_211)
    })
}

fn fixed_signature(sol: &Sol) -> (u16, Vec<usize>) {
    let mask = sol.fixed.iter().enumerate().fold(0u16, |mask, (i, fixed)| {
        if *fixed { mask | (1u16 << i) } else { mask }
    });
    let coordinates = sol.fixed.iter().enumerate()
        .filter_map(|(i, fixed)| fixed.then_some(i)).collect();
    (mask, coordinates)
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
    let consistent = (0..rows).all(|i| !(0..n).all(|j| a[i][j].0 == 0) || a[i][n].0 == 0);
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
    for (q, c) in cols.iter().zip(&x) {
        check = check.add(&q.scale(*c))
    }
    Sol {
        rank: rr,
        fixed,
        values,
        residual_zero: check.sub(&rhs).0.is_empty(),
        equations: rows,
        unknowns: n,
        pivot_cols: piv.iter().map(|(_, c)| *c).collect(),
        consistent,
        witness: x,
    }
}

fn run_primal_witness(samples: &[(u64, u64)]) {
    let axis = std::env::var("MARICI_WITNESS_AXIS").ok().and_then(|x| x.chars().next()).unwrap_or('u');
    let master: usize = std::env::var("MARICI_WITNESS_MASTER").ok().and_then(|x| x.parse().ok()).unwrap_or(0);
    let mut accepted = Vec::new();
    let mut rejected = Vec::new();
    for (u, v) in samples {
        let s = solve(&geometry(*u, *v, axis), master, 8);
        let signature = fixed_signature(&s);
        if s.consistent && s.residual_zero && s.rank == 117 && signature.0 == 3847 {
            let values: Vec<u64> = s.pivot_cols.iter().map(|c| s.witness[*c].0).collect();
            accepted.push((*u, *v, s.pivot_cols, values));
        } else {
            rejected.push((*u, *v, s.consistent, s.rank, signature.0));
        }
    }
    println!("{{\"schema\":\"marici.benincasa.marked_relative_primal_witness_sampler.v1\",\"prime\":{},\"axis\":\"{}\",\"master\":{},\"primitive_degree\":8,\"unknowns\":372,\"equations\":132,\"accepted_points\":[{}],\"rejected_points\":[{}]}}",
        P, axis, master,
        accepted.iter().map(|(u,v,piv,x)| format!("{{\"u\":{},\"v\":{},\"pivot_columns\":{:?},\"values\":{:?}}}",u,v,piv,x)).collect::<Vec<_>>().join(","),
        rejected.iter().map(|(u,v,c,r,m)| format!("{{\"u\":{},\"v\":{},\"consistent\":{},\"rank\":{},\"fixed_mask\":{}}}",u,v,c,r,m)).collect::<Vec<_>>().join(","));
}

#[derive(Default)]
struct SparseRank { pivots: BTreeMap<usize, BTreeMap<usize, F>> }
impl SparseRank {
    fn insert(&mut self, mut row: BTreeMap<usize, F>) {
        loop {
            let Some((&pivot, &value)) = row.iter().next() else { return };
            if let Some(base) = self.pivots.get(&pivot) {
                let factor = value;
                for (&column, &coefficient) in base {
                    let next = row.get(&column).copied().unwrap_or(F::z()).sub(factor.mul(coefficient));
                    if next == F::z() { row.remove(&column); } else { row.insert(column, next); }
                }
            } else {
                let inverse = value.inv();
                for coefficient in row.values_mut() { *coefficient = coefficient.mul(inverse); }
                self.pivots.insert(pivot, row);
                return;
            }
        }
    }
    fn rank(&self) -> usize { self.pivots.len() }
}

fn system_data(g: &Geometry, master: usize) -> (Vec<Mon>, Vec<Poly>, Poly) {
    let cs = classes(g);
    let mut columns: Vec<Poly> = cs.iter().map(|q| common(g, q)).collect();
    for (sa, sb) in [(1, 1), (1, 0), (0, 1), (0, 0)] {
        for m in monomials(8) {
            columns.push(exact(g, sa, sb, m, false));
            columns.push(exact(g, sa, sb, m, true));
        }
    }
    let rhs = target(g, &cs[master]);
    let mut support = BTreeSet::new();
    for column in &columns { support.extend(column.0.keys().copied()); }
    support.extend(rhs.0.keys().copied());
    (support.into_iter().collect(), columns, rhs)
}

fn run_polynomial_module_gate(samples: &[(u64, u64)]) {
    let axis = std::env::var("MARICI_WITNESS_AXIS").ok().and_then(|x| x.chars().next()).unwrap_or('u');
    let master: usize = std::env::var("MARICI_WITNESS_MASTER").ok().and_then(|x| x.parse().ok()).unwrap_or(0);
    let numerator_degree: u8 = std::env::var("MARICI_MODULE_NUMERATOR_DEGREE").ok().and_then(|x| x.parse().ok()).unwrap_or(0);
    let denominator_degree: u8 = std::env::var("MARICI_MODULE_DENOMINATOR_DEGREE").ok().and_then(|x| x.parse().ok()).unwrap_or(0);
    let numerator_monomials = monomials(numerator_degree);
    let denominator_monomials = monomials(denominator_degree);
    let numerator_unknowns = 372 * numerator_monomials.len();
    let denominator_unknowns = denominator_monomials.len();
    let mut numerator_rank = SparseRank::default();
    let mut full_rank = SparseRank::default();
    let mut accepted = 0usize;
    for (u, v) in samples {
        let g = geometry(*u, *v, axis);
        let (support, columns, rhs) = system_data(&g, master);
        if support.len() != 132 { continue }
        let numerator_values: Vec<F> = numerator_monomials.iter().map(|(i,j)| F::n(*u).pow(*i as u64).mul(F::n(*v).pow(*j as u64))).collect();
        let denominator_values: Vec<F> = denominator_monomials.iter().map(|(i,j)| F::n(*u).pow(*i as u64).mul(F::n(*v).pow(*j as u64))).collect();
        for monomial in &support {
            let mut numerator_row = BTreeMap::new();
            for (column_index, column) in columns.iter().enumerate() {
                let coefficient = column.0.get(monomial).copied().unwrap_or(F::z());
                if coefficient == F::z() { continue }
                for (term, value) in numerator_values.iter().enumerate() {
                    let entry = coefficient.mul(*value);
                    if entry != F::z() { numerator_row.insert(column_index * numerator_values.len() + term, entry); }
                }
            }
            let mut full_row = numerator_row.clone();
            let target = rhs.0.get(monomial).copied().unwrap_or(F::z()).neg();
            if target != F::z() {
                for (term, value) in denominator_values.iter().enumerate() {
                    let entry = target.mul(*value);
                    if entry != F::z() { full_row.insert(numerator_unknowns + term, entry); }
                }
            }
            numerator_rank.insert(numerator_row);
            full_rank.insert(full_row);
        }
        accepted += 1;
    }
    let excess = denominator_unknowns as isize - (full_rank.rank() as isize - numerator_rank.rank() as isize);
    println!("{{\"schema\":\"marici.benincasa.marked_extension_polynomial_module_gate.v1\",\"prime\":{},\"axis\":\"{}\",\"master\":{},\"numerator_degree\":{},\"denominator_degree\":{},\"samples\":{},\"numerator_unknowns\":{},\"denominator_unknowns\":{},\"numerator_rank\":{},\"full_rank\":{},\"denominator_kernel_excess\":{},\"nonzero_denominator_solution\":{}}}",
        P, axis, master, numerator_degree, denominator_degree, accepted, numerator_unknowns, denominator_unknowns,
        numerator_rank.rank(), full_rank.rank(), excess, excess > 0);
}

fn dual_rows(g: &Geometry, degree: u8) -> Option<(usize, Vec<usize>, Vec<usize>, Vec<Vec<F>>)> {
    let cs = classes(g);
    let mut cols: Vec<Poly> = cs.iter().map(|q| common(g, q)).collect();
    for (sa, sb) in [(1, 1), (1, 0), (0, 1), (0, 0)] {
        for m in monomials(degree) {
            cols.push(exact(g, sa, sb, m, false));
            cols.push(exact(g, sa, sb, m, true));
        }
    }
    let mut mons = BTreeSet::new();
    for q in &cols { mons.extend(q.0.keys().copied()) }
    let n = cols.len();
    let rows = mons.len();
    let mut a: Vec<Vec<F>> = mons.iter().map(|m| cols.iter()
        .map(|q| q.0.get(m).copied().unwrap_or(F::z())).collect()).collect();
    let mut transform = vec![vec![F::z(); rows]; rows];
    let mut row_labels: Vec<usize> = (0..rows).collect();
    for (i, row) in transform.iter_mut().enumerate() { row[i] = F::o() }
    let mut piv = Vec::new();
    let mut rr = 0;
    for c in 0..n {
        let Some(p) = (rr..rows).find(|&i| a[i][c].0 != 0) else { continue };
        a.swap(rr, p); transform.swap(rr, p); row_labels.swap(rr, p);
        let z = a[rr][c].inv();
        for j in c..n { a[rr][j] = a[rr][j].mul(z) }
        for j in 0..rows { transform[rr][j] = transform[rr][j].mul(z) }
        for i in 0..rows {
            if i != rr && a[i][c].0 != 0 {
                let z = a[i][c];
                for j in c..n { a[i][j] = a[i][j].sub(z.mul(a[rr][j])) }
                for j in 0..rows { transform[i][j] = transform[i][j].sub(z.mul(transform[rr][j])) }
            }
        }
        piv.push((rr, c)); rr += 1;
        if rr == rows { break }
    }
    if rr != 117 { return None }
    let mut out = Vec::new();
    for target in 8..12 {
        let row = piv.iter().find_map(|(r, c)| (*c == target).then_some(*r))?;
        if !(0..n).all(|c| a[row][c] == if c == target { F::o() } else { F::z() }) {
            return None;
        }
        out.push(transform[row].clone());
    }
    Some((rows, piv.iter().map(|(_, c)| *c).collect(), row_labels[..rr].to_vec(), out))
}

fn run_dual(samples: &[(u64, u64)]) {
    let mut accepted = Vec::new();
    let mut rejected = Vec::new();
    for (u, v) in samples {
        let g = geometry(*u, *v, 'u');
        match dual_rows(&g, 8) {
            Some((equations, pivots, pivot_rows, rows)) => accepted.push((*u, *v, equations, pivots, pivot_rows, rows)),
            None => rejected.push((*u, *v)),
        }
    }
    println!("{{");
    println!("  \"schema\": \"marici.benincasa.marked_relative_dual_sampler.v1\",");
    println!("  \"prime\": {},", P);
    println!("  \"requested_points\": {},", samples.len());
    println!("  \"accepted_points\": {},", accepted.len());
    println!("  \"rejected_points\": [{}],", rejected.iter().map(|(u,v)| format!("[{u},{v}]")).collect::<Vec<_>>().join(","));
    println!("  \"dual_rows\": [");
    for (i, (u, v, equations, pivots, pivot_rows, rows)) in accepted.iter().enumerate() {
        let data = rows.iter().map(|row| format!("[{}]", row.iter()
            .map(|x| x.0.to_string()).collect::<Vec<_>>().join(",")))
            .collect::<Vec<_>>().join(",");
        println!("    {{\"u\":{},\"v\":{},\"equations\":{},\"pivot_columns\":{:?},\"pivot_rows\":{:?},\"coordinates\":[8,9,10,11],\"vectors\":[{}]}}{}",
            u, v, equations, pivots, pivot_rows, data, if i + 1 == accepted.len() { "" } else { "," });
    }
    println!("  ]");
    println!("}}");
}

fn run_exceptional_p_chart(samples: &[(u64, u64)]) {
    let mut records = Vec::new();
    for (s, _) in samples {
        let g = exceptional_p_chart_geometry(*s, true);
        let class_columns: Vec<Poly> = classes(&g).iter().map(|class| common(&g, class)).collect();
        let mut exact_columns = Vec::new();
        for (sa, sb) in [(1, 1), (1, 0), (0, 1), (0, 0)] {
            for monomial in monomials(8) {
                exact_columns.push(exact(&g, sa, sb, monomial, false));
                exact_columns.push(exact(&g, sa, sb, monomial, true));
            }
        }
        let exact_rank = polynomial_column_rank(&exact_columns);
        let class_rank_increments: Vec<usize> = (0..class_columns.len())
            .map(|index| {
                let mut columns = exact_columns.clone();
                columns.extend(class_columns[..=index].iter().cloned());
                polynomial_column_rank(&columns)
            })
            .scan(exact_rank, |previous, rank| {
                let increment = rank - *previous;
                *previous = rank;
                Some(increment)
            })
            .collect();
        let (quotient_basis, quotient_coordinates) =
            quotient_coordinate_matrix(&class_columns, &exact_columns);
        let quotient_connection = quotient_derivative_matrix(
            &g, &class_columns, &exact_columns, &quotient_basis);
        let mut all_columns = class_columns;
        all_columns.extend(exact_columns);
        let all_rank = polynomial_column_rank(&all_columns);
        let quotient_dimension = all_rank - exact_rank;
        for master in 0..12 {
            let solution = solve(&g, master, 8);
            let (mask, coordinates) = fixed_signature(&solution);
            records.push((*s, master, solution.consistent, solution.residual_zero,
                solution.rank, mask, coordinates, solution.equations, solution.unknowns,
                pivot_hash(&solution.pivot_cols), exact_rank, all_rank, quotient_dimension,
                class_rank_increments.clone(), quotient_basis.clone(), quotient_coordinates.clone(),
                quotient_connection.clone()));
        }
    }
    println!("{{");
    println!("  \"schema\": \"marici.benincasa.rank12_u0_v2_exceptional_p_chart_reduction.v1\",");
    println!("  \"prime\": {},", P);
    println!("  \"chart\": \"p_nonzero\",");
    println!("  \"coordinate\": \"s=q/p\",");
    println!("  \"primitive_degree\": 8,");
    println!("  \"records\": [");
    for (index, (s, master, consistent, residual, rank, mask, coordinates, equations, unknowns, hash, exact_rank, all_rank, quotient_dimension, increments, quotient_basis, quotient_coordinates, quotient_connection)) in records.iter().enumerate() {
        let quotient_rows = quotient_coordinates.iter()
            .map(|row| format!("[{}]", row.iter().map(|entry| entry.0.to_string()).collect::<Vec<_>>().join(",")))
            .collect::<Vec<_>>().join(",");
        let rational_absolute_line = quotient_coordinates[6..]
            .iter()
            .map(|row| rational_reconstruction(row[3])
                .map(|(numerator, denominator)| format!("\"{numerator}/{denominator}\""))
                .unwrap_or_else(|| "null".to_string()))
            .collect::<Vec<_>>().join(",");
        let rational_connection = quotient_connection.iter().map(|row| {
            format!("[{}]", row.iter().map(|entry| rational_reconstruction(*entry)
                .map(|(numerator, denominator)| format!("\"{numerator}/{denominator}\""))
                .unwrap_or_else(|| "null".to_string())).collect::<Vec<_>>().join(","))
        }).collect::<Vec<_>>().join(",");
        println!("    {{\"s\":{},\"master\":{},\"consistent\":{},\"residual_zero\":{},\"rank\":{},\"fixed_mask\":{},\"fixed_coordinates\":{:?},\"equations\":{},\"unknowns\":{},\"pivot_hash\":{},\"exact_rank\":{},\"all_rank\":{},\"quotient_dimension\":{},\"class_rank_increments\":{:?},\"quotient_basis_class_indices\":{:?},\"quotient_coordinate_matrix\":[{}],\"absolute_line_coordinates_rational\":[{}],\"quotient_connection_rational\":[{}]}}{}",
            s, master, consistent, residual, rank, mask, coordinates, equations, unknowns, hash, exact_rank, all_rank, quotient_dimension,
            increments, quotient_basis, quotient_rows, rational_absolute_line, rational_connection,
            if index + 1 == records.len() { "" } else { "," });
    }
    println!("  ]");
    println!("}}");
}

fn quotient_derivative_matrix(
    geometry: &Geometry,
    class_columns: &[Poly],
    exact_columns: &[Poly],
    basis_indices: &[usize],
) -> Vec<Vec<F>> {
    let mut solving_columns: Vec<Poly> = basis_indices
        .iter().map(|index| class_columns[*index].clone()).collect();
    solving_columns.extend(exact_columns.iter().cloned());
    let classes = classes(geometry);
    basis_indices.iter().map(|index| {
        let derivative = target(geometry, &classes[*index]);
        solve_selected_coordinates(&solving_columns, &derivative, basis_indices.len())
    }).collect()
}

fn run_exceptional_interpolation() {
    let samples: Vec<(F, Vec<F>, F)> = (2_u64..=28)
        .map(|s| {
            let geometry = exceptional_p_chart_geometry(s, true);
            let class_columns: Vec<Poly> = classes(&geometry).iter()
                .map(|class| common(&geometry, class)).collect();
            let mut exact_columns = Vec::new();
            for (sa, sb) in [(1, 1), (1, 0), (0, 1), (0, 0)] {
                for monomial in monomials(8) {
                    exact_columns.push(exact(&geometry, sa, sb, monomial, false));
                    exact_columns.push(exact(&geometry, sa, sb, monomial, true));
                }
            }
            let (basis, coordinates) = quotient_coordinate_matrix(&class_columns, &exact_columns);
            assert_eq!(basis, vec![0, 1, 2, 6]);
            let connection = quotient_derivative_matrix(
                &geometry, &class_columns, &exact_columns, &basis);
            (F::n(s), coordinates[6..].iter().map(|row| row[3]).collect(), connection[3][3])
        })
        .collect();
    let discovery = &samples[..18];
    let verification = &samples[18..];
    println!("{{");
    println!("  \"schema\": \"marici.benincasa.rank12_u0_v2_exceptional_line_interpolation.v1\",");
    println!("  \"prime\": {},", P);
    println!("  \"basis\": [\"e4\"],");
    println!("  \"coordinates\": [");
    for coordinate in 0..6 {
        let values: Vec<(F, F)> = discovery.iter().map(|(s, row, _)| (*s, row[coordinate])).collect();
        let (numerator, denominator) = (0..=17)
            .find_map(|total| (0..=total).find_map(|denominator_degree| {
                let numerator_degree = total - denominator_degree;
                rational_interpolate(&values, numerator_degree, denominator_degree)
                    .filter(|(numerator, denominator)| verification.iter().all(|(s, row, _)| {
                        evaluate_coefficients(numerator, *s)
                            == row[coordinate].mul(evaluate_coefficients(denominator, *s))
                    }))
            }))
            .expect("bounded rational interpolation must succeed");
        let numerator_rational = numerator.iter().map(|coefficient| {
            let (n, d) = rational_reconstruction(*coefficient).expect("coefficient reconstruction");
            format!("\"{n}/{d}\"")
        }).collect::<Vec<_>>().join(",");
        let denominator_rational = denominator.iter().map(|coefficient| {
            let (n, d) = rational_reconstruction(*coefficient).expect("coefficient reconstruction");
            format!("\"{n}/{d}\"")
        }).collect::<Vec<_>>().join(",");
        println!("    {{\"class_index\":{},\"numerator_coefficients_ascending\":[{}],\"denominator_coefficients_ascending\":[{}],\"verification_points\":{}}}{}",
            coordinate + 6, numerator_rational, denominator_rational, verification.len(),
            if coordinate == 5 { "" } else { "," });
    }
    println!("  ],");
    let connection_values: Vec<(F, F)> = discovery.iter()
        .map(|(s, _, connection)| (*s, *connection)).collect();
    let (connection_numerator, connection_denominator) = (0..=17)
        .find_map(|total| (0..=total).find_map(|denominator_degree| {
            let numerator_degree = total - denominator_degree;
            rational_interpolate(&connection_values, numerator_degree, denominator_degree)
                .filter(|(numerator, denominator)| verification.iter().all(|(s, _, connection)| {
                    evaluate_coefficients(numerator, *s)
                        == connection.mul(evaluate_coefficients(denominator, *s))
                }))
        })).expect("absolute connection interpolation must succeed");
    let render = |coefficients: &[F]| coefficients.iter().map(|coefficient| {
        let (numerator, denominator) = rational_reconstruction(*coefficient).unwrap();
        format!("\"{numerator}/{denominator}\"")
    }).collect::<Vec<_>>().join(",");
    println!("  \"absolute_line_connection\": {{\"numerator_coefficients_ascending\":[{}],\"denominator_coefficients_ascending\":[{}],\"verification_points\":{}}}",
        render(&connection_numerator), render(&connection_denominator), verification.len());
    println!("}}");
}

fn evaluate_coefficients(coefficients: &[F], value: F) -> F {
    coefficients.iter().rev().fold(F::z(), |accumulator, coefficient| {
        accumulator.mul(value).add(*coefficient)
    })
}

fn rational_interpolate(samples: &[(F, F)], numerator_degree: usize, denominator_degree: usize)
    -> Option<(Vec<F>, Vec<F>)>
{
    let unknowns = numerator_degree + 1 + denominator_degree;
    if samples.len() < unknowns {
        return None;
    }
    let mut matrix = Vec::new();
    for (x, y) in samples {
        let mut powers = vec![F::o()];
        for degree in 1..=numerator_degree.max(denominator_degree) {
            powers.push(powers[degree - 1].mul(*x));
        }
        let mut row = Vec::new();
        row.extend(powers[..=numerator_degree].iter().copied());
        for power in powers.iter().take(denominator_degree) {
            row.push(y.mul(*power).neg());
        }
        row.push(y.mul(powers[denominator_degree]));
        matrix.push(row);
    }
    let rows = matrix.len();
    let mut pivot_row = 0;
    let mut pivots = Vec::new();
    for column in 0..unknowns {
        let row = (pivot_row..rows).find(|row| matrix[*row][column].0 != 0)?;
        matrix.swap(pivot_row, row);
        let inverse = matrix[pivot_row][column].inv();
        for entry in column..=unknowns {
            matrix[pivot_row][entry] = matrix[pivot_row][entry].mul(inverse);
        }
        for row in 0..rows {
            if row != pivot_row && matrix[row][column].0 != 0 {
                let multiplier = matrix[row][column];
                for entry in column..=unknowns {
                    matrix[row][entry] = matrix[row][entry]
                        .sub(multiplier.mul(matrix[pivot_row][entry]));
                }
            }
        }
        pivots.push((pivot_row, column));
        pivot_row += 1;
    }
    if !(0..rows).all(|row| {
        !(0..unknowns).all(|column| matrix[row][column].0 == 0)
            || matrix[row][unknowns].0 == 0
    }) {
        return None;
    }
    let solution: Vec<F> = (0..unknowns).map(|column| {
        let row = pivots.iter().find_map(|(row, pivot)| (*pivot == column).then_some(*row))?;
        Some(matrix[row][unknowns])
    }).collect::<Option<_>>()?;
    let numerator = solution[..=numerator_degree].to_vec();
    let mut denominator = solution[numerator_degree + 1..].to_vec();
    denominator.push(F::o());
    Some((numerator, denominator))
}

fn rational_reconstruction(value: F) -> Option<(i128, i128)> {
    let modulus = P as i128;
    let bound = ((modulus / 2) as f64).sqrt() as i128;
    let mut old_remainder = modulus;
    let mut remainder = value.0 as i128;
    let mut old_denominator = 0_i128;
    let mut denominator = 1_i128;
    while remainder.abs() > bound {
        let quotient = old_remainder / remainder;
        (old_remainder, remainder) = (remainder, old_remainder - quotient * remainder);
        (old_denominator, denominator) =
            (denominator, old_denominator - quotient * denominator);
    }
    if denominator == 0 || denominator.abs() > bound {
        return None;
    }
    let mut numerator = remainder;
    if denominator < 0 {
        numerator = -numerator;
        denominator = -denominator;
    }
    if (numerator - value.0 as i128 * denominator).rem_euclid(modulus) != 0 {
        return None;
    }
    Some((numerator, denominator))
}

fn quotient_coordinate_matrix(class_columns: &[Poly], exact_columns: &[Poly]) -> (Vec<usize>, Vec<Vec<F>>) {
    let mut basis_indices = Vec::new();
    let mut working = exact_columns.to_vec();
    let mut rank = polynomial_column_rank(&working);
    for (index, class_column) in class_columns.iter().enumerate() {
        let mut candidate = working.clone();
        candidate.push(class_column.clone());
        let next_rank = polynomial_column_rank(&candidate);
        if next_rank > rank {
            basis_indices.push(index);
            working.push(class_column.clone());
            rank = next_rank;
        }
    }
    assert_eq!(basis_indices.len(), 4);

    let mut solving_columns: Vec<Poly> = basis_indices
        .iter()
        .map(|index| class_columns[*index].clone())
        .collect();
    solving_columns.extend(exact_columns.iter().cloned());
    let coordinates = class_columns
        .iter()
        .map(|target| solve_selected_coordinates(&solving_columns, target, basis_indices.len()))
        .collect();
    (basis_indices, coordinates)
}

fn solve_selected_coordinates(columns: &[Poly], target: &Poly, selected: usize) -> Vec<F> {
    let mut monomials = BTreeSet::new();
    for column in columns {
        monomials.extend(column.0.keys().copied());
    }
    monomials.extend(target.0.keys().copied());
    let unknowns = columns.len();
    let mut matrix: Vec<Vec<F>> = monomials
        .iter()
        .map(|monomial| {
            let mut row: Vec<F> = columns.iter()
                .map(|column| column.0.get(monomial).copied().unwrap_or(F::z()))
                .collect();
            row.push(target.0.get(monomial).copied().unwrap_or(F::z()));
            row
        })
        .collect();
    let rows = matrix.len();
    let mut pivots = Vec::new();
    let mut pivot_row = 0;
    for column in 0..unknowns {
        let Some(row) = (pivot_row..rows).find(|row| matrix[*row][column].0 != 0) else {
            continue;
        };
        matrix.swap(pivot_row, row);
        let inverse = matrix[pivot_row][column].inv();
        for entry in column..=unknowns {
            matrix[pivot_row][entry] = matrix[pivot_row][entry].mul(inverse);
        }
        for row in 0..rows {
            if row != pivot_row && matrix[row][column].0 != 0 {
                let multiplier = matrix[row][column];
                for entry in column..=unknowns {
                    matrix[row][entry] = matrix[row][entry]
                        .sub(multiplier.mul(matrix[pivot_row][entry]));
                }
            }
        }
        pivots.push((pivot_row, column));
        pivot_row += 1;
    }
    assert!((0..rows).all(|row| {
        !(0..unknowns).all(|column| matrix[row][column].0 == 0)
            || matrix[row][unknowns].0 == 0
    }));
    (0..selected)
        .map(|column| {
            let row = pivots.iter().find_map(|(row, pivot)| (*pivot == column).then_some(*row))
                .expect("selected quotient coordinate must pivot");
            assert!((selected..unknowns).all(|free| {
                !pivots.iter().all(|(_, pivot)| *pivot != free) || matrix[row][free].0 == 0
            }), "selected quotient coordinate must be independent of exact primitive choices");
            matrix[row][unknowns]
        })
        .collect()
}

fn polynomial_column_rank(columns: &[Poly]) -> usize {
    let mut monomials = BTreeSet::new();
    for column in columns {
        monomials.extend(column.0.keys().copied());
    }
    let mut matrix: Vec<Vec<F>> = monomials
        .iter()
        .map(|monomial| columns.iter()
            .map(|column| column.0.get(monomial).copied().unwrap_or(F::z()))
            .collect())
        .collect();
    let rows = matrix.len();
    let column_count = columns.len();
    let mut pivot_row = 0;
    for column in 0..column_count {
        let Some(row) = (pivot_row..rows).find(|row| matrix[*row][column].0 != 0) else {
            continue;
        };
        matrix.swap(pivot_row, row);
        let inverse = matrix[pivot_row][column].inv();
        for entry in column..column_count {
            matrix[pivot_row][entry] = matrix[pivot_row][entry].mul(inverse);
        }
        for row in 0..rows {
            if row != pivot_row && matrix[row][column].0 != 0 {
                let multiplier = matrix[row][column];
                for entry in column..column_count {
                    matrix[row][entry] = matrix[row][entry]
                        .sub(multiplier.mul(matrix[pivot_row][entry]));
                }
            }
        }
        pivot_row += 1;
        if pivot_row == rows {
            break;
        }
    }
    pivot_row
}

fn main() {
    let reconstruction_mode = std::env::var_os("MARICI_RECONSTRUCTION_MODE").is_some();
    let master_count = if reconstruction_mode { 3 } else { 12 };
    let samples: Vec<(u64, u64)> = std::env::var("MARICI_UV_SAMPLES")
        .ok()
        .map(|raw| {
            raw.split(';').map(|pair| {
                let mut fields = pair.split(',');
                let u = fields.next().unwrap().parse().unwrap();
                let v = fields.next().unwrap().parse().unwrap();
                assert!(fields.next().is_none());
                (u, v)
            }).collect()
        })
        .unwrap_or_else(|| vec![(7, 11), (13, 19), (23, 29)]);
    let sample_count = samples.len();
    if std::env::var_os("MARICI_EXCEPTIONAL_INTERPOLATE").is_some() {
        run_exceptional_interpolation();
        return;
    }
    if std::env::var_os("MARICI_EXCEPTIONAL_P_CHART").is_some() {
        run_exceptional_p_chart(&samples);
        return;
    }
    if std::env::var_os("MARICI_DUAL_MODE").is_some() {
        run_dual(&samples);
        return;
    }
    if std::env::var_os("MARICI_PRIMAL_WITNESS_MODE").is_some() {
        run_primal_witness(&samples);
        return;
    }
    if std::env::var_os("MARICI_POLYNOMIAL_MODULE_MODE").is_some() {
        run_polynomial_module_gate(&samples);
        return;
    }
    let mut wall_blocks = Vec::new();
    let mut min_fixed = 12;
    let mut rank_range = (usize::MAX, 0usize);
    let mut fixed_masks = BTreeSet::new();
    let mut equations = 0;
    let mut unknowns = 0;
    let mut pivot_records = Vec::new();
    let mut rejected = Vec::new();
    for (u, v) in samples {
        for axis in ['u', 'v'] {
            let g = geometry(u, v, axis);
            let gate = solve(&g, 0, 8);
            let (gate_mask, gate_coordinates) = fixed_signature(&gate);
            if !gate.consistent || gate.rank != 117 || gate_mask != 3847 || gate_coordinates != vec![0,1,2,8,9,10,11] {
                rejected.push((u, v, axis, gate.consistent, gate.rank, gate_mask, pivot_hash(&gate.pivot_cols)));
                continue;
            }
            let mut wall_block = vec![vec![F::z(); 3]; 3];
            let mut fixed_extension_block = vec![vec![F::z(); 3]; 4];
            for master in 0..master_count {
                let s = solve(&g, master, 8);
                assert!(s.consistent);
                assert!(s.residual_zero);
                let (fixed_mask, fixed_coordinates) = fixed_signature(&s);
                assert_eq!(s.rank, 117, "bad-prime/sample rank at p={P} u={u} v={v} axis={axis} master={master}");
                assert_eq!(fixed_mask, 3847, "bad-prime/sample fixed mask at p={P} u={u} v={v} axis={axis} master={master}");
                assert_eq!(fixed_coordinates, vec![0,1,2,8,9,10,11],
                    "bad-prime/sample fixed coordinates at p={P} u={u} v={v} axis={axis} master={master}");
                pivot_records.push((u, v, axis, master, s.rank, fixed_mask, pivot_hash(&s.pivot_cols)));
                let nf = s.fixed.iter().filter(|q| **q).count();
                min_fixed = min_fixed.min(nf);
                fixed_masks.insert(s.fixed.iter().enumerate().fold(0u16, |m, (i, q)| {
                    if *q {
                        m | (1u16 << i)
                    } else {
                        m
                    }
                }));
                rank_range.0 = rank_range.0.min(s.rank);
                rank_range.1 = rank_range.1.max(s.rank);
                equations = s.equations;
                unknowns = s.unknowns;
                if master >= 3 {
                    assert!(s.values[..3].iter().all(|q| q.0 == 0));
                } else {
                    assert!(s.fixed[..3].iter().all(|q| *q));
                    for row in 0..3 {
                        wall_block[row][master] = s.values[row];
                    }
                    for (out_row, row) in (8..12).enumerate() {
                        assert!(s.fixed[row]);
                        fixed_extension_block[out_row][master] = s.values[row];
                    }
                }
            }
            wall_blocks.push((u, v, axis, wall_block, fixed_extension_block));
        }
    }
    assert_eq!(unknowns, 372);
    assert_eq!(min_fixed, 7);
    assert_eq!(fixed_masks, BTreeSet::from([3847u16]));
    let fixed_extension_nonzero = wall_blocks
        .iter()
        .flat_map(|(_, _, _, _, block)| block.iter().flatten())
        .filter(|q| q.0 != 0)
        .count();
    assert_eq!(fixed_extension_nonzero, wall_blocks.len() * 4 * 3);
    println!("{{");
    println!("  \"schema\": \"marici.benincasa.marked_relative_reduction_engine.v1\",");
    println!("  \"prime\": {},", P);
    println!("  \"samples\": {},", sample_count);
    println!("  \"accepted_direction_samples\": {},", wall_blocks.len());
    println!("  \"rejected_direction_samples\": [");
    for (i, (u, v, axis, consistent, rank, mask, hash)) in rejected.iter().enumerate() {
        println!("    {{\"u\":{},\"v\":{},\"axis\":\"{}\",\"consistent\":{},\"rank\":{},\"fixed_mask\":{},\"pivot_hash\":{}}}{}",
            u, v, axis, consistent, rank, mask, hash, if i + 1 == rejected.len() { "" } else { "," });
    }
    println!("  ],");
    println!("  \"directions\": [\"u\",\"v\"],");
    println!("  \"masters\": {},", master_count);
    println!("  \"reconstruction_mode\": {},", reconstruction_mode);
    println!("  \"primitive_degree\": 8,");
    println!("  \"unknowns_per_reduction\": {},", unknowns);
    println!("  \"equations_per_reduction\": {},", equations);
    println!("  \"rank_range\": [{},{}],", rank_range.0, rank_range.1);
    println!("  \"minimum_fixed_master_coordinates\": {},", min_fixed);
    println!("  \"fixed_coordinate_masks_decimal\": [3847],");
    println!("  \"pivot_rank_records\": [");
    for (i, (u, v, axis, master, rank, mask, hash)) in pivot_records.iter().enumerate() {
        println!("    {{\"u\":{},\"v\":{},\"axis\":\"{}\",\"master\":{},\"rank\":{},\"fixed_mask\":{},\"pivot_hash\":{}}}{}",
            u, v, axis, master, rank, mask, hash,
            if i + 1 == pivot_records.len() { "" } else { "," });
    }
    println!("  ],");
    println!("  \"all_cleared_identities_zero\": true,");
    println!("  \"absolute_to_marked_block_zero\": true,");
    println!("  \"fixed_extension_e6_e9_nonzero_entries\": {},", fixed_extension_nonzero);
    println!("  \"wall_quotient_blocks\": [");
    for (sample_index, (u, v, axis, block, fixed_extension)) in wall_blocks.iter().enumerate() {
        let rows: Vec<String> = block
            .iter()
            .map(|row| format!("[{}]", row.iter().map(|q| q.0.to_string()).collect::<Vec<_>>().join(",")))
            .collect();
        println!(
            "    {{\"u\":{},\"v\":{},\"axis\":\"{}\",\"matrix_mod_p\":[{}],\"fixed_extension_e6_e9_mod_p\":[{}]}}{}",
            u,
            v,
            axis,
            rows.join(","),
            fixed_extension.iter().map(|row| format!("[{}]", row.iter().map(|q| q.0.to_string()).collect::<Vec<_>>().join(","))).collect::<Vec<_>>().join(","),
            if sample_index + 1 == wall_blocks.len() { "" } else { "," }
        );
    }
    println!("  ],");
    println!(
        "  \"status\": \"generic four-stratum engine passes; wall Laurent replication pending\""
    );
    println!("}}");
}
