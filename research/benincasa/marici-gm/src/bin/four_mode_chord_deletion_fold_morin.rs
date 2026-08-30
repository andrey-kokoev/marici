use serde_json::json;
use std::fs;
use symbolica::prelude::*;

fn a(s:&str)->Atom { Atom::parse(s,"marici",Default::default()).unwrap().expand() }
fn det(m:&[Vec<Atom>])->Atom {
    if m.len()==1{return m[0][0].clone()}
    (0..m.len()).fold(a("0"),|sum,c|{
        let q=m[1..].iter().map(|row|row.iter().enumerate().filter(|(j,_)|*j!=c).map(|(_,x)|x.clone()).collect()).collect::<Vec<Vec<_>>>();
        if c%2==0{sum+m[0][c].clone()*det(&q)}else{sum-m[0][c].clone()*det(&q)}
    }).expand()
}
fn cross3(rows:&[Vec<Atom>])->Vec<Atom>{
    (0..4).map(|omit|{
        let m=rows.iter().map(|row|row.iter().enumerate().filter(|(j,_)|*j!=omit).map(|(_,x)|x.clone()).collect()).collect::<Vec<Vec<_>>>();
        if omit%2==0{det(&m)}else{-det(&m)}
    }).collect()
}

fn main(){
    let vars=["a","b","c","d"].iter().map(|s|Symbol::parse(*s,"marici").unwrap()).collect::<Vec<_>>();
    let d=a("1-a^2-b^2-c^2-d^2+a^2*c^2+b^2*d^2-2*a*b*c*d");
    let ns=["-a^2+a^2*c^2-a*b*c*d","-b^2+b^2*d^2-a*b*c*d","-c^2+a^2*c^2-a*b*c*d","-d^2+b^2*d^2-a*b*c*d"].iter().map(|s|a(s)).collect::<Vec<_>>();
    let j=ns.iter().map(|n|vars.iter().map(|v|(n.derivative(*v)*d.clone()-n.clone()*d.derivative(*v)).expand()).collect()).collect::<Vec<Vec<_>>>();
    let jd=det(&j).factor();
    let r=(jd/(a("8")*d.clone().pow(3))).together().factor();
    let charts=(0..4).map(|omit|{
        let rows=j.iter().enumerate().filter(|(q,_)|*q!=omit).map(|(_,row)|row.clone()).collect::<Vec<_>>();
        let kernel=cross3(&rows);
        let normal=(0..4).fold(a("0"),|s,i|s+kernel[i].clone()*r.derivative(vars[i])).expand();
        (omit,kernel,normal)
    }).collect::<Vec<_>>();
    let rp=r.to_polynomial::<_,u16>(&Q,vars.clone());
    let gcds=charts.iter().map(|(_,_,normal)|rp.gcd(&normal.to_polynomial::<_,u16>(&Q,vars.clone())).to_expression().factor()).collect::<Vec<_>>();
    let packet=json!({"schema":"marici.four-mode-chord-deletion-fold-morin.v3","criterion":"four-chart kernel derivatives of the Jacobian determinant","rankdrop":r.to_string(),"charts":charts.iter().zip(gcds.iter()).map(|((omit,kernel,normal),gcd)|json!({"omitted_row":omit,"kernel":kernel.iter().map(|x|x.factor().to_string()).collect::<Vec<_>>(),"kernel_normal_derivative":normal.to_string(),"gcd_rankdrop_normal_derivative":gcd.to_string()})).collect::<Vec<_>>(),"conclusion":if gcds.iter().all(|g|*g==a("1")){"every adjugate chart is generically ordinary-fold; exceptional points require joint chart-compatible analysis"}else{"a divisorial Morin degeneration remains in at least one chart"}});
    fs::write("../results/four-mode-chord-deletion-fold-morin.json",serde_json::to_string_pretty(&packet).unwrap()+"\n").unwrap();
    println!("{}",serde_json::to_string_pretty(&json!({"gcds":gcds.iter().map(ToString::to_string).collect::<Vec<_>>(),"normal_bytes":charts.iter().map(|x|x.2.to_string().len()).collect::<Vec<_>>()})).unwrap());
}
