use serde_json::json;
use std::fs;
use symbolica::prelude::*;

const N: usize = 8;

fn a(source: &str) -> Atom {
    Atom::parse(source, "marici", Default::default())
        .unwrap()
        .expand()
}

fn determinant(matrix: &[Vec<Atom>]) -> Atom {
    if matrix.len() == 1 {
        return matrix[0][0].clone();
    }
    (0..matrix.len())
        .fold(a("0"), |sum, column| {
            let minor = matrix[1..]
                .iter()
                .map(|row| {
                    row.iter()
                        .enumerate()
                        .filter(|(index, _)| *index != column)
                        .map(|(_, value)| value.clone())
                        .collect::<Vec<_>>()
                })
                .collect::<Vec<_>>();
            let term = matrix[0][column].clone() * determinant(&minor);
            if column % 2 == 0 {
                sum + term
            } else {
                sum - term
            }
        })
        .expand()
}

fn adjugate(matrix: &[Vec<Atom>]) -> Vec<Vec<Atom>> {
    let n = matrix.len();
    let mut result = vec![vec![a("0"); n]; n];
    for row in 0..n {
        for column in 0..n {
            let minor = matrix
                .iter()
                .enumerate()
                .filter(|(index, _)| *index != column)
                .map(|(_, source)| {
                    source
                        .iter()
                        .enumerate()
                        .filter(|(index, _)| *index != row)
                        .map(|(_, value)| value.clone())
                        .collect::<Vec<_>>()
                })
                .collect::<Vec<_>>();
            result[row][column] = if (row + column) % 2 == 0 {
                determinant(&minor)
            } else {
                -determinant(&minor)
            };
        }
    }
    result
}

fn dot(left: &[i32], right: &[i32], k: &Atom, l: &Atom) -> Atom {
    left.iter()
        .enumerate()
        .fold(a("0"), |sum, (i, x)| {
            sum + right.iter().enumerate().fold(a("0"), |inner, (j, y)| {
                let separation = i.abs_diff(j);
                let distance = separation.min(N - separation);
                let pairing = match distance {
                    0 => a("2"),
                    1 => a("3/2"),
                    2 => a("1/2"),
                    3 => k.clone(),
                    4 => l.clone(),
                    _ => unreachable!(),
                };
                inner + a(&x.to_string()) * a(&y.to_string()) * pairing
            })
        })
        .expand()
}

fn quadratic(vector: &[Atom], matrix: &[Vec<Atom>]) -> Atom {
    vector
        .iter()
        .enumerate()
        .fold(a("0"), |sum, (i, left)| {
            sum + vector.iter().enumerate().fold(a("0"), |inner, (j, right)| {
                inner + left.clone() * matrix[i][j].clone() * right.clone()
            })
        })
        .expand()
}

fn cover(squares: &[Atom]) -> Vec<Atom> {
    let k = a("k");
    let l = a("l");
    let routing = [
        vec![1, 0, 0, 0, 0, 0, 0, 0],
        vec![1, 1, 0, 0, 0, 0, 0, 0],
        vec![1, 1, 1, 0, 0, 0, 0, 0],
        vec![1, 1, 1, 1, 0, 0, 0, 0],
    ];
    let extensions = [
        vec![1, 1, 1, 1, 1, 0, 0, 0],
        vec![1, 1, 1, 1, 1, 1, 0, 0],
        vec![1, 1, 1, 1, 1, 1, 1, 0],
    ];
    let gram = routing
        .iter()
        .map(|left| {
            routing
                .iter()
                .map(|right| dot(left, right, &k, &l))
                .collect()
        })
        .collect::<Vec<Vec<_>>>();
    let det = determinant(&gram).factor();
    let adj = adjugate(&gram);
    let u = (0..4)
        .map(|i| {
            ((squares[0].clone() + gram[i][i].clone() - squares[i + 1].clone()) / a("2")).expand()
        })
        .collect::<Vec<_>>();
    let first = (det.clone() * squares[0].clone() - quadratic(&u, &adj)).expand();
    let extension = |route: &Vec<i32>, square: &Atom| {
        let b = routing
            .iter()
            .map(|base| dot(base, route, &k, &l))
            .collect::<Vec<_>>();
        let linear = (0..4).fold(a("0"), |sum, i| {
            sum + (0..4).fold(a("0"), |inner, j| inner + adj[i][j].clone() * b[j].clone())
                * u[i].clone()
        });
        (det.clone() * (square.clone() - squares[0].clone() - dot(route, route, &k, &l))
            + a("2") * linear)
            .expand()
    };
    std::iter::once(first)
        .chain(
            extensions
                .iter()
                .enumerate()
                .map(|(index, route)| extension(route, &squares[index + 5])),
        )
        .collect()
}

fn model(name: &str, squares: Vec<Atom>, variables: &[&str]) -> serde_json::Value {
    let equations = cover(&squares);
    let symbols = variables
        .iter()
        .map(|name| Symbol::parse(*name, "marici").unwrap())
        .collect::<Vec<_>>();
    let jacobian = equations
        .iter()
        .map(|equation| {
            symbols
                .iter()
                .map(|variable| equation.derivative(*variable).expand())
                .collect()
        })
        .collect::<Vec<Vec<_>>>();
    let det = determinant(&jacobian).factor();
    json!({
        "name":name,
        "squares":squares.iter().map(ToString::to_string).collect::<Vec<_>>(),
        "variables":variables,
        "cover_equations":equations.iter().map(|equation|equation.factor().to_string()).collect::<Vec<_>>(),
        "jacobian_determinant":det.to_string()
    })
}

fn main() {
    let zero = a("0");
    let square = |name: &str| {
        let value = a(name);
        (value.clone() * value).expand()
    };
    let family_a = model(
        "family_A_surviving_edge_1_free_even",
        vec![
            square("z"),
            square("a"),
            zero.clone(),
            square("b"),
            zero.clone(),
            square("c"),
            zero.clone(),
            square("d"),
        ],
        &["a", "b", "c", "d"],
    );
    let family_b8 = model(
        "family_B_surviving_edge_8_free_odd",
        vec![
            square("a"),
            zero.clone(),
            square("b"),
            zero.clone(),
            square("c"),
            zero.clone(),
            square("d"),
            square("z"),
        ],
        &["a", "b", "c", "d"],
    );
    let family_b6 = model(
        "family_B_surviving_edge_6_free_odd",
        vec![
            square("a"),
            zero.clone(),
            square("b"),
            zero.clone(),
            square("c"),
            square("z"),
            square("d"),
            zero.clone(),
        ],
        &["a", "b", "c", "d"],
    );
    let family_b4 = model(
        "family_B_surviving_edge_4_free_odd",
        vec![
            square("a"),
            zero.clone(),
            square("b"),
            square("z"),
            square("c"),
            zero.clone(),
            square("d"),
            zero.clone(),
        ],
        &["a", "b", "c", "d"],
    );
    let packet = json!({
        "schema":"marici.eight_site_base_reduced_companion_models.v1",
        "models":[family_a,family_b8,family_b6,family_b4],
        "scope":"all four labelled source-base-reduced C8 rank-four wall patterns"
    });
    fs::write(
        "../results/eight-site-base-reduced-companion-models.json",
        serde_json::to_string_pretty(&packet).unwrap() + "\n",
    )
    .unwrap();
    println!("{}", json!({"models":4}));
}
