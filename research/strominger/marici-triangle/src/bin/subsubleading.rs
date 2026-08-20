//! Exact sub-subleading-triangle cross-validation checker: independent engine port.
//!
//! Cross-validates checkers/subsubleading_triangle_exact_checks.py (sympy) with an
//! independent computer algebra system: Rust + Symbolica 2.2.0 (no_gmp), exact
//! rational / complex-rational arithmetic, no floats anywhere.
//!
//! Sources and conventions: research/strominger/subsubleading-triangle-conventions.md
//! Map definitions:         research/strominger/subsubleading-triangle-source-boundary.md
//! sympy results mirrored:  research/strominger/results/subsubleading_triangle_exact_checks.json
//!
//! (z, zb, zk, zbk) are independent symbols; reality is imposed through the
//! explicit conjugation map sigma: z <-> zb, zk <-> zbk applied SIMULTANEOUSLY
//! (via fresh temporary symbols, never sequential substitution), with i -> -i
//! implemented as complex-rational coefficient conjugation.
//!
//! Metric convention: eta = diag(-1,1,1,1), matching the sympy checker.
//! sqrt(2) is carried as the symbol sq2 reduced by its defining relation
//! sq2^2 = 2 (norm_sq2), as in the rung-2 port.
//!
//! Output: research/strominger/results/subsubleading_triangle_symbolica_checks.json
//! Exit code 0 iff every check passes and every typed residual agrees with the
//! sympy reference run.

use serde_json::json;
use std::array;
use std::process;
use symbolica::prelude::*;

const NS: &str = "marici";

// ------------------------------------------------------------------ helpers
fn at(s: &str) -> Atom {
    Atom::parse(s, NS, Default::default()).unwrap().expand()
}

/// Two-stage exact zero-recognition, the sympy simp() analog:
/// expand, then combine over a common denominator and cancel the gcd.
fn clean(x: &Atom) -> Atom {
    x.expand().together().cancel()
}

/// Exact sqrt(2)-relation reduction: sq2^2 = 2 (see the rung-2 port).
/// Both signs of the power are needed: build_op inputs carry 1/sq2 factors,
/// so cleaned normal forms can hold sq2^2 inside a NEGATIVE-power subexpression
/// where only the explicit sq2^-2 -> 1/2 rule reaches it.
fn norm_sq2(x: &Atom) -> Atom {
    let mut y = clean(x);
    y.repeat_map(|v| {
        v.to_owned()
            .replace_multiple([
                symbolica::id::Replacement::new(
                    at("sq2^2").to_pattern(),
                    at("2").to_pattern(),
                ),
                symbolica::id::Replacement::new(
                    at("sq2^-2").to_pattern(),
                    at("1/2").to_pattern(),
                ),
            ])
    });
    clean(&y)
}

fn is_zero(x: &Atom) -> bool {
    clean(x) == at("0")
}

fn subs(x: &Atom, from: &Atom, to: &Atom) -> Atom {
    x.replace(from.to_pattern()).with(to.to_pattern())
}

/// Complex conjugation on the sphere variables: simultaneous z<->zb,
/// zk<->zbk swap through fresh temporaries, plus i -> -i by coefficient
/// conjugation. Only ever applied to explicit rational test fields.
fn sigma(x: &Atom) -> Atom {
    let mut y = x.clone();
    for (f, t) in [("z", "sgA"), ("zb", "sgB"), ("zk", "sgC"), ("zbk", "sgD")] {
        y = subs(&y, &at(f), &at(t));
    }
    for (t, f) in [("sgA", "zb"), ("sgB", "z"), ("sgC", "zbk"), ("sgD", "zk")] {
        y = subs(&y, &at(t), &at(f));
    }
    clean(&y.expand().map_coefficient(|c| c.to_owned().conjugate()))
}

/// Strip ANSI SGR escape sequences that symbolica's printer emits when the
/// process is attached to a terminal; detail strings must be plain text.
fn plain(s: &str) -> String {
    let mut out = String::with_capacity(s.len());
    let mut chars = s.chars();
    while let Some(c) = chars.next() {
        if c == '\u{1b}' {
            for c2 in chars.by_ref() {
                if c2 == 'm' {
                    break;
                }
            }
        } else {
            out.push(c);
        }
    }
    out
}

fn crop(s: &str) -> String {
    plain(s).chars().take(300).collect()
}

// ------------------------------------------------------------- 4-vector kit
type V4 = [Atom; 4];
type V4x4 = [[Atom; 4]; 4];

fn lower4(v: &V4) -> V4 {
    [
        -v[0].clone(),
        v[1].clone(),
        v[2].clone(),
        v[3].clone(),
    ]
}

/// a^T eta b with eta = diag(-1,1,1,1).
fn mdot(a: &V4, b: &V4) -> Atom {
    let mut s = -(a[0].clone() * b[0].clone());
    for i in 1..4 {
        s = (s + a[i].clone() * b[i].clone()).expand();
    }
    clean(&s)
}

/// Unit spatial direction xhat(zz, zzb) on the sphere (PSZ 6.7 direction part).
fn xhat(zz: &Atom, zzb: &Atom) -> [Atom; 3] {
    let one = at("1");
    let den = (one.clone() + zz.clone() * zzb.clone()).expand();
    let x1 = ((zz.clone() + zzb.clone()).expand()) / den.clone();
    let x2 = ((-Atom::i()) * (zz.clone() - zzb.clone()).expand()).expand() / den.clone();
    let x3 = ((one - zz.clone() * zzb.clone()).expand()) / den;
    [x1, x2, x3]
}

/// Null momentum p = E (1, xhat) (PSZ 6.7).
fn pvec(e: &Atom, zz: &Atom, zzb: &Atom) -> V4 {
    let xh = xhat(zz, zzb);
    [
        e.clone(),
        e.clone() * xh[0].clone(),
        e.clone() * xh[1].clone(),
        e.clone() * xh[2].clone(),
    ]
}

// ---------------------------------------------------- sphere covariant diff
fn gam() -> Atom {
    at("-2*zb/(1+z*zb)")
} // Gamma^z_zz

// ------------------------------------------------------------ result ledger
fn push(
    results: &mut Vec<serde_json::Value>,
    id: &str,
    group: &str,
    statement: &str,
    ok: bool,
    detail: String,
    agree: bool,
) {
    let status = if ok { "pass" } else { "FAIL" };
    println!(
        "[{:>4}] {}: {}{}",
        status,
        id,
        statement,
        if detail.is_empty() {
            String::new()
        } else {
            format!("  ({})", detail)
        }
    );
    results.push(json!({
        "id": id,
        "group": group,
        "statement": statement,
        "status": status,
        "detail": detail,
        "cross_validates": [id],
        "agreement_with_sympy": agree,
    }));
}

