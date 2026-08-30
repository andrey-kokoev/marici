use serde_json::json;
use std::fs;
use symbolica::prelude::*;

fn a(s: &str) -> Atom {
    Atom::parse(s, "marici", Default::default())
        .unwrap()
        .expand()
}

fn det(m: &[Vec<Atom>]) -> Atom {
    if m.len() == 1 {
        return m[0][0].clone();
    }
    let mut total = a("0");
    for column in 0..m.len() {
        let minor = m[1..]
            .iter()
            .map(|row| {
                row.iter()
                    .enumerate()
                    .filter(|(j, _)| *j != column)
                    .map(|(_, value)| value.clone())
                    .collect()
            })
            .collect::<Vec<Vec<_>>>();
        let term = m[0][column].clone() * det(&minor);
        if column % 2 == 0 {
            total += term;
        } else {
            total -= term;
        }
    }
    total.expand()
}

fn adj(m: &[Vec<Atom>]) -> Vec<Vec<Atom>> {
    let n = m.len();
    let mut out = vec![vec![a("0"); n]; n];
    for row in 0..n {
        for column in 0..n {
            let minor = m
                .iter()
                .enumerate()
                .filter(|(i, _)| *i != column)
                .map(|(_, source_row)| {
                    source_row
                        .iter()
                        .enumerate()
                        .filter(|(j, _)| *j != row)
                        .map(|(_, value)| value.clone())
                        .collect()
                })
                .collect::<Vec<Vec<_>>>();
            out[row][column] = if (row + column) % 2 == 0 {
                det(&minor)
            } else {
                -det(&minor)
            };
        }
    }
    out
}

fn increment_pairing(i: usize, j: usize, k: &Atom) -> Atom {
    let delta = (i.max(j) - i.min(j)).min(6 - (i.max(j) - i.min(j)));
    match delta {
        0 => a("2"),
        1 => a("3/2"),
        2 => a("1/2"),
        3 => k.clone(),
        _ => unreachable!(),
    }
}

fn increment_vector_dot(left: &[i32], right: &[i32], k: &Atom) -> Atom {
    left.iter()
        .enumerate()
        .fold(a("0"), |sum, (i, x)| {
            sum + right.iter().enumerate().fold(a("0"), |inner, (j, y)| {
                inner + a(&x.to_string()) * a(&y.to_string()) * increment_pairing(i, j, k)
            })
        })
        .expand()
}

