use std::collections::BTreeSet;

#[derive(Clone,Copy,Debug,Eq,Ord,PartialEq,PartialOrd)]
struct Rat{n:u128,d:u128}
fn gcd(mut a:u128,mut b:u128)->u128{while b!=0{let r=a%b;a=b;b=r;}a}
fn rat(n:u128,d:u128)->Rat{let g=gcd(n,d);Rat{n:n/g,d:d/g}}
fn mul(a:Rat,b:Rat)->Rat{rat(a.n*b.n,a.d*b.d)}
fn pow(mut a:Rat,mut n:usize)->Rat{let mut z=rat(1,1);while n>0{if n%2==1{z=mul(z,a);}a=mul(a,a);n/=2;}z}

// Squared coefficients of leaf cumulants. For cumulant order r, a block
// coefficient is (m/N)^(r/2), hence its square is (m/N)^r.
fn trees(n:usize,r:usize)->BTreeSet<Vec<Rat>>{
    if n==1{return vec![vec![rat(1,1)]].into_iter().collect();}
    let mut out=BTreeSet::new();
    for m in 1..n{
        let wl=pow(rat(m as u128,n as u128),r);
        let wr=pow(rat((n-m) as u128,n as u128),r);
        for l in trees(m,r){for rr in trees(n-m,r){
            let mut v=Vec::with_capacity(n);
            v.extend(l.iter().copied().map(|x|mul(wl,x)));
            v.extend(rr.iter().copied().map(|x|mul(wr,x)));
            out.insert(v);
        }}
    }
    out
}

fn catalan(n:usize)->usize{let mut c=vec![0usize;n+1];c[0]=1;for k in 1..=n{for i in 0..k{c[k]+=c[i]*c[k-1-i];}}c[n]}

fn main(){
    let mut species_counts=0usize;let mut leaf_checks=0usize;let mut bracketings=0usize;
    for r in 1..=12usize{for n in 1..=12usize{
        let got=trees(n,r);assert_eq!(got.len(),1);
        let expected=rat(1,(n as u128).pow(r as u32));
        for &x in got.iter().next().unwrap(){assert_eq!(x,expected);leaf_checks+=1;}
        species_counts+=1;bracketings+=catalan(n-1);
    }}
    println!("{{");
    println!("  \"schema\": \"marici.cardinality_weighted_cumulant_species.v1\",");
    println!("  \"max_cumulant_order\": 12,");
    println!("  \"max_occurrence_count\": 12,");
    println!("  \"species_occurrence_pairs_checked\": {species_counts},");
    println!("  \"leaf_coefficient_checks\": {leaf_checks},");
    println!("  \"ordered_binary_bracketings_certified\": {bracketings},");
    println!("  \"cumulant_orders_mix_under_merge\": false,");
    println!("  \"species_weight_rule\": \"(block_size/total_size)^(r/2)\"");
    println!("}}");
}
