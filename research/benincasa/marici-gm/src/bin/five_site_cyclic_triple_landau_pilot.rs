use serde_json::{json, Value};
use std::fs;
use symbolica::prelude::*;

fn a(text: &str) -> Atom { Atom::parse(text, "marici", Default::default()).unwrap().expand() }

fn det(matrix: &[Vec<Atom>]) -> Atom {
    if matrix.len() == 1 { return matrix[0][0].clone(); }
    let mut out = a("0");
    for column in 0..matrix.len() {
        let minor = matrix[1..].iter().map(|row| row.iter().enumerate()
            .filter(|(index, _)| *index != column).map(|(_, value)| value.clone()).collect())
            .collect::<Vec<Vec<Atom>>>();
        let term = matrix[0][column].clone() * det(&minor);
        if column % 2 == 0 { out += term; } else { out -= term; }
    }
    out.expand()
}

fn adj(matrix: &[Vec<Atom>]) -> Vec<Vec<Atom>> {
    let n = matrix.len(); let mut out = vec![vec![a("0"); n]; n];
    for row in 0..n { for column in 0..n {
        let minor = matrix.iter().enumerate().filter(|(index, _)| *index != column)
            .map(|(_, values)| values.iter().enumerate().filter(|(index, _)| *index != row)
                .map(|(_, value)| value.clone()).collect()).collect::<Vec<Vec<Atom>>>();
        let cofactor = det(&minor);
        out[row][column] = if (row + column) % 2 == 0 { cofactor } else { -cofactor };
    }} out
}

fn dot(matrix: &[Vec<Atom>], left: &[Atom], right: &[Atom]) -> Atom {
    let mut out = a("0");
    for row in 0..left.len() { for column in 0..right.len() {
        out += left[row].clone() * matrix[row][column].clone() * right[column].clone();
    }} out.expand()
}

fn coefficient(polynomial: &Atom, variable: Symbol, order: usize) -> Atom {
    let mut value = polynomial.clone();
    for _ in 0..order { value = value.derivative(variable).expand(); }
    let factorial = (1..=order).product::<usize>().max(1);
    (value / a(&factorial.to_string()))
        .replace(a("v").to_pattern()).with(a("0").to_pattern()).expand()
}

fn affine_at_repeated_root_numerator(expression:&Atom,variable:Symbol,p1:&Atom,p2:&Atom)->Atom{
    let e0=coefficient(expression,variable,0);
    let e1=coefficient(expression,variable,1);
    assert_eq!((e0.clone()+e1.clone()*a("v")).expand(),expression.clone().expand());
    (a("2")*p2.clone()*e0-e1*p1.clone()).expand().factor()
}

fn quadratic_norm(expression: Atom) -> Atom {
    let s = a("s");
    let original = expression
        .replace(a("125^(1/2)").to_pattern()).with(a("5*s").to_pattern())
        .replace(a("5^(1/2)").to_pattern()).with(s.to_pattern()).expand();
    let conjugate = original.clone().replace(s.to_pattern()).with(a("-s").to_pattern()).expand();
    (original * conjugate).together().cancel().expand()
        .replace(a("s^2").to_pattern()).with(a("5").to_pattern())
        .together().cancel().expand().factor()
}

