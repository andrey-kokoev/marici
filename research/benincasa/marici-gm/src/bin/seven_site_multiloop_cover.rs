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
    (0..matrix.len())
        .fold(a("0"), |total, column| {
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
                total + term
            } else {
                total - term
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
        .fold(a("0"), |sum, (i, left_entry)| {
            sum + right
                .iter()
                .enumerate()
                .fold(a("0"), |inner, (j, right_entry)| {
                    let separation = i.max(j) - i.min(j);
                    let distance = separation.min(7 - separation);
                    let pairing = match distance {
                        0 => a("2"),
                        1 => a("3/2"),
                        2 => a("1/2"),
                        3 => k.clone(),
                        _ => unreachable!(),
                    };
                    inner + a(&left_entry.to_string()) * a(&right_entry.to_string()) * pairing
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
    let x = a("x");
    let w = a("w");
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
    assert_eq!(gram_det.clone(), a("-1/4*k*(6+7*k)").factor());
    let b5 = routing
        .iter()
        .map(|route| dot_k(route, &q5, &k))
        .collect::<Vec<_>>();
    let b6 = routing
        .iter()
        .map(|route| dot_k(route, &q6, &k))
        .collect::<Vec<_>>();

    let site_energies = [
        a("-s6-p"),
        a("s2"),
        a("q"),
        a("-s2-s4-q"),
        a("s4-s5"),
        a("s6-s5"),
        a("p"),
    ];
    let signed_energies = [a("0"), a("s2"), a("y3"), a("s4"), a("s5"), a("s6"), a("y7")];
    let wall_forms = [
        site_energies[0].clone()
            + site_energies[1].clone()
            + site_energies[2].clone()
            + site_energies[3].clone()
            + site_energies[4].clone()
            + site_energies[6].clone()
            + signed_energies[4].clone()
            + signed_energies[5].clone(),
        site_energies[0].clone()
            + site_energies[5].clone()
            + site_energies[6].clone()
            + signed_energies[0].clone()
            + signed_energies[4].clone(),
        site_energies[0].clone()
            + site_energies[6].clone()
            + signed_energies[0].clone()
            + signed_energies[5].clone(),
        site_energies[1].clone()
            + site_energies[2].clone()
            + site_energies[3].clone()
            + site_energies[4].clone()
            + signed_energies[0].clone()
            + signed_energies[4].clone(),
        site_energies[2].clone()
            + site_energies[3].clone()
            + signed_energies[1].clone()
            + signed_energies[3].clone(),
        site_energies[2].clone()
            + site_energies[3].clone()
            + site_energies[4].clone()
            + signed_energies[1].clone()
            + signed_energies[4].clone(),
    ];
    for wall in &wall_forms {
        assert_eq!(wall.clone().expand(), a("0"));
    }

    // The selected walls are solved over the generic labelled X_i base by
    // y3 and y7 free. The five determined signed energies are algebraically
    // independent external parameters s2,s4,s5,s6. Their source-labelled
    // reconstruction is retained in the packet below.
    let squares = [a("0"), a("B"), x.clone(), a("D"), a("E"), a("U"), w.clone()];
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
        "schema":"marici.seven_site_multiloop_cover.v1",
        "selected_incidence":["g_123457","g_167","g_17","g_2345","g_34","g_345"],
        "wall_equations":[
            "X1+X2+X3+X4+X5+X7+y5+y6=0",
            "X1+X6+X7+y1+y5=0",
            "X1+X7+y1+y6=0",
            "X2+X3+X4+X5+y1+y5=0",
            "X3+X4+y2+y4=0",
            "X3+X4+X5+y2+y5=0"
        ],
        "base_relation":"X1+X6+X7=X2+X3+X4+X5",
        "source_labelled_wall_solution":{
            "y1":"0",
            "y2":"X2",
            "y3":"free",
            "y4":"-X2-X3-X4",
            "y5":"-X2-X3-X4-X5",
            "y6":"-X1-X7",
            "y7":"free"
        },
        "coefficient_parameterization":{"y1":"0","B":"y2^2","D":"y4^2","E":"y5^2","U":"y6^2","x":"y3^2","w":"y7^2"},
        "source_reconstruction":{"X1":"-s6-p","X2":"s2","X3":"q","X4":"-s2-s4-q","X5":"s4-s5","X6":"s6-s5","X7":"p"},
        "routing_gram_determinant":gram_det.to_string(),
        "pulled_cover":{"F1":first.to_string(),"F6":sixth.to_string(),"F7":seventh.to_string()},
        "critical_variables":["x=y3^2","w=y7^2"],
        "source_orientation":"ordered incidence and signed-energy labels retained from the selection packet"
    });
    fs::write(
        "../results/seven-site-multiloop-cover.json",
        serde_json::to_string_pretty(&packet).unwrap() + "\n",
    )
    .unwrap();
    println!(
        "{}",
        json!({"Gram":gram_det.to_string(),"dF1_dx":first.derivative(symbol!("marici::x")).factor().to_string(),"dF6_dx":sixth.derivative(symbol!("marici::x")).factor().to_string(),"dF7_dw":seventh.derivative(symbol!("marici::w")).factor().to_string()})
    );
}
