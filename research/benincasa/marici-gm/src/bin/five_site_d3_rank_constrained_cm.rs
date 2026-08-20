use serde_json::json;
use std::fs;
use symbolica::prelude::*;

fn a(text: &str) -> Atom {
    Atom::parse(text, "marici", Default::default()).unwrap().expand()
}
fn det(m: &[Vec<Atom>]) -> Atom {
    if m.len() == 1 { return m[0][0].clone(); }
    let mut out=a("0");
    for j in 0..m.len() {
        let minor=m[1..].iter().map(|r|r.iter().enumerate()
            .filter(|(k,_)|*k!=j).map(|(_,x)|x.clone()).collect()).collect::<Vec<Vec<_>>>();
        let term=m[0][j].clone()*det(&minor);
        if j%2==0 {out+=term}else{out-=term}
    }
    out.expand()
}
fn adj(m:&[Vec<Atom>])->Vec<Vec<Atom>>{
    let n=m.len(); let mut out=vec![vec![a("0");n];n];
    for i in 0..n { for j in 0..n {
        let minor=m.iter().enumerate().filter(|(r,_)|*r!=j).map(|(_,row)|row.iter()
            .enumerate().filter(|(c,_)|*c!=i).map(|(_,x)|x.clone()).collect()).collect::<Vec<Vec<_>>>();
        let cof=det(&minor); out[i][j]=if(i+j)%2==0{cof}else{-cof};
    }} out
}
fn quad(m:&[Vec<Atom>],x:&[Atom],y:&[Atom])->Atom{
    let mut out=a("0");
    for i in 0..x.len(){for j in 0..y.len(){out+=x[i].clone()*m[i][j].clone()*y[j].clone();}}
    out.expand()
}
fn minor_delete(m:&[Vec<Atom>],row:usize,col:usize)->Atom{
    let sub=m.iter().enumerate().filter(|(i,_)|*i!=row).map(|(_,r)|r.iter().enumerate()
        .filter(|(j,_)|*j!=col).map(|(_,x)|x.clone()).collect()).collect::<Vec<Vec<_>>>();
    det(&sub)
}

fn main(){
    let h=vec![
        vec![a("h11"),a("h12"),a("h13")],
        vec![a("h12"),a("h22"),a("h23")],
        vec![a("h13"),a("h23"),a("h33")],
    ];
    let c=vec![a("c1"),a("c2"),a("c3")];
    let u=vec![a("u1"),a("u2"),a("u3")];
    let dh=det(&h); let ah=adj(&h);
    let hc=(0..3).map(|i|(0..3).fold(a("0"),|s,j|s+h[i][j].clone()*c[j].clone()).expand()).collect::<Vec<_>>();
    let cthc=(0..3).fold(a("0"),|s,i|s+c[i].clone()*hc[i].clone()).expand();
    let ctu=(0..3).fold(a("0"),|s,i|s+c[i].clone()*u[i].clone()).expand();
    let l=a("L"); let ysq=a("Ysq");
    let mut g=vec![vec![a("0");4];4];
    for i in 0..3{for j in 0..3{g[i][j]=h[i][j].clone();}g[i][3]=hc[i].clone();g[3][i]=hc[i].clone();}
    g[3][3]=cthc;
    let mut b=vec![vec![a("0");5];5]; b[0][0]=ysq.clone();
    for i in 0..3{b[0][i+1]=u[i].clone();b[i+1][0]=u[i].clone();}
    b[0][4]=(ctu+l.clone()).expand();b[4][0]=b[0][4].clone();
    for i in 0..4{for j in 0..4{b[i+1][j+1]=g[i][j].clone();}}
    let q=(dh.clone()*ysq.clone()-quad(&ah,&u,&u)).expand();
    let y_on_q=(quad(&ah,&u,&u)/dh.clone()).together().cancel();
    let mut checked=0;
    for i in 0..5{for j in 0..5{
        let reduced=minor_delete(&b,i,j).replace(l.clone().to_pattern()).with(a("0").to_pattern())
            .replace(ysq.clone().to_pattern()).with(y_on_q.clone().to_pattern()).together().cancel().expand();
        assert_eq!(reduced,a("0")); checked+=1;
    }}
    let packet=json!({
        "schema":"marici.benincasa.five_site.d3_rank_constrained_cm.v1",
        "pivot":"labelled nonsingular external 3x3 Gram minor H",
        "external_fourth_vector":"q4=sum_i c_i q_i",
        "linear_constraint":"L=v4-c^T*u=0",
        "quadratic_constraint":"Q=det(H)*Y1^2-u^T*adj(H)*u=0",
        "regularity_jacobian":"det d(L,Q)/d(v4,Y1^2)=det(H), a unit on the pivot chart",
        "codimension":2,
        "five_edge_variables":5,
        "independent_physical_variables":3,
        "four_by_four_gram_minors_checked":checked,
        "all_minors_vanish_on_L_Q":true,
        "pivot_change":"changes generators by an invertible matrix on overlaps; the rank<=3 determinantal ideal is intrinsic",
        "classification":"existing external-Gram determinantal support, not a new carrier stratum",
        "physical_measure_current":"not yet computed; requires the coarea/Jacobian induced on the complete intersection",
        "new_carrier_datum":false
    });
    assert_eq!(q.replace(ysq.to_pattern()).with(y_on_q.to_pattern()).together().cancel().expand(),a("0"));
    fs::write("../results/five-site-d3-rank-constrained-cm.json",serde_json::to_string_pretty(&packet).unwrap()+"\n").unwrap();
    println!("{}",serde_json::to_string(&packet).unwrap());
}
