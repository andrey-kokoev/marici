use std::collections::BTreeMap;

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct C { re: i128, im: i128 }
impl C {
    fn z() -> Self { Self { re:0, im:0 } }
    fn r(x:i128) -> Self { Self { re:x, im:0 } }
    fn i(x:i128) -> Self { Self { re:0, im:x } }
    fn add(self,o:Self)->Self { Self{re:self.re+o.re,im:self.im+o.im} }
    fn mul(self,o:Self)->Self { Self{re:self.re*o.re-self.im*o.im,im:self.re*o.im+self.im*o.re} }
    fn scale(self,n:i128)->Self { Self{re:self.re*n,im:self.im*n} }
}
type Key=[usize;9]; // q,p,h for factors 0,1,2
type Elem=BTreeMap<Key,C>;

fn binom(n:usize,k:usize)->i128 {
    let mut z=1_i128; for j in 0..k { z=z*(n-j) as i128/(j+1) as i128; } z
}
fn fact(n:usize)->i128 { (1..=n as i128).product() }
fn mip(k:usize)->C { match k%4 {0=>C::r(1),1=>C::i(-1),2=>C::r(-1),_=>C::i(1)} }
fn factor_mul(a:(usize,usize,usize),b:(usize,usize,usize))->Vec<((usize,usize,usize),C)> {
    let mut out=Vec::new();
    for k in 0..=a.1.min(b.0) {
        out.push(((a.0+b.0-k,a.1+b.1-k,a.2+b.2+k),
                  mip(k).scale(fact(k)*binom(a.1,k)*binom(b.0,k))));
    }
    out
}
fn put(e:&mut Elem,k:Key,c:C) {
    let n=e.get(&k).copied().unwrap_or(C::z()).add(c);
    if n==C::z(){e.remove(&k);}else{e.insert(k,n);}
}
fn one()->Elem { BTreeMap::from([([0;9],C::r(1))]) }
fn gen(f:usize,slot:usize)->Elem {
    let mut k=[0_usize;9]; k[3*f+slot]=1; BTreeMap::from([(k,C::r(1))])
}
fn mono(k:Key)->Elem { BTreeMap::from([(k,C::r(1))]) }
fn add(a:&Elem,b:&Elem)->Elem { let mut z=a.clone(); for(k,c)in b{put(&mut z,*k,*c);}z }
fn scale(a:&Elem,c:C)->Elem { let mut z=Elem::new();for(k,v)in a{put(&mut z,*k,v.mul(c));}z }
fn mul(a:&Elem,b:&Elem)->Elem {
    let mut z=Elem::new();
    for(ka,ca)in a { for(kb,cb)in b {
        for(x,cx)in factor_mul((ka[0],ka[1],ka[2]),(kb[0],kb[1],kb[2])) {
        for(y,cy)in factor_mul((ka[3],ka[4],ka[5]),(kb[3],kb[4],kb[5])) {
        for(w,cw)in factor_mul((ka[6],ka[7],ka[8]),(kb[6],kb[7],kb[8])) {
            put(&mut z,[x.0,x.1,x.2,y.0,y.1,y.2,w.0,w.1,w.2],
                ca.mul(*cb).mul(cx).mul(cy).mul(cw));
        }}}
    }} z
}
fn pow(a:&Elem,n:usize)->Elem { let mut z=one();for _ in 0..n{z=mul(&z,a);}z }
fn sum_gen(factors:&[usize],slot:usize)->Elem {
    let mut z=Elem::new();for &f in factors{z=add(&z,&gen(f,slot));}z
}

fn dpk_delta(k:usize,factors:&[usize])->Elem {
    if k==0{return Elem::new();}
    let q=sum_gen(factors,0);let p=sum_gen(factors,1);let h=sum_gen(factors,2);
    let mut z=scale(&mul(&pow(&q,2),&pow(&p,k-1)),C::r(-(k as i128)));
    if k>=2 {
        z=add(&z,&scale(&mul(&mul(&h,&q),&pow(&p,k-2)),C::i(2*binom(k,2))));
    }
    if k>=3 {
        z=add(&z,&scale(&mul(&pow(&h,2),&pow(&p,k-3)),C::r(2*binom(k,3))));
    }
    z
}
fn theta_pair(k:usize,a:usize,b:usize)->Elem {
    if k==0{return Elem::new();}
    let p=sum_gen(&[a,b],1);
    let dp=scale(&add(&pow(&gen(a,0),2),&pow(&gen(b,0),2)),C::r(-1));
    let mut d_delta=Elem::new();
    for j in 0..k {
        d_delta=add(&d_delta,&mul(&mul(&pow(&p,j),&dp),&pow(&p,k-1-j)));
    }
    add(&dpk_delta(k,&[a,b]),&scale(&d_delta,C::r(-1)))
}

fn split_factor(poly:&Elem,which:usize)->Elem {
    let (left,right) = if which==0 {(0,1)} else {(1,2)};
    let mut out=Elem::new();
    for(k,c)in poly {
        assert_eq!(k[3],0);assert_eq!(k[4],0);assert_eq!(k[5],0);
        let source=if which==0 {(k[0],k[1],k[2])} else {(k[6],k[7],k[8])};
        let untouched=if which==0 {(k[6],k[7],k[8])} else {(k[0],k[1],k[2])};
        let mut term=scale(&one(),*c);
        term=mul(&term,&pow(&sum_gen(&[left,right],0),source.0));
        term=mul(&term,&pow(&sum_gen(&[left,right],1),source.1));
        term=mul(&term,&pow(&sum_gen(&[left,right],2),source.2));
        let mut uk=[0_usize;9];
        let uf=if which==0 {2}else{0};
        uk[3*uf]=untouched.0;uk[3*uf+1]=untouched.1;uk[3*uf+2]=untouched.2;
        term=mul(&term,&mono(uk));
        out=add(&out,&term);
    }
    out
}

fn main(){
    let theta_02=theta_pair(3,0,2);
    assert_eq!(theta_02.len(),8);

    let mut left=split_factor(&theta_02,0); // (Delta tensor 1)Theta
    let mut right=split_factor(&theta_02,2); // (1 tensor Delta)Theta

    // +(Theta tensor 1)Delta(p^3)
    for k in 0..=3 {
        let t=theta_pair(k,0,1);
        let p2=pow(&gen(2,1),3-k);
        left=add(&left,&scale(&mul(&t,&p2),C::r(binom(3,k))));
    }
    // +(1 tensor Theta)Delta(p^3)
    for k in 0..=3 {
        let p0=pow(&gen(0,1),k);
        let t=theta_pair(3-k,1,2);
        right=add(&right,&scale(&mul(&p0,&t),C::r(binom(3,k))));
    }
    assert_eq!(left,right);
    let central=left.iter().filter(|(k,_)| k[0]==0&&k[1]==0&&k[3]==0&&k[4]==0&&k[6]==0&&k[7]==0).count();
    let scalar=left.get(&[0;9]).copied().unwrap_or(C::z());
    assert_eq!(scalar,C::z());

    println!("{{");
    println!("  \"schema\": \"marici.weyl_p3_cohochschild_cocycle.v1\",");
    println!("  \"binary_theta_terms\": {},",theta_02.len());
    println!("  \"three_factor_terms_per_route\": {},",left.len());
    println!("  \"pure_central_three_factor_terms\": {central},");
    println!("  \"scalar_residual_re\": {},",scalar.re);
    println!("  \"scalar_residual_im\": {},",scalar.im);
    println!("  \"complete_quantum_cohochschild_identity\": true");
    println!("}}");
}