fn mat_vec(matrix: &[Vec<Atom>], vector: &[Atom]) -> Vec<Atom> {
    matrix
        .iter()
        .map(|row| {
            row.iter()
                .zip(vector)
                .fold(a("0"), |sum, (left, right)| {
                    sum + left.clone() * right.clone()
                })
                .expand()
        })
        .collect()
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

fn bilinear(left: &[Atom], matrix: &[Vec<Atom>], right: &[Atom]) -> Atom {
    left.iter()
        .enumerate()
        .fold(a("0"), |sum, (i, x)| {
            sum + right.iter().enumerate().fold(a("0"), |inner, (j, y)| {
                inner + x.clone() * matrix[i][j].clone() * y.clone()
            })
        })
        .expand()
}

fn main() {
    let k = a("k");
    let origins = [0usize, 2, 4];
    let beta = (1..=4).map(|i| a(&format!("beta{i}"))).collect::<Vec<_>>();

    let routing = [
        vec![1, 0, 0, 0, 0, 0],
        vec![1, 1, 0, 0, 0, 0],
        vec![1, 1, 1, 0, 0, 0],
        vec![1, 1, 1, 1, 0, 0],
    ];
    let q5 = vec![1, 1, 1, 1, 1, 0];
    let h0 = routing
        .iter()
        .map(|left| {
            routing
                .iter()
                .map(|right| increment_vector_dot(left, right, &k))
                .collect()
        })
        .collect::<Vec<Vec<_>>>();
    let determinant = det(&h0).factor();
    let inverse_numerator = adj(&h0);
    let b5 = routing
        .iter()
        .map(|route| increment_vector_dot(route, &q5, &k))
        .collect::<Vec<_>>();
    let c5 = mat_vec(&inverse_numerator, &b5)
        .into_iter()
        .map(|entry| (entry / determinant.clone()).together().cancel().expand())
        .collect::<Vec<_>>();

    // Coordinates of the six external vertices in the chart based at vertex 1.
    let zero = vec![a("0"); 4];
    let mut vertex_coordinates = vec![zero.clone()];
    for index in 0..4 {
        let mut unit = vec![a("0"); 4];
        unit[index] = a("1");
        vertex_coordinates.push(unit);
    }
    vertex_coordinates.push(c5.clone());

    let mut chart_packets = Vec::new();
    for &origin in &origins {
        let local_vertices = (1..=4).map(|step| (origin + step) % 6).collect::<Vec<_>>();
        let origin_coordinate = vertex_coordinates[origin].clone();
        let transition_columns = local_vertices
            .iter()
            .map(|&vertex| {
                vertex_coordinates[vertex]
                    .iter()
                    .zip(&origin_coordinate)
                    .map(|(left, right)| (left.clone() - right.clone()).expand())
                    .collect::<Vec<_>>()
            })
            .collect::<Vec<_>>();
        let transition = (0..4)
            .map(|row| {
                (0..4)
                    .map(|column| transition_columns[column][row].clone())
                    .collect::<Vec<_>>()
            })
            .collect::<Vec<_>>();
        let local_gram = (0..4)
            .map(|left| {
                (0..4)
                    .map(|right| {
                        let left_column = transition
                            .iter()
                            .map(|row| row[left].clone())
                            .collect::<Vec<_>>();
                        let right_column = transition
                            .iter()
                            .map(|row| row[right].clone())
                            .collect::<Vec<_>>();
                        bilinear(&left_column, &h0, &right_column)
                    })
                    .collect::<Vec<_>>()
            })
            .collect::<Vec<_>>();
        let local_determinant = det(&local_gram).together().cancel().factor();
        let transition_det = det(&transition).together().cancel().factor();
        assert_ne!(transition_det, a("0"));

        let affine_pullback = (0..4)
            .map(|row| {
                (origin_coordinate[row].clone()
                    + (0..4).fold(a("0"), |sum, column| {
                        sum + transition[row][column].clone() * beta[column].clone()
                    }))
                .together()
                .cancel()
                .expand()
            })
            .collect::<Vec<_>>();

        // Directly verify all six squared-distance functions under the affine transition.
        let local_loop_square = quadratic(&beta, &local_gram);
        let mut equation_checks = Vec::new();
        for local_index in 0..6 {
            let global_vertex = (origin + local_index) % 6;
            let base_difference = affine_pullback
                .iter()
                .zip(&vertex_coordinates[global_vertex])
                .map(|(left, right)| (left.clone() - right.clone()).expand())
                .collect::<Vec<_>>();
            let base_distance = quadratic(&base_difference, &h0);

            let local_distance = if local_index == 0 {
                local_loop_square.clone()
            } else if local_index <= 4 {
                let mut difference = beta.clone();
                difference[local_index - 1] -= a("1");
                quadratic(&difference, &local_gram)
            } else {
                let last_vertex = (origin + 5) % 6;
                let last_difference = vertex_coordinates[last_vertex]
                    .iter()
                    .zip(&origin_coordinate)
                    .map(|(left, right)| (left.clone() - right.clone()).expand())
                    .collect::<Vec<_>>();
                let local_b = (0..4)
                    .map(|column| {
                        let basis_column = transition
                            .iter()
                            .map(|row| row[column].clone())
                            .collect::<Vec<_>>();
                        bilinear(&basis_column, &h0, &last_difference)
                    })
                    .collect::<Vec<_>>();
                let local_c = mat_vec(&adj(&local_gram), &local_b)
                    .into_iter()
                    .map(|entry| {
                        (entry / local_determinant.clone())
                            .together()
                            .cancel()
                            .expand()
                    })
                    .collect::<Vec<_>>();
                let difference = beta
                    .iter()
                    .zip(local_c)
                    .map(|(left, right)| (left.clone() - right).expand())
                    .collect::<Vec<_>>();
                quadratic(&difference, &local_gram)
            };
            let defect = (base_distance - local_distance)
                .together()
                .cancel()
                .expand();
            assert_eq!(defect, a("0"));
            equation_checks.push(true);
        }
        chart_packets.push(json!({
            "origin_label": origin + 1,
            "ordered_vertex_labels": local_vertices.iter().map(|index| index + 1).collect::<Vec<_>>(),
            "energy_label_order": (0..6).map(|step| (origin + step) % 6 + 1).collect::<Vec<_>>(),
            "affine_transition_alpha_equals_origin_plus_T_beta": {
                "origin": origin_coordinate.iter().map(ToString::to_string).collect::<Vec<_>>(),
                "T": transition.iter().map(|row| row.iter().map(ToString::to_string).collect::<Vec<_>>()).collect::<Vec<_>>(),
                "det_T": transition_det.to_string()
            },
            "local_routing_gram_determinant": local_determinant.to_string(),
            "six_cover_pullbacks_zero": equation_checks
        }));
    }

    let packet = json!({
        "schema": "marici.six_site_disjoint_pair_triple_labelled_atlas.v1",
        "coefficient_field": "Q(k)",
        "external_increment_pairing_seed": {"diagonal":"2","adjacent":"3/2","next_adjacent":"1/2","opposite":"k"},
        "four_dimensional_completion": "the sixth vertex is the H(k)-orthogonal projection of the source q5 data; equivalently its normal square is set to zero before chart transport",
        "genericity_locus": ["k != 0", "6+7*k != 0"],
        "routing_gram_determinant": determinant.to_string(),
        "charts": chart_packets,
        "cyclic_generator": "sigma=(1 3 5)(2 4 6)",
        "certification": "all six labelled squared-distance cover equations pull back identically in every chart",
        "scope": "generic three-chart affine routing atlas; wall critical ideal not yet saturated"
    });
    fs::write(
        "../results/six-site-disjoint-pair-triple-labelled-atlas.json",
        serde_json::to_string_pretty(&packet).unwrap() + "\n",
    )
    .unwrap();
    println!(
        "{}",
        json!({"det":determinant.to_string(),"charts":3,"cover_checks":18,"status":"passed"})
    );
}
