use std::collections::BTreeMap;

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct C { re: i128, im: i128 }
impl C {
    fn new(re: i128, im: i128) -> Self { Self { re, im } }
    fn add(self, o: Self) -> Self { Self::new(self.re + o.re, self.im + o.im) }
    fn mul(self, o: Self) -> Self {
        Self::new(self.re * o.re - self.im * o.im, self.re * o.im + self.im * o.re)
    }
    fn scale(self, n: i128) -> Self { Self::new(self.re * n, self.im * n) }
}

type Key = [usize; 6]; // qL,pL,hL,qR,pR,hR
type Elem = BTreeMap<Key, C>;

fn binomial(n: usize, k: usize) -> i128 {
    let mut out = 1_i128;
    for i in 0..k { out = out * (n - i) as i128 / (i + 1) as i128; }
    out
}
fn factorial(n: usize) -> i128 { (1..=n as i128).product() }
fn minus_i_pow(k: usize) -> C {
    match k % 4 { 0 => C::new(1,0), 1 => C::new(0,-1), 2 => C::new(-1,0), _ => C::new(0,1) }
}
fn add_term(e: &mut Elem, k: Key, c: C) {
    let next = e.get(&k).copied().unwrap_or(C::new(0,0)).add(c);
    if next == C::new(0,0) { e.remove(&k); } else { e.insert(k, next); }
}
fn one() -> Elem { BTreeMap::from([([0;6], C::new(1,0))]) }
fn generator(index: usize) -> Elem {
    let mut k = [0_usize;6]; k[index] = 1;
    BTreeMap::from([(k, C::new(1,0))])
}
fn add_elem(a: &Elem, b: &Elem) -> Elem {
    let mut out = a.clone();
    for (k,c) in b { add_term(&mut out, *k, *c); }
    out
}
fn scale_elem(a: &Elem, c: C) -> Elem {
    let mut out = Elem::new();
    for (k,v) in a { add_term(&mut out, *k, v.mul(c)); }
    out
}

fn factor_products(aq:usize, ap:usize, ah:usize, bq:usize, bp:usize, bh:usize)
    -> Vec<((usize,usize,usize), C)> {
    let mut out = Vec::new();
    for k in 0..=ap.min(bq) {
        let integer = factorial(k) * binomial(ap,k) * binomial(bq,k);
        out.push(((aq+bq-k, ap+bp-k, ah+bh+k), minus_i_pow(k).scale(integer)));
    }
    out
}
fn mul_elem(a: &Elem, b: &Elem) -> Elem {
    let mut out = Elem::new();
    for (ka,ca) in a {
        for (kb,cb) in b {
            for (l,cl) in factor_products(ka[0],ka[1],ka[2],kb[0],kb[1],kb[2]) {
                for (r,cr) in factor_products(ka[3],ka[4],ka[5],kb[3],kb[4],kb[5]) {
                    add_term(&mut out, [l.0,l.1,l.2,r.0,r.1,r.2], ca.mul(*cb).mul(cl).mul(cr));
                }
            }
        }
    }
    out
}
fn pow(a: &Elem, n: usize) -> Elem {
    let mut out = one();
    for _ in 0..n { out = mul_elem(&out,a); }
    out
}

fn main() {
    let q = add_elem(&generator(0), &generator(3));
    let p = add_elem(&generator(1), &generator(4));
    let h = add_elem(&generator(2), &generator(5));

    // Delta(D p^3) from the normal-ordered formula.
    let term0 = scale_elem(&mul_elem(&pow(&q,2), &pow(&p,2)), C::new(-3,0));
    let term1 = scale_elem(&mul_elem(&mul_elem(&h,&q),&p), C::new(0,6));
    let term2 = scale_elem(&pow(&h,2), C::new(2,0));
    let delta_dp3 = add_elem(&add_elem(&term0,&term1),&term2);

    // (D tensor 1 + 1 tensor D) Delta(p^3), using Dp=-(qL^2+qR^2).
    let dp = scale_elem(&add_elem(&pow(&generator(0),2),&pow(&generator(3),2)), C::new(-1,0));
    let p2 = pow(&p,2);
    let d_delta_p3 = add_elem(
        &add_elem(&mul_elem(&dp,&p2), &mul_elem(&mul_elem(&p,&dp),&p)),
        &mul_elem(&p2,&dp));
    let theta = add_elem(&delta_dp3, &scale_elem(&d_delta_p3,C::new(-1,0)));

    assert!(!theta.is_empty());
    let central_terms: Vec<_> = theta.iter().filter(|(k,_)| k[0]==0&&k[1]==0&&k[3]==0&&k[4]==0).collect();
    // Primitive hbar makes all pure central contributions part of the same
    // binary defect; no scalar term independent of hL,hR is allowed.
    assert!(central_terms.iter().all(|(k,_)| k[2]+k[5] > 0));
    let scalar_residual = theta.get(&[0;6]).copied().unwrap_or(C::new(0,0));
    assert_eq!(scalar_residual, C::new(0,0));
    assert_eq!(central_terms.len(), 1);
    let (central_key, central_value) = central_terms[0];

    println!("{{");
    println!("  \"schema\": \"marici.weyl_p3_coleibniz_defect.v1\",");
    println!("  \"theta_term_count\": {},", theta.len());
    println!("  \"central_hbar_term_count\": {},", central_terms.len());
    println!("  \"central_hbar_exponents\": \"hL^{} hR^{}\",", central_key[2], central_key[5]);
    println!("  \"central_hbar_coefficient_re\": {},", central_value.re);
    println!("  \"central_hbar_coefficient_im\": {},", central_value.im);
    println!("  \"scalar_residual_re\": {},", scalar_residual.re);
    println!("  \"scalar_residual_im\": {},", scalar_residual.im);
    println!("  \"hbar_squared_grade_absorbed_by_binary_defect\": true");
    println!("}}");
}
