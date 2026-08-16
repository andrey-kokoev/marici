mod frozen {
    #![allow(dead_code)]
    include!("check_split_occurrence_weight_zero.rs");

    pub fn primitive_coefficients(x: i128, y: i128, which_31: bool) -> Vec<(i128, i128)> {
        primitive_polynomial(x, y, which_31)
            .1
            .into_iter()
            .map(|q| (q.n, q.d))
            .collect()
    }
}

use std::{env, fs};

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct Q {
    n: i128,
    d: i128,
}

impl Q {
    const Z: Self = Self { n: 0, d: 1 };
    const O: Self = Self { n: 1, d: 1 };

    fn new(mut n: i128, mut d: i128) -> Self {
        assert_ne!(d, 0);
        if d < 0 { n = -n; d = -d; }
        let g = gcd(n.abs(), d.abs());
        Self { n: n / g, d: d / g }
    }
    fn add(self, rhs: Self) -> Self { Self::new(self.n * rhs.d + rhs.n * self.d, self.d * rhs.d) }
    fn neg(self) -> Self { Self::new(-self.n, self.d) }
    fn mul(self, rhs: Self) -> Self { Self::new(self.n * rhs.n, self.d * rhs.d) }
    fn div(self, rhs: Self) -> Self { Self::new(self.n * rhs.d, self.d * rhs.n) }
    fn pow(self, mut k: usize) -> Self {
        let mut a = self;
        let mut z = Self::O;
        while k > 0 {
            if k & 1 == 1 { z = z.mul(a); }
            k >>= 1;
            if k > 0 { a = a.mul(a); }
        }
        z
    }
}

fn gcd(mut a: i128, mut b: i128) -> i128 {
    while b != 0 { (a, b) = (b, a % b); }
    a.max(1)
}

fn coeff(x: i128, y: i128, occurrence_31: bool, degree: usize) -> Q {
    let h = frozen::primitive_coefficients(x, y, occurrence_31);
    let (n, d) = h.get(degree).copied().unwrap_or((0, 1));
    Q::new(n, d)
}

fn scaling_degree(degree: usize) -> i32 {
    // Source dimensional grading: [n^(2j+1)]H has energy degree j+2.
    ((degree + 3) / 2) as i32
}

fn solve(mut a: Vec<Vec<Q>>, vars: usize) -> Option<Vec<Q>> {
    let rows = a.len();
    let mut pivot_row = 0;
    let mut pivots = Vec::new();
    for col in 0..vars {
        let found = (pivot_row..rows).find(|&r| a[r][col] != Q::Z)?;
        a.swap(pivot_row, found);
        let p = a[pivot_row][col];
        for j in col..=vars { a[pivot_row][j] = a[pivot_row][j].div(p); }
        for r in 0..rows {
            if r == pivot_row { continue; }
            let f = a[r][col];
            if f == Q::Z { continue; }
            for j in col..=vars { a[r][j] = a[r][j].add(a[pivot_row][j].mul(f).neg()); }
        }
        pivots.push((pivot_row, col));
        pivot_row += 1;
    }
    for row in pivot_row..rows {
        if (0..vars).all(|c| a[row][c] == Q::Z) && a[row][vars] != Q::Z { return None; }
    }
    let mut out = vec![Q::Z; vars];
    for (r, c) in pivots { out[c] = a[r][vars]; }
    Some(out)
}

// Fit the homogeneous coefficient as y^e f(x/y)=y^e P(t)/Q(t).
// Small coprime pairs avoid i128 overflow in the frozen exact source expansion.
fn rational_interpolate(occurrence_31: bool, degree: usize, homogeneity: i32) -> (Vec<Q>, Vec<Q>, usize) {
    let samples: Vec<(i128, i128)> = vec![
        (1, 2), (1, 3), (2, 3), (2, 5), (3, 4), (3, 5),
        (2, 1), (3, 1), (3, 2), (5, 2), (4, 3), (5, 3),
    ];
    let data: Vec<(Q, Q)> = samples.iter().map(|&(x, y)| {
        let value = coeff(x, y, occurrence_31, degree);
        let normalized = if homogeneity >= 0 {
            value.div(Q::new(y.pow(homogeneity as u32), 1))
        } else {
            value.mul(Q::new(y.pow((-homogeneity) as u32), 1))
        };
        (Q::new(x, y), normalized)
    }).collect();
    for total in 0..=10_usize {
        for qdeg in 0..=total {
            let pdeg = total - qdeg;
            let vars = pdeg + 1 + qdeg;
            if vars + 2 > samples.len() { continue; }
            let mut matrix = Vec::new();
            for &(t, f) in data.iter().take(vars + 1) {
                let mut row = vec![Q::Z; vars + 1];
                for (j, slot) in row.iter_mut().take(pdeg + 1).enumerate() {
                    *slot = t.pow(j).neg();
                }
                for j in 0..qdeg {
                    row[pdeg + 1 + j] = f.mul(t.pow(j));
                }
                row[vars] = f.mul(t.pow(qdeg)).neg();
                matrix.push(row);
            }
            let Some(sol) = solve(matrix, vars) else { continue };
            let p = sol[..=pdeg].to_vec();
            let mut q = sol[pdeg + 1..].to_vec();
            q.push(Q::O);
            let held_out = data.len() - (vars + 1);
            let valid = data.iter().skip(vars + 1).all(|&(t, f)| {
                let eval = |poly: &[Q]| poly.iter().rev().fold(Q::Z, |z, &c| z.mul(t).add(c));
                eval(&p) == f.mul(eval(&q))
            });
            if valid { return (p, q, held_out); }
        }
    }
    panic!("no bounded rational interpolation for occurrence={} n^{}", occurrence_31, degree)
}

fn poly_json(poly: &[Q]) -> String {
    format!("[{}]", poly.iter().map(|q| format!("\"{}/{}\"", q.n, q.d)).collect::<Vec<_>>().join(","))
}

fn main() {
    let output = env::args().nth(1).expect("output path");
    let mut rows = Vec::new();
    let mut scaling_checks = 0_u64;
    let mut interpolation_checks = 0_u64;
    for occurrence_31 in [true, false] {
        for degree in [1_usize, 3, 5, 7, 9] {
            let homogeneity = scaling_degree(degree);
            scaling_checks += 1; // exact source-dimensional grading assignment
            let (p, q, held_out) = rational_interpolate(occurrence_31, degree, homogeneity);
            interpolation_checks += held_out as u64;
            rows.push(format!(
                "    {{\"occurrence\":\"{}\",\"n_degree\":{},\"homogeneity\":{},\"numerator_t_coefficients\":{},\"denominator_t_coefficients\":{}}}",
                if occurrence_31 { "31" } else { "23" }, degree, homogeneity, poly_json(&p), poly_json(&q)
            ));
        }
    }
    let json = format!(
        "{{\n  \"schema\": \"marici.occurrence-jet-connection.v1\",\n  \"source_dimensional_grading_assignments\": {},\n  \"exact_out_of_sample_interpolation_checks\": {},\n  \"coefficient_models\": [\n{}\n  ]\n}}\n",
        scaling_checks, interpolation_checks, rows.join(",\n")
    );
    fs::write(output, json).expect("write certificate");
}
