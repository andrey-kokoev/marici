// No input graph or target order. Keep a seeded reservoir of legal labelled histories.
// rustc -O ramsey_38_blind_frontier.rs; run [width] [seed].
use std::env;
#[derive(Clone)] struct State { rows:Vec<u64>, independent:Vec<u64> }
struct Rng(u64);
impl Rng {fn next(&mut self)->u64{self.0=self.0.wrapping_add(0x9e3779b97f4a7c15);let mut z=self.0;z=(z^(z>>30)).wrapping_mul(0xbf58476d1ce4e5b9);z=(z^(z>>27)).wrapping_mul(0x94d049bb133111eb);z^(z>>31)}fn below(&mut self,n:u64)->u64{let t=n.wrapping_neg()%n;loop{let z=self.next();if z>=t{return z%n}}}}
fn main(){let args:Vec<_>=env::args().collect();let cap:usize=args.get(1).map_or(256,|s|s.parse().unwrap());assert!(cap>0);let mut rng=Rng(args.get(2).map_or(38,|s|s.parse().unwrap()));let mut states=vec![State{rows:vec![],independent:vec![0]}];loop{let n=states[0].rows.len();let mut picks=vec![];let mut seen=0u64;let mut fertile=0;
 for(i,s) in states.iter().enumerate(){let obligations:Vec<_>=s.independent.iter().copied().filter(|m|m.count_ones()==7).collect();let before=seen;for &p in &s.independent{if !obligations.iter().all(|o|p&o!=0){continue}seen+=1;if picks.len()<cap{picks.push((i,p))}else{let j=rng.below(seen);if j<(cap as u64){picks[j as usize]=(i,p)}}}fertile+=(seen>before) as usize;}
 println!("n={n} retained={} extendible={fertile} legal_borders={seen}",states.len());if picks.is_empty(){println!("witness_masks={:?}",states[0].rows);break}assert!(n<63,"mask capacity reached");states=picks.into_iter().map(|(i,p)|{let mut s=states[i].clone();let old=s.independent.len();for j in 0..old{let q=s.independent[j];if q&p==0{s.independent.push(q|(1<<n))}}s.rows.push(p);s}).collect();}}
