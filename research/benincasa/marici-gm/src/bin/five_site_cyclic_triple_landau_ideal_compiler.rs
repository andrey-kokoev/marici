use serde_json::{json, Value};
use std::{collections::BTreeMap, fs};
use symbolica::prelude::*;

fn atom(text: &str) -> Atom {
    Atom::parse(text, "marici", Default::default()).unwrap().expand()
}

fn determinant(matrix: &[Vec<Atom>]) -> Atom {
    if matrix.len() == 1 { return matrix[0][0].clone(); }
    let mut total = atom("0");
    for column in 0..matrix.len() {
        let minor = matrix[1..].iter().map(|row| row.iter().enumerate()
            .filter(|(index, _)| *index != column).map(|(_, value)| value.clone()).collect())
            .collect::<Vec<Vec<Atom>>>();
        let term = matrix[0][column].clone() * determinant(&minor);
        if column % 2 == 0 { total += term; } else { total -= term; }
    }
    total.expand()
}

fn adjugate(matrix: &[Vec<Atom>]) -> Vec<Vec<Atom>> {
    let size = matrix.len();
    let mut result = vec![vec![atom("0"); size]; size];
    for row in 0..size { for column in 0..size {
        let minor = matrix.iter().enumerate().filter(|(index, _)| *index != column)
            .map(|(_, values)| values.iter().enumerate().filter(|(index, _)| *index != row)
                .map(|(_, value)| value.clone()).collect()).collect::<Vec<Vec<Atom>>>();
        let cofactor = determinant(&minor);
        result[row][column] = if (row + column) % 2 == 0 { cofactor } else { -cofactor };
    }}
    result
}

fn dot(left: &[i32], right: &[i32]) -> Atom {
    let mut result = atom("0");
    for (i, left_value) in left.iter().enumerate() { for (j, right_value) in right.iter().enumerate() {
        let distance = (i.max(j) - i.min(j)).min(5 - (i.max(j) - i.min(j)));
        let entry = match distance {
            0 => atom("2"),
            1 => atom("(3+sqrt(5))/4"),
            2 => atom("(3-sqrt(5))/4"),
            _ => unreachable!(),
        };
        result += atom(&left_value.to_string()) * atom(&right_value.to_string()) * entry;
    }}
    result.expand()
}

fn wall_vector(label: &str) -> (i32, Vec<i32>) {
    let mut y = vec![0; 5];
    if label == "G" { return (5, y); }
    if let Some(edge) = label.strip_prefix("G_minus_e") {
        let first = edge.chars().next().unwrap().to_digit(10).unwrap() as usize - 1;
        y[first] = 2;
        return (5, y);
    }
    let sites = label.strip_prefix("g_").unwrap().chars()
        .map(|character| character.to_digit(10).unwrap() as usize - 1)
        .collect::<std::collections::BTreeSet<_>>();
    for edge in 0..5 {
        if sites.contains(&edge) != sites.contains(&((edge + 1) % 5)) { y[edge] = 1; }
    }
    (sites.len() as i32, y)
}

fn integer_rank(mut matrix: Vec<Vec<i64>>) -> usize {
    let rows = matrix.len(); let columns = matrix[0].len(); let mut rank = 0usize;
    for column in 0..columns {
        let Some(pivot) = (rank..rows).find(|row| matrix[*row][column] != 0) else { continue; };
        matrix.swap(rank, pivot);
        for row in rank + 1..rows {
            let left = matrix[rank][column]; let right = matrix[row][column];
            if right == 0 { continue; }
            for entry in column..columns { matrix[row][entry] = left * matrix[row][entry] - right * matrix[rank][entry]; }
        }
        rank += 1;
    }
    rank
}

fn det3(matrix: &[[i64; 3]; 3]) -> i64 {
    matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
}

fn gcd(mut left: i64, mut right: i64) -> i64 {
    while right != 0 {
        let remainder = left % right;
        left = right;
        right = remainder;
    }
    left.abs()
}

fn normalized_fraction(numerator: i64, denominator: i64) -> (i64, i64) {
    let common = gcd(numerator, denominator);
    let mut numerator = numerator / common;
    let mut denominator = denominator / common;
    if denominator < 0 {
        numerator = -numerator;
        denominator = -denominator;
    }
    (numerator, denominator)
}

