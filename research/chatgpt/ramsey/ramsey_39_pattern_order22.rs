// Input from ramsey_39_pattern_order22.py. Compile with rustc -O.
use std::io::{self,Read};
const BASE:u32=(1<<22)-1;
fn seven(m:u32,rows:&[u32],a:&[u8],k:u8)->bool{
 if k==0{return true} let extra=m & !BASE;
 if extra==0{return a[(m&BASE) as usize]>=k}
 let v=31-extra.leading_zeros();let rest=m^(1<<v);
 seven(rest,rows,a,k)||seven(rest & !rows[v as usize],rows,a,k-1)
}
fn dfs(target:usize,opts:&[u32],rows:&mut Vec<u32>,path:&mut Vec<u32>,a:&[u8],idx:&[usize],wins:&mut [bool],example:&mut Vec<u32>){
 let n=rows.len();if opts.len()<target-n{return} // no old type can be used twice (checked below)
 for (i,&p) in opts.iter().enumerate(){
 path.push(p);
 if n+1==target {for &r in path.iter(){wins[idx[(r&BASE) as usize]]=true} if example.is_empty(){*example=path.clone()}}
 else {let mut child=Vec::new();for &q in &opts[i+1..]{if q&BASE==p&BASE{continue} if p&q==0{child.push(q|(1<<n));}if !seven(((1<<n)-1)&!(p|q),rows,a,7){child.push(q)}}
 rows.push(p);dfs(target,&child,rows,path,a,idx,wins,example);rows.pop();}path.pop();
 }
}
fn main(){let mut s=String::new();io::stdin().read_to_string(&mut s).unwrap();let mut rows:Vec<u32>=s.split_whitespace().map(|x|x.parse().unwrap()).collect();assert_eq!(rows.len(),22);
 let mut a=vec![0u8;1<<22];for m in 1..=BASE{let v=31-m.leading_zeros();let rest=m^(1<<v);a[m as usize]=a[rest as usize].max(1+a[(rest & !rows[v as usize]) as usize]);}
 let opts:Vec<_>=(0..=BASE).filter(|&m|a[m as usize] as u32==m.count_ones() && a[(BASE^m) as usize]<8).collect();assert_eq!(opts.len(),455);assert!(opts.iter().all(|&p|p!=0 && a[(BASE^p) as usize]>=7));
 let mut idx=vec![0;1<<22];for (i,&p) in opts.iter().enumerate(){idx[p as usize]=i}let mut wins=vec![false;opts.len()];let mut ex=vec![];let target=if std::env::args().any(|x|x=="--29"){29}else{28};dfs(target,&opts,&mut rows,&mut vec![],&a,&idx,&mut wins,&mut ex);
 if std::env::args().any(|x|x=="--scores") {
  for (&p,&won) in opts.iter().zip(&wins){let score=opts.iter().filter(|&&q|p&q==0 || a[(BASE & !(p|q)) as usize]<7).count();println!("{} {} {}",p,score,won as usize);}return
 }
 println!("{}",wins.iter().filter(|&&x|x).count());for p in ex{println!("{}",p)}
}
