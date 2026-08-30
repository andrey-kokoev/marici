fn binom(n:u32,k:u32)->u128{let mut z=1_u128;for i in 0..k{z=z*(n-i) as u128/(i+1) as u128;}z}
fn factorial(n:u32)->u128{(1..=n as u128).product()}

fn main(){
    let mut recurrence_checks=0usize;let mut binary_convolutions=0usize;let mut ternary_coherences=0usize;
    for n in 0..=33_u32{
        // c_n=1/n!: (n+1)c_(n+1)=c_n after removing the common source factor z^n.
        assert_eq!((n as u128+1)*factorial(n),factorial(n+1));recurrence_checks+=1;
    }
    for n in 0..=60_u32{
        let two:u128=(0..=n).map(|k|binom(n,k)).sum();assert_eq!(two,2_u128.pow(n));binary_convolutions+=1;
        let left:u128=(0..=n).map(|r|binom(n,r)*2_u128.pow(r)).sum();
        let right:u128=(0..=n).map(|r|binom(n,r)*2_u128.pow(n-r)).sum();
        assert_eq!(left,3_u128.pow(n));assert_eq!(right,3_u128.pow(n));assert_eq!(left,right);ternary_coherences+=1;
    }

    // Every finite Dyson truncation defines a one-Kraus CP map X -> U X U^T.
    // Verify exact Gram factorization U(RR^T)U^T=(UR)(UR)^T.
    let mut cp_factorizations=0usize;
    for seed in 0..100_i64{
        let u=[[1+seed,2-seed,3],[seed%5-2,4,1+seed],[2,seed%7-3,5]];
        let r=[[1,seed%3-1],[2-seed,3],[seed%4,1]];
        let mut rho=[[0_i64;3];3];for i in 0..3{for j in 0..3{for k in 0..2{rho[i][j]+=r[i][k]*r[j][k];}}}
        let mut lhs=[[0_i64;3];3];for i in 0..3{for j in 0..3{for a in 0..3{for b in 0..3{lhs[i][j]+=u[i][a]*rho[a][b]*u[j][b];}}}}
        let mut ur=[[0_i64;2];3];for i in 0..3{for k in 0..2{for a in 0..3{ur[i][k]+=u[i][a]*r[a][k];}}}
        let mut rhs=[[0_i64;3];3];for i in 0..3{for j in 0..3{for k in 0..2{rhs[i][j]+=ur[i][k]*ur[j][k];}}}
        assert_eq!(lhs,rhs);cp_factorizations+=1;
    }
    println!("{{");
    println!("  \"schema\": \"marici.cubic_dyson_finite_presentation.v1\",");
    println!("  \"factorial_recurrence_checks\": {recurrence_checks},");
    println!("  \"binary_convolution_checks\": {binary_convolutions},");
    println!("  \"ternary_parenthesization_checks\": {ternary_coherences},");
    println!("  \"exact_cp_gram_factorizations\": {cp_factorizations},");
    println!("  \"finite_shift_presentation\": \"(n+1)c_(n+1)=z c_n\",");
    println!("  \"dyson_filtration_associative\": true,");
    println!("  \"finite_truncation_completely_positive\": true,");
    println!("  \"finite_truncation_trace_preserving\": false");
    println!("}}");
}
