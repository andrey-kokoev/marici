use std::fs;

fn hypergeometric_3f2() -> (f64, usize, f64) {
    let (a1, a2, a3) = (-0.5_f64, 2.0_f64, 5.0_f64);
    let (b1, b2) = (4.0_f64, 7.0_f64);
    let mut term = 1.0_f64;
    let mut sum = term;
    let mut n = 0_usize;
    loop {
        let k = n as f64;
        term *= (a1 + k) * (a2 + k) * (a3 + k)
            / ((b1 + k) * (b2 + k) * (k + 1.0));
        sum += term;
        n += 1;
        if term.abs() < 1.0e-17 || n == 1_000_000 {
            return (sum, n, term);
        }
    }
}

fn midpoint_period(n: usize) -> f64 {
    let step = 1.0 / n as f64;
    let mut sum = 0.0_f64;
    for ix in 0..n {
        let x = (ix as f64 + 0.5) * step;
        let x_weight = x * (1.0 - x);
        for iy in 0..n {
            let y = (iy as f64 + 0.5) * step;
            sum -= x_weight * y.powi(4) * (1.0 - y) * (1.0 - x * y).sqrt();
        }
    }
    sum * step * step
}

fn main() {
    let (series, terms, last_term) = hypergeometric_3f2();
    let hypergeometric_period = -series / 180.0;
    let coarse_n = 800_usize;
    let fine_n = 1600_usize;
    let coarse = midpoint_period(coarse_n);
    let fine = midpoint_period(fine_n);
    let richardson = fine + (fine - coarse) / 3.0;
    let absolute_error = (richardson - hypergeometric_period).abs();
    let tolerance = 2.0e-10_f64;
    assert!(
        absolute_error < tolerance,
        "Euler/hypergeometric mismatch: {absolute_error:e}"
    );

    let json = format!(
        concat!(
            "{{\n",
            "  \"source_chamber\": \"0 < z2 < z3 < 1 with (z1,z4,z5)=(0,1,infinity)\",\n",
            "  \"loading\": {{\"a\": 2.0, \"b\": 0.5, \"c\": 1.0, \"d\": 2.0, \"e\": 2.0}},\n",
            "  \"orientation_sign\": -1,\n",
            "  \"formula\": \"-B(a,e) B(a+c+e,d) 3F2(-b,a,a+c+e; a+e,a+c+e+d; 1)\",\n",
            "  \"beta_product\": 0.005555555555555556,\n",
            "  \"hypergeometric_3f2\": {:.17},\n",
            "  \"hypergeometric_terms\": {},\n",
            "  \"last_series_term\": {:.17e},\n",
            "  \"midpoint_coarse_n\": {},\n",
            "  \"midpoint_coarse\": {:.17},\n",
            "  \"midpoint_fine_n\": {},\n",
            "  \"midpoint_fine\": {:.17},\n",
            "  \"richardson_period\": {:.17},\n",
            "  \"hypergeometric_period\": {:.17},\n",
            "  \"absolute_error\": {:.17e},\n",
            "  \"tolerance\": {:.1e},\n",
            "  \"passed\": true\n",
            "}}\n"
        ),
        series,
        terms,
        last_term,
        coarse_n,
        coarse,
        fine_n,
        fine,
        richardson,
        hypergeometric_period,
        absolute_error,
        tolerance
    );
    let output = "../string-five-point-finite-pt-period.json";
    fs::write(output, &json).expect("write finite-period packet");
    print!("{json}");
}
