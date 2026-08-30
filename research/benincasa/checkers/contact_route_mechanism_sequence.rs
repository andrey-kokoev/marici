fn rank(mut a: Vec<Vec<f64>>) -> usize {
    let (m,n)=(a.len(),a[0].len()); let mut r=0;
    for c in 0..n {if let Some(p)=(r..m).find(|&i|a[i][c].abs()>1e-9){
        a.swap(r,p); let q=a[r][c]; for j in c..n{a[r][j]/=q;}
        for i in 0..m{if i!=r{let q=a[i][c];for j in c..n{a[i][j]-=q*a[r][j];}}} r+=1;
    }} r
}
fn main(){
    let c=[2.,3.,5.];
    let mut t=vec![vec![0.;3];6];
    for e in 0..3 {t[2*e][e]=8.*c[e]; t[2*e+1][e]=-8.*c[e];}
    assert_eq!(rank(t.clone()),3);
    let mut sigma_t=vec![vec![0.;3];3];
    for e in 0..3 {for j in 0..3 {sigma_t[e][j]=t[2*e][j]+t[2*e+1][j];}}
    assert_eq!(rank(sigma_t),0);
    println!("{{\"status\":\"pass\",\"route_map_rank\":3,\"route_loss_rank\":0,\"interference_rank\":3,\"classification\":\"pure_destructive_interference\"}}");
}
