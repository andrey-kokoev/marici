use symbolica::prelude::*;

fn a(s:&str)->Atom { Atom::parse(s,"marici",Default::default()).unwrap().expand() }

fn determinant(m:&[Vec<Atom>])->Atom {
    fn rec(m:&[Vec<Atom>], row:usize, used:&mut [bool], perm:&mut Vec<usize>, out:&mut Atom) {
        let n=m.len();
        if row==n {
            let inv=(0..n).flat_map(|i|(i+1..n).map(move|j|(i,j))).filter(|(i,j)|perm[*i]>perm[*j]).count();
            let mut term=a(if inv%2==0{"1"}else{"-1"});
            for i in 0..n { term=(term.clone()*m[i][perm[i]].clone()).expand(); }
            *out=(out.clone()+term).expand();
            return;
        }
        for col in 0..n { if !used[col] { used[col]=true;perm.push(col);rec(m,row+1,used,perm,out);perm.pop();used[col]=false; } }
    }
    let mut out=a("0");rec(m,0,&mut vec![false;m.len()],&mut Vec::new(),&mut out);out.expand()
}

fn resultant_cubics(f:&[Atom;4],g:&[Atom;4])->Atom {
    let z=a("0");
    determinant(&vec![
        vec![f[3].clone(),f[2].clone(),f[1].clone(),f[0].clone(),z.clone(),z.clone()],
        vec![z.clone(),f[3].clone(),f[2].clone(),f[1].clone(),f[0].clone(),z.clone()],
        vec![z.clone(),z.clone(),f[3].clone(),f[2].clone(),f[1].clone(),f[0].clone()],
        vec![g[3].clone(),g[2].clone(),g[1].clone(),g[0].clone(),z.clone(),z.clone()],
        vec![z.clone(),g[3].clone(),g[2].clone(),g[1].clone(),g[0].clone(),z.clone()],
        vec![z.clone(),z,g[3].clone(),g[2].clone(),g[1].clone(),g[0].clone()],
    ])
}

fn eliminate(m:i32,dei:&str,dej:&str,dij:&str)->(Atom,Atom) {
    let c=a(&format!("(25/2+{})*x-{}-{}",m*m,dei,dej));
    let r=a(&format!("{}+({}-(25/2+{}))*x",dei, m*m, m*m));
    let delta=a(&format!("({})-({})",dei,dej));
    let f=[
        a(&format!("-25*{}*x^2*({}*x-({}))",m*m,m*m,dij)),
        (a("4")*c.clone()*c.clone()).expand(),
        (a("-16")*c).expand(),
        a("16"),
    ];
    let g=[
        (a(&format!("{}*x",m*m))*(delta.clone()*delta-r.clone()*r.clone())).expand(),
        (a("-4")*a(&format!("{}*x",m*m))*r.clone()+a("4")*r.clone()*r.clone()).expand(),
        (a(&format!("-4*{}*x",m*m))+a("16")*r).expand(),
        a("16"),
    ];
    let raw=resultant_cubics(&f,&g).factor();
    let known=a("x");
    let saturated=(raw.clone()/known).together().cancel().factor();
    (raw,saturated)
}

fn main(){
    let n1="2";
    let n2="(11+sqrt(5))/2";
    let n3="(21+sqrt(5))/2";
    let n4="17";
    let cases=[
        ("G_minus_e12|g_3",1,n1,n2,n1),
        ("G_minus_e12|g_4",1,n2,n3,n1),
        ("G_minus_e12|g_5",1,n3,n4,n1),
        ("G_minus_e12|g_34",2,n1,n3,n2),
        ("G_minus_e12|g_45",2,n2,n4,n2),
        ("G_minus_e12|g_345",3,n1,n4,n3),
    ];
    println!("{{\"schema\":\"marici.five_site_disjoint_mixed_pair_landau.v1\",\"cases\":[");
    for (i,(label,m,dei,dej,dij)) in cases.iter().enumerate(){
        if i>0{println!(",");}
        let (result,saturated)=eliminate(*m,dei,dej,dij);
        print!("{{\"label\":\"{}\",\"m\":{},\"d_ei_sq\":\"{}\",\"d_ej_sq\":\"{}\",\"d_ij_sq\":\"{}\",\"removed_universal_factor\":\"x\",\"resultant_in_x\":\"{}\",\"saturated_resultant\":\"{}\"}}",label,m,dei,dej,dij,result,saturated);
    }
    println!("]}}");
}
