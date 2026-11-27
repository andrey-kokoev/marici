// Scan graph6 lines from stdin for single-promotion realizations of any supplied envelope.
use std::{env,fs,io::{self,BufRead}};
fn main(){let args:Vec<_>=env::args().collect();let mut tab=vec![Vec::new();128*7];for l in fs::read_to_string(&args[1]).unwrap().lines(){let v:Vec<u128>=l.split_whitespace().map(|s|s.parse().unwrap()).collect();tab[v[0] as usize*7+v[1] as usize].push((1u128<<(v[2] as usize),v[3]));}
let(mut records,mut roots,mut moves,mut fits)=(0u64,0u64,0u64,0u64);for l in io::stdin().lock().lines(){let s=l.unwrap();let w=s.as_bytes();assert_eq!(w[0],90);records+=1;let mut g=[0u32;27];let mut k=0;for j in 1..27{for i in 0..j{if (w[1+k/6]-63)>>(5-k%6)&1==1{g[i]|=1<<j;g[j]|=1<<i;}k+=1;}}
for u in 0..27{if g[u].count_ones()!=7{continue}let cols:Vec<_>=(0..27).filter(|v|g[u]>>v&1==1).collect();let mut occ=0u128;let mut dup=0u128;let mut tris=Vec::new();let mut ok=true;for x in 0..27{if x==u || g[u]>>x&1==1{continue}let t=g[x]&g[u];if t.count_ones()>4{ok=false;break}let m=cols.iter().enumerate().fold(0usize,|a,(j,&v)|a|(((t>>v&1) as usize)<<j));let b=1u128<<m;dup|=occ&b;occ|=b;if t.count_ones()==3{tris.push((x,m));}}
if !ok{continue}roots+=1;for (x,m) in tris{let b=1u128<<m;if dup&b!=0{continue}let rest=occ^b;for (j,&v) in cols.iter().enumerate(){if m>>j&1!=0 || g[x]&g[v]!=0{continue}moves+=1;for &(e,a) in &tab[m*7+j]{if rest & !a==0 && rest&e!=0 && dup&e==0{fits+=1;println!("{} {} {} {} {} {}",records,u+1,x+1,v+1,e.trailing_zeros(),a);}}}}
}}
eprintln!("records={records} eligible_roots={roots} unique_triangle_legal_moves={moves} template_matches={fits}");}
