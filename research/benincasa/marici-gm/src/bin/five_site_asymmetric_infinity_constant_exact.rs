use num_bigint::BigInt;
use num_integer::Integer;
use num_traits::{One, Signed, ToPrimitive, Zero};
use serde_json::{json,Value};
use std::{collections::BTreeMap, fmt, ops::{Add, Div, Mul, Neg}, fs};

#[derive(Clone, Debug, Eq, PartialEq)]
struct Rat { n: BigInt, d: BigInt }

impl Rat {
    fn new(n: impl Into<BigInt>, d: impl Into<BigInt>) -> Self {
        let mut n=n.into(); let mut d=d.into();
        assert!(!d.is_zero());
        if d.is_negative() { n=-n; d=-d; }
        let g=n.gcd(&d);
        Self{n:n/g.clone(),d:d/g}
    }
    fn integer(n:i64)->Self {Self::new(n,1)}
    fn powi(&self,n:usize)->Self {
        (0..n).fold(Self::integer(1),|a,_|a*self.clone())
    }
    fn to_f64(&self)->f64 {self.n.to_f64().unwrap()/self.d.to_f64().unwrap()}
}
impl Add for Rat {type Output=Self;fn add(self,r:Self)->Self{Rat::new(self.n*r.d.clone()+r.n*self.d.clone(),self.d*r.d)}}
impl Mul for Rat {type Output=Self;fn mul(self,r:Self)->Self{Rat::new(self.n*r.n,self.d*r.d)}}
impl Div for Rat {type Output=Self;fn div(self,r:Self)->Self{Rat::new(self.n*r.d,self.d*r.n)}}
impl Neg for Rat {type Output=Self;fn neg(self)->Self{Rat::new(-self.n,self.d)}}
impl fmt::Display for Rat {
    fn fmt(&self,f:&mut fmt::Formatter<'_>)->fmt::Result {
        if self.d.is_one(){write!(f,"{}",self.n)}else{write!(f,"{}/{}",self.n,self.d)}
    }
}

fn binomial(n:usize,k:usize)->BigInt {
    if k>n{return BigInt::zero();}
    (0..k).fold(BigInt::one(),|a,i|a*BigInt::from(n-i)/BigInt::from(i+1))
}

fn convolution(a:&[Rat],b:&[Rat],degree:usize)->Vec<Rat>{
    let mut out=vec![Rat::integer(0);degree+1];
    for (i,x) in a.iter().enumerate(){for(j,y)in b.iter().enumerate(){
        if i+j<=degree{out[i+j]=out[i+j].clone()+x.clone()*y.clone();}
    }}
    out
}

fn inverse_linear_power(constant:i64,power:usize,degree:usize)->Vec<Rat>{
    (0..=degree).map(|n|{
        let sign=if n%2==0{1}else{-1};
        let coefficient=BigInt::from(sign)*binomial(power+n-1,n);
        Rat::new(coefficient,BigInt::from(constant).pow((power+n) as u32))
    }).collect()
}

fn term_partial_fractions(count:i64,sizes:&[usize],cycle_size:usize)->BTreeMap<(usize,usize),Rat>{
    let mut multiplicities=BTreeMap::<usize,usize>::new();
    multiplicities.insert(1,cycle_size);
    for &k in sizes{*multiplicities.entry(k).or_default()+=1;}
    let mut result=BTreeMap::new();
    for (&pole,&m) in &multiplicities {
        let degree=m-1;
        // count/n * r^2, with r=(x-pole)/2.
        let mut series=vec![Rat::integer(0);degree+1];
        let base_denominator=4*cycle_size as i64;
        series[0]=Rat::new(count*(pole as i64).pow(2),base_denominator);
        if degree>=1 {series[1]=Rat::new(-2*count*pole as i64,base_denominator);}
        if degree>=2 {series[2]=Rat::new(count,base_denominator);}
        for (&other,&power) in &multiplicities {
            if other==pole{continue;}
            series=convolution(&series,&inverse_linear_power(other as i64-pole as i64,power,degree),degree);
        }
        for j in 1..=m {
            result.insert((pole,j),series[m-j].clone());
        }
    }
    result
}

