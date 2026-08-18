use std::collections::BTreeSet;

const P: i64 = 32_003;

fn add(a: i64, b: i64) -> i64 { (a + b).rem_euclid(P) }
fn mul(a: i64, b: i64) -> i64 { ((a as i128 * b as i128) % P as i128) as i64 }
fn pow(mut a: i64, mut n: i64) -> i64 {
    let mut r = 1;
    while n > 0 { if n & 1 == 1 { r = mul(r, a); } a = mul(a, a); n >>= 1; }
    r
}
fn inv(a: i64) -> i64 { pow(a.rem_euclid(P), P - 2) }

fn k0(a: i64, b: i64, x: i64, y: i64, z: i64) -> i64 {
    let c = -(x + y + z);
    let (c2, a2, b2) = (mul(c,c), mul(a,a), mul(b,b));
    let (x2, y2, z2) = (mul(x,x), mul(y,y), mul(z,z));
    [
        mul(x2, mul(a2,a2)),
        -mul(x2 + y2 - z2, mul(a2,b2)),
        mul(y2, mul(b2,b2)),
        mul(x2 * (x2-y2-z2), a2),
        mul(-x2+y2-z2, mul(c2,a2)),
        mul(y2 * (y2-x2-z2), b2),
        mul(-y2+x2-z2, mul(c2,b2)),
        mul(z2, mul(c2,c2)),
        mul(z2 * (-x2-y2+z2), c2),
        mul(z2, mul(x2,y2)),
    ].into_iter().fold(0, add)
}

fn trim(mut f: Vec<i64>) -> Vec<i64> {
    while f.last() == Some(&0) { f.pop(); }
    f
}
fn div_rem(mut f: Vec<i64>, g: &[i64]) -> Vec<i64> {
    let gd = g.len()-1;
    let gi = inv(g[gd]);
    while f.len() >= g.len() {
        let d = f.len()-1-gd;
        let q = mul(*f.last().unwrap(), gi);
        for (i,&v) in g.iter().enumerate() { f[d+i] = add(f[d+i], -mul(q,v)); }
        f = trim(f);
    }
    f
}
fn gcd_degree(mut f: Vec<i64>, mut g: Vec<i64>) -> usize {
    f=trim(f); g=trim(g);
    while !g.is_empty() { let r=div_rem(f,&g); f=g; g=r; }
    f.len().saturating_sub(1)
}
fn interpolate(values: &[i64]) -> Vec<i64> {
    let n=values.len();
    let mut a=vec![vec![0_i64;n+1];n];
    for i in 0..n {
        let mut power=1;
        for j in 0..n { a[i][j]=power; power=mul(power,i as i64); }
        a[i][n]=values[i];
    }
    for col in 0..n {
        let pivot=(col..n).find(|&row| a[row][col]!=0).unwrap();
        a.swap(col,pivot);
        let scale=inv(a[col][col]);
        for j in col..=n { a[col][j]=mul(a[col][j],scale); }
        for row in 0..n {
            if row==col { continue; }
            let q=a[row][col];
            for j in col..=n { a[row][j]=add(a[row][j],-mul(q,a[col][j])); }
        }
    }
    trim((0..n).map(|i|a[i][n]).collect())
}
fn branch_punctures(line: [i64;3], x:i64,y:i64,z:i64) -> usize {
    let values:Vec<_>=(0..5).map(|t| {
        if line[1]!=0 {
            let a=t as i64;
            let b=mul(-(mul(line[0],a)+line[2]),inv(line[1]));
            k0(a,b,x,y,z)
        } else {
            let b=t as i64;
            let a=mul(-(mul(line[1],b)+line[2]),inv(line[0]));
            k0(a,b,x,y,z)
        }
    }).collect();
    let f=interpolate(&values);
    let derivative:Vec<_>=(1..f.len()).map(|i|mul(i as i64,f[i])).collect();
    f.len()-1-gcd_degree(f,derivative)
}
fn intersection(l:[i64;3],m:[i64;3])->Option<(i64,i64)> {
    let det=add(mul(l[0],m[1]),-mul(m[0],l[1]));
    if det==0 { return None; }
    let a=mul(add(mul(l[1],m[2]),-mul(m[1],l[2])),inv(det));
    let b=mul(add(mul(l[2],m[0]),-mul(m[2],l[0])),inv(det));
    Some((a,b))
}
fn audit(x:i64,y:i64,z:i64,last_name:&'static str,last_line:[i64;3]) {
    let lines=[
        ("q_g1",[0,1,-(y+z)]),
        ("q_g2",[1,0,-(x+z)]),
        ("q_g3",[1,1,z]),
        (last_name,last_line),
    ];
    let mut rank=9_usize;
    for i in 0..lines.len() {
        let branch=branch_punctures(lines[i].1,x,y,z);
        let mut finite=BTreeSet::new();
        for j in 0..i {
            if let Some(point)=intersection(lines[i].1,lines[j].1) {
                if k0(point.0,point.1,x,y,z)!=0 { finite.insert(point); }
            }
        }
        let punctures=branch+finite.len();
        let increment=punctures-1;
        rank+=increment;
        println!("point=({x},{y},{z}) line={} branch_punctures={branch} finite_new={} increment={increment}",lines[i].0,finite.len());
    }
    println!("point=({x},{y},{z}) partner={last_name} four_mark_residue_rank={rank} five_pole_rank={}",15+rank);
}
fn main(){
    audit(2,3,4,"q_g23",[0,1,-2]);
    audit(3,5,6,"q_g23",[0,1,-3]);
    audit(2,3,4,"q_g31",[1,0,-3]);
    audit(3,5,6,"q_g31",[1,0,-5]);
}
