// Counts endpoint words up to endpoint renaming. Usage: exe k goal extra-lookahead.
use std::collections::BTreeMap;
#[derive(Clone)]struct State{w:Vec<u8>,ind:Vec<u32>,rows:Vec<u32>}
impl State{fn next(&self,k:u32)->Vec<Self>{let n=self.rows.len();let last=self.w[n];let mut out=Vec::new();for y in 0..=*self.w.iter().max().unwrap()+1{let mut p=0u32;for i in 0..n{if self.w[i+1]==last||self.w[i]==y{p|=1<<i}}
if (0..n).any(|i|p&(1<<i)!=0 && self.rows[i]&p!=0)||self.ind.iter().any(|&s|s.count_ones()==k-1 && s&p==0){continue}let mut q=self.clone();q.w.push(y);q.rows.push(p);q.ind.extend(self.ind.iter().filter(|&&s|s&p==0).map(|s|s|(1<<n)));out.push(q)}out}}
fn ways(s:&State,k:u32,d:usize)->u64{if d==0{1}else{s.next(k).iter().map(|x|ways(x,k,d-1)).sum()}}
fn visit(s:&State,k:u32,goal:usize,d:usize,h:&mut BTreeMap<usize,u64>){let n=s.rows.len();if n<goal{let opts=s.next(k);let scores:Vec<_>=opts.iter().map(|x|ways(x,k,d.min(goal-n-1))).collect();if let Some(m)=scores.iter().max(){for(x,v)in opts.iter().zip(&scores){if v==m{visit(x,k,goal,d,h)}}return}}*h.entry(n).or_insert(0)+=1;}
fn main(){let args:Vec<_>=std::env::args().skip(1).map(|s|s.parse::<usize>().unwrap()).collect();let mut h=BTreeMap::new();visit(&State{w:vec![0],ind:vec![0],rows:vec![]},args[0] as u32,args[1],args[2],&mut h);println!("{:?}",h)}
