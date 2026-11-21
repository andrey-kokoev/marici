// Count normalized ten-distinct-weight 2-bases mod 39. Count is not modulo isomorphism.
fn dfs(v:&mut Vec<u32>, next:u32, mask:u64, count:&mut u64, sample:&mut Vec<u32>) {
    let n=v.len();
    if n*(n+1)/2-mask.count_ones() as usize > 55-39 {return;}
    if n==10 {assert_eq!(mask.count_ones(),39); *count+=1; if sample.is_empty(){*sample=v.clone();} return;}
    for x in next..=(39-(10-n) as u32) {
        let mut m=mask|1u64<<((2*x)%39); for &y in v.iter(){m|=1u64<<((x+y)%39);}
        v.push(x);dfs(v,x+1,m,count,sample);v.pop();
    }
}
fn main(){let mut count=0;let mut sample=vec![];dfs(&mut vec![0,1],2,7,&mut count,&mut sample);
println!("normalized covering sets: {count}, example: {sample:?}");
let mut odd=0u64;for i in (0..10).step_by(2){for j in (1..10).step_by(2){odd|=1u64<<((sample[i]+sample[j])%39);}}
println!("phases with no odd address in this order: {:?}",(0..39).filter(|k|odd&(1u64<<k)==0).collect::<Vec<_>>());}
