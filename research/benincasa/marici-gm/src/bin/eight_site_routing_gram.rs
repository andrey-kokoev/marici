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
    (0..matrix.len()).fold(a("0"), |sum, column| {
        let minor = matrix
            .iter()
            .skip(1)
            .map(|row| {
                row.iter()
                    .enumerate()
                    .filter(|(index, _)| *index != column)
                    .map(|(_, value)| value.clone())
                    .collect::<Vec<_>>()
            })
            .collect::<Vec<_>>();
        let term = matrix[0][column].clone() * determinant(&minor);
        if column % 2 == 0 { sum + term } else { sum - term }
    })
    .expand()
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

fn main() {
    let k = a("k");
    let l = a("l");
    let routing = [
        vec![1, 0, 0, 0, 0, 0, 0, 0],
        vec![1, 1, 0, 0, 0, 0, 0, 0],
        vec![1, 1, 1, 0, 0, 0, 0, 0],
        vec![1, 1, 1, 1, 0, 0, 0, 0],
    ];
    let gram = routing
        .iter()
        .map(|x| routing.iter().map(|y| dot(x, y, &k, &l)).collect())
        .collect::<Vec<Vec<_>>>();
    let determinant = determinant(&gram).factor();
    let output = std::env::var("OUTPUT")
        .unwrap_or_else(|_| "../results/eight-site-routing-gram.json".into());
    let packet = json!({
        "schema":"marici.eight_site_routing_gram.v1",
        "pairing_by_cyclic_distance":{"0":"2","1":"3/2","2":"1/2","3":"k","4":"l"},
        "routing_basis":["q1","q1+q2","q1+q2+q3","q1+q2+q3+q4"],
        "gram":gram.iter().map(|row|row.iter().map(ToString::to_string).collect::<Vec<_>>()).collect::<Vec<_>>(),
        "determinant":determinant.to_string(),
        "scope":"universal labelled C8 cyclic routing Gram family before orbit selection"
    });
    fs::write(output, serde_json::to_string_pretty(&packet).unwrap()+"\n").unwrap();
    println!("{}", json!({"determinant":determinant.to_string()}));
}
