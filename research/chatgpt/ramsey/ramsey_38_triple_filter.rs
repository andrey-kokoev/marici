// Necessary test for nine vertex orbits of size three: every degree class,
// and every class with the same neighbor-degree histogram, has size divisible by 3.
use std::io::{self,BufRead};use std::collections::HashMap;
fn main(){let(mut total,mut pass)=(0,0);for s in io::stdin().lock().lines(){let s=s.unwrap();total+=1;let b=s.as_bytes();assert_eq!((b[0],b.len()),(90,60));let mut a=[0u32;27];let mut z=0;for j in 0..27{for i in 0..j{if (b[1+z/6]-63)>>(5-z%6)&1!=0{a[i]|=1<<j;a[j]|=1<<i}z+=1}}
let d=a.map(|m|m.count_ones() as usize);let mut h=[0;27];for i in d{h[i]+=1}if h.iter().any(|i|i%3!=0){continue}pass+=1;
let mut classes=HashMap::new();for i in 0..27{let mut hist=[0u8;27];for j in 0..27{if a[i]>>j&1!=0{hist[d[j]]+=1}}*classes.entry((d[i],hist)).or_insert(0)+=1;}if classes.values().all(|n|n%3==0){println!("{} {}",total,s)}}eprintln!("{} records, {} pass degree test",total,pass);}
