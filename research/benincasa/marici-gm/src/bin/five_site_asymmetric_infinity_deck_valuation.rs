use serde_json::{json,Value};
use std::{collections::BTreeSet,fs};

fn mm(a:i64,b:i64,p:i64)->i64{((a as i128*b as i128)%p as i128)as i64}
fn mp(mut a:i64,mut n:i64,p:i64)->i64{let mut r=1;while n>0{if n&1==1{r=mm(r,a,p);}a=mm(a,a,p);n>>=1;}r}
fn mi(a:i64,p:i64)->i64{mp(a.rem_euclid(p),p-2,p)}
fn ms(a:i64,p:i64)->Option<i64>{let a=a.rem_euclid(p);(1..p).find(|x|mm(*x,*x,p)==a)}

fn cuts(label:&str)->Vec<usize>{
    let sites=label.strip_prefix("g_").unwrap().chars()
        .map(|d|d.to_digit(10).unwrap()as usize-1).collect::<BTreeSet<_>>();
    (0..5).filter(|e|sites.contains(e)!=sites.contains(&((e+1)%5))).collect()
}
fn grows(label:&str,mask:usize)->usize{
    if label=="G"{return 0}
    if label.starts_with("G_minus_e"){return 1}
    let c=cuts(label);assert_eq!(c.len(),2);
    usize::from(((mask>>c[0])&1)==((mask>>c[1])&1))
}
fn leading_wall(label:&str,mask:usize,z:i64,r:i64,c:&[i64;5],p:i64)->(usize,i64){
    if label=="G"{return(0,(5*z).rem_euclid(p))}
    if let Some(edge)=label.strip_prefix("G_minus_e"){
        let e=edge.chars().next().unwrap().to_digit(10).unwrap()as usize-1;
        let sign=if(mask>>e)&1==0{1}else{-1};return(1,(2*sign*r).rem_euclid(p))
    }
    let cut=cuts(label);let sa=if(mask>>cut[0])&1==0{1}else{-1};let sb=if(mask>>cut[1])&1==0{1}else{-1};
    if sa==sb{(1,((sa+sb)*r).rem_euclid(p))}else{
        let size=label.strip_prefix("g_").unwrap().len()as i64;
        (0,(sa*c[cut[0]]+sb*c[cut[1]]+size*z).rem_euclid(p))
    }
}
fn leading_audit(prime:i64,z:i64,common:&[String],terms:&[Vec<String>])->Value{
    let (v,r)=(1_i64..prime).find_map(|a|{let v=[(3*a+2)%prime,(5*a+3)%prime,(7*a+5)%prime];
        let f=(2*v[0]*v[0]+2*v[1]*v[1]+v[2]*v[2]-2*v[0]*v[1]-2*v[1]*v[2]).rem_euclid(prime);
        ms(f,prime).map(|r|(v,r))}).unwrap();
    let linear=[0,-2*v[0],-2*v[1],-2*v[2],2*v[0]+2*v[1]-8*v[2]];
    let c=linear.map(|x|mm(x.rem_euclid(prime),mi(2*r,prime),prime));
    let rows=(0_usize..32).map(|mask|{
        let data=terms.iter().map(|term|{let mut order=0;let mut coeff=1;
            for label in common.iter().chain(term){let (o,q)=leading_wall(label,mask,z,r,&c,prime);order+=o;coeff=mm(coeff,q,prime);}
            (order,mi(coeff,prime))}).collect::<Vec<_>>();
        let min=data.iter().map(|x|x.0).min().unwrap();let sum=data.iter().filter(|x|x.0==min).fold(0_i64,|a,x|(a+x.1).rem_euclid(prime));
        json!({"mask":mask,"minimum_growth":min,"leading_sum":sum,"leading_cancels":sum==0})
    }).collect::<Vec<_>>();
    json!({"prime":prime,"z":z,"direction":v,"root_leading":r,"rows":rows})
}
fn main(){
    let source:Value=serde_json::from_str(&fs::read_to_string("../results/five-cycle-ofpt-packet.json").unwrap()).unwrap();
    let cycle=&source["five_cycle"];
    let common=cycle["common_prefactor"].as_array().unwrap().iter().map(|x|x.as_str().unwrap().to_owned()).collect::<Vec<_>>();
    let terms=cycle["terms"].as_array().unwrap().iter().map(|t|t.as_array().unwrap().iter().map(|x|x.as_str().unwrap().to_owned()).collect()).collect::<Vec<Vec<String>>>();
    let rows=(0_usize..32).map(|mask|{
        let valuations=terms.iter().map(|term|common.iter().chain(term).map(|label|grows(label,mask)).sum::<usize>()).collect::<Vec<_>>();
        let minimum=*valuations.iter().min().unwrap();let maximum=*valuations.iter().max().unwrap();
        json!({"mask":mask,"hamming_weight":mask.count_ones(),"minimum_denominator_growth":minimum,
            "maximum_denominator_growth":maximum,"terms_at_minimum":valuations.iter().filter(|v|**v==minimum).count(),
            "valuation_histogram":(minimum..=maximum).map(|v|json!({"growth":v,"terms":valuations.iter().filter(|x|**x==v).count()})).collect::<Vec<_>>()})
    }).collect::<Vec<_>>();
    let audits=[leading_audit(1009,7,&common,&terms),leading_audit(1013,11,&common,&terms)];
    let packet=json!({"schema":"marici.benincasa.five_site.asymmetric.infinity_deck_valuation.v1",
        "scaling":"u_i=R v_i with generic v; all five roots have common leading magnitude and labelled deck signs",
        "rule":{"G":0,"G_minus_e":1,"g_A":"1 iff its two cut-edge signs agree; 0 iff they cancel"},
        "warning":"termwise minimum is a lower bound on canonical-sum decay until leading cancellation is audited",
        "rows":rows,"leading_coefficient_audits":audits});
    fs::write("../results/five-site-asymmetric-infinity-deck-valuation.json",serde_json::to_string_pretty(&packet).unwrap()+"\n").unwrap();
    println!("{}",serde_json::to_string(&packet["rows"]).unwrap());
}
