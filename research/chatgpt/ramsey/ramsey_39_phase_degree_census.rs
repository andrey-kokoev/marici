// Exhaustive via CRT coordinates (mod 3, mod 13). rustc -O -C target-cpu=native.
use std::collections::BTreeSet;
const F:u32=8191;
fn rot(m:u32,k:u32)->u32 {((m<<k)|(m>>(13-k)))&F}
fn dil(m:u32,u:u32)->u32 {(0..13).filter(|i|m&(1<<i)!=0).map(|i|1<<((i*u)%13)).sum()}
struct Row{m:u32,r:[u32;13]}
fn main(){let rows:Vec<_>=(0..=F).map(|m|{let rev=dil(m,12);Row{m,r:std::array::from_fn(|s|rot(rev,s as u32))}}).collect();let bins:Vec<Vec<&Row>>=(0..=13).map(|n|rows.iter().filter(|a|a.m.count_ones()==n).collect()).collect();let mut tested=0u64;let mut pass=0;let mut best=0;let mut ex=[0;3];let mut best_refined=0;let mut survivors=BTreeSet::new();
 for na in 4..=12{let mut seen=BTreeSet::new();for a in &bins[na]{if !seen.insert(a.m){continue} for u in 1..13{let x=dil(a.m,u);for j in 0..13{seen.insert(rot(x,j));}}
 for nb in 0..=na.min(12-na){let nc=12-na-nb;if nc>nb{continue}for b in &bins[nb]{for c in &bins[nc]{tested+=1;let arr=[*a,*b,*c];let mut sum=0;let mut ok=true;let mut hist=[0u32;10];'outer: for k in 0..3{let x=arr[k];let y=arr[(k+1)%3];let z=arr[(k+2)%3];for s in 0..13{let h=(x.m&x.r[s]).count_ones()+2*(y.m&z.r[s]).count_ones();if h<2{ok=false;break 'outer}let cap=(2*h).min(9);sum+=cap;hist[cap as usize]+=1;}}
 if !ok{continue} pass+=1;if sum>best{best=sum;ex=[a.m,b.m,c.m]}if sum<272{continue}best_refined+=1;survivors.insert(hist);
 }}}}}
 println!("CRT candidates {tested}, all phases cap>=3 {pass}, max capped sum {best} example {ex:?}, pass 272: {best_refined}, histograms {}",survivors.len());for h in survivors{println!("{h:?}");}}
