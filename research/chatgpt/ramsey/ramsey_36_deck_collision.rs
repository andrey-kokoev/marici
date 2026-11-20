// Compare exact coefficient vectors for one order of the graph6 catalogue.
use std::{io::{self,BufRead},collections::HashMap};
fn visit(mut p:u32,k:usize,chosen:u32,a:&[u32],counts:&mut [[u16;6]]){
 counts[a.len()][k]+=1;let mut t=chosen;while t!=0{let i=t.trailing_zeros() as usize;t&=t-1;counts[i][k]+=1;}
 while p!=0{let i=p.trailing_zeros() as usize;p&=p-1;visit(p&!a[i],k+1,chosen|1<<i,a,counts)}
}
fn main(){let mut seen=HashMap::new();for line in io::stdin().lock().lines(){let s=line.unwrap();let b=s.as_bytes();let n=(b[0]-63) as usize;let mut a=vec![0;n];let mut k=0;for j in 0..n{for i in 0..j{if (b[1+k/6]-63)>>(5-k%6)&1!=0{a[i]|=1<<j;a[j]|=1<<i}k+=1}}
 let mut c=vec![[0u16;6];n+1];visit((1<<n)-1,0,0,&a,&mut c);c[..n].sort();if let Some(prev)=seen.get(&c){println!("{} {}",prev,s)}else{seen.insert(c,s);}
}}