fn exact_integral(cycle_size:usize,profiles:&[(i64,Vec<usize>)])->(String,f64){
    let mut coefficients=BTreeMap::<(usize,usize),Rat>::new();
    for (count,sizes) in profiles {
        for (key,value) in term_partial_fractions(*count,sizes,cycle_size) {
            let old=coefficients.remove(&key).unwrap_or_else(||Rat::integer(0));
            coefficients.insert(key,old+value);
        }
    }
    let simple_sum=(1..=cycle_size).map(|k|coefficients.get(&(k,1)).cloned().unwrap_or_else(||Rat::integer(0)))
        .fold(Rat::integer(0),|a,b|a+b);
    assert_eq!(simple_sum,Rat::integer(0));

    let mut rational=Rat::integer(0);
    let mut logs=BTreeMap::<usize,Rat>::new();
    for ((k,j),a) in &coefficients {
        if *j==1 {
            logs.insert(*k, -a.clone()/Rat::integer(2));
        } else {
            let denominator=Rat::integer(2*(*j as i64-1))*Rat::integer(*k as i64).powi(*j-1);
            rational=rational.clone()+a.clone()/denominator;
        }
    }
    logs.remove(&1);
    let log4=logs.remove(&4).unwrap_or_else(||Rat::integer(0));
    let log2=logs.remove(&2).unwrap_or_else(||Rat::integer(0))+Rat::integer(2)*log4;
    logs.insert(2,log2);
    logs.retain(|_,a|!a.n.is_zero());
    let expression=std::iter::once(rational.to_string())
        .chain(logs.iter().map(|(k,a)|format!("({a})*log({k})")))
        .collect::<Vec<_>>().join("+");
    let numeric_i=rational.to_f64()+logs.iter().map(|(k,a)|a.to_f64()*(*k as f64).ln()).sum::<f64>();
    let numeric_c=4.0*std::f64::consts::PI*numeric_i;
    (expression,numeric_c)
}

fn main(){
    let profiles5=vec![
        (10,vec![2,2,3,4]),(20,vec![2,2,3,5]),(10,vec![2,2,4,5]),
        (10,vec![2,3,3,4]),(10,vec![2,3,3,5]),(20,vec![2,3,4,4]),
        (50,vec![2,3,4,5]),(10,vec![2,4,4,5]),(10,vec![3,3,4,4]),
        (20,vec![3,3,4,5]),(10,vec![3,4,4,5]),
    ];
    let profiles4=vec![
        (4,vec![2,2,4]),(4,vec![2,3,3]),(16,vec![2,3,4]),(4,vec![3,3,4]),
    ];
    let (expression,numeric_c)=exact_integral(5,&profiles5);
    let (expression4,numeric_c4)=exact_integral(4,&profiles4);
    let source6:Value=serde_json::from_str(
        &fs::read_to_string("../results/six-cycle-ofpt-packet.json").unwrap()
    ).unwrap();
    let mut profile_counts=BTreeMap::<Vec<usize>,i64>::new();
    for term in source6["six_cycle"]["terms"].as_array().unwrap() {
        let mut profile=term.as_array().unwrap().iter().map(|label|{
            let label=label.as_str().unwrap();
            label.strip_prefix("g_").map(str::len).unwrap_or_else(||{
                assert!(label.starts_with("G_minus_e"));
                6
            })
        }).collect::<Vec<_>>();
        profile.sort_unstable();
        *profile_counts.entry(profile).or_default()+=1;
    }
    assert_eq!(profile_counts.values().sum::<i64>(),1476);
    let profiles6=profile_counts.iter().map(|(p,c)|(*c,p.clone())).collect::<Vec<_>>();
    let (expression6,numeric_c6)=exact_integral(6,&profiles6);
    let packet6=json!({
        "schema":"marici.benincasa.six_site.asymmetric.infinity_constant_exact.v1",
        "source_term_count":1476,
        "profile_count":profile_counts.len(),
        "profile_counts":profile_counts.into_iter().map(|(sizes,count)|json!({"sizes":sizes,"count":count})).collect::<Vec<_>>(),
        "radial_integral_exact":expression6,
        "constant_exact":format!("4*pi*({expression6})"),
        "constant_numeric_f64_evaluation":numeric_c6,
        "numeric_scope":"The direct f64 evaluation is diagnostic only because the exact summands cancel strongly; use the independent quadrature packet for numerical evaluation.",
        "simple_pole_sum_zero":true,
        "scope":"Exact rational partial-fraction evaluation of the source-derived six-cycle positive-sheet exceptional period."
    });
    fs::write("../results/six-site-asymmetric-infinity-constant-exact.json",serde_json::to_string_pretty(&packet6).unwrap()+"\n").unwrap();
    let packet=json!({
        "schema":"marici.benincasa.five_site.asymmetric.infinity_constant_exact.v1",
        "radial_integral_exact":expression,
        "constant_exact":format!("4*pi*({expression})"),
        "constant_numeric":numeric_c,
        "agrees_with_quadrature":(numeric_c-0.01131604369562018_f64).abs()<1e-14,
        "four_cycle_constant_exact":format!("4*pi*({expression4})"),
        "four_cycle_constant_numeric":numeric_c4,
        "ratio_C5_over_C4":numeric_c/numeric_c4,
        "simple_pole_sum_zero":true,
        "scope":"Exact rational partial-fraction evaluation of the coalesced-focus radial integral."
    });
    fs::write("../results/five-site-asymmetric-infinity-constant-exact.json",serde_json::to_string_pretty(&packet).unwrap()+"\n").unwrap();
    println!("I={expression}");
    println!("C=4*pi*({expression})");
    println!("C_numeric={numeric_c:.17}");
    println!("C4=4*pi*({expression4})");
    println!("C4_numeric={numeric_c4:.17}");
    println!("C5_over_C4={:.17}",numeric_c/numeric_c4);
    println!("C6=4*pi*({expression6})");
    println!("C6_numeric_f64_diagnostic={numeric_c6:.17}");
}
