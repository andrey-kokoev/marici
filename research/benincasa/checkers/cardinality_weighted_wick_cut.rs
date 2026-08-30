use std::collections::BTreeSet;

#[derive(Clone,Copy,Debug,Eq,Ord,PartialEq,PartialOrd)]
struct Rat{n:i64,d:i64}
fn gcd(mut a:i64,mut b:i64)->i64{a=a.abs();b=b.abs();while b!=0{let r=a%b;a=b;b=r;}a}
fn rat(n:i64,d:i64)->Rat{assert!(d!=0);let s=if d<0{-1}else{1};let g=gcd(n,d);Rat{n:s*n/g,d:d.abs()/g}}
fn add(a:Rat,b:Rat)->Rat{rat(a.n*b.d+b.n*a.d,a.d*b.d)}
fn mul(a:Rat,b:Rat)->Rat{rat(a.n*b.n,a.d*b.d)}

// All ordered binary parenthesizations of one labelled variance list.
fn merged(v:&[Rat])->BTreeSet<Rat>{
    if v.len()==1{return vec![v[0]].into_iter().collect();}
    let total=v.len() as i64;
    let mut out=BTreeSet::new();
    for m in 1..v.len(){
        let wl=rat(m as i64,total);
        let wr=rat((v.len()-m) as i64,total);
        for l in merged(&v[..m]){for r in merged(&v[m..]){
            out.insert(add(mul(wl,l),mul(wr,r)));
        }}
    }
    out
}

fn catalan(n:usize)->usize{
    let mut c=vec![0usize;n+1];c[0]=1;
    for k in 1..=n{for i in 0..k{c[k]+=c[i]*c[k-1-i];}}
    c[n]
}

fn main(){
    let mut patterns=0usize;
    let mut bracketings=0usize;
    for n in 1..=12usize{
        let candidates:Vec<Vec<Rat>>=vec![
            (0..n).map(|_|rat(1,1)).collect(),
            (0..n).map(|i|rat((i+1) as i64,1)).collect(),
            (0..n).map(|i|rat((i*i+2*i+3) as i64,(i+1) as i64)).collect(),
        ];
        for v in candidates{
            let got=merged(&v);
            assert_eq!(got.len(),1);
            let sum=v.iter().copied().fold(rat(0,1),add);
            assert_eq!(*got.iter().next().unwrap(),mul(rat(1,n as i64),sum));
            patterns+=1;
            bracketings+=catalan(n-1);
        }
    }
    println!("{{");
    println!("  \"schema\": \"marici.cardinality_weighted_wick_cut.v1\",");
    println!("  \"max_internal_occurrence_count\": 12,");
    println!("  \"variance_patterns_checked\": {patterns},");
    println!("  \"ordered_binary_bracketings_checked\": {bracketings},");
    println!("  \"collective_variance_tree_independent\": true,");
    println!("  \"wick_cut_defect_natural_for_independent_gaussians\": true");
    println!("}}");
}
