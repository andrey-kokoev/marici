//! Analytic second-jet QMC for the complete six-simplex relative source.

use std::f64::consts::PI;
use std::ops::{Add, Div, Mul, Neg, Sub};

#[derive(Clone, Copy)]
struct J {
    v: f64,
    d: f64,
    d2: f64,
}

impl J {
    fn c(v: f64) -> Self {
        Self { v, d: 0.0, d2: 0.0 }
    }
    fn t(v: f64, d: f64) -> Self {
        Self { v, d, d2: 0.0 }
    }
    fn inv(self) -> Self {
        Self {
            v: 1.0 / self.v,
            d: -self.d / self.v.powi(2),
            d2: 2.0 * self.d.powi(2) / self.v.powi(3) - self.d2 / self.v.powi(2),
        }
    }
    fn sqrt(self) -> Self {
        let root = self.v.sqrt();
        Self {
            v: root,
            d: self.d / (2.0 * root),
            d2: self.d2 / (2.0 * root) - self.d.powi(2) / (4.0 * root.powi(3)),
        }
    }
}

impl Add for J {
    type Output = Self;
    fn add(self, rhs: Self) -> Self {
        Self {
            v: self.v + rhs.v,
            d: self.d + rhs.d,
            d2: self.d2 + rhs.d2,
        }
    }
}
impl Sub for J {
    type Output = Self;
    fn sub(self, rhs: Self) -> Self {
        self + (-rhs)
    }
}
impl Neg for J {
    type Output = Self;
    fn neg(self) -> Self {
        Self {
            v: -self.v,
            d: -self.d,
            d2: -self.d2,
        }
    }
}
impl Mul for J {
    type Output = Self;
    fn mul(self, rhs: Self) -> Self {
        Self {
            v: self.v * rhs.v,
            d: self.d * rhs.v + self.v * rhs.d,
            d2: self.d2 * rhs.v + 2.0 * self.d * rhs.d + self.v * rhs.d2,
        }
    }
}
impl Div for J {
    type Output = Self;
    fn div(self, rhs: Self) -> Self {
        self * rhs.inv()
    }
}

fn halton(mut i: u64, base: u64) -> f64 {
    let (mut f, mut x) = (1.0, 0.0);
    while i > 0 {
        f /= base as f64;
        x += f * (i % base) as f64;
        i /= base;
    }
    x
}

fn jnorm(v: [J; 3]) -> J {
    (v[0] * v[0] + v[1] * v[1] + v[2] * v[2]).sqrt()
}

fn density(l: [f64; 3]) -> J {
    density_routed(l, 0)
}

fn density_routed(l: [f64; 3], route: u8) -> J {
    let (one, two) = (J::c(1.0), J::c(2.0));
    let x1 = J::t(1.0, 1.0);
    let x2 = J::t(1.0, -1.0);
    let x3 = one;
    let e = x1 + x2 + x3;
    let cos12 = (x3 * x3 - x1 * x1 - x2 * x2) / (two * x1 * x2);
    let sin12 = (one - cos12 * cos12).sqrt();
    let p1 = [x1, J::c(0.0), J::c(0.0)];
    let p2 = [x2 * cos12, x2 * sin12, J::c(0.0)];
    let mut lj = [J::c(l[0]), J::c(l[1]), J::c(l[2])];
    if route >= 1 {
        for i in 0..3 {
            lj[i] = lj[i] + p1[i];
        }
    }
    if route >= 2 {
        for i in 0..3 {
            lj[i] = lj[i] + p2[i];
        }
    }
    let y12 = jnorm(lj);
    let y23 = jnorm([lj[0] + p1[0], lj[1] + p1[1], lj[2]]);
    let y31 = jnorm([lj[0] + p1[0] + p2[0], lj[1] + p2[1], lj[2]]);
    let g1 = y31 + x1 + y12;
    let g2 = y12 + x2 + y23;
    let g3 = y23 + x3 + y31;
    let b12 = e + y12;
    let b23 = e + y23;
    let b31 = e + y31;
    let s12 = x1 + x2 + y23 + y31;
    let s23 = x2 + x3 + y31 + y12;
    let s31 = x3 + x1 + y12 + y23;
    let six = b12.inv() * (s23.inv() + s31.inv())
        + b23.inv() * (s31.inv() + s12.inv())
        + b31.inv() * (s12.inv() + s23.inv());
    six / (e * g1 * g2 * g3)
}

