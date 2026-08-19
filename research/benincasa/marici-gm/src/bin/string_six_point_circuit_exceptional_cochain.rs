use serde_json::{json, Value};
use symbolica::prelude::*;

fn a(s: &str) -> Atom {
    Atom::parse(s, "marici", Default::default()).unwrap()
}
fn clean(x: Atom) -> Atom {
    x.together().cancel().factor()
}

fn main() {
    let prior: Value = serde_json::from_str(
        &std::fs::read_to_string("../string-six-point-exceptional-row-factorization.json").unwrap(),
    )
    .unwrap();
    let u: Vec<Atom> = prior["factorizations"]
        .as_array()
        .unwrap()
        .iter()
        .map(|x| a(x["quotient"].as_str().unwrap()))
        .collect();
    assert_eq!(u.len(), 6);

    let f = [
        a("(Z*A2)^2-1"),
        a("(Z*A2*B24)^2-1"),
        a("(Z*A2*B24)^2-1"),
        a("(A3/Z)^2-1"),
        a("(A3*B34/Z)^2-1"),
        a("(A3*B34/Z)^2-1"),
    ];
    let desired: Vec<Atom> = (0..6).map(|i| clean(f[i].clone() * u[i].clone())).collect();

    // Unique target cochain in dense chamber-row order.  Singleton columns
    // fix lambda_1, lambda_3, lambda_4, lambda_5.  The two oriented circuit
    // columns then force the endpoint differences lambda_3-lambda_2 and
    // lambda_1-lambda_0.
    let lambda = [
        clean(u[0].clone() - u[4].clone()),
        u[0].clone(),
        clean(u[3].clone() - u[1].clone()),
        u[3].clone(),
        u[2].clone(),
        u[5].clone(),
    ];

    let mut c = vec![vec![a("0"); 6]; 6];
    c[1][0] = f[0].clone();
    c[2][1] = -f[1].clone();
    c[3][1] = f[1].clone();
    c[4][2] = f[2].clone();
    c[3][3] = f[3].clone();
    c[0][4] = -f[4].clone();
    c[1][4] = f[4].clone();
    c[5][5] = f[5].clone();

    let evaluated: Vec<Atom> = (0..6)
        .map(|j| {
            clean(
                (0..6)
                    .map(|i| lambda[i].clone() * c[i][j].clone())
                    .fold(a("0"), |sum, x| sum + x),
            )
        })
        .collect();
    for i in 0..6 {
        assert_eq!(clean(evaluated[i].clone() - desired[i].clone()), a("0"));
    }
    assert_eq!(clean(lambda[3].clone() - lambda[2].clone() - u[1].clone()), a("0"));
    assert_eq!(clean(lambda[1].clone() - lambda[0].clone() - u[4].clone()), a("0"));

    let packet = json!({
        "schema":"marici.benincasa.string_six_point_circuit_exceptional_cochain.v1",
        "target_row_order":["123456","124356","132456","134256","142356","143256"],
        "cochain":lambda.iter().map(ToString::to_string).collect::<Vec<_>>(),
        "circuit_equations":[
            {"column":1,"orientation":"-132456+134256","identity":"lambda_3-lambda_2=u_1"},
            {"column":4,"orientation":"-123456+124356","identity":"lambda_1-lambda_0=u_4"}
        ],
        "singleton_equations":[
            "lambda_1=u_0","lambda_4=u_2","lambda_3=u_3","lambda_5=u_5"
        ],
        "all_six_evaluations_match":true,
        "generic_uniqueness":"the loaded matrix is generically invertible by Entry 967",
        "classification":"the exact exceptional row has a unique lift as a cochain on the frozen loaded incidence matrix; circuit columns evaluate by oriented endpoint differences",
        "scope":"rank-one cochain comparison; not a six-dimensional chain equivalence or horizontal connection map"
    });
    let text = serde_json::to_string_pretty(&packet).unwrap() + "\n";
    std::fs::write("../string-six-point-circuit-exceptional-cochain.json", &text).unwrap();
    print!("{text}");
}
