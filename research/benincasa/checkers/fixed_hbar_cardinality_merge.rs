use std::collections::BTreeSet;

#[derive(Clone,Copy,Debug,Eq,Ord,PartialEq,PartialOrd)]
struct Rat{i:u64,j:u64}

fn gcd(mut a:u64,mut b:u64)->u64{while b!=0{let r=a%b;a=b;b=r;}a}
fn rat(i:u64,j:u64)->Rat{let g=gcd(i,j);Rat{i:i/g,j:j/g}}
fn mul(a:Rat,b:Rat)->Rat{rat(a.i*b.i,a.j*b.j)}

// Return every squared leaf-coefficient vector produced by every ordered
// binary bracketing of n labelled occurrences. A merge of block sizes m,n
// multiplies the left and right squared coefficients by m/(m+n), n/(m+n).
fn trees(n:usize)->BTreeSet<Vec<Rat>>{
    if n==1{return vec![vec![rat(1,1)]].into_iter().collect();}
    let mut out=BTreeSet::new();
    for m in 1..n{
        for l in trees(m){for r in trees(n-m){
            let mut v=Vec::with_capacity(n);
            v.extend(l.iter().copied().map(|x|mul(x,rat(m as u64,n as u64))));
            v.extend(r.iter().copied().map(|x|mul(x,rat((n-m) as u64,n as u64))));
            out.insert(v);
        }}
    }
    out
}

fn main(){
    let mut bracketings_checked=0usize;
    let mut leaf_weights_checked=0usize;
    for n in 1..=12{
        let outputs=trees(n);
        // Every binary tree must produce the same collective normalization.
        assert_eq!(outputs.len(),1);
        let v=outputs.iter().next().unwrap();
        assert_eq!(v.len(),n);
        for &x in v{assert_eq!(x,rat(1,n as u64));leaf_weights_checked+=1;}
        // Sum of squared coefficients is one, hence [Q_N,P_N]=i hbar.
        let numerator:u64=v.iter().map(|x|x.i).sum();
        assert_eq!(numerator,v[0].j);
        bracketings_checked+=catalan(n-1);
    }
    println!("{{");
    println!("  \"schema\": \"marici.fixed_hbar_cardinality_merge.v1\",");
    println!("  \"max_occurrence_count\": 12,");
    println!("  \"ordered_binary_bracketings_checked\": {bracketings_checked},");
    println!("  \"leaf_weights_checked\": {leaf_weights_checked},");
    println!("  \"unique_output_per_occurrence_count\": true,");
    println!("  \"fixed_hbar_preserved\": true,");
    println!("  \"cardinality_weighted_merge_associative\": true");
    println!("}}");
}

fn catalan(n:usize)->usize{
    let mut c=vec![0usize;n+1];c[0]=1;
    for k in 1..=n{for i in 0..k{c[k]+=c[i]*c[k-1-i];}}
    c[n]
}
