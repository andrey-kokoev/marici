use std::{f64::consts::PI,fs};
#[derive(Clone,Copy)]struct C{re:f64,im:f64}
impl C{fn z()->Self{Self{re:0.0,im:0.0}}fn exp_i(x:f64)->Self{Self{re:x.cos(),im:x.sin()}}fn add(self,q:Self)->Self{Self{re:self.re+q.re,im:self.im+q.im}}fn sub(self,q:Self)->Self{Self{re:self.re-q.re,im:self.im-q.im}}fn mul(self,q:Self)->Self{Self{re:self.re*q.re-self.im*q.im,im:self.re*q.im+self.im*q.re}}fn div(self,q:Self)->Self{let d=q.re*q.re+q.im*q.im;Self{re:(self.re*q.re+self.im*q.im)/d,im:(self.im*q.re-self.re*q.im)/d}}fn scale(self,x:f64)->Self{Self{re:self.re*x,im:self.im*x}}fn abs(self)->f64{self.re.hypot(self.im)}}
fn csc(s:f64)->C{let m=C::exp_i(2.0*PI*s);C{re:0.0,im:2.0}.mul(C::exp_i(PI*s).div(m.sub(C{re:1.0,im:0.0})))}
fn cot(s:f64)->C{let m=C::exp_i(2.0*PI*s);C{re:0.0,im:2.0}.mul(C{re:1.0,im:0.0}.div(m.sub(C{re:1.0,im:0.0})).add(C{re:0.5,im:0.0}))}
fn block(s:&[[f64;7];7],p:[usize;7])->([[C;2];2],[[C;2];2]){let v=|i:usize,j:usize|s[p[i]][p[j]];let(a,x,y,z)=(v(1,2),v(3,4),v(3,5),v(4,5));let q=x+y+z;let d=csc(a).mul(csc(x)).mul(csc(q));let m=[[d,csc(a).mul(csc(q)).mul(cot(x).add(cot(y))).scale(-1.0)],[csc(a).mul(csc(q)).mul(cot(x).add(cot(z))).scale(-1.0),d]];let sn=|u:f64|(PI*u).sin();let n=[[C{re:-sn(a)*sn(y)*sn(z),im:0.0},C{re:-sn(a)*sn(z)*sn(x+y),im:0.0}],[C{re:-sn(a)*sn(y)*sn(x+z),im:0.0},C{re:-sn(a)*sn(y)*sn(z),im:0.0}]];(m,n)}
fn rev(a:[[C;2];2])->[[C;2];2]{[[a[1][1],a[1][0]],[a[0][1],a[0][0]]]}
fn map_label(label:&str,p:[usize;7])->String{label.chars().map(|c|{let i=c.to_digit(10).unwrap()as usize;char::from_digit(p[i]as u32,10).unwrap()}).collect()}
fn main(){
 let mut s=[[0.0_f64;7];7];let vals=[((1,2),0.23),((1,3),-0.31),((1,4),0.41),((2,3),0.19),((2,4),-0.27),((2,5),0.33),((3,4),0.37),((3,5),0.29),((4,5),-0.17)];for((i,j),v)in vals{s[i][j]=v;s[j][i]=v;}
 let id=[0,1,2,3,4,5,6];let p23=[0,1,3,2,4,5,6];let p24=[0,1,4,3,2,5,6];
 let base_cols=["123456","124356"];let base_rows=["153462","154362"];
 let cols1=base_cols.map(|x|map_label(x,p23));let rows1=base_rows.map(|x|map_label(x,p23));
 let raw_cols2=base_cols.map(|x|map_label(x,p24));let raw_rows2=base_rows.map(|x|map_label(x,p24));
 assert_eq!(cols1,["132456","134256"]);assert_eq!(rows1,["152463","154263"]);
 assert_eq!(raw_cols2,["143256","142356"]);assert_eq!(raw_rows2,["153264","152364"]);
 let(b0,n0)=block(&s,id);let(b1,n1)=block(&s,p23);let(rb2,rn2)=block(&s,p24);let(b2,n2)=(rev(rb2),rev(rn2));
 let blocks=[b0,b1,b2];let inverses=[n0,n1,n2];let mut full=[[C::z();6];6];let mut full_inv=[[C::z();6];6];for k in 0..3{for i in 0..2{for j in 0..2{full[2*k+i][2*k+j]=blocks[k][i][j];full_inv[2*k+i][2*k+j]=inverses[k][i][j];}}}
 let mut identity_error=0.0_f64;for i in 0..6{for j in 0..6{let mut q=C::z();for k in 0..6{q=q.add(full[i][k].mul(full_inv[k][j]));}let e=if i==j{1.0}else{0.0};identity_error=identity_error.max(q.sub(C{re:e,im:0.0}).abs());}}
 let mut off_block_max=0.0_f64;for i in 0..6{for j in 0..6{if i/2!=j/2{off_block_max=off_block_max.max(full[i][j].abs());}}}
 let tolerance=2.0e-14;assert!(identity_error<tolerance&&off_block_max==0.0);
 let json=format!(concat!("{{\n  \"column_blocks\": [[\"123456\",\"124356\"],[\"132456\",\"134256\"],[\"142356\",\"143256\"]],\n",
 "  \"row_blocks\": [[\"153462\",\"154362\"],[\"152463\",\"154263\"],[\"152364\",\"153264\"]],\n",
 "  \"block_transitions\": [\"identity\",\"swap(2,3)\",\"J swap(2,4) J\"],\n",
 "  \"block_count\": 3,\n  \"off_block_maximum\": {:.17e},\n  \"full_inverse_identity_error\": {:.17e},\n",
 "  \"new_gluing_divisor\": false,\n  \"tolerance\": {:.1e},\n  \"passed\": true\n}}\n"),off_block_max,identity_error,tolerance);
 fs::write("../string-six-point-block-atlas.json",&json).expect("write packet");print!("{json}");
}
