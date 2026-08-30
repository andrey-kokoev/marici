use serde_json::json;
use std::fs;

fn disc_coeffs(k: f64, b: f64, d: f64) -> (f64, f64, f64) {
    let q2 = -10.0;
    let q1 = 18.0 * k * b - 4.0 * k * d + 56.0 * k - 16.0 * b + 28.0 * d + 48.0;
    let q0 = -276.0 - 280.0 * k - 40.0 * k * b - 22.0 * k * b * d + 4.0 * k * b * b - 40.0 * k * d
        + 4.0 * k * d * d
        + 49.0 * k * k
        - 14.0 * k * k * b
        - 2.0 * k * k * b * d
        + k * k * b * b
        - 14.0 * k * k * d
        + k * k * d * d
        - 24.0 * b
        + 32.0 * b * d
        - 22.0 * b * b
        - 24.0 * d
        - 22.0 * d * d;
    (q2, q1, q0)
}

fn solve_u(k: f64, b: f64, d: f64, e: f64) -> f64 {
    let q = -6.0
        - 67.0 * k
        - 47.0 * k * b
        - 22.0 * k * d
        - 11.0 * k * e
        - 118.0 * k * k
        - 18.0 * k * k * b
        - 14.0 * k * k * d
        - 10.0 * k * k * e
        - 56.0 * k * k * k
        + 16.0 * k * k * k * b
        + 12.0 * k * k * k * d
        - 9.0 * b
        - 9.0 * d
        + 3.0 * e;
    -q / (12.0 * k + 14.0 * k * k)
}

fn solve_x(k: f64, b: f64, d: f64, e: f64) -> f64 {
    -(2.0 + 3.0 * k + (3.0 - k) * (b + d) - e) / (2.0 * k - 4.0)
}

fn solve_w(k: f64, b: f64, d: f64, e: f64, x: f64) -> f64 {
    let q = 6.0 + 139.0 * k - 50.0 * k * x + 58.0 * k * b + 11.0 * k * d + 18.0 * k * e - 12.0 * x
        + 226.0 * k * k
        - 18.0 * k * k * x
        + 2.0 * k * k * b
        + 30.0 * k * k * d
        + 2.0 * k * k * e
        + 84.0 * k * k * k
        + 28.0 * k * k * k * x
        - 20.0 * k * k * k * b
        - 8.0 * k * k * k * d
        + 9.0 * b
        + 9.0 * d
        - 3.0 * e;
    q / (12.0 * k + 14.0 * k * k)
}

fn physical_frame(b: f64, d: f64, e: f64, u: f64, x: f64, w: f64) -> Option<serde_json::Value> {
    let (s2, s4, s5, s6) = (b.sqrt(), -d.sqrt(), -e.sqrt(), -u.sqrt());
    if !(s4 < -s2 && s5 < s4 && s5 < s6 && s6 < 0.0) {
        return None;
    }
    let (q, p) = ((-s2 - s4) / 2.0, -s6 / 2.0);
    let xs = [-s6 - p, s2, q, -s2 - s4 - q, s4 - s5, s6 - s5, p];
    for e3 in [-1.0, 1.0] {
        for e7 in [-1.0, 1.0] {
            let (y3, y7) = (e3 * x.sqrt(), e7 * w.sqrt());
            let factors = [
                -2.0 * s5,
                -s6 - p + y7,
                2.0 * s2,
                q + s2 + y3,
                y3 - s2 - q,
                2.0 * s4,
                2.0 * s6,
                p + s6 + y7,
            ];
            let min = factors
                .iter()
                .map(|v| v.abs())
                .fold(f64::INFINITY, f64::min);
            if min > 1e-6 {
                return Some(
                    json!({"signed_parameters":{"s2":s2,"s4":s4,"s5":s5,"s6":s6,"y3":y3,"y7":y7,"p":p,"q":q},"positive_site_energies":xs,"source_factor_values":factors,"minimum_absolute_source_factor":min}),
                );
            }
        }
    }
    None
}

fn main() {
    let max = std::env::var("SEARCH_MAX")
        .ok()
        .map(|v| v.parse::<i32>().unwrap())
        .unwrap_or(120);
    let roots = [(3.0 + 17.0_f64.sqrt()) / 4.0, (3.0 - 17.0_f64.sqrt()) / 4.0];
    let mut algebraic_records = Vec::new();
    let mut physical_records = Vec::new();
    for (branch, k) in roots.into_iter().enumerate() {
        let mut first_algebraic = None;
        'search: for bi in 1..=max {
            for di in 1..=max {
                let (b, d) = (f64::from(bi), f64::from(di));
                let (qa, qb, qc) = disc_coeffs(k, b, d);
                let rad = qb * qb - 4.0 * qa * qc;
                if rad <= 0.0 {
                    continue;
                }
                for sign in [-1.0, 1.0] {
                    let e = (-qb + sign * rad.sqrt()) / (2.0 * qa);
                    if e <= 0.0 {
                        continue;
                    }
                    let u = solve_u(k, b, d, e);
                    let x = solve_x(k, b, d, e);
                    let w = solve_w(k, b, d, e, x);
                    if u <= 0.0 || x <= 0.0 || w <= 0.0 {
                        continue;
                    }
                    let base = json!({"branch":branch,"k_interval":[k-1e-12,k+1e-12],"integer_slice":{"B":bi,"D":di},"E_interval":[e-1e-10,e+1e-10],"U_interval":[u-1e-10,u+1e-10],"x_interval":[x-1e-10,x+1e-10],"w_interval":[w-1e-10,w+1e-10],"exact_definition":"C(k)=0; E is the indicated real root of Disc_x(F)=0; U solves G=0; x solves F_x=0; w solves H=0"});
                    if first_algebraic.is_none() {
                        first_algebraic = Some(base.clone());
                    }
                    if let Some(frame) = physical_frame(b, d, e, u, x, w) {
                        let mut physical = base;
                        physical["physical_frame"] = frame;
                        physical_records.push(physical);
                        break 'search;
                    }
                }
            }
        }
        if let Some(record) = first_algebraic {
            algebraic_records.push(record);
        }
    }
    let packet = json!({"schema":"marici.seven_site_multiloop_real_discovery.v3","status":"bounded discovery only; exact polynomial towers certify the algebraic records","searched_integer_box":format!("1 <= B,D <= {max}"),"algebraic_real_records":algebraic_records,"physical_positive_X_records":physical_records,"both_algebraic_real_branches_found":algebraic_records.len()==2,"positive_X_null_census_is_not_proof":true});
    fs::write(
        "../results/seven-site-multiloop-real-discovery.json",
        serde_json::to_string_pretty(&packet).unwrap() + "\n",
    )
    .unwrap();
    println!(
        "{}",
        json!({"algebraic_real_records":algebraic_records.len(),"physical_positive_X_records":physical_records.len()})
    );
}
