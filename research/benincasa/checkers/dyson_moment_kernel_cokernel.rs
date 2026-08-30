use std::collections::BTreeMap;
type Poly=BTreeMap<(usize,usize),i64>;

fn add_mod(a:i64,b:i64,p:i64)->i64{let z=(a+b)%p;if z<0{z+p}else{z}}
fn mul_mod(a:i64,b:i64,p:i64)->i64{((a as i128*b as i128)%(p as i128)) as i64}
fn d(f:&Poly,pmod:i64)->Poly{
    let mut o=Poly::new();for (&(q,p),&c) in f{
        if q>0{let k=(q-1,p+1);let v=mul_mod(c,q as i64,pmod);let z=add_mod(*o.get(&k).unwrap_or(&0),v,pmod);if z==0{o.remove(&k);}else{o.insert(k,z);}}
        if p>0{let k=(q+2,p-1);let v=mul_mod(c,-(p as i64),pmod);let z=add_mod(*o.get(&k).unwrap_or(&0),v,pmod);if z==0{o.remove(&k);}else{o.insert(k,z);}}
    }o
}
fn basis(deg:usize)->Vec<(usize,usize)>{(0..=deg).flat_map(|t|(0..=t).map(move|q|(q,t-q))).collect()}
fn pow_mod(mut a:i64,mut n:i64,p:i64)->i64{let mut z=1_i64;while n>0{if n%2==1{z=mul_mod(z,a,p);}a=mul_mod(a,a,p);n/=2;}z}
fn rank(mut a:Vec<Vec<i64>>,p:i64)->usize{
    let rows=a.len();let cols=if rows==0{0}else{a[0].len()};let mut r=0usize;
    for c in 0..cols{let Some(piv)=(r..rows).find(|&i|a[i][c]!=0)else{continue};a.swap(r,piv);
        let inv=pow_mod(a[r][c],p-2,p);for j in c..cols{a[r][j]=mul_mod(a[r][j],inv,p);}
        for i in 0..rows{if i!=r&&a[i][c]!=0{let x=a[i][c];for j in c..cols{a[i][j]=add_mod(a[i][j],-mul_mod(x,a[r][j],p),p);}}}
        r+=1;if r==rows{break;}
    }r
}

fn main(){
    let primes=[1_000_000_007_i64,1_000_000_009_i64];
    let mut maps=0usize;let mut prime_rank_agreements=0usize;let mut predicted_kernel_matches=0usize;
    let mut min_cokernel=usize::MAX;let mut max_cokernel=0usize;let mut conserved_checks=0usize;
    for deg in 0..=18usize{for n in 1..=6usize{
        let src=basis(deg);let tgt=basis(deg+n);let idx:BTreeMap<(usize,usize),usize>=tgt.iter().enumerate().map(|(i,&x)|(x,i)).collect();
        let mut ranks=Vec::new();
        for &pm in &primes{
            let mut mat=vec![vec![0_i64;src.len()];tgt.len()];
            for (j,&mon) in src.iter().enumerate(){let mut f=Poly::from([(mon,1_i64)]);for _ in 0..n{f=d(&f,pm);}for (k,c) in f{mat[idx[&k]][j]=c;}}
            ranks.push(rank(mat,pm));
        }
        assert_eq!(ranks[0],ranks[1]);prime_rank_agreements+=1;
        let kernel=src.len()-ranks[0];let predicted=deg/3+1;assert_eq!(kernel,predicted);predicted_kernel_matches+=1;
        let cokernel=tgt.len()-ranks[0];min_cokernel=min_cokernel.min(cokernel);max_cokernel=max_cokernel.max(cokernel);maps+=1;

        // H_tilde=3p^2+2q^3 and all powers fitting the source filtration are killed by D^n.
        for k in 0..=deg/3{for &pm in &primes{
            let mut h=Poly::from([((0,0),1_i64)]);
            for _ in 0..k{let mut next=Poly::new();for (&(q,p),&c) in &h{
                for (dq,dp,coef) in [(0,2,3_i64),(3,0,2_i64)]{let key=(q+dq,p+dp);let z=add_mod(*next.get(&key).unwrap_or(&0),mul_mod(c,coef,pm),pm);next.insert(key,z);}
            }h=next;}
            for _ in 0..n{h=d(&h,pm);}assert!(h.is_empty());conserved_checks+=1;
        }}
    }}
    println!("{{");
    println!("  \"schema\": \"marici.dyson_moment_kernel_cokernel.v1\",");
    println!("  \"filtered_maps_checked\": {maps},");
    println!("  \"two_prime_rank_agreements\": {prime_rank_agreements},");
    println!("  \"kernel_formula_matches\": {predicted_kernel_matches},");
    println!("  \"conserved_hamiltonian_power_checks\": {conserved_checks},");
    println!("  \"kernel_dimension_formula\": \"floor(D/3)+1\",");
    println!("  \"minimum_cokernel_dimension\": {min_cokernel},");
    println!("  \"maximum_cokernel_dimension\": {max_cokernel},");
    println!("  \"stable_relative_class_identified\": false");
    println!("}}");
}
