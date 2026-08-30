use serde_json::json;
use std::fs;
use symbolica::prelude::*;
fn a(s:&str)->Atom{Atom::parse(s,"marici",Default::default()).unwrap().expand()}
fn det(m:&[Vec<Atom>])->Atom{if m.len()==1{return m[0][0].clone()}let mut t=a("0");for c in 0..m.len(){let q=m[1..].iter().map(|r|r.iter().enumerate().filter(|(j,_)|*j!=c).map(|(_,x)|x.clone()).collect()).collect::<Vec<Vec<_>>>();if c%2==0{t+=m[0][c].clone()*det(&q)}else{t-=m[0][c].clone()*det(&q)}}t.expand()}
fn adj(m:&[Vec<Atom>])->Vec<Vec<Atom>>{let n=m.len();let mut out=vec![vec![a("0");n];n];for r in 0..n{for c in 0..n{let q=m.iter().enumerate().filter(|(i,_)|*i!=c).map(|(_,row)|row.iter().enumerate().filter(|(j,_)|*j!=r).map(|(_,x)|x.clone()).collect()).collect::<Vec<Vec<_>>>();out[r][c]=if(r+c)%2==0{det(&q)}else{-det(&q)}}}out}
fn dot(l:&[i32],r:&[i32])->Atom{let mut s=a("0");for(i,x)in l.iter().enumerate(){for(j,y)in r.iter().enumerate(){let d=(i.max(j)-i.min(j)).min(6-(i.max(j)-i.min(j)));let e=match d{0=>a("2"),1=>a("3/2"),2=>a("1/2"),3=>a("0"),_=>unreachable!()};s+=a(&x.to_string())*a(&y.to_string())*e}}s.expand()}
fn dot_k(l:&[i32],r:&[i32],k:&Atom)->Atom{let mut s=a("0");for(i,x)in l.iter().enumerate(){for(j,y)in r.iter().enumerate(){let d=(i.max(j)-i.min(j)).min(6-(i.max(j)-i.min(j)));let e=match d{0=>a("2"),1=>a("3/2"),2=>a("1/2"),3=>k.clone(),_=>unreachable!()};s+=a(&x.to_string())*a(&y.to_string())*e}}s.expand()}
fn coefficients(p:&Atom,var:Symbol)->Vec<Atom>{let mut d=p.clone().expand();let mut fact=1usize;let mut out=Vec::new();loop{out.push((d.clone()/a(&fact.to_string())).replace(a("x").to_pattern()).with(a("0").to_pattern()).expand());let next=d.derivative(var).expand();if next==a("0"){break}d=next;fact*=out.len();}while out.len()>1&&out.last()==Some(&a("0")){out.pop();}out}
fn resultant(l:&Atom,r:&Atom,var:Symbol)->Atom{let lc=coefficients(l,var);let rc=coefficients(r,var);let(ld,rd)=(lc.len()-1,rc.len()-1);let n=ld+rd;let mut m=vec![vec![a("0");n];n];let lrev=lc.iter().rev().cloned().collect::<Vec<_>>();let rrev=rc.iter().rev().cloned().collect::<Vec<_>>();for i in 0..rd{for(j,c)in lrev.iter().enumerate(){m[i][i+j]=c.clone()}}for i in 0..ld{for(j,c)in rrev.iter().enumerate(){m[rd+i][i+j]=c.clone()}}det(&m).expand().factor()}
fn main(){
 let routing=[vec![1,0,0,0,0,0],vec![1,1,0,0,0,0],vec![1,1,1,0,0,0],vec![1,1,1,1,0,0]];let q5=vec![1,1,1,1,1,0];
 let h=routing.iter().map(|l|routing.iter().map(|r|dot(l,r)).collect()).collect::<Vec<Vec<_>>>();let dh=det(&h).factor();let ah=adj(&h);let b=routing.iter().map(|r|dot(r,&q5)).collect::<Vec<_>>();
 if dh==a("0"){
  let minor3=det(&h[0..3].iter().map(|row|row[0..3].to_vec()).collect::<Vec<_>>()).factor();assert_ne!(minor3,a("0"));
  let nullvec=(0..4).find_map(|column|{let v=(0..4).map(|row|ah[row][column].clone()).collect::<Vec<_>>();if v.iter().any(|x|*x!=a("0")){Some(v)}else{None}}).unwrap();
  assert!((0..4).all(|row|(0..4).fold(a("0"),|s,column|s+h[row][column].clone()*nullvec[column].clone()).expand()==a("0")));
  let k=a("k");let hk=routing.iter().map(|l|routing.iter().map(|r|dot_k(l,r,&k)).collect()).collect::<Vec<Vec<_>>>();let dk=det(&hk).factor();let ak=adj(&hk);let bk=routing.iter().map(|r|dot_k(r,&q5,&k)).collect::<Vec<_>>();
  let x=a("x");let z=a("z");let squares=[z.clone(),x.clone(),z.clone(),x.clone()];let uk=(0..4).map(|i|((x.clone()+hk[i][i].clone()-squares[i].clone())/a("2")).expand()).collect::<Vec<_>>();
  let q5_residual=(dot_k(&q5,&q5,&k)-(0..4).fold(a("0"),|s,i|s+(0..4).fold(a("0"),|q,j|q+bk[i].clone()*ak[i][j].clone()*bk[j].clone()))/dk.clone()).together().cancel().factor();
  let fk=(dk.clone()*x.clone()-(0..4).fold(a("0"),|s,i|s+(0..4).fold(a("0"),|q,j|q+uk[i].clone()*ak[i][j].clone()*uk[j].clone()))).expand().factor();
  let linear=(0..4).fold(a("0"),|s,i|s+(0..4).fold(a("0"),|q,j|q+ak[i][j].clone()*bk[j].clone())*uk[i].clone());
  let gk=(dk.clone()*(z.clone()-x.clone()-dot_k(&q5,&q5,&k))+a("2")*linear).expand().factor();
  let rk=resultant(&fk,&gk,symbol!("marici::x"));
  let rk0=rk.clone().replace(k.to_pattern()).with(a("0").to_pattern()).expand().factor();
  let inherited=(-a("1/32")*k.clone()*k.clone()*(a("6")+a("7")*k.clone())*(a("6")+a("7")*k.clone())*(a("6")+a("7")*k.clone())).expand();
  let strict=(rk.clone()/inherited.clone()).together().cancel().expand().factor();let strict0=strict.clone().replace(k.to_pattern()).with(a("0").to_pattern()).expand();assert_eq!(strict0,a("36"));
  let v=a("v");let w=a("w");let full_squares=[z.clone(),v.clone(),z.clone(),w.clone()];let uf=(0..4).map(|i|((x.clone()+hk[i][i].clone()-full_squares[i].clone())/a("2")).expand()).collect::<Vec<_>>();
  let ffull=(dk.clone()*x.clone()-(0..4).fold(a("0"),|s,i|s+(0..4).fold(a("0"),|q,j|q+uf[i].clone()*ak[i][j].clone()*uf[j].clone()))).expand().factor();
  let lfull=(0..4).fold(a("0"),|s,i|s+(0..4).fold(a("0"),|q,j|q+ak[i][j].clone()*bk[j].clone())*uf[i].clone());
  let gfull=(dk.clone()*(z.clone()-x.clone()-dot_k(&q5,&q5,&k))+a("2")*lfull).expand().factor();
  let alpha=(1..=4).map(|i|a(&format!("alpha{i}"))).collect::<Vec<_>>();
  let ys=(1..=6).map(|i|a(&format!("y{i}"))).collect::<Vec<_>>();
  let ell_sq=(0..4).fold(a("0"),|s,i|s+(0..4).fold(a("0"),|q,j|q+alpha[i].clone()*hk[i][j].clone()*alpha[j].clone())).expand();
  let ell_dot_r=(0..4).map(|i|(0..4).fold(a("0"),|s,j|s+hk[i][j].clone()*alpha[j].clone()).expand()).collect::<Vec<_>>();
  let ell_dot_q5=(0..4).fold(a("0"),|s,i|s+alpha[i].clone()*bk[i].clone()).expand();
  let mut labelled_cover=Vec::new();
  labelled_cover.push((ys[0].clone()*ys[0].clone()-ell_sq.clone()).expand());
  for i in 0..4 {
   labelled_cover.push((ys[i+1].clone()*ys[i+1].clone()-ell_sq.clone()+a("2")*ell_dot_r[i].clone()-hk[i][i].clone()).expand());
  }
  labelled_cover.push((ys[5].clone()*ys[5].clone()-ell_sq+a("2")*ell_dot_q5-dot_k(&q5,&q5,&k)).expand());
  let fexc=(ffull.clone()/(a("6")+a("7")*k.clone())).together().cancel().expand().replace(k.to_pattern()).with(a("0").to_pattern()).expand().factor();
  let gexc=(gfull.clone()/(k.clone()*(a("6")+a("7")*k.clone()))).together().cancel().expand().replace(k.to_pattern()).with(a("0").to_pattern()).expand().factor();
  let vars=[symbol!("marici::x"),symbol!("marici::v"),symbol!("marici::w")];let minors=(0..3).flat_map(|i|((i+1)..3).map(move|j|(i,j))).map(|(i,j)|(fexc.derivative(vars[i])*gexc.derivative(vars[j])-fexc.derivative(vars[j])*gexc.derivative(vars[i])).expand().factor()).collect::<Vec<_>>();
  let xline=a("8/3+4*z-3*v");let wline=a("-2/3+2*z-v");assert_eq!(fexc.clone().replace(x.to_pattern()).with(xline.to_pattern()).replace(w.to_pattern()).with(wline.to_pattern()).expand(),a("0"));assert_eq!(gexc.clone().replace(x.to_pattern()).with(xline.to_pattern()).replace(w.to_pattern()).with(wline.to_pattern()).expand(),a("0"));assert!(minors.iter().all(|m|m.clone().replace(x.to_pattern()).with(xline.to_pattern()).replace(w.to_pattern()).with(wline.to_pattern()).expand()==a("0")));
  let packet=json!({"schema":"marici.six_site_disjoint_pair_triple_symmetric_landau.v6","coefficient_field":"Q(k)","routing_gram":h.iter().map(|r|r.iter().map(ToString::to_string).collect::<Vec<_>>()).collect::<Vec<_>>(),"det_routing_gram":"0","certified_rank":3,"nonzero_leading_3x3_minor":minor3.to_string(),"routing_null_vector":nullvec.iter().map(ToString::to_string).collect::<Vec<_>>(),"generic_labelled_cover":{"routing_coordinates":["alpha1","alpha2","alpha3","alpha4"],"cover_variables":["y1","y2","y3","y4","y5","y6"],"equations":labelled_cover.iter().map(ToString::to_string).collect::<Vec<_>>(),"active_walls":["q_g12=y1+y2+P12","q_g34=y3+y4+P34","q_g56=y5+y6+P56"],"wall_pullback":"in the frozen homogeneous incidence normalization: y2=y4=y6=-t, y2^2=y4^2=y6^2=z","generic_wall_first_equation":ffull.to_string(),"generic_wall_final_equation":gfull.to_string(),"sixth_vertex_normal_square":q5_residual.to_string()},"deformation":{"opposite_site_pairing":"k","det_routing_gram":dk.to_string(),"cleared_first_cover":fk.to_string(),"cleared_final_cover":gk.to_string(),"symmetric_resultant":rk.to_string(),"resultant_at_k_zero":rk0.to_string(),"inherited_gram_factor":inherited.to_string(),"strict_transform_factor":strict.to_string(),"strict_transform_at_k_zero":strict0.to_string()},"full_exceptional_cover":{"variables":["x=y1^2","v=y3^2","w=y5^2"],"first_equation":fexc.to_string(),"final_equation":gexc.to_string(),"critical_jacobian_minors":minors.iter().map(ToString::to_string).collect::<Vec<_>>(),"nonsymmetric_critical_line":{"parameter":"v","x":xline.to_string(),"w":wline.to_string(),"lies_over_every_z":true,"contains_symmetric_point":false}},"status":"generic labelled cover retained before the homogeneous Gram specialization","conclusion":"no finite homogeneous z-divisor arises in either the stabilizer-fixed or nonsymmetric exceptional sector","scope":"generic cover and wall equations exported in one routing chart; the sixth-vertex normal square tests whether cyclic chart transport is geometrically typed"});
  fs::write("../results/six-site-disjoint-pair-triple-symmetric-landau.json",serde_json::to_string_pretty(&packet).unwrap()+"\n").unwrap();println!("{}",json!({"det_routing_gram":0,"rank":3,"status":"homogeneous slice rejected"}));return;
 }
 let c=(0..4).map(|i|((0..4).fold(a("0"),|s,j|s+ah[i][j].clone()*b[j].clone())/dh.clone()).together().cancel().expand()).collect::<Vec<_>>();
 let x=a("x");let z=a("z");let squares=[z.clone(),x.clone(),z.clone(),x.clone()];let u=(0..4).map(|i|((x.clone()+h[i][i].clone()-squares[i].clone())/a("2")).expand()).collect::<Vec<_>>();
 let quad=(0..4).fold(a("0"),|s,i|s+(0..4).fold(a("0"),|q,j|q+u[i].clone()*ah[i][j].clone()*u[j].clone()));
 let f=(dh.clone()*x.clone()-quad).expand().factor();let q5norm=dot(&q5,&q5);
 let g=(z.clone()-x.clone()+a("2")*(0..4).fold(a("0"),|s,i|s+c[i].clone()*u[i].clone())-q5norm).expand().factor();
 let resultant=resultant(&f,&g,symbol!("marici::x"));
 let packet=json!({"schema":"marici.six_site_disjoint_pair_triple_symmetric_landau.v1","coefficient_field":"Q","routing_gram":h.iter().map(|r|r.iter().map(ToString::to_string).collect::<Vec<_>>()).collect::<Vec<_>>(),"det_routing_gram":dh.to_string(),"q5_coordinates":c.iter().map(ToString::to_string).collect::<Vec<_>>(),"wall_solution":"y2=y4=y6=-t","stabilizer_fixed_sector":"y1^2=y3^2=y5^2=x","first_cover_equation":f.to_string(),"sixth_cover_equation":g.to_string(),"symmetric_critical_resultant":resultant.to_string(),"scope":"stabilizer-fixed critical sector; saturation and nonsoftness not yet certified"});
 fs::write("../results/six-site-disjoint-pair-triple-symmetric-landau.json",serde_json::to_string_pretty(&packet).unwrap()+"\n").unwrap();println!("{}",json!({"F":f.to_string(),"G":g.to_string(),"resultant":resultant.to_string()}));
}
