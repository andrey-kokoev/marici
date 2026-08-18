use std::cmp::max;
use symbolica::prelude::*;

#[derive(Clone)]
struct BiPoly(Vec<Vec<Atom>>);

fn atom(s: &str) -> Atom {
    Atom::parse(s, "marici", Default::default())
        .unwrap()
        .expand()
}

impl BiPoly {
    fn zero() -> Self {
        Self(vec![vec![atom("0")]])
    }

    fn constant(s: &str) -> Self {
        Self(vec![vec![atom(s)]])
    }

    fn from_terms(terms: &[(usize, usize, &str)]) -> Self {
        let max_u = terms.iter().map(|term| term.0).max().unwrap_or(0);
        let max_t = terms.iter().map(|term| term.1).max().unwrap_or(0);
        let mut out = vec![vec![atom("0"); max_t + 1]; max_u + 1];
        for &(u_degree, t_degree, coefficient) in terms {
            out[u_degree][t_degree] = (&out[u_degree][t_degree] + &atom(coefficient)).expand();
        }
        Self(out)
    }

    fn coefficient(&self, u_degree: usize, t_degree: usize) -> Atom {
        self.0
            .get(u_degree)
            .and_then(|row| row.get(t_degree))
            .cloned()
            .unwrap_or_else(|| atom("0"))
    }

    fn add(&self, rhs: &Self) -> Self {
        let max_u = max(self.0.len(), rhs.0.len());
        let max_t = max(
            self.0.iter().map(Vec::len).max().unwrap_or(1),
            rhs.0.iter().map(Vec::len).max().unwrap_or(1),
        );
        let mut out = vec![vec![atom("0"); max_t]; max_u];
        for (u_degree, row) in out.iter_mut().enumerate() {
            for (t_degree, entry) in row.iter_mut().enumerate() {
                *entry = (self.coefficient(u_degree, t_degree)
                    + rhs.coefficient(u_degree, t_degree))
                .expand();
            }
        }
        Self(out)
    }

    fn scale(&self, scalar: i32) -> Self {
        let scalar = atom(&scalar.to_string());
        Self(
            self.0
                .iter()
                .map(|row| row.iter().map(|entry| (&scalar * entry).expand()).collect())
                .collect(),
        )
    }

    fn mul(&self, rhs: &Self) -> Self {
        let self_t = self.0.iter().map(Vec::len).max().unwrap_or(1);
        let rhs_t = rhs.0.iter().map(Vec::len).max().unwrap_or(1);
        let mut out = vec![vec![atom("0"); self_t + rhs_t - 1]; self.0.len() + rhs.0.len() - 1];
        for (left_u, left_row) in self.0.iter().enumerate() {
            for (left_t, left) in left_row.iter().enumerate() {
                for (right_u, right_row) in rhs.0.iter().enumerate() {
                    for (right_t, right) in right_row.iter().enumerate() {
                        let target = &mut out[left_u + right_u][left_t + right_t];
                        *target = (&*target + &(left * right)).expand();
                    }
                }
            }
        }
        Self(out)
    }

    fn leading_u(&self) -> Option<(usize, Vec<Atom>)> {
        self.0.iter().enumerate().find_map(|(degree, row)| {
            if row.iter().any(|entry| *entry != atom("0")) {
                Some((degree, row.clone()))
            } else {
                None
            }
        })
    }
}

fn permutation_sign(p: &[usize]) -> i32 {
    let inversions = (0..p.len())
        .flat_map(|i| ((i + 1)..p.len()).map(move |j| (i, j)))
        .filter(|&(i, j)| p[i] > p[j])
        .count();
    if inversions % 2 == 0 {
        1
    } else {
        -1
    }
}

fn permutations(values: &mut [usize], start: usize, out: &mut Vec<Vec<usize>>) {
    if start == values.len() {
        out.push(values.to_vec());
        return;
    }
    for index in start..values.len() {
        values.swap(start, index);
        permutations(values, start + 1, out);
        values.swap(start, index);
    }
}

