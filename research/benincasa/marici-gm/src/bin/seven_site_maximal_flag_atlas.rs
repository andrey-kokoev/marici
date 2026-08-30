use serde_json::json;
use std::fs;
use symbolica::prelude::*;

fn a(source: &str) -> Atom {
    Atom::parse(source, "marici", Default::default())
        .unwrap()
        .expand()
}

fn det(matrix: &[Vec<Atom>]) -> Atom {
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
        let term = matrix[0][column].clone() * det(&minor);
        if column % 2 == 0 {
            total += term;
        } else {
            total -= term;
        }
    }
    total.expand()
}

fn adj(matrix: &[Vec<Atom>]) -> Vec<Vec<Atom>> {
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
                det(&minor)
            } else {
                -det(&minor)
            };
        }
    }
    result
}

fn pairing(left: &[i32], right: &[i32], k: &Atom) -> Atom {
    left.iter()
        .enumerate()
        .fold(a("0"), |sum, (i, x)| {
            sum + right.iter().enumerate().fold(a("0"), |inner, (j, y)| {
                let distance = (i.max(j) - i.min(j)).min(7 - (i.max(j) - i.min(j)));
                let value = match distance {
                    0 => a("2"),
                    1 => a("3/2"),
                    2 => a("1/2"),
                    3 => k.clone(),
                    _ => unreachable!(),
                };
                inner + a(&x.to_string()) * a(&y.to_string()) * value
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
        .together()
        .cancel()
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

fn main() {
    let k = a("k");
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
        .map(|left| {
            routing
                .iter()
                .map(|right| pairing(left, right, &k))
                .collect()
        })
        .collect::<Vec<Vec<_>>>();
    let determinant = det(&gram).factor();
    let inverse_numerator = adj(&gram);
    let b5 = routing
        .iter()
        .map(|route| pairing(route, &q5, &k))
        .collect::<Vec<_>>();
    let b6 = routing
        .iter()
        .map(|route| pairing(route, &q6, &k))
        .collect::<Vec<_>>();
    let c5 = mat_vec(&inverse_numerator, &b5)
        .into_iter()
        .map(|entry| (entry / determinant.clone()).together().cancel().expand())
        .collect::<Vec<_>>();
    let c6 = mat_vec(&inverse_numerator, &b6)
        .into_iter()
        .map(|entry| (entry / determinant.clone()).together().cancel().expand())
        .collect::<Vec<_>>();
    let normal55 = (pairing(&q5, &q5, &k) - bilinear(&c5, &gram, &c5))
        .together()
        .cancel()
        .factor();
    let normal66 = (pairing(&q6, &q6, &k) - bilinear(&c6, &gram, &c6))
        .together()
        .cancel()
        .factor();
    let normal56 = (pairing(&q5, &q6, &k) - bilinear(&c5, &gram, &c6))
        .together()
        .cancel()
        .factor();

    let zero = vec![a("0"); 4];
    let mut vertex_coordinates = vec![zero];
    for index in 0..4 {
        let mut unit = vec![a("0"); 4];
        unit[index] = a("1");
        vertex_coordinates.push(unit);
    }
    vertex_coordinates.push(c5);
    vertex_coordinates.push(c6);
    let beta = (1..=4)
        .map(|index| a(&format!("beta{index}")))
        .collect::<Vec<_>>();

    let mut chart_packets = Vec::new();
    for origin in 0..7 {
        let basis_vertices = (1..=4).map(|step| (origin + step) % 7).collect::<Vec<_>>();
        let origin_coordinate = vertex_coordinates[origin].clone();
        let columns = basis_vertices
            .iter()
            .map(|vertex| {
                vertex_coordinates[*vertex]
                    .iter()
                    .zip(&origin_coordinate)
                    .map(|(left, right)| (left.clone() - right.clone()).expand())
                    .collect::<Vec<_>>()
            })
            .collect::<Vec<_>>();
        let transition = (0..4)
            .map(|row| (0..4).map(|column| columns[column][row].clone()).collect())
            .collect::<Vec<Vec<_>>>();
        let transition_det = det(&transition).together().cancel().factor();
        assert_ne!(transition_det, a("0"));
        let local_gram = (0..4)
            .map(|left| {
                (0..4)
                    .map(|right| bilinear(&columns[left], &gram, &columns[right]))
                    .collect()
            })
            .collect::<Vec<Vec<_>>>();
        let local_det = det(&local_gram).together().cancel().factor();
        let alpha_pullback = (0..4)
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
        let mut checks = Vec::new();
        for local_index in 0..7 {
            let global_vertex = (origin + local_index) % 7;
            let base_difference = alpha_pullback
                .iter()
                .zip(&vertex_coordinates[global_vertex])
                .map(|(left, right)| (left.clone() - right.clone()).expand())
                .collect::<Vec<_>>();
            let base_distance = bilinear(&base_difference, &gram, &base_difference);
            let local_coordinate = if local_index == 0 {
                vec![a("0"); 4]
            } else if local_index <= 4 {
                let mut unit = vec![a("0"); 4];
                unit[local_index - 1] = a("1");
                unit
            } else {
                let target_difference = vertex_coordinates[global_vertex]
                    .iter()
                    .zip(&origin_coordinate)
                    .map(|(left, right)| (left.clone() - right.clone()).expand())
                    .collect::<Vec<_>>();
                let b = columns
                    .iter()
                    .map(|column| bilinear(column, &gram, &target_difference))
                    .collect::<Vec<_>>();
                mat_vec(&adj(&local_gram), &b)
                    .into_iter()
                    .map(|entry| (entry / local_det.clone()).together().cancel().expand())
                    .collect()
            };
            let local_difference = beta
                .iter()
                .zip(local_coordinate)
                .map(|(left, right)| (left.clone() - right).expand())
                .collect::<Vec<_>>();
            let local_distance = bilinear(&local_difference, &local_gram, &local_difference);
            assert_eq!(
                (base_distance - local_distance)
                    .together()
                    .cancel()
                    .expand(),
                a("0")
            );
            checks.push(true);
        }
        chart_packets.push(json!({
            "origin":origin+1,
            "energy_order":(0..7).map(|step|(origin+step)%7+1).collect::<Vec<_>>(),
            "transition_det":transition_det.to_string(),
            "local_gram_det":local_det.to_string(),
            "seven_cover_pullbacks_zero":checks
        }));
    }

    let packet = json!({
        "schema":"marici.seven_site_maximal_flag_atlas.v1",
        "routing_gram_determinant":determinant.to_string(),
        "unrestricted_normal_gram":{"q5_q5":normal55.to_string(),"q5_q6":normal56.to_string(),"q6_q6":normal66.to_string()},
        "atlas_completion":"q5 and q6 are projected to the routing four-plane before chart transport",
        "charts":chart_packets,
        "certification":"49 exact labelled squared-distance pullback identities",
        "scope":"complete seven-chart Gram-completed routing atlas; unrestricted normal data retained separately"
    });
    fs::write(
        "../results/seven-site-maximal-flag-atlas.json",
        serde_json::to_string_pretty(&packet).unwrap() + "\n",
    )
    .unwrap();
    println!(
        "{}",
        json!({"charts":7,"checks":49,"det":determinant.to_string(),"normal_gram":[normal55.to_string(),normal56.to_string(),normal66.to_string()]})
    );
}
