//! Deterministic QMC pilot for the literal six-simplex three-site source.
//!
//! This uses the fixed momentum-space cycle l in R^3.  It is discovery
//! evidence, not an IBP or interval certificate.

use std::f64::consts::PI;

fn halton(mut index: u64, base: u64) -> f64 {
    let mut factor = 1.0;
    let mut value = 0.0;
    while index > 0 {
        factor /= base as f64;
        value += factor * (index % base) as f64;
        index /= base;
    }
    value
}

fn norm(v: [f64; 3]) -> f64 {
    (v[0] * v[0] + v[1] * v[1] + v[2] * v[2]).sqrt()
}

fn add(a: [f64; 3], b: [f64; 3]) -> [f64; 3] {
    [a[0] + b[0], a[1] + b[1], a[2] + b[2]]
}

fn source_density(l: [f64; 3], t: f64) -> f64 {
    let x1 = 1.0 + t;
    let x2 = 1.0 - t;
    let x3 = 1.0;
    let energy = x1 + x2 + x3;

    let cos12 = (x3 * x3 - x1 * x1 - x2 * x2) / (2.0 * x1 * x2);
    let sin12 = (1.0 - cos12 * cos12).sqrt();
    let p1 = [x1, 0.0, 0.0];
    let p2 = [x2 * cos12, x2 * sin12, 0.0];

    let y12 = norm(l);
    let y23 = norm(add(l, p1));
    let y31 = norm(add(add(l, p1), p2));

    let g1 = y31 + x1 + y12;
    let g2 = y12 + x2 + y23;
    let g3 = y23 + x3 + y31;
    let big12 = energy + y12;
    let big23 = energy + y23;
    let big31 = energy + y31;
    let small12 = x1 + x2 + y23 + y31;
    let small23 = x2 + x3 + y31 + y12;
    let small31 = x3 + x1 + y12 + y23;

    let six = (1.0 / big12) * (1.0 / small23 + 1.0 / small31)
        + (1.0 / big23) * (1.0 / small31 + 1.0 / small12)
        + (1.0 / big31) * (1.0 / small12 + 1.0 / small23);
    six / (energy * g1 * g2 * g3)
}

fn integral(samples: u64, t: f64) -> f64 {
    let skip: u64 = std::env::var("HALTON_SKIP")
        .ok()
        .and_then(|raw| raw.parse().ok())
        .unwrap_or(0);
    let mut sum = 0.0;
    for i in 1..=samples {
        let index = i + skip;
        let u = halton(index, 2);
        let z = 2.0 * halton(index, 3) - 1.0;
        let phi = 2.0 * PI * halton(index, 5);
        let radial = u / (1.0 - u);
        let transverse = (1.0 - z * z).sqrt();
        let l = [
            radial * transverse * phi.cos(),
            radial * transverse * phi.sin(),
            radial * z,
        ];
        let jacobian = 4.0 * PI * radial * radial / ((1.0 - u) * (1.0 - u));
        sum += jacobian * source_density(l, t);
    }
    sum / samples as f64
}

fn main() {
    let samples: u64 = std::env::var("SAMPLES")
        .ok()
        .and_then(|raw| raw.parse().ok())
        .unwrap_or(1_000_000);
    let h: f64 = std::env::var("SHAPE_STEP")
        .ok()
        .and_then(|raw| raw.parse().ok())
        .unwrap_or(0.02);
    let skip: u64 = std::env::var("HALTON_SKIP")
        .ok()
        .and_then(|raw| raw.parse().ok())
        .unwrap_or(0);

    let minus = integral(samples, -h);
    let zero = integral(samples, 0.0);
    let plus = integral(samples, h);
    let first = (plus - minus) / (2.0 * h);
    let second = (plus - 2.0 * zero + minus) / (h * h);
    println!(
        "{{\"schema\":\"marici.physical-relative-shape-qmc.v1\",\"samples\":{samples},\"skip\":{skip},\"h\":{h:.17},\"minus\":{minus:.17},\"zero\":{zero:.17},\"plus\":{plus:.17},\"first\":{first:.17},\"second\":{second:.17}}}"
    );
}