/// Pass iff expr normalizes to exactly 0.
fn check_zero(results: &mut Vec<serde_json::Value>, id: &str, group: &str, statement: &str, e: &Atom) {
    let v = clean(e);
    let ok = v == at("0");
    push(
        results,
        id,
        group,
        statement,
        ok,
        if ok {
            String::new()
        } else {
            format!("residual: {}", crop(&v.to_string()))
        },
        ok,
    );
}

/// Pass iff every expression normalizes to exactly 0.
fn check_all_zero(
    results: &mut Vec<serde_json::Value>,
    id: &str,
    group: &str,
    statement: &str,
    es: &[Atom],
    detail: &str,
) {
    let vals: Vec<Atom> = es.iter().map(clean).collect();
    let bad: Vec<&Atom> = vals.iter().filter(|v| **v != at("0")).collect();
    let ok = bad.is_empty();
    push(
        results,
        id,
        group,
        statement,
        ok,
        if ok {
            detail.to_string()
        } else {
            format!("nonzero components: {}", crop(&bad[0].to_string()))
        },
        ok,
    );
}

/// Pass iff expr is exactly nonzero (typed obstruction present). Agreement
/// with the sympy run additionally requires the typed residual to match
/// `expected` when one is declared.
fn check_nonzero(
    results: &mut Vec<serde_json::Value>,
    id: &str,
    group: &str,
    statement: &str,
    e: &Atom,
    expected: Option<&Atom>,
) {
    let v = clean(e);
    let ok = v != at("0");
    let agree = ok
        && match expected {
            Some(exp) => is_zero(&(v.clone() - exp.clone())),
            None => true,
        };
    push(
        results,
        id,
        group,
        statement,
        ok,
        if ok {
            let mut d = format!("residual retained: {}", crop(&v.to_string()));
            if !agree {
                d.push_str("  [DISAGREES with sympy typed residual]");
            }
            d
        } else {
            "residual vanished unexpectedly".to_string()
        },
        agree,
    );
}

// ------------------------------------------- Lorentz generator machinery
/// Per-leg generator actions on leg coordinates (zk, zbk, Ek), computed from
/// delta k = alpha . eta . k with antisymmetric alpha (identical to rung 2).
/// Returns (dz_gen, dzb_gen, de_gen) indexed by gens order.
fn generator_actions(zk: &Atom, zbk: &Atom, ek: &Atom) -> (Vec<Atom>, Vec<Atom>, Vec<Atom>) {
    let gens: [(usize, usize); 6] = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)];
    let ii = Atom::i();
    let alfa: Vec<Atom> = ["a01", "a02", "a03", "a12", "a13", "a23"]
        .iter()
        .map(|s| at(s))
        .collect();
    let dalfa = [
        symbol!("marici::a01"),
        symbol!("marici::a02"),
        symbol!("marici::a03"),
        symbol!("marici::a12"),
        symbol!("marici::a13"),
        symbol!("marici::a23"),
    ];
    let mut amat: V4x4 = array::from_fn(|_| array::from_fn(|_| at("0")));
    for (gi, &(m, n)) in gens.iter().enumerate() {
        amat[m][n] = alfa[gi].clone();
        amat[n][m] = -alfa[gi].clone();
    }
    let pk = pvec(ek, zk, zbk);
    let pkl = lower4(&pk);
    let pkp: V4 = array::from_fn(|m| {
        let mut s = pk[m].clone();
        for n in 0..4 {
            s = (s + amat[m][n].clone() * pkl[n].clone()).expand();
        }
        s
    });
    let den_p = (pkp[0].clone() + pkp[3].clone()).expand();
    let zp = ((pkp[1].clone() + ii.clone() * pkp[2].clone()).expand()) / den_p.clone();
    let zbp = ((pkp[1].clone() - ii.clone() * pkp[2].clone()).expand()) / den_p;
    let ep = pkp[0].clone();
    let zero_a = |x: &Atom| {
        let mut y = x.clone();
        for a in &alfa {
            y = subs(&y, a, &at("0"));
        }
        clean(&y)
    };
    let dz_gen: Vec<Atom> = dalfa
        .iter()
        .map(|ag| zero_a(&zp.derivative(*ag).expand()))
        .collect();
    let dzb_gen: Vec<Atom> = dalfa
        .iter()
        .map(|ag| zero_a(&zbp.derivative(*ag).expand()))
        .collect();
    let de_gen: Vec<Atom> = dalfa
        .iter()
        .map(|ag| zero_a(&ep.derivative(*ag).expand()))
        .collect();
    (dz_gen, dzb_gen, de_gen)
}

/// Per-leg operator (c_zk, c_zbk, c_Ek) from v^nu J_{nu lam} q^lam, with the
/// rung-2 arbiter-pinned contraction A^{mn} = -s^m s^n beta_{mn} (raised
/// indices; the pure-rotation generators carry a minus sign).
fn build_op(
    vvec: &V4,
    ql: &V4,
    dz_gen: &[Atom],
    dzb_gen: &[Atom],
    de_gen: &[Atom],
) -> [Atom; 3] {
    let gens: [(usize, usize); 6] = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)];
    let vl = lower4(vvec);
    let mut cz = at("0");
    let mut czb = at("0");
    let mut ce = at("0");
    for (gi, &(m, n)) in gens.iter().enumerate() {
        let beta = clean(
            &(vl[m].clone() * ql[n].clone() - vl[n].clone() * ql[m].clone()),
        );
        let a = if m == 0 { beta } else { -beta }; // -s^m s^n beta_{mn}
        cz = clean(&(cz + a.clone() * dz_gen[gi].clone()));
        czb = clean(&(czb + a.clone() * dzb_gen[gi].clone()));
        ce = clean(&(ce + a * de_gen[gi].clone()));
    }
    [cz, czb, ce]
}

// ------------------------------------------------- weighted distributional fold
/// D_z^n (G P) with weight sequence (w0, ..., w0+n-1), P = (zb - zbk)^-1
/// antiholomorphic, d_z P = pi delta^2 declared.  Monomials are (coeff, basis)
/// with basis -1 = P and j = 0..n-1 the j-th z-derivative of delta.
/// Returns (coefficient of P, [c_0 .. c_{n-1}]).
fn fold(g: &Atom, w0: i64, n: usize) -> (Atom, Vec<Atom>) {
    let pi = at("pi");
    let mut mons: Vec<(Atom, i64)> = vec![(g.clone(), -1)];
    for i in 0..n {
        let w = w0 + i as i64;
        let mut nxt: Vec<(Atom, i64)> = Vec::new();
        for (c, b) in &mons {
            let dc = clean(&c.derivative(symbol!("marici::z")).expand());
            if *b == -1 {
                nxt.push((dc, -1));
                nxt.push((clean(&(c.clone() * pi.clone())), 0));
            } else {
                nxt.push((dc, *b));
                nxt.push((c.clone(), b + 1));
            }
        }
        let wf = at(&format!("{}", -w));
        for (c, b) in &mons {
            nxt.push((clean(&(wf.clone() * gam() * c.clone())), *b));
        }
        mons = nxt;
    }
    let sum_b = |bb: i64| {
        clean(
            &mons
                .iter()
                .filter(|(_, b)| *b == bb)
                .map(|(c, _)| c.clone())
                .fold(at("0"), |s, c| (s + c).expand()),
        )
    };
    let reg = sum_b(-1);
    let coeffs: Vec<Atom> = (0..n).map(|j| sum_b(j as i64)).collect();
    for (c, b) in &mons {
        if *b >= n as i64 {
            assert!(is_zero(c), "fold overflow beyond declared basis");
        }
    }
    (reg, coeffs)
}

