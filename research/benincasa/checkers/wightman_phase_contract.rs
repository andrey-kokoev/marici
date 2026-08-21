#[derive(Clone, Copy, Debug)]
struct Complex {
    re: f64,
    im: f64,
}

impl Complex {
    fn new(re: f64, im: f64) -> Self {
        Self { re, im }
    }
    fn conj(self) -> Self {
        Self::new(self.re, -self.im)
    }
    fn norm2(self) -> f64 {
        self.re * self.re + self.im * self.im
    }
}

impl std::ops::Add for Complex {
    type Output = Self;
    fn add(self, rhs: Self) -> Self {
        Self::new(self.re + rhs.re, self.im + rhs.im)
    }
}
impl std::ops::Sub for Complex {
    type Output = Self;
    fn sub(self, rhs: Self) -> Self {
        Self::new(self.re - rhs.re, self.im - rhs.im)
    }
}
impl std::ops::Mul for Complex {
    type Output = Self;
    fn mul(self, rhs: Self) -> Self {
        Self::new(
            self.re * rhs.re - self.im * rhs.im,
            self.re * rhs.im + self.im * rhs.re,
        )
    }
}

fn phase(angle: f64) -> Complex {
    Complex::new(angle.cos(), angle.sin())
}

fn greater(k: f64, eta: f64, eta_prime: f64) -> Complex {
    Complex::new(1.0, k * eta)
        * Complex::new(1.0, -k * eta_prime)
        * phase(-k * (eta - eta_prime))
}

fn lesser_hermitian(k: f64, eta: f64, eta_prime: f64) -> Complex {
    Complex::new(1.0, -k * eta)
        * Complex::new(1.0, k * eta_prime)
        * phase(k * (eta - eta_prime))
}

fn lesser_literal_tex(k: f64, eta: f64, eta_prime: f64) -> Complex {
    Complex::new(1.0, -k * eta)
        * Complex::new(1.0, k * eta_prime)
        * phase(-k * (eta - eta_prime))
}

fn main() {
    let samples = [(2.0, -1.25, -0.4), (3.0, -0.7, -0.2), (5.0, -1.1, -0.3)];
    let mut minimum_literal_defect = f64::INFINITY;
    for (k, eta, eta_prime) in samples {
        let target = greater(k, eta, eta_prime).conj();
        let hermitian_defect = (lesser_hermitian(k, eta, eta_prime) - target).norm2();
        let literal_defect = (lesser_literal_tex(k, eta, eta_prime) - target).norm2();
        assert!(hermitian_defect < 1e-26);
        assert!(literal_defect > 1e-8);
        minimum_literal_defect = minimum_literal_defect.min(literal_defect);
    }
    println!("{{");
    println!("  \"schema\": \"marici.wightman_phase_contract.v1\",");
    println!("  \"sample_count\": 3,");
    println!("  \"hermitian_mode_conjugation\": true,");
    println!("  \"literal_tex_mode_conjugation\": false,");
    println!("  \"minimum_literal_defect_norm2\": {minimum_literal_defect:.15e}");
    println!("}}");
}

