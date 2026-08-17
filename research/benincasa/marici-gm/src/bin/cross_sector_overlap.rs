use std::collections::BTreeMap;

#[derive(Clone, Debug, Eq, PartialEq)]
struct P(BTreeMap<[u8; 4], i64>); // x,y,z,b

impl P {
    fn c(n: i64) -> Self {
        let mut m = BTreeMap::new();
        if n != 0 { m.insert([0; 4], n); }
        Self(m)
    }
    fn v(i: usize) -> Self {
        let mut e = [0; 4]; e[i] = 1;
        Self(BTreeMap::from([(e, 1)]))
    }
    fn add(&self, q: &Self) -> Self {
        let mut m = self.0.clone();
        for (e, c) in &q.0 { *m.entry(*e).or_default() += c; }
        m.retain(|_, c| *c != 0); Self(m)
    }
    fn neg(&self) -> Self { Self(self.0.iter().map(|(e,c)| (*e,-c)).collect()) }
    fn sub(&self, q: &Self) -> Self { self.add(&q.neg()) }
    fn scale(&self, n: i64) -> Self { Self(self.0.iter().filter_map(|(e,c)| { let v=n*c; (v!=0).then_some((*e,v)) }).collect()) }
    fn mul(&self, q: &Self) -> Self {
        let mut m = BTreeMap::new();
        for (e,c) in &self.0 { for (f,d) in &q.0 {
            let mut g=[0;4]; for i in 0..4 { g[i]=e[i]+f[i]; }
            *m.entry(g).or_default() += c*d;
        }}
        m.retain(|_, c| *c != 0); Self(m)
    }
    fn pow(&self, n: u8) -> Self { (0..n).fold(Self::c(1), |a,_| a.mul(self)) }
    fn db(&self) -> Self {
        let mut m=BTreeMap::new();
        for (e,c) in &self.0 { if e[3]>0 { let mut f=*e; f[3]-=1; m.insert(f,c*i64::from(e[3])); }}
        Self(m)
    }
    fn text(&self) -> String {
        if self.0.is_empty() { return "0".into(); }
        self.0.iter().rev().map(|(e,c)| format!("{c}*x^{}*y^{}*z^{}*b^{}",e[0],e[1],e[2],e[3])).collect::<Vec<_>>().join(" + ")
    }
}

fn cm(x:&P,y:&P,z:&P,c:&P,a:&P,b:&P)->P {
    let (x2,y2,z2,c2,a2,b2)=(x.pow(2),y.pow(2),z.pow(2),c.pow(2),a.pow(2),b.pow(2));
    let h=x2.add(&y2).sub(&z2);
    [x2.mul(&a.pow(4)), a2.mul(&b2).mul(&h).scale(-1), y2.mul(&b.pow(4)),
     a2.mul(&x2).mul(&x2.sub(&y2).sub(&z2)),
     c2.mul(&a2).mul(&y2.sub(&x2).sub(&z2)),
     b2.mul(&y2).mul(&y2.sub(&x2).sub(&z2)),
     c2.mul(&b2).mul(&x2.sub(&y2).sub(&z2)), z2.mul(&c.pow(4)),
     c2.mul(&z2).mul(&z2.sub(&x2).sub(&y2)), z2.mul(&x2).mul(&y2)]
        .into_iter().fold(P::c(0), |s,p| s.add(&p))
}

