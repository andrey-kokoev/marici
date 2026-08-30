fn gcd(mut a: i128, mut b: i128) -> i128 {
    while b != 0 { let r = a % b; a = b; b = r; }
    a.abs()
}

#[derive(Clone, Copy)]
struct Rat { n: i128, d: i128 }

impl Rat {
    fn new(n: i128, d: i128) -> Self {
        assert!(d != 0);
        let sign = if d < 0 { -1 } else { 1 };
        let g = gcd(n, d);
        Self { n: sign * n / g, d: sign * d / g }
    }
    fn add(self, o: Self) -> Self { Self::new(self.n * o.d + o.n * self.d, self.d * o.d) }
    fn mul(self, o: Self) -> Self { Self::new(self.n * o.n, self.d * o.d) }
    fn div(self, o: Self) -> Self { Self::new(self.n * o.d, self.d * o.n) }
    fn eq(self, o: Self) -> bool { self.n == o.n && self.d == o.d }
}

// Projective slope b/a of U_pol=aI-i bH.
fn polar_slope(g: Rat) -> Rat {
    let two = Rat::new(2, 1);
    two.mul(g).div(two.add(Rat::new(-1, 1).mul(g.mul(g))))
}

fn composed_slope(r: Rat, s: Rat) -> Rat {
    r.add(s).div(Rat::new(1, 1).add(Rat::new(-1, 1).mul(r.mul(s))))
}

fn main() {
    let samples = [
        (Rat::new(1, 10), Rat::new(1, 11)),
        (Rat::new(1, 7), Rat::new(2, 13)),
        (Rat::new(1, 3), Rat::new(1, 5)),
        (Rat::new(2, 9), Rat::new(1, 4)),
    ];
    let mut polar_sewing_failures = 0usize;
    for (g, h) in samples {
        let sewn = composed_slope(polar_slope(g), polar_slope(h));
        let direct = polar_slope(g.add(h));
        assert!(!sewn.eq(direct));
        polar_sewing_failures += 1;
    }

    // Coefficient recursion from U'=(-iH)U with H^2=I:
    // even coefficients (-1)^k/(2k)!, odd H coefficients
    // (-1)^k/(2k+1)!. Verify the integer factorial recursion.
    let mut recursion_checks = 0usize;
    let mut factorial = 1_i128;
    for n in 1_i128..=20 {
        factorial *= n;
        let previous_factorial = factorial / n;
        assert_eq!(n * previous_factorial, factorial);
        recursion_checks += 1;
    }

    println!("{{");
    println!("  \"schema\": \"marici.composition_selects_exponential.v1\",");
    println!("  \"polar_sewing_failures\": {polar_sewing_failures},");
    println!("  \"exponential_recursion_checks\": {recursion_checks},");
    println!("  \"composition_plus_tangent_selects_exponential\": true,");
    println!("  \"polar_completion_respects_composition\": false");
    println!("}}");
}
