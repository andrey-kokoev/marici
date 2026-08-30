fn rank(mut a:Vec<Vec<f64>>)->usize{let(m,n)=(a.len(),a[0].len());let mut r=0;for c in 0..n{if let Some(p)=(r..m).find(|&i|a[i][c].abs()>1e-9){a.swap(r,p);let q=a[r][c];for j in c..n{a[r][j]/=q;}for i in 0..m{if i!=r{let q=a[i][c];for j in c..n{a[i][j]-=q*a[r][j];}}}r+=1;}}r}
fn eval(y:&[i64],d:usize)->Vec<Vec<f64>>{y.iter().map(|x|(0..d).map(|k|(*x as f64).powi(k as i32)).collect()).collect()}
fn main(){
    assert_eq!(rank(eval(&[2,3,5,7],4)),4);
    assert_eq!(rank(eval(&[2,2,5,5,7],3)),3);
    assert_eq!(rank(eval(&[2,2,2,2],1)),1);
    println!("{{\"status\":\"pass\",\"rank_rule\":\"number_of_distinct_edge_energies\",\"faithful_jet_degree\":\"d-1 for d distinct energies\",\"collision_support_type\":\"readout_rank_loss\"}}");
}
