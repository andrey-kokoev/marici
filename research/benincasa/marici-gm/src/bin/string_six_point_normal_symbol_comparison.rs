use serde_json::{json, Value};
use symbolica::prelude::*;

fn a(s:&str)->Atom{Atom::parse(s,"marici",Default::default()).unwrap()}
fn clean(x:Atom)->Atom{x.together().cancel().factor()}
fn shift(v:&[Atom],name:&str)->Vec<Atom>{v.iter().cloned().map(|x|clean(x.replace(a(name).to_pattern()).with((-a(name)).to_pattern()))).collect()}
fn eval(v:&[Atom],m:&[Vec<Atom>])->Vec<Atom>{(0..m[0].len()).map(|j|clean((0..v.len()).fold(a("0"),|s,i|s+v[i].clone()*m[i][j].clone()))).collect()}
fn project(v:&[Atom],ex:i32,ey:i32)->Vec<Atom>{let x=shift(v,"B24");let y=shift(v,"B34");let xy=shift(&x,"B34");(0..v.len()).map(|i|clean(v[i].clone()+a(&ex.to_string())*x[i].clone()+a(&ey.to_string())*y[i].clone()+a(&(ex*ey).to_string())*xy[i].clone())).collect()}
fn minors(x:&[Atom],y:&[Atom])->Vec<Atom>{let mut out=Vec::new();for i in 0..x.len(){for j in i+1..x.len(){out.push(clean(x[i].clone()*y[j].clone()-x[j].clone()*y[i].clone()));}}out}

fn main(){
 let lp:Value=serde_json::from_str(&std::fs::read_to_string("../string-six-point-circuit-exceptional-cochain.json").unwrap()).unwrap();
 let cp:Value=serde_json::from_str(&std::fs::read_to_string("../string-six-point-loaded-corner-comparison.json").unwrap()).unwrap();
 let l:Vec<Atom>=lp["cochain"].as_array().unwrap().iter().map(|x|a(x.as_str().unwrap())).collect();
 let c:Vec<Vec<Atom>>=cp["matrix"].as_array().unwrap().iter().map(|r|r.as_array().unwrap().iter().map(|x|a(x.as_str().unwrap())).collect()).collect();
 let occurrence=eval(&l,&c);
 let p=[4usize,1,0,5,3,2];
 let mut loaded_word=vec![a("0");6];
 for i in 0..6{loaded_word[p[i]]=occurrence[i].clone();}
 let normal=vec![
  a("-2*(-1+A2*B24)*(-1+A3*B34)*(1+A2*B24)*(1+A3*B34)/(A2*B24*A3*B34)"),
  a("-2*(-1+A3)*(-1+A2*B24)*(1+A3)*(1+A2*B24)/(A2*B24*A3)"),
  a("-2*(-1+A2*B24)*(-1+A3*B34)*(1+A2*B24)*(1+A3*B34)/(A2*B24*A3*B34)"),
  a("-2*(-1+A2)*(-1+A3*B34)*(1+A2)*(1+A3*B34)/(A2*A3*B34)"),
  a("-2*(-1+A2)*(-1+A3)*(1+A2)*(1+A3)/(A2*A3)"),
  a("-2*(-1+A2)*(-1+A3)*(1+A2)*(1+A3)/(A2*A3)")];
 let chars=[("++",1,1),("-+",-1,1),("+-",1,-1),("--",-1,-1)];
 let mut rec=Vec::new();
 for(label,ex,ey)in chars{
  let x=project(&loaded_word,ex,ey);let y=project(&normal,ex,ey);let ms=minors(&x,&y);let nz=ms.iter().filter(|z|**z!=a("0")).count();
  let first_minor=ms.iter().find(|z|**z!=a("0")).map(ToString::to_string);
  let scalar=if nz==0{
   let i=(0..6).find(|i|y[*i]!=a("0")).unwrap();
   let q=clean(x[i].clone()/y[i].clone());
   assert!((0..6).all(|j|clean(x[j].clone()-q.clone()*y[j].clone())==a("0")));
   Some(q.to_string())
  }else{None};
  rec.push(json!({"character":label,"nonzero_projective_minors":nz,"proportional":nz==0,"combined_generic_rank":if nz==0{1}else{2},"comparison_scalar":scalar,"first_nonzero_minor":first_minor}));
 }
 let proportional=rec.iter().filter(|r|r["proportional"]==true).count();
 let packet=json!({
  "schema":"marici.benincasa.string_six_point_normal_symbol_comparison.v1",
  "basis_alignment":{"occurrence_to_dense_permutation":p,"dense_order":["123456","124356","132456","134256","142356","143256"]},
  "character_comparisons":rec,
  "proportional_character_count":proportional,
  "rank_two_character_count":4-proportional,
  "classification":if proportional==4{"the loaded occurrence image and normal-symbol row agree characterwise"}else{"matching deck characters do not identify the loaded occurrence image with the independently defined normal-symbol module"},
  "scope":"direct proportionality in the source-derived common six-word basis; no additional intertwiner is fitted"
 });
 let text=serde_json::to_string_pretty(&packet).unwrap()+"\n";std::fs::write("../string-six-point-normal-symbol-comparison.json",&text).unwrap();print!("{text}");
}