const PRIME: i128 = 2_147_483_647;
fn inverse(mut value: i128) -> i128 { value=value.rem_euclid(PRIME);let(mut r0,mut r)=(value,PRIME);let(mut s0,mut s)=(1,0);while r!=0{let q=r0/r;(r0,r)=(r,r0-q*r);(s0,s)=(s,s0-q*s);}assert_eq!(r0,1);s0.rem_euclid(PRIME) }
fn scalar_mod(text:&str)->i128{if let Some((n,d))=text.split_once('/') {(n.parse::<i128>().unwrap_or_else(|_|panic!("bad numerator {text}")).rem_euclid(PRIME)*inverse(d.parse::<i128>().unwrap_or_else(|_|panic!("bad denominator {text}")))).rem_euclid(PRIME)}else{text.parse::<i128>().unwrap_or_else(|_|panic!("bad integer {text}")).rem_euclid(PRIME)}}
fn trim(poly:&mut Vec<i128>){while poly.len()>1&&poly.last()==Some(&0){poly.pop();}}
fn coefficients(polynomial:Atom,variable:Symbol)->Vec<i128>{let mut out=Vec::new();let mut derivative=polynomial.expand();let mut factorial=1i128;loop{let at_zero=derivative.clone().replace(a("z").to_pattern()).with(a("0").to_pattern()).expand();out.push((scalar_mod(&at_zero.to_string())*inverse(factorial)).rem_euclid(PRIME));let next=derivative.derivative(variable).expand();if next==a("0"){break;}derivative=next;factorial=(factorial*out.len() as i128).rem_euclid(PRIME);}trim(&mut out);out}
fn remainder(mut left:Vec<i128>,right:&[i128])->Vec<i128>{let inv=inverse(*right.last().unwrap());while left.len()>=right.len()&&!(left.len()==1&&left[0]==0){let shift=left.len()-right.len();let c=(left[left.len()-1]*inv).rem_euclid(PRIME);for(i,x)in right.iter().enumerate(){left[i+shift]=(left[i+shift]-c*x).rem_euclid(PRIME);}trim(&mut left);}left}
fn gcd_degree(mut left:Vec<i128>,mut right:Vec<i128>)->usize{trim(&mut left);trim(&mut right);while !(right.len()==1&&right[0]==0){let next=remainder(left,&right);left=right;right=next;}left.len()-1}

