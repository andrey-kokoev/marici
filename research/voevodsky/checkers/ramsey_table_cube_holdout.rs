// Direct enumeration, no binomial formulas. Pass width as the only argument.
fn main(){
 let k:usize=std::env::args().nth(1).unwrap().parse().unwrap();assert!(k>=5);
 let n=k+1;let idx=|a,b,c| (a*n+b)*n+c;
 let mut rows=Vec::new();for a in 1..=k{for b in a+2..=k{for c in b+2..=k{rows.push([a,b,c]);}}}
 let(mut lo,mut hi,mut center)=(0,rows.len(),0);let mut upper=vec![false;n*n*n];
 while lo<hi{let [a,b,c]=rows[hi-1];let matched=rows[lo]==[n-c,n-b,n-a];if matched&&lo+1==hi{center=1;break}let [i,j,h]=rows[lo];upper[idx(i,j,h)]=true;lo+=1;if matched{hi-=1}}
 let mut seen=vec![false;upper.len()];let mut counts=[0usize;9];
 for a in 1..k{for b in a+1..k{for c in b+1..k{
 let corners:[usize;8]=std::array::from_fn(|s|idx(a+(s>>2),b+((s>>1)&1),c+(s&1)));
 if corners.iter().all(|&i|upper[i]){let mut fresh=0u8;for(s,&i)in corners.iter().enumerate(){if !seen[i]{fresh|=1<<s;seen[i]=true;}}assert!(fresh!=0);
 // Check Cartesian closure: each fresh corner set is a genuine face, not just the right size.
 let mut proj=[0u8;3];for s in 0..8{if fresh>>s&1!=0{for j in 0..3{proj[j]|=1<<((s>>j)&1)}}}assert_eq!(fresh.count_ones(),proj.iter().map(|m|m.count_ones()).product());counts[fresh.count_ones()as usize]+=1;}
 }}}
 let u=upper.iter().zip(&seen).filter(|(x,y)|**x&&!**y).count();assert_eq!(lo,u+counts.iter().enumerate().map(|(i,v)|i*v).sum::<usize>());
 println!("{{\"width\":{k},\"original\":{},\"upper\":{lo},\"center\":{center},\"cube\":{},\"square\":{},\"edge\":{},\"point\":{},\"uncovered\":{u},\"display_rows\":{},\"records\":{}}}",rows.len(),counts[8],counts[4],counts[2],counts[1],2*lo+center,2*(counts.iter().sum::<usize>()+u)+center);
}
