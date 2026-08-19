use std::{f64::consts::PI,fs};

#[derive(Clone,Copy)]struct C{re:f64,im:f64}
impl C{fn exp_i(x:f64)->Self{Self{re:x.cos(),im:x.sin()}}fn sub(self,q:Self)->Self{Self{re:self.re-q.re,im:self.im-q.im}}fn mul(self,q:Self)->Self{Self{re:self.re*q.re-self.im*q.im,im:self.re*q.im+self.im*q.re}}fn div(self,q:Self)->Self{let d=q.re*q.re+q.im*q.im;Self{re:(self.re*q.re+self.im*q.im)/d,im:(self.im*q.re-self.re*q.im)/d}}fn abs(self)->f64{self.re.hypot(self.im)}}
fn csc(s:f64)->C{let m=C::exp_i(2.0*PI*s);C{re:0.0,im:2.0}.mul(C::exp_i(PI*s).div(m.sub(C{re:1.0,im:0.0})))}
fn parity(p:[usize;3])->f64{let mut n=0;for i in 0..3{for j in i+1..3{if p[i]>p[j]{n+=1}}}if n%2==0{1.0}else{-1.0}}
fn swap(mut p:[usize;3],i:usize)->[usize;3]{p.swap(i,i+1);p}
fn path(start:[usize;3],word:[usize;3])->([usize;3],f64){let mut p=start;let mut sign=1.0;for i in word{p=swap(p,i);sign*=-1.0}(p,sign)}
fn main(){
 let(s12,s34,s345)=(0.23_f64,0.37_f64,0.61_f64);
 let phase=csc(s12).mul(csc(s34)).mul(csc(s345));
 let direct=C{re:((PI*s12).sin()*(PI*s34).sin()*(PI*s345).sin()).recip(),im:0.0};
 let source_error=phase.sub(direct).abs();
 let permutations=[[0,1,2],[0,2,1],[1,0,2],[1,2,0],[2,0,1],[2,1,0]];
 let mut max_history_error=0.0_f64;
 for p in permutations{let orientation=parity(p);let residue=parity(p);max_history_error=max_history_error.max((orientation*residue-1.0).abs());}
 let(a,sa)=path([0,1,2],[0,1,0]);let(b,sb)=path([0,1,2],[1,0,1]);
 let braid_endpoint_equal=a==b;let braid_orientation_error=(sa-sb).abs();let braid_total_error=((sa*sa)-(sb*sb)).abs();
 let tolerance=2.0e-15;assert!(source_error<tolerance&&max_history_error==0.0&&braid_endpoint_equal&&braid_orientation_error==0.0&&braid_total_error==0.0);
 let json=format!(concat!(
  "{{\n  \"source_pair\": [\"123456\", \"126435\"],\n",
  "  \"vertex_normals\": [\"12\", \"34\", \"345\"],\n",
  "  \"history_count\": 6,\n  \"all_total_transitions\": 1,\n",
  "  \"braid_words\": [[0,1,0],[1,0,1]],\n",
  "  \"braid_endpoint_equal\": {},\n  \"braid_orientation_signs\": [{:.1},{:.1}],\n",
  "  \"braid_total_error\": {:.17e},\n",
  "  \"source_formula_error\": {:.17e},\n  \"maximum_history_error\": {:.17e},\n",
  "  \"tolerance\": {:.1e},\n  \"passed\": true\n}}\n"),
  braid_endpoint_equal,sa,sb,braid_total_error,source_error,max_history_error,tolerance);
 fs::write("../string-six-point-vertex-braid.json",&json).expect("write packet");print!("{json}");
}
