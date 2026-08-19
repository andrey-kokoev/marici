use serde_json::Value;
use std::collections::BTreeMap;
use std::fs;

fn add(a:u64,b:u64,p:u64)->u64{((a as u128+b as u128)%p as u128)as u64}
fn sub(a:u64,b:u64,p:u64)->u64{if a>=b{a-b}else{p-(b-a)}}
fn mul(a:u64,b:u64,p:u64)->u64{((a as u128*b as u128)%p as u128)as u64}
fn pow(mut a:u64,mut n:u64,p:u64)->u64{let mut r=1;while n>0{if n&1==1{r=mul(r,a,p)}a=mul(a,a,p);n>>=1;}r}
fn inv(a:u64,p:u64)->u64{assert_ne!(a,0);pow(a,p-2,p)}

fn mons(d:usize)->Vec<(usize,usize)>{
    if std::env::var_os("MARICI_RECON_UNIVAR_U").is_some(){return(0..=d).map(|i|(i,0)).collect()}
    (0..=d).flat_map(|s|(0..=s).map(move|i|(i,s-i))).collect()
}
fn eval_mons(u:u64,v:u64,ms:&[(usize,usize)],p:u64)->Vec<u64>{
    ms.iter().map(|(i,j)|mul(pow(u,*i as u64,p),pow(v,*j as u64,p),p)).collect()
}

fn pivot_rows(mut a:Vec<Vec<u64>>,p:u64)->Option<Vec<usize>>{
    let rows=a.len(); let cols=a[0].len(); let mut labels:Vec<usize>=(0..rows).collect(); let mut r=0;
    for c in 0..cols{
        let q=(r..rows).find(|i|a[*i][c]!=0)?;
        a.swap(r,q);labels.swap(r,q);let z=inv(a[r][c],p);
        for j in c..cols{a[r][j]=mul(a[r][j],z,p)}
        for i in 0..rows{if i!=r&&a[i][c]!=0{let z=a[i][c];for j in c..cols{a[i][j]=sub(a[i][j],mul(z,a[r][j],p),p)}}}
        r+=1;if r==cols{return Some(labels[..r].to_vec())}
    }
    None
}

fn inverse(mut a:Vec<Vec<u64>>,p:u64)->Vec<Vec<u64>>{
    let n=a.len();for(i,row)in a.iter_mut().enumerate(){row.extend((0..n).map(|j|u64::from(i==j)))}
    for c in 0..n{let q=(c..n).find(|i|a[*i][c]!=0).unwrap();a.swap(c,q);let z=inv(a[c][c],p);for j in 0..2*n{a[c][j]=mul(a[c][j],z,p)}for i in 0..n{if i!=c&&a[i][c]!=0{let z=a[i][c];for j in 0..2*n{a[i][j]=sub(a[i][j],mul(z,a[c][j],p),p)}}}}
    a.into_iter().map(|r|r[n..].to_vec()).collect()
}
fn row_mul(row:&[u64],m:&[Vec<u64>],p:u64)->Vec<u64>{
    (0..m[0].len()).map(|j|row.iter().zip(m).fold(0,|z,(x,r)|add(z,mul(*x,r[j],p),p))).collect()
}
fn mat_vec(m:&[Vec<u64>],v:&[u64],p:u64)->Vec<u64>{m.iter().map(|r|r.iter().zip(v).fold(0,|z,(a,b)|add(z,mul(*a,*b,p),p))).collect()}

fn null_line(mut a:Vec<Vec<u64>>,n:usize,p:u64)->Option<Vec<u64>>{
    let rows=a.len();let mut piv=Vec::new();let mut r=0;
    for c in 0..n{let Some(q)=(r..rows).find(|i|a[*i][c]!=0)else{continue};a.swap(r,q);let z=inv(a[r][c],p);for j in c..n{a[r][j]=mul(a[r][j],z,p)}for i in 0..rows{if i!=r&&a[i][c]!=0{let z=a[i][c];for j in c..n{a[i][j]=sub(a[i][j],mul(z,a[r][j],p),p)}}}piv.push(c);r+=1;if r==rows{break}}
    if n-r!=1{return None}let free=(0..n).find(|c|!piv.contains(c)).unwrap();let mut x=vec![0;n];x[free]=1;
    for(row,c)in piv.into_iter().enumerate().rev(){let mut z=0;for j in c+1..n{z=add(z,mul(a[row][j],x[j],p),p)}x[c]=sub(0,z,p)}Some(x)
}

