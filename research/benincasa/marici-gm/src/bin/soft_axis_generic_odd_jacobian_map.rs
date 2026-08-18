use std::collections::{BTreeMap, HashMap};

const P: i64 = 2_305_843_009_213_693_951;
type Mon = (u8, usize, usize);
type Poly = BTreeMap<Mon, i64>;

fn add_mod(x: i64, y: i64) -> i64 {
    ((x as i128 + y as i128).rem_euclid(P as i128)) as i64
}
fn mul_mod(x: i64, y: i64) -> i64 {
    ((x as i128 * y as i128).rem_euclid(P as i128)) as i64
}
fn pow_mod(mut x: i64, mut n: i64) -> i64 {
    let mut out = 1;
    while n > 0 {
        if n & 1 == 1 { out = mul_mod(out, x); }
        x = mul_mod(x, x);
        n >>= 1;
    }
    out
}
fn inv(x: i64) -> i64 { pow_mod(x, P - 2) }
fn scale(p: &Poly, c: i64) -> Poly {
    p.iter().filter_map(|(&m, &x)| {
        let y = mul_mod(x, c);
        (y != 0).then_some((m, y))
    }).collect()
}
fn add(ps: &[Poly]) -> Poly {
    let mut out = Poly::new();
    for p in ps {
        for (&m, &x) in p {
            let y = add_mod(*out.get(&m).unwrap_or(&0), x);
            if y == 0 { out.remove(&m); } else { out.insert(m, y); }
        }
    }
    out
}
fn mul(x: &Poly, y: &Poly) -> Poly {
    let mut out = Poly::new();
    for (&(u1,a1,b1), &c1) in x {
        for (&(u2,a2,b2), &c2) in y {
            if u1 + u2 >= 2 { continue; }
            let m = (u1 + u2, a1 + a2, b1 + b2);
            let c = add_mod(*out.get(&m).unwrap_or(&0), mul_mod(c1,c2));
            if c == 0 { out.remove(&m); } else { out.insert(m,c); }
        }
    }
    out
}
fn power(x: &Poly, n: usize) -> Poly {
    let mut out = mon(0,0,0,1);
    for _ in 0..n { out = mul(&out,x); }
    out
}
fn deriv(x: &Poly, coordinate: usize) -> Poly {
    let mut out = Poly::new();
    for (&(u,a,b), &c) in x {
        let degrees = [u as usize,a,b];
        if degrees[coordinate] == 0 { continue; }
        let mut target = [u as usize,a,b];
        target[coordinate] -= 1;
        out.insert((target[0] as u8,target[1],target[2]),mul_mod(c,degrees[coordinate] as i64));
    }
    out
}
fn mon(u:u8,a:usize,b:usize,c:i64)->Poly {
    BTreeMap::from([((u,a,b),c.rem_euclid(P))])
}
fn exact(sector:(usize,usize), f:&Poly, is_q:bool, plus:bool)->Poly {
    let one=mon(0,0,0,1); let u=mon(1,0,0,1); let a=mon(0,1,0,1); let b=mon(0,0,1,1);
    let l1=add(&[b.clone(),one,scale(&u,P-1)]);
    let l2=add(&[a,scale(&u,if plus { inv(2) } else { P-inv(2) })]);
    let k=add(&[mon(0,4,0,1),mon(1,2,0,1),mon(1,2,2,P-1)]);
    let (sa,sb)=sector; let (ea,eb)=(2-sa,2-sb);
    let base=mul(&power(&l1,ea),&power(&l2,eb));
    if !is_q {
        let mut terms=vec![scale(&mul(&mul(&deriv(f,2),&base),&k),P-1)];
        if sa>0 { terms.push(scale(&mul(&mul(f,&power(&l1,ea-1)),&mul(&power(&l2,eb),&k)),sa as i64)); }
        terms.push(scale(&mul(&mul(f,&base),&deriv(&k,2)),mul_mod(3,inv(2))));
        add(&terms)
    } else {
        let mut terms=vec![mul(&mul(&deriv(f,1),&base),&k)];
        if sb>0 { terms.push(scale(&mul(&mul(f,&power(&l1,ea)),&mul(&power(&l2,eb-1),&k)),P-sb as i64)); }
        terms.push(scale(&mul(&mul(f,&base),&deriv(&k,1)),P-mul_mod(3,inv(2))));
        add(&terms)
    }
}
fn evaluate(p:&Poly,bv:i64)->HashMap<(u8,usize),i64> {
    let mut out=HashMap::new();
    for (&(u,a,b),&c) in p {
        let y=mul_mod(c,pow_mod(bv.rem_euclid(P),b as i64));
        let z=add_mod(*out.get(&(u,a)).unwrap_or(&0),y);
        if z==0 {out.remove(&(u,a));} else {out.insert((u,a),z);}
    }
    out
}
fn rank(mut cols:Vec<Vec<i64>>)->usize {
    let rows=cols.first().map_or(0,|c|c.len());
    let mut r=0;
    for i in 0..rows {
        let Some(j)=(r..cols.len()).find(|&j|cols[j][i]!=0) else {continue};
        cols.swap(r,j); let z=inv(cols[r][i]);
        for x in &mut cols[r] {*x=mul_mod(*x,z);}
        for j in 0..cols.len() {
            if j==r || cols[j][i]==0 {continue;}
            let z=cols[j][i];
            for k in i..rows {cols[j][k]=add_mod(cols[j][k],P-mul_mod(z,cols[r][k]));}
        }
        r+=1;
    }
    r
}
fn audit(d:usize,bv:i64) {
    let rows:Vec<_>=(0..=1).flat_map(|u|(1..=d).step_by(2).map(move|a|(u,a))).collect();
    let pos:HashMap<_,_>=rows.iter().enumerate().map(|(i,&m)|(m,i)).collect();
    let mut columns=Vec::new();
    for sector in [(1,1),(1,0),(0,1),(0,0)] {
        for total in 0..=d {
            for ad in 0..=total {
                let f=mon(0,ad,total-ad,1);
                for plus in [false,true] { for is_q in [false,true] {
                    let e=evaluate(&exact(sector,&f,is_q,plus),bv);
                    if e.keys().map(|m|m.1).max().unwrap_or(0)>d {continue;}
                    let mut c=vec![0;rows.len()];
                    let mut uc=vec![0;rows.len()];
                    for (m,x) in e {
                        if let Some(&i)=pos.get(&m) {c[i]=x;}
                        if m.0==0 {if let Some(&i)=pos.get(&(1,m.1)){uc[i]=x;}}
                    }
                    if c.iter().any(|&x|x!=0){columns.push(c);}
                    if uc.iter().any(|&x|x!=0){columns.push(uc);}
                }}
            }
        }
    }
    let image_rank=rank(columns.clone());
    let c=(1-mul_mod(bv,bv)).rem_euclid(P);
    let mut carrier_columns=vec![vec![0;2];rows.len()];
    for (i,&(u,a)) in rows.iter().enumerate() {
        match (u,a) {
            (0,1)=>carrier_columns[i][0]=1,
            (1,1)=>carrier_columns[i][1]=1,
            (0,3)=>carrier_columns[i][1]=P-mul_mod(c,inv(2)),
            _=>{}
        }
    }
    for col in &columns {
        let mut y=[0,0];
        for (i,&x) in col.iter().enumerate(){for k in 0..2{y[k]=add_mod(y[k],mul_mod(x,carrier_columns[i][k]));}}
        assert_eq!(y,[0,0],"exact image must die in the Jacobian quotient");
    }
    let carrier_rank=rank(carrier_columns);
    let cokernel_dim=rows.len()-image_rank;
    let relative_kernel_dim=rows.len()-carrier_rank-image_rank;
    assert_eq!((cokernel_dim,carrier_rank,relative_kernel_dim),(3,2,1));
    println!("b={bv},D={d}: cokernel={cokernel_dim}, carrier_image={carrier_rank}, relative_kernel={relative_kernel_dim}");
}
fn audit_even(d:usize,bv:i64) {
    let rows:Vec<_>=(0..=1).flat_map(|u|(0..=d).step_by(2).map(move|a|(u,a))).collect();
    let pos:HashMap<_,_>=rows.iter().enumerate().map(|(i,&m)|(m,i)).collect();
    let mut columns=Vec::new();
    for sector in [(1,1),(1,0),(0,1),(0,0)] {
        for total in 0..=d {
            for ad in 0..=total {
                let f=mon(0,ad,total-ad,1);
                for plus in [false,true] { for is_q in [false,true] {
                    let e=evaluate(&exact(sector,&f,is_q,plus),bv);
                    if e.keys().map(|m|m.1).max().unwrap_or(0)>d {continue;}
                    let mut c=vec![0;rows.len()];
                    let mut uc=vec![0;rows.len()];
                    for (m,x) in e {
                        if let Some(&i)=pos.get(&m) {c[i]=x;}
                        if m.0==0 {if let Some(&i)=pos.get(&(1,m.1)){uc[i]=x;}}
                    }
                    if c.iter().any(|&x|x!=0){columns.push(c);}
                    if uc.iter().any(|&x|x!=0){columns.push(uc);}
                }}
            }
        }
    }
    let image_rank=rank(columns.clone());
    // The generic even Jacobian quotient has basis [1], [u], [a^2].
    // Here u[a^2]=0 follows from K-aK_a/4=(u(1-b^2)/2)a^2.
    let mut carrier_columns=vec![vec![0;3];rows.len()];
    for (i,&(u,a)) in rows.iter().enumerate() {
        match (u,a) {
            (0,0)=>carrier_columns[i][0]=1,
            (1,0)=>carrier_columns[i][1]=1,
            (0,2)=>carrier_columns[i][2]=1,
            _=>{}
        }
    }
    for col in &columns {
        let mut y=[0,0,0];
        for (i,&x) in col.iter().enumerate(){for k in 0..3{y[k]=add_mod(y[k],mul_mod(x,carrier_columns[i][k]));}}
        assert_eq!(y,[0,0,0],"exact image must die in the even Jacobian quotient");
    }
    let carrier_rank=rank(carrier_columns);
    let cokernel_dim=rows.len()-image_rank;
    let relative_kernel_dim=rows.len()-carrier_rank-image_rank;
    assert_eq!((cokernel_dim,carrier_rank,relative_kernel_dim),(4,3,1));
    println!("even b={bv},D={d}: cokernel={cokernel_dim}, carrier_image={carrier_rank}, relative_kernel={relative_kernel_dim}");
}
fn main(){
    for b in [0,2,3] {for d in [12,16,20,24]{audit(d,b);}}
    for b in [0,2,3] {for d in [12,16,20,24]{audit_even(d,b);}}
    println!("{}", r#"{"schema":"marici.benincasa.soft_axis_generic_jacobian_map.v2","odd":{"cokernel_dimension":3,"carrier_rank":2,"h0_kernel_dimension":1},"even":{"cokernel_dimension":4,"carrier_rank":3,"h0_kernel_dimension":1,"conormal_length":2,"h0_kernel_is_conormal":false},"full_derived_fiber_required":true,"new_carrier_datum":false}"#);
}