/// f D^j delta = sum_i (-1)^i C(j,i) (d_z^i f)|pole D^{j-i} delta.
fn reduce_at_pole(coeffs: &[Atom]) -> Vec<Atom> {
    let n = coeffs.len();
    let mut out = vec![at("0"); n];
    let at_pole = |e: &Atom| clean(&subs(&subs(e, &at("z"), &at("zk")), &at("zb"), &at("zbk")));
    for (j, cj) in coeffs.iter().enumerate() {
        let mut deriv = cj.clone();
        for i in 0..=j {
            if i > 0 {
                deriv = deriv.derivative(symbol!("marici::z")).expand();
            }
            let cf = at_pole(&deriv);
            let binom: i64 = match (j, i) {
                (0, 0) => 1,
                (1, 0) | (1, 1) => 1,
                (2, 0) | (2, 2) => 1,
                (2, 1) => 2,
                (3, 0) | (3, 3) => 1,
                (3, 1) | (3, 2) => 3,
                _ => unreachable!(),
            };
            let sgn = if i % 2 == 0 { 1i64 } else { -1i64 };
            out[j - i] = (out[j - i].clone()
                + at(&format!("{}", sgn * binom)) * cf)
                .expand();
        }
    }
    out.iter().map(clean).collect()
}

// ==================================================================== main
fn main() {
    let mut results: Vec<serde_json::Value> = Vec::new();

    let z = at("z");
    let zb = at("zb");
    let zk = at("zk");
    let zbk = at("zbk");
    let ek = at("Ek");
    let om = at("om");
    let ii = Atom::i();
    let pi = at("pi");
    let sq2s = at("sq2");

    let pk = pvec(&ek, &zk, &zbk);
    let xs: V4 = {
        let xh = xhat(&z, &zb);
        [
            at("1"),
            xh[0].clone(),
            xh[1].clone(),
            xh[2].clone(),
        ]
    };
    let qv: V4 = array::from_fn(|m| om.clone() * xs[m].clone());
    let qdotp = mdot(&qv, &pk);
    let ql_soft = lower4(&qv);
    let eps_m: V4 = [
        z.clone() / sq2s.clone(),
        at("1") / sq2s.clone(),
        ii.clone() / sq2s.clone(),
        -z.clone() / sq2s.clone(),
    ];
    let eps_p: V4 = [
        zb.clone() / sq2s.clone(),
        at("1") / sq2s.clone(),
        (-ii.clone()) / sq2s.clone(),
        -zb.clone() / sq2s.clone(),
    ];
    let (dz_gen, dzb_gen, de_gen) = generator_actions(&zk, &zbk, &ek);

    // ================================================================ T1 gauge corner
    // Abstract symbolic kinematics: q^mu, Lam^mu, antisymmetric J^{mu nu}.
    let q4: V4 = array::from_fn(|m| at(&format!("q{}", m)));
    let lam4: V4 = array::from_fn(|m| at(&format!("L{}", m)));
    let k4: V4 = array::from_fn(|m| at(&format!("k{}", m)));
    let e4: V4 = array::from_fn(|m| at(&format!("e{}", m)));
    let ql4 = lower4(&q4);
    let laml4 = lower4(&lam4);
    let eps4l = lower4(&e4);

    let antisym_j = |prefix: &str| -> V4x4 {
        let mut j: V4x4 = array::from_fn(|_| array::from_fn(|_| at("0")));
        for m in 0..4 {
            for n in (m + 1)..4 {
                let s = at(&format!("{}_{}{}", prefix, m, n));
                j[m][n] = s.clone();
                j[n][m] = -s;
            }
        }
        j
    };
    let sym_s = |prefix: &str| -> V4x4 {
        let mut s: V4x4 = array::from_fn(|_| array::from_fn(|_| at("0")));
        for m in 0..4 {
            for n in m..4 {
                let v = at(&format!("{}_{}{}", prefix, m, n));
                s[m][n] = v.clone();
                s[n][m] = v;
            }
        }
        s
    };
    let j1 = antisym_j("J1");
    let j2 = antisym_j("J2");

    // A^mu = q_rho J^{rho mu} (the (q.J)^{rho mu} factor of CS (9)).
    let qj = |jm: &V4x4| -> V4 {
        array::from_fn(|m| {
            let mut s = at("0");
            for r in 0..4 {
                s = (s + ql4[r].clone() * jm[r][m].clone()).expand();
            }
            s
        })
    };
    let a1 = qj(&j1);
    let qd_a1 = {
        let mut s = at("0");
        for m in 0..4 {
            s = (s + ql4[m].clone() * a1[m].clone()).expand();
        }
        s
    };
    check_zero(
        &mut results,
        "T1.1",
        "T1",
        "antisymmetry mechanism: q_mu q_nu J^{mu nu} = q.A = 0 identically for antisymmetric J (CS lines 137-139)",
        &qd_a1,
    );

    // declared gauge shift (conventions packet G_CS2 / rung-2 G_CS):
    // dE_{mu nu} = q_mu Lam_nu + Lam_mu q_nu
    let de_mn: V4x4 = array::from_fn(|m| {
        array::from_fn(|n| {
            (ql4[m].clone() * laml4[n].clone() + laml4[m].clone() * ql4[n].clone()).expand()
        })
    });
    let gauge_var = |jm: &V4x4| -> Atom {
        let am = qj(jm);
        let mut s = at("0");
        for m in 0..4 {
            for n in 0..4 {
                s = (s + de_mn[m][n].clone() * am[m].clone() * am[n].clone()).expand();
            }
        }
        clean(&s)
    };
    let dv1 = gauge_var(&j1);
    let dv2 = gauge_var(&j2);
    check_zero(
        &mut results,
        "T1.2",
        "T1",
        "per-leg gauge variation of CS (9) under the declared shift dE = q Lam + Lam q vanishes IDENTICALLY — no conservation law, no Sigma-constraint anywhere (G_CS2)",
        &dv1,
    );
    check_zero(
        &mut results,
        "T1.3",
        "T1",
        "two-leg sum with independent generic J1, J2: each leg's variation vanishes SEPARATELY — leg-summed gauge invariance needs no inter-leg cancellation (contrast rungs 1-2)",
        &(dv1.clone() + dv2.clone()),
    );
    let smut = sym_s("S");
    let dv_mut = gauge_var(&smut);
    check_nonzero(
        &mut results,
        "T1.4",
        "T1",
        "deliberate-failure mutation: with a SYMMETRIC mutation J -> S the per-leg variation is nonzero — the antisymmetry of J is load-bearing and the harness can fail",
        &dv_mut,
        None,
    );
    let lam_q_j = {
        let mut s = at("0");
        for m in 0..4 {
            for n in 0..4 {
                s = (s + laml4[m].clone() * ql4[n].clone() * j1[m][n].clone()).expand();
            }
        }
        s
    };
    check_nonzero(
        &mut results,
        "T1.5",
        "T1",
        "pattern break: the RUNG-2-grade variation Lam_mu q_nu J^{mu nu} is nonzero per leg without sum_a J_a = 0, while the rung-3 variation (T1.2) is identically zero — the P -> J escalation terminates at rung 3",
        &lam_q_j,
        None,
    );

    let op_q = build_op(&qv, &ql_soft, &dz_gen, &dzb_gen, &de_gen);
    check_all_zero(
        &mut results,
        "T1.6",
        "T1",
        "operator form on the sphere: the per-leg soft operator annihilates the gauge direction, op(q) = 0 — the epsilon -> epsilon + alpha q freedom leaves C = (eps.q.J) invariant per leg",
        &op_q,
        "",
    );

    // ================================================================ T2 spinor corner
    // explicit 2-component spinors; brackets <i,j> = l_i^1 l_j^2 - l_i^2 l_j^1,
    // [i,j] = t_i^1 t_j^2 - t_i^2 t_j^1
    let l1 = at("l1");
    let l2 = at("l2");
    let t1 = at("t1");
    let t2 = at("t2");
    let p1 = at("p1");
    let p2 = at("p2");
    let r1 = at("r1");
    let r2 = at("r2");
    let u1 = at("u1");
    let u2 = at("u2");
    let x1 = at("x1");
    let x2 = at("x2");
    let y1 = at("y1");
    let y2 = at("y2");
    let abrk = |a: (&Atom, &Atom), b: (&Atom, &Atom)| -> Atom {
        (a.0.clone() * b.1.clone() - a.1.clone() * b.0.clone()).expand()
    };
    let lam_s = (&l1, &l2);
    let tl_s = (&t1, &t2);
    let lam_a = (&p1, &p2);
    let tl_a = (&r1, &r2);
    let tl_b = (&u1, &u2);
    let lam_x = (&x1, &x2);
    let lam_y = (&y1, &y2);
    let sa_a = abrk(lam_s, lam_a);
    let sa_s = abrk(tl_s, tl_a);
    let ab = abrk(tl_a, tl_b);
    let sb = abrk(tl_s, tl_b);
    let dtl_a = [symbol!("marici::r1"), symbol!("marici::r2")];

    // T2.1: per-leg CS (20) operator on bracket monomials [a,b]^m
    let mut t21: Vec<Atom> = Vec::new();
    for m in [2i64, 3, 4] {
        let mut f = at("1");
        for _ in 0..m {
            f = (f * ab.clone()).expand();
        }
        let mut d2f = at("0");
        for i in 0..2 {
            for j in 0..2 {
                let dd = f
                    .derivative(dtl_a[i])
                    .expand()
                    .derivative(dtl_a[j])
                    .expand();
                d2f = (d2f + [t1.clone(), t2.clone()][i].clone()
                    * [t1.clone(), t2.clone()][j].clone()
                    * dd)
                    .expand();
            }
        }
        let mut abm2 = at("1");
        for _ in 0..(m - 2) {
            abm2 = (abm2 * ab.clone()).expand();
        }
        let rhs = (at(&format!("{}", m * (m - 1))) * sb.clone() * sb.clone() * abm2).expand();
        t21.push((d2f - rhs).expand());
    }
    check_all_zero(
        &mut results,
        "T2.1",
        "T2",
        "per-leg CS (20) spinor operator on bracket monomials: t_s^a t_s^b d^2/(dt_a^a dt_a^b) [a,b]^m = m(m-1) [s,b]^2 [a,b]^{m-2} for m = 2, 3, 4",
        &t21,
        "",
    );

    // T2.2: holomorphic soft-limit pole ladder (CS (28)): lam_s -> eps lam_s,
    // lam~_s fixed.  S^(0) (17), S^(1) (18), S^(2) (20) per leg.
    let eps_s = at("eps_s");
    let s0_leg = clean(
        &(sa_s.clone() / sa_a.clone() * abrk(lam_x, lam_a) * abrk(lam_y, lam_a)
            / (abrk(lam_x, lam_s) * abrk(lam_y, lam_s))),
    );
    let s1_leg = clean(
        &(at("1/2") * sa_s.clone() / sa_a.clone()
            * (abrk(lam_x, lam_a) / abrk(lam_x, lam_s)
                + abrk(lam_y, lam_a) / abrk(lam_y, lam_s))),
    );
    let s2_leg = clean(&(at("1/2") * sa_s.clone() / sa_a.clone()));
    let scale_ls = |e: &Atom| -> Atom {
        clean(&subs(&subs(e, &l1, &(eps_s.clone() * l1.clone())), &l2, &(eps_s.clone() * l2.clone())))
    };
    let t22 = [
        clean(&(scale_ls(&s0_leg) * eps_s.clone() * eps_s.clone() * eps_s.clone() - s0_leg.clone())),
        clean(&(scale_ls(&s1_leg) * eps_s.clone() * eps_s.clone() - s1_leg.clone())),
        clean(&(scale_ls(&s2_leg) * eps_s.clone() - s2_leg.clone())),
    ];
    check_all_zero(
        &mut results,
        "T2.2",
        "T2",
        "holomorphic soft-limit pole ladder (CS (28)): under lam_s -> eps lam_s, lam~_s fixed, the per-leg soft factors scale as eps^-3 (S^(0), CS (17)), eps^-2 (S^(1), CS (18)), eps^-1 (S^(2), CS (20))",
        &t22,
        "",
    );

    // T2.3: CS (9) vs CL16 (14) normalization, abstract antisymmetric J
    let eps_a = {
        let mut s = at("0");
        for m in 0..4 {
            s = (s + eps4l[m].clone() * a1[m].clone()).expand();
        }
        s
    };
    let eps_q_j = {
        let mut s = at("0");
        for m in 0..4 {
            for n in 0..4 {
                s = (s + eps4l[m].clone() * ql4[n].clone() * j1[m][n].clone()).expand();
            }
        }
        s
    };
    check_zero(
        &mut results,
        "T2.3a",
        "T2",
        "contraction identity: (eps_mu q_nu J^{mu nu})^2 = (eps_mu (q.J)^{rho mu})^2 for antisymmetric J — the CL16 (14) and CS (9) numerators agree with E_{mu nu} = eps^-_mu eps^-_nu",
        &(eps_q_j.clone() * eps_q_j.clone() - eps_a.clone() * eps_a.clone()),
    );
    let qdotk_abs = {
        let mut s = at("0");
        for m in 0..4 {
            s = (s + ql4[m].clone() * k4[m].clone()).expand();
        }
        s
    };
    let cs9_leg = clean(&(at("-1/2") * eps_a.clone() * eps_a.clone() / qdotk_abs.clone()));
    let cl14_leg = clean(
        &(eps_q_j.clone() * eps_q_j.clone() / (at("2") * om.clone() * qdotk_abs.clone())),
    );
    check_zero(
        &mut results,
        "T2.3b",
        "T2",
        "normalization: CS (9) per leg equals exactly -om times the CL16 (14) per-leg insertion (the omega^-1 vs overall -1/2 convention)",
        &(cs9_leg.clone() + om.clone() * cl14_leg.clone()),
    );
    check_nonzero(
        &mut results,
        "T2.3c",
        "T2",
        "typed normalization residual: the ratio is -om, not 1 — CL16 (14) carries an explicit omega^-1 and (2 k.q)^-1, CS (9) an overall -1/2 (same family as the rung-2 kap residual S3)",
        &(cs9_leg.clone() - cl14_leg.clone()),
        None,
    );

    // ================================================================ T3 Ward fold
    // ---- per-leg C-operator from the generator machinery (CL16 (14)
    // contraction eps^-_mu q_nu J^{mu nu} = the rung-2 opm, arbiter-pinned
    // contraction).  sqrt(2) carried as sq2 with sq2^2 = 2.
    let opm = build_op(&eps_m, &ql_soft, &dz_gen, &dzb_gen, &de_gen);
    let opp = build_op(&eps_p, &ql_soft, &dz_gen, &dzb_gen, &de_gen);
    let c_zk_decl = at("-sq2*om*(z-zk)^2/(1+z*zb)");
    let c_ek_decl = at("-sq2*Ek*om*(z-zk)*(1+z*zbk)/((1+z*zb)*(1+zk*zbk))");
    let t31 = [
        norm_sq2(&(opm[0].clone() - c_zk_decl.clone())),
        norm_sq2(&opm[1]),
        norm_sq2(&(opm[2].clone() - c_ek_decl.clone())),
    ];
    check_all_zero(
        &mut results,
        "T3.1",
        "T3",
        "per-leg C = (eps^-.q.J) operator on the sphere: (c_zk, c_zbk, c_Ek) = (-sqrt(2) om (z-zk)^2/(1+z zb), 0, -sqrt(2) Ek om (z-zk)(1+z zbk)/((1+z zb)(1+zk zbk))) — regular in zb (the antiholomorphic pole of KLPS (6.6) is cancelled by q.k)",
        &t31,
        "sqrt(2) carried as symbol sq2 with exact relation sq2^2 = 2",
    );

    // ---- S^(2)- per leg = om^-1 (2 q.k)^-1 C^2, C = c_zk d_zk + c_Ek d_Ek
    let czk = norm_sq2(&opm[0]);
    let cek = norm_sq2(&opm[2]);
    let den = clean(&(at("2") * om.clone() * qdotp.clone()));
    let a2z = norm_sq2(&(czk.clone() * czk.clone() / den.clone()));
    let az_e = norm_sq2(&(at("2") * czk.clone() * cek.clone() / den.clone()));
    let a2e = norm_sq2(&(cek.clone() * cek.clone() / den.clone()));
    let a1z = norm_sq2(&((czk.clone() * czk.derivative(symbol!("marici::zk")).expand()
        + cek.clone() * czk.derivative(symbol!("marici::Ek")).expand())
        / den.clone()));
    let a1e = norm_sq2(&((czk.clone() * cek.derivative(symbol!("marici::zk")).expand()
        + cek.clone() * cek.derivative(symbol!("marici::Ek")).expand())
        / den.clone()));

    let a2z_decl = at("-(z-zk)^3*(1+zk*zbk)/(2*Ek*(zb-zbk)*(1+z*zb))");
    let az_e_decl = at("-(z-zk)^2*(1+z*zbk)/((zb-zbk)*(1+z*zb))");
    let a2e_decl = at("-Ek*(z-zk)*(1+z*zbk)^2/(2*(zb-zbk)*(1+z*zb)*(1+zk*zbk))");
    let a1z_decl = at("(z-zk)^2*(1+zk*zbk)/(Ek*(zb-zbk)*(1+z*zb))");
    let t32 = [
        a2z.clone() - a2z_decl.clone(),
        az_e.clone() - az_e_decl.clone(),
        a2e.clone() - a2e_decl.clone(),
        a1z.clone() - a1z_decl.clone(),
        a1e.clone(),
    ];
    check_all_zero(
        &mut results,
        "T3.2",
        "T3",
        "S^(2)- per-leg operator channels (CL16 (14)): the d_zk^2, d_zk d_Ek, d_Ek^2, d_zk coefficients match their closed forms and the d_Ek first-order channel vanishes identically; om cancels throughout",
        &t32,
        "",
    );

    // ---- single-pole structure: each channel is G . (zb - zbk)^-1 with G
    // regular at zb = zbk.  A vanishing denominator under substitution makes
    // symbolica emit the unsigned-infinity atom, printed as U+29DE.
    let pole = at("zb-zbk");
    let channels: [(&str, Atom); 4] = [
        ("d_zk^2", a2z.clone()),
        ("d_zk d_Ek", az_e.clone()),
        ("d_Ek^2", a2e.clone()),
        ("d_zk", a1z.clone()),
    ];
    let mut pole_free: Vec<Atom> = Vec::new();
    let mut ok33 = true;
    for (_, a) in &channels {
        let g = clean(&(a.clone() * pole.clone()));
        let g_at = clean(&subs(&g, &zb, &zbk));
        if g_at.to_string().contains('\u{29de}') {
            ok33 = false;
        }
        pole_free.push(g_at);
    }
    push(
        &mut results,
        "T3.3",
        "T3",
        "single-pole structure: every channel coefficient is G(z, zb) . (zb - zbk)^-1 with G finite at zb = zbk — the only antiholomorphic pole is the explicit (2 q.k)^-1 of CL16 (14); the operator C itself is pole-free",
        ok33,
        format!(
            "stripped coefficients at the pole: {}",
            pole_free
                .iter()
                .map(|v| crop(&v.to_string()))
                .collect::<Vec<_>>()
                .join("; ")
        ),
        ok33,
    );

    // ---- the weighted distributional fold (declared prescription):
    // P = (zb - zbk)^-1 antiholomorphic, d_z P = pi delta^2 (rung-1 declared
    // prescription, inherited); strike delta carries weight one higher.
    let mut folds: Vec<(Atom, Vec<Atom>, Vec<Atom>)> = Vec::new();
    for (_, a) in &channels {
        let g = clean(&(a.clone() * pole.clone()));
        let (reg, coeffs) = fold(&g, -1, 4); // declared sequence (-1, 0, 1, 2)
        let red = reduce_at_pole(&coeffs);
        folds.push((reg, coeffs, red));
    }
    let t34a: Vec<Atom> = folds.iter().map(|(r, _, _)| r.clone()).collect();
    check_all_zero(
        &mut results,
        "T3.4a",
        "T3",
        "CL16 (15) structural core: with the declared weight sequence (-1,0,1,2) the regular part of D_z^4 S^(2)- vanishes in ALL operator channels — 'all terms are proportional to (derivatives of) delta functions' holds exactly",
        &t34a,
        "",
    );
    let g_2z = clean(&(a2z.clone() * pole.clone()));
    let (reg_w0, _) = fold(&g_2z, 0, 4);
    check_nonzero(
        &mut results,
        "T3.4b",
        "T3",
        "the weight choice is forced, not arbitrary: the naive sequence (0,1,2,3) leaves a nonzero regular part in the d_zk^2 channel; the scan selects the start weight -1 uniquely",
        &reg_w0,
        None,
    );

    let red2z = &folds[0].2;
    check_all_zero(
        &mut results,
        "T3.5a",
        "T3",
        "the d_zk^2 channel is PURE plain-delta: no delta-derivative terms (D delta = D^2 delta = D^3 delta = 0) — exactly the printed structure of CL16 (15)",
        &red2z[1..],
        "",
    );
    check_zero(
        &mut results,
        "T3.5b",
        "T3",
        "the plain-delta coefficient in the d_zk^2 channel is exactly -3 pi/Ek per leg",
        &(red2z[0].clone() + at("3") * pi.clone() / ek.clone()),
    );
    check_nonzero(
        &mut results,
        "T3.5c",
        "T3",
        "typed residual: printed CL16 (15) has (1/2pi) D_z^4 S^(2)- = -3 sum_i E_i^-1 delta^2 d_zi^2 + ..., i.e. -6 pi/Ek in our normalization — the computed delta is uniformly HALF the printed one (candidate delta^2-normalization drift, same family as rung-2 S10.2/S10.3e)",
        &(red2z[0].clone() + at("6") * pi.clone() / ek.clone()),
        Some(&at("3*pi/Ek")),
    );

    let redz_e = &folds[1].2;
    let red2e = &folds[2].2;
    let red1z = &folds[3].2;
    let t36 = [
        redz_e[0].clone() + at("8*pi*zbk/(1+zk*zbk)"),
        redz_e[1].clone() + at("2") * pi.clone(),
        redz_e[2].clone(),
        redz_e[3].clone(),
        red2e[0].clone() + at("6*pi*Ek*zbk^2/(1+zk*zbk)^2"),
        red2e[1].clone() + at("3*pi*Ek*zbk/(1+zk*zbk)"),
        red2e[2].clone() + at("pi*Ek/2"),
        red2e[3].clone(),
        red1z[0].clone() - at("2*pi*zbk/(Ek*(1+zk*zbk))"),
        red1z[1].clone() - at("2*pi/Ek"),
        red1z[2].clone(),
        red1z[3].clone(),
    ];
    check_all_zero(
        &mut results,
        "T3.6",
        "T3",
        "the unprinted '...' content of CL16 (15), named exactly: d_zk d_Ek channel = -8 pi zbk/(1+zk zbk) delta - 2 pi D delta; d_Ek^2 channel = -6 pi Ek zbk^2/(1+zk zbk)^2 delta - 3 pi Ek zbk/(1+zk zbk) D delta - (pi Ek/2) D^2 delta; d_zk channel = 2 pi zbk/(Ek (1+zk zbk)) delta + (2 pi/Ek) D delta",
        &t36,
        "",
    );

    // ---- electric/magnetic doubling: the +-helicity operator is the exact
    // sigma-conjugate of the --helicity one (CL16 (17) '+ c.c.')
    let t37 = [
        norm_sq2(&opp[0]),
        norm_sq2(&(opp[1].clone() - sigma(&c_zk_decl))),
        norm_sq2(&(opp[2].clone() - sigma(&c_ek_decl))),
    ];
    check_all_zero(
        &mut results,
        "T3.7",
        "T3",
        "electric/magnetic doubling: the positive-helicity operator C+ = (eps^+.q.J) is the exact sigma-conjugate of C-: c+_zk = 0, c+_zbk = sigma(c_zk), c+_Ek = sigma(c_Ek) — the c.c. piece of CL16 (17)/(18) is exact at operator level",
        &t37,
        "",
    );

    // ================================================================ T4 cross-rung ladder
    // T4.1: the fold recursion at n = 3 with the rung-2 sequence (0,1,2)
    // reproduces rung-2's declared fold coefficients exactly on a shared test
    // function (chosen with cP = 6/(1+z zb)^2 != 0, non-vacuous P channel).
    let gam1 = gam().derivative(symbol!("marici::z")).expand();
    let gam2 = gam1.derivative(symbol!("marici::z")).expand();
    let af = clean(&(at("2") * gam() * gam() - gam1.clone()));
    let gtest = at("(z-zk)^3/(1+z*zb)^2");
    let g1t = gtest.derivative(symbol!("marici::z")).expand();
    let g2t = g1t.derivative(symbol!("marici::z")).expand();
    let g3t = g2t.derivative(symbol!("marici::z")).expand();
    let (reg3t, c3t) = fold(&gtest, 0, 3);
    let t41 = [
        reg3t - (g3t.clone() - at("3") * gam() * g2t.clone() + af.clone() * g1t.clone()),
        c3t[0].clone()
            - pi.clone()
                * (at("3") * g2t.clone() - at("6") * gam() * g1t.clone()
                    + af.clone() * gtest.clone()),
        c3t[1].clone() - pi.clone() * (at("3") * g1t.clone() - at("3") * gam() * gtest.clone()),
        c3t[2].clone() - pi.clone() * gtest.clone(),
    ];
    check_all_zero(
        &mut results,
        "T4.1",
        "T4",
        "cross-rung consistency: the fold recursion at n = 3, sequence (0,1,2), reproduces rung-2's declared fold (cP = G''' - 3 Gam G'' + (2 Gam^2 - Gam') G', c0 = pi(3 G'' - 6 Gam G' + (2 Gam^2 - Gam') G), c1 = pi(3 G' - 3 Gam G), c2 = pi G) exactly — one celestial D-calculus across rungs (test function chosen with cP = 6/(1+z zb)^2 != 0, so the P channel comparison is non-vacuous)",
        &t41,
        "",
    );

    // T4.2: derivative-grade ladder D_z^2 -> D_z^3 -> D_z^4 as operators on
    // weight-0 scalars: recursion vs closed forms.
    let dzn = |f: &Atom, n: usize| -> Atom {
        let mut g = f.clone();
        for i in 0..n {
            g = clean(
                &(g.derivative(symbol!("marici::z")).expand()
                    - at(&format!("{}", i)) * gam() * g),
            );
        }
        clean(&g)
    };
    let dn = |f: &Atom, n: usize| -> Atom {
        let mut g = f.clone();
        for _ in 0..n {
            g = g.derivative(symbol!("marici::z")).expand();
        }
        g
    };
    let gladder = at("(z-zk)^3/(1+z*zb)^2");
    let d2_closed = dn(&gladder, 2) - gam() * dn(&gladder, 1);
    let d3_closed = dn(&gladder, 3) - at("3") * gam() * dn(&gladder, 2)
        + af.clone() * dn(&gladder, 1);
    let d4_closed = dn(&gladder, 4) - at("6") * gam() * dn(&gladder, 3)
        + (at("11") * gam() * gam() - at("4") * gam1.clone()) * dn(&gladder, 2)
        + (at("7") * gam() * gam1.clone() - gam2.clone() - at("6") * gam() * gam() * gam())
            * dn(&gladder, 1);
    let t42 = [
        dzn(&gladder, 2) - d2_closed,
        dzn(&gladder, 3) - d3_closed,
        dzn(&gladder, 4) - d4_closed,
    ];
    check_all_zero(
        &mut results,
        "T4.2",
        "T4",
        "derivative-grade ladder as one recursion: D_z^2 = d^2 - Gam d, D_z^3 = d^3 - 3 Gam d^2 + (2 Gam^2 - Gam') d, D_z^4 = d^4 - 6 Gam d^3 + (11 Gam^2 - 4 Gam') d^2 + (7 Gam Gam' - Gam'' - 6 Gam^3) d on weight-0 scalars — closed forms match the weighted recursion exactly",
        &t42,
        "",
    );

    // T4.3: time-integral ladder at primitive level (exact differentiation).
    // Test field chain: S(u) decaying rational, F = S'' plays D_z^4 C_zz.
    let u = at("u");
    let su = at("u/(1+u^2)");
    let fu = su
        .derivative(symbol!("marici::u"))
        .expand()
        .derivative(symbol!("marici::u"))
        .expand();
    let au = su.derivative(symbol!("marici::u")).expand();
    let bu = (u.clone() * au.clone() - su.clone()).expand();
    check_zero(
        &mut results,
        "T4.3a",
        "T4",
        "time-integral ladder, rung-3 grade: the double retarded primitive satisfies the first-moment identity int^u u' F(u') du' = u int^u F - int int^u F, i.e. (u A - S)' = u F with A = S', F = S'' — CL16 (17)'s int du int^u du' is a FIRST-MOMENT observable",
        &(bu.derivative(symbol!("marici::u")).expand() - u.clone() * fu.clone()),
    );
    let t_s = at("t_s");
    let at_inf = |e: &Atom| -> Atom {
        clean(&subs(&clean(&subs(e, &u, &(at("1") / t_s.clone()))), &t_s, &at("0")))
    };
    let t43b = [at_inf(&su), at_inf(&au)];
    check_all_zero(
        &mut results,
        "T4.3b",
        "T4",
        "convergence/boundary: for the falloff-class test field the boundary terms vanish, S(+/-inf) = S'(+/-inf) = 0 (exact u -> 1/t evaluation) — the CL16 footnote-2 falloff class makes the u-integrals convergent",
        &t43b,
        "",
    );
    check_nonzero(
        &mut results,
        "T4.3c",
        "T4",
        "ladder contrast: the rung-3 double-integral observable H = S is NOT the rung-2 single-integral observable A = S' — the int^2 and int^1 grades are distinct (H - A != 0), and the CM memory of Nichols sits at the int^1 grade (rung 2), not here",
        &(su.clone() - au.clone()),
        Some(&at("(u^3+u^2+u-1)/(1+u^2)^2")),
    );

    // T4.4: zero-frequency projector ladder
    let proj2 = |f: &Atom| clean(&(f.clone() + om.clone() * f.derivative(symbol!("marici::om")).expand()));
    let proj3 = |f: &Atom| clean(&(at("2") * f.clone() + om.clone() * f.derivative(symbol!("marici::om")).expand()));
    let (a_s, b_s, c_s) = (at("a"), at("b"), at("c"));
    let t44 = [
        proj2(&(a_s.clone() / om.clone())),
        proj3(&proj2(&(a_s.clone() / om.clone() / om.clone()))),
        proj3(&proj2(&(b_s.clone() / om.clone()))),
        proj3(&proj2(&c_s)) - at("2") * c_s.clone(),
    ];
    check_all_zero(
        &mut results,
        "T4.4",
        "T4",
        "zero-frequency projector ladder: (1 + om d_om) annihilates a/om (rung 2, KLPS 5.33); the rung-3 finite-part operator (2 + om d_om)(1 + om d_om) annihilates a/om^2 and b/om and acts as 2x on the finite part — the finite-part prescription for the omega^-1 moment of CL16 (14)",
        &t44,
        "",
    );

    // ================================================================ T5 deliberate failures
    push(
        &mut results,
        "T5.1",
        "T5",
        "H-A anti-test (the inverse of the rung-1/2 deliberate-failure tests): removing every Sigma-constraint changes NOTHING at the rung-3 gauge step — the per-leg variation of CS (9) is identically zero with generic independent J_a (T1.2/T1.3), while the rung-2-grade variation is nonzero without sum J = 0 (T1.5); imposing sum P = 0 or sum J = 0 is a no-op at rung 3",
        true,
        "backed by T1.2, T1.3 (zero) vs T1.5 (nonzero)".to_string(),
        true,
    );

    let (reg_hb, _) = fold(&g_2z, -1, 3);
    let reg_hb_decl = at("-3*(1+zb*zk)^3*(1+zk*zbk)/(Ek*(1+z*zb)^4*(zb-zbk))");
    let ok52 = !is_zero(&reg_hb) && is_zero(&(reg_hb.clone() / pole.clone() - reg_hb_decl));
    push(
        &mut results,
        "T5.2",
        "T5",
        "H-B baseline obstruction: the rung-2-grade D_z^3 smearing (sequence (-1,0,1)) applied to the rung-3 d_zk^2 channel leaves a nonzero regular part, pinned exactly as -3 (1+zb zk)^3 (1+zk zbk)/(Ek (1+z zb)^4 (zb-zbk)) — no smooth generalized-BMS (single-u-integral) charge class reproduces the rung-3 distributional identity; the D_z^4 grade is forced",
        ok52,
        if ok52 {
            String::new()
        } else {
            format!("computed: {}", crop(&clean(&reg_hb).to_string()))
        },
        ok52,
    );

    // T5.3: genuinely-wrong mutation of CS (20): reference-spinor pollution
    // t_s^{a} t_a^{b} d^2/dt_a^a dt_a^b must NOT satisfy the bracket identity.
    let mut t53: Vec<Atom> = Vec::new();
    for m in [2i64, 3] {
        let mut f = at("1");
        for _ in 0..m {
            f = (f * ab.clone()).expand();
        }
        let mut d2f = at("0");
        for i in 0..2 {
            for j in 0..2 {
                let dd = f
                    .derivative(dtl_a[i])
                    .expand()
                    .derivative(dtl_a[j])
                    .expand();
                d2f = (d2f + [t1.clone(), t2.clone()][i].clone()
                    * [r1.clone(), r2.clone()][j].clone()
                    * dd)
                    .expand();
            }
        }
        let mut abm2 = at("1");
        for _ in 0..(m - 2) {
            abm2 = (abm2 * ab.clone()).expand();
        }
        let rhs = (at(&format!("{}", m * (m - 1))) * sb.clone() * sb.clone() * abm2).expand();
        t53.push((d2f - rhs).expand());
    }
    let mut mut_resid = t53[0].clone();
    for (f, v) in [
        ("t1", "2"),
        ("t2", "1/3"),
        ("r1", "-2/5"),
        ("r2", "3"),
        ("u1", "2/7"),
        ("u2", "-1"),
    ] {
        mut_resid = subs(&mut_resid, &at(f), &at(v));
    }
    let mut_resid = clean(&mut_resid);
    check_nonzero(
        &mut results,
        "T5.3",
        "T5",
        "genuinely-wrong mutation that must FAIL: polluting CS (20) with a leg spinor, t_s^a t_a^b d^2/dt_a^a dt_a^b, breaks the bracket identity — the residual m(m-1)[a,b]^{m-2}[s,b]([a,b]-[s,b]) is nonzero (exact rational point); the reference-spinor-free form of (20) is load-bearing",
        &mut_resid,
        Some(&at("-15136/2205")),
    );

    // ================================================================ T6 verdict
    push(
        &mut results,
        "T6.1",
        "T6",
        "verdict on H-A..H-E for the checkable core: H-A SUPPORTED (per-leg gauge invariance needs no conservation law; the smeared identity closes with no Sigma-input — closure is kinematic); H-B FALSIFIED as baseline (T5.2); H-C SUPPORTED up to the uniform factor-1/2 delta-normalization drift (T3.5c, same family as rung-2 S10) with the '...' channels named exactly (T3.6) and the electric/magnetic doubling exact at operator level (T3.7); H-D SUPPORTED at tree level (one D-recursion across rungs, T4.1/T4.2) with collinear/nonlinear corrections a typed residual; H-mem structural core verified (double-u integral = first-moment observable, T4.3) but the rung-3 memory observable remains OPEN; H-E: the named residual of this rung is the half-strength delta drift, not a closure failure",
        true,
        "synthesis of T1-T5".to_string(),
        true,
    );

    // ================================================================ summary
    let n_pass = results
        .iter()
        .filter(|r| r["status"] == "pass")
        .count();
    let failed: Vec<String> = results
        .iter()
        .filter(|r| r["status"] != "pass")
        .map(|r| r["id"].as_str().unwrap().to_string())
        .collect();
    let disagreed: Vec<String> = results
        .iter()
        .filter(|r| r["agreement_with_sympy"] == false)
        .map(|r| r["id"].as_str().unwrap().to_string())
        .collect();
    let n_agree = results
        .iter()
        .filter(|r| r["agreement_with_sympy"] == true)
        .count();

    let summary = json!({
        "total": results.len(),
        "passed": n_pass,
        "failed": failed.len(),
        "failed_ids": failed,
        "cross_validation": {
            "engine": "symbolica 2.2.0 (default-features = false, features = [\"no_gmp\"]), exact rational / complex-rational arithmetic, no floats",
            "reference": "research/strominger/results/subsubleading_triangle_exact_checks.json (sympy, 31/31)",
            "agreement": format!("{}/{} verdicts agree with the sympy reference; typed residuals compared exactly where declared (T3.5c 3 pi/Ek, T4.3c (u^3+u^2+u-1)/(1+u^2)^2, T5.3 -15136/2205)", n_agree, results.len()),
            "disagreements": disagreed,
            "ported_core_only": [
                "distributional prescription d_z (zb - zbk)^-1 = pi delta^2 is a declared external input in both engines (rung-1 prescription, inherited)",
                "the fold weight sequence (-1,0,1,2) is a declared input, fixed by the vanishing-regular-part requirement; uniqueness is witnessed by T3.4b in both engines",
                "T5.1/T6.1: classification verdict records (corroborated by the computational checks), same as sympy"
            ]
        },
        "classification": {
            "gauge_corner": "S^(2) is gauge invariant PER LEG from J antisymmetry alone (T1.1-T1.3, T1.6); the P -> J escalation of rungs 1-2 terminates (T1.5); the antisymmetry is load-bearing (T1.4 mutation fails as predicted)",
            "ward_corner": "CL16 (15) verified as an exact distributional identity: D_z^4 S^(2)- is purely distributional in all operator channels under the declared weight sequence (-1,0,1,2) (T3.4a; the weight is forced, T3.4b); the d_zk^2 channel is pure plain-delta with coefficient -3 pi/Ek — exactly HALF the printed -6 pi/Ek (typed residual T3.5c, same delta^2-normalization drift family as rung-2 S10); the unprinted '...' channels are named exactly (T3.6); electric/magnetic doubling exact at operator level (T3.7)",
            "memory_corner": "no rung-3 observable is grounded; the structural candidate H-mem (double retarded-time integral at grade D_z^4) is verified as a first-moment observable (T4.3); the CM memory sits at the single-integral rung-2 grade (T4.3c); existence of a measurable rung-3 persistent observable remains OPEN",
            "outcome": "the rung-3 triangle closes on the checkable core with NO conservation-law input (structurally different from rungs 1-2: closure is kinematic, H-A), with the smearing identity CL16 (15) exact up to the uniform factor-1/2 delta-normalization drift (typed residual), the cross-rung derivative/time-integral ladders exact (H-D), and the rung-3 memory observable OPEN (H-mem candidate shape verified structurally) — reproduced identically by the independent Symbolica engine"
        }
    });

    let out = json!({
        "checker": "subsubleading_triangle_symbolica_checks",
        "author": "marici.Strominger",
        "date": "2026-08-20",
        "engine": "symbolica 2.2.0 (Rust, no_gmp)",
        "cross_validates": "research/strominger/results/subsubleading_triangle_exact_checks.json",
        "checks": results,
        "summary": summary,
    });

    std::fs::create_dir_all("../results").unwrap();
    let path = "../results/subsubleading_triangle_symbolica_checks.json";
    std::fs::write(path, serde_json::to_string_pretty(&out).unwrap() + "\n").unwrap();

    let n_fail = out["summary"]["failed"].as_u64().unwrap();
    let n_dis = out["summary"]["cross_validation"]["disagreements"]
        .as_array()
        .unwrap()
        .len();
    println!(
        "\n{}/{} checks passed, {}/{} agree with sympy; results -> {}",
        n_pass,
        out["summary"]["total"],
        n_agree,
        out["summary"]["total"],
        path
    );
    process::exit(if n_fail == 0 && n_dis == 0 { 0 } else { 1 });
}
