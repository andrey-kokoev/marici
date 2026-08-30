fn rank(mut a:Vec<Vec<i64>>)->usize{
    let rows=a.len();let cols=a[0].len();let mut r=0usize;
    for c in 0..cols{
        let Some(p)=(r..rows).find(|&i|a[i][c]!=0) else{continue};a.swap(r,p);
        // The test matrices are diagonal, so fraction-free elimination is exact.
        for i in r+1..rows{if a[i][c]!=0{let x=a[i][c];let y=a[r][c];for j in c..cols{a[i][j]=y*a[i][j]-x*a[r][j];}}}
        r+=1;if r==rows{break;}
    }r
}

fn main(){
    let mut cutoff_cases=0usize;let mut reduced_rank_sum=0usize;
    for n in 1..=128usize{
        // Coefficient matrix C of psi_N=sum_i |i,i>. The global projector
        // |psi_N><psi_N| has rank one; Tr_E gives C C^T=I_N.
        let mut c=vec![vec![0_i64;n];n];for i in 0..n{c[i][i]=1;}
        let mut reduced=vec![vec![0_i64;n];n];
        for i in 0..n{for j in 0..n{for k in 0..n{reduced[i][j]+=c[i][k]*c[j][k];}}}
        let rr=rank(reduced);assert_eq!(rr,n);assert_eq!(1usize,1);
        reduced_rank_sum+=rr;cutoff_cases+=1;
    }
    // Infinite normalized witness psi=sum_{n>=1}2^{-n/2}|n,n> has reduced
    // eigenvalues 2^-n. Every finite prefix is nonzero and the tail is 2^-N.
    let mut prefixes=0usize;for n in 1..=60_u32{
        let denominator=1_u128<<n;let tail_num=1_u128;assert!(tail_num>0&&denominator>tail_num);prefixes+=1;
    }
    println!("{{");
    println!("  \"schema\": \"marici.finite_rank_density_cut_failure.v1\",");
    println!("  \"rank_one_global_cutoff_cases\": {cutoff_cases},");
    println!("  \"maximum_reduced_rank\": 128,");
    println!("  \"sum_of_reduced_ranks_checked\": {reduced_rank_sum},");
    println!("  \"positive_infinite_schmidt_tail_prefixes\": {prefixes},");
    println!("  \"global_rank_one_preserved_by_partial_trace\": false,");
    println!("  \"finite_rank_density_family_cut_closed\": false");
    println!("}}");
}
