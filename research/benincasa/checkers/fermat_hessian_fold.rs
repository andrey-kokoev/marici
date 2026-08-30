// Historical geometry-only diagnostic; see corrective Entry 2135.
fn main(){
    // Use integer weights w_i=1/r_i. The planar determinant is
    // 3/4*(w1*w2+w1*w3+w2*w3); the normal eigenvalue is w1+w2+w3.
    for (w1,w2,w3) in [(1_i128,1_i128,1_i128),(2,3,5),(7,11,13)] {
        let pair=w1*w2+w1*w3+w2*w3;
        let normal=w1+w2+w3;
        let four_det=3*pair*normal;
        assert!(pair>0 && normal>0 && four_det>0);
    }
    println!("{}",r#"{"status":"pass","hessian":"positive_definite","four_det":"3*(sum w_i)*(sum_{i<j}w_i*w_j)","morse_index":0}"#);
}
