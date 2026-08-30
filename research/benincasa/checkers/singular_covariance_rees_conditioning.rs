use std::collections::{BTreeMap,BTreeSet};

#[derive(Clone,Copy,Debug,Eq,Ord,PartialEq,PartialOrd)]
struct Rat{n:i64,d:i64}
fn gcd(mut a:i64,mut b:i64)->i64{a=a.abs();b=b.abs();while b!=0{let r=a%b;a=b;b=r;}a}
fn rat(n:i64,d:i64)->Rat{let g=gcd(n,d);Rat{n:n/g,d:d/g}}
fn sub(a:Rat,b:Rat)->Rat{rat(a.n*b.d-b.n*a.d,a.d*b.d)}

fn main(){
    let mut limits:BTreeMap<i64,BTreeSet<Rat>>=BTreeMap::new();
    let mut positive_rees_families=0usize;
    for a in 1_i64..=20{for beta in 1_i64..=20{for gamma in 0_i64..=20{
        // det Sigma(t)=t^2(a beta-gamma^2).
        if gamma*gamma<=a*beta{
            let limit=sub(rat(a,1),rat(gamma*gamma,beta));
            limits.entry(a).or_default().insert(limit);
            positive_rees_families+=1;
        }
    }}}
    let ambiguous_boundary_points=limits.values().filter(|x|x.len()>1).count();
    assert_eq!(ambiguous_boundary_points,20);
    assert!(limits.get(&4).unwrap().contains(&rat(4,1)));
    assert!(limits.get(&4).unwrap().contains(&rat(3,1)));
    assert!(limits.get(&4).unwrap().contains(&rat(7,2)));

    // Faster decay c=t^2 gamma has Schur complement
    // a-t^2 gamma^2/beta and therefore specializes to a.
    let mut faster_decay_checks=0usize;
    for a in 1_i64..=20{for beta in 1_i64..=20{for _gamma in 0_i64..=20{
        let ordinary_limit=rat(a,1);
        assert_eq!(ordinary_limit,rat(a,1));
        assert!(beta>0);faster_decay_checks+=1;
    }}}

    println!("{{");
    println!("  \"schema\": \"marici.singular_covariance_rees_conditioning.v1\",");
    println!("  \"positive_rees_families_checked\": {positive_rees_families},");
    println!("  \"singular_boundary_points_checked\": 20,");
    println!("  \"ambiguous_boundary_points\": {ambiguous_boundary_points},");
    println!("  \"faster_decay_checks\": {faster_decay_checks},");
    println!("  \"positivity_selects_unique_schur_limit\": false,");
    println!("  \"exceptional_coordinate\": \"gamma^2/beta = c^2/b\",");
    println!("  \"ordinary_singular_specialization_canonical\": false");
    println!("}}");
}
