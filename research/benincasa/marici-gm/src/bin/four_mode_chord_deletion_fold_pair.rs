//! Numerical discovery of the second local sheet at the Gaussian rank-drop fold.
//! Exact certification is deliberately deferred to a separate algebraic checker.

use serde_json::{json, Value};
use std::fs;

fn det_x(x: &[f64; 4]) -> f64 {
    let [a,b,c,d] = *x;
    1.0-2.0*a*b*c*d-a*a+a*a*c*c-b*b+b*b*d*d-c*c-d*d
}

fn readout(x: &[f64; 4]) -> [f64; 4] {
    let [a,b,c,d] = *x;
    let q = 4.0*det_x(x);
    [a*(-a+a*c*c-b*c*d)/q,
     -b*(a*c*d+b-b*d*d)/q,
     c*(-a*b*d-c+a*a*c)/q,
     -d*(a*b*c+d-b*b*d)/q]
}

fn cycle(x: &[f64; 4]) -> f64 {
    let [a,b,c,d] = *x;
    let n = 2.0*a*b*c*d-a*b*c*d.powi(3)-a*b*c.powi(3)*d-a*b.powi(3)*c*d
        +2.0*a*b.powi(3)*c*d.powi(3)+a*a*b*b*c*c-4.0*a*a*b*b*c*c*d*d
        +a*a*b*b*d*d+a*a*c*c*d*d-a.powi(3)*b*c*d
        +2.0*a.powi(3)*b*c.powi(3)*d+b*b*c*c*d*d;
    n/(16.0*det_x(x).powi(2))
}

fn parse_q(s:&str)->f64 {
    if let Some((n,d))=s.split_once('/') { n.parse::<f64>().unwrap()/d.parse::<f64>().unwrap() }
    else { s.parse().unwrap() }
}

fn solve4(mut a: [[f64;4];4], mut b: [f64;4]) -> Option<[f64;4]> {
    for k in 0..4 {
        let p=(k..4).max_by(|&i,&j| a[i][k].abs().partial_cmp(&a[j][k].abs()).unwrap())?;
        if a[p][k].abs()<1e-18 { return None; }
        a.swap(k,p); b.swap(k,p);
        for i in k+1..4 { let q=a[i][k]/a[k][k]; for j in k..4 {a[i][j]-=q*a[k][j];} b[i]-=q*b[k]; }
    }
    let mut x=[0.0;4];
    for i in (0..4).rev() { x[i]=(b[i]-(i+1..4).map(|j|a[i][j]*x[j]).sum::<f64>())/a[i][i]; }
    Some(x)
}

fn det3(m:[[f64;3];3])->f64 { m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1])-m[0][1]*(m[1][0]*m[2][2]-m[1][2]*m[2][0])+m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0]) }
fn null_from_three_rows(rows:[[f64;4];3])->[f64;4] {
    let mut z=[0.0;4];
    for omit in 0..4 { let m: [[f64;3];3]=std::array::from_fn(|i| {let mut q=0; std::array::from_fn(|_|{while q==omit{q+=1;} let v=rows[i][q];q+=1;v})}); z[omit]=(if omit%2==0{1.0}else{-1.0})*det3(m); }
    let n=z.iter().map(|v|v*v).sum::<f64>().sqrt(); z.map(|v|v/n)
}
fn jacobian(x:&[f64;4])->[[f64;4];4] { let mut j=[[0.0;4];4]; for c in 0..4 {let h=1e-6*(1.0+x[c].abs());let mut p=*x;let mut m=*x;p[c]+=h;m[c]-=h;let fp=readout(&p);let fm=readout(&m);for r in 0..4{j[r][c]=(fp[r]-fm[r])/(2.0*h);}}j }

fn newton(mut x:[f64;4], target:[f64;4]) -> Option<[f64;4]> {
    for _ in 0..100 {
        let y=readout(&x); let f:[f64;4]=std::array::from_fn(|i| y[i]-target[i]);
        if f.iter().map(|v|v.abs()).fold(0.0,f64::max)<1e-12 { return Some(x); }
        let mut j=[[0.0;4];4];
        for c in 0..4 { let h=1e-6*(1.0+x[c].abs()); let mut xp=x; let mut xm=x; xp[c]+=h; xm[c]-=h;
            let yp=readout(&xp); let ym=readout(&xm); for r in 0..4 {j[r][c]=(yp[r]-ym[r])/(2.0*h);} }
        let mut normal=[[0.0;4];4]; let mut rhs=[0.0;4];
        for p in 0..4 { for q in 0..4 {normal[p][q]=(0..4).map(|r|j[r][p]*j[r][q]).sum();}
            normal[p][p]+=1e-14; rhs[p]=-(0..4).map(|r|j[r][p]*f[r]).sum::<f64>(); }
        let step=solve4(normal,rhs)?;
        let mut accepted=false;
        for back in 0..16 { let t=0.5f64.powi(back); let trial=std::array::from_fn(|i|x[i]+t*step[i]);
            if det_x(&trial)>0.0 && readout(&trial).iter().zip(target).map(|(u,v)|(u-v).abs()).fold(0.0,f64::max)
                < f.iter().map(|v|v.abs()).fold(0.0,f64::max) {x=trial; accepted=true; break;} }
        if !accepted{return None;}
    } None
}

