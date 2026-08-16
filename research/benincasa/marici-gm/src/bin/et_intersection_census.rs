use std::env;
use std::fs;

#[derive(Clone, Copy)]
struct Divisor {
    name: &'static str,
    class: &'static str,
    // Primitive polynomial in v after restricting u=E_T=0.
    coeffs: &'static [i64],
    genuine: bool,
}

fn eval(coeffs: &[i64], v: i64) -> i64 {
    coeffs.iter().rev().fold(0, |acc, c| acc * v + c)
}

fn integer_roots(coeffs: &[i64]) -> Vec<i64> {
    if coeffs.len() <= 1 {
        return Vec::new();
    }
    (-16..=16).filter(|v| eval(coeffs, *v) == 0).collect()
}

fn is_site_soft(v: i64) -> bool {
    // At u=0 with X1=1: X2=v/2-1 and X3=-v/2.
    v == 0 || v == 2
}

fn divisors() -> Vec<Divisor> {
    vec![
        Divisor { name: "X2", class: "site_energy", coeffs: &[-2, 1], genuine: true },
        Divisor { name: "X3", class: "site_energy", coeffs: &[0, 1], genuine: true },
        Divisor { name: "X1+X2", class: "energy_sum", coeffs: &[0, 1], genuine: true },
        Divisor { name: "X1+X3", class: "energy_sum", coeffs: &[2, -1], genuine: true },
        Divisor { name: "ell2", class: "signed_energy", coeffs: &[2, -1], genuine: true },
        Divisor { name: "ell3", class: "signed_energy", coeffs: &[0, 1], genuine: true },
        Divisor { name: "A", class: "elliptic_discriminant", coeffs: &[2, -1], genuine: true },
        Divisor { name: "A-B", class: "elliptic_discriminant", coeffs: &[2, -1], genuine: true },
        Divisor { name: "D1", class: "algebraic_kernel", coeffs: &[0, 4, -4, 1], genuine: true },
        Divisor { name: "P6", class: "algebraic_kernel", coeffs: &[4, -4, 1], genuine: true },
        Divisor { name: "other_kernel_y", class: "algebraic_kernel", coeffs: &[-2, 1], genuine: true },
        Divisor { name: "Q", class: "apparent_presentation", coeffs: &[4, -4, 1], genuine: false },
    ]
}

fn main() {
    let args: Vec<String> = env::args().collect();
    if args.len() != 2 {
        eprintln!("usage: et_intersection_census <output.json>");
        std::process::exit(2);
    }
    let ds = divisors();
    let mut rows = Vec::new();
    let mut nonsoft = 0usize;
    for d in &ds {
        let roots = integer_roots(d.coeffs);
        assert!(!roots.is_empty(), "{} has no audited intersection", d.name);
        let soft = roots.iter().all(|r| is_site_soft(*r));
        if d.genuine && !soft {
            nonsoft += 1;
        }
        rows.push(format!(
            "{{\"name\":\"{}\",\"class\":\"{}\",\"genuine\":{},\"roots_v\":{:?},\"all_site_soft\":{}}}",
            d.name, d.class, d.genuine, roots, soft
        ));
    }
    assert_eq!(nonsoft, 0);
    let out = format!(
        "{{\"schema\":\"marici.gm.et_intersection_census.v1\",\"normal\":\"u=ell4=E_T\",\"chart\":\"X1=1; X2=(u+v)/2-1; X3=(u-v)/2\",\"divisors\":[{}],\"genuine_nonsoft_intersections\":0,\"soft_roots_v\":[0,2],\"generic_ET_open\":\"v*(v-2)!=0\",\"Q_status\":\"apparent_and_soft_on_ET\",\"classification\":\"generic E_T nearby cycle plus existing site-soft intersections; no additional nonsoft carrier incidence\"}}",
        rows.join(",")
    );
    fs::write(&args[1], out).expect("write ET intersection census");
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn every_genuine_intersection_is_site_soft() {
        for d in divisors().into_iter().filter(|d| d.genuine) {
            let roots = integer_roots(d.coeffs);
            assert!(!roots.is_empty(), "{}", d.name);
            assert!(roots.into_iter().all(is_site_soft), "{}", d.name);
        }
    }

    #[test]
    fn q_restricts_to_a_soft_square() {
        let q = divisors().into_iter().find(|d| d.name == "Q").unwrap();
        assert_eq!(q.coeffs, &[4, -4, 1]);
        assert_eq!(integer_roots(q.coeffs), vec![2]);
        assert!(!q.genuine);
    }
}
