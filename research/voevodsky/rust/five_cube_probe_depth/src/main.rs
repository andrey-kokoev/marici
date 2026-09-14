use serde::Serialize;
use sha2::{Digest, Sha256};
use std::collections::{BTreeMap, BTreeSet, HashMap};
use std::fs;
use std::time::Instant;

const MODULI: [u64; 2] = [1_000_000_007, 1_000_000_009];
const SETTINGS: [(u64, u64); 4] = [(5, 6), (3, 4), (7, 10), (2, 3)];

#[derive(Clone, Debug, Serialize)]
struct Edge { grade: usize, shell: usize, scale: usize, source: usize, target: usize, p: usize, q: usize }
#[derive(Serialize)]
struct JointRank { settings: usize, rank: usize, deficiency: usize }
#[derive(Serialize)]
struct ModulusResult { modulus: u64, boundary_rank: usize, cycle_dimension: usize, joint: Vec<JointRank>, elapsed_ms: u128 }
#[derive(Serialize)]
struct CutoffResult { cutoff: usize, edges: usize, vertices: usize, grade_edges: Vec<Edge>, moduli: Vec<ModulusResult> }
#[derive(Serialize)]
struct CubeEdge { mask: usize, shell: usize, source: usize, target: usize, grade: usize }
#[derive(Serialize)]
struct CubeResult { base: usize, vertices: BTreeMap<usize,usize>, edges: Vec<CubeEdge>, completion_grade: usize, latest_edges: Vec<CubeEdge> }
#[derive(Serialize)]
struct Output { schema: &'static str, packet_sha256: String, settings: Vec<String>, cutoffs: Vec<CutoffResult>, cube: CubeResult, deletion_three_setting_deficiencies: BTreeMap<String,Vec<usize>>, checks: BTreeMap<String,bool>, passed: bool, disposition: BTreeMap<String,String> }

fn mod_pow(mut a:u64, mut n:u64, p:u64)->u64 { let mut r=1u64; while n>0 { if n&1==1 {r=((r as u128*a as u128)%p as u128) as u64;} a=((a as u128*a as u128)%p as u128) as u64;n>>=1;} r }
fn mod_mul(a:u64,b:u64,p:u64)->u64 { ((a as u128*b as u128)%p as u128) as u64 }
fn primes(n:usize)->Vec<usize>{ let mut s=vec![true;n+1];s[0]=false;s[1]=false;let mut p=2;while p*p<=n{if s[p]{let mut q=p*p;while q<=n{s[q]=false;q+=p;}}p+=1;}s.iter().enumerate().filter_map(|(i,&x)|x.then_some(i)).collect() }
fn graph(cutoff:usize)->(Vec<Edge>,Vec<usize>){let ps=primes(cutoff/2+2);let mut e=Vec::new();for (j,w) in ps.windows(2).enumerate(){let (p,q)=(w[0],w[1]);for k in 1..=cutoff/(p*q){e.push(Edge{grade:k*p*q,shell:j+1,scale:k,source:k*p,target:k*q,p,q});}}e.sort_by_key(|x|(x.grade,x.shell,x.scale));let mut vs=BTreeSet::new();for x in &e{vs.insert(x.source);vs.insert(x.target);} (e,vs.into_iter().collect())}

struct Eliminator { modulus:u64, basis:Vec<Option<BTreeMap<usize,u64>>>, rank:usize }
impl Eliminator {
 fn new(modulus:u64, cols:usize)->Self{Self{modulus,basis:vec![None;cols],rank:0}}
 fn insert(&mut self, mut row:BTreeMap<usize,u64>){
  loop {
   let Some((&lead,&factor))=row.iter().next() else{return};
   if self.basis[lead].is_none(){let inv=mod_pow(factor,self.modulus-2,self.modulus);for value in row.values_mut(){*value=mod_mul(*value,inv,self.modulus);}self.basis[lead]=Some(row);self.rank+=1;return;}
   let updates:Vec<(usize,u64)>=self.basis[lead].as_ref().unwrap().iter().map(|(&k,&v)|(k,v)).collect();
   for (k,v) in updates {let old=*row.get(&k).unwrap_or(&0);let sub=mod_mul(factor,v,self.modulus);let value=(old+self.modulus-sub)%self.modulus;if value==0{row.remove(&k);}else{row.insert(k,value);}}
  }
 }
}
fn add_block(elim:&mut Eliminator, incidence:&[Vec<(usize,bool)>], edges:&[Edge], setting:Option<(u64,u64)>){let t=setting.map(|(a,b)|mod_mul(a,mod_pow(b,elim.modulus-2,elim.modulus),elim.modulus));for entries in incidence{let mut row=BTreeMap::new();for &(col,positive) in entries{let w=t.map_or(1,|x|mod_pow(x,edges[col].shell as u64,elim.modulus));let value=if positive{w}else{elim.modulus-w};row.insert(col,value);}elim.insert(row);}}
fn ranks(cutoff:usize,modulus:u64)->ModulusResult{let start=Instant::now();let (edges,vertices)=graph(cutoff);let vi:HashMap<usize,usize>=vertices.iter().enumerate().map(|(i,&v)|(v,i)).collect();let mut incidence=vec![Vec::new();vertices.len()];for (c,e) in edges.iter().enumerate(){incidence[vi[&e.source]].push((c,false));incidence[vi[&e.target]].push((c,true));}let mut elim=Eliminator::new(modulus,edges.len());add_block(&mut elim,&incidence,&edges,None);let boundary_rank=elim.rank;let mut joint=Vec::new();for (i,&setting) in SETTINGS.iter().enumerate(){add_block(&mut elim,&incidence,&edges,Some(setting));joint.push(JointRank{settings:i+1,rank:elim.rank,deficiency:edges.len()-elim.rank});println!("cutoff={cutoff} modulus={modulus} settings={} deficiency={}",i+1,edges.len()-elim.rank);}ModulusResult{modulus,boundary_rank,cycle_dimension:edges.len()-boundary_rank,joint,elapsed_ms:start.elapsed().as_millis()}}
fn deletion_deficiency(removed:&Edge,modulus:u64)->usize{let (mut edges,_)=graph(165165);edges.retain(|e|!(e.grade==removed.grade&&e.shell==removed.shell&&e.scale==removed.scale));let mut set=BTreeSet::new();for e in &edges{set.insert(e.source);set.insert(e.target);}let vertices:Vec<usize>=set.into_iter().collect();let vi:HashMap<usize,usize>=vertices.iter().enumerate().map(|(i,&v)|(v,i)).collect();let mut incidence=vec![Vec::new();vertices.len()];for (c,e) in edges.iter().enumerate(){incidence[vi[&e.source]].push((c,false));incidence[vi[&e.target]].push((c,true));}let mut elim=Eliminator::new(modulus,edges.len());add_block(&mut elim,&incidence,&edges,None);for &setting in SETTINGS.iter().take(3){add_block(&mut elim,&incidence,&edges,Some(setting));}edges.len()-elim.rank}
fn cube()->CubeResult{let base=2*3*5*7*11;let ratios=[(3,2),(5,3),(7,5),(11,7),(13,11)];let mut vertices=BTreeMap::new();for mask in 0..32{let mut v=base;for (i,&(q,p)) in ratios.iter().enumerate(){if mask>>i&1==1{v=v*q/p;}}vertices.insert(mask,v);}let mut edges=Vec::new();for (&mask,&source) in &vertices{for (i,&(q,p)) in ratios.iter().enumerate(){if mask>>i&1==0{edges.push(CubeEdge{mask,shell:i+1,source,target:vertices[&(mask|1<<i)],grade:(source/p)*p*q});}}}let completion_grade=edges.iter().map(|e|e.grade).max().unwrap();let latest_edges=edges.iter().filter(|e|e.grade==completion_grade).map(|e|CubeEdge{mask:e.mask,shell:e.shell,source:e.source,target:e.target,grade:e.grade}).collect();CubeResult{base,vertices,edges,completion_grade,latest_edges}}
fn main(){let packet=fs::read("research/voevodsky/five_cube_probe_depth_conjecture.md").unwrap();let packet_sha256=format!("{:x}",Sha256::digest(&packet));let mut cutoffs=Vec::new();for cutoff in [165164usize,165165usize]{let (edges,vertices)=graph(cutoff);let grade_edges=edges.iter().filter(|e|e.grade==cutoff).cloned().collect();let moduli=MODULI.iter().map(|&p|ranks(cutoff,p)).collect();cutoffs.push(CutoffResult{cutoff,edges:edges.len(),vertices:vertices.len(),grade_edges,moduli});}let cube=cube();let a=&cutoffs[0];let b=&cutoffs[1];let mut checks=BTreeMap::new();checks.insert("moduli_agree_below".into(),a.moduli[0].joint.iter().map(|x|x.deficiency).eq(a.moduli[1].joint.iter().map(|x|x.deficiency)));checks.insert("moduli_agree_at".into(),b.moduli[0].joint.iter().map(|x|x.deficiency).eq(b.moduli[1].joint.iter().map(|x|x.deficiency)));checks.insert("below_three_settings_full".into(),a.moduli.iter().all(|x|x.joint[2].deficiency==0));checks.insert("at_three_settings_deficiency_one".into(),b.moduli.iter().all(|x|x.joint[2].deficiency==1));checks.insert("at_four_settings_full".into(),b.moduli.iter().all(|x|x.joint[3].deficiency==0));checks.insert("cube_32_vertices_80_edges".into(),cube.vertices.len()==32&&cube.edges.len()==80);checks.insert("cube_completion_grade".into(),cube.completion_grade==165165);checks.insert("unique_final_edge".into(),cube.latest_edges.len()==1&&cube.latest_edges[0].source==12705&&cube.latest_edges[0].target==15015);let mut deletion_three_setting_deficiencies=BTreeMap::new();for edge in &b.grade_edges{let key=format!("shell_{}_{}_{}",edge.shell,edge.source,edge.target);let values=MODULI.iter().map(|&p|deletion_deficiency(edge,p)).collect();deletion_three_setting_deficiencies.insert(key,values);}checks.insert("nonfinal_edges_leave_defect".into(),deletion_three_setting_deficiencies.iter().filter(|(k,_)|!k.contains("12705_15015")).all(|(_,v)|v==&vec![1,1]));checks.insert("cube_final_edge_uniquely_restores_rank".into(),deletion_three_setting_deficiencies.get("shell_5_12705_15015")==Some(&vec![0,0]));let passed=checks.values().all(|&x|x);let mut disposition=BTreeMap::new();disposition.insert("prediction".into(),"three settings become deficient by one at five-cube completion; four restore full rank".into());disposition.insert("localization".into(),"only deletion of the cube-final edge restores three-setting full rank".into());let output=Output{schema:"marici.voevodsky.five-cube-probe-depth.v1",packet_sha256,settings:SETTINGS.iter().map(|(a,b)|format!("{a}/{b}")).collect(),cutoffs,cube,deletion_three_setting_deficiencies,checks,passed,disposition};fs::create_dir_all("research/voevodsky/results").unwrap();fs::write("research/voevodsky/results/five_cube_probe_depth.json",serde_json::to_string_pretty(&output).unwrap()+"\n").unwrap();println!("passed={}",output.passed);if !output.passed{std::process::exit(1);}}
