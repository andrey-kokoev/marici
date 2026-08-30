use serde_json::{json, Value};
use std::fs;
use symbolica::prelude::*;

fn a(source: &str) -> Atom {
    Atom::parse(source, "marici", Default::default())
        .unwrap()
        .expand()
}

fn replace(expression: Atom, variable: &Atom, value: &Atom) -> Atom {
    expression
        .replace(variable.to_pattern())
        .with(value.to_pattern())
}

fn coefficients(polynomial: &Atom, variable: Symbol, variable_name: &str) -> Vec<Atom> {
    let mut derivative = polynomial.clone().expand();
    let mut factorial = 1usize;
    let mut output = Vec::new();
    loop {
        output.push(
            (derivative.clone() / a(&factorial.to_string()))
                .replace(a(variable_name).to_pattern())
                .with(a("0").to_pattern())
                .expand(),
        );
        let next = derivative.derivative(variable).expand();
        if next == a("0") {
            break;
        }
        derivative = next;
        factorial *= output.len();
    }
    while output.len() > 1 && output.last() == Some(&a("0")) {
        output.pop();
    }
    output
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

fn resultant(left: &Atom, right: &Atom, variable: Symbol, name: &str) -> Atom {
    let left_coefficients = coefficients(left, variable, name);
    let right_coefficients = coefficients(right, variable, name);
    let left_degree = left_coefficients.len() - 1;
    let right_degree = right_coefficients.len() - 1;
    assert!(left_degree > 0 && right_degree > 0);
    let size = left_degree + right_degree;
    let mut sylvester = vec![vec![a("0"); size]; size];
    let left_descending = left_coefficients.iter().rev().cloned().collect::<Vec<_>>();
    let right_descending = right_coefficients.iter().rev().cloned().collect::<Vec<_>>();
    for row in 0..right_degree {
        for (column, coefficient) in left_descending.iter().enumerate() {
            sylvester[row][row + column] = coefficient.clone();
        }
    }
    for row in 0..left_degree {
        for (column, coefficient) in right_descending.iter().enumerate() {
            sylvester[right_degree + row][row + column] = coefficient.clone();
        }
    }
    determinant(&sylvester).expand().factor()
}

fn main() {
    let packet: Value = serde_json::from_str(
        &fs::read_to_string("../results/seven-site-multiloop-cover.json").unwrap(),
    )
    .unwrap();
    let f = a(packet["pulled_cover"]["F1"].as_str().unwrap());
    let g = a(packet["pulled_cover"]["F6"].as_str().unwrap());
    let h = a(packet["pulled_cover"]["F7"].as_str().unwrap());
    let k = a("k");
    let x = a("x");
    let w = a("w");
    let c = a("2*k^2-3*k-1").factor();
    let fx = f.derivative(symbol!("marici::x")).factor();
    let gx = g.derivative(symbol!("marici::x")).factor();
    let hw = h.derivative(symbol!("marici::w")).factor();
    let fw = f.derivative(symbol!("marici::w")).expand();
    let gw = g.derivative(symbol!("marici::w")).expand();
    assert_eq!(fw, a("0"));
    assert_eq!(gw, a("0"));
    assert_eq!(hw.clone(), a("-1/4*k*(6+7*k)").factor());
    assert_eq!(gx.clone(), a("1/4*(6+7*k)*(2*k^2-3*k-1)").factor());

    // Away from routing Gram, the 3x2 Jacobian drops rank precisely when
    // F_x=G_x=0. G_x contributes the irreducible quadratic C(k).
    let f_coefficients = coefficients(&f, symbol!("marici::x"), "x");
    assert_eq!(f_coefficients.len(), 3);
    let discriminant = (f_coefficients[1].clone() * f_coefficients[1].clone()
        - a("4") * f_coefficients[2].clone() * f_coefficients[0].clone())
    .expand()
    .factor();
    let g0 = replace(g.clone(), &x, &a("0")).factor();
    let h0 = replace(h.clone(), &w, &a("0")).factor();
    let resultant_c_g0 = resultant(&c, &g0, symbol!("marici::k"), "k");
    let resultant_c_discriminant = resultant(&c, &discriminant, symbol!("marici::k"), "k");
    assert_ne!(resultant_c_g0, a("0"));
    assert_ne!(resultant_c_discriminant, a("0"));

    // H is linear in w with Gram coefficient, so on the Gram-saturated chart
    // it determines w uniquely and creates no additional Jacobian condition.
    let w_solution = (-h0 / hw.clone()).together().cancel().expand();
    let gram_previews = [a("0"), a("-6/7")]
        .iter()
        .map(|value| {
            json!({
                "k":value.to_string(),
                "F":replace(f.clone(),&k,value).factor().to_string(),
                "G":replace(g.clone(),&k,value).factor().to_string(),
                "H":replace(h.clone(),&k,value).factor().to_string()
            })
        })
        .collect::<Vec<_>>();
    let critical = json!({
        "schema":"marici.seven_site_multiloop_critical.v1",
        "critical_variables":["x","w"],
        "jacobian":{
            "F_x":fx.to_string(),"F_w":"0",
            "G_x":gx.to_string(),"G_w":"0",
            "H_x":h.derivative(symbol!("marici::x")).factor().to_string(),"H_w":hw.to_string()
        },
        "Gram_saturation":"invert k*(6+7*k)",
        "rank_drop_equations_after_Gram_saturation":["F_x=0","G_x=0"],
        "horizontal_indicial_factor":c.to_string(),
        "elimination_on_C":{
            "G_at_x0":g0.to_string(),
            "Disc_x_F":discriminant.to_string(),
            "Res_k(C,G_at_x0)":resultant_c_g0.to_string(),
            "Res_k(C,Disc_x_F)":resultant_c_discriminant.to_string(),
            "w_solution":w_solution.to_string()
        },
        "codimension_certificate":"C is irreducible over Q and G|_{x=0} is not divisible by C; every Gram-saturated critical component therefore has base codimension at least two, not one. Disc_x(F)=0 supplies the remaining displayed critical equation without being used to overclaim a codimension-three regular sequence",
        "generic_divisor_conclusion":"no horizontal physical divisor",
        "remaining_supported_center":"C(k)=0 together with G|_{x=0}=0 and Disc_x(F)=0; H fixes w",
        "Gram_fiber_previews":gram_previews,
        "classification_pending":"classify the higher-codimension center against soft and lower-incidence support, then audit both Gram components"
    });
    fs::write(
        "../results/seven-site-multiloop-critical.json",
        serde_json::to_string_pretty(&critical).unwrap() + "\n",
    )
    .unwrap();
    println!(
        "{}",
        json!({"C":c.to_string(),"Res_C_G0_nonzero":resultant_c_g0!=a("0"),"Res_C_Disc_nonzero":resultant_c_discriminant!=a("0"),"conclusion":"no horizontal divisor"})
    );
}
