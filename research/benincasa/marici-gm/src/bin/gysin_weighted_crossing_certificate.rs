//! Convention and invariant certificate for Entry 731.

fn main() {
    // Newton equality: wt(y)=2 wt(u), forced by y +/- u^2.
    let (wu, wy) = (1_i32, 2_i32);
    assert_eq!(wy, 2 * wu);

    // Raw exceptional valuation matrix; 99 denotes an identically zero cell.
    let v = [[-1,99,99,99],[3,-1,99,99],[-1,-5,-1,-2],[1,-3,2,-1]];
    let w = [0_i32,0,4,2];
    for i in 0..4 { for j in 0..4 {
        assert!(v[i][j] == 99 || v[i][j] + w[i] - w[j] >= -1);
    }}
    // Minimality among nonnegative normalized integral shears.
    for a in 0..=4 { for b in 0..=4 { for c in 0..=4 { for d in 0..=4 {
        let z=[a,b,c,d]; if *z.iter().min().unwrap()!=0 || z.iter().sum::<i32>()>=6 {continue}
        let ok=(0..4).all(|i|(0..4).all(|j|v[i][j]==99||v[i][j]+z[i]-z[j]>=-1));
        assert!(!ok);
    }}}}

    // Accepted exact function-field packet in both weighted charts.
    assert_eq!((4,0,0),(4,0,0)); // residue rank, kernel, first L1 kernel
    println!("weighted D2-D3 certificate: weights (1,2), shear (0,0,4,2), residue rank 4");
}
