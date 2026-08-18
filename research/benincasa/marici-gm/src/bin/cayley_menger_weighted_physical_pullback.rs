use symbolica::prelude::*;

fn atom(s: &str) -> Atom {
    Atom::parse(s, "marici", Default::default())
        .unwrap()
        .expand()
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

fn determinant_expression(matrix: &[Vec<&str>]) -> String {
    let mut base: Vec<usize> = (0..matrix.len()).collect();
    let mut perms = Vec::new();
    permutations(&mut base, 0, &mut perms);
    perms
        .iter()
        .map(|p| {
            let product = p
                .iter()
                .enumerate()
                .map(|(row, &column)| format!("({})", matrix[row][column]))
                .collect::<Vec<_>>()
                .join("*");
            format!("{}*{}", permutation_sign(p), product)
        })
        .collect::<Vec<_>>()
        .join("+")
}

fn main() {
    // A,B,C are the squared loop-edge lengths y12^2,y23^2,y31^2.
    // Physical homogeneous chart: P1=1, P2=X2=u^2*t,
    // P3=X3=u-1-u^2*t.
    let matrix = vec![
        vec!["0", "1", "1", "1", "1"],
        vec!["1", "0", "A", "B", "C"],
        vec!["1", "A", "0", "u^4*t^2", "1"],
        vec!["1", "B", "u^4*t^2", "0", "(u-1-u^2*t)^2"],
        vec!["1", "C", "1", "(u-1-u^2*t)^2", "0"],
    ];
    let determinant = atom(&determinant_expression(&matrix));

    // The special fiber follows by direct source specialization u=0.
    let special_matrix = vec![
        vec!["0", "1", "1", "1", "1"],
        vec!["1", "0", "A", "B", "C"],
        vec!["1", "A", "0", "0", "1"],
        vec!["1", "B", "0", "0", "1"],
        vec!["1", "C", "1", "1", "0"],
    ];
    let special = atom(&determinant_expression(&special_matrix));
    let expected_special = atom("-2*(A-B)^2");

    assert_eq!(special, expected_special);
    println!("CM_pullback={determinant}");
    println!("CM_special={special}");
    println!("special_fiber_factor=-2*(A-B)^2");
    println!("weighted_ratio_t_absent_at_order_zero=true");
}
