use serde_json::json;
use std::fs;
use symbolica::prelude::*;

fn a(source: &str) -> Atom {
    Atom::parse(source, "marici", Default::default())
        .unwrap()
        .expand()
}

fn determinant(matrix: &[Vec<Atom>]) -> Atom {
    if matrix.len() == 1 {
        return matrix[0][0].clone();
    }
    let mut total = a("0");
    for column in 0..matrix.len() {
        let minor = matrix[1..]
            .iter()
            .map(|row| {
                row.iter()
                    .enumerate()
                    .filter(|(index, _)| *index != column)
                    .map(|(_, value)| value.clone())
                    .collect()
            })
            .collect::<Vec<Vec<_>>>();
        let term = matrix[0][column].clone() * determinant(&minor);
        if column % 2 == 0 {
            total += term;
        } else {
            total -= term;
        }
    }
    total.expand()
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
                .map(|(_, source_row)| {
                    source_row
                        .iter()
                        .enumerate()
                        .filter(|(index, _)| *index != row)
                        .map(|(_, value)| value.clone())
                        .collect()
                })
                .collect::<Vec<Vec<_>>>();
            result[row][column] = if (row + column) % 2 == 0 {
                determinant(&minor)
            } else {
                -determinant(&minor)
            };
        }
    }
    result
}

