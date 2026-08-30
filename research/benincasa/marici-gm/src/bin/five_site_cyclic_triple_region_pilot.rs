use serde_json::json;
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

fn coefficients(polynomial: &Atom, variable: Symbol, variable_name: &str) -> Vec<Atom> {
    let mut derivative = polynomial.clone().expand();
    let mut factorial = 1usize;
    let mut out = Vec::new();
    loop {
        out.push((derivative.clone() / a(&factorial.to_string()))
            .replace(a(variable_name).to_pattern()).with(a("0").to_pattern()).expand());
        let next = derivative.derivative(variable).expand();
        if next == a("0") { break; }
        derivative = next;
        factorial *= out.len();
    }
    while out.len() > 1 && out.last() == Some(&a("0")) { out.pop(); }
    out
}

fn affine_at_repeated_root_numerator(expression:&Atom, variable:Symbol, variable_name:&str, p1:&Atom, p2:&Atom)->Atom {
    let values=coefficients(expression,variable,variable_name);
    assert!(values.len()<=2);
    let e0=values[0].clone();
    let e1=values.get(1).cloned().unwrap_or_else(||a("0"));
    (a("2")*p2.clone()*e0-e1*p1.clone()).expand().factor()
}

fn resultant(left: &Atom, right: &Atom, variable: Symbol, variable_name: &str) -> Atom {
    let left_coefficients = coefficients(left, variable, variable_name);
    let right_coefficients = coefficients(right, variable, variable_name);
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
    det(&sylvester).expand().factor()
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
fn coefficients_mod(polynomial:Atom,variable:Symbol)->Vec<i128>{let mut out=Vec::new();let mut derivative=polynomial.expand();let mut factorial=1i128;loop{let at_zero=derivative.clone().replace(a("z").to_pattern()).with(a("0").to_pattern()).expand();out.push((scalar_mod(&at_zero.to_string())*inverse(factorial)).rem_euclid(PRIME));let next=derivative.derivative(variable).expand();if next==a("0"){break;}derivative=next;factorial=(factorial*out.len() as i128).rem_euclid(PRIME);}trim(&mut out);out}
fn remainder(mut left:Vec<i128>,right:&[i128])->Vec<i128>{let inv=inverse(*right.last().unwrap());while left.len()>=right.len()&&!(left.len()==1&&left[0]==0){let shift=left.len()-right.len();let c=(left[left.len()-1]*inv).rem_euclid(PRIME);for(i,x)in right.iter().enumerate(){left[i+shift]=(left[i+shift]-c*x).rem_euclid(PRIME);}trim(&mut left);}left}
fn gcd_degree(mut left:Vec<i128>,mut right:Vec<i128>)->usize{trim(&mut left);trim(&mut right);while !(right.len()==1&&right[0]==0){let next=remainder(left,&right);left=right;right=next;}left.len()-1}

fn region_only_discriminant(
    h: &[Vec<Atom>], adjugate: &[Vec<Atom>], determinant: &Atom, c: &[Atom],
    fixed_squares: [Option<&str>; 5], free_indices: [usize; 2],
) -> (Atom, Atom, Atom, Atom, Atom, Atom, Atom, Atom, Atom) {
    let mut squares = fixed_squares.map(|value| value.map(a).unwrap_or_else(||a("0")));
    squares[free_indices[0]] = a("x");
    squares[free_indices[1]] = a("v");
    let u = vec![
        ((squares[0].clone()+h[0][0].clone()-squares[1].clone())/a("2")).expand(),
        ((squares[0].clone()+h[1][1].clone()-squares[2].clone())/a("2")).expand(),
        ((squares[0].clone()+h[2][2].clone()-squares[3].clone())/a("2")).expand(),
    ];
    let f=(determinant.clone()*squares[0].clone()-dot(adjugate,&u,&u)).expand().factor();
    let g=(squares[4].clone()-squares[0].clone()+a("2")*(c[0].clone()*u[0].clone()+c[1].clone()*u[1].clone()+c[2].clone()*u[2].clone())-a("17")).expand().factor();
    let x_symbol=symbol!("marici::x"); let v_symbol=symbol!("marici::v");
    let elimination=resultant(&f,&g,x_symbol,"x");
    let elimination_coefficients=coefficients(&elimination,v_symbol,"v");
    assert_eq!(elimination_coefficients.len(),3);
    let repeated_v=(-elimination_coefficients[1].clone()/(a("2")*elimination_coefficients[2].clone())).together().cancel();
    let g_coefficients=coefficients(&g,x_symbol,"x");
    assert_eq!(g_coefficients.len(),2);
    let repeated_x=(-g_coefficients[0].clone()/g_coefficients[1].clone())
        .replace(a("v").to_pattern()).with(repeated_v.clone().to_pattern()).together().cancel();
    let discriminant=resultant(&elimination,&elimination.derivative(v_symbol).expand(),v_symbol,"v");
    let norm=quadratic_norm(discriminant.clone());
    let x_soft=quadratic_norm(resultant(
        &f.clone().replace(a("x").to_pattern()).with(a("0").to_pattern()).expand(),
        &g.clone().replace(a("x").to_pattern()).with(a("0").to_pattern()).expand(),v_symbol,"v"));
    let v_soft=quadratic_norm(resultant(
        &f.clone().replace(a("v").to_pattern()).with(a("0").to_pattern()).expand(),
        &g.clone().replace(a("v").to_pattern()).with(a("0").to_pattern()).expand(),x_symbol,"x"));
    (f,g,elimination,discriminant,norm,x_soft,v_soft,repeated_x,repeated_v)
}

fn restrict_to_repeated_root(expression:&Atom,g:&Atom,elimination:&Atom)->Atom {
    let x_symbol=symbol!("marici::x"); let v_symbol=symbol!("marici::v");
    let g_coefficients=coefficients(g,x_symbol,"x"); assert_eq!(g_coefficients.len(),2);
    let expression_coefficients=coefficients(expression,x_symbol,"x"); assert!(expression_coefficients.len()<=2);
    let after_g=(expression_coefficients[0].clone()*g_coefficients[1].clone()
        - expression_coefficients.get(1).cloned().unwrap_or_else(||a("0"))*g_coefficients[0].clone()).expand();
    let elimination_coefficients=coefficients(elimination,v_symbol,"v"); assert_eq!(elimination_coefficients.len(),3);
    affine_at_repeated_root_numerator(&after_g,v_symbol,"v",&elimination_coefficients[1],&elimination_coefficients[2])
}

fn generic_multiplier_packet(
    h:&[Vec<Atom>],adjugate:&[Vec<Atom>],determinant:&Atom,c:&[Atom],
    fixed_squares:[Option<&str>;5],fixed_coefficients:[Option<&str>;5],free_indices:[usize;2],
    wall_rows:[[i32;5];3],g:&Atom,elimination:&Atom,candidate_mod:&[i128],z_symbol:Symbol,
)->serde_json::Value {
    let mut squares=fixed_squares.map(|value|value.map(a).unwrap_or_else(||a("0")));
    squares[free_indices[0]]=a("x"); squares[free_indices[1]]=a("v");
    let u=vec![
        ((squares[0].clone()+h[0][0].clone()-squares[1].clone())/a("2")).expand(),
        ((squares[0].clone()+h[1][1].clone()-squares[2].clone())/a("2")).expand(),
        ((squares[0].clone()+h[2][2].clone()-squares[3].clone())/a("2")).expand(),
    ];
    let hu=(0..3).map(|row|(0..3).fold(a("0"),|sum,column|sum+adjugate[row][column].clone()*u[column].clone()).expand()).collect::<Vec<_>>();
    let fixed_indices=(0..5).filter(|index|!free_indices.contains(index)).collect::<Vec<_>>(); assert_eq!(fixed_indices.len(),3);
    let directions=[vec![a("0"),a("0"),a("0")],vec![a("1"),a("0"),a("0")],vec![a("0"),a("1"),a("0")],vec![a("0"),a("0"),a("1")],c.to_vec()];
    let full_matrix=(0..4).map(|row|fixed_indices.iter().map(|index|if row==0{a("1")}else{directions[*index][row-1].clone()}).collect::<Vec<_>>()).collect::<Vec<_>>();
    let rhs=vec![determinant.clone(),hu[0].clone(),hu[1].clone(),hu[2].clone()];
    let mut selected=None;
    for omitted in 0..4 {
        let rows=(0..4).filter(|row|*row!=omitted).collect::<Vec<_>>();
        let matrix=rows.iter().map(|row|full_matrix[*row].clone()).collect::<Vec<_>>();
        let determinant_matrix=det(&matrix).factor();
        if determinant_matrix!=a("0"){selected=Some((omitted,rows,matrix,determinant_matrix));break;}
    }
    let (omitted,rows,matrix,determinant_matrix)=selected.unwrap();
    let matrix_adjugate=adj(&matrix);
    let alpha=(0..3).map(|row|(0..3).fold(a("0"),|sum,column|sum+matrix_adjugate[row][column].clone()*rhs[rows[column]].clone()).expand()).collect::<Vec<_>>();
    let consistency=((0..3).fold(a("0"),|sum,column|sum+full_matrix[omitted][column].clone()*alpha[column].clone())-determinant_matrix.clone()*rhs[omitted].clone()).expand();
    let wall_transpose=fixed_indices.iter().map(|index|(0..3).map(|wall|a(&wall_rows[wall][*index].to_string())).collect::<Vec<_>>()).collect::<Vec<_>>();
    let wall_det=det(&wall_transpose).factor(); assert_ne!(wall_det,a("0"));
    let wall_adjugate=adj(&wall_transpose);
    let beta_rhs=fixed_indices.iter().enumerate().map(|(position,index)|
        (-a("2")*determinant.clone()*alpha[position].clone()*a(fixed_coefficients[*index].unwrap())).expand()).collect::<Vec<_>>();
    let beta=(0..3).map(|row|(0..3).fold(a("0"),|sum,column|sum+wall_adjugate[row][column].clone()*beta_rhs[column].clone()).expand()).collect::<Vec<_>>();
    let consistency_restricted=restrict_to_repeated_root(&consistency,g,elimination);
    let consistency_norm=quadratic_norm(consistency_restricted.clone());
    assert_eq!(gcd_degree(candidate_mod.to_vec(),coefficients_mod(consistency_norm,z_symbol)),4);
    let beta_restricted=beta.iter().map(|value|restrict_to_repeated_root(value,g,elimination)).collect::<Vec<_>>();
    let beta_norms=beta_restricted.iter().cloned().map(quadratic_norm).collect::<Vec<_>>();
    for value in &beta_norms{assert_eq!(gcd_degree(candidate_mod.to_vec(),coefficients_mod(value.clone(),z_symbol)),0);}
    json!({
        "fixed_y_indices":fixed_indices.iter().map(|index|index+1).collect::<Vec<_>>(),
        "omitted_routing_equation":omitted,
        "alpha_pivot_determinant":determinant_matrix.to_string(),
        "wall_pivot_determinant":wall_det.to_string(),
        "routing_consistency_at_repeated_root":consistency_restricted.to_string(),
        "wall_multiplier_zero_numerators_over_Qsqrt5":beta_restricted.iter().map(ToString::to_string).collect::<Vec<_>>(),
        "wall_multiplier_zero_norms":beta_norms.iter().map(ToString::to_string).collect::<Vec<_>>(),
        "all_three_wall_multipliers_nonzero_on_generic_quartic":true
    })
}

fn main() {
    let h = vec![
        vec![a("2"), a("(11+sqrt(5))/4"), a("7/2")],
        vec![a("(11+sqrt(5))/4"), a("(11+sqrt(5))/2"), a("7+sqrt(5)/2")],
        vec![a("7/2"), a("7+sqrt(5)/2"), a("(21+sqrt(5))/2")],
    ];
    let determinant = det(&h).factor();
    let adjugate = adj(&h);
    let c = vec![a("(3+sqrt(5))/2"), a("-(1+sqrt(5))"), a("(3+sqrt(5))/2")];
    let x = a("x");
    let v = a("v");

    // g_1234|g_234|g_2345 fixes y1=y4=-3t/2 and y5=-5t/2;
    // x=y2^2 and v=y3^2 remain.
    let y1_squared = a("9*z/4");
    let y4_squared = a("9*z/4");
    let y5_squared = a("25*z/4");
    let u1 = ((y1_squared.clone() + h[0][0].clone() - x.clone()) / a("2")).expand();
    let u2 = ((y1_squared.clone() + h[1][1].clone() - v.clone()) / a("2")).expand();
    let u3 = ((y1_squared.clone() + h[2][2].clone() - y4_squared) / a("2")).expand();
    let u = vec![u1.clone(), u2.clone(), u3.clone()];
    let f = (determinant.clone() * y1_squared.clone() - dot(&adjugate, &u, &u)).expand().factor();
    let g = (y5_squared - y1_squared + a("2") * (c[0].clone()*u1.clone()+c[1].clone()*u2.clone()+c[2].clone()*u3.clone()) - a("17"))
        .expand().factor();
    let x_symbol = symbol!("marici::x");
    let v_symbol = symbol!("marici::v");
    let elimination = resultant(&f, &g, x_symbol, "x");
    let elimination_derivative = elimination.derivative(v_symbol).expand();
    let discriminant = resultant(&elimination, &elimination_derivative, v_symbol, "v");
    let norm = quadratic_norm(discriminant.clone());
    let norm_primitive = a("2016064-5586608*z+5762041*z^2-2628992*z^3+446464*z^4");
    assert_eq!(norm.clone().expand(), (a("443125/1048576")*norm_primitive.clone()).expand());

    // Since the wall matrix has zero y2 and y3 columns, nonsoftness forces
    // alpha2=alpha3=0. Normalize sum(alpha_i)=1 and solve the remaining
    // routing-gradient equations H^-1*u=alpha4*e3+alpha5*c.
    let hu=(0..3).map(|row|(0..3).fold(a("0"),|sum,column|sum+adjugate[row][column].clone()*u[column].clone()).expand()).collect::<Vec<_>>();
    // Use the homogeneous scale det(H)*c1 to avoid field denominators.
    let alpha5=hu[0].clone();
    let alpha4=(c[0].clone()*hu[2].clone()-c[2].clone()*hu[0].clone()).expand();
    let alpha1=(determinant.clone()*c[0].clone()-alpha4.clone()-alpha5.clone()).expand();
    let routing_consistency=(c[0].clone()*hu[1].clone()-c[1].clone()*hu[0].clone()).expand();

    let rhs1=(-a("2")*determinant.clone()*alpha1*a("-3/2")).expand();
    let rhs4=(-a("2")*determinant.clone()*alpha4*a("-3/2")).expand();
    let rhs5=(-a("2")*determinant.clone()*alpha5*a("-5/2")).expand();
    let beta=vec![
        ((rhs4.clone()+rhs5.clone()-rhs1.clone())/a("2")).together().cancel(),
        ((rhs1.clone()+rhs4.clone()-rhs5.clone())/a("2")).together().cancel(),
        ((rhs1+rhs5-rhs4)/a("2")).together().cancel(),
    ];
    let g_coefficients=coefficients(&g,x_symbol,"x");
    assert_eq!(g_coefficients.len(),2);
    let g0=g_coefficients[0].clone(); let g1=g_coefficients[1].clone();
    let elimination_coefficients=coefficients(&elimination,v_symbol,"v");
    assert_eq!(elimination_coefficients.len(),3);
    let multiplier_zero_tests=beta.iter().map(|value| {
        let beta_coefficients=coefficients(value,x_symbol,"x");
        assert!(beta_coefficients.len()<=2);
        let beta0=beta_coefficients[0].clone();
        let beta1=beta_coefficients.get(1).cloned().unwrap_or_else(||a("0"));
        let cleared=(beta0*g1.clone()-beta1*g0.clone()).expand();
        affine_at_repeated_root_numerator(&cleared,v_symbol,"v",&elimination_coefficients[1],&elimination_coefficients[2])
    }).collect::<Vec<_>>();
    let multiplier_zero_norms=multiplier_zero_tests.iter().cloned().map(quadratic_norm).collect::<Vec<_>>();
    let consistency_coefficients=coefficients(&routing_consistency,x_symbol,"x");
    assert!(consistency_coefficients.len()<=2);
    let consistency_after_g=(consistency_coefficients[0].clone()*g1.clone()
        - consistency_coefficients.get(1).cloned().unwrap_or_else(||a("0"))*g0.clone()).expand();
    let consistency_at_repeated_root=affine_at_repeated_root_numerator(
        &consistency_after_g,v_symbol,"v",&elimination_coefficients[1],&elimination_coefficients[2]);
    let consistency_norm=quadratic_norm(consistency_at_repeated_root.clone());

    let z_symbol = symbol!("marici::z");
    let candidate_mod = coefficients_mod(norm_primitive.clone(), z_symbol);
    let derivative_mod=(1..candidate_mod.len()).map(|power|(candidate_mod[power]*power as i128).rem_euclid(PRIME)).collect::<Vec<_>>();
    assert_eq!(gcd_degree(candidate_mod.clone(), derivative_mod), 0);
    assert_eq!(gcd_degree(candidate_mod.clone(),coefficients_mod(consistency_norm.clone(),z_symbol)),4);

    let y2_soft = resultant(
        &f.clone().replace(x.to_pattern()).with(a("0").to_pattern()).expand(),
        &g.clone().replace(x.to_pattern()).with(a("0").to_pattern()).expand(),
        v_symbol,"v");
    let y3_soft = resultant(
        &f.clone().replace(v.to_pattern()).with(a("0").to_pattern()).expand(),
        &g.clone().replace(v.to_pattern()).with(a("0").to_pattern()).expand(),
        x_symbol,"x");
    let y2_soft_norm = quadratic_norm(y2_soft.clone());
    let y3_soft_norm = quadratic_norm(y3_soft.clone());
    assert_eq!(gcd_degree(candidate_mod.clone(),coefficients_mod(y2_soft_norm.clone(),z_symbol)),0);
    assert_eq!(gcd_degree(candidate_mod.clone(),coefficients_mod(y3_soft_norm.clone(),z_symbol)),0);

    let prior:serde_json::Value=serde_json::from_str(&fs::read_to_string("../results/five-site-cyclic-landau-candidate-bound.json").unwrap()).unwrap();
    let mut prior_factors=vec![a(prior["one_wall_factor"].as_str().unwrap()),a(prior["region_pair_factor"].as_str().unwrap())];
    for row in prior["disjoint_mixed_pair_norms"].as_array().unwrap(){prior_factors.push(a(row["rational_quadratic_field_norm"].as_str().unwrap()));}
    let first_pilot:serde_json::Value=serde_json::from_str(&fs::read_to_string("../results/five-site-cyclic-triple-landau-pilot.json").unwrap()).unwrap();
    prior_factors.push(a(first_pilot["rational_field_norm"].as_str().unwrap()));
    for factor in &prior_factors { assert_eq!(gcd_degree(candidate_mod.clone(),coefficients_mod(factor.clone(),z_symbol)),0); }
    for factor in &multiplier_zero_norms { assert_eq!(gcd_degree(candidate_mod.clone(),coefficients_mod(factor.clone(),z_symbol)),0); }

    let packet = json!({
        "schema": "marici.five_site_cyclic_triple_region_pilot.v1",
        "representative": "g_1234|g_234|g_2345",
        "wall_solution": {"y1":"-3*t/2","y4":"-3*t/2","y5":"-5*t/2"},
        "parameter": "z=t^2",
        "remaining_square_variables": ["x=y2^2","v=y3^2"],
        "solved_routing_coordinates": [u1.to_string(),u2.to_string(),u3.to_string()],
        "first_cover_equation": f.to_string(),
        "fifth_cover_equation": g.to_string(),
        "elimination_in_v": elimination.to_string(),
        "critical_discriminant_over_Qsqrt5": discriminant.to_string(),
        "rational_field_norm_raw": norm.to_string(),
        "rational_field_norm_primitive": norm_primitive.to_string(),
        "soft_exclusion_norms": {"y2_zero_test":y2_soft_norm.to_string(),"y3_zero_test":y3_soft_norm.to_string()},
        "modular_certificate": {"prime":PRIME,"candidate_squarefree":true,"coprime_to_degree_87_union":true,"coprime_to_y2_soft_test":true,"coprime_to_y3_soft_test":true},
        "wall_multiplier_zero_numerators_over_Qsqrt5":multiplier_zero_tests.iter().map(ToString::to_string).collect::<Vec<_>>(),
        "wall_multiplier_zero_norms":multiplier_zero_norms.iter().map(ToString::to_string).collect::<Vec<_>>(),
        "routing_gradient_consistency_at_repeated_root":consistency_at_repeated_root.to_string(),
        "all_three_wall_multipliers_nonzero_on_generic_quartic":true,
        "status": "saturated region-only triple-wall Landau divisor",
        "new_carrier_datum": false
    });
    fs::write("../results/five-site-cyclic-triple-region-pilot.json",
        serde_json::to_string_pretty(&packet).unwrap() + "\n").unwrap();

    let census_inputs = [
        ("g_1234|g_234|g_2345", [Some("9*z/4"),None,None,Some("9*z/4"),Some("25*z/4")], [Some("-3/2"),None,None,Some("-3/2"),Some("-5/2")], [1,2], [[0,0,0,1,1],[1,0,0,1,0],[1,0,0,0,1]]),
        ("g_1234|g_34|g_345", [None,Some("z/4"),None,Some("9*z/4"),Some("25*z/4")], [None,Some("-1/2"),None,Some("-3/2"),Some("-5/2")], [0,2], [[0,0,0,1,1],[0,1,0,1,0],[0,1,0,0,1]]),
        ("g_123|g_4|g_5", [None,None,Some("9*z/4"),Some("z/4"),Some("9*z/4")], [None,None,Some("-3/2"),Some("1/2"),Some("-3/2")], [0,1], [[0,0,1,0,1],[0,0,1,1,0],[0,0,0,1,1]]),
        ("g_12|g_34|g_5", [None,Some("9*z/4"),None,Some("z/4"),Some("z/4")], [None,Some("-3/2"),None,Some("-1/2"),Some("-1/2")], [0,2], [[0,1,0,0,1],[0,1,0,1,0],[0,0,0,1,1]]),
    ];
    let mut census_records=Vec::new();
    let mut census_polynomials=Vec::new();
    for (representative,fixed_squares,fixed_coefficients,free_indices,wall_rows) in census_inputs {
        let (_case_f,case_g,case_elimination,case_discriminant,case_norm,x_soft,v_soft,repeated_x,repeated_v)=region_only_discriminant(
            &h,&adjugate,&determinant,&c,fixed_squares,free_indices);
        let case_mod=coefficients_mod(case_norm.clone(),z_symbol);
        let derivative=(1..case_mod.len()).map(|power|(case_mod[power]*power as i128).rem_euclid(PRIME)).collect::<Vec<_>>();
        assert_eq!(gcd_degree(case_mod.clone(),derivative),0);
        assert_eq!(gcd_degree(case_mod.clone(),coefficients_mod(x_soft.clone(),z_symbol)),0);
        assert_eq!(gcd_degree(case_mod.clone(),coefficients_mod(v_soft.clone(),z_symbol)),0);
        for factor in &prior_factors { assert_eq!(gcd_degree(case_mod.clone(),coefficients_mod(factor.clone(),z_symbol)),0); }
        let multiplier_packet=generic_multiplier_packet(&h,&adjugate,&determinant,&c,
            fixed_squares,fixed_coefficients,free_indices,wall_rows,&case_g,&case_elimination,&case_mod,z_symbol);
        let case_g_coefficients=coefficients(&case_g,symbol!("marici::x"),"x");
        assert_eq!(case_g_coefficients.len(),2);
        let case_elimination_coefficients=coefficients(&case_elimination,v_symbol,"v");
        assert_eq!(case_elimination_coefficients.len(),3);
        let gx_norm=quadratic_norm(case_g_coefficients[1].clone());
        let quadratic_leading_norm=quadratic_norm(case_elimination_coefficients[2].clone());
        assert_eq!(gcd_degree(case_mod.clone(),coefficients_mod(gx_norm.clone(),z_symbol)),0);
        assert_eq!(gcd_degree(case_mod.clone(),coefficients_mod(quadratic_leading_norm.clone(),z_symbol)),0);
        census_records.push(json!({
            "representative":representative,
            "free_y_indices":free_indices.map(|index|index+1),
            "fixed_linear_y_over_t":fixed_coefficients.iter().map(|value|*value).collect::<Vec<_>>(),
            "elimination_degree_v":coefficients(&case_elimination,v_symbol,"v").len()-1,
            "critical_discriminant_over_Qsqrt5":case_discriminant.to_string(),
            "elimination_in_second_free_square":case_elimination.to_string(),
            "local_fold_certificate":{
                "linear_first_free_pivot":case_g_coefficients[1].to_string(),
                "linear_first_free_pivot_norm":gx_norm.to_string(),
                "quadratic_second_free_leading_coefficient":case_elimination_coefficients[2].to_string(),
                "quadratic_second_free_leading_norm":quadratic_leading_norm.to_string(),
                "both_pivots_coprime_to_quartic":true,
                "transverse_discriminant_simple_from_squarefree_norm":true
            },
            "rational_field_norm_raw":case_norm.to_string(),
            "repeated_critical_squares":{"first_free_y_squared":repeated_x.to_string(),"second_free_y_squared":repeated_v.to_string()},
            "soft_exclusion_norms":{"first_free_y_zero":x_soft.to_string(),"second_free_y_zero":v_soft.to_string()},
            "squarefree":true,
            "coprime_to_both_free_coordinate_soft_tests":true,
            "coprime_to_entry_1870_and_lower_union":true,
            "multiplier_saturation":multiplier_packet
        }));
        census_polynomials.push(case_norm);
    }
    let pairwise_gcd_degrees=(0..census_polynomials.len()).flat_map(|left|((left+1)..census_polynomials.len()).map(move|right|(left,right)))
        .map(|(left,right)|json!({"left":left,"right":right,"gcd_degree":gcd_degree(
            coefficients_mod(census_polynomials[left].clone(),z_symbol),
            coefficients_mod(census_polynomials[right].clone(),z_symbol))})).collect::<Vec<_>>();
    let census_packet=json!({
        "schema":"marici.five_site_cyclic_triple_region_census.v1",
        "coefficient_field":"Q(sqrt(5))",
        "records":census_records,
        "pairwise_gcd_degrees":pairwise_gcd_degrees,
        "scope":"raw norm census for all four nonsoft pure-t region-only representatives; multiplier saturation certified only for record zero",
        "new_carrier_datum":false
    });
    fs::write("../results/five-site-cyclic-triple-region-census.json",
        serde_json::to_string_pretty(&census_packet).unwrap()+"\n").unwrap();
    println!("{}", json!({
        "elimination_degree_v": coefficients(&elimination,v_symbol,"v").len()-1,
        "primitive_norm": norm_primitive.to_string(),
        "region_census_pairwise_gcd_degrees":pairwise_gcd_degrees
    }));
}
