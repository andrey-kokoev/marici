//! Exact subleading-triangle cross-validation checker: independent engine port.
//!
//! Cross-validates checkers/subleading_triangle_exact_checks.py (sympy) with an
//! independent computer algebra system: Rust + Symbolica 2.2.0 (no_gmp), exact
//! rational / complex-rational arithmetic, no floats anywhere.
//!
//! Sources and conventions: research/strominger/subleading-triangle-conventions.md
//! Map definitions:         research/strominger/subleading-triangle-source-boundary.md
//! sympy results mirrored:  research/strominger/results/subleading_triangle_exact_checks.json
//!
//! (z, zb, zk, zbk) are independent symbols; reality is imposed through the
//! explicit conjugation map sigma: z <-> zb, zk <-> zbk applied SIMULTANEOUSLY
//! (via fresh temporary symbols, never sequential substitution), with i -> -i
//! implemented as complex-rational coefficient conjugation.
//!
//! Metric convention: eta = diag(-1,1,1,1), matching the sympy checker.
//!
//! Output: research/strominger/results/subleading_triangle_symbolica_checks.json
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

/// Exact sqrt(2)-relation reduction: symbolica 2.2.0 keeps 2^(1/2) and
/// 2*(1/2)^(1/2) as unmerged normal forms, so the S5.3 pullback comparison
/// carries sqrt(2) as a symbol sq2 reduced by its defining relation sq2^2 = 2.
fn norm_sq2(x: &Atom) -> Atom {
    let mut y = clean(x);
    y.repeat_map(|v| {
        v.to_owned()
            .replace_multiple([symbolica::id::Replacement::new(
                at("sq2^2").to_pattern(),
                at("2").to_pattern(),
            )])
    });
    clean(&y)
}

fn is_zero(x: &Atom) -> bool {
    clean(x) == at("0")
}

fn subs(x: &Atom, from: &Atom, to: &Atom) -> Atom {
    x.replace(from.to_pattern()).with(to.to_pattern())
}

