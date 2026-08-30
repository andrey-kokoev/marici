use serde_json::json;
use std::f64::consts::PI;

const EXPS: [(usize, usize, usize); 20] = [
    (0,0,0),(1,0,0),(0,1,0),(0,0,1),(2,0,0),(1,1,0),(1,0,1),(0,2,0),(0,1,1),(0,0,2),
    (3,0,0),(2,1,0),(2,0,1),(1,2,0),(1,1,1),(1,0,2),(0,3,0),(0,2,1),(0,1,2),(0,0,3),
];
// Source order: L1,L2,L3,D1,D2,D3,C12,C13,C23,U.
const TARGET: [usize; 10] = [1,2,3,4,7,9,5,6,8,14];

#[derive(Clone, Copy)]
struct Jet([f64; 20]);

impl Jet {
    fn scalar(x: f64) -> Self { let mut a=[0.0;20]; a[0]=x; Self(a) }
    fn var(i: usize) -> Self { let mut a=[0.0;20]; a[1+i]=1.0; Self(a) }
    fn add(self, rhs: Self) -> Self { let mut a=[0.0;20]; for i in 0..20 {a[i]=self.0[i]+rhs.0[i];} Self(a) }
    fn sub(self, rhs: Self) -> Self { let mut a=[0.0;20]; for i in 0..20 {a[i]=self.0[i]-rhs.0[i];} Self(a) }
    fn scale(self, c:f64) -> Self { let mut a=[0.0;20]; for i in 0..20 {a[i]=self.0[i]*c;} Self(a) }
    fn mul(self, rhs: Self) -> Self {
        let mut a=[0.0;20];
        for i in 0..20 { for j in 0..20 {
            let e=(EXPS[i].0+EXPS[j].0,EXPS[i].1+EXPS[j].1,EXPS[i].2+EXPS[j].2);
            if e.0+e.1+e.2<=3 { if let Some(k)=EXPS.iter().position(|x|*x==e) {a[k]+=self.0[i]*rhs.0[j];} }
        }}
        Self(a)
    }
    fn inv(self) -> Self {
        let c=self.0[0]; let u=self.sub(Self::scalar(c)).scale(1.0/c);
        Self::scalar(1.0).sub(u).add(u.mul(u)).sub(u.mul(u).mul(u)).scale(1.0/c)
    }
    fn sqrt(self) -> Self {
        let c=self.0[0]; let u=self.sub(Self::scalar(c)).scale(1.0/c);
        Self::scalar(1.0).add(u.scale(0.5)).sub(u.mul(u).scale(0.125)).add(u.mul(u).mul(u).scale(0.0625)).scale(c.sqrt())
    }
}

fn gl_nodes(n:usize, lo:f64, hi:f64)->Vec<(f64,f64)> {
    let mut out=Vec::with_capacity(n);
    for i in 0..n {
        let mut z=(PI*((i as f64)+0.75)/((n as f64)+0.5)).cos();
        loop {
            let (mut p0,mut p1)=(1.0,z);
            for k in 2..=n { let p=((2*k-1) as f64*z*p1-((k-1) as f64)*p0)/(k as f64); p0=p1;p1=p; }
            let dp=(n as f64)*(z*p1-p0)/(z*z-1.0);
            let nz=z-p1/dp;
            if (nz-z).abs()<2e-15 {z=nz;break;} z=nz;
        }
        let (mut p0,mut p1)=(1.0,z);
        for k in 2..=n {let p=((2*k-1) as f64*z*p1-((k-1) as f64)*p0)/(k as f64);p0=p1;p1=p;}
        let dp=(n as f64)*(z*p1-p0)/(z*z-1.0);
        let w=2.0/((1.0-z*z)*dp*dp);
        out.push((((hi-lo)*z+hi+lo)/2.0,w*(hi-lo)/2.0));
    }
    out.sort_by(|a,b|a.0.partial_cmp(&b.0).unwrap()); out
}

fn density(l:[f64;3], x:[f64;3])->Jet {
    let nu=[Jet::var(0),Jet::var(1),Jet::var(2)];
    let ps=[Jet::scalar(x[0]*x[0]).add(nu[0]),Jet::scalar(x[1]*x[1]).add(nu[1]),Jet::scalar(x[2]*x[2]).add(nu[2])];
    let p2=ps[1].sqrt();
    let x4=ps[0].add(ps[1]).sub(ps[2]).mul(p2.scale(2.0).inv());
    let y4=ps[0].sub(x4.mul(x4)).sqrt();
    let c=(l[0]*l[0]+l[1]*l[1]+l[2]*l[2]).sqrt();
    let a=Jet::scalar(l[0]).sub(p2).mul(Jet::scalar(l[0]).sub(p2)).add(Jet::scalar(l[1]*l[1]+l[2]*l[2])).sqrt();
    let b=Jet::scalar(l[0]).sub(x4).mul(Jet::scalar(l[0]).sub(x4)).add(Jet::scalar(l[1]).sub(y4).mul(Jet::scalar(l[1]).sub(y4))).add(Jet::scalar(l[2]*l[2])).sqrt();
    let walls=[Jet::scalar(c+x[0]).add(b),Jet::scalar(c+x[1]).add(a),a.add(b).add(Jet::scalar(x[2])),Jet::scalar(c+x[1]+x[2]).add(b)];
    walls.iter().fold(Jet::scalar(1.0),|q,w|q.mul(w.inv()))
}

