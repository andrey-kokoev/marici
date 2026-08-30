use serde_json::{json,Value};
use std::{collections::BTreeSet,fs};

fn add(a:i64,b:i64,p:i64)->i64{(a+b).rem_euclid(p)}
fn mul(a:i64,b:i64,p:i64)->i64{((a as i128*b as i128)%p as i128)as i64}
fn pow(mut a:i64,mut n:usize,p:i64)->i64{let mut r=1;while n>0{if n&1==1{r=mul(r,a,p);}a=mul(a,a,p);n>>=1;}r}
fn inv(a:i64,p:i64)->i64{pow(a.rem_euclid(p),(p-2)as usize,p)}

fn cut_support(label:&str)->Vec<usize>{
    let sites=label.strip_prefix("g_").unwrap().chars().map(|d|d.to_digit(10).unwrap()as usize).collect::<BTreeSet<_>>();
    (1..=5).filter(|e|sites.contains(e)!=sites.contains(&(e%5+1))).collect()
}
fn grows(label:&str,mask:usize)->usize{if label=="G"{0}else if label.starts_with("G_minus_e"){1}else{
    let c=cut_support(label);usize::from(((mask>>(c[0]-1))&1)==((mask>>(c[1]-1))&1))}}
fn rotate5(mask:usize)->usize{((mask<<1)&31)|(mask>>4)}
fn orbit_rep(mut mask:usize)->usize{let mut rep=mask;for _ in 1..5{mask=rotate5(mask);rep=rep.min(mask);}rep}
fn radial_constant(label:&str,sheet:usize,r:&[i64;5],p:i64)->i64{
    if let Some(edge)=label.strip_prefix("G_minus_e"){let e=edge.chars().next().unwrap().to_digit(10).unwrap()as usize-1;let sign=if sheet&(1<<e)==0{1}else{-1};return mul(2*sign,r[e],p);}
    let cut=cut_support(label);cut.into_iter().fold(0_i64,|out,e|{let i=e-1;let sign=if sheet&(1<<i)==0{1}else{-1};add(out,mul(sign,r[i],p),p)})
}
fn uniform_leading(terms:&[Vec<String>],common:&[String],sheet:usize,r:&[i64;5],p:i64)->i64{
    let mut out=0;for term in terms{let mut product=5_i64;for label in common.iter().chain(term){if label=="G"{continue;}let c=radial_constant(label,sheet,r,p);assert_ne!(c,0);product=mul(product,c,p);}out=add(out,inv(product,p),p);}out
}
fn wall_packet(label:&str)->Value{
    if label=="G"{return json!({"label":label,"cleared_numerator":"5*w","blowup_order":1,"exceptional_linear_form":"5*tau"});}
    if let Some(edge)=label.strip_prefix("G_minus_e"){
        return json!({"label":label,"cleared_numerator":format!("5*w+2*x*r_{edge}"),"blowup_order":1,"exceptional_linear_form":format!("5*tau+2*r_{edge}")});
    }
    let size=label.strip_prefix("g_").unwrap().len();let cut=cut_support(label);
    json!({"label":label,"cleared_numerator":format!("{size}*w+x*(r_{}+r_{})",cut[0],cut[1]),"blowup_order":1,
        "exceptional_linear_form":format!("{size}*tau+r_{}+r_{}",cut[0],cut[1])})
}
fn main(){
    let source:Value=serde_json::from_str(&fs::read_to_string("../results/five-cycle-ofpt-packet.json").unwrap()).unwrap();let cycle=&source["five_cycle"];
    let common=cycle["common_prefactor"].as_array().unwrap().iter().map(|x|x.as_str().unwrap().to_owned()).collect::<Vec<_>>();
    let terms=cycle["terms"].as_array().unwrap().iter().map(|t|t.as_array().unwrap().iter().map(|x|x.as_str().unwrap().to_owned()).collect::<Vec<_>>()).collect::<Vec<Vec<String>>>();
    let labels=common.iter().chain(terms.iter().flatten()).cloned().collect::<BTreeSet<_>>();let walls=labels.iter().map(|q|wall_packet(q)).collect::<Vec<_>>();
    let term_denominator_counts=terms.iter().map(|t|common.len()+t.len()).collect::<BTreeSet<_>>();
    let sheet_orders=(0_usize..32).map(|sheet|{let order=terms.iter().map(|t|common.iter().chain(t).map(|q|grows(q,sheet)).sum::<usize>()).min().unwrap();
        json!({"sheet":sheet,"cyclic_orbit_rep":orbit_rep(sheet),"tau_vanishing_order":order})}).collect::<Vec<_>>();
    let mut order_histogram=std::collections::BTreeMap::<usize,usize>::new();for s in &sheet_orders{*order_histogram.entry(s["tau_vanishing_order"].as_u64().unwrap()as usize).or_default()+=1;}
    let complement_pairs=(0_usize..16).map(|sheet|{let complement=sheet^31;let order=sheet_orders[sheet]["tau_vanishing_order"].as_u64().unwrap()as usize;
        let complement_order=sheet_orders[complement]["tau_vanishing_order"].as_u64().unwrap()as usize;
        json!({"sheet":sheet,"complement":complement,"order":order,"complement_order":complement_order,"same_order":order==complement_order,
            "leading_coefficient_character":if order%2==0{"even"}else{"odd"}})}).collect::<Vec<_>>();
    let uniform_samples=[(1019_i64,[11_i64,23,37,41,53]),(1009_i64,[13_i64,29,31,43,59])].into_iter().map(|(p,r)|{let positive=uniform_leading(&terms,&common,0,&r,p);let negative=uniform_leading(&terms,&common,31,&r,p);
        json!({"prime":p,"radial_point":r,"positive_sheet":positive,"negative_sheet":negative,"exact_negatives":add(positive,negative,p)==0})}).collect::<Vec<_>>();
    let packet=json!({"schema":"marici.benincasa.five_site.two_normal_rees.v1","normals":{"x":"1/z","w":"1/R"},"blowup":"Bl_(x,w)",
        "exceptional_chart":"w=x*tau, so tau=z/R and R/z=tau^-1","wall_count":labels.len(),"walls":walls,"term_count":terms.len(),
        "term_denominator_counts":term_denominator_counts,"generic_exceptional_denominator_order_per_term":10,"physical_measure_order":-3,
        "physical_form_order_in_x":7,"tau_sheet_orders":sheet_orders,"tau_order_histogram":order_histogram,
        "deck_complement_pairs":complement_pairs,"all_complements_preserve_order":complement_pairs.iter().all(|x|x["same_order"]==true),
        "uniform_order_nine_samples":uniform_samples,"uniform_samples_are_exact_negatives":uniform_samples.iter().all(|x|x["exact_negatives"]==true),
        "all_walls_newton_linear":walls.iter().all(|w|w["blowup_order"]==1)});
    fs::write("../results/five-site-two-normal-rees.json",serde_json::to_string_pretty(&packet).unwrap()+"\n").unwrap();println!("{}",serde_json::to_string(&packet).unwrap());
}
