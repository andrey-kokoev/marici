use std::collections::HashMap;

const P: i64 = 2_305_843_009_213_693_951;
fn add(x:i64,y:i64)->i64{((x as i128+y as i128).rem_euclid(P as i128))as i64}
fn mul(x:i64,y:i64)->i64{((x as i128*y as i128).rem_euclid(P as i128))as i64}
fn pow(mut x:i64,mut n:i64)->i64{let mut r=1;while n>0{if n&1==1{r=mul(r,x)}x=mul(x,x);n>>=1;}r}
fn rank(mut cols:Vec<Vec<i64>>)->usize{
 let n=cols.first().map_or(0,|x|x.len());let mut r=0;
 for i in 0..n{let Some(j)=(r..cols.len()).find(|&j|cols[j][i]!=0)else{continue};
  cols.swap(r,j);let z=pow(cols[r][i],P-2);for x in &mut cols[r]{*x=mul(*x,z)}
  for j in 0..cols.len(){if j==r||cols[j][i]==0{continue}let z=cols[j][i];
   for k in i..n{cols[j][k]=add(cols[j][k],P-mul(z,cols[r][k]));}}
  r+=1;
 }r
}
fn choose(n:usize,k:usize)->i64{
 if k>n{return 0} let mut r=1i64;for i in 0..k{r=r*(n-i)as i64/(i+1)as i64;}r
}
fn audit(d:usize){
 let mons:Vec<_>=(0..=d).flat_map(|t|(0..=t).map(move|a|(a,t-a))).collect();
 let pos:HashMap<_,_>=mons.iter().enumerate().map(|(i,&m)|(m,i)).collect();
 let mut image=Vec::new();let mut degrees=Vec::new();
 let mut emit=|terms:HashMap<(usize,usize),i64>|{
  let terms:Vec<_>=terms.into_iter().filter(|(_,c)|c.rem_euclid(P)!=0).collect();
  if terms.is_empty()||terms.iter().map(|(m,_)|m.0+m.1).max().unwrap()>d{return}
  let mut v=vec![0;mons.len()];let mut degree=0;
  for(m,c)in terms{v[pos[&m]]=c.rem_euclid(P);degree=degree.max(m.0+m.1)}
  image.push(v);degrees.push(degree);
 };
 for(sa,sb)in[(1usize,1usize),(1,0),(0,1),(0,0)]{
  let ea=2-sa;let eb=2-sb;
  for t in 0..=d{for i in 0..=t{let j=t-i;
   let mut p=HashMap::new();
   if j>0{for k in 0..=ea{*p.entry((i+eb,j-1+k)).or_insert(0)-=(j as i64)*choose(ea,k);}}
   if sa>0{for k in 0..ea{*p.entry((i+eb,j+k)).or_insert(0)+=choose(ea-1,k);}}
   emit(p);
   let mut q=HashMap::new();
   if i>0{for k in 0..=ea{*q.entry((i-1+eb,j+k)).or_insert(0)+=(i as i64)*choose(ea,k);}}
   for k in 0..=ea{*q.entry((i+eb-1,j+k)).or_insert(0)-=((sb+6)as i64)*choose(ea,k);}
   emit(q);
  }}
 }
 let ri=rank(image.clone());assert_eq!(mons.len()-ri,2);
 let mut products=Vec::new();
 for(v,&degree)in image.iter().zip(&degrees){if degree+2>d{continue}let mut w=vec![0;mons.len()];
  for(i,&c)in v.iter().enumerate(){if c!=0{let(a,b)=mons[i];w[pos[&(a+2,b)]]=c;}}products.push(w);
 }
 let defect=rank(image.into_iter().chain(products).collect())-ri;
 assert_eq!(defect,1);println!("D={d}: a2_multiplication_defect={defect}");
}
fn main(){for d in[12,16,20,24,28]{audit(d)}
 println!("{{\"schema\":\"marici.benincasa.plus_cartier_action_gate.v1\",\"a2_preserves_exact_image\":false,\"stable_defect_rank\":1,\"smith_over_A_plus_defined\":false}}");}
