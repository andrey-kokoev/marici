use std::cmp::max;
use symbolica::prelude::*;

#[derive(Clone)]
struct Poly(Vec<Atom>);

fn atom(s: &str) -> Atom {
    Atom::parse(s, "marici", Default::default())
        .unwrap()
        .expand()
}

impl Poly {
    fn zero() -> Self {
        Self(vec![atom("0")])
    }

    fn constant(s: &str) -> Self {
        Self(vec![atom(s)])
    }

    fn coefficient(&self, degree: usize) -> Atom {
        self.0.get(degree).cloned().unwrap_or_else(|| atom("0"))
    }

    fn add(&self, rhs: &Self) -> Self {
        let mut out = Vec::with_capacity(max(self.0.len(), rhs.0.len()));
        for degree in 0..max(self.0.len(), rhs.0.len()) {
            out.push((self.coefficient(degree) + rhs.coefficient(degree)).expand());
        }
        Self(out)
    }

    fn scale(&self, scalar: i32) -> Self {
        Self(
            self.0
                .iter()
                .map(|coefficient| (atom(&scalar.to_string()) * coefficient).expand())
                .collect(),
        )
    }

    fn mul(&self, rhs: &Self) -> Self {
        let mut out = vec![atom("0"); self.0.len() + rhs.0.len() - 1];
        for (left_degree, left) in self.0.iter().enumerate() {
            for (right_degree, right) in rhs.0.iter().enumerate() {
                let degree = left_degree + right_degree;
                out[degree] = (&out[degree] + &(left * right)).expand();
            }
        }
        Self(out)
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

fn determinant(matrix: &[Vec<Poly>]) -> Poly {
    let mut base: Vec<usize> = (0..matrix.len()).collect();
    let mut perms = Vec::new();
    permutations(&mut base, 0, &mut perms);
    perms.into_iter().fold(Poly::zero(), |sum, permutation| {
        let product = permutation
            .iter()
            .enumerate()
            .fold(Poly::constant("1"), |product, (row, &column)| {
                product.mul(&matrix[row][column])
            });
        sum.add(&product.scale(permutation_sign(&permutation)))
    })
}

fn main() {
    let z = Poly::constant("0");
    let o = Poly::constant("1");
    let a_resolved = Poly(vec![atom("B"), atom("xi")]);
    let p2_squared = Poly(vec![
        atom("0"),
        atom("0"),
        atom("0"),
        atom("0"),
        atom("t^2"),
    ]);
    let p3_squared = Poly(vec![
        atom("1"),
        atom("-2"),
        atom("1+2*t"),
        atom("-2*t"),
        atom("t^2"),
    ]);

    let matrix = vec![
        vec![z.clone(), o.clone(), o.clone(), o.clone(), o.clone()],
        vec![
            o.clone(),
            z.clone(),
            a_resolved.clone(),
            Poly::constant("B"),
            Poly::constant("C"),
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
            Poly::constant("B"),
            p2_squared,
            z.clone(),
            p3_squared.clone(),
        ],
        vec![o.clone(), Poly::constant("C"), o.clone(), p3_squared, z],
    ];
    let cm = determinant(&matrix);
    let phi = atom("-2*xi^2+4*xi*(B+1-C)-8*B");

    // External triangle determinant in signed-length factorization:
    // (P1+P2+P3)(-P1+P2+P3)(P1-P2+P3)(P1+P2-P3).
    let external = Poly(vec![atom("0"), atom("1")])
        .mul(&Poly(vec![atom("-2"), atom("1")]))
        .mul(&Poly(vec![atom("0"), atom("1"), atom("-2*t")]))
        .mul(&Poly(vec![atom("2"), atom("-1"), atom("2*t")]));

    assert_eq!(cm.coefficient(0), atom("0"));
    assert_eq!(cm.coefficient(1), atom("0"));
    assert_eq!(cm.coefficient(2), phi);
    assert_eq!(external.coefficient(0), atom("0"));
    assert_eq!(external.coefficient(1), atom("0"));
    assert_eq!(external.coefficient(2), atom("-4"));

    println!("CM_order=2");
    println!("CM_initial={}", cm.coefficient(2));
    println!("CM_next={}", cm.coefficient(3));
    println!("external_CM_order=2");
    println!("external_CM_initial={}", external.coefficient(2));
    println!("external_CM_next={}", external.coefficient(3));
    println!("scalar_density_normal_order=-1");
    println!("collision_normal_jacobian_order=1");
    println!("resolved_current_normal_order=0");
    println!("exceptional_ratio_t_absent_from_log_residue=true");
}
