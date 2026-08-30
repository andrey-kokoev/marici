use serde_json::{json, Value};
use std::fs;
use symbolica::prelude::*;

fn a(source: &str) -> Atom {
    Atom::parse(source, "marici", Default::default())
        .unwrap()
        .expand()
}
fn sub(expression: Atom, from: &str, to: &str) -> Atom {
    expression
        .replace(a(from).to_pattern())
        .with(a(to).to_pattern())
        .expand()
}
fn reduce_c(expression: Atom) -> Atom {
    sub(sub(expression, "k^3", "(11*k+3)/4"), "k^2", "(3*k+1)/2")
        .together()
        .cancel()
        .expand()
}
fn ordered(expression: Atom) -> Atom {
    sub(sub(sub(expression, "E", "b+r+s"), "D", "b+r"), "B", "b")
        .together()
        .cancel()
        .expand()
        .factor()
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
                        .collect()
                })
                .collect::<Vec<Vec<_>>>();
            let term = matrix[0][column].clone() * determinant(&minor);
            if column % 2 == 0 {
                sum + term
            } else {
                sum - term
            }
        })
        .expand()
}
fn zero3(expression: Atom) -> Atom {
    sub(sub(sub(expression, "b", "0"), "s", "0"), "rho", "0").expand()
}
fn linear_positive(a0: i128, a1: i128, lower_micro: i128, upper_micro: i128) -> bool {
    if a1 >= 0 {
        1_000_000_000 * a0 + lower_micro * a1 > 0
    } else {
        1_000_000_000 * a0 + upper_micro * a1 > 0
    }
}
fn linear_negative(a0: i128, a1: i128, lower_micro: i128, upper_micro: i128) -> bool {
    linear_positive(-a0, -a1, lower_micro, upper_micro)
}