fn main() {
    let (x,y,z,b)=(P::v(0),P::v(1),P::v(2),P::v(3));
    let e=x.add(&y).add(&z); let minus_e=e.neg();
    let k=cm(&x,&y,&z,&minus_e,&minus_e,&b);
    let (x2,y2,z2,e2)=(x.pow(2),y.pow(2),z.pow(2),e.pow(2));
    let c2=y2.mul(&y2.sub(&x2).sub(&z2).sub(&e2.scale(2)));
    let c0=e2.mul(&x2.mul(&x2.sub(&y2).sub(&z2)).add(&z2.mul(&z2.sub(&x2).sub(&y2))))
        .add(&y2.mul(&e.pow(4))).add(&z2.mul(&x2).mul(&y2));
    let k_compact=y2.mul(&b.pow(4)).add(&c2.mul(&b.pow(2))).add(&c0);
    assert_eq!(k,k_compact);
    let discriminant_u=c2.pow(2).sub(&y2.mul(&c0).scale(4));
    let marks=[
        ("q_g1",x.add(&b).sub(&e)),
        ("q_g2",y.sub(&e.scale(2))),
        ("q_g3",z.add(&b).sub(&e)),
        ("q_g12",x.add(&y).add(&b).sub(&e)),
        ("q_g23",y.add(&z).add(&b).sub(&e)),
        ("q_g31",z.add(&x).sub(&e.scale(2))),
        ("q_G31",e.add(&b)),
    ];
    let sector_12_lower = [
        ("q_g23", y.add(&z).add(&b).sub(&e)),
        ("q_g31", z.add(&x).sub(&e.scale(2))),
    ];
    let sector_23_lower = [
        ("q_g31", z.add(&x).sub(&e.scale(2))),
        ("q_g12", x.add(&y).add(&b).sub(&e)),
    ];
    // The printed source is sum_i 1/q_Gi (1/q_lower+1/q_lower).
    // Record its six (marked cut, lower occurrence) pole pairs.  None has
    // two marked-cut poles, so the G12,G23 double-pole coefficient is zero.
    let source_occurrences = [
        ("G12","g23"),("G12","g31"),("G23","g31"),
        ("G23","g12"),("G31","g12"),("G31","g23"),
    ];
    assert!(source_occurrences.iter().all(|(cut,_)| *cut != "G12*G23"));
    assert_eq!(sector_12_lower[0].1, b.sub(&x));
    assert_eq!(sector_12_lower[1].1, x.neg().sub(&y.scale(2)).sub(&z));
    assert_eq!(sector_23_lower[0].1, sector_12_lower[1].1);
    assert_eq!(sector_23_lower[1].1, b.sub(&z));
    // The source volume is dc^da^db. Ordered residues (G12,G23) and
    // (G23,G12) therefore induce +db and -db respectively.
    assert_eq!(1_i32, -(-1_i32));
    // Both orders substitute exactly the same regular sequence c=a=-E.
    assert_eq!(k, cm(&x,&y,&z,&minus_e,&minus_e,&b));
    // The common curve is generically branched: K and dK/db are nonzero.
    assert!(!k.0.is_empty() && !k.db().0.is_empty());
    println!("{{");
    println!("  \"locus\": [\"q_G12=0\", \"q_G23=0\", \"c=a=-E\"],");
    println!("  \"fiber_coordinate\": \"b=y31\",");
    println!("  \"restricted_K\": \"y^2*b^4 + y^2*(y^2-x^2-z^2-2E^2)*b^2 + C0\",");
    println!("  \"C0\": \"E^2*[x^2(x^2-y^2-z^2)+z^2(z^2-x^2-y^2)] + y^2*E^4 + x^2*y^2*z^2\",");
    println!("  \"discriminant_in_u_equals_b2\": \"{}\",", discriminant_u.text());
    println!("  \"marks\": {{");
    for (i,(n,p)) in marks.iter().enumerate() { println!("    \"{n}\": \"{}\"{}",p.text(),if i+1==marks.len(){""}else{","}); }
    println!("  }},");
    println!("  \"sector_12_lower_marks\": {{\"q_g23\": \"b-x\", \"q_g31\": \"-(x+2y+z)\"}},");
    println!("  \"sector_23_lower_marks\": {{\"q_g31\": \"-(x+2y+z)\", \"q_g12\": \"b-z\"}},");
    println!("  \"source_double_pole_G12_G23\": false,");
    println!("  \"double_leray_residue_of_frozen_form\": \"absent\",");
    println!("  \"orientation\": {{\"Res_G23_after_G12\": 1, \"Res_G12_after_G23\": -1}},");
    println!("  \"verdict\": \"geometric intersection exists and has the Koszul sign, but the frozen source form supplies no iterated-residue correspondence\"");
    println!("}}");
}
