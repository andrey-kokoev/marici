// Seek one path from order 21 to 29. Candidate columns remain sorted by original
// priority, not by their signs to later vertices. Equal base types are allowed.
use std::io::{self,Read};
fn seven<const BASE:u32>(m:u32,rows:&[u32],a:&[u8],k:u8)->bool{
 if k==0{return true} let extra=m & !BASE;
 let old=a[(m&BASE) as usize];if old>=k{return true} if (old as u32)+extra.count_ones()<(k as u32){return false}
 let v=31-extra.leading_zeros();let rest=m^(1<<v);
 seven::<BASE>(rest,rows,a,k)||seven::<BASE>(rest & !rows[v as usize],rows,a,k-1)
}
fn seek<const BASE:u32>(target:usize,opts:&[u32],rows:&mut Vec<u32>,a:&[u8])->bool{
 let n=rows.len();let mut first=0;
 // If even reusing every repeatable prefix type up to the target leaves too
 // few slots, prune. Distinct sign variants of one type do not add capacity.
 if opts.len()<2*(target-n) {let mut cap=0;let mut last=None;for &q in opts {let p=q&BASE;if last==Some(p){continue}last=Some(p);if p==0 || a[(BASE^p) as usize]<7 {cap=target-n;break}cap+=1;}if cap<target-n{return false}}
 for (i,&p) in opts.iter().enumerate(){
 if n+1==target{rows.push(p);return true}
 if i>0 && opts[i-1]&BASE!=p&BASE{first=i}
 let mut child=Vec::new();for &q in &opts[first..]{if p&q==0{child.push(q|(1<<n));}if !seven::<BASE>(((1<<n)-1)&!(p|q),rows,a,7){child.push(q)}}
 if !child.is_empty(){rows.push(p);if seek::<BASE>(target,&child,rows,a){return true}rows.pop();}
 }false
}
fn main(){let mut s=String::new();io::stdin().read_to_string(&mut s).unwrap();let mut rows:Vec<u32>=s.split_whitespace().map(|x|x.parse().unwrap()).collect();match rows.len(){21=>solve::<{(1<<21)-1}>(&mut rows),22=>solve::<{(1<<22)-1}>(&mut rows),23=>solve::<{(1<<23)-1}>(&mut rows),24=>solve::<{(1<<24)-1}>(&mut rows),_=>panic!("unsupported prefix length")}}
fn solve<const BASE:u32>(rows:&mut Vec<u32>){let n0=rows.len();
 let mut a=vec![0u8;BASE as usize+1];for m in 1..=BASE{let v=31-m.leading_zeros();let rest=m^(1<<v);a[m as usize]=a[rest as usize].max(1+a[(rest & !rows[v as usize]) as usize]);}
 let mut opts:Vec<u32>=(0..=BASE).filter(|&m|a[m as usize] as u32==m.count_ones() && a[(BASE^m) as usize]<8).collect();
 let mut ranks:Vec<_>=opts.iter().map(|&p|(std::cmp::Reverse(opts.iter().filter(|&&q|p&q==0||a[(BASE&!(p|q)) as usize]<7).count()),p)).collect();ranks.sort();opts=ranks.into_iter().map(|x|x.1).collect();println!("{}",opts.len());let target=std::env::args().nth(1).map_or(29,|s|s.parse().unwrap());assert!((29..=30).contains(&target));if seek::<BASE>(target,&opts,rows,&a){for &p in &rows[n0..]{println!("{}",p)}}
}