fn determinant(matrix: &[Vec<BiPoly>]) -> BiPoly {
    let mut base: Vec<usize> = (0..matrix.len()).collect();
    let mut perms = Vec::new();
    permutations(&mut base, 0, &mut perms);
    perms.into_iter().fold(BiPoly::zero(), |sum, permutation| {
        let product = permutation
            .iter()
            .enumerate()
            .fold(BiPoly::constant("1"), |product, (row, &column)| {
                product.mul(&matrix[row][column])
            });
        sum.add(&product.scale(permutation_sign(&permutation)))
    })
}

fn subsets_of_size(size: usize, selected: usize) -> Vec<Vec<usize>> {
    (1usize..(1usize << size))
        .filter(|mask| mask.count_ones() as usize == selected)
        .map(|mask| (0..size).filter(|index| mask & (1 << index) != 0).collect())
        .collect()
}

fn evaluate_t(row: &[Atom], value: i32) -> Atom {
    row.iter()
        .enumerate()
        .fold(atom("0"), |sum, (degree, coefficient)| {
            let scalar = value.pow(degree as u32);
            (sum + atom(&scalar.to_string()) * coefficient).expand()
        })
}

fn format_t_polynomial(row: &[Atom]) -> Atom {
    row.iter()
        .enumerate()
        .fold(atom("0"), |sum, (degree, coefficient)| {
            (sum + coefficient * atom(&format!("T^{degree}"))).expand()
        })
}

fn main() {
    let z = BiPoly::constant("0");
    let o = BiPoly::constant("1");
    let a_resolved = BiPoly::from_terms(&[(0, 0, "B"), (1, 0, "xi")]);
    let p2_squared = BiPoly::from_terms(&[(4, 2, "1")]);
    let p3_squared = BiPoly::from_terms(&[
        (0, 0, "1"),
        (1, 0, "-2"),
        (2, 0, "1"),
        (2, 1, "2"),
        (3, 1, "-2"),
        (4, 2, "1"),
    ]);
    let matrix = vec![
        vec![z.clone(), o.clone(), o.clone(), o.clone(), o.clone()],
        vec![
            o.clone(),
            z.clone(),
            a_resolved.clone(),
            BiPoly::constant("B"),
            BiPoly::constant("C"),
        ],
        vec![
            o.clone(),
            a_resolved,
            z.clone(),
            p2_squared.clone(),
            o.clone(),
        ],
        vec![
            o.clone(),
            BiPoly::constant("B"),
            p2_squared,
            z.clone(),
            p3_squared.clone(),
        ],
        vec![o.clone(), BiPoly::constant("C"), o.clone(), p3_squared, z],
    ];

    let zero = atom("0");
    let mut audited = 0usize;
    let mut identically_zero = 0usize;
    let mut degenerate_plus = 0usize;
    let mut degenerate_minus = 0usize;
    for minor_size in 3..=matrix.len() {
        for rows in subsets_of_size(matrix.len(), minor_size) {
            for columns in subsets_of_size(matrix.len(), minor_size) {
                let minor: Vec<Vec<BiPoly>> = rows
                    .iter()
                    .map(|&row| {
                        columns
                            .iter()
                            .map(|&column| matrix[row][column].clone())
                            .collect()
                    })
                    .collect();
                let determinant = determinant(&minor);
                let Some((order, initial)) = determinant.leading_u() else {
                    identically_zero += 1;
                    println!("identically_zero;rows={rows:?};columns={columns:?}");
                    continue;
                };
                let at_plus = evaluate_t(&initial, 1);
                let at_minus = evaluate_t(&initial, -1);
                if at_plus == zero {
                    degenerate_plus += 1;
                    println!(
                        "degenerate_plus;rows={rows:?};columns={columns:?};order={order};initial={}",
                        format_t_polynomial(&initial)
                    );
                }
                if at_minus == zero {
                    degenerate_minus += 1;
                    println!(
                        "degenerate_minus;rows={rows:?};columns={columns:?};order={order};initial={}",
                        format_t_polynomial(&initial)
                    );
                }
                audited += 1;
            }
        }
    }
    println!("source_boundary_minors_nonzero={audited}");
    println!("source_boundary_minors_identically_zero={identically_zero}");
    println!("degenerate_at_t_plus={degenerate_plus}");
    println!("degenerate_at_t_minus={degenerate_minus}");
}
