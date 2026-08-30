use std::collections::BTreeSet;

#[derive(Clone,Copy,Debug,Eq,Ord,PartialEq,PartialOrd)]
struct Rat{n:i64,d:i64}
fn gcd(mut a:i64,mut b:i64)->i64{a=a.abs();b=b.abs();while b!=0{let r=a%b;a=b;b=r;}a}
fn rat(n:i64,d:i64)->Rat{let s=if d<0{-1}else{1};let g=gcd(n,d);Rat{n:s*n/g,d:d.abs()/g}}
fn add(a:Rat,b:Rat)->Rat{rat(a.n*b.d+b.n*a.d,a.d*b.d)}
fn mul(a:Rat,b:Rat)->Rat{rat(a.n*b.n,a.d*b.d)}

fn cross(s:&[Vec<Rat>],a:std::ops::Range<usize>,b:std::ops::Range<usize>)->Rat{
    let mut z=rat(0,1);
    for i in a{for j in b.clone(){z=add(z,s[i][j]);}}
    z
}

// Return all normalized variances obtained by all contiguous binary merge trees.
fn trees(s:&[Vec<Rat>],lo:usize,hi:usize)->BTreeSet<Rat>{
    if hi-lo==1{return vec![s[lo][lo]].into_iter().collect();}
    let mut out=BTreeSet::new();
    let total=(hi-lo) as i64;
    for mid in lo+1..hi{
        let nl=(mid-lo) as i64;let nr=(hi-mid) as i64;
        let k=cross(s,lo..mid,mid..hi);
        for vl in trees(s,lo,mid){for vr in trees(s,mid,hi){
            let extensive=add(add(mul(rat(nl,1),vl),mul(rat(nr,1),vr)),mul(rat(2,1),k));
            out.insert(mul(rat(1,total),extensive));
        }}
    }
    out
}

fn direct(s:&[Vec<Rat>])->Rat{
    let mut z=rat(0,1);
    for row in s{for &x in row{z=add(z,x);}}
    mul(rat(1,s.len() as i64),z)
}

fn catalan(n:usize)->usize{let mut c=vec![0usize;n+1];c[0]=1;for k in 1..=n{for i in 0..k{c[k]+=c[i]*c[k-1-i];}}c[n]}

fn main(){
    let mut matrices=0usize;let mut bracketings=0usize;let mut cross_updates=0usize;
    for n in 1..=11usize{
        for mode in 0..3usize{
            let mut s=vec![vec![rat(0,1);n];n];
            for i in 0..n{for j in i..n{
                let x=match mode{
                    0=>if i==j{rat((i+2) as i64,1)}else{rat(1,(i+j+2) as i64)},
                    1=>rat((i+j+1) as i64,(i*j+i+j+1) as i64),
                    _=>if i==j{rat(5,1)}else{rat(((i+1)*(j+2)) as i64,7)},
                };
                s[i][j]=x;s[j][i]=x;
            }}
            let got=trees(&s,0,n);
            assert_eq!(got.len(),1);
            assert_eq!(*got.iter().next().unwrap(),direct(&s));
            // Verify K_(A union B),C = K_A,C + K_B,C at every triple cut.
            for i in 1..n{for j in i+1..n{
                let lhs=cross(&s,0..j,j..n);
                let rhs=add(cross(&s,0..i,j..n),cross(&s,i..j,j..n));
                assert_eq!(lhs,rhs);cross_updates+=1;
            }}
            matrices+=1;bracketings+=catalan(n-1);
        }
    }
    println!("{{");
    println!("  \"schema\": \"marici.full_covariance_cut_descent.v1\",");
    println!("  \"max_internal_occurrence_count\": 11,");
    println!("  \"covariance_matrices_checked\": {matrices},");
    println!("  \"ordered_binary_bracketings_checked\": {bracketings},");
    println!("  \"cross_covariance_updates_checked\": {cross_updates},");
    println!("  \"full_covariance_merge_tree_independent\": true,");
    println!("  \"correlated_wick_cut_defect_natural\": true");
    println!("}}");
}