fn main() {
    let h = vec![
        vec![a("2"), a("(11+sqrt(5))/4"), a("7/2")],
        vec![a("(11+sqrt(5))/4"), a("(11+sqrt(5))/2"), a("7+sqrt(5)/2")],
        vec![a("7/2"), a("7+sqrt(5)/2"), a("(21+sqrt(5))/2")],
    ];
    let determinant = det(&h).factor();
    let adjugate = adj(&h);
    let v = a("v");

    // The source walls fix y1=-5t/2, y2=-3t/2, y3=-t/2.
    // Differences K_i-K_1 then solve the three routing coordinates.
    let u1 = a("1+2*z");
    let u2 = ((h[1][1].clone() + a("6*z")) / a("2")).expand();
    let u3 = ((h[2][2].clone() + a("25*z/4") - v.clone()) / a("2")).expand();
    let u = vec![u1.clone(), u2.clone(), u3.clone()];
    let p = (determinant.clone() * a("25*z/4") - dot(&adjugate, &u, &u)).expand().factor();
    let v_symbol = symbol!("marici::v");
    let p0 = coefficient(&p, v_symbol, 0);
    let p1 = coefficient(&p, v_symbol, 1);
    let p2 = coefficient(&p, v_symbol, 2);
    assert_ne!(p2, a("0"));
    assert_eq!((p0.clone() + p1.clone() * v.clone() + p2.clone() * v.clone().pow(2)).expand(), p.clone().expand());
    let discriminant = (p1.clone().pow(2) - a("4") * p2.clone() * p0.clone()).expand().factor();
    let norm = quadratic_norm(discriminant.clone());

    // At the repeated root v=-p1/(2p2), exclude the y4=0 and y5=0 branches.
    let v_critical = (-p1.clone() / (a("2") * p2.clone())).together().cancel();
    let c = vec![
        a("(3+sqrt(5))/2"),
        a("-(1+sqrt(5))"),
        a("(3+sqrt(5))/2"),
    ];
    let q4_squared=a("17");
    let y5_squared=(a("25*z/4")-a("2")*(c[0].clone()*u1.clone()+c[1].clone()*u2.clone()+c[2].clone()*u3.clone())+q4_squared)
        .replace(v.to_pattern()).with(v_critical.clone().to_pattern()).together().cancel();
    let y4_soft_norm=quadratic_norm(p1.clone());
    let y5_zero_linear=a("780-375*z-140*sqrt(5)+173*sqrt(5)*z");
    let y5_simplified=(-y5_zero_linear.clone()/a("4*(-25+3*sqrt(5))")).together().cancel();
    assert_eq!(y5_squared.clone().replace(a("125^(1/2)").to_pattern()).with(a("5*sqrt(5)").to_pattern()).together().cancel().expand(),y5_simplified.clone().expand());
    let y5_soft_norm=quadratic_norm(y5_zero_linear.clone());

    // Source-ordered left-kernel multipliers. With S=alpha1+alpha2+alpha3=1,
    // alpha2=(H^-1 u)_1, alpha3=(H^-1 u)_2. The three wall multipliers vanish
    // precisely with alpha2, alpha3, and 5-8*alpha2-6*alpha3 respectively.
    let hu=(0..3).map(|row|(0..3).fold(a("0"),|sum,column|sum+adjugate[row][column].clone()*u[column].clone()).expand()).collect::<Vec<_>>();
    let multiplier_numerators=vec![
        affine_at_repeated_root_numerator(&hu[0],v_symbol,&p1,&p2),
        affine_at_repeated_root_numerator(&hu[1],v_symbol,&p1,&p2),
        affine_at_repeated_root_numerator(&(a("5")*determinant.clone()-a("8")*hu[0].clone()-a("6")*hu[1].clone()).expand(),v_symbol,&p1,&p2),
    ];
    let multiplier_norms=multiplier_numerators.iter().cloned().map(quadratic_norm).collect::<Vec<_>>();

    let z_symbol=symbol!("marici::z");
    let pilot_mod=coefficients(norm.clone(),z_symbol);
    let derivative_mod=(1..pilot_mod.len()).map(|power|(pilot_mod[power]*power as i128).rem_euclid(PRIME)).collect::<Vec<_>>();
    assert_eq!(gcd_degree(pilot_mod.clone(),derivative_mod),0);
    assert_eq!(gcd_degree(pilot_mod.clone(),coefficients(y4_soft_norm.clone(),z_symbol)),0);
    assert_eq!(gcd_degree(pilot_mod.clone(),coefficients(y5_soft_norm.clone(),z_symbol)),0);
    for multiplier_norm in &multiplier_norms{assert_eq!(gcd_degree(pilot_mod.clone(),coefficients(multiplier_norm.clone(),z_symbol)),0);}

    let prior:Value=serde_json::from_str(&fs::read_to_string("../results/five-site-cyclic-landau-candidate-bound.json").unwrap()).unwrap();
    let mut prior_factors=vec![a(prior["one_wall_factor"].as_str().unwrap()),a(prior["region_pair_factor"].as_str().unwrap())];
    for row in prior["disjoint_mixed_pair_norms"].as_array().unwrap(){prior_factors.push(a(row["rational_quadratic_field_norm"].as_str().unwrap()));}
    for factor in &prior_factors{assert_eq!(gcd_degree(pilot_mod.clone(),coefficients(factor.clone(),z_symbol)),0);}

    let packet = json!({
        "schema": "marici.five_site_cyclic_triple_landau_pilot.v1",
        "representative": "G_minus_e12|g_1345|g_145",
        "wall_solution": {"y1":"-5*t/2","y2":"-3*t/2","y3":"-t/2"},
        "parameter": "z=t^2",
        "remaining_square_variable": "v=y4^2",
        "solved_routing_coordinates": [u1.to_string(),u2.to_string(),u3.to_string()],
        "reduced_quadratic_in_v": p.to_string(),
        "quadratic_discriminant_over_Qsqrt5": discriminant.to_string(),
        "rational_field_norm": norm.to_string(),
        "repeated_root_v": v_critical.to_string(),
        "y5_squared_at_repeated_root": y5_squared.to_string(),
        "soft_exclusion_norms": {"y4_zero_test":y4_soft_norm.to_string(),"y5_zero_linear_over_Qsqrt5":y5_zero_linear.to_string(),"y5_zero_test":y5_soft_norm.to_string()},
        "modular_certificate": {"prime":PRIME,"pilot_squarefree":true,"coprime_to_eight_entry_1866_blocks":true,"coprime_to_y4_soft_test":true,"coprime_to_y5_soft_test":true},
        "wall_multiplier_zero_numerators_over_Qsqrt5":multiplier_numerators.iter().map(ToString::to_string).collect::<Vec<_>>(),
        "wall_multiplier_zero_norms":multiplier_norms.iter().map(ToString::to_string).collect::<Vec<_>>(),
        "all_three_wall_multipliers_nonzero_on_generic_pilot_quartic":true,
        "scope": "critical discriminant after linear wall and routing elimination; lower-wall/soft saturation comparison still required",
        "new_carrier_datum": false
    });
    fs::write("../results/five-site-cyclic-triple-landau-pilot.json",
        serde_json::to_string_pretty(&packet).unwrap() + "\n").unwrap();
    println!("{}", json!({"discriminant":discriminant.to_string(),"norm":norm.to_string()}));
}
