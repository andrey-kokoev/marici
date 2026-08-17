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
    Sol {
        rank: rr,
        fixed,
        values,
        residual_zero: check.sub(&rhs).0.is_empty(),
        equations: rows,
        unknowns: n,
    }
}

fn rational_jet(samples: &[(F, F)], max_degree: usize) -> (F, F, usize, usize) {
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
            return (n0, n1.sub(n0.mul(d1)), nd, dd);
        }
    }
    panic!("no bounded rational jet")
}

fn valuation_from_t2(samples: &[(F, F)]) -> (i32, usize, usize) {
    let z = rational_jet(samples, 24);
    let valuation = if z.0 .0 != 0 {
        -2
    } else if z.1 .0 != 0 {
        -1
    } else {
        0
    };
    (valuation, z.2, z.3)
}

fn chart(name: &str, r0: u64) -> (i32, i32, usize, usize) {
    let cols = [0usize, 1, 2, 8, 9, 10, 11];
    let col_weights = [2i32, 2, 2, 0, 0, 1, 1];
    let mut radial = vec![vec![Vec::<(F, F)>::new(); 12]; 3];
    let mut tangent = vec![vec![Vec::<(F, F)>::new(); 12]; 3];
    for ti in 31_u64..=110 {
        let t = F::n(ti);
        let r = F::n(r0);
        let eight = F::n(8);
        let (u, v) = if name == "E" {
            (t, t.mul(r))
        } else {
            (t.mul(r), t)
        };
        let gu = geometry(u.0, v.0, 'u');
        let gv = geometry(u.0, v.0, 'v');
        let s6u = solve(&gu, 8, 8);
        let s6v = solve(&gv, 8, 8);
        let g = F::o().mul(eight.mul(u).inv());
        let (dgt, dgr) = if name == "E" {
            (eight.mul(t.pow(2)).inv().neg(), F::z())
        } else {
            (
                eight.mul(r).mul(t.pow(2)).inv().neg(),
                eight.mul(t).mul(r.pow(2)).inv().neg(),
            )
        };
        for master in 0..3 {
            let su = solve(&gu, master, 8);
            let sv = solve(&gv, master, 8);
            for col in cols {
                assert!(su.fixed[col] && sv.fixed[col] && s6u.fixed[col] && s6v.fixed[col]);
                // The reduction engine has the opposite global connection sign
                // from the frozen source convention, calibrated by e6/8.
                let au = su.values[col].neg();
                let av = sv.values[col].neg();
                let a6u = s6u.values[col].neg();
                let a6v = s6v.values[col].neg();
                let (mut at, mut ar, at6, ar6) = if name == "E" {
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
                if master == 0 {
                    at = at.add(g.mul(at6));
                    ar = ar.add(g.mul(ar6));
                    if col == 8 {
                        let a00 = su.values[0].neg();
                        let b00 = sv.values[0].neg();
                        let (at00, ar00) = if name == "E" {
                            (a00.add(r.mul(b00)), t.mul(b00))
                        } else {
                            (r.mul(a00).add(b00), t.mul(a00))
                        };
                        at = at.add(dgt).sub(g.mul(at00));
                        ar = ar.add(dgr).sub(g.mul(ar00));
                    }
                } else if col == 8 {
                    let ai0u = su.values[0].neg();
                    let ai0v = sv.values[0].neg();
                    let (ai0t, ai0r) = if name == "E" {
                        (ai0u.add(r.mul(ai0v)), t.mul(ai0v))
                    } else {
                        (r.mul(ai0u).add(ai0v), t.mul(ai0u))
                    };
                    at = at.sub(g.mul(ai0t));
                    ar = ar.sub(g.mul(ai0r));
                }
                radial[master][col].push((t, at.mul(t.pow(2))));
                tangent[master][col].push((t, ar.mul(t.pow(2))));
            }
        }
    }
    let mut min_rad = 9;
    let mut min_tan = 9;
    let mut maxn = 0;
    let mut maxd = 0;
    for m in 0..3 {
        for (ci, c) in cols.iter().enumerate() {
            let zr = valuation_from_t2(&radial[m][*c]);
            let zt = valuation_from_t2(&tangent[m][*c]);
            maxn = maxn.max(zr.1).max(zt.1);
            maxd = maxd.max(zr.2).max(zt.2);
            let vr = zr.0 + 2 - col_weights[ci];
            let vt = zt.0 + 2 - col_weights[ci];
            min_rad = min_rad.min(vr);
            min_tan = min_tan.min(vt);
        }
    }
    assert!(min_rad >= -1, "nonlog radial valuation {min_rad}");
    assert!(
        min_tan >= 0,
        "singular exceptional tangent valuation {min_tan}"
    );
    (min_rad, min_tan, maxn, maxd)
}

fn main() {
    let mut min_rad = 9;
    let mut min_tan = 9;
    let mut maxn = 0;
    let mut maxd = 0;
    for name in ["E", "V"] {
        for r in [2u64, 3, 4, 5] {
            let z = chart(name, r);
            min_rad = min_rad.min(z.0);
            min_tan = min_tan.min(z.1);
            maxn = maxn.max(z.2);
            maxd = maxd.max(z.3);
        }
    }
    println!("{{");
    println!("  \"schema\": \"marici.benincasa.marked_radial_pullback.v1\",");
    println!("  \"charts\": [\"u=t,v=tr\",\"v=t,u=tr\"],");
    println!("  \"exceptional_directions\": [2,3,4,5],");
    println!("  \"marked_weights\": [2,2,2],");
    println!("  \"absolute_tail_weights\": [0,0,1,1],");
    println!("  \"minimum_radial_valuation\": {min_rad},");
    println!("  \"minimum_exceptional_tangent_valuation\": {min_tan},");
    println!("  \"max_numerator_degree\": {maxn},");
    println!("  \"max_denominator_degree\": {maxd},");
    println!("  \"new_generic_radial_support\": false");
    println!("}}");
}
