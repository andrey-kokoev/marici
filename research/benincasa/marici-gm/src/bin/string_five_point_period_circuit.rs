use std::{collections::BTreeMap, f64::consts::PI, fs};

#[derive(Clone, Copy)]
struct EulerData { sign: f64, a: f64, b: f64, c: f64, d: f64, e: f64 }

fn gamma(z: f64) -> f64 {
    const P: [f64; 9] = [0.9999999999998099, 676.5203681218851,
        -1259.1392167224028, 771.3234287776531, -176.6150291621406,
        12.507343278686905, -0.13857109526572012, 9.984369578019572e-6,
        1.5056327351493116e-7];
    if z < 0.5 { return PI / ((PI * z).sin() * gamma(1.0 - z)); }
    let q = z - 1.0;
    let mut x = P[0];
    for (i, coefficient) in P.iter().enumerate().skip(1) { x += coefficient / (q + i as f64); }
    let t = q + 7.5;
    (2.0 * PI).sqrt() * t.powf(q + 0.5) * (-t).exp() * x
}

fn beta(x: f64, y: f64) -> f64 { gamma(x) * gamma(y) / gamma(x + y) }

fn period(p: EulerData) -> (f64, usize) {
    let (mut term, mut sum) = (1.0, 1.0);
    for n in 0..5_000_000_usize {
        let k = n as f64;
        term *= (-p.e + k) * (p.a + k) * (p.c + k)
            / ((p.a + p.b + k) * (p.c + p.d + k) * (k + 1.0));
        sum += term;
        if term.abs() < 1.0e-17 {
            return (p.sign * beta(p.a, p.b) * beta(p.c, p.d) * sum, n + 1);
        }
    }
    panic!("hypergeometric recurrence did not converge");
}

fn main() {
    // (s12,s24,s13,s34,s23)=(9/20,-17/40,11/8,-17/5,1/2).
    let (s12, s24, s13, s34, s23) =
        (9.0/20.0, -17.0/40.0, 11.0/8.0, -17.0/5.0, 1.0/2.0);
    // Derived by source-labelled relabelling to 0 < xy < y < 1.
    let chambers = [
        ("12354", EulerData { sign: 1.0, a: 9.0/20.0, b: 1.0/2.0,
            c: 93.0/40.0, d: 101.0/40.0, e: -21.0/40.0 }),
        ("13254", EulerData { sign: -1.0, a: 19.0/8.0, b: 1.0/2.0,
            c: 93.0/40.0, d: 19.0/40.0, e: 61.0/40.0 }),
        ("14253", EulerData { sign: 1.0, a: 5.0/2.0, b: 23.0/40.0,
            c: 101.0/40.0, d: 19.0/40.0, e: 53.0/40.0 }),
    ];
    let (mut values, mut terms) = (BTreeMap::new(), BTreeMap::new());
    for (name, p) in chambers {
        assert!(p.a > 0.0 && p.b > 0.0 && p.c > 0.0 && p.d > 0.0);
        assert!(p.b + p.d + p.e > 0.0);
        let (value, count) = period(p);
        values.insert(name, value); terms.insert(name, count);
    }
    let c1 = -((PI * (s12 + s23)).sin() / (PI * s12).sin());
    let c2 = -((PI * s24).sin() / (PI * s12).sin());
    let predicted = c1 * values["13254"] + c2 * values["14253"];
    let residual = values["12354"] - predicted;
    let relative = residual.abs() / values["12354"].abs();
    let tolerance = 5.0e-13;
    assert!(relative < tolerance, "circuit mismatch: {relative:e}");
    let json = format!(concat!(
        "{{\n  \"fixed_cocycle\": \"PT(12345)\",\n",
        "  \"mandelstam\": {{\"s12\": {:.17}, \"s24\": {:.17}, \"s13\": {:.17}, \"s34\": {:.17}, \"s23\": {:.17}}},\n",
        "  \"common_convergence_locus\": true,\n",
        "  \"periods\": {{\"12354\": {:.17}, \"13254\": {:.17}, \"14253\": {:.17}}},\n",
        "  \"series_terms\": {{\"12354\": {}, \"13254\": {}, \"14253\": {}}},\n",
        "  \"circuit_coefficients\": {{\"13254\": {:.17}, \"14253\": {:.17}}},\n",
        "  \"predicted_12354\": {:.17},\n  \"residual\": {:.17e},\n",
        "  \"relative_residual\": {:.17e},\n  \"tolerance\": {:.1e},\n  \"passed\": true\n}}\n"),
        s12,s24,s13,s34,s23, values["12354"],values["13254"],values["14253"],
        terms["12354"],terms["13254"],terms["14253"],c1,c2,predicted,residual,relative,tolerance);
    fs::write("../string-five-point-period-circuit.json", &json).expect("write packet");
    print!("{json}");
}
