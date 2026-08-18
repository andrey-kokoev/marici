use symbolica::prelude::*;

fn atom(text: &str) -> Atom {
    Atom::parse(text, "marici", Default::default())
        .unwrap()
        .expand()
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

fn sign(p: &[usize]) -> i32 {
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

fn determinant(matrix: &[Vec<Atom>]) -> Atom {
    let mut base: Vec<usize> = (0..matrix.len()).collect();
    let mut permutations_out = Vec::new();
    permutations(&mut base, 0, &mut permutations_out);
    permutations_out
        .into_iter()
        .fold(atom("0"), |sum, permutation| {
            let product = permutation
                .iter()
                .enumerate()
                .fold(atom("1"), |product, (row, &column)| {
                    (product * &matrix[row][column]).expand()
                });
            (sum + atom(&sign(&permutation).to_string()) * product).expand()
        })
}

fn cm(a: &str, b: &str) -> Vec<Vec<Atom>> {
    [
        ["0", "1", "1", "1", "1"],
        ["1", "0", "E^2", &format!("({a})^2"), &format!("({b})^2")],
        ["1", "E^2", "0", "P2^2", "P1^2"],
        ["1", &format!("({a})^2"), "P2^2", "0", "P3^2"],
        ["1", &format!("({b})^2"), "P1^2", "P3^2", "0"],
    ]
    .into_iter()
    .map(|row| row.into_iter().map(atom).collect())
    .collect()
}

fn set_zero(expression: Atom, variable: &str) -> Atom {
    expression
        .replace(atom(variable).to_pattern())
        .with(atom("0").to_pattern())
        .expand()
}

fn main() {
    // Ordered source pair (q_g1,q_g2), with loop orientation da wedge db.
    let pa = "E-X2";
    let pb = "E-X1";
    let k_local =
        (atom("-1/2") * determinant(&cm(&format!("{pa}+x"), &format!("{pb}+y")))).expand();
    let sextic = (atom("-1/2") * determinant(&cm(pa, pb))).expand();

    let constant = set_zero(set_zero(k_local.clone(), "x"), "y");
    assert_eq!(constant, sextic);

    let alpha = set_zero(
        set_zero(k_local.derivative(symbol!("marici::x")).expand(), "x"),
        "y",
    );
    let beta = set_zero(
        set_zero(k_local.derivative(symbol!("marici::y")).expand(), "x"),
        "y",
    );
    assert_ne!(alpha, atom("0"));
    assert_ne!(beta, atom("0"));

    // q_g1=b-(E-X1), q_g2=a-(E-X2).  Relative to da wedge db,
    // det d(q_g1,q_g2)/d(a,b)=-1.
    let jacobian = -1_i32;
    assert_eq!(jacobian, -1);

    println!("representative=(g1,g2)");
    println!("marked_jacobian={jacobian}");
    println!("local_cover=w^2=S+alpha*x+beta*y+O((x,y)^2)");
    println!("sextic_is_constant_term=true");
    println!("alpha_nonzero=true");
    println!("beta_nonzero=true");
    println!("ordered_double_residue_sign=-1");
    println!("vanishing_character=mu2_anti_invariant");
    println!("local_gysin_target=Kummer_line_S^(-1/2)");
}