fn main() {
    let p="../checkers/results/four-mode-chord-deletion-rankdrop-census.json";
    let v:Value=serde_json::from_str(&fs::read_to_string(p).unwrap()).unwrap();
    let b=&v["certified_positive_segment_bracket"];
    let parse=|side:&str| -> [f64;4] { std::array::from_fn(|i|parse_q(b[side][i].as_str().unwrap())) };
    let l=parse("left"); let r=parse("right"); let fold:[f64;4]=std::array::from_fn(|i|(l[i]+r[i])/2.0);
    let j=jacobian(&fold); let right=null_from_three_rows([j[0],j[1],j[2]]);
    let jt:[[f64;4];4]=std::array::from_fn(|i|std::array::from_fn(|q|j[q][i]));
    let left=null_from_three_rows([jt[0],jt[1],jt[2]]);
    let k=right;
    let mut out=Vec::new();
    for scale in [1e-4,3e-4,1e-3,3e-3,1e-2,3e-2] {
      for side in [-1.0,1.0] {
        let source=std::array::from_fn(|i|fold[i]+side*scale*k[i]);
        let reflected=std::array::from_fn(|i|fold[i]-side*scale*k[i]);
        let target=readout(&source);
        if let (Some(x1),Some(x2))=(newton(source,target),newton(reflected,target)) {
            let sep=x1.iter().zip(x2).map(|(u,v)|(u-v).powi(2)).sum::<f64>().sqrt();
            if sep>1e-7 { let residual=readout(&x1).iter().zip(readout(&x2)).map(|(u,v)|(u-v).abs()).fold(0.0,f64::max);
                out.push(json!({"scale":scale,"source_side":side,"first":x1,"second":x2,"edge_readout":readout(&x1),"edge_residual_max":residual,
                    "parameter_separation":sep,"cycle_first":cycle(&x1),"cycle_second":cycle(&x2),"cycle_difference":cycle(&x1)-cycle(&x2),
                    "det_x_first":det_x(&x1),"det_x_second":det_x(&x2)})); }
        }}
    }
    let h=1e-4; let p=std::array::from_fn(|i|fold[i]+h*right[i]); let m=std::array::from_fn(|i|fold[i]-h*right[i]);
    let f0=readout(&fold);let fp=readout(&p);let fm=readout(&m);
    let second:[f64;4]=std::array::from_fn(|i|(fp[i]-2.0*f0[i]+fm[i])/(h*h));
    let fold_scalar=left.iter().zip(second).map(|(u,v)|u*v).sum::<f64>();
    let base=readout(&fold);
    for scale in [1e-4,3e-4,1e-3,3e-3,1e-2] {
        let delta=0.5*fold_scalar*scale*scale;
        let target=std::array::from_fn(|i|base[i]+delta*left[i]);
        let sp=std::array::from_fn(|i|fold[i]+scale*right[i]);
        let sm=std::array::from_fn(|i|fold[i]-scale*right[i]);
        if let (Some(x1),Some(x2))=(newton(sp,target),newton(sm,target)) {
            let sep=x1.iter().zip(x2).map(|(u,v)|(u-v).powi(2)).sum::<f64>().sqrt();
            if sep>1e-7 {let residual=readout(&x1).iter().zip(readout(&x2)).map(|(u,v)|(u-v).abs()).fold(0.0,f64::max);
                out.push(json!({"construction":"left-null normal target","scale":scale,"first":x1,"second":x2,"edge_readout":readout(&x1),
                    "edge_residual_max":residual,"parameter_separation":sep,"cycle_first":cycle(&x1),"cycle_second":cycle(&x2),
                    "cycle_difference":cycle(&x1)-cycle(&x2),"det_x_first":det_x(&x1),"det_x_second":det_x(&x2)}));}
        }
    }
    // Freeze one sheet at terminating-decimal (hence rational) coordinates.
    // The target readout is then exactly rational in the source model; only
    // existence and isolation of the second root remain to be certified.
    let rational_first=[-0.6999667,-0.6999808,-0.6001426,0.5002516];
    let rational_target=readout(&rational_first);
    let other_seed=[-0.7000331,-0.7000191,-0.6010082,0.5020499];
    if let Some(second)=newton(other_seed,rational_target) {
        let residual=readout(&second).iter().zip(rational_target).map(|(u,v)|(u-v).abs()).fold(0.0,f64::max);
        out.push(json!({"construction":"rational first sheet","first":rational_first,"second":second,"edge_readout":rational_target,
            "edge_residual_max":residual,"parameter_separation":rational_first.iter().zip(second).map(|(u,v)|(u-v).powi(2)).sum::<f64>().sqrt(),
            "cycle_first":cycle(&rational_first),"cycle_second":cycle(&second),"cycle_difference":cycle(&rational_first)-cycle(&second),
            "det_x_first":det_x(&rational_first),"det_x_second":det_x(&second)}));
    }
    let packet=json!({"schema":"marici.four-mode-chord-deletion-fold-pair.v1","status":"numerical discovery; exact algebraic certification required","fold_diagnostic":{"right_null":right,"left_null":left,"projected_second_derivative":fold_scalar},"candidates":out});
    let dst="../checkers/results/four-mode-chord-deletion-fold-pair.json";
    fs::write(dst,serde_json::to_string_pretty(&packet).unwrap()+"\n").unwrap();
    println!("{}",serde_json::to_string_pretty(&packet).unwrap());
}
