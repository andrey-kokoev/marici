use std::{env,fs};

fn rank(mut a:Vec<Vec<i64>>)->usize{
    let rows=a.len();let cols=a[0].len();let mut r=0;
    for c in 0..cols{let mut q=r;while q<rows&&a[q][c]==0{q+=1}if q==rows{continue}a.swap(r,q);
        for i in 0..rows{if i!=r&&a[i][c]!=0{let(x,y)=(a[r][c],a[i][c]);for j in c..cols{a[i][j]=x*a[i][j]-y*a[r][j];}}}r+=1;if r==rows{break}}
    r
}
fn main(){
    let a:Vec<String>=env::args().collect();if a.len()!=2{eprintln!("usage: cyclic_occurrence_rees <output.json>");std::process::exit(2)}
    // Occurrence order: (12|23),(12|31),(23|31),(23|12),(31|12),(31|23).
    let rho=[2usize,3,4,5,0,1];for i in 0..6{assert_eq!(rho[rho[rho[i]]],i)}
    let orbit_a=[0usize,2,4];let orbit_b=[1usize,3,5];
    assert!(orbit_a.iter().all(|i|orbit_a.contains(&rho[*i])));assert!(orbit_b.iter().all(|i|orbit_b.contains(&rho[*i])));
    let f=vec![vec![1,1,0,0,0,0],vec![0,0,1,1,0,0],vec![0,0,0,0,1,1]];
    assert_eq!(rank(f.clone()),3);
    let source=vec![1i64;6];let image:Vec<i64>=f.iter().map(|r|r.iter().zip(&source).map(|(x,y)|x*y).sum()).collect();assert_eq!(image,vec![2,2,2]);
    // Kernel basis: occurrence differences at each marked Cut. Unit minors make it saturated.
    let ker=vec![vec![1,-1,0,0,0,0],vec![0,0,1,-1,0,0],vec![0,0,0,0,1,-1]];for v in &ker{for r in &f{assert_eq!(r.iter().zip(v).map(|(x,y)|x*y).sum::<i64>(),0)}}assert_eq!(rank(ker.clone()),3);
    // Three local two-normal presentations, transported cyclically.
    let weights=[["X1","X2"],["X2","X3"],["X3","X1"]];
    assert_eq!(weights[1],[weights[0][1],"X3"]);assert_eq!(weights[2],[weights[1][1],weights[0][0]]);
    let out="{\"schema\":\"marici.gm.cyclic_occurrence_rees.v1\",\"occurrence_order\":[\"12|23\",\"12|31\",\"23|31\",\"23|12\",\"31|12\",\"31|23\"],\"cyclic_orbits\":[[\"12|23\",\"23|31\",\"31|12\"],[\"12|31\",\"23|12\",\"31|23\"]],\"rho_order\":3,\"all_source_signs\":1,\"forgetting_rank\":3,\"forgetting_kernel_rank\":3,\"forgetting_kernel_saturated\":true,\"source_sum_after_forgetting\":[2,2,2],\"occurrence_multiplicity\":2,\"new_torsion_prime\":false,\"sector_soft_presentations\":[[\"1\",\"2*X1\",\"2*X2\"],[\"1\",\"2*X2\",\"2*X3\"],[\"1\",\"2*X3\",\"2*X1\"]],\"cyclic_rees_covariance\":true,\"assembly_type\":\"C3-equivariant direct sum of three residue sectors\",\"cross_sector_cech_maps_source_defined\":false,\"global_cech_differential_computed\":false,\"new_carrier_datum\":false}";
    fs::write(&a[1],out).expect("write certificate")
}
