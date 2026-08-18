use std::collections::{BTreeMap, HashMap};
const P:u64=2_305_843_009_213_693_951;
#[derive(Clone,Copy,PartialEq,Eq,PartialOrd,Ord,Hash)] struct M{u:u8,a:u8,b:u8}
type Poly=BTreeMap<M,u64>;
fn addmod(x:u64,y:u64)->u64{let z=x as u128+y as u128;(z%(P as u128))as u64}
fn mulmod(x:u64,y:u64)->u64{((x as u128*y as u128)%(P as u128))as u64}
fn neg(x:u64)->u64{if x==0{0}else{P-x}}
fn inv(mut a:u64)->u64{let mut e=P-2;let mut r=1;while e>0{if e&1==1{r=mulmod(r,a)}a=mulmod(a,a);e>>=1}r}
fn mono(u:u8,a:u8,b:u8,c:u64)->Poly{let mut p=Poly::new();if c!=0{p.insert(M{u,a,b},c);}p}
fn add(x:&Poly,y:&Poly)->Poly{let mut z=x.clone();for(m,c)in y{let v=addmod(*z.get(m).unwrap_or(&0),*c);if v==0{z.remove(m);}else{z.insert(*m,v);}}z}
fn scale(x:&Poly,c:u64)->Poly{x.iter().filter_map(|(m,v)|{let q=mulmod(*v,c);(q!=0).then_some((*m,q))}).collect()}
fn mul(x:&Poly,y:&Poly)->Poly{let mut z=Poly::new();for(m,c)in x{for(n,d)in y{if m.u+n.u>=2{continue}let k=M{u:m.u+n.u,a:m.a+n.a,b:m.b+n.b};let v=addmod(*z.get(&k).unwrap_or(&0),mulmod(*c,*d));if v==0{z.remove(&k);}else{z.insert(k,v);}}}z}
fn pow(x:&Poly,n:u8)->Poly{let mut z=mono(0,0,0,1);for _ in 0..n{z=mul(&z,x)}z}
fn der(x:&Poly,var:u8)->Poly{let mut z=Poly::new();for(m,c)in x{let d=match var{1=>m.a,2=>m.b,_=>m.u};if d==0{continue}let mut n=*m;match var{1=>n.a-=1,2=>n.b-=1,_=>n.u-=1};z.insert(n,mulmod(*c,d as u64));}z}
fn exact(sa:u8,sb:u8,f:&Poly,is_q:bool,plus:bool,k:&Poly,l1:&Poly,l2m:&Poly,l2p:&Poly)->Poly{
 let ea=2-sa;let eb=2-sb;let l2=if plus{l2p}else{l2m};let base=mul(&pow(l1,ea),&pow(l2,eb));
 if !is_q{let mut r=scale(&mul(&mul(&der(f,2),&base),k),neg(1));if sa>0{r=add(&r,&scale(&mul(&mul(f,&mul(&pow(l1,ea-1),&pow(l2,eb))),k),sa as u64));}add(&r,&scale(&mul(&mul(f,&base),&der(k,2)),mulmod(3,inv(2))))}
 else{let mut r=mul(&mul(&der(f,1),&base),k);if sb>0{r=add(&r,&scale(&mul(&mul(f,&mul(&pow(l1,ea),&pow(l2,eb-1))),k),neg(sb as u64)));}add(&r,&scale(&mul(&mul(f,&base),&der(k,1)),neg(mulmod(3,inv(2)))))}
}
fn rank(mut a:Vec<Vec<u64>>)->usize{if a.is_empty(){return 0}let nr=a.len();let nc=a[0].len();let mut r=0;for c in 0..nc{let Some(piv)=(r..nr).find(|&i|a[i][c]!=0)else{continue};a.swap(r,piv);let q=inv(a[r][c]);for j in c..nc{a[r][j]=mulmod(a[r][j],q)}for i in 0..nr{if i==r{continue}let q=a[i][c];if q==0{continue}for j in c..nc{a[i][j]=addmod(a[i][j],neg(mulmod(q,a[r][j])));}}r+=1;if r==nr{break}}r}
fn quotient_units(columns:&[Vec<u64>],mons:&[M],odd:bool)->Vec<M>{
 fn insert(mut v:Vec<u64>,basis:&mut BTreeMap<usize,Vec<u64>>)->bool{
  loop{let Some(p)=v.iter().position(|x|*x!=0)else{return false};if let Some(b)=basis.get(&p){let q=v[p];for j in p..v.len(){v[j]=addmod(v[j],neg(mulmod(q,b[j])));}}else{let q=inv(v[p]);for x in &mut v[p..]{*x=mulmod(*x,q)}basis.insert(p,v);return true}}
 }
 let mut basis=BTreeMap::new();for v in columns{insert(v.clone(),&mut basis);}
 let mut out=Vec::new();for(i,m)in mons.iter().enumerate(){if (m.a%2==1)!=odd{continue}let mut e=vec![0;mons.len()];e[i]=1;if insert(e,&mut basis){out.push(*m)}}
 out
}
fn main(){
 let one=mono(0,0,0,1);let u=mono(1,0,0,1);let aa=mono(0,1,0,1);let b=mono(0,0,1,1);
 let l1=add(&add(&b,&one),&scale(&u,neg(1)));let half=inv(2);let l2m=add(&aa,&scale(&u,neg(half)));let l2p=add(&aa,&scale(&u,half));
 let a2=pow(&aa,2);let k=add(&pow(&aa,4),&add(&mul(&u,&a2),&scale(&mul(&mul(&u,&a2),&pow(&b,2)),neg(1))));
 for d in [12u8,16,20,24,28]{
  let mons:Vec<M>=(0..2).flat_map(|uu|(0..=d).flat_map(move|s|(0..=s).map(move|i|M{u:uu,a:i,b:s-i}))).collect();
  let pos:HashMap<M,usize>=mons.iter().enumerate().map(|(i,m)|(*m,i)).collect();let mut cols=Vec::new();let mut minus_cols=Vec::new();
  for(sa,sb)in[(1,1),(1,0),(0,1),(0,0)]{for s in 0..=d{for i in 0..=s{let f=mono(0,i,s-i,1);for plus in[false,true]{for q in[false,true]{let p=exact(sa,sb,&f,q,plus,&k,&l1,&l2m,&l2p);if p.is_empty()||p.keys().any(|m|m.a+m.b>d){continue}let mut v=vec![0;mons.len()];let mut uv=vec![0;mons.len()];for(m,c)in p{v[*pos.get(&m).unwrap()]=c;if m.u==0{uv[*pos.get(&M{u:1,a:m.a,b:m.b}).unwrap()]=c}}if !plus{minus_cols.push(v.clone());minus_cols.push(uv.clone())}cols.push(v);cols.push(uv)}}}}}
  let mut even=Vec::new();let mut odd=Vec::new();for v in&cols{let mut e=vec![0;mons.len()];let mut o=vec![0;mons.len()];for(i,m)in mons.iter().enumerate(){if m.a%2==0{e[i]=v[i]}else{o[i]=v[i]}}even.push(e);odd.push(o)}
  let one_sided_rank=rank(minus_cols);let re=rank(even);let ro=rank(odd.clone());let te=mons.iter().filter(|m|m.a%2==0).count();let to=mons.len()-te;let ce=te-re;let co=to-ro;if d>=16{let qb=quotient_units(&odd,&mons,true);let mut groups:BTreeMap<(u8,u8),(usize,u8,u8)>=BTreeMap::new();for m in qb{let e=groups.entry((m.u,m.a)).or_insert((0,m.b,m.b));e.0+=1;e.1=e.1.min(m.b);e.2=e.2.max(m.b)}eprintln!("odd_quotient_groups_D{d}={:?}",groups);}
  println!("{{\"D\":{d},\"target\":{},\"image_rank\":{},\"cokernel\":{},\"one_sided_cokernel\":{},\"even_cokernel\":{ce},\"odd_cokernel\":{co},\"flat_expected\":{},\"flat\":{}}}",mons.len(),re+ro,ce+co,mons.len()-one_sided_rank,8*d,ce+co==8*(d as usize));
 }
}