#[derive(Clone, Copy, Debug, Default)]
struct C { re: f64, im: f64 }

impl C {
    fn new(re: f64, im: f64) -> Self { Self { re, im } }
    fn conj(self) -> Self { Self::new(self.re, -self.im) }
}

fn mul(a: C, b: C) -> C {
    C::new(a.re*b.re-a.im*b.im, a.re*b.im+a.im*b.re)
}

fn kron(a: [C;2], b: [C;2]) -> [C;4] {
    [mul(a[0],b[0]), mul(a[0],b[1]), mul(a[1],b[0]), mul(a[1],b[1])]
}

fn state(s: &str) -> [C;2] {
    let q=1.0_f64/2.0_f64.sqrt();
    match s {
        "H" => [C::new(1.0,0.0),C::new(0.0,0.0)],
        "V" => [C::new(0.0,0.0),C::new(1.0,0.0)],
        "D" => [C::new(q,0.0),C::new(q,0.0)],
        "R" => [C::new(q,0.0),C::new(0.0,-q)],
        "L" => [C::new(q,0.0),C::new(0.0,q)],
        _ => panic!("bad state"),
    }
}

fn row(psi: [C;4]) -> [f64;16] {
    let mut r=[0.0;16];
    for i in 0..4 { r[i]=psi[i].re*psi[i].re+psi[i].im*psi[i].im; }
    let mut k=4;
    for i in 0..4 { for j in i+1..4 {
        let z=mul(psi[i].conj(),psi[j]);
        r[k]=2.0*z.re;
        r[k+1]=-2.0*z.im;
        k+=2;
    }}
    r
}

fn solve(mut a: [[f64;17];16]) -> [f64;16] {
    for c in 0..16 {
        let mut p=c;
        for i in c+1..16 { if a[i][c].abs()>a[p][c].abs() { p=i; } }
        assert!(a[p][c].abs()>1e-12);
        a.swap(c,p);
        let d=a[c][c]; for j in c..17 { a[c][j]/=d; }
        for i in 0..16 { if i!=c { let f=a[i][c]; for j in c..17 { a[i][j]-=f*a[c][j]; } } }
    }
    let mut x=[0.0;16]; for i in 0..16 { x[i]=a[i][16]; } x
}

fn rho_from(x: [f64;16]) -> [[C;4];4] {
    let mut r=[[C::default();4];4];
    for i in 0..4 { r[i][i]=C::new(x[i],0.0); }
    let mut k=4;
    for i in 0..4 { for j in i+1..4 {
        r[i][j]=C::new(x[k],x[k+1]); r[j][i]=r[i][j].conj(); k+=2;
    }} r
}

fn partial_transpose(r: [[C;4];4]) -> [[C;4];4] {
    let mut t=[[C::default();4];4];
    for a in 0..2 { for b in 0..2 { for c in 0..2 { for d in 0..2 {
        t[2*a+b][2*c+d]=r[2*a+d][2*c+b];
    }}}} t
}

fn published_ml_rho() -> [[C;4];4] {
    let mut r=[[C::default();4];4];
    r[0]=[C::new(0.5069,0.0),C::new(-0.0239,0.0106),C::new(-0.0412,-0.0221),C::new(0.4833,0.0329)];
    r[1]=[C::new(-0.0239,-0.0106),C::new(0.0048,0.0),C::new(0.0023,0.0019),C::new(-0.0296,-0.0077)];
    r[2]=[C::new(-0.0412,0.0221),C::new(0.0023,-0.0019),C::new(0.0045,0.0),C::new(-0.0425,0.0192)];
    r[3]=[C::new(0.4833,-0.0329),C::new(-0.0296,0.0077),C::new(-0.0425,-0.0192),C::new(0.4839,0.0)];
    r
}

fn real_embed(h: [[C;4];4]) -> [[f64;8];8] {
    let mut a=[[0.0;8];8];
    for i in 0..4 { for j in 0..4 {
        a[i][j]=h[i][j].re; a[i][j+4]=-h[i][j].im;
        a[i+4][j]=h[i][j].im; a[i+4][j+4]=h[i][j].re;
    }} a
}