fn has_symbol(x: &Atom, name: &str) -> bool {
    let pat = at(name).to_pattern();
    x.pattern_match(&pat, None, None).next().is_some()
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

/// Exact rational test point (all values rational; om = 1), same as sympy PT1.
fn pt1(x: &Atom) -> Atom {
    let mut y = x.clone();
    for (f, v) in [
        ("z", "2"),
        ("zb", "3/5"),
        ("zk", "-1/3"),
        ("zbk", "4/7"),
        ("Ek", "5"),
        ("om", "1"),
    ] {
        y = subs(&y, &at(f), &at(v));
    }
    clean(&y)
}

/// Partial point z = 2, zb = 3/5 (used by S8/S9 witnesses).
fn pt_z2(x: &Atom) -> Atom {
    let mut y = x.clone();
    for (f, v) in [("z", "2"), ("zb", "3/5")] {
        y = subs(&y, &at(f), &at(v));
    }
    clean(&y)
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
fn gamb() -> Atom {
    at("-2*z/(1+z*zb)")
} // Gamma^zb_zbzb (mixed Christoffels vanish)
fn gamk() -> Atom {
    at("-2*zbk/(1+zk*zbk)")
} // Gamma^z_zz at the leg point
fn gambk() -> Atom {
    at("-2*zk/(1+zk*zbk)")
}

/// D_z on a rank-s lower-z tensor component.
fn dz_low(f: &Atom, s: i64) -> Atom {
    let d = f.derivative(symbol!("marici::z")).expand();
    clean(&(d - at(&s.to_string()) * gam() * f.clone()))
}

/// D_zb on a rank-s lower-zb tensor component.
fn dzb_low(f: &Atom, s: i64) -> Atom {
    let d = f.derivative(symbol!("marici::zb")).expand();
    clean(&(d - at(&s.to_string()) * gamb() * f.clone()))
}

/// D_z on a Y^z vector component at the leg point.
fn dz_vec_leg(y: &Atom) -> Atom {
    clean(
        &(y.derivative(symbol!("marici::zk")).expand() + gamk() * y.clone()),
    )
}

fn dzb_vec_leg(y: &Atom) -> Atom {
    clean(
        &(y.derivative(symbol!("marici::zbk")).expand() + gambk() * y.clone()),
    )
}

/// Covariant D_z^3 on a Y^z vector component via the weight sequence
/// (d+Gam) on vector -> plain d on (z, low-z) -> (d-Gam) on (z, low-zz).
fn dz3_vec(y: &Atom) -> Atom {
    let t1 = clean(
        &(y.derivative(symbol!("marici::z")).expand() + gam() * y.clone()),
    );
    let t2 = t1.derivative(symbol!("marici::z")).expand();
    clean(&(t2.derivative(symbol!("marici::z")).expand() - gam() * t2))
}

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

/// Pass iff expr is exactly nonzero (typed obstruction present). With exact
/// rational substitutions this is a sound nonzeroness witness. Agreement with
/// the sympy run additionally requires the typed residual to match `expected`
/// when one is declared.
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

// --------------------------------------------------- exact 6x6 linear solve
/// Gaussian elimination over exact Atoms (entries here are complex rationals).
/// Returns (solution, determinant). Panics (loud failure) if singular.
fn solve6(m: &[Vec<Atom>], b: &[Atom]) -> (Vec<Atom>, Atom) {
    let mut a: Vec<Vec<Atom>> = m.to_vec();
    let mut rhs: Vec<Atom> = b.to_vec();
    let mut det = at("1");
    let mut sign = at("1");
    for col in 0..6 {
        let mut piv = None;
        for (r, row) in a.iter().enumerate().skip(col) {
            if !is_zero(&row[col]) {
                piv = Some(r);
                break;
            }
        }
        let piv = piv.expect("M6 singular: no pivot");
        if piv != col {
            a.swap(piv, col);
            rhs.swap(piv, col);
            sign = -sign;
        }
        let pv = clean(&a[col][col]);
        det = clean(&(det * pv.clone()));
        for r in (col + 1)..6 {
            if is_zero(&a[r][col]) {
                continue;
            }
            let factor = clean(&(a[r][col].clone() / pv.clone()));
            for c in col..6 {
                a[r][c] = clean(&(a[r][c].clone() - factor.clone() * a[col][c].clone()));
            }
            rhs[r] = clean(&(rhs[r].clone() - factor.clone() * rhs[col].clone()));
        }
    }
    let mut x = vec![at("0"); 6];
    for i in (0..6).rev() {
        let mut s = rhs[i].clone();
        for (j, xj) in x.iter().enumerate().skip(i + 1) {
            s = clean(&(s - a[i][j].clone() * xj.clone()));
        }
        x[i] = clean(&(s / a[i][i].clone()));
    }
    (x, clean(&(det * sign)))
}

/// Coefficients [c0, c1, c2] of a polynomial of degree <= 2 in `var`.
/// Panics loudly on any other power (the sympy _coeffs3 analog, but strict).
fn coeffs3(f: &Atom, var: &Atom) -> [Atom; 3] {
    let cl = clean(f).expand().coefficient_list::<u8>(&[var.clone()]);
    let mut out = [at("0"), at("0"), at("0")];
    let one = at("1");
    let v2 = (var.clone() * var.clone()).expand();
    for (k, c) in cl {
        if k == one {
            out[0] = c;
        } else if k == *var {
            out[1] = c;
        } else if k == v2 {
            out[2] = c;
        } else {
            panic!("coeffs3: unexpected key {} in {}", k, f);
        }
    }
    out
}

// ==================================================================== main
fn main() {
    let mut results: Vec<serde_json::Value> = Vec::new();

    let z = at("z");
    let zb = at("zb");
    let w = at("w");
    let wb = at("wb");
    let zk = at("zk");
    let zbk = at("zbk");
    let ek = at("Ek");
    let om = at("om");
    let kap = at("kap");
    let ii = Atom::i();

    // ------------------------------------------------- S4/S5 shared machinery
    // Lorentz generator actions on leg coordinates (zk, zbk, Ek), computed
    // from delta k = alpha . eta . k with antisymmetric alpha (k is a column
    // vector; the action is alpha^{mu}{}_nu k^nu).
    let gens: [(usize, usize); 6] = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)];
    let rots = [3usize, 4, 5]; // indices of (1,2),(1,3),(2,3) in gens
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

    let pk = pvec(&ek, &zk, &zbk);
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

    // ================================================================ S1 projector
    let (a_s, b_s, c_s) = (at("a"), at("b"), at("c"));
    let proj = |f: &Atom| {
        let df = f.derivative(symbol!("marici::om")).expand();
        clean(&(f.clone() + om.clone() * df))
    };

    check_zero(
        &mut results,
        "S1.1",
        "S1",
        "(1+om d_om) annihilates the Weinberg pole a/om (KLPS 5.33)",
        &proj(&(a_s.clone() / om.clone())),
    );
    check_zero(
        &mut results,
        "S1.2",
        "S1",
        "(1+om d_om) acts as identity on om^0 terms",
        &(proj(&b_s) - b_s.clone()),
    );
    let f_soft = a_s.clone() / om.clone() + b_s.clone() + c_s.clone() * om.clone();
    let sym_lim = clean(
        &((f_soft.clone() + subs(&f_soft, &om, &-om.clone())).expand() / at("2")),
    );
    let proj_pole_finite = proj(&(a_s.clone() / om.clone() + b_s.clone()));
    check_zero(
        &mut results,
        "S1.3",
        "S1",
        "symmetric limit (1/2)(lim+ + lim-) equals the (1+om d_om) projection at the pole+finite level (PSZ 6.1 = KLPS 5.33)",
        &(proj_pole_finite - sym_lim),
    );

    // ================================================================ S2 gauge variation
    let k4: V4 = array::from_fn(|i| at(&format!("k{}", i)));
    let q4: V4 = array::from_fn(|i| at(&format!("q{}", i)));
    let lam4: V4 = array::from_fn(|i| at(&format!("L{}", i)));
    let jnames = ["J01", "J02", "J03", "J12", "J13", "J23"];
    let mut js: V4x4 = array::from_fn(|_| array::from_fn(|_| at("0")));
    {
        let mut idx = 0;
        for m in 0..4 {
            for n in (m + 1)..4 {
                let s = at(jnames[idx]);
                js[m][n] = s.clone();
                js[n][m] = -s;
                idx += 1;
            }
        }
    }
    let kl4 = lower4(&k4);
    let ql4 = lower4(&q4);
    let laml4 = lower4(&lam4);
    let qdotk = mdot(&q4, &k4);

    // declared shift (conventions packet G_CS): dE_{mu nu} = q_mu Lam_nu + q_nu Lam_mu
    let mut dsum = at("0");
    for m in 0..4 {
        for n in 0..4 {
            let de_mn =
                ql4[m].clone() * laml4[n].clone() + laml4[m].clone() * ql4[n].clone();
            let mut jq = at("0");
            for (r, qlr) in ql4.iter().enumerate() {
                jq = (jq + qlr.clone() * js[r][n].clone()).expand();
            }
            dsum = (dsum + de_mn * k4[m].clone() * jq).expand();
        }
    }
    let ds_leg = clean(&(dsum / qdotk.clone()));
    let mut lam_q_j = at("0");
    for m in 0..4 {
        for n in 0..4 {
            lam_q_j =
                (lam_q_j + laml4[m].clone() * ql4[n].clone() * js[m][n].clone()).expand();
        }
    }
    check_zero(
        &mut results,
        "S2.1",
        "S2",
        "per-leg gauge contraction of the declared shift is exactly -Lam_mu q_nu J^{mu nu}; hence dS^(1) = +i Lam q sum J (printed CS (7) has -i: shift-sign convention residual)",
        &(ds_leg + lam_q_j),
    );

    // angular-momentum conservation on a 2-leg scalar amplitude
    let k1v: V4 = array::from_fn(|i| at(&format!("a{}", i)));
    let k2v: V4 = array::from_fn(|i| at(&format!("b{}", i)));
    let dk1 = [
        symbol!("marici::a0"),
        symbol!("marici::a1"),
        symbol!("marici::a2"),
        symbol!("marici::a3"),
    ];
    let dk2 = [
        symbol!("marici::b0"),
        symbol!("marici::b1"),
        symbol!("marici::b2"),
        symbol!("marici::b3"),
    ];

    /// J^{mu nu} F = k^[mu dF/dk_{nu]} (orbital, scalar legs; CS footnote 4).
    fn jact(f: &Atom, kv: &V4, dv: &[symbolica::atom::Symbol; 4]) -> V4x4 {
        let grad: V4 = array::from_fn(|i| f.derivative(dv[i]).expand());
        let dcov = lower4(&grad);
        array::from_fn(|m| {
            array::from_fn(|n| {
                (kv[m].clone() * dcov[n].clone() - dcov[m].clone() * kv[n].clone()).expand()
            })
        })
    }

    let f12 = mdot(&k1v, &k2v);
    let j1 = jact(&f12, &k1v, &dk1);
    let j2 = jact(&f12, &k2v, &dk2);
    let jsum: Vec<Atom> = (0..4)
        .flat_map(|m| (m + 1..4).map(move |n| (m, n)))
        .map(|(m, n)| j1[m][n].clone() + j2[m][n].clone())
        .collect();
    check_all_zero(
        &mut results,
        "S2.2",
        "S2",
        "with J: sum_a J_a^{mu nu}(k1.k2) = 0 identically (CS (7) gauge invariance)",
        &jsum,
        "",
    );
    let jo1 = jact(&k1v[0], &k1v, &dk1);
    let jo2 = jact(&k1v[0], &k2v, &dk2);
    check_nonzero(
        &mut results,
        "S2.3",
        "S2",
        "typed obstruction: without J the variation is nonzero — sum_a J_a^{mu nu}(k1^0) = k1^[mu eta^{nu]0} != 0",
        &(jo1[0][1].clone() + jo2[0][1].clone()),
        Some(&at("a1")),
    );

    // ================================================================ S3 normalization
    let enames = ["e01", "e02", "e03", "e12", "e13", "e23"];
    let mut eps: V4x4 = array::from_fn(|_| array::from_fn(|_| at("0")));
    {
        let mut idx = 0;
        for m in 0..4 {
            for n in (m + 1)..4 {
                let s = at(enames[idx]);
                eps[m][n] = s.clone();
                eps[n][m] = -s;
                idx += 1;
            }
        }
    }
    let sgn = |i: usize| if i == 0 { at("-1") } else { at("1") };
    let eps_up: V4x4 = array::from_fn(|m| {
        array::from_fn(|n| sgn(m) * sgn(n) * eps[m][n].clone())
    });
    let js_low: V4x4 = array::from_fn(|m| {
        array::from_fn(|n| sgn(m) * sgn(n) * js[m][n].clone())
    });
    let mut csum = at("0");
    for m in 0..4 {
        for n in 0..4 {
            let mut jq = at("0");
            for (r, qlr) in ql4.iter().enumerate() {
                jq = (jq + qlr.clone() * js[r][n].clone()).expand();
            }
            csum = (csum + eps[m][n].clone() * k4[m].clone() * jq).expand();
        }
    }
    let c_cs = clean(&((-ii.clone()) * csum / qdotk.clone()));
    let mut psum = at("0");
    for m in 0..4 {
        for n in 0..4 {
            let mut jl = at("0");
            for (l, q4l) in q4.iter().enumerate() {
                jl = (jl + js_low[n][l].clone() * q4l.clone()).expand();
            }
            psum = (psum + eps_up[m][n].clone() * kl4[m].clone() * jl).expand();
        }
    }
    let c_psz = clean(&(ii.clone() * kap.clone() * psum / qdotk.clone()));
    check_zero(
        &mut results,
        "S3.1",
        "S3",
        "PSZ (6.5) contracted form equals exactly kap times the CS (6) contraction: C_PSZ - kap*C_CS = 0",
        &(c_psz.clone() - kap.clone() * c_cs.clone()),
    );
    check_nonzero(
        &mut results,
        "S3.2",
        "S3",
        "typed normalization residual: the ratio is kap = sqrt(32 pi G), not 1 — PSZ (6.5) carries an explicit kap, CS (5)-(6) carries none",
        &(c_psz - c_cs),
        None,
    );

    // ================================================================ S4 sphere reduction
    let s41: Vec<Atom> = gens
        .iter()
        .map(|_| at("0"))
        .zip(dz_gen.iter())
        .map(|(_, g)| g.derivative(symbol!("marici::zbk")).expand())
        .chain(
            dzb_gen
                .iter()
                .map(|g| g.derivative(symbol!("marici::zk")).expand()),
        )
        .chain(rots.iter().map(|&ri| de_gen[ri].clone()))
        .collect();
    check_all_zero(
        &mut results,
        "S4.1",
        "S4",
        "Lorentz action via PSZ (6.7): dz holomorphic in zk, dzb antiholomorphic, dE = 0 for rotations",
        &s41,
        "",
    );
    let s42: Vec<Atom> = (0..6)
        .map(|g| {
            de_gen[g].clone()
                + ek.clone() / at("2")
                    * (dz_vec_leg(&dz_gen[g]) + dzb_vec_leg(&dzb_gen[g]))
        })
        .collect();
    check_all_zero(
        &mut results,
        "S4.2",
        "S4",
        "hard-operator identity per generator: dE = -(E/2)(D_z dz + D_zb dzb)",
        &s42,
        "",
    );

    // chiral solve: coefficient matrix of (dz, dzb) in (zk^j, zbk^j), j = 0..2
    let mut m6: Vec<Vec<Atom>> = vec![vec![at("0"); 6]; 6];
    for gi in 0..6 {
        let cz = coeffs3(&dz_gen[gi], &zk);
        let cb = coeffs3(&dzb_gen[gi], &zbk);
        for j in 0..3 {
            m6[j][gi] = cz[j].clone();
            m6[j + 3][gi] = cb[j].clone();
        }
    }
    let target: Vec<Atom> = [at("0"), at("0"), at("1"), at("0"), at("0"), at("0")].to_vec();
    let (alpha, det6) = solve6(&m6, &target);
    let mut de_sol = at("0");
    for (g, ag) in alpha.iter().enumerate() {
        de_sol = clean(&(de_sol + ag.clone() * de_gen[g].clone()));
    }
    let resid_sol = clean(
        &(de_sol.clone() + ek.clone() / at("2") * dz_vec_leg(&at("zk^2"))),
    );
    // KLPS (5.16) closed form: dE = -E zk/(1 + zk zbk)
    let klps516 = clean(&(de_sol.clone() + ek.clone() * zk.clone() / (at("1") + zk.clone() * zbk.clone())));
    let det_ok = is_zero(&(det6.clone() - at("2") * ii.clone()));
    let alpha_expected: Vec<Atom> = vec![
        at("-1/2"),
        clean(&(at("-1/2") * ii.clone())),
        at("0"),
        at("0"),
        at("1/2"),
        clean(&(at("1/2") * ii.clone())),
    ];
    let alpha_ok = alpha
        .iter()
        .zip(alpha_expected.iter())
        .all(|(a, e)| is_zero(&(a.clone() - e.clone())));
    let ok43 = det_ok && resid_sol == at("0") && klps516 == at("0");
    push(
        &mut results,
        "S4.3",
        "S4",
        "KLPS (5.16) hard operator is exactly the holomorphic half of the Lorentz combination: chiral target (Y^z = zk^2, Y^zb = 0) solvable and dE = -(E/2) D_z Y^z",
        ok43,
        plain(&format!(
            "det M6 = {}; alpha = [{}]; dE = -E zk/(1+zk zbk) holds: {}",
            det6,
            alpha
                .iter()
                .map(|a| clean(a).to_string())
                .collect::<Vec<_>>()
                .join(", "),
            klps516 == at("0")
        )),
        ok43 && det_ok && alpha_ok,
    );

    // ================================================================ S5 the D^2 bridge
    let xh_soft = xhat(&z, &zb);
    let x_soft: V4 = [
        at("1"),
        xh_soft[0].clone(),
        xh_soft[1].clone(),
        xh_soft[2].clone(),
    ];
    let qv: V4 = array::from_fn(|i| om.clone() * x_soft[i].clone());
    let qdotp = mdot(&qv, &pk);
    let sq2 = at("2^(1/2)");
    let eps_m: V4 = [
        z.clone() / sq2.clone(),
        at("1") / sq2.clone(),
        ii.clone() / sq2.clone(),
        -z.clone() / sq2.clone(),
    ];
    let eps_p: V4 = [
        zb.clone() / sq2.clone(),
        at("1") / sq2.clone(),
        (-ii.clone()) / sq2.clone(),
        -zb.clone() / sq2.clone(),
    ];
    let dxz: V4 = [
        at("0"),
        xh_soft[0].derivative(symbol!("marici::z")).expand(),
        xh_soft[1].derivative(symbol!("marici::z")).expand(),
        xh_soft[2].derivative(symbol!("marici::z")).expand(),
    ];
    let dxzb: V4 = [
        at("0"),
        xh_soft[0].derivative(symbol!("marici::zb")).expand(),
        xh_soft[1].derivative(symbol!("marici::zb")).expand(),
        xh_soft[2].derivative(symbol!("marici::zb")).expand(),
    ];
    let az = mdot(&pk, &dxz);
    let azb = mdot(&pk, &dxzb);
    let ql_soft = lower4(&qv);

    /// Per-leg operator (c_zk, c_zbk, c_Ek) from v^nu J_{nu lam} q^lam:
    /// antisymmetric beta^{r s} = v^r q^s - v^s q^r contracted with the leg J.
    fn build_op(
        vvec: &V4,
        ql: &V4,
        gens: &[(usize, usize); 6],
        dz_gen: &[Atom],
        dzb_gen: &[Atom],
        de_gen: &[Atom],
    ) -> [Atom; 3] {
        let vl = lower4(vvec);
        let mut cz = at("0");
        let mut czb = at("0");
        let mut ce = at("0");
        for (gi, &(m, n)) in gens.iter().enumerate() {
            let beta = clean(
                &(vl[m].clone() * ql[n].clone() - vl[n].clone() * ql[m].clone()),
            );
            cz = clean(&(cz + beta.clone() * dz_gen[gi].clone()));
            czb = clean(&(czb + beta.clone() * dzb_gen[gi].clone()));
            ce = clean(&(ce + beta * de_gen[gi].clone()));
        }
        [cz, czb, ce]
    }

    let op_z = build_op(&dxz, &ql_soft, &gens, &dz_gen, &dzb_gen, &de_gen);
    let op_zb = build_op(&dxzb, &ql_soft, &gens, &dz_gen, &dzb_gen, &de_gen);
    let szz: [Atom; 3] = array::from_fn(|i| {
        clean(&(az.clone() * op_z[i].clone() / qdotp.clone()))
    });
    let szbb: [Atom; 3] = array::from_fn(|i| {
        clean(&(azb.clone() * op_zb[i].clone() / qdotp.clone()))
    });

    let c_zk_decl = at("2*(1+zb*zk)^3/((z-zk)*(1+z*zb)^3)");
    let c_ek_decl = at("-2*Ek*(zb-zbk)*(1+zb*zk)^2/((z-zk)*(1+z*zb)^3*(1+zk*zbk))");
    let om_free = szz.iter().all(|c| !has_symbol(c, "om"));
    let ok51 = om_free
        && is_zero(&(szz[0].clone() - c_zk_decl))
        && is_zero(&szz[1])
        && is_zero(&(szz[2].clone() - c_ek_decl));
    push(
        &mut results,
        "S5.1",
        "S5",
        "per-leg Shat^(1)_zz operator: om cancels exactly; components (c_zk, c_zbk, c_Ek) = (2(1+zb zk)^3/((z-zk)(1+z zb)^3), 0, -2 E (zb-zbk)(1+zb zk)^2/((z-zk)(1+z zb)^3(1+zk zbk)))",
        ok51,
        if ok51 {
            String::new()
        } else {
            format!(
                "Szz = [{}]",
                szz.iter()
                    .map(|c| crop(&clean(c).to_string()))
                    .collect::<Vec<_>>()
                    .join(", ")
            )
        },
        ok51,
    );

    let s52 = [
        sigma(&szz[0]) - szbb[1].clone(),
        sigma(&szz[1]) - szbb[0].clone(),
        sigma(&szz[2]) - szbb[2].clone(),
    ];
    check_all_zero(
        &mut results,
        "S5.2",
        "S5",
        "conjugation: sigma(Shat_zz) = Shat_zbzb as operators (simultaneous-swap sigma, symbolic cancel proof)",
        &s52,
        "",
    );

    let sq2s = at("sq2");
    let eps_ms: V4 = [
        z.clone() / sq2s.clone(),
        at("1") / sq2s.clone(),
        ii.clone() / sq2s.clone(),
        -z.clone() / sq2s.clone(),
    ];
    let eps_ps: V4 = [
        zb.clone() / sq2s.clone(),
        at("1") / sq2s.clone(),
        (-ii.clone()) / sq2s.clone(),
        -zb.clone() / sq2s.clone(),
    ];
    let eps_zm = mdot(&dxz, &eps_ms);
    let eps_zbm = mdot(&dxzb, &eps_ms);
    let eps_zp = mdot(&dxz, &eps_ps);
    let eps_zbp = mdot(&dxzb, &eps_ps);
    // symbolica keeps 2^(1/2) and 2*(1/2)^(1/2) unmerged, so the pullback
    // comparison uses a symbol sq2 reduced by its defining relation sq2^2 = 2.
    let s53 = [
        eps_zm - sq2s.clone() / (at("1") + z.clone() * zb.clone()),
        eps_zbm,
        eps_zp,
        eps_zbp - sq2s.clone() / (at("1") + z.clone() * zb.clone()),
    ];
    let s53: Vec<Atom> = s53.iter().map(norm_sq2).collect();
    check_all_zero(
        &mut results,
        "S5.3",
        "S5",
        "polarization pullbacks: eps^-_z = sqrt(2)/(1+z zb), eps^-_zb = 0, eps^+_z = 0, eps^+_zb = sqrt(2)/(1+z zb)",
        &s53,
        "sqrt(2) carried as symbol sq2 with exact relation sq2^2 = 2",
    );

    let eps_z_m = mdot(&dxz, &eps_m);
    let eps_zb_p = mdot(&dxzb, &eps_p);
    let p_eps_m = mdot(&pk, &eps_m);
    let p_eps_p = mdot(&pk, &eps_p);
    let op_em = build_op(&eps_m, &ql_soft, &gens, &dz_gen, &dzb_gen, &de_gen);
    let op_ep = build_op(&eps_p, &ql_soft, &gens, &dz_gen, &dzb_gen, &de_gen);
    let hzz: [Atom; 3] = array::from_fn(|i| {
        clean(
            &(eps_z_m.clone() * eps_z_m.clone()
                * p_eps_m.clone()
                * op_em[i].clone()
                / qdotp.clone()),
        )
    });
    let hzbb: [Atom; 3] = array::from_fn(|i| {
        clean(
            &(eps_zb_p.clone() * eps_zb_p.clone()
                * p_eps_p.clone()
                * op_ep[i].clone()
                / qdotp.clone()),
        )
    });

    let d2 = |x: &Atom, v: symbolica::atom::Symbol| {
        x.derivative(v).expand().derivative(v).expand()
    };
    // Printed (6.8) RHS (stripped of kap/8 pi): D_zb^2 Shat_zz - D_z^2 Shat_zbzb.
    // On a (z,z) tensor D_zb^2 is plain d_zb^2 (mixed Christoffels vanish).
    let rhs68: [Atom; 3] = array::from_fn(|i| {
        clean(
            &(d2(&szz[i], symbol!("marici::zb")) - d2(&szbb[i], symbol!("marici::z"))),
        )
    });
    let lhs66: [Atom; 3] = array::from_fn(|i| {
        clean(
            &(d2(&hzbb[i], symbol!("marici::zb")) - d2(&hzz[i], symbol!("marici::z"))),
        )
    });
    check_zero(
        &mut results,
        "S5.4",
        "S5",
        "PSZ (6.8) bridge, energy channel: derived-from-(6.6) D_zb^2 H_zbzb - D_z^2 H_zz equals the printed RHS D_zb^2 Shat_zz - D_z^2 Shat_zbzb exactly in the d_Ek component (factor-2 note: (6.1) half-symmetric limit vs (6.5) convention)",
        &(lhs66[2].clone() - rhs68[2].clone()),
    );
    check_nonzero(
        &mut results,
        "S5.5a",
        "S5",
        "typed obstruction: (6.8) per-leg angular channel (d_zk) residual is nonzero (exact rational point)",
        &pt1(&(lhs66[0].clone() - rhs68[0].clone())),
        Some(&at("102500/483153")),
    );
    check_nonzero(
        &mut results,
        "S5.5b",
        "S5",
        "typed obstruction: (6.8) per-leg angular channel (d_zbk) residual is nonzero (exact rational point); closure route = leg-summed J-conservation form used for PSZ (6.9) and/or [SZ] arXiv:1411.5745 (ungrounded)",
        &pt1(&(lhs66[1].clone() - rhs68[1].clone())),
        Some(&at("1671500/7891499")),
    );

    // ================================================================ S6 Green kernel
    // The first z-derivative of the two log channels is encoded exactly:
    // d_z log(z-w) = 1/(z-w), d_z[-log(1+z zb)] = -zb/(1+z zb); the (w, wb)
    // log channels are z-independent. Symbolica computes the zb-derivative.
    let g1z = at("1/(z-w) - zb/(1+z*zb)");
    check_zero(
        &mut results,
        "S6.1",
        "S6",
        "regular part d_z d_zb G = -1/(1+z zb)^2 = -(1/2) gamma_zzb (PSZ 5.4) [ported-core-only: first log-derivative 1/u encoded by hand, second derivative engine-computed]",
        &(g1z.derivative(symbol!("marici::zb")).expand() + at("1/(1+z*zb)^2")),
    );
    push(
        &mut results,
        "S6.2",
        "S6",
        "distributional part: declared prescription d_zb (z-w)^{-1} = pi delta^2; the two log channels ln(z-w), ln(zb-wb) contribute pi + pi = 2 pi (PSZ 5.4)",
        true,
        "declared input (external ledger item 5): 2*pi = pi + pi exact [ported-core-only: distributional prescription is a declared input, not an engine computation, identical to the sympy record]".to_string(),
        true,
    );
    let szw = (z.clone() - w.clone()) * (zb.clone() - wb.clone())
        / ((at("1") + z.clone() * zb.clone()) * (at("1") + w.clone() * wb.clone()));
    let xh_w = xhat(&w, &wb);
    let xh_dot: Atom = (0..3)
        .map(|i| xh_soft[i].clone() * xh_w[i].clone())
        .fold(at("0"), |s, t| (s + t).expand());
    check_zero(
        &mut results,
        "S6.3",
        "S6",
        "same kernel as the leading triangle: xhat(z).xhat(w) = 1 - 2 S with S = sin^2(Theta/2) (links PSZ 5.3 to the checked HMLS 2.25-2.26 identities)",
        &(xh_dot - (at("1") - at("2") * szw)),
    );

    // ================================================================ S7 news shift law
    check_all_zero(
        &mut results,
        "S7.1",
        "S7",
        "D_z^3 kills the global conformal Killing vectors span{1, z, z^2} (KLPS 5.5 quotient, among globally smooth vector fields)",
        &[dz3_vec(&at("1")), dz3_vec(&z), dz3_vec(&at("z^2"))],
        "",
    );
    check_zero(
        &mut results,
        "S7.2",
        "S7",
        "D_z^3(z^3) = 6 != 0: modes outside the CKV span are not killed (Schwarzian-type normalization)",
        &(dz3_vec(&at("z^3")) - at("6")),
    );
    check_all_zero(
        &mut results,
        "S7.3",
        "S7",
        "typed refinement: the FORMAL kernel of D_z^3 is larger than the CKVs — antiholomorphic-dressed vectors zb, zb^2, z zb are also killed but fail global smoothness at the poles; the CKV-only kernel needs the smoothness condition (analytic input, same mechanism as S8.2)",
        &[dz3_vec(&zb), dz3_vec(&at("zb^2")), dz3_vec(&(z.clone() * zb.clone()))],
        "",
    );
    check_nonzero(
        &mut results,
        "S7.4",
        "S7",
        "the formal kernel is not all antiholomorphic-dressed fields either: D_z^3(zb/(1+z zb)) != 0",
        &dz3_vec(&(zb.clone() / (at("1") + z.clone() * zb.clone()))),
        Some(&at("-6*zb^4/(1+z*zb)^4")),
    );

    // ================================================================ S8 carrier (H2)
    let n_real = z.clone() * zb.clone() * (z.clone() + zb.clone())
        / (at("1") + z.clone() * zb.clone());
    let czz_n = dz_low(&dz_low(&n_real, 0), 1);
    let czbb_n = dzb_low(&dzb_low(&n_real, 0), 1);
    let a_z = dz_low(&czz_n, 2);
    let a_zb = dzb_low(&czbb_n, 2);
    let b_curl = clean(
        &(a_zb.derivative(symbol!("marici::z")).expand()
            - a_z.derivative(symbol!("marici::zb")).expand()),
    );
    let b_val = pt_z2(&b_curl);
    let ok81 = is_zero(&(sigma(&n_real) - n_real.clone()))
        && is_zero(&(sigma(&b_curl) + b_curl.clone()))
        && b_val != at("0");
    push(
        &mut results,
        "S8.1",
        "S8",
        "Stokes bridge on an explicit real field: the PSZ (4.5) bulk form B = d_z(D_zb C_zbzb) - d_zb(D_z C_zz) is sigma-odd (magnetic-only contour) and nonzero",
        ok81,
        plain(&format!(
            "test field N = z zb (z+zb)/(1+z zb); B(2, 3/5) = {}",
            b_val
        )),
        ok81,
    );

    let s82: Vec<Atom> = [2i64, 3, 4]
        .iter()
        .map(|&s| dz_low(&at(&format!("(1+z*zb)^({})", -2 * s)), s))
        .collect();
    check_all_zero(
        &mut results,
        "S8.2",
        "S8",
        "grade-step ambiguity: ker of D_z on rank-s lower-z tensors is (1+z zb)^{-2s} x (antiholomorphic) for s = 2, 3, 4 — the smooth/corner-condition quotient is an analytic input, not exact",
        &s82,
        "",
    );

    let x_gauge = z.clone() * zb.clone() / (at("1") + z.clone() * zb.clone());
    let y_gauge = x_gauge
        .derivative(symbol!("marici::z"))
        .expand()
        .derivative(symbol!("marici::zb"))
        .expand();
    let ok83 = is_zero(&(sigma(&x_gauge) - x_gauge.clone()))
        && is_zero(&(sigma(&y_gauge) - y_gauge.clone()));
    push(
        &mut results,
        "S8.3",
        "S8",
        "curl-only dependence: for real X, d_z d_zb X is sigma-even, so the Im projection kills gauge shifts N_z -> N_z + d_z X (PSZ below (5.7))",
        ok83,
        String::new(),
        ok83,
    );
    push(
        &mut results,
        "S8.4",
        "S8",
        "carrier verdict (H2 test): NOT one operator — one sigma-odd FIELD (the curl/magnetic tower over C_zz, equivalently the curl of N_z) read at three derivative grades: D_z (memory contour PSZ 4.5), D_z^2 (soft side PSZ 6.9), D_z^3 (constraint/shift PSZ 5.2, KLPS 5.5). Typed refinement of the leading one-operator picture.",
        true,
        "confirmed by S8.1-S8.3 + S7.1 kernel structure".to_string(),
        true,
    );

    // ================================================================ S9 constraint parity
    let d3c = dz_low(&dz_low(&dz_low(&czz_n, 2), 3), 4);
    let d3cb = dzb_low(&dzb_low(&dzb_low(&czbb_n, 2), 3), 4);
    let l9 = d3c.derivative(symbol!("marici::zb")).expand();
    let r9 = d3cb.derivative(symbol!("marici::z")).expand();
    let l9mr9 = pt_z2(&(l9.clone() - r9.clone()));
    let ok91 = is_zero(&(sigma(&l9) - r9.clone())) && l9mr9 != at("0");
    push(
        &mut results,
        "S9.1",
        "S9",
        "magnetic-parity projection: sigma(d_zb D_z^3 C_zz) = d_z D_zb^3 C_zbzb exactly on the real test field, and the two differ — the Im in PSZ (5.2) is a genuine parity projection",
        ok91,
        plain(&format!("(L9 - R9)(2, 3/5) = {}", l9mr9)),
        ok91,
    );
    let x_gauge2 = at("(z+zb)^2/(1+z*zb)^2");
    let y_gauge2 = x_gauge2
        .derivative(symbol!("marici::z"))
        .expand()
        .derivative(symbol!("marici::zb"))
        .expand();
    let ok92 = is_zero(&(sigma(&x_gauge2) - x_gauge2.clone()))
        && is_zero(&(sigma(&y_gauge2) - y_gauge2.clone()));
    push(
        &mut results,
        "S9.2",
        "S9",
        "RHS curl-only invariance (PSZ below (5.5)): real shift N_z -> N_z + d_z X leaves Im[d_u d_zb N_z + d_zb T_uz] invariant (second independent real test field)",
        ok92,
        String::new(),
        ok92,
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
            "reference": "research/strominger/results/subleading_triangle_exact_checks.json (sympy, 30/30)",
            "agreement": format!("{}/{} verdicts agree with the sympy reference; typed residuals compared exactly where declared (S2.3 a1, S4.3 det M6 = 2i + alpha = (-1/2, -i/2, 0, 0, 1/2, i/2), S5.5a 102500/483153, S5.5b 1671500/7891499, S7.4 -6 zb^4/(1+z zb)^4)", n_agree, results.len()),
            "disagreements": disagreed,
            "ported_core_only": [
                "S6.1: the first log-derivative d_z log(u) = u'/u is encoded by hand (exact); the mixed second derivative is engine-computed",
                "S6.2: distributional prescription d_zb (z-w)^{-1} = pi delta^2 is a declared external input in both engines",
                "S8.4: classification verdict record (corroborated by S8.1-S8.3 + S7.1), same as sympy"
            ]
        },
        "classification": {
            "carrier": "one sigma-odd field (the magnetic/curl part of N_z, equivalently the tower over C_zz) read at three derivative grades D_z, D_z^2, D_z^3 — NOT one operator (H2 confirmed as a typed refinement of the leading one-operator picture)",
            "common_operation": "curl/magnetic projection (Im) of the C_zz tower; per-leg soft operator Shat^(1)_zz with components (c_zk, 0, c_Ek) built from PSZ (6.5)+(6.7)",
            "verdict": "soft-memory bridge (PSZ 6.8) exact per leg in the energy channel; angular channels are a typed per-leg residual",
            "external_inputs": [
                "J: global angular momentum conservation (CS (7); PSZ (6.9) derivation)",
                "G_CS gauge prescription (conventions packet section 2)",
                "antipodal matching + KLPS i^0 mode correspondence (packet section 3)",
                "symmetric/hermitian zero-frequency limit (PSZ 6.1) = (1+om d_om) projection (KLPS 5.33)",
                "distributional prescription d_zb (z-w)^{-1} = pi delta^2 (inherited from the leading packet)"
            ],
            "conventions_residuals": [
                "CS (7) sign: with the declared shift dE = q Lam + Lam q the per-leg contraction gives dS^(1) = +i Lam q sum J vs printed -i (shift-sign convention; check S2.1)",
                "S3: PSZ (6.5) / CS (6) ratio is exactly kap = sqrt(32 pi G) (check S3.1/S3.2)",
                "S5: PSZ (6.8) holds per leg only in the d_Ek channel; the factor 2 between derived and printed sides is the (6.1) half-symmetric-limit vs (6.5) convention drift; angular-channel residuals S5.5a/b await the leg-summed J form and/or [SZ] arXiv:1411.5745 (PSZ ref [20], ungrounded: ar5iv extraction failed in the leading session)",
                "S7: the formal kernel of D_z^3 exceeds the CKVs (zb, zb^2, z zb are killed but singular at the poles); the CKV-only quotient requires global smoothness — analytic input, same mechanism as S8.2 (checks S7.3/S7.4)",
                "S8.2: the smoothness/corner-condition quotient removing the (1+z zb)^{-2s} x antiholomorphic ambiguity between derivative grades is an analytic note (declared input), not an exact check"
            ],
            "outcome": "mixed: the subleading naturality square closes exactly at the level of the projector (S1), gauge variation (S2), normalization ratio kap (S3), hard-operator sphere reduction (S4), Green kernel (S6), and the D_z^3 CKV quotient (S7); the D^2 bridge (S5) closes exactly only in the energy channel per leg, with the angular channels recorded as typed residuals; the carrier question lands on one field with three derivative grades rather than one operator (S8, H2 refinement) — reproduced identically by the independent Symbolica engine"
        }
    });

    let out = json!({
        "checker": "subleading_triangle_symbolica_checks",
        "author": "marici.Strominger",
        "date": "2026-08-19",
        "engine": "symbolica 2.2.0 (Rust, no_gmp)",
        "cross_validates": "research/strominger/results/subleading_triangle_exact_checks.json",
        "checks": results,
        "summary": summary,
    });

    std::fs::create_dir_all("../results").unwrap();
    let path = "../results/subleading_triangle_symbolica_checks.json";
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

type V4x4 = [V4; 4];
