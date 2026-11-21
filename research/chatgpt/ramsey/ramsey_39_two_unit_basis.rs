// Enumerate normalized restricted 2-bases (repetition allowed in each sum).
fn dfs(v:&mut Vec<u32>,next:u32,mask:u64,c:&mut [u64;10]){
 let n=v.len(); if n*(n+1)/2-mask.count_ones() as usize>6{return} c[n]+=1;
 if n==9{if c[n]<=3{println!("basis {:?}",v)}return}
 for x in next..=(39-(9-n) as u32){let mut m=mask|1u64<<((2*x)%39); for &y in v.iter(){m|=1u64<<((x+y)%39)}v.push(x);dfs(v,x+1,m,c);v.pop();}
}
fn main(){let mut c=[0;10];dfs(&mut vec![0,1],2,7,&mut c);println!("prefix counts {:?}",c);}
