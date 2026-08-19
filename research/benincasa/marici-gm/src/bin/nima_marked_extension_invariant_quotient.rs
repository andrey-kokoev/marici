//! Rank of the primitive-lift ambiguity projected to the nine absolute rows.
mod source {
    #![allow(dead_code)]
    include!("marked_relative_reduction_engine.rs");

    pub fn projected_ambiguity(u:u64,v:u64,axis:char,master:usize)->(usize,usize,usize,Vec<Vec<u64>>){
        let g=geometry(u,v,axis);let cs=classes(&g);
        let mut cols:Vec<Poly>=cs.iter().map(|q|common(&g,q)).collect();
        for(sa,sb)in[(1,1),(1,0),(0,1),(0,0)]{for m in monomials(8){cols.push(exact(&g,sa,sb,m,false));cols.push(exact(&g,sa,sb,m,true));}}
        let rhs=target(&g,&cs[master]);let mut mons=BTreeSet::new();for q in &cols{mons.extend(q.0.keys().copied())}mons.extend(rhs.0.keys().copied());
        let n=cols.len();let mut a:Vec<Vec<F>>=mons.iter().map(|m|{let mut r:Vec<F>=cols.iter().map(|q|q.0.get(m).copied().unwrap_or(F::z())).collect();r.push(rhs.0.get(m).copied().unwrap_or(F::z()));r}).collect();
        let rows=a.len();let mut piv=Vec::new();let mut rr=0;
        for c in 0..n{let Some(p)=(rr..rows).find(|&i|a[i][c].0!=0)else{continue};a.swap(rr,p);let z=a[rr][c].inv();for j in c..=n{a[rr][j]=a[rr][j].mul(z)}for i in 0..rows{if i!=rr&&a[i][c].0!=0{let z=a[i][c];for j in c..=n{a[i][j]=a[i][j].sub(z.mul(a[rr][j]))}}}piv.push((rr,c));rr+=1;if rr==rows{break}}
        let pivot_cols:BTreeSet<usize>=piv.iter().map(|(_,c)|*c).collect();let free:Vec<usize>=(0..n).filter(|c|!pivot_cols.contains(c)).collect();
        let mut projected:Vec<Vec<F>>=Vec::new();
        for f in free{let mut vector=vec![F::z();9];if(3..12).contains(&f){vector[f-3]=F::n(1)}for(row,col)in &piv{if(3..12).contains(col){vector[*col-3]=F::z().sub(a[*row][f])}}if vector.iter().any(|x|x.0!=0){projected.push(vector)}}
        let mut rank=0;for c in 0..9{let Some(p)=(rank..projected.len()).find(|i|projected[*i][c].0!=0)else{continue};projected.swap(rank,p);let z=projected[rank][c].inv();for j in c..9{projected[rank][j]=projected[rank][j].mul(z)}for i in 0..projected.len(){if i!=rank&&projected[i][c].0!=0{let z=projected[i][c];for j in c..9{projected[i][j]=projected[i][j].sub(z.mul(projected[rank][j]))}}}rank+=1}
        let basis=projected.into_iter().take(rank).map(|row|row.into_iter().map(|x|x.0).collect()).collect();
        (rr,rank,9-rank,basis)
    }
    pub fn prime()->u64{P}
}

fn main(){
    let p=source::prime();let mut points=vec![(7,11,"generic"),(13,19,"generic"),(23,29,"generic"),(5,17,"generic")];
    if p==2_305_843_009_213_693_951{points.extend([(8,1_223_657_616_096_235_422,"quartic"),(12,2_135_523_325_595_541_720,"quartic")])}
    if p==2_305_843_009_213_693_723{points.extend([(3,2_186_357_971_342_101_205,"quartic"),(3,119_485_037_871_592_534,"quartic")])}
    let inv2=(p+1)/2;let mut out=Vec::new();
    for(u,v,kind)in points{for axis in['u','v']{for master in 0..3{let(r,a,q,b)=source::projected_ambiguity(u,v,axis,master);let c=((((3u128*u as u128+v as u128+p as u128-2)%p as u128)*inv2 as u128)%p as u128)as u64;let expected=vec![vec![1,0,0,u%p,(((u%p)as u128*c as u128)%p as u128)as u64,0,0,0,0],vec![0,1,(u+1)%p,p-1,if c==0{0}else{p-c},0,0,0,0]];assert_eq!(b,expected,"ambiguity normal form");out.push(format!("{{\"u\":{},\"v\":{},\"kind\":\"{}\",\"axis\":\"{}\",\"master\":{},\"source_rank\":{},\"ambiguity_rank\":{},\"invariant_quotient_dimension\":{},\"normal_form_verified\":true}}",u,v,kind,axis,master,r,a,q));}}}
    println!("{{\"schema\":\"marici.nima.marked_extension_invariant_quotient.v2\",\"prime\":{},\"ambiguity_normal_form\":[\"(1,0,0,u,u*c,0,0,0,0)\",\"(0,1,u+1,-1,-c,0,0,0,0)\"],\"c\":\"(3u+v-2)/2\",\"mixed_invariants\":[\"x2-(u+1)x1\",\"x3-u*x0+x1\",\"x4-u*c*x0+c*x1\"],\"records\":[{}]}}",p,out.join(","));
}