#[derive(Clone)] struct Point{u:u64,v:u64,f:Vec<u64>}
fn load(path:&str)->(u64,Vec<Point>,u8){
    let root:Value=serde_json::from_str(&fs::read_to_string(path).unwrap()).unwrap();let p=root["prime"].as_u64().unwrap();
    if root["schema"].as_str().unwrap().contains("dual_sampler") {
        let points=root["dual_rows"].as_array().unwrap().iter().map(|q|{let u=q["u"].as_u64().unwrap();let v=q["v"].as_u64().unwrap();let f=q["vectors"].as_array().unwrap().iter().flat_map(|r|r.as_array().unwrap().iter().map(|x|x.as_u64().unwrap())).collect();Point{u,v,f}}).collect();
        return(p,points,1)
    }
    if root["schema"].as_str().unwrap().contains("primal_witness_sampler") {
        let points=root["accepted_points"].as_array().unwrap().iter().map(|q|Point{u:q["u"].as_u64().unwrap(),v:q["v"].as_u64().unwrap(),f:q["values"].as_array().unwrap().iter().map(|x|x.as_u64().unwrap()).collect()}).collect();
        return(p,points,2)
    }
    let mut map:BTreeMap<(u64,u64),[Option<Vec<Vec<u64>>>;2]>=BTreeMap::new();
    for q in root["wall_quotient_blocks"].as_array().unwrap(){let u=q["u"].as_u64().unwrap();let v=q["v"].as_u64().unwrap();let axis=usize::from(q["axis"].as_str().unwrap()=="v");let m=q["fixed_extension_e6_e9_mod_p"].as_array().unwrap().iter().map(|r|r.as_array().unwrap().iter().map(|x|x.as_u64().unwrap()).collect()).collect();map.entry((u,v)).or_default()[axis]=Some(m)}
    let points=map.into_iter().filter_map(|((u,v),axes)|{let[a,b]=axes;let(a,b)=(a?,b?);let mut f=Vec::new();for m in [a,b]{for row in m{f.extend(row)}}Some(Point{u,v,f})}).collect();(p,points,0)
}

fn attempt(points:&[Point],p:u64,dn:usize,dd:usize,ks:&[usize])->Option<(Vec<u64>,Vec<Vec<u64>>)> {
    let mn=mons(dn);let md=mons(dd);if points.len()<mn.len()+1{return None}
    let vn:Vec<_>=points.iter().map(|q|eval_mons(q.u,q.v,&mn,p)).collect();let wd:Vec<_>=points.iter().map(|q|eval_mons(q.u,q.v,&md,p)).collect();
    let piv=pivot_rows(vn.clone(),p)?;let v0:Vec<_>=piv.iter().map(|i|vn[*i].clone()).collect();let vi=inverse(v0,p);
    let rest:Vec<_>=(0..points.len()).filter(|i|!piv.contains(i)).collect();let mut constraints=Vec::new();
    for k in ks{for r in &rest{let t=row_mul(&vn[*r],&vi,p);let mut row=wd[*r].iter().map(|x|mul(points[*r].f[*k],*x,p)).collect::<Vec<_>>();for(j,pi)in piv.iter().enumerate(){let z=mul(t[j],points[*pi].f[*k],p);for c in 0..md.len(){row[c]=sub(row[c],mul(z,wd[*pi][c],p),p)}}constraints.push(row)}}
    let d=null_line(constraints,md.len(),p)?;let mut nums=Vec::new();
    for k in ks{let y:Vec<_>=piv.iter().map(|i|mul(points[*i].f[*k],wd[*i].iter().zip(&d).fold(0,|z,(a,b)|add(z,mul(*a,*b,p),p)),p)).collect();nums.push(mat_vec(&vi,&y,p))}
    for q in points{let dv=eval_mons(q.u,q.v,&md,p).iter().zip(&d).fold(0,|z,(a,b)|add(z,mul(*a,*b,p),p));if dv==0{return None}let nv=eval_mons(q.u,q.v,&mn,p);for(out,k)in ks.iter().enumerate(){let z=nv.iter().zip(&nums[out]).fold(0,|s,(a,b)|add(s,mul(*a,*b,p),p));if z!=mul(q.f[*k],dv,p){return None}}}
    Some((d,nums))
}

