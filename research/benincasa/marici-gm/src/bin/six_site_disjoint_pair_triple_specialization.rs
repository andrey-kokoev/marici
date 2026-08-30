use serde_json::json;
use std::fs;
use symbolica::prelude::*;

fn a(source: &str) -> Atom {
    Atom::parse(source, "marici", Default::default())
        .unwrap()
        .expand()
}

fn at_zero(expression: Atom, variable: &Atom) -> Atom {
    expression
        .replace(variable.to_pattern())
        .with(a("0").to_pattern())
        .expand()
}

fn main() {
    let k = a("k");
    let x = a("x");
    let v = a("v");
    let w = a("w");
    let z = a("z");
    let aa = a("1026+69*k-500*k^2+196*k^3");
    let nz = a("5586+5341*k+98*k^2+392*k^3");
    let nx = a("2*(4674+3161*k-247*k^2+658*k^3)");
    let nv = a("2*(2622+2981*k-10*k^2)");
    let nw = a("2*(2622+209*k-934*k^2+616*k^3)");

    let closure_equations = vec![
        (aa.clone() * z.clone() - nz.clone()).expand(),
        (aa.clone() * x.clone() - nx.clone()).expand(),
        (aa.clone() * v.clone() - nv.clone()).expand(),
        (aa.clone() * w.clone() - nw.clone()).expand(),
    ];
    let special_fiber = closure_equations
        .iter()
        .map(|equation| at_zero(equation.clone(), &k).factor())
        .collect::<Vec<_>>();
    let point = [a("82/9"), a("46/9"), a("46/9"), a("49/9")];
    let variables = [x.clone(), v.clone(), w.clone(), z.clone()];
    for equation in &special_fiber {
        let value = variables
            .iter()
            .zip(&point)
            .fold(equation.clone(), |current, (variable, value)| {
                current
                    .replace(variable.to_pattern())
                    .with(value.to_pattern())
            })
            .expand();
        assert_eq!(value, a("0"));
    }
    let special_jacobian = (0..4)
        .map(|row| {
            (0..4)
                .map(|column| {
                    special_fiber[row]
                        .derivative(
                            [
                                symbol!("marici::x"),
                                symbol!("marici::v"),
                                symbol!("marici::w"),
                                symbol!("marici::z"),
                            ][column],
                        )
                        .expand()
                })
                .collect::<Vec<_>>()
        })
        .collect::<Vec<_>>();
    let pivot_columns = [3usize, 0, 1, 2];
    assert!((0..4).all(|row| special_jacobian[row][pivot_columns[row]] == a("1026")));
    assert!((0..4).all(|row| (0..4)
        .all(|column| column == pivot_columns[row] || special_jacobian[row][column] == a("0"))));

    let l = a("-2+x-6*z+4*v+w");
    let m = a("-6+2*x-6*z+5*v-w");
    let point_substitution = |expression: Atom| {
        variables
            .iter()
            .zip(&point)
            .fold(expression, |current, (variable, value)| {
                current
                    .replace(variable.to_pattern())
                    .with(value.to_pattern())
            })
            .expand()
    };
    assert_eq!(point_substitution(l.clone()), a("0"));
    assert_eq!(point_substitution(m.clone()), a("0"));

    let divisor = a("-5586-5341*k-98*k^2-392*k^3+z*(1026+69*k-500*k^2+196*k^3)");
    let divisor_special = at_zero(divisor.clone(), &k).factor();
    assert_eq!(
        divisor_special.clone().expand(),
        a("114*(-49+9*z)").expand()
    );
    assert_eq!(
        divisor
            .derivative(symbol!("marici::z"))
            .replace(k.to_pattern())
            .with(a("0").to_pattern())
            .expand(),
        a("1026")
    );

    let multiplier_factors = vec![
        a("7/8*k^2*(-3+k)*(6+7*k)*(114+73*k-10*k^2+16*k^3)/(1026+69*k-500*k^2+196*k^3)"),
        a("1/8*k^2*(-3+k)*(6+7*k)*(-570-1457*k-528*k^2+84*k^3)/(1026+69*k-500*k^2+196*k^3)"),
        a("7/8*k^2*(-3+k)*(6+7*k)^2*(19+2*k)/(1026+69*k-500*k^2+196*k^3)"),
    ];
    let multiplier_second_grades = multiplier_factors
        .iter()
        .map(|entry| {
            at_zero(
                (entry.clone() / k.clone() / k.clone()).together().cancel(),
                &k,
            )
            .expand()
        })
        .collect::<Vec<_>>();
    assert!(multiplier_second_grades
        .iter()
        .all(|grade| *grade != a("0")));

    let hessian_det = a("-k*(6+7*k)^2*(1026+69*k-500*k^2+196*k^3)/(-3+k)^2");
    let hessian_first_grade =
        at_zero((hessian_det.clone() / k.clone()).together().cancel(), &k).expand();
    assert_ne!(hessian_first_grade, a("0"));

    let packet = json!({
        "schema":"marici.six_site_disjoint_pair_triple_specialization.v1",
        "generic_branch_closure":{
            "equations":closure_equations.iter().map(ToString::to_string).collect::<Vec<_>>(),
            "special_fiber_equations":special_fiber.iter().map(ToString::to_string).collect::<Vec<_>>(),
            "special_point":{"x":"82/9","v":"46/9","w":"46/9","z":"49/9"},
            "special_fiber_jacobian":"1026 times the permutation matrix for equation order (z,x,v,w)",
            "reduced_length":1
        },
        "homogeneous_exceptional_object":{
            "ideal":["L^2","M"],
            "L":l.to_string(),
            "M":m.to_string(),
            "support":"affine critical line",
            "Cartier_length_along_support":2
        },
        "intersection":{
            "generic_divisor_at_k_zero":divisor_special.to_string(),
            "dz_coefficient_at_k_zero":"1026",
            "point_lies_on_exceptional_support":true,
            "base_intersection_multiplicity":1
        },
        "normal_orders":{
            "three_source_wall_multipliers":2,
            "multiplier_second_grades":multiplier_second_grades.iter().map(ToString::to_string).collect::<Vec<_>>(),
            "transverse_hessian_determinant":1,
            "hessian_first_grade":hessian_first_grade.to_string()
        },
        "conclusion":"the physical generic branch meets the homogeneous Cartier support transversely at one reduced point; it does not specialize to the length-two Cartier line",
        "classification":"horizontal physical coefficient divisor plus an additional vertical Gram-supported Cartier excess; no new carrier datum"
    });
    fs::write(
        "../results/six-site-disjoint-pair-triple-specialization.json",
        serde_json::to_string_pretty(&packet).unwrap() + "\n",
    )
    .unwrap();
    println!(
        "{}",
        json!({"special_point":"(82/9,46/9,46/9,49/9)","closure_length":1,"cartier_length":2,"equal":false})
    );
}