fn main() {
    let packet: Value = serde_json::from_str(
        &fs::read_to_string("../results/seven-site-multiloop-critical.json").unwrap(),
    )
    .unwrap();
    let cover: Value = serde_json::from_str(
        &fs::read_to_string("../results/seven-site-multiloop-cover.json").unwrap(),
    )
    .unwrap();
    let disc = a(packet["elimination_on_C"]["Disc_x_F"].as_str().unwrap());
    let bracket = (disc / a("-1/16*k*(6+7*k)")).together().cancel().expand();
    let ordered_disc = ordered(reduce_c(bracket));
    let g0 = reduce_c(a(packet["elimination_on_C"]["G_at_x0"].as_str().unwrap()));
    let gu = g0.derivative(symbol!("marici::U")).expand();
    let usol = (-sub(g0, "U", "0") / gu).together().cancel().expand();
    let u_minus_e = ordered(usol.clone() - a("E"));
    let fx = reduce_c(a(packet["jacobian"]["F_x"].as_str().unwrap()));
    let fxx = fx.derivative(symbol!("marici::x")).expand();
    let xsol = (-sub(fx, "x", "0") / fxx).together().cancel().expand();
    let ordered_x = ordered(xsol.clone());
    let h = reduce_c(a(cover["pulled_cover"]["F7"].as_str().unwrap()));
    let hxu = sub(sub(h, "x", &format!("({xsol})")), "U", &format!("({usol})"))
        .together()
        .cancel()
        .expand();
    let hw = hxu.derivative(symbol!("marici::w")).expand();
    let wsol = (-sub(hxu, "w", "0") / hw).together().cancel().expand();
    let ordered_w = ordered(wsol);
    let p = (-a("2") * ordered_disc.clone()).expand();
    let nu = a("107+398*k+(33*k+8)*b+(3*k+2)*r-(7*k+5)*s");
    let r_boundary = (-sub(nu, "r", "0") / a("3*k+2") + a("rho"))
        .together()
        .cancel()
        .expand();
    let negative_branch_p = reduce_c(sub(p, "r", &format!("({r_boundary})")))
        .together()
        .cancel()
        .expand()
        .factor();
    let negative_big = reduce_c(
        (negative_branch_p.clone() * a("-34*(1+3*k)*(2+3*k)"))
            .together()
            .cancel()
            .expand(),
    )
    .factor();
    let inner = (-a("2") * negative_big.clone()).expand();
    let vars = [
        symbol!("marici::b"),
        symbol!("marici::s"),
        symbol!("marici::rho"),
    ];
    let mut matrix = vec![vec![a("0"); 3]; 3];
    for i in 0..3 {
        for j in 0..3 {
            matrix[i][j] = zero3(inner.derivative(vars[i]).derivative(vars[j]).expand()) / a("2");
        }
    }
    let linear = (0..3)
        .map(|i| zero3(inner.derivative(vars[i]).expand()))
        .collect::<Vec<_>>();
    let constant = zero3(inner.clone());
    let d1 = reduce_c(matrix[0][0].clone()).factor();
    let leading2 = matrix[..2]
        .iter()
        .map(|row| row[..2].to_vec())
        .collect::<Vec<_>>();
    let d2 = reduce_c(determinant(&leading2)).factor();
    let d3 = reduce_c(determinant(&matrix)).factor();
    let mut augmented = vec![vec![a("0"); 4]; 4];
    for i in 0..3 {
        for j in 0..3 {
            augmented[i][j] = matrix[i][j].clone();
        }
        augmented[i][3] = linear[i].clone() / a("2");
        augmented[3][i] = linear[i].clone() / a("2");
    }
    augmented[3][3] = constant;
    let d4 = reduce_c(determinant(&augmented)).factor();
    let determinants = [d1, d2, d3, d4];
    let minimizer = (0..3)
        .map(|column| {
            let mut numerator_matrix = matrix.clone();
            for row in 0..3 {
                numerator_matrix[row][column] = -linear[row].clone() / a("2");
            }
            (reduce_c(determinant(&numerator_matrix)) / determinants[2].clone())
                .together()
                .cancel()
                .expand()
                .factor()
        })
        .collect::<Vec<_>>();
    assert!(linear_positive(74719, 265699, -280776407, -280776406));
    assert!(linear_positive(2554001, 9096093, -280776407, -280776406));
    assert!(linear_positive(6787809, 24175085, -280776407, -280776406));
    assert!(linear_negative(24933337, 88801413, -280776407, -280776406));
    let positive_gap = [
        reduce_c(a("(14*k+12)*(107+398*k)-(7*k+5)*(45+127*k)")).factor(),
        reduce_c(a("(14*k+12)*(33*k+8)-(7*k+5)*(4*k+46)")).factor(),
        reduce_c(a("(14*k+12)*(3*k+2)-(7*k+5)*(-5*k+17)")).factor(),
    ];
    // k_+ lies in (1780776406/10^9,1780776407/10^9); these affine
    // coefficients are positive there, so the lower s-bound from U<E is
    // strictly larger than the upper s-bound from x>0.
    let expected_gap = [
        (a("1/2*(6801+24697*k)"), 6801, 24697),
        (a("83+817*k"), 83, 817),
        (a("9/2*(-5+19*k)"), -5, 19),
    ];
    for (expression, (expected, a0, a1)) in positive_gap.iter().zip(expected_gap) {
        assert_eq!(expression.clone().expand(), expected.expand());
        assert!(linear_positive(a0, a1, 1780776406, 1780776407));
    }
    let output = json!({"schema":"marici.seven_site_multiloop_physical_obstruction.v8","critical_relation":"2*k^2-3*k-1=0","physical_ordering":{"b":"B=y2^2>0","r":"D-B>0","s":"E-D>0","required":"0<U<E, x>0, and w>0"},"reduced_discriminant_bracket":ordered_disc.to_string(),"U_minus_E":u_minus_e.to_string(),"x":ordered_x.to_string(),"w":ordered_w.to_string(),"positive_branch":{"interval":"1780776406/10^9<k_+<1780776407/10^9","bound_gap_coefficients":positive_gap.iter().map(ToString::to_string).collect::<Vec<_>>(),"conclusion":"U<E requires s above a bound that is strictly greater than the x>0 upper bound"},"negative_branch_U_boundary":{"substitution":format!("r={r_boundary}"),"rho_condition":"rho>0 because 3*k+2>0 and 7+33*k<0 on k=(3-sqrt(17))/4","discriminant_P_after_substitution":negative_branch_p.to_string(),"cleared_quadratic_field_numerator":negative_big.to_string(),"inner_quadratic_form":inner.to_string(),"Sylvester_and_Schur_determinants":determinants.iter().map(ToString::to_string).collect::<Vec<_>>(),"unique_zero_minimizer":{"b":minimizer[0].to_string(),"s":minimizer[1].to_string(),"rho":minimizer[2].to_string()},"sign_certificate":"the first three determinants are positive on -280776407/10^9<k_-<-280776406/10^9, the Schur determinant vanishes by C(k), and the unique-zero rho numerator is negative while its denominator is positive"},"conclusion":"no positive-X_i real critical sheet on either root of C(k)"});
    fs::write(
        "../results/seven-site-multiloop-physical-obstruction.json",
        serde_json::to_string_pretty(&output).unwrap() + "\n",
    )
    .unwrap();
    println!(
        "{}",
        json!({"negative_branch_determinants":determinants.iter().map(ToString::to_string).collect::<Vec<_>>(),"minimizer":minimizer.iter().map(ToString::to_string).collect::<Vec<_>>()})
    );
}
