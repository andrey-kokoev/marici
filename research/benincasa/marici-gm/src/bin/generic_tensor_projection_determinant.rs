use symbolica::prelude::*;

fn a(s: &str) -> Atom {
    Atom::parse(s, "marici", Default::default()).unwrap()
}

fn clean(x: Atom) -> Atom {
    x.expand().factor()
}

fn main() {
    let aa = a("a");
    let b = a("b");
    let c = a("c");
    let r = a("r");
    let q2 = clean(aa.clone() * aa.clone() + b.clone() * b.clone() + c.clone() * c.clone());

    // Hard momenta (2,0),(-1,r),(-1,-r), with r^2=3 imposed after
    // construction.  u=(-b,a,0), v=(-ac,-bc,a^2+b^2) span q-perp.
    let ps = [(a("2"), a("0")), (-a("1"), r.clone()), (-a("1"), -r.clone())];
    let ws = [a("w1"), a("w2"), a("w3")];
    let mut rows = Vec::new();
    for ((x, y), w) in ps.into_iter().zip(ws) {
        let pu = clean(-b.clone() * x.clone() + aa.clone() * y.clone());
        let pv = clean(-aa.clone() * c.clone() * x - b.clone() * c.clone() * y);
        let xx = clean(q2.clone() * pu.clone() * pu.clone() - pv.clone() * pv.clone());
        let yy = clean(a("2") * q2.clone() * pu * pv);
        rows.push([a("1"), clean(w.clone() * xx), clean(w * yy)]);
    }

    let det = clean(
        rows[0][0].clone()
            * (rows[1][1].clone() * rows[2][2].clone()
                - rows[1][2].clone() * rows[2][1].clone())
            - rows[0][1].clone()
                * (rows[1][0].clone() * rows[2][2].clone()
                    - rows[1][2].clone() * rows[2][0].clone())
            + rows[0][2].clone()
                * (rows[1][0].clone() * rows[2][1].clone()
                    - rows[1][1].clone() * rows[2][0].clone()),
    );

    // Replace r^2 by 3 after expansion.  The determinant is odd in r, so
    // divide by r first and reduce the remaining even polynomial.
    let reduced = clean((det.clone() / r.clone()).replace(a("r^2").to_pattern()).with(a("3").to_pattern()));
    println!("raw_factor={det}");
    println!("equilateral_reduced_factor={reduced}");

    let mut minimum = f64::INFINITY;
    let mut argmin = (0.0, 0.0, 0.0);
    for ia in -20..=20 {
        for ib in -20..=20 {
            for ic in 1..=20 {
                let (af, bf, cf) = (ia as f64 / 5.0, ib as f64 / 5.0, ic as f64 / 5.0);
                let psf = [(2.0, 0.0), (-1.0, 3.0_f64.sqrt()), (-1.0, -3.0_f64.sqrt())];
                let mut wf = [0.0; 3];
                for (i, (x, y)) in psf.into_iter().enumerate() {
                    let kp = ((x + af).powi(2) + (y + bf).powi(2) + cf * cf).sqrt();
                    wf[i] = 1.0 / (2.0 + kp);
                }
                let [w1, w2, w3] = wf;
                let bracket = 2.0 * af * bf * 3.0_f64.sqrt() * w1 * (w2 - w3)
                    + 3.0 * af * af * w2 * w3
                    + 2.0 * bf * bf * w1 * (w2 + w3)
                    - bf * bf * w2 * w3
                    + 2.0 * cf * cf * (w1 * w2 + w1 * w3 + w2 * w3);
                if bracket < minimum {
                    minimum = bracket;
                    argmin = (af, bf, cf);
                }
            }
        }
    }
    println!("physical_grid_minimum_bracket={minimum:.12e} at q={argmin:?}");

    let mut state = 0x9e3779b97f4a7c15_u64;
    let mut random_minimum = f64::INFINITY;
    let mut random_argmin = (0.0, 0.0, 0.0);
    for _ in 0..500_000 {
        let mut next = || {
            state = state.wrapping_mul(6364136223846793005).wrapping_add(1442695040888963407);
            ((state >> 11) as f64) / ((1_u64 << 53) as f64)
        };
        let af = 100.0 * next() - 50.0;
        let bf = 100.0 * next() - 50.0;
        let cf = 10_f64.powf(4.0 * next() - 3.0);
        let psf = [(2.0, 0.0), (-1.0, 3.0_f64.sqrt()), (-1.0, -3.0_f64.sqrt())];
        let mut wf = [0.0; 3];
        for (i, (x, y)) in psf.into_iter().enumerate() {
            let kp = ((x + af).powi(2) + (y + bf).powi(2) + cf * cf).sqrt();
            wf[i] = 1.0 / (2.0 + kp);
        }
        let [w1, w2, w3] = wf;
        let bracket = 2.0 * af * bf * 3.0_f64.sqrt() * w1 * (w2 - w3)
            + 3.0 * af * af * w2 * w3
            + 2.0 * bf * bf * w1 * (w2 + w3)
            - bf * bf * w2 * w3
            + 2.0 * cf * cf * (w1 * w2 + w1 * w3 + w2 * w3);
        if bracket < random_minimum {
            random_minimum = bracket;
            random_argmin = (af, bf, cf);
        }
    }
    println!("physical_random_minimum_bracket={random_minimum:.12e} at q={random_argmin:?}");

    // Rewrite the residual in shifted energies t_i=|p_i+q|.  Put
    // A=a=(2t1^2-t2^2-t3^2)/12 and R=sqrt(3)b=(t2^2-t3^2)/4.
    let t1 = a("t1");
    let t2 = a("t2");
    let t3 = a("t3");
    let x1 = t1.clone() * t1.clone();
    let x2 = t2.clone() * t2.clone();
    let x3 = t3.clone() * t3.clone();
    let av = clean((a("2") * x1.clone() - x2.clone() - x3.clone()) / a("12"));
    let rv = clean((x2.clone() - x3.clone()) / a("4"));
    let qsq = clean((x1 + x2 + x3) / a("3") - a("4"));
    let csq = clean(qsq - av.clone() * av.clone() - rv.clone() * rv.clone() / a("3"));
    let ew = [
        clean(a("1") / (a("2") + t1)),
        clean(a("1") / (a("2") + t2)),
        clean(a("1") / (a("2") + t3)),
    ];
    let energy_residual = clean(
        a("2") * av.clone() * rv.clone() * ew[0].clone() * (ew[1].clone() - ew[2].clone())
            + a("3") * av.clone() * av * ew[1].clone() * ew[2].clone()
            + rv.clone() * rv / a("3")
                * (a("2") * ew[0].clone() * ew[1].clone()
                    + a("2") * ew[0].clone() * ew[2].clone()
                    - ew[1].clone() * ew[2].clone())
            + a("2") * csq
                * (ew[0].clone() * ew[1].clone()
                    + ew[0].clone() * ew[2].clone()
                    + ew[1].clone() * ew[2].clone()),
    );
    println!("shifted_energy_residual={energy_residual}");
}
