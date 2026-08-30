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
            if column % 2 == 0 { sum + term } else { sum - term }
        })
        .expand()
}

fn main() {
    let av = a("a");
    let bv = a("b");
    let cv = a("c");
    let dv = a("d");
    let variables = ["a", "b", "c", "d"]
        .iter()
        .map(|name| Symbol::parse(*name, "marici").unwrap())
        .collect::<Vec<_>>();

    // det(X) for X with unit diagonal, cycle edges a,b,c,d, and deleted chords.
    let det_x = a("1-a^2-b^2-c^2-d^2+a^2*c^2+b^2*d^2-2*a*b*c*d");
    let numerators = vec![
        (-av.clone() * av.clone() + av.clone() * av.clone() * cv.clone() * cv.clone()
            - av.clone() * bv.clone() * cv.clone() * dv.clone()).expand(),
        (-bv.clone() * bv.clone() + bv.clone() * bv.clone() * dv.clone() * dv.clone()
            - av.clone() * bv.clone() * cv.clone() * dv.clone()).expand(),
        (-cv.clone() * cv.clone() + av.clone() * av.clone() * cv.clone() * cv.clone()
            - av.clone() * bv.clone() * cv.clone() * dv.clone()).expand(),
        (-dv.clone() * dv.clone() + bv.clone() * bv.clone() * dv.clone() * dv.clone()
            - av.clone() * bv.clone() * cv.clone() * dv.clone()).expand(),
    ];

    // The common denominator 4 det(X) contributes only a unit on the positive
    // covariance locus.  Clear it row-wise before factoring the Jacobian.
    let cleared_jacobian = numerators
        .iter()
        .map(|numerator| {
            variables
                .iter()
                .map(|variable| {
                    (numerator.derivative(*variable) * det_x.clone()
                        - numerator.clone() * det_x.derivative(*variable))
                        .expand()
                })
                .collect::<Vec<_>>()
        })
        .collect::<Vec<_>>();
    let cleared_det = determinant(&cleared_jacobian).factor();
    let rankdrop = (cleared_det.clone() / (a("8") * det_x.clone().pow(3)))
        .together().factor();

    let ua = a("-a+a*c^2-b*c*d");
    let ub = a("-b+b*d^2-a*c*d");
    let uc = a("-c+a^2*c-a*b*d");
    let ud = a("-d+b^2*d-a*b*c");
    let cycle_numerator = (av.clone() * cv.clone() * ub * ud
        + bv.clone() * dv.clone() * ua * uc).expand();
    // L=N_L/(16 det(X)^2); clear the common denominator in its gradient.
    let cycle_row = variables.iter().map(|variable| {
        (cycle_numerator.derivative(*variable) * det_x.clone()
            - a("2") * cycle_numerator.clone() * det_x.derivative(*variable))
            .expand()
    }).collect::<Vec<_>>();
    let augmented_minors = (0..4).map(|omitted| {
        let mut matrix = cleared_jacobian.iter().enumerate()
            .filter(|(row,_)| *row != omitted)
            .map(|(_,row)|row.clone()).collect::<Vec<_>>();
        matrix.push(cycle_row.clone());
        determinant(&matrix).factor()
    }).collect::<Vec<_>>();
    let rankdrop_poly = rankdrop.to_polynomial::<_, u16>(&Q, variables.clone());
    let augmented_gcds = augmented_minors.iter()
        .map(|minor| {
            let minor_poly = minor.to_polynomial::<_, u16>(&Q, variables.clone());
            rankdrop_poly.gcd(&minor_poly).to_expression().factor()
        })
        .collect::<Vec<_>>();
    let symmetric_ac_bd = cleared_det
        .replace(a("c").to_pattern()).with(a("a").to_pattern())
        .replace(a("d").to_pattern()).with(a("b").to_pattern())
        .expand().factor();
    let equal_cycle = cleared_det
        .replace(a("b").to_pattern()).with(a("a").to_pattern())
        .replace(a("c").to_pattern()).with(a("a").to_pattern())
        .replace(a("d").to_pattern()).with(a("a").to_pattern())
        .expand().factor();

    let packet = json!({
        "schema":"marici.four-mode-chord-deletion-symbolic-jacobian.v1",
        "det_X":det_x.factor().to_string(),
        "edge_numerators":numerators.iter().map(|x|x.factor().to_string()).collect::<Vec<_>>(),
        "cleared_jacobian_determinant":cleared_det.to_string(),
        "physical_rankdrop_polynomial":rankdrop.to_string(),
        "cycle_numerator":cycle_numerator.factor().to_string(),
        "augmented_minors":augmented_minors.iter().map(ToString::to_string).collect::<Vec<_>>(),
        "rankdrop_augmented_gcds":augmented_gcds.iter().map(ToString::to_string).collect::<Vec<_>>(),
        "specialization_c_eq_a_d_eq_b":symmetric_ac_bd.to_string(),
        "specialization_all_edges_equal":equal_cycle.to_string(),
        "physical_denominator":"(4 det(X))^4",
        "scope":"Exact rank-drop divisor in the normalized block-diagonal pure Gaussian chord-deletion chart."
    });
    fs::write(
        "../results/four-mode-chord-deletion-symbolic-jacobian.json",
        serde_json::to_string_pretty(&packet).unwrap() + "\n",
    )
    .unwrap();
    println!("{}", serde_json::to_string_pretty(&packet).unwrap());
}
