use serde_json::json;
use symbolica::prelude::*;

fn a(source: &str) -> Atom {
    Atom::parse(source, "marici", Default::default()).unwrap().expand()
}

fn determinant(matrix: &[Vec<Atom>]) -> Atom {
    if matrix.len() == 1 { return matrix[0][0].clone(); }
    (0..matrix.len()).fold(a("0"), |sum, column| {
        let minor = matrix.iter().skip(1).map(|row| {
            row.iter().enumerate().filter(|(index, _)| *index != column)
                .map(|(_, value)| value.clone()).collect::<Vec<_>>()
        }).collect::<Vec<_>>();
        let term = matrix[0][column].clone() * determinant(&minor);
        if column % 2 == 0 { sum + term } else { sum - term }
    }).expand()
}

fn main() {
    let routes = [
        "1/((x1+x2+x3+a)*(x2+x3+a+c))",
        "1/((x1+x2+x3+a)*(x3+x1+a+b))",
        "1/((x1+x2+x3+b)*(x3+x1+a+b))",
        "1/((x1+x2+x3+b)*(x1+x2+b+c))",
        "1/((x1+x2+x3+c)*(x1+x2+b+c))",
        "1/((x1+x2+x3+c)*(x2+x3+a+c))",
    ].map(a);
    let x1 = symbol!("marici::x1");
    let x2 = symbol!("marici::x2");
    let x3 = symbol!("marici::x3");
    let rows = vec![
        routes.to_vec(),
        routes.iter().map(|r| r.derivative(x1).expand()).collect(),
        routes.iter().map(|r| r.derivative(x2).expand()).collect(),
        routes.iter().map(|r| r.derivative(x3).expand()).collect(),
        routes.iter().map(|r| r.derivative(x1).derivative(x1).expand()).collect(),
        routes.iter().map(|r| r.derivative(x1).derivative(x2).expand()).collect(),
    ];
    let det = determinant(&rows).factor();
    assert_ne!(det, a("0"));
    println!("{}", json!({
        "status":"pass",
        "rows":["1","dX1","dX2","dX3","dX1dX1","dX1dX2"],
        "determinant":det.to_string()
    }));
}