fn pure_t_wall_solution(vectors: &[(i32, Vec<i32>)]) -> Option<Value> {
    for first in 0..3 {
        for second in first + 1..4 {
            for third in second + 1..5 {
                let pivot_columns = [first, second, third];
                let free_columns = (0..5).filter(|column| !pivot_columns.contains(column)).collect::<Vec<_>>();
                if vectors.iter().any(|(_, row)| free_columns.iter().any(|column| row[*column] != 0)) {
                    continue;
                }
                let pivot = std::array::from_fn(|row| {
                    std::array::from_fn(|column| vectors[row].1[pivot_columns[column]] as i64)
                });
                let denominator = det3(&pivot);
                if denominator == 0 { continue; }
                let rhs = vectors.iter().map(|(coefficient, _)| -(*coefficient as i64)).collect::<Vec<_>>();
                let numerators = (0..3).map(|column| {
                    let mut replaced = pivot;
                    for row in 0..3 { replaced[row][column] = rhs[row]; }
                    det3(&replaced)
                }).collect::<Vec<_>>();
                for row in 0..3 {
                    let recovered = (0..3).map(|column| pivot[row][column] * numerators[column]).sum::<i64>();
                    assert_eq!(recovered, denominator * rhs[row]);
                }
                let fractions = numerators.iter().map(|numerator| normalized_fraction(*numerator, denominator))
                    .collect::<Vec<_>>();
                return Some(json!({
                    "pivot_y_indices": pivot_columns.map(|column| column + 1),
                    "free_y_indices": free_columns.iter().map(|column| column + 1).collect::<Vec<_>>(),
                    "determinant": denominator,
                    "solution_numerators": numerators,
                    "all_pivot_y_nonzero_for_t_nonzero": numerators.iter().all(|numerator| *numerator != 0),
                    "solution": pivot_columns.iter().zip(fractions.iter()).map(|(column, (numerator, denominator))|
                        format!("y{}=({}/{})*t", column + 1, numerator, denominator)
                    ).collect::<Vec<_>>()
                }));
            }
        }
    }
    None
}

