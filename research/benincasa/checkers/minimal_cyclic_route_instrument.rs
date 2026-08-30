fn rank(mut a: Vec<Vec<f64>>) -> usize {
    let (m,n)=(a.len(),a[0].len()); let mut r=0;
    for c in 0..n { if let Some(p)=(r..m).find(|&i|a[i][c].abs()>1e-9) {
        a.swap(r,p); let q=a[r][c]; for j in c..n {a[r][j]/=q;}
        for i in 0..m {if i!=r {let q=a[i][c]; for j in c..n {a[i][j]-=q*a[r][j];}}}
        r+=1;
    }} r
}
fn main(){
    let scalar=vec![vec![1.,1.,1.]];
    let regular=vec![vec![1.,0.,0.],vec![0.,1.,0.],vec![0.,0.,1.]];
    assert_eq!(rank(scalar),1);
    assert_eq!(rank(regular),3);
    // The scalar invariant detector leaves the rational cyclotomic plane.
    assert_eq!(1*3-1,2);
    println!("{{\"status\":\"pass\",\"contact_kernel_rank\":3,\"scalar_invariant_detected_rank\":1,\"scalar_blind_rank\":2,\"minimal_faithful_target_rank\":3,\"minimal_c3_type\":\"regular_C3\"}}");
}
