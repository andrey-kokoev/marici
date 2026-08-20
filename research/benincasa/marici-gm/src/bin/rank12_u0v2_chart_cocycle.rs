use symbolica::prelude::*;

fn a(text: &str) -> Atom {
    Atom::parse(text, "marici", Default::default()).unwrap().expand()
}
fn clean(x: Atom) -> Atom { x.expand().together().cancel().factor() }
fn zero_matrix() -> Vec<Vec<Atom>> { vec![vec![a("0"); 4]; 4] }

fn frame(matrix: &[Vec<Atom>], f: &Atom, variable: Symbol) -> Vec<Vec<Atom>> {
    let mut out = zero_matrix();
    for i in 0..4 {
        for j in 0..4 {
            let gi = if i == 3 { f.clone() } else { a("1") };
            let gj = if j == 3 { f.clone() } else { a("1") };
            out[i][j] = clean(gi * matrix[i][j].clone() / gj);
        }
    }
    out[3][3] = clean(out[3][3].clone() + f.derivative(variable) / f.clone());
    out
}

fn main() {
    let s = symbol!("marici::s");
    let r = symbol!("marici::r");
    let mut p = zero_matrix();
    p[0][0] = a("-1/s");
    p[0][1] = a("-(s+1)/(s*(s^2+6*s+1))");
    p[0][3] = a("3*(s^4-4*s^3-14*s^2-12*s-3)/(s*(s-1)*(s+3)*(s^2+3)*(s^2+6*s+1))");
    p[1][1] = a("-(s+3)/(s^2+6*s+1)");
    p[1][3] = a("-24*(s+1)^3/((s-1)*(s+3)*(s^2+3)*(s^2+6*s+1))");
    p[2][2] = a("-1/(s+1)");
    p[2][3] = a("-6*(s+1)/((s-1)*(s+3)*(s^2+3))");
    p[3][3] = a("(s^4+4*s^3+6*s^2-12*s+33)/((s-1)*(s+1)*(s+3)*(s^2+3))");
    let fp = a("-24/((s+3)*(s^2+3))");
    let p5 = frame(&p, &fp, s);

    let mut q = zero_matrix();
    q[0][0] = a("-1/r");
    q[0][1] = a("(r+1)/(r*(r^2+6*r+1))");
    q[0][3] = a("3*(1-4*r-14*r^2-12*r^3-3*r^4)/(-r^2-8*r^3-13*r^4-8*r^5-27*r^6+48*r^7+9*r^8)");
    q[1][1] = a("-(r+3)/(r^2+6*r+1)");
    q[1][3] = a("-24*(r+1)^3/(-r-8*r^2-13*r^3-8*r^4-27*r^5+48*r^6+9*r^7)");
    q[2][2] = a("-1/(r+1)");
    q[2][3] = a("-6*(r+1)/(-r-2*r^2-6*r^4+9*r^5)");
    q[3][3] = a("(1+4*r-18*r^2+36*r^3+9*r^4)/(-1-3*r-2*r^2-6*r^3+3*r^4+9*r^5)");
    let fq = a("-24*r^2/((1+3*r)*(1+3*r^2))");
    let q5 = frame(&q, &fq, r);

    let weights = [a("r^-2"), a("r^-1"), a("r^-1"), a("1")];
    let mut defects: Vec<(usize, usize, Atom)> = Vec::new();
    for i in 0..4 {
        for j in 0..4 {
            let pulled = p5[i][j]
                .clone().replace(a("s").to_pattern()).with(a("1/r").to_pattern())
                * a("-1/r^2");
            let mut expected = clean(weights[i].clone() * pulled / weights[j].clone());
            if i == j {
                expected = clean(expected + weights[i].derivative(r) / weights[i].clone());
            }
            let defect = clean(q5[i][j].clone() - expected);
            if defect != a("0") {
                defects.push((i, j, defect));
            }
        }
    }
    println!("quotient_rank=4");
    println!("overlap_transition=diag(r^-2,r^-1,r^-1,1)");
    println!("diagonal_transition_cocycle={}", defects.is_empty());
    println!("defect_count={}", defects.len());
    for (i, j, defect) in defects {
        println!("defect_{i}_{j}={defect}");
    }
}
