use serde_json::json;
use std::{collections::{BTreeMap,BTreeSet},fs};

fn rank(mut a:Vec<Vec<i64>>)->usize{
    a.retain(|row|row.iter().any(|x|*x!=0));if a.is_empty(){return 0}let cols=a[0].len();let mut r=0;
    for c in 0..cols{let Some(p)=(r..a.len()).find(|i|a[*i][c]!=0)else{continue};a.swap(r,p);
        for i in r+1..a.len(){let x=a[i][c];if x==0{continue}let y=a[r][c];for j in c..cols{a[i][j]=y*a[i][j]-x*a[r][j];}}r+=1;}r
}
fn label(sites:&BTreeSet<usize>)->String{format!("g_{}",sites.iter().map(|i|(i+1).to_string()).collect::<String>())}
fn rotate(label:&str,shift:usize)->String{let mut sites=label.strip_prefix("g_").unwrap().chars()
    .map(|c|(c.to_digit(10).unwrap() as usize-1+shift)%6).collect::<Vec<_>>();sites.sort();
    format!("g_{}",sites.iter().map(|i|(i+1).to_string()).collect::<String>())}

fn main(){
    const N:usize=6;let mut vertices=Vec::new();
    for i in 0..N{let j=(i+1)%N;for (si,sj,se) in [(1,1,-1),(1,-1,1),(-1,1,1)]{let mut v=vec![0;2*N];v[i]=si;v[j]=sj;v[N+i]=se;vertices.push(v);}}
    let mut facets=BTreeMap::<String,Vec<i64>>::new();
    for len in 1..N{for start in 0..N{let sites=(0..len).map(|k|(start+k)%N).collect::<BTreeSet<_>>();let mut q=vec![0;2*N];
        for i in &sites{q[*i]=1}for e in 0..N{if sites.contains(&e)!=sites.contains(&((e+1)%N)){q[N+e]=1}}facets.insert(label(&sites),q);}}
    for e in 0..N{let mut q=vec![1;N];q.extend(vec![0;N]);q[N+e]=2;facets.insert(format!("G_minus_e{}{}",e+1,(e+1)%N+1),q);}
    facets.insert("G".into(),vec![1;N].into_iter().chain(vec![0;N]).collect());
    let common=(0..N).map(|i|format!("g_{}",i+1)).chain(std::iter::once("G".into())).collect::<BTreeSet<_>>();
    let active=["g_12","g_34","g_56"];
    let remaining=facets.keys().filter(|name|!common.contains(*name)&&!active.contains(&name.as_str())).cloned().collect::<Vec<_>>();
    let mut completions=Vec::new();
    for i in 0..remaining.len(){for j in i+1..remaining.len(){let names=active.iter().map(|s|s.to_string()).chain([remaining[i].clone(),remaining[j].clone()]).collect::<Vec<_>>();
        let zeros=vertices.iter().filter(|v|names.iter().all(|name|facets[name].iter().zip(v.iter()).map(|(a,b)|a*b).sum::<i64>()==0)).collect::<Vec<_>>();
        if zeros.is_empty(){continue}let base=zeros[0];let affine=rank(zeros.iter().skip(1).map(|v|v.iter().zip(base.iter()).map(|(x,y)|x-y).collect()).collect());
        if affine!=6{continue}let rows=common.iter().chain(names.iter()).map(|name|facets[name].clone()).collect::<Vec<_>>();if rank(rows)==12{completions.push(vec![remaining[i].clone(),remaining[j].clone()]);}
    }}
    let orbit=(0..6).map(|s|{let mut x=active.iter().map(|a|rotate(a,s)).collect::<Vec<_>>();x.sort();x}).collect::<BTreeSet<_>>();
    assert_eq!(orbit.len(),2);
    let packet=json!({"schema":"marici.six_site_disjoint_pair_triple_source_gate.v1","n":6,
        "active_triple":active,"cyclic_orbit_size":orbit.len(),"cyclic_occurrences":orbit,
        "compatible_source_term_completions":completions,"containing_source_term_count":completions.len(),
        "gate_passes":!completions.is_empty(),"scope":"source incidence only; no six-site Landau elimination or physical activation claim"});
    fs::write("../results/six-site-disjoint-pair-triple-source-gate.json",serde_json::to_string_pretty(&packet).unwrap()+"\n").unwrap();
    println!("{}",json!({"orbit_size":2,"containing_source_term_count":completions.len(),"gate_passes":!completions.is_empty()}));
}