fn jacobi(mut a: [[f64;8];8]) -> [f64;8] {
    for _ in 0..200 {
        let (mut p,mut q,mut best)=(0,1,a[0][1].abs());
        for i in 0..8 { for j in i+1..8 { if a[i][j].abs()>best { p=i;q=j;best=a[i][j].abs(); } } }
        if best<1e-13 { break; }
        let phi=0.5*(2.0*a[p][q]).atan2(a[q][q]-a[p][p]); let (s,c)=phi.sin_cos();
        for k in 0..8 { if k!=p && k!=q {
            let x=a[k][p]; let y=a[k][q]; a[k][p]=c*x-s*y; a[p][k]=a[k][p]; a[k][q]=s*x+c*y; a[q][k]=a[k][q];
        }}
        let app=a[p][p]; let aqq=a[q][q]; let apq=a[p][q];
        a[p][p]=c*c*app-2.0*s*c*apq+s*s*aqq;
        a[q][q]=s*s*app+2.0*s*c*apq+c*c*aqq; a[p][q]=0.0;a[q][p]=0.0;
    }
    let mut e=[0.0;8]; for i in 0..8 { e[i]=a[i][i]; } e.sort_by(|x,y|x.partial_cmp(y).unwrap()); e
}

fn main() {
    let data=[
        ("H","H",34749.0),("H","V",324.0),("V","H",444.0),("V","V",35805.0),
        ("H","D",17238.0),("H","L",16722.0),("D","H",16901.0),("R","H",16324.0),
        ("D","D",32028.0),("R","D",15132.0),("R","L",33586.0),("D","R",17932.0),
        ("D","V",13441.0),("R","V",17521.0),("V","D",13171.0),("V","L",17170.0),
    ];
    let norm=data[0].2+data[1].2+data[2].2+data[3].2;
    let mut a=[[0.0;17];16];
    for (i,(s,t,n)) in data.iter().enumerate() {
        let rr=row(kron(state(s),state(t))); for j in 0..16 { a[i][j]=rr[j]; } a[i][16]=n/norm;
    }
    let rho=rho_from(solve(a));
    let xx=2.0*(rho[0][3].re+rho[1][2].re);
    let yy=2.0*(rho[1][2].re-rho[0][3].re);
    let zz=rho[0][0].re-rho[1][1].re-rho[2][2].re+rho[3][3].re;
    let witness=(1.0-xx+yy-zz)/4.0;
    let rho_eval=jacobi(real_embed(rho));
    let eval=jacobi(real_embed(partial_transpose(rho)));
    println!("normalization={norm:.0}");
    println!("rho_eigenvalues_doubled={rho_eval:?}");
    println!("xx={xx:.12} yy={yy:.12} zz={zz:.12} witness={witness:.12}");
    println!("pt_eigenvalues_doubled={eval:?}");
    println!("minimum_pt_eigenvalue={:.12}",eval[0]);
    let ml=published_ml_rho();
    let ml_eval=jacobi(real_embed(ml));
    let ml_pt=jacobi(real_embed(partial_transpose(ml)));
    let ml_xx=2.0*(ml[0][3].re+ml[1][2].re);
    let ml_yy=2.0*(ml[1][2].re-ml[0][3].re);
    let ml_zz=ml[0][0].re-ml[1][1].re-ml[2][2].re+ml[3][3].re;
    let ml_w=(1.0-ml_xx+ml_yy-ml_zz)/4.0;
    println!("ml_rho_eigenvalues_doubled={ml_eval:?}");
    println!("ml_xx={ml_xx:.12} ml_yy={ml_yy:.12} ml_zz={ml_zz:.12} ml_witness={ml_w:.12}");
    println!("ml_pt_eigenvalues_doubled={ml_pt:?}");
    assert!(eval[0] < -0.1);
    assert!(ml_eval[0] > -1e-3);
    assert!(ml_pt[0] < -0.4);
}
