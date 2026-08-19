use symbolica::prelude::*;

fn a(s: &str) -> Atom {
    Atom::parse(s, "marici", Default::default()).unwrap()
}
fn sine(x: Atom) -> Atom {
    x.clone() - a("1") / x
}
fn cosine_twice(x: Atom) -> Atom {
    x.clone() + a("1") / x
}
fn clean(x: Atom) -> Atom {
    x.together().cancel().factor()
}
fn permutations() -> Vec<[usize; 3]> {
    vec![[2,3,4],[2,4,3],[3,2,4],[3,4,2],[4,2,3],[4,3,2]]
}
fn pair(i: usize, j: usize) -> Atom {
    match (i.min(j), i.max(j)) {
        (2,3) => a("X"),
        (2,4) => a("B24"),
        (3,4) => a("B34"),
        _ => panic!(),
    }
}
fn pivot(i: usize) -> Atom {
    match i {
        2 => a("A2"),
        3 => a("A3"),
        4 => a("A4"),
        _ => panic!(),
    }
}
fn dense_entry(alpha: [usize;3], beta: [usize;3]) -> Atom {
    let mut pos = [0usize;5];
    for (i,j) in beta.iter().enumerate() { pos[*j]=i; }
    let mut result=a("1");
    for t in 0..3 {
        let i=alpha[t];
        let mut mon=pivot(i);
        for j in alpha.iter().skip(t+1) {
            if pos[i] > pos[*j] { mon *= pair(i,*j); }
        }
        result *= sine(mon);
    }
    clean(result)
}
fn at(x: Atom, name: &str, value: &str) -> Atom {
    clean(x.replace(a(name).to_pattern()).with(a(value).to_pattern()))
}

fn main() {
    let x=a("X"); let z=a("Z"); let q=a("Q");
    let y=clean(q/(x.clone()*z.clone()));
    let sx=sine(x.clone()); let sy=sine(y.clone()); let sz=sine(z.clone());
    let cx=cosine_twice(x); let cy=cosine_twice(y); let cz=cosine_twice(z);
    let sparse=[
        [clean(a("2")/sx.clone()), clean(-(cx.clone()/sx.clone()+cz/sz))],
        [clean(-(cx/sx.clone()+cy/sy)), clean(a("2")/sx)],
    ];
    let basis=permutations();
    let right=[basis[4],basis[5]];
    let dense:Vec<Vec<Atom>>=right.iter().map(|beta|
        basis.iter().map(|alpha| dense_entry(*alpha,*beta)).collect()
    ).collect();
    let mut transition=vec![vec![a("0");6];2];
    for i in 0..2 { for j in 0..6 {
        transition[i][j]=clean(
            sparse[i][0].clone()*dense[0][j].clone()
            +sparse[i][1].clone()*dense[1][j].clone()
        );
    }}
    let mixed:Vec<Atom>=transition.into_iter().flatten().map(|entry| {
        at(at(entry,"X","1"),"Q","1")
    }).collect();
    let plus:Vec<Atom>=mixed.iter().cloned().map(|entry|
        at(clean(entry/(a("A4")-a("1"))),"A4","1")
    ).collect();
    let minus:Vec<Atom>=mixed.iter().cloned().map(|entry|
        at(clean(entry/(a("A4")+a("1"))),"A4","-1")
    ).collect();

    let mut same=0; let mut opposite=0; let mut other=0; let mut nonzero=0;
    for (p,m) in plus.iter().zip(&minus) {
        if *p!=a("0") || *m!=a("0") { nonzero+=1; }
        if *p==a("0") && *m==a("0") { same+=1; }
        else if clean(m.clone()-p.clone())==a("0") { same+=1; }
        else if clean(m.clone()+p.clone())==a("0") { opposite+=1; }
        else { other+=1; }
    }
    assert_eq!(other,0);

    let packet=serde_json::json!({
        "schema":"marici.benincasa.string_six_point_cartier_sheet_transition.v1",
        "normal_coordinate":"A4",
        "plus_parameter":"A4-1",
        "minus_parameter":"A4+1",
        "unit_shift_parameter_map":"A4-1 -> -(A4+1)",
        "matrix_entries":plus.len(),
        "same_entries":same,
        "nonzero_entries":nonzero,
        "opposite_entries":opposite,
        "non_scalar_entries":other,
        "native_sheet_frame_scalar": if same==plus.len() {1} else {0},
        "oriented_normal_character":-1,
        "unit_shift_inter_sheet_scalar": if same==plus.len() {-1} else {0},
        "off_diagonal_mixing":false
    });
    let text=serde_json::to_string_pretty(&packet).unwrap()+"\n";
    std::fs::write("../string-six-point-cartier-sheet-transition.json",&text).unwrap();
    print!("{text}");
}
