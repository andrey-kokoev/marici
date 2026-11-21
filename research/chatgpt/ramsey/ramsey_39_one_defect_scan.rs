// Empty residue 0, doubled residue 1 (weights 1,14), normalized by affine relabelling.
fn main(){let mut cnt=0;for mut code in 0..3u32.pow(11){let mut w=vec![1u32,14];for j in 2..13{w.push(j+13*(code%3));code/=3;}let mut h=[0u32;39];for &a in &w{for &b in &w{h[((a+b)%39)as usize]+=1;}}if h.iter().any(|&x|x<2)||h.iter().map(|x|(2*x).min(9)).sum::<u32>()<272{continue}cnt+=1;let m=w.iter().map(|x|1u64<<x).sum::<u64>();let flip=w.iter().map(|x|1u64<<((14*x)%39)).sum::<u64>(); // 14 fixes residue mod13 and interchanges weights 1 and 14
if m<=flip{println!("{m}")}}eprintln!("passing {cnt}");}
