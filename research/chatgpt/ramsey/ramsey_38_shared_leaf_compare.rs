// Same legal-border generator and retained width as the blind baseline. No target order.
use std::env;
#[derive(Clone)] struct State { rows:Vec<u64>, independent:Vec<u64> }
struct Rng(u64);
impl Rng {fn next(&mut self)->u64{self.0=self.0.wrapping_add(0x9e3779b97f4a7c15);let mut z=self.0;z=(z^(z>>30)).wrapping_mul(0xbf58476d1ce4e5b9);z=(z^(z>>27)).wrapping_mul(0x94d049bb133111eb);z^(z>>31)}fn below(&mut self,n:u64)->usize{let t=n.wrapping_neg()%n;loop{let z=self.next();if z>=t{return (z%n) as usize}}}}
fn coexist(p:u64,q:u64,r:u64,six:&[u64],five:&[u64])->bool{
 let pairs=[(p,q),(p,r),(q,r)];let mut required=0;let mut can_plus=false;
 for (a,b) in pairs {let plus=a&b==0;can_plus|=plus;if six.iter().any(|s|s&(a|b)==0){if !plus{return false}required+=1;}}
 // At least one positive internal edge avoids an all-negative triple; never choose all three positive.
 required<3 && (can_plus || five.iter().all(|s|s&(p|q|r)!=0))
}
fn main(){let args:Vec<_>=env::args().collect();let guided=args[1]=="guided";let mut rng=Rng(args[2].parse().unwrap());let width=256;let pool=if guided {2*width}else{width};let mut states=vec![State{rows:vec![],independent:vec![0]}];loop{let n=states[0].rows.len();let mut picks=vec![];let mut seen=0u64;let mut options=vec![];
 for(i,s) in states.iter().enumerate(){let seven:Vec<_>=s.independent.iter().copied().filter(|m|m.count_ones()==7).collect();let mut opts=vec![];for &p in &s.independent{if !seven.iter().all(|o|p&o!=0){continue}opts.push(p);seen+=1;if picks.len()<pool{picks.push((i,p))}else{let j=rng.below(seen);if j<pool{picks[j]=(i,p)}}}options.push(opts);}
 if picks.is_empty(){println!("{} {} {} {:?}",args[1],args[2],n,states[0].rows);break}
 if guided && picks.len()>width {let mut scored=vec![];for (i,p) in picks {let o=&options[i];let fam=&states[i].independent;let layer=|k|fam.iter().copied().filter(|x|x.count_ones()==k).collect::<Vec<_>>();let six=layer(6);let five=layer(5);let mut hits=0;for _ in 0..16 {let q=o[rng.below(o.len() as u64)];let r=o[rng.below(o.len() as u64)];hits+=coexist(p,q,r,&six,&five) as usize;}scored.push((hits,rng.next(),i,p));}scored.sort_unstable_by(|a,b|b.cmp(a));picks=scored.into_iter().take(width).map(|(_,_,i,p)|(i,p)).collect();}
 assert!(n<63);states=picks.into_iter().map(|(i,p)|{let mut s=states[i].clone();let old=s.independent.len();for j in 0..old{let q=s.independent[j];if q&p==0{s.independent.push(q|(1<<n))}}s.rows.push(p);s}).collect();}}
