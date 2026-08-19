use serde_json::{json, Value};
use symbolica::prelude::*;

fn a(s: &str) -> Atom {
    Atom::parse(s, "marici", Default::default()).unwrap()
}
fn clean(x: Atom) -> Atom {
    x.together().cancel().factor()
}
fn shift(v: &[Atom], name: &str) -> Vec<Atom> {
    v.iter()
        .cloned()
        .map(|x| {
            clean(
                x.replace(a(name).to_pattern())
                    .with((-a(name)).to_pattern()),
            )
        })
        .collect()
}
fn project(v: &[Atom], names: [&str; 2], ex: i32, ey: i32) -> Vec<Atom> {
    let x = shift(v, names[0]);
    let y = shift(v, names[1]);
    let xy = shift(&x, names[1]);
    (0..v.len())
        .map(|i| {
            clean(
                v[i].clone()
                    + a(&ex.to_string()) * x[i].clone()
                    + a(&ey.to_string()) * y[i].clone()
                    + a(&(ex * ey).to_string()) * xy[i].clone(),
            )
        })
        .collect()
}
fn eval(v: &[Atom], m: &[Vec<Atom>]) -> Vec<Atom> {
    (0..m[0].len())
        .map(|j| clean((0..v.len()).fold(a("0"), |s, i| s + v[i].clone() * m[i][j].clone())))
        .collect()
}
fn sigma_atom(mut x: Atom) -> Atom {
    for (from, to) in [
        ("A2", "TA2"),
        ("A3", "TA3"),
        ("A4", "TA4"),
        ("B23", "TB23"),
        ("B24", "TB24"),
        ("B34", "TB34"),
        ("Z0", "TZ0"),
        ("Z1", "TZ1"),
        ("Z2", "TZ2"),
    ] {
        x = x.replace(a(from).to_pattern()).with(a(to).to_pattern());
    }
    for (from, to) in [
        ("TA2", "A3"),
        ("TA3", "A4"),
        ("TA4", "A2"),
        ("TB23", "B34"),
        ("TB24", "B23"),
        ("TB34", "B24"),
        ("TZ0", "Z1"),
        ("TZ1", "Z2"),
        ("TZ2", "Z0"),
    ] {
        x = x.replace(a(from).to_pattern()).with(a(to).to_pattern());
    }
    clean(x)
}
fn sigma(v: &[Atom]) -> Vec<Atom> {
    let p = [3usize, 2, 5, 4, 0, 1];
    let mut out = vec![a("0"); 6];
    for i in 0..6 {
        out[p[i]] = sigma_atom(v[i].clone());
    }
    out
}
fn scale_add(x: &[Atom], q: Atom, y: &[Atom]) -> Vec<Atom> {
    (0..x.len())
        .map(|i| clean(x[i].clone() + q.clone() * y[i].clone()))
        .collect()
}
fn rename_z(v: Vec<Atom>) -> Vec<Atom> {
    v.into_iter()
        .map(|x| clean(x.replace(a("Z").to_pattern()).with(a("Z0").to_pattern())))
        .collect()
}

fn main() {
    let lp: Value = serde_json::from_str(
        &std::fs::read_to_string("../string-six-point-circuit-exceptional-cochain.json").unwrap(),
    )
    .unwrap();
    let cp: Value = serde_json::from_str(
        &std::fs::read_to_string("../string-six-point-loaded-corner-comparison.json").unwrap(),
    )
    .unwrap();
    let l: Vec<Atom> = lp["cochain"]
        .as_array()
        .unwrap()
        .iter()
        .map(|x| a(x.as_str().unwrap()))
        .collect();
    let c: Vec<Vec<Atom>> = cp["matrix"]
        .as_array()
        .unwrap()
        .iter()
        .map(|r| {
            r.as_array()
                .unwrap()
                .iter()
                .map(|x| a(x.as_str().unwrap()))
                .collect()
        })
        .collect();
    let occurrence = eval(&l, &c);
    let occurrence_to_dense = [4usize, 1, 0, 5, 3, 2];
    let mut loaded = vec![a("0"); 6];
    for i in 0..6 {
        loaded[occurrence_to_dense[i]] = occurrence[i].clone();
    }
    let loaded = rename_z(loaded);
    let normal = rename_z(vec![
        a("-2*(-1+A2*B24)*(-1+A3*B34)*(1+A2*B24)*(1+A3*B34)/(A2*B24*A3*B34)"),
        a("-2*(-1+A3)*(-1+A2*B24)*(1+A3)*(1+A2*B24)/(A2*B24*A3)"),
        a("-2*(-1+A2*B24)*(-1+A3*B34)*(1+A2*B24)*(1+A3*B34)/(A2*B24*A3*B34)"),
        a("-2*(-1+A2)*(-1+A3*B34)*(1+A2)*(1+A3*B34)/(A2*A3*B34)"),
        a("-2*(-1+A2)*(-1+A3)*(1+A2)*(1+A3)/(A2*A3)"),
        a("-2*(-1+A2)*(-1+A3)*(1+A2)*(1+A3)/(A2*A3)"),
    ]);
    let generators = [["B24", "B34"], ["B23", "B24"], ["B34", "B23"]];
    let mut records = Vec::new();
    for (label, ex, ey) in [("++", 1, 1), ("--", -1, -1)] {
        let mut lu = loaded.clone();
        let mut nu = normal.clone();
        let mut line0: Option<Vec<Atom>> = None;
        let mut previous: Option<Vec<Atom>> = None;
        let mut steps = Vec::new();
        for k in 0..3 {
            let lp = project(&lu, generators[k], ex, ey);
            let np = project(&nu, generators[k], ex, ey);
            let zk = format!("Z{k}");
            let g = clean((a("1") + a(&zk) * a(&zk)) / (a(&zk) * a(&zk) - a("1")));
            let line = scale_add(&lp, -g, &np);
            if k == 0 {
                line0 = Some(line.clone());
            }
            if let Some(prev) = previous.take() {
                assert_eq!(sigma(&prev), line);
                steps.push(true);
            }
            previous = Some(line);
            lu = sigma(&lu);
            nu = sigma(&nu);
        }
        let returned = sigma(previous.as_ref().unwrap());
        assert_eq!(returned, *line0.as_ref().unwrap());
        steps.push(true);
        records.push(json!({"character":label,"chart_generators":generators,"stepwise_line_covariance":steps,"three_step_holonomy":"identity"}));
    }
    let packet = json!({"schema":"marici.benincasa.string_six_point_corrected_line_cyclic_descent.v1","cyclic_label_action":"(234)","global_dense_word_permutation":[3,2,5,4,0,1],"planes":records,"classification":"the corrected minus eigenlines descend through all three cyclic occurrence charts with identity holonomy","scope":"source-labelled degree-zero six-word atlas"});
    let text = serde_json::to_string_pretty(&packet).unwrap() + "\n";
    std::fs::write(
        "../string-six-point-corrected-line-cyclic-descent.json",
        &text,
    )
    .unwrap();
    print!("{text}");
}