fn main() {
    if std::env::var("MODE").ok().as_deref() == Some("routing_scan") {
        routing_scan();
        return;
    }
    if std::env::var("MODE").ok().as_deref() == Some("inversion_scan") {
        inversion_scan();
        return;
    }
    if std::env::var("MODE").ok().as_deref() == Some("radial_scan") {
        radial_scan();
        return;
    }
    let n: u64 = std::env::var("SAMPLES")
        .ok()
        .and_then(|x| x.parse().ok())
        .unwrap_or(4_000_000);
    let skip: u64 = std::env::var("HALTON_SKIP")
        .ok()
        .and_then(|x| x.parse().ok())
        .unwrap_or(0);
    let (mut value, mut first, mut second) = (0.0, 0.0, 0.0);
    let (mut positive, mut negative, mut positive_count) = (0.0, 0.0, 0_u64);
    for i in 1..=n {
        let k = i + skip;
        let u = halton(k, 2);
        let z = 2.0 * halton(k, 3) - 1.0;
        let phi = 2.0 * PI * halton(k, 5);
        let r = u / (1.0 - u);
        let s = (1.0 - z * z).sqrt();
        let jet = density([r * s * phi.cos(), r * s * phi.sin(), r * z]);
        let jac = 4.0 * PI * r * r / (1.0 - u).powi(2);
        value += jac * jet.v;
        first += jac * jet.d;
        second += jac * jet.d2;
        if jet.d2 >= 0.0 {
            positive += jac * jet.d2;
            positive_count += 1;
        } else {
            negative += jac * jet.d2;
        }
    }
    let scale = 1.0 / n as f64;
    println!("{{\"schema\":\"marici.physical-relative-shape-jet-qmc.v1\",\"samples\":{n},\"skip\":{skip},\"value\":{:.17},\"first\":{:.17},\"second\":{:.17},\"positive_part\":{:.17},\"negative_part\":{:.17},\"positive_fraction\":{:.17}}}", value*scale, first*scale, second*scale, positive*scale, negative*scale, positive_count as f64*scale);
}

fn routing_scan() {
    let n: u64 = std::env::var("SAMPLES")
        .ok()
        .and_then(|x| x.parse().ok())
        .unwrap_or(8_000_000);
    let skip: u64 = std::env::var("HALTON_SKIP")
        .ok()
        .and_then(|x| x.parse().ok())
        .unwrap_or(0);
    let (mut total, mut positive, mut negative, mut positive_count) = (0.0, 0.0, 0.0, 0_u64);
    for i in 1..=n {
        let k = i + skip;
        let u = halton(k, 2);
        let z = 2.0 * halton(k, 3) - 1.0;
        let phi = 2.0 * PI * halton(k, 5);
        let r = u / (1.0 - u);
        let s = (1.0 - z * z).sqrt();
        let l = [r * s * phi.cos(), r * s * phi.sin(), r * z];
        let d2 =
            (density_routed(l, 0).d2 + density_routed(l, 1).d2 + density_routed(l, 2).d2) / 3.0;
        let weighted = 4.0 * PI * r * r / (1.0 - u).powi(2) * d2;
        total += weighted;
        if d2 >= 0.0 {
            positive += weighted;
            positive_count += 1;
        } else {
            negative += weighted;
        }
    }
    let scale = 1.0 / n as f64;
    println!("{{\"schema\":\"marici.physical-relative-shape-routing-scan.v1\",\"samples\":{n},\"skip\":{skip},\"second\":{},\"positive_part\":{},\"negative_part\":{},\"positive_fraction\":{}}}", total * scale, positive * scale, negative * scale, positive_count as f64 * scale);
}

