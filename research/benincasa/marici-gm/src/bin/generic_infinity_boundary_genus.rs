use std::collections::BTreeMap;
use symbolica::prelude::*;

#[derive(Clone)]
struct Laurent(BTreeMap<i32, Atom>);

fn atom(s: &str) -> Atom {
    Atom::parse(s, "marici", Default::default())
        .unwrap()
        .expand()
}

impl Laurent {
    fn zero() -> Self {
        Self(BTreeMap::new())
    }

    fn monomial(power: i32, coefficient: &str) -> Self {
        let mut terms = BTreeMap::new();
        terms.insert(power, atom(coefficient));
        Self(terms)
    }

    fn add(&self, rhs: &Self) -> Self {
        let mut out = self.0.clone();
        for (&power, coefficient) in &rhs.0 {
            let updated =
                (out.get(&power).cloned().unwrap_or_else(|| atom("0")) + coefficient).expand();
            if updated == atom("0") {
                out.remove(&power);
            } else {
                out.insert(power, updated);
            }
        }
        Self(out)
    }

    fn scale(&self, scalar: i32) -> Self {
        let scalar = atom(&scalar.to_string());
        Self(
            self.0
                .iter()
                .map(|(&power, coefficient)| (power, (&scalar * coefficient).expand()))
                .collect(),
        )
    }

    fn mul(&self, rhs: &Self) -> Self {
        let mut out = Self::zero();
        for (&left_power, left) in &self.0 {
            for (&right_power, right) in &rhs.0 {
                out = out.add(&Self::monomial(
                    left_power + right_power,
                    &(left * right).expand().to_string(),
                ));
            }
        }
        out
    }

    fn coefficient(&self, power: i32) -> Atom {
        self.0.get(&power).cloned().unwrap_or_else(|| atom("0"))
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

fn determinant(matrix: &[Vec<Laurent>]) -> Laurent {
    let mut base: Vec<usize> = (0..matrix.len()).collect();
    let mut perms = Vec::new();
    permutations(&mut base, 0, &mut perms);
    perms.into_iter().fold(Laurent::zero(), |sum, permutation| {
        let product = permutation
            .iter()
            .enumerate()
            .fold(Laurent::monomial(0, "1"), |product, (row, &column)| {
                product.mul(&matrix[row][column])
            });
        sum.add(&product.scale(permutation_sign(&permutation)))
    })
}

fn main() {
    // Generic q_G12 residue: c=-E, while P1,P2,P3 remain independent of
    // the site energies. Infinity chart b=1/s, a=t/s.
    let z = Laurent::monomial(0, "0");
    let o = Laurent::monomial(0, "1");
    let matrix = vec![
        vec![z.clone(), o.clone(), o.clone(), o.clone(), o.clone()],
        vec![
            o.clone(),
            z.clone(),
            Laurent::monomial(0, "E^2"),
            Laurent::monomial(-2, "t^2"),
            Laurent::monomial(-2, "1"),
        ],
        vec![
            o.clone(),
            Laurent::monomial(0, "E^2"),
            z.clone(),
            Laurent::monomial(0, "P2^2"),
            Laurent::monomial(0, "P1^2"),
        ],
        vec![
            o.clone(),
            Laurent::monomial(-2, "t^2"),
            Laurent::monomial(0, "P2^2"),
            z.clone(),
            Laurent::monomial(0, "P3^2"),
        ],
        vec![
            o,
            Laurent::monomial(-2, "1"),
            Laurent::monomial(0, "P1^2"),
            Laurent::monomial(0, "P3^2"),
            z,
        ],
    ];

    let determinant = determinant(&matrix);
    let boundary = determinant.coefficient(-4);
    let h = atom("P1^2+P2^2-P3^2");
    let normalized = atom("P1^2*t^4-(P1^2+P2^2-P3^2)*t^2+P2^2");
    assert_eq!(boundary, (atom("-2") * normalized.clone()).expand());

    let triangle = atom("(P1+P2+P3)*(P1+P2-P3)*(P1-P2+P3)*(P1-P2-P3)");
    assert_eq!((h.clone() * h - atom("4*P1^2*P2^2")).expand(), triangle);
    let discriminant = atom("16*P1^2*P2^2") * triangle.clone() * triangle.clone();

    println!("raw_CM_boundary={boundary}");
    println!("source_normalized_boundary={normalized}");
    println!("site_energy_E_present=false");
    println!("generic_boundary_degree=4");
    println!("generic_boundary_genus=1");
    println!("triangle_factor={triangle}");
    println!("quartic_discriminant={}", discriminant.expand());
    println!("new_branch_support=false");
}