fn dot_k(left: &[i32], right: &[i32], k: &Atom) -> Atom {
    left.iter()
        .enumerate()
        .fold(a("0"), |sum, (i, x)| {
            sum + right.iter().enumerate().fold(a("0"), |inner, (j, y)| {
                let distance = (i.max(j) - i.min(j)).min(7 - (i.max(j) - i.min(j)));
                let pairing = match distance {
                    0 => a("2"),
                    1 => a("3/2"),
                    2 => a("1/2"),
                    3 => k.clone(),
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

fn main() {
    let k = a("k");
    let t = a("t");
    let z = a("z");
    let x = a("x");
    let routing = [
        vec![1, 0, 0, 0, 0, 0, 0],
        vec![1, 1, 0, 0, 0, 0, 0],
        vec![1, 1, 1, 0, 0, 0, 0],
        vec![1, 1, 1, 1, 0, 0, 0],
    ];
    let q5 = vec![1, 1, 1, 1, 1, 0, 0];
    let q6 = vec![1, 1, 1, 1, 1, 1, 0];
    let gram = routing
        .iter()
        .map(|left| routing.iter().map(|right| dot_k(left, right, &k)).collect())
        .collect::<Vec<Vec<_>>>();
    let gram_det = determinant(&gram).factor();
    let gram_adj = adjugate(&gram);
    let b5 = routing
        .iter()
        .map(|route| dot_k(route, &q5, &k))
        .collect::<Vec<_>>();
    let b6 = routing
        .iter()
        .map(|route| dot_k(route, &q6, &k))
        .collect::<Vec<_>>();

    let alpha = (1..=4)
        .map(|index| a(&format!("alpha{index}")))
        .collect::<Vec<_>>();
    let energies = (1..=7)
        .map(|index| a(&format!("y{index}")))
        .collect::<Vec<_>>();
    let loop_square = quadratic(&alpha, &gram);
    let loop_dot_r = (0..4)
        .map(|row| {
            (0..4)
                .fold(a("0"), |sum, column| {
                    sum + gram[row][column].clone() * alpha[column].clone()
                })
                .expand()
        })
        .collect::<Vec<_>>();
    let loop_dot_q5 = (0..4)
        .fold(a("0"), |sum, index| {
            sum + alpha[index].clone() * b5[index].clone()
        })
        .expand();
    let loop_dot_q6 = (0..4)
        .fold(a("0"), |sum, index| {
            sum + alpha[index].clone() * b6[index].clone()
        })
        .expand();
    let mut cover =
        vec![(energies[0].clone() * energies[0].clone() - loop_square.clone()).expand()];
    for index in 0..4 {
        cover.push(
            (energies[index + 1].clone() * energies[index + 1].clone() - loop_square.clone()
                + a("2") * loop_dot_r[index].clone()
                - gram[index][index].clone())
            .expand(),
        );
    }
    cover.push(
        (energies[5].clone() * energies[5].clone() - loop_square.clone() + a("2") * loop_dot_q5
            - dot_k(&q5, &q5, &k))
        .expand(),
    );
    cover.push(
        (energies[6].clone() * energies[6].clone() - loop_square + a("2") * loop_dot_q6
            - dot_k(&q6, &q6, &k))
        .expand(),
    );

    let wall_forms = vec![
        a("7*t+2*y1"),
        a("6*t+y1+y2"),
        a("5*t+y1+y3"),
        a("4*t+y1+y4"),
        a("3*t+y1+y5"),
        a("2*t+y1+y6"),
    ];
    let wall_solution = [
        a("-7/2*t"),
        a("-5/2*t"),
        a("-3/2*t"),
        a("-1/2*t"),
        a("1/2*t"),
        a("3/2*t"),
    ];
    for wall in &wall_forms {
        let reduced = (0..6).fold(wall.clone(), |current, index| {
            current
                .replace(energies[index].to_pattern())
                .with(wall_solution[index].to_pattern())
        });
        assert_eq!(reduced.expand(), a("0"));
    }

    let squares = [
        a("49/4*z"),
        a("25/4*z"),
        a("9/4*z"),
        a("1/4*z"),
        a("1/4*z"),
        a("9/4*z"),
        x.clone(),
    ];
    let u = (0..4)
        .map(|index| {
            ((squares[0].clone() + gram[index][index].clone() - squares[index + 1].clone())
                / a("2"))
            .expand()
        })
        .collect::<Vec<_>>();
    let first = (gram_det.clone() * squares[0].clone() - quadratic(&u, &gram_adj))
        .expand()
        .factor();
    let q5_linear = (0..4).fold(a("0"), |sum, i| {
        sum + (0..4).fold(a("0"), |inner, j| {
            inner + gram_adj[i][j].clone() * b5[j].clone()
        }) * u[i].clone()
    });
    let sixth = (gram_det.clone()
        * (squares[5].clone() - squares[0].clone() - dot_k(&q5, &q5, &k))
        + a("2") * q5_linear)
        .expand()
        .factor();
    let q6_linear = (0..4).fold(a("0"), |sum, i| {
        sum + (0..4).fold(a("0"), |inner, j| {
            inner + gram_adj[i][j].clone() * b6[j].clone()
        }) * u[i].clone()
    });
    let seventh = (gram_det.clone()
        * (squares[6].clone() - squares[0].clone() - dot_k(&q6, &q6, &k))
        + a("2") * q6_linear)
        .expand()
        .factor();

    let packet = json!({
        "schema":"marici.seven_site_maximal_flag_cover.v1",
        "selected_incidence":["G_minus_e12","g_134567","g_14567","g_1567","g_167","g_17"],
        "coefficient_field":"Q(k)",
        "increment_pairing":{"diagonal":"2","distance_1":"3/2","distance_2":"1/2","distance_3":"k"},
        "routing_gram":gram.iter().map(|row|row.iter().map(ToString::to_string).collect::<Vec<_>>()).collect::<Vec<_>>(),
        "routing_gram_determinant":gram_det.to_string(),
        "generic_labelled_cover":{"routing_coordinates":["alpha1","alpha2","alpha3","alpha4"],"energy_labels":["y1","y2","y3","y4","y5","y6","y7"],"equations":cover.iter().map(ToString::to_string).collect::<Vec<_>>()},
        "wall_forms":wall_forms.iter().map(ToString::to_string).collect::<Vec<_>>(),
        "wall_solution":{"y1":"-7*t/2","y2":"-5*t/2","y3":"-3*t/2","y4":"-t/2","y5":"t/2","y6":"3*t/2","free":"y7","z":"t^2","x":"y7^2"},
        "pulled_back_cover":{"F1":first.to_string(),"F6":sixth.to_string(),"F7":seventh.to_string()},
        "scope":"one generic routing chart and exact flag pullback; cyclic Gram-completed atlas and critical elimination remain pending"
    });
    fs::write(
        "../results/seven-site-maximal-flag-cover.json",
        serde_json::to_string_pretty(&packet).unwrap() + "\n",
    )
    .unwrap();
    println!(
        "{}",
        json!({"det":gram_det.to_string(),"F1":first.to_string(),"F6":sixth.to_string(),"F7":seventh.to_string()})
    );
}
