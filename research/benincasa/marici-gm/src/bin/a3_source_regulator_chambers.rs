#[derive(Clone, Copy, Debug)]
struct C {
    re: f64,
    im: f64,
}

impl std::ops::Add for C {
    type Output = C;
    fn add(self, rhs: C) -> C {
        C {
            re: self.re + rhs.re,
            im: self.im + rhs.im,
        }
    }
}
impl std::ops::Sub for C {
    type Output = C;
    fn sub(self, rhs: C) -> C {
        C {
            re: self.re - rhs.re,
            im: self.im - rhs.im,
        }
    }
}
impl std::ops::Mul for C {
    type Output = C;
    fn mul(self, rhs: C) -> C {
        C {
            re: self.re * rhs.re - self.im * rhs.im,
            im: self.re * rhs.im + self.im * rhs.re,
        }
    }
}

fn scale(x: C, q: f64) -> C {
    C {
        re: q * x.re,
        im: q * x.im,
    }
}
fn norm2(x: C) -> f64 {
    x.re * x.re + x.im * x.im
}

fn regulator_map(p1: f64, p2: f64, eps_e: f64, eps_p1: f64, eps_p3: f64) -> (C, C, C) {
    let e = C { re: p1, im: -eps_e };
    let p1c = C {
        re: p1,
        im: -eps_p1,
    };
    let p3c = C {
        re: 0.0,
        im: -eps_p3,
    };
    let delta = e * e - p1c * p1c;
    let q = p3c * p3c;
    let d = p1 * p1 - p2 * p2;
    let t2 = scale(delta, -d) + scale(q, -2.0 * p1 * p1) - delta * q;
    let t0 = q * (delta * delta + scale(delta, d) + delta * q + scale(q, p1 * p1));
    (t0, C { re: 0.0, im: 0.0 }, t2)
}

fn discriminant(p1: f64, t0: C, t2: C) -> C {
    let bracket = t2 * t2 - scale(t0, 4.0 * p1 * p1);
    t0 * bracket * bracket
}

fn main() {
    let p1 = 3.0;
    let p2 = 2.0;
    let plus = regulator_map(p1, p2, 0.02, 0.01, 0.005);
    let minus = regulator_map(p1, p2, 0.01, 0.02, 0.005);
    assert_eq!(plus.1.re, 0.0);
    assert_eq!(plus.1.im, 0.0);
    assert!(plus.2.im > 0.0);
    assert!(minus.2.im < 0.0);
    assert!(norm2(discriminant(p1, plus.0, plus.2)) > 1e-30);
    assert!(norm2(discriminant(p1, minus.0, minus.2)) > 1e-30);

    println!("J_t1=0");
    println!("J_t2=-d*delta-2*P1^2*q-delta*q");
    println!("J_t0=q*(delta^2+d*delta+delta*q+P1^2*q)");
    println!("delta=(P1-i*epsE)^2-(P1-i*epsP1)^2");
    println!("q=(-i*epsP3)^2");
    println!("positive_assignment_1_t2_im_sign=+");
    println!("positive_assignment_2_t2_im_sign=-");
    println!("both_assignments_off_discriminant=true");
    println!("unique_braid_chamber=false");
    println!("mixed_coherence_test=unauthorized_without_chamber");
}
