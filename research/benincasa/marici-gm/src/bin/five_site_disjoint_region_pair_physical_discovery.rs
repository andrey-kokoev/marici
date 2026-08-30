use serde_json::{json, Value};
use std::{f64::consts::PI, fs};

type V3 = [f64; 3];

fn add(a: V3, b: V3) -> V3 { [a[0]+b[0], a[1]+b[1], a[2]+b[2]] }
fn sub(a: V3, b: V3) -> V3 { [a[0]-b[0], a[1]-b[1], a[2]-b[2]] }
fn scale(s: f64, a: V3) -> V3 { [s*a[0], s*a[1], s*a[2]] }
fn dot(a: V3, b: V3) -> f64 { a[0]*b[0]+a[1]*b[1]+a[2]*b[2] }
fn norm(a: V3) -> f64 { dot(a,a).sqrt() }
fn cross(a: V3, b: V3) -> V3 {
    [a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0]]
}

fn cuts(label: &str) -> Vec<usize> {
    let mut sites=[false;5];
    for c in label.strip_prefix("g_").unwrap().chars() {
        sites[c.to_digit(10).unwrap() as usize-1]=true;
    }
    (0..5).filter(|&e| sites[e] != sites[(e+1)%5]).collect()
}

fn residual(x: V3, a: &[usize], b: &[usize], m: f64, n: f64, centers: &[V3]) -> [f64;4] {
    let mut r=[0.;5]; let mut u=[[0.;3];5];
    for i in 0..5 { let d=sub(x,centers[i]); r[i]=norm(d); if r[i]<1e-10{return [1e6;4]} u[i]=scale(1./r[i],d); }
    let va=add(u[a[0]],u[a[1]]); let vb=add(u[b[0]],u[b[1]]); let c=cross(va,vb);
    let sa=r[a[0]]+r[a[1]]; let sb=r[b[0]]+r[b[1]]; let q=(n*sa-m*sb)/(1_f64.max(sa).max(sb));
    [q,c[0],c[1],c[2]]
}
fn rnorm(r:[f64;4])->f64{r.iter().map(|q|q*q).sum::<f64>().sqrt()}

fn solve3(mut a:[[f64;3];3],mut b:[f64;3])->Option<V3>{
    for k in 0..3 {
        let p=(k..3).max_by(|&i,&j|a[i][k].abs().partial_cmp(&a[j][k].abs()).unwrap()).unwrap();
        if a[p][k].abs()<1e-18{return None} a.swap(k,p);b.swap(k,p);
        for i in k+1..3{let f=a[i][k]/a[k][k];for j in k..3{a[i][j]-=f*a[k][j]}b[i]-=f*b[k];}
    }
    let mut x=[0.;3];for i in (0..3).rev(){x[i]=(b[i]-(i+1..3).map(|j|a[i][j]*x[j]).sum::<f64>())/a[i][i];}Some(x)
}

fn lm(mut x:V3,a:&[usize],b:&[usize],m:f64,n:f64,c:&[V3])->(V3,f64){
    let mut mu=1e-4; let mut rr=residual(x,a,b,m,n,c); let mut best=rnorm(rr);
    for _ in 0..400 {
        let h=1e-6*(1.+norm(x));let mut j=[[0.;3];4];
        for k in 0..3{let mut xp=x;xp[k]+=h;let rp=residual(xp,a,b,m,n,c);for i in 0..4{j[i][k]=(rp[i]-rr[i])/h;}}
        let mut aa=[[0.;3];3];let mut bb=[0.;3];
        for k in 0..3{for l in 0..3{aa[k][l]=(0..4).map(|i|j[i][k]*j[i][l]).sum();}aa[k][k]+=mu;bb[k]=-(0..4).map(|i|j[i][k]*rr[i]).sum::<f64>();}
        let Some(dx)=solve3(aa,bb) else{break}; let xn=add(x,dx);let rn=residual(xn,a,b,m,n,c);let score=rnorm(rn);
        if score<best{x=xn;rr=rn;best=score;mu*=0.3;if norm(dx)<1e-11{break}}else{mu*=10.;if mu>1e14{break}}
    }(x,best)
}

fn main(){
    let source:Value=serde_json::from_str(&fs::read_to_string("../results/five-site-region-pair-physical-gradient-reduction.json").unwrap()).unwrap();
    let labels=source["disjoint_cut_candidates"].as_array().unwrap();
    let p=(0..5).map(|k|[(2.*PI*k as f64/5.).cos(),(2.*PI*k as f64/5.).sin(),1.]).collect::<Vec<_>>();
    let mut centers=vec![[0.;3]];for k in 0..4{centers.push(add(centers[k],p[k]));}
    let mut state=0x8f4d_63a2_19b7_c501_u64;let mut random=||{state=state.wrapping_mul(6364136223846793005).wrapping_add(1442695040888963407);((state>>11)as f64)/(1_u64<<53)as f64};
    let mut records=Vec::new();
    for pair in labels{
        let pair=pair.as_array().unwrap();let left=pair[0].as_str().unwrap();let right=pair[1].as_str().unwrap();let a=cuts(left);let b=cuts(right);let m=left.len()-2;let n=right.len()-2;
        let mut sols:Vec<V3>=Vec::new();
        for s in 0..1200{
            let x0=if s<centers.len(){centers[s]}else{[(random()-0.5)*16.,(random()-0.5)*16.,(random()-0.5)*16.]};
            let (x,score)=lm(x0,&a,&b,m as f64,n as f64,&centers);if score>1e-8||norm(x)>100.{continue}
            let da=a.iter().map(|&i|{let d=sub(x,centers[i]);scale(1./norm(d),d)}).fold([0.;3],add);
            let db=b.iter().map(|&i|{let d=sub(x,centers[i]);scale(1./norm(d),d)}).fold([0.;3],add);
            if norm(da)<1e-7||norm(db)<1e-7||dot(da,db)>=0.{continue}
            if sols.iter().all(|&q|norm(sub(x,q))>1e-5){sols.push(x)}
        }
        records.push(json!({"representative":[left,right],"cut_supports":[a,b],"starts":1200,"candidate_count":sols.len(),"candidates":sols}));
    }
    let packet=json!({"schema":"marici.five_site_disjoint_region_pair_physical_discovery.v1","precision":"f64 bounded LM discovery; every survivor requires exact certification and a null census is not proof","records":records,"total_candidate_count":records.iter().map(|r|r["candidate_count"].as_u64().unwrap()).sum::<u64>()});
    fs::write("../results/five-site-disjoint-region-pair-physical-discovery.json",serde_json::to_string_pretty(&packet).unwrap()+"\n").unwrap();
    println!("{}",serde_json::to_string(&json!({"total_candidate_count":packet["total_candidate_count"],"counts":packet["records"].as_array().unwrap().iter().map(|r|json!([r["representative"].clone(),r["candidate_count"].clone()])).collect::<Vec<_>>() })).unwrap());
}
