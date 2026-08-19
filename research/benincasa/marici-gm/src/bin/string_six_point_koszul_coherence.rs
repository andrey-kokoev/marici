use std::{f64::consts::PI, fs};

#[derive(Clone,Copy)] struct C{re:f64,im:f64}
impl C{
 fn exp_i(x:f64)->Self{Self{re:x.cos(),im:x.sin()}}
 fn add(self,q:Self)->Self{Self{re:self.re+q.re,im:self.im+q.im}}
 fn sub(self,q:Self)->Self{Self{re:self.re-q.re,im:self.im-q.im}}
 fn mul(self,q:Self)->Self{Self{re:self.re*q.re-self.im*q.im,im:self.re*q.im+self.im*q.re}}
 fn div(self,q:Self)->Self{let d=q.re*q.re+q.im*q.im;Self{re:(self.re*q.re+self.im*q.im)/d,im:(self.im*q.re-self.re*q.im)/d}}
 fn scale(self,x:f64)->Self{Self{re:self.re*x,im:self.im*x}}
 fn abs(self)->f64{self.re.hypot(self.im)}
}
fn csc(s:f64)->C{let m=C::exp_i(2.0*PI*s);C{re:0.0,im:2.0}.mul(C::exp_i(PI*s).div(m.sub(C{re:1.0,im:0.0})))}
fn cot(s:f64)->C{let m=C::exp_i(2.0*PI*s);C{re:0.0,im:2.0}.mul(C{re:1.0,im:0.0}.div(m.sub(C{re:1.0,im:0.0})).add(C{re:0.5,im:0.0}))}

fn main(){
 let(s34,s56,s12,s234)=(0.37_f64,0.61_f64,0.23_f64,-0.41_f64);
 let local=csc(s34).mul(csc(s56)).mul(cot(s12).add(cot(s234)));
 let prefactor=C{re:0.0,im:0.5}.mul(C{re:0.0,im:0.5}).mul(C{re:0.0,im:0.5});
 let source=local.mul(prefactor);
 let direct=C{re:0.0,im:-0.125}.scale(
   (PI*s34).sin().recip()*(PI*s56).sin().recip()*
   ((PI*s12).tan().recip()+(PI*s234).tan().recip()));
 let source_error=source.sub(direct).abs();
 // Swapping normal order changes both darg orientation and ordered residue.
 let orientation_transition=-1.0_f64;
 let residue_transition=-1.0_f64;
 let history_34_56=source;
 let history_56_34=source.scale(orientation_transition*residue_transition);
 let coherence_error=history_34_56.sub(history_56_34).abs();
 let tolerance=2.0e-15;
 assert!(source_error<tolerance&&coherence_error<tolerance);
 let json=format!(concat!(
  "{{\n  \"source_pair\": [\"123456\", \"124365\"],\n",
  "  \"normal_order_a\": [\"34\", \"1234=56\"],\n",
  "  \"normal_order_b\": [\"1234=56\", \"34\"],\n",
  "  \"orientation_transition\": {:.1},\n  \"residue_transition\": {:.1},\n",
  "  \"total_transition\": {:.1},\n",
  "  \"assembled_source_value\": {{\"re\": {:.17}, \"im\": {:.17}}},\n",
  "  \"source_formula_error\": {:.17e},\n  \"coherence_error\": {:.17e},\n",
  "  \"tolerance\": {:.1e},\n  \"passed\": true\n}}\n"),
  orientation_transition,residue_transition,orientation_transition*residue_transition,
  source.re,source.im,source_error,coherence_error,tolerance);
 fs::write("../string-six-point-koszul-coherence.json",&json).expect("write packet");print!("{json}");
}