fn integrate(x:[f64;3], n:usize)->[f64;11] {
    let ts=gl_nodes(n,0.0,1.0); let mus=gl_nodes(n,-1.0,1.0); let phis=gl_nodes(n,0.0,2.0*PI);
    let x4=(x[0]*x[0]+x[1]*x[1]-x[2]*x[2])/(2.0*x[1]);
    let y4=(x[0]*x[0]-x4*x4).sqrt();
    let centers=[[0.0,0.0,0.0],[x[1],0.0,0.0],[x4,y4,0.0]];
    let mut sum=[0.0;20];
    for chart in 0..3 { for &(t,wt) in &ts { let r=t/(1.0-t); let radial=r*r/((1.0-t)*(1.0-t));
        for &(mu,wm) in &mus {let st=(1.0-mu*mu).sqrt();
          for &(phi,wp) in &phis {
            let l=[centers[chart][0]+r*st*phi.cos(),centers[chart][1]+r*st*phi.sin(),centers[chart][2]+r*mu];
            let mut inv4=[0.0;3];for q in 0..3{let d2=(l[0]-centers[q][0]).powi(2)+(l[1]-centers[q][1]).powi(2)+(l[2]-centers[q][2]).powi(2);inv4[q]=1.0/(d2*d2);}
            let partition=inv4[chart]/(inv4[0]+inv4[1]+inv4[2]);
            let j=density(l,x);let w=wt*wm*wp*radial*partition;for k in 0..20{sum[k]+=w*j.0[k];}
          }
        }
    }}
    let mut out=[0.0;11];out[0]=sum[0];for (q,&k) in TARGET.iter().enumerate(){out[q+1]=sum[k]/sum[0];}out
}

fn rank(mut a:Vec<Vec<f64>>,tol:f64)->(usize,f64) {
    for c in 0..a[0].len(){let s=a.iter().fold(0.0_f64,|m,row|m.max(row[c].abs()));if s>0.0{for row in &mut a{row[c]/=s;}}}
    let scale=1.0;let mut r=0;let mut minp=f64::INFINITY;
    for c in 0..a[0].len(){let mut p=r;for i in r..a.len(){if a[i][c].abs()>a[p][c].abs(){p=i;}}if a[p][c].abs()<=tol*scale{continue;}a.swap(r,p);let pv=a[r][c];minp=minp.min(pv.abs()/scale);for i in r+1..a.len(){let f=a[i][c]/pv;for j in c..a[0].len(){a[i][j]-=f*a[r][j];}}r+=1;if r==a.len(){break;}}
    (r,minp)
}

fn main(){
    let contexts=[[3.,4.,5.],[4.,5.,6.],[4.,6.,7.],[5.,7.,8.],[5.,8.,9.],[6.,7.,10.],[6.,9.,11.],[7.,8.,12.],[7.,10.,13.],[8.,11.,14.]];
    let orders=[28usize,36,48];let mut runs=Vec::new();let mut previous:Option<Vec<[f64;11]>>=None;
    for n in orders {let rows:Vec<[f64;11]>=contexts.iter().map(|&x|integrate(x,n)).collect();let matrix:Vec<Vec<f64>>=rows.iter().map(|r|r[1..].to_vec()).collect();let (rk,minp)=rank(matrix,1e-8);
      let quotient:Vec<Vec<f64>>=rows.iter().map(|r|(1..=7).map(|j|r[j]).collect()).collect();let(qrk,qminp)=rank(quotient,1e-8);
      let mut relation_residuals=Vec::new();
      for (row,x) in rows.iter().zip(contexts.iter()) {let f=&row[1..];let(p1,p2,p3)=(x[0]*x[0],x[1]*x[1],x[2]*x[2]);
        let relations=[
          [0.,0.,0.,p3-p2,-p2,p3,-p2,p3,0.,0.],
          [0.,0.,0.,-p1,p3-p1,p3,-p1,0.,p3,0.],
          [0.,0.,0.,-1.,-1.,0.,-1.,0.,0.,p3],
        ];
        let mut rr=[0.0;3];for q in 0..3{let num=(0..10).map(|j|f[j]*relations[q][j]).sum::<f64>().abs();let den=(0..10).map(|j|(f[j]*relations[q][j]).abs()).sum::<f64>().max(1e-300);rr[q]=num/den;}relation_residuals.push(rr);
      }
      let mut max_relation_residual=[0.0_f64;3];for rr in &relation_residuals{for q in 0..3{max_relation_residual[q]=max_relation_residual[q].max(rr[q]);}}
      let delta=previous.as_ref().map(|old|{let mut d=[0.0_f64;11];for i in 0..rows.len(){for j in 0..11{d[j]=d[j].max((rows[i][j]-old[i][j]).abs());}}d});
      runs.push(json!({"order":n,"column_normalized_rank":rk,"minimum_scaled_pivot":minp,"quotient_frame_rank":qrk,"quotient_minimum_scaled_pivot":qminp,"maximum_relative_source_relation_residuals":max_relation_residual,"max_absolute_change_from_previous":delta}));previous=Some(rows);
    }
    println!("{}",serde_json::to_string_pretty(&json!({"schema":"marici.benincasa.integrated-period-normal-jet.v1","contexts":contexts,"runs":runs})).unwrap());
}
