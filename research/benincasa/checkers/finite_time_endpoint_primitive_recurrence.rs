#[derive(Clone, Copy, Debug, Default)]
struct C { r: f64, i: f64 }

impl C {
    fn new(r: f64, i: f64) -> Self { Self { r, i } }
    fn abs(self) -> f64 { (self.r * self.r + self.i * self.i).sqrt() }
}

impl std::ops::Add for C {
    type Output = Self;
    fn add(self, rhs: Self) -> Self { Self::new(self.r + rhs.r, self.i + rhs.i) }
}
impl std::ops::Sub for C {
    type Output = Self;
    fn sub(self, rhs: Self) -> Self { Self::new(self.r - rhs.r, self.i - rhs.i) }
}
impl std::ops::Mul for C {
    type Output = Self;
    fn mul(self, rhs: Self) -> Self {
        Self::new(self.r * rhs.r - self.i * rhs.i, self.r * rhs.i + self.i * rhs.r)
    }
}
impl std::ops::Mul<f64> for C {
    type Output = Self;
    fn mul(self, rhs: f64) -> Self { Self::new(self.r * rhs, self.i * rhs) }
}
impl std::ops::Div for C {
    type Output = Self;
    fn div(self, rhs: Self) -> Self {
        let d = rhs.r * rhs.r + rhs.i * rhs.i;
        Self::new((self.r * rhs.r + self.i * rhs.i) / d,
                  (self.i * rhs.r - self.r * rhs.i) / d)
    }
}

fn falling(n: i32, length: usize) -> f64 {
    (0..length).map(|j| f64::from(n - j as i32)).product()
}

// Coefficient of t^(n-r) in the endpoint primitive of t^n exp(i omega t).
fn primitive_coefficient(n: i32, r: usize, omega: f64) -> C {
    let sign = if r % 2 == 0 { 1.0 } else { -1.0 };
    C::new(sign * falling(n, r), 0.0)
        / (0..=r).fold(C::new(1.0, 0.0), |z, _| z * C::new(0.0, omega))
}

fn main() {
    let omega = 1.7;
    let truncation = 7usize;
    let mut tests = 0usize;
    for n in -2..=3 {
        let coefficients: Vec<C> = (0..=truncation)
            .map(|r| primitive_coefficient(n, r, omega))
            .collect();
        assert!((C::new(0.0, omega) * coefficients[0] - C::new(1.0, 0.0)).abs() < 1e-13);
        for r in 1..=truncation {
            let cancellation = coefficients[r - 1] * f64::from(n - r as i32 + 1)
                + C::new(0.0, omega) * coefficients[r];
            assert!(cancellation.abs() < 1e-12);
            tests += 1;
        }
        let residual = coefficients[truncation] * f64::from(n - truncation as i32);
        let expected = C::new(
            if truncation % 2 == 0 { 1.0 } else { -1.0 } * falling(n, truncation + 1),
            0.0,
        ) / (0..=truncation).fold(C::new(1.0, 0.0), |z, _| z * C::new(0.0, omega));
        assert!((residual - expected).abs() < 1e-11);
    }
    println!("{{");
    println!("  \"schema\": \"marici.finite_time_endpoint_primitive_recurrence.v1\",");
    println!("  \"powers_tested\": [-2, -1, 0, 1, 2, 3],");
    println!("  \"truncation_order\": {truncation},");
    println!("  \"telescoping_identities_tested\": {tests},");
    println!("  \"recurrence_passes\": true");
    println!("}}");
}
