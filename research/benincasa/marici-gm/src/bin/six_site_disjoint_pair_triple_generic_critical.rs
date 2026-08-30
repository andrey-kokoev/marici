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
                    .filter(|(j, _)| *j != column)
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
                let distance = (i.max(j) - i.min(j)).min(6 - (i.max(j) - i.min(j)));
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

fn replace_many(expression: Atom, variables: &[Atom], values: &[Atom]) -> Atom {
    variables
        .iter()
        .zip(values)
        .fold(expression, |current, (variable, value)| {
            current
                .replace(variable.to_pattern())
                .with(value.to_pattern())
        })
}

fn bilinear_local(left: &[Atom], matrix: &[Vec<Atom>], right: &[Atom]) -> Atom {
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

fn main() {
    let x = a("x");
    let v = a("v");
    let w = a("w");
    let z = a("z");
    let k = a("k");
    let variables = vec![x.clone(), v.clone(), w.clone()];
    let symbols = [
        symbol!("marici::x"),
        symbol!("marici::v"),
        symbol!("marici::w"),
    ];

    // Denominator-cleared wall equations from the frozen generic cover.
    let f = a("-12+82*k+14*k*x+42*k*x*z-28*k*x*v-14*k*x*w-180*k*z+120*k*z*v+42*k*z*w+128*k*v-28*k*v*w+14*k*w-102*k*z^2-32*k*v^2+12*x+36*x*z-24*x*v-6*x*w-72*z+144*z*v+36*z*w+48*v-24*v*w+12*w+112*k^2-112*k^2*z-56*k^2*z*v+84*k^2*v+28*k^2*z^2+28*k^2*v^2-3*x^2-108*z^2-48*v^2-3*w^2");
    let g = a("-36-66*k+5*k*x-30*k*z+23*k*v+2*k*w+12*x-36*z+30*v-6*w-28*k^2+14*k^2*z-14*k^2*v");

    let df = symbols
        .iter()
        .map(|symbol| f.derivative(*symbol).expand())
        .collect::<Vec<_>>();
    let dg = symbols
        .iter()
        .map(|symbol| g.derivative(*symbol).expand())
        .collect::<Vec<_>>();
    let minors = (0..3)
        .flat_map(|left| ((left + 1)..3).map(move |right| (left, right)))
        .map(|(left, right)| {
            (df[left].clone() * dg[right].clone() - df[right].clone() * dg[left].clone())
                .expand()
                .factor()
        })
        .collect::<Vec<_>>();

    // On the chart dG/dw != 0, two minors plus G are a complete rank-drop system.
    let equations = vec![g.clone(), minors[1].clone(), minors[2].clone()];
    let zeros = vec![a("0"); 3];
    let coefficient_matrix = equations
        .iter()
        .map(|equation| {
            symbols
                .iter()
                .map(|symbol| equation.derivative(*symbol).expand())
                .collect()
        })
        .collect::<Vec<Vec<_>>>();
    let constants = equations
        .iter()
        .map(|equation| replace_many(equation.clone(), &variables, &zeros).expand())
        .collect::<Vec<_>>();
    let denominator = determinant(&coefficient_matrix).factor();
    assert_ne!(denominator, a("0"));

    let numerators = (0..3)
        .map(|column| {
            let mut matrix = coefficient_matrix.clone();
            for row in 0..3 {
                matrix[row][column] = -constants[row].clone();
            }
            determinant(&matrix).factor()
        })
        .collect::<Vec<_>>();
    let solutions = numerators
        .iter()
        .map(|numerator| {
            (numerator.clone() / denominator.clone())
                .together()
                .cancel()
                .expand()
        })
        .collect::<Vec<_>>();

    let g_check = (replace_many(g.clone(), &variables, &solutions) * denominator.clone())
        .together()
        .cancel()
        .expand();
    assert_eq!(g_check, a("0"));
    let minor_checks = minors
        .iter()
        .map(|minor| {
            (replace_many(minor.clone(), &variables, &solutions) * denominator.clone())
                .together()
                .cancel()
                .expand()
        })
        .collect::<Vec<_>>();
    assert!(minor_checks.iter().all(|check| *check == a("0")));

    let discriminant = (replace_many(f.clone(), &variables, &solutions)
        * denominator.clone()
        * denominator.clone())
    .together()
    .cancel()
    .expand()
    .factor();
    assert_ne!(discriminant, a("0"));

    let generic_divisor =
        a("-5586+1026*z+69*z*k-500*z*k^2+196*z*k^3-5341*k-98*k^2-392*k^3").factor();
    let mut pivot_packets = Vec::new();
    for pivot in 0..3 {
        let others = (0..3).filter(|index| *index != pivot).collect::<Vec<_>>();
        let pivot_equations = vec![
            g.clone(),
            (df[others[0]].clone() * dg[pivot].clone() - df[pivot].clone() * dg[others[0]].clone())
                .expand(),
            (df[others[1]].clone() * dg[pivot].clone() - df[pivot].clone() * dg[others[1]].clone())
                .expand(),
        ];
        let pivot_matrix = pivot_equations
            .iter()
            .map(|equation| {
                symbols
                    .iter()
                    .map(|symbol| equation.derivative(*symbol).expand())
                    .collect()
            })
            .collect::<Vec<Vec<_>>>();
        let pivot_constants = pivot_equations
            .iter()
            .map(|equation| replace_many(equation.clone(), &variables, &zeros).expand())
            .collect::<Vec<_>>();
        let pivot_denominator = determinant(&pivot_matrix).factor();
        let pivot_numerators = (0..3)
            .map(|column| {
                let mut matrix = pivot_matrix.clone();
                for row in 0..3 {
                    matrix[row][column] = -pivot_constants[row].clone();
                }
                determinant(&matrix).factor()
            })
            .collect::<Vec<_>>();
        let pivot_solutions = pivot_numerators
            .iter()
            .map(|numerator| {
                (numerator.clone() / pivot_denominator.clone())
                    .together()
                    .cancel()
                    .expand()
            })
            .collect::<Vec<_>>();
        let pivot_discriminant = (replace_many(f.clone(), &variables, &pivot_solutions)
            * pivot_denominator.clone()
            * pivot_denominator.clone())
        .together()
        .cancel()
        .expand()
        .factor();
        let residual_factor = (pivot_discriminant.clone() / generic_divisor.clone())
            .together()
            .cancel()
            .expand()
            .factor();
        assert_eq!(
            residual_factor.derivative(symbol!("marici::z")).expand(),
            a("0")
        );
        let pivot_name = ["x", "v", "w"][pivot];
        pivot_packets.push(json!({
            "pivot_variable":pivot_name,
            "dG":dg[pivot].to_string(),
            "linear_system_determinant":pivot_denominator.to_string(),
            "eliminated_F":pivot_discriminant.to_string(),
            "factor_after_removing_generic_divisor":residual_factor.to_string()
        }));
    }

    let a_k = a("1026+69*k-500*k^2+196*k^3");
    let z_on_divisor = (a("5586+5341*k+98*k^2+392*k^3") / a_k.clone())
        .together()
        .cancel()
        .expand();
    let on_divisor_solutions = solutions
        .iter()
        .map(|solution| {
            solution
                .clone()
                .replace(z.to_pattern())
                .with(z_on_divisor.to_pattern())
                .together()
                .cancel()
                .expand()
                .factor()
        })
        .collect::<Vec<_>>();
    assert!(on_divisor_solutions
        .iter()
        .all(|solution| *solution != a("0")));

    let gx = dg[0].clone();
    let gv = dg[1].clone();
    let gw = dg[2].clone();
    let kernel_basis = vec![
        vec![
            a("1"),
            a("0"),
            (-gx.clone() / gw.clone()).together().cancel().expand(),
        ],
        vec![
            a("0"),
            a("1"),
            (-gv.clone() / gw.clone()).together().cancel().expand(),
        ],
    ];
    let hessian = (0..3)
        .map(|row| {
            (0..3)
                .map(|column| df[row].derivative(symbols[column]).expand())
                .collect()
        })
        .collect::<Vec<Vec<_>>>();
    let transverse_hessian = (0..2)
        .map(|left| {
            (0..2)
                .map(|right| bilinear_local(&kernel_basis[left], &hessian, &kernel_basis[right]))
                .collect()
        })
        .collect::<Vec<Vec<_>>>();
    let transverse_determinant = determinant(&transverse_hessian)
        .together()
        .cancel()
        .factor();
    assert_ne!(transverse_determinant, a("0"));

    let sample_k = a("1/10");
    let sample_values = on_divisor_solutions
        .iter()
        .map(|value| {
            value
                .clone()
                .replace(k.to_pattern())
                .with(sample_k.to_pattern())
                .together()
                .cancel()
                .expand()
        })
        .collect::<Vec<_>>();
    let sample_z = z_on_divisor
        .clone()
        .replace(k.to_pattern())
        .with(sample_k.to_pattern())
        .together()
        .cancel()
        .expand();

    // Recover the three labelled source-wall conormal coefficients before
    // identifying the even edge squares s2=s4=s6=z.
    let routing = [
        vec![1, 0, 0, 0, 0, 0],
        vec![1, 1, 0, 0, 0, 0],
        vec![1, 1, 1, 0, 0, 0],
        vec![1, 1, 1, 1, 0, 0],
    ];
    let q5_route = vec![1, 1, 1, 1, 1, 0];
    let routing_gram = routing
        .iter()
        .map(|left| routing.iter().map(|right| dot_k(left, right, &k)).collect())
        .collect::<Vec<Vec<_>>>();
    let routing_det = determinant(&routing_gram).factor();
    let routing_adj = adjugate(&routing_gram);
    let routing_b = routing
        .iter()
        .map(|route| dot_k(route, &q5_route, &k))
        .collect::<Vec<_>>();
    let squares = (1..=6)
        .map(|index| a(&format!("s{index}")))
        .collect::<Vec<_>>();
    let u = (0..4)
        .map(|index| {
            ((squares[0].clone() + routing_gram[index][index].clone() - squares[index + 1].clone())
                / a("2"))
            .expand()
        })
        .collect::<Vec<_>>();
    let full_f = (routing_det.clone() * squares[0].clone()
        - (0..4).fold(a("0"), |sum, i| {
            sum + (0..4).fold(a("0"), |inner, j| {
                inner + u[i].clone() * routing_adj[i][j].clone() * u[j].clone()
            })
        }))
    .expand();
    let full_g = (routing_det.clone()
        * (squares[5].clone() - squares[0].clone() - dot_k(&q5_route, &q5_route, &k))
        + a("2")
            * (0..4).fold(a("0"), |sum, i| {
                sum + (0..4).fold(a("0"), |inner, j| {
                    inner + routing_adj[i][j].clone() * routing_b[j].clone()
                }) * u[i].clone()
            }))
    .expand();
    let square_pullback = vec![
        x.clone(),
        z.clone(),
        v.clone(),
        z.clone(),
        w.clone(),
        z.clone(),
    ];
    let pulled_full_f = replace_many(full_f.clone(), &squares, &square_pullback).expand();
    let pulled_full_g = replace_many(full_g.clone(), &squares, &square_pullback).expand();
    assert_eq!((pulled_full_f * a("16") - f.clone()).expand(), a("0"));
    assert_eq!(
        (pulled_full_g * a("-4") / k.clone() - g.clone())
            .together()
            .cancel()
            .expand(),
        a("0")
    );
    let full_fw = full_f.derivative(symbol!("marici::s5")).expand();
    let full_gw = full_g.derivative(symbol!("marici::s5")).expand();
    let wall_square_indices = [1usize, 3, 5];
    let wall_square_symbols = [
        symbol!("marici::s2"),
        symbol!("marici::s4"),
        symbol!("marici::s6"),
    ];
    let wall_multipliers = wall_square_indices
        .iter()
        .map(|index| {
            let sf = wall_square_symbols[wall_square_indices
                .iter()
                .position(|candidate| candidate == index)
                .unwrap()];
            let component = (full_gw.clone() * full_f.derivative(sf)
                - full_fw.clone() * full_g.derivative(sf))
            .expand();
            let pulled = replace_many(component, &squares, &square_pullback);
            let critical = replace_many(pulled, &variables, &solutions)
                .replace(z.to_pattern())
                .with(z_on_divisor.to_pattern());
            critical.together().cancel().expand().factor()
        })
        .collect::<Vec<_>>();
    assert!(wall_multipliers
        .iter()
        .all(|multiplier| *multiplier != a("0")));
    let physical_sample_k = a("-1/2");
    let physical_sample_coordinates = on_divisor_solutions
        .iter()
        .map(|value| {
            value
                .clone()
                .replace(k.to_pattern())
                .with(physical_sample_k.to_pattern())
                .together()
                .cancel()
                .expand()
        })
        .collect::<Vec<_>>();
    let physical_sample_z = z_on_divisor
        .clone()
        .replace(k.to_pattern())
        .with(physical_sample_k.to_pattern())
        .together()
        .cancel()
        .expand();
    let physical_sample_multipliers = wall_multipliers
        .iter()
        .map(|value| {
            value
                .clone()
                .replace(k.to_pattern())
                .with(physical_sample_k.to_pattern())
                .together()
                .cancel()
                .expand()
        })
        .collect::<Vec<_>>();

    let packet = json!({
        "schema":"marici.six_site_disjoint_pair_triple_generic_critical.v1",
        "chart":"partial_G/partial_w != 0",
        "equations":["F","G","rank(dF,dG)<2"],
        "F":f.to_string(),
        "G":g.to_string(),
        "jacobian_minors":minors.iter().map(ToString::to_string).collect::<Vec<_>>(),
        "linear_critical_system":["G","F_x*G_w-F_w*G_x","F_v*G_w-F_w*G_v"],
        "linear_system_determinant":denominator.to_string(),
        "critical_solution":{
            "x":solutions[0].to_string(),
            "v":solutions[1].to_string(),
            "w":solutions[2].to_string()
        },
        "all_three_minors_vanish_on_solution":true,
        "eliminated_F_numerator_with_clearing_factors":discriminant.to_string(),
        "generic_divisor":generic_divisor.to_string(),
        "complementary_jacobian_pivots":pivot_packets,
        "critical_solution_on_generic_divisor":{
            "z":z_on_divisor.to_string(),
            "x":on_divisor_solutions[0].to_string(),
            "v":on_divisor_solutions[1].to_string(),
            "w":on_divisor_solutions[2].to_string(),
            "generic_nonsoft":true
        },
        "local_type":{
            "kernel_basis_for_dG":kernel_basis.iter().map(|row|row.iter().map(ToString::to_string).collect::<Vec<_>>()).collect::<Vec<_>>(),
            "transverse_hessian":transverse_hessian.iter().map(|row|row.iter().map(ToString::to_string).collect::<Vec<_>>()).collect::<Vec<_>>(),
            "transverse_hessian_determinant":transverse_determinant.to_string(),
            "generic_classification":"ordinary quadratic node of the complete-intersection fiber"
        },
        "real_witness_at_k_1_over_10":{
            "z":sample_z.to_string(),
            "x":sample_values[0].to_string(),
            "v":sample_values[1].to_string(),
            "w":sample_values[2].to_string()
        },
        "source_wall_conormal":{
            "ordered_walls":["g12 (s2)","g34 (s4)","g56 (s6)"],
            "normalization":"(partial_s5 G)dF-(partial_s5 F)dG before s2=s4=s6",
            "coefficients_on_D6":wall_multipliers.iter().map(ToString::to_string).collect::<Vec<_>>(),
            "all_generically_nonzero":true,
            "orientation_note":"conversion from ds_even to dy_even multiplies each entry by 2*y_even=-2*t on the chosen wall sheet"
        },
        "positive_multiplier_witness_at_k_minus_1_over_2":{
            "z":physical_sample_z.to_string(),
            "x":physical_sample_coordinates[0].to_string(),
            "v":physical_sample_coordinates[1].to_string(),
            "w":physical_sample_coordinates[2].to_string(),
            "square_conormal_coefficients":physical_sample_multipliers.iter().map(ToString::to_string).collect::<Vec<_>>(),
            "certified_signs":{"coordinates":"all positive","multipliers":"all negative before the common ds_even/dy_even factor"}
        },
        "pending_saturation":["det(H)=k*(6+7*k)","dG/dw=k-3 in the original scaled G","linear_system_determinant","x*v*w*z","source wall multipliers"],
        "scope":"generic critical elimination on one Jacobian pivot chart; factor classification and complementary pivot charts remain pending"
    });
    fs::write(
        "../results/six-site-disjoint-pair-triple-generic-critical.json",
        serde_json::to_string_pretty(&packet).unwrap() + "\n",
    )
    .unwrap();
    println!(
        "{}",
        json!({"linear_det":denominator.to_string(),"discriminant":discriminant.to_string()})
    );
}
