use serde_json::{json, Value};
use std::{collections::BTreeSet, f64::consts::PI, fs};

fn cut_support(label: &str) -> Vec<usize> {
    let sites = label.strip_prefix("g_").unwrap().chars()
        .map(|digit| digit.to_digit(10).unwrap() as usize - 1)
        .collect::<BTreeSet<_>>();
    (0..5).filter(|edge|
        sites.contains(edge) != sites.contains(&((edge + 1) % 5))
    ).collect()
}

fn denominator(label: &str, z: f64, y: &[f64; 5]) -> f64 {
    if label == "G" { return 5.0 * z; }
    if let Some(edge) = label.strip_prefix("G_minus_e") {
        let index = edge.chars().next().unwrap().to_digit(10).unwrap() as usize - 1;
        return 5.0 * z + 2.0 * y[index];
    }
    let size = label.strip_prefix("g_").unwrap().len() as f64;
    let cuts = cut_support(label);
    assert_eq!(cuts.len(), 2);
    size * z + y[cuts[0]] + y[cuts[1]]
}

fn gauss_legendre(n: usize) -> Vec<(f64, f64)> {
    let mut rows = Vec::with_capacity(n);
    for i in 0..n {
        let mut x = (PI * (i as f64 + 0.75) / (n as f64 + 0.5)).cos();
        for _ in 0..30 {
            let mut p0 = 1.0;
            let mut p1 = x;
            for k in 2..=n {
                let p2 = ((2 * k - 1) as f64 * x * p1 - (k - 1) as f64 * p0) / k as f64;
                p0 = p1;
                p1 = p2;
            }
            let derivative = n as f64 * (x * p1 - p0) / (x * x - 1.0);
            let delta = p1 / derivative;
            x -= delta;
            if delta.abs() < 2e-15 { break; }
        }
        let mut p0 = 1.0;
        let mut p1 = x;
        for k in 2..=n {
            let p2 = ((2 * k - 1) as f64 * x * p1 - (k - 1) as f64 * p0) / k as f64;
            p0 = p1;
            p1 = p2;
        }
        let derivative = n as f64 * (x * p1 - p0) / (x * x - 1.0);
        let weight = 2.0 / ((1.0 - x * x) * derivative * derivative);
        rows.push((x, weight));
    }
    rows.sort_by(|a, b| a.0.partial_cmp(&b.0).unwrap());
    rows
}

fn period(z: f64, n: usize, common: &[String], terms: &[Vec<String>]) -> f64 {
    let quadrature = gauss_legendre(n);
    let mut sum = 0.0_f64;
    for &(x1, w1) in &quadrature {
        let c1 = (PI * x1 / 2.0).cos();
        let v1 = (PI * x1 / 2.0).tan();
        let j1 = PI / (2.0 * c1 * c1);
        for &(x2, w2) in &quadrature {
            let c2 = (PI * x2 / 2.0).cos();
            let v2 = (PI * x2 / 2.0).tan();
            let j2 = PI / (2.0 * c2 * c2);
            for &(x3, w3) in &quadrature {
                let c3 = (PI * x3 / 2.0).cos();
                let v3 = (PI * x3 / 2.0).tan();
                let j3 = PI / (2.0 * c3 * c3);
                let u1 = z * v1;
                let u2 = z * v2;
                let u3 = z * v3;
                let f1 = 2.0*u1*u1 + 2.0*u2*u2 + u3*u3 - 2.0*u1*u2 - 2.0*u2*u3;
                let f = [
                    f1,
                    f1 - 2.0*u1 + 1.0,
                    f1 - 2.0*u2 + 2.0,
                    f1 - 2.0*u3 + 3.0,
                    f1 + 2.0*u1 + 2.0*u2 - 8.0*u3 + 29.0,
                ];
                if f.iter().any(|value| *value < -1e-10) { panic!("negative radicand"); }
                let y = f.map(|value| value.max(0.0).sqrt());
                let common_product = common.iter()
                    .map(|label| denominator(label, z, &y)).product::<f64>();
                let canonical = terms.iter().map(|term| {
                    let selected = term.iter().map(|label| denominator(label, z, &y)).product::<f64>();
                    1.0 / (common_product * selected)
                }).sum::<f64>();
                let jacobian = z.powi(3) * j1 * j2 * j3;
                sum += w1 * w2 * w3 * jacobian * canonical;
            }
        }
    }
    sum
}

fn run() {
    let source: Value = serde_json::from_str(
        &fs::read_to_string("../results/five-cycle-ofpt-packet.json").unwrap()
    ).unwrap();
    let cycle = &source["five_cycle"];
    let common = cycle["common_prefactor"].as_array().unwrap().iter()
        .map(|entry| entry.as_str().unwrap().to_owned()).collect::<Vec<_>>();
    let terms = cycle["terms"].as_array().unwrap().iter().map(|term|
        term.as_array().unwrap().iter().map(|entry| entry.as_str().unwrap().to_owned()).collect::<Vec<_>>()
    ).collect::<Vec<_>>();
    assert_eq!(common.len(), 6);
    assert_eq!(terms.len(), 180);
    assert!(terms.iter().all(|term| term.len() == 4));

    let zs = [6.0_f64, 8.0, 12.0, 24.0, 48.0, 96.0];
    let orders = [24_usize, 32, 40];
    let mut rows = Vec::new();
    for z in zs {
        let estimates = orders.iter().map(|n| {
            let value = period(z, *n, &common, &terms);
            json!({"quadrature_order": n, "period": value, "scaled_z7": value*z.powi(7)})
        }).collect::<Vec<_>>();
        rows.push(json!({"z": z, "estimates": estimates}));
        println!("z={z} complete");
    }
    let packet = json!({
        "schema": "marici.benincasa.five_site.asymmetric.period_discovery.v1",
        "method": "tensor Gauss-Legendre after u_i=z*tan(pi*x_i/2)",
        "source_terms": 180,
        "common_denominators": 6,
        "selected_denominators_per_term": 4,
        "quadrature_orders": orders,
        "rows": rows,
        "status": "numerical discovery only; not admissible as a period identity or differential equation",
        "next_use": "Estimate convergence and asymptotic structure before freezing an exact telescoper ansatz."
    });
    fs::write(
        "../results/five-site-asymmetric-period-discovery.json",
        serde_json::to_string_pretty(&packet).unwrap() + "\n",
    ).unwrap();
}

fn main() {
    run();
}