fn main() {
    let source: Value = serde_json::from_str(
        &fs::read_to_string("../results/five-site-compatible-landau-subsets.json").unwrap(),
    ).unwrap();
    let triple = source["census"].as_array().unwrap().iter()
        .find(|entry| entry["active_wall_count"] == 3).unwrap();
    let representatives = triple["nonzero_D5_representatives"].as_array().unwrap();
    assert_eq!(representatives.len(), 96);

    let routing = [vec![1,0,0,0,0], vec![1,1,0,0,0], vec![1,1,1,0,0]];
    let q4 = vec![1,1,1,1,0];
    let h = routing.iter().map(|left| routing.iter().map(|right| dot(left, right)).collect())
        .collect::<Vec<Vec<Atom>>>();
    let det_h = determinant(&h).factor();
    let adj_h = adjugate(&h);
    let b = routing.iter().map(|vector| dot(vector, &q4)).collect::<Vec<_>>();
    let c = (0..3).map(|row| {
        let numerator = (0..3).fold(atom("0"), |sum, column| sum + adj_h[row][column].clone() * b[column].clone());
        (numerator / det_h.clone()).together().cancel().expand()
    }).collect::<Vec<_>>();

    let mut rank_counts = BTreeMap::<usize, usize>::new();
    let mut pure_t_count = 0usize;
    let mut pure_t_kind_counts = BTreeMap::<String, usize>::new();
    let mut nonsoft_pure_t_count = 0usize;
    let mut nonsoft_pure_t_kind_counts = BTreeMap::<String, usize>::new();
    let records = representatives.iter().map(|value| {
        let representative = value.as_str().unwrap();
        let labels = representative.split('|').collect::<Vec<_>>();
        let vectors = labels.iter().map(|label| wall_vector(label)).collect::<Vec<_>>();
        let fiber_rank = integer_rank(vectors.iter().map(|(_, y)| y.iter().map(|value| *value as i64).collect()).collect());
        *rank_counts.entry(fiber_rank).or_default() += 1;
        let pure_t_solution = pure_t_wall_solution(&vectors);
        if pure_t_solution.is_some() {
            pure_t_count += 1;
            let kind = labels.iter().map(|label| {
                if label.starts_with("G_minus_e") { "G-e" } else if *label == "G" { "G" } else { "g" }
            }).collect::<Vec<_>>().join("+");
            *pure_t_kind_counts.entry(kind).or_default() += 1;
            if pure_t_solution.as_ref().unwrap()["all_pivot_y_nonzero_for_t_nonzero"] == true {
                nonsoft_pure_t_count += 1;
                *nonsoft_pure_t_kind_counts.entry(labels.iter().map(|label| {
                    if label.starts_with("G_minus_e") { "G-e" } else if *label == "G" { "G" } else { "g" }
                }).collect::<Vec<_>>().join("+")).or_default() += 1;
            }
        }
        let wall_equations = labels.iter().zip(vectors.iter()).map(|(label, (t_coefficient, y))| json!({
            "label": label,
            "t_coefficient": t_coefficient,
            "y_coefficients": y,
            "equation": format!("{}*t+{}", t_coefficient, y.iter().enumerate().filter(|(_, coefficient)| **coefficient != 0)
                .map(|(index, coefficient)| if *coefficient == 1 { format!("y{}", index + 1) } else { format!("{}*y{}", coefficient, index + 1) })
                .collect::<Vec<_>>().join("+"))
        })).collect::<Vec<_>>();
        json!({
            "representative": representative,
            "wall_equations": wall_equations,
            "fiber_wall_rank": fiber_rank,
            "pure_t_wall_solution": pure_t_solution,
            "critical_ideal": if fiber_rank == 3 {
                "five Kummer cover equations + three wall equations + determinant of their 8x8 fiber Jacobian"
            } else {
                "rank-deficient wall pullback: use maximal minors after deriving the excess component; do not use the square Jacobian determinant"
            },
            "saturation_factors": ["det(H)", "y1*y2*y3*y4*y5", "nonzero wall multipliers", "noncoincident focal gradients"]
        })
    }).collect::<Vec<_>>();

    let packet = json!({
        "schema": "marici.five_site_cyclic_triple_landau_ideal_compiler.v1",
        "slice": "Entry 1234 cyclic physical slice",
        "coefficient_field": "Q(sqrt(5))",
        "fiber_variables": ["u1","u2","u3","y1","y2","y3","y4","y5"],
        "parameter": "t",
        "routing_gram": h.iter().map(|row| row.iter().map(ToString::to_string).collect::<Vec<_>>()).collect::<Vec<_>>(),
        "det_routing_gram": det_h.to_string(),
        "q4_coordinates_in_routing_basis": c.iter().map(ToString::to_string).collect::<Vec<_>>(),
        "cover_equations": [
            "det(H)*y1^2-u^T*adj(H)*u=0",
            "det(H)*y2^2-F1+2*det(H)*u1-det(H)*h11=0",
            "det(H)*y3^2-F1+2*det(H)*u2-det(H)*h22=0",
            "det(H)*y4^2-F1+2*det(H)*u3-det(H)*h33=0",
            "det(H)*y5^2-F1+2*det(H)*c^T*u-det(H)*c^T*H*c=0"
        ],
        "representative_count": records.len(),
        "fiber_wall_rank_distribution": rank_counts,
        "pure_t_wall_solution_count": pure_t_count,
        "pure_t_wall_solution_kind_distribution": pure_t_kind_counts,
        "nonsoft_pure_t_wall_solution_count": nonsoft_pure_t_count,
        "nonsoft_pure_t_wall_solution_kind_distribution": nonsoft_pure_t_kind_counts,
        "records": records,
        "status": "typed exact ideal compiler packet; Groebner saturation and elimination not yet run",
        "new_carrier_datum": false
    });
    fs::write("../results/five-site-cyclic-triple-landau-ideal-compiler.json",
        serde_json::to_string_pretty(&packet).unwrap() + "\n").unwrap();
    println!("{}", json!({
        "representatives": 96,
        "fiber_wall_rank_distribution": rank_counts,
        "pure_t_wall_solution_count": pure_t_count,
        "pure_t_wall_solution_kind_distribution": pure_t_kind_counts,
        "nonsoft_pure_t_wall_solution_count": nonsoft_pure_t_count,
        "nonsoft_pure_t_wall_solution_kind_distribution": nonsoft_pure_t_kind_counts
    }));
}