fn angular_average(r: f64, angular: u64) -> f64 {
    let golden = PI * (3.0 - 5.0_f64.sqrt());
    let mut average = 0.0;
    for j in 0..angular {
        let z = 1.0 - 2.0 * (j as f64 + 0.5) / angular as f64;
        let phi = golden * j as f64;
        let s = (1.0 - z * z).sqrt();
        average += density([r * s * phi.cos(), r * s * phi.sin(), r * z]).d2;
    }
    average / angular as f64
}

fn inversion_scan() {
    let angular: u64 = std::env::var("ANGULAR_SAMPLES")
        .ok()
        .and_then(|x| x.parse().ok())
        .unwrap_or(200_000);
    let points: u32 = std::env::var("RADIAL_POINTS")
        .ok()
        .and_then(|x| x.parse().ok())
        .unwrap_or(161);
    let mut negative = Vec::new();
    let mut minimum = (f64::INFINITY, 0.0);
    for k in 0..points {
        let r = 10.0_f64.powf(-6.0 + 6.0 * k as f64 / (points - 1) as f64);
        let paired =
            r * r * angular_average(r, angular) + angular_average(1.0 / r, angular) / r.powi(4);
        if paired < minimum.0 {
            minimum = (paired, r);
        }
        if paired < 0.0 {
            negative.push((r, paired));
        }
    }
    let neg = negative
        .iter()
        .map(|(r, p)| format!("[{},{}]", r, p))
        .collect::<Vec<_>>()
        .join(",");
    println!("{{\"schema\":\"marici.physical-relative-shape-inversion-scan.v1\",\"angular_samples\":{angular},\"radial_points\":{points},\"negative_count\":{},\"minimum\":{},\"minimum_radius\":{},\"negative\":[{}]}}", negative.len(), minimum.0, minimum.1, neg);
}

fn radial_scan() {
    let angular: u64 = std::env::var("ANGULAR_SAMPLES")
        .ok()
        .and_then(|x| x.parse().ok())
        .unwrap_or(100_000);
    let radial_points: u32 = std::env::var("RADIAL_POINTS")
        .ok()
        .and_then(|x| x.parse().ok())
        .unwrap_or(161);
    let golden = PI * (3.0 - 5.0_f64.sqrt());
    let mut negative = Vec::new();
    let mut minimum = (f64::INFINITY, 0.0);
    let mut selected = Vec::new();
    for k in 0..radial_points {
        let exponent = -6.0 + 12.0 * k as f64 / (radial_points - 1) as f64;
        let r = 10.0_f64.powf(exponent);
        let mut average = 0.0;
        for j in 0..angular {
            let z = 1.0 - 2.0 * (j as f64 + 0.5) / angular as f64;
            let phi = golden * j as f64;
            let s = (1.0 - z * z).sqrt();
            average += density([r * s * phi.cos(), r * s * phi.sin(), r * z]).d2;
        }
        average /= angular as f64;
        if average < minimum.0 {
            minimum = (average, r);
        }
        if average < 0.0 {
            negative.push((r, average));
        }
        if k % 20 == 0 || k + 1 == radial_points {
            selected.push((r, average));
        }
    }
    let selected_json = selected
        .iter()
        .map(|(r, a)| format!("[{},{}]", r, a))
        .collect::<Vec<_>>()
        .join(",");
    let negative_json = negative
        .iter()
        .map(|(r, a)| format!("[{},{}]", r, a))
        .collect::<Vec<_>>()
        .join(",");
    println!(
        "{{\"schema\":\"marici.physical-relative-shape-radial-scan.v1\",\"angular_samples\":{angular},\"radial_points\":{radial_points},\"negative_radius_count\":{},\"minimum_average\":{},\"minimum_radius\":{},\"negative\":[{}],\"selected\":[{}]}}",
        negative.len(), minimum.0, minimum.1, negative_json, selected_json
    );
}