fn main(){
    let path=std::env::args().nth(1).expect("sample packet path");let(p,mut points,mode)=load(&path);let max=std::env::var("MARICI_MAX_RECON_DEGREE").ok().and_then(|x|x.parse().ok()).unwrap_or(15usize);
    if let Some(n)=std::env::var("MARICI_RECON_TRAIN_POINTS").ok().and_then(|x|x.parse::<usize>().ok()){points.truncate(n.min(points.len()))}
    let mut out=Vec::new();
    if mode==2 {
        let ks:Vec<_>=(0..117).collect();let direct=std::env::var("MARICI_RECON_DEGREES").ok().map(|x|{let mut q=x.split(',').map(|z|z.parse::<usize>().expect("degree"));(q.next().unwrap(),q.next().unwrap())});let mut found=None;if let Some((dn,dd))=direct{if let Some((d,n))=attempt(&points,p,dn,dd,&ks){found=Some((dn,dd,d,n))}}else{let total_start=std::env::var("MARICI_RECON_TOTAL_START").ok().and_then(|x|x.parse().ok()).unwrap_or(0);for total in total_start..=2*max{for dd in 0..=max{let Some(dn)=total.checked_sub(dd)else{continue};if dn>max{continue}if let Some((d,n))=attempt(&points,p,dn,dd,&ks){found=Some((dn,dd,d,n));break}}if found.is_some(){break}}}let(dn,dd,d,n)=found.unwrap_or_else(||panic!("no primal witness reconstruction through degree {max}"));println!("{{\"schema\":\"marici.benincasa.marked_extension_primal_witness_reconstruct.v1\",\"prime\":{},\"points\":{},\"numerator_degree\":{},\"denominator_degree\":{},\"denominator\":{:?},\"numerators\":{:?}}}",p,points.len(),dn,dd,d,n);return
    }
    if mode==1 {
        let coordinates:Vec<usize>=std::env::var("MARICI_DUAL_COORDINATE").ok().map(|x|vec![x.parse::<usize>().expect("dual coordinate")-8]).unwrap_or_else(||(0..4).collect());
        for coordinate in coordinates { let ks:Vec<_>=(coordinate*132..(coordinate+1)*132).collect();let direct=std::env::var("MARICI_RECON_DEGREES").ok().map(|x|{let mut q=x.split(',').map(|z|z.parse::<usize>().expect("degree"));(q.next().unwrap(),q.next().unwrap())});let mut found=None;if let Some((dn,dd))=direct{if let Some((d,n))=attempt(&points,p,dn,dd,&ks){found=Some((dn,dd,d,n))}}else{let total_start=std::env::var("MARICI_RECON_TOTAL_START").ok().and_then(|x|x.parse().ok()).unwrap_or(0);for total in total_start..=2*max{for dd in 0..=max{let Some(dn)=total.checked_sub(dd)else{continue};if dn>max{continue}if let Some((d,n))=attempt(&points,p,dn,dd,&ks){found=Some((dn,dd,d,n));break}}if found.is_some(){break}}}let(dn,dd,d,n)=found.unwrap_or_else(||panic!("no dual coordinate {} reconstruction through degree {max}",coordinate+8));out.push(format!("{{\"coordinate\":{},\"numerator_degree\":{},\"denominator_degree\":{},\"denominator\":{:?},\"numerators\":{:?}}}",coordinate+8,dn,dd,d,n))}
        println!("{{\"schema\":\"marici.benincasa.marked_extension_dual_reconstruct.v1\",\"prime\":{},\"points\":{},\"dual_rows\":[{}]}}",p,points.len(),out.join(","));return
    }
    for k in 0..24{let axis=if k<12{"u"}else{"v"};let local=k%12;let row=local/3;let col=local%3;let mut found=None;for total in 0..=2*max{for dd in 0..=max{let Some(dn)=total.checked_sub(dd)else{continue};if dn>max{continue}if let Some((d,n))=attempt(&points,p,dn,dd,&[k]){found=Some((dn,dd,d,n));break}}if found.is_some(){break}}let(dn,dd,d,n)=found.unwrap_or_else(||panic!("no {axis}[{row},{col}] reconstruction through degree {max}"));out.push(format!("{{\"axis\":\"{}\",\"row\":{},\"column\":{},\"numerator_degree\":{},\"denominator_degree\":{},\"denominator\":{:?},\"numerator\":{:?}}}",axis,row,col,dn,dd,d,n[0]))}
    println!("{{\"schema\":\"marici.benincasa.marked_extension_joint_reconstruct.v3\",\"prime\":{},\"points\":{},\"entries\":[{}]}}",p,points.len(),out.join(","))
}
