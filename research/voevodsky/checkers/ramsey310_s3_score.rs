// Same frozen degree weights as ramsey310_s3_contrast.py. S3 permutes pairs, not sides.
fn s3_cut(a:&[u32],s:&[u32],p:B,l:[u32;3],r:[u32;3],need:[u32;26])->Option<(usize,usize,i32,i32)>{
 let mut deg=[0u32;8];for v in 0..26{deg[a[v].count_ones() as usize]|=1<<v}
 let pos=[0,1,2].map(|i|((l[i]|r[i])&deg[5])|(l[i]&deg[4]));let neg=l.map(|x|x&deg[7]);
 let d=[0,1,2].map(|i|(0..26).map(|v|need[v]as i32*(((pos[i]>>v)&1)as i32-((neg[i]>>v)&1)as i32)).sum::<i32>());
 let mut all=vec![];p.each(|j|all.push([0,1,2].map(|i|(s[j]&pos[i]).count_ones()as i32-(s[j]&neg[i]).count_ones()as i32)));
 for i in 0..3{for j in 0..3{if i==j{continue}let mut scores:Vec<_>=all.iter().map(|v|v[i]-v[j]).collect();scores.sort_unstable_by(|a,b|b.cmp(a));let upper=scores.iter().take(6).sum();if d[i]-d[j]>upper{return Some((i,j,d[i]-d[j],upper))}}}None
}
