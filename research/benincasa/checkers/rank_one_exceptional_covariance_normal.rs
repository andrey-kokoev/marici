use std::collections::{BTreeMap,BTreeSet};

#[derive(Clone,Copy,Debug,Eq,Ord,PartialEq,PartialOrd)]
struct Rat{n:i64,d:i64}
fn gcd(mut a:i64,mut b:i64)->i64{a=a.abs();b=b.abs();while b!=0{let r=a%b;a=b;b=r;}a}
fn rat(n:i64,d:i64)->Rat{let g=gcd(n,d);Rat{n:n/g,d:d/g}}
fn sub(a:Rat,b:Rat)->Rat{rat(a.n*b.d-b.n*a.d,a.d*b.d)}

fn main(){
    // On the exact rank-one block diag(k,0), positivity of the principal
    // (A,null) minor forces the transverse cross coordinate y to vanish.
    let mut exact_stratum_tests=0usize;let mut allowed_transverse=0usize;
    for a in 1_i64..=20{for y in -20_i64..=20{
        let minor=0_i64*a-y*y;
        if minor>=0{allowed_transverse+=1;assert_eq!(y,0);}
        exact_stratum_tests+=1;
    }}
    assert_eq!(allowed_transverse,20);

    // Nearby K_t=diag(k,t^2 beta), v_t=(x,t gamma) retains the additional
    // finite correction gamma^2/beta while having the same rank-one limit.
    let mut limits:BTreeMap<(i64,i64,i64),BTreeSet<Rat>>=BTreeMap::new();
    let mut positive_families=0usize;
    for a in 1_i64..=20{for k in 1_i64..=10{for x in -10_i64..=10{
        if x*x>a*k{continue;}
        for beta in 1_i64..=10{for gamma in 0_i64..=10{
            let limit=sub(sub(rat(a,1),rat(x*x,k)),rat(gamma*gamma,beta));
            if limit.n<0{continue;}
            limits.entry((a,k,x)).or_default().insert(limit);
            positive_families+=1;
        }}
    }}}
    let ambiguous=limits.values().filter(|s|s.len()>1).count();
    assert!(ambiguous>0);

    println!("{{");
    println!("  \"schema\": \"marici.rank_one_exceptional_covariance_normal.v1\",");
    println!("  \"exact_rank_one_positivity_tests\": {exact_stratum_tests},");
    println!("  \"allowed_nonzero_transverse_coordinates\": 0,");
    println!("  \"positive_nearby_families_checked\": {positive_families},");
    println!("  \"rank_one_boundary_points_with_multiple_limits\": {ambiguous},");
    println!("  \"pseudoinverse_intrinsic_on_exact_stratum\": true,");
    println!("  \"nearby_specialization_canonical\": false,");
    println!("  \"secondary_normal_coordinate\": \"gamma^2/beta\"");
    println!("}}");
}
