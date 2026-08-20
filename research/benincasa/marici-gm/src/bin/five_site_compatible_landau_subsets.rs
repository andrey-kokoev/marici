use serde_json::{json,Value};
use std::{collections::{BTreeMap,BTreeSet},fs};

fn rotate(label:&str,shift:usize)->String{
    if label=="G"{return "G".to_owned();}
    if let Some(edge)=label.strip_prefix("G_minus_e"){
        let digits=edge.chars().map(|c|c.to_digit(10).unwrap() as usize-1).map(|i|(i+shift)%5+1).collect::<Vec<_>>();
        return format!("G_minus_e{}{}",digits[0],digits[1]);
    }
    let mut sites=label.strip_prefix("g_").unwrap().chars().map(|c|c.to_digit(10).unwrap() as usize-1).map(|i|(i+shift)%5+1).collect::<Vec<_>>();
    sites.sort();format!("g_{}",sites.iter().map(|i|i.to_string()).collect::<String>())
}

fn canonical_orbit(labels:&[String])->String{
    (0..5).map(|shift|{
        let mut image=labels.iter().map(|label|rotate(label,shift)).collect::<Vec<_>>();image.sort();image.join("|")
    }).min().unwrap()
}

fn cut_support(label:&str)->Vec<usize>{
    if label=="G"{return vec![];}
    if let Some(edge)=label.strip_prefix("G_minus_e"){
        return vec![edge.chars().next().unwrap().to_digit(10).unwrap() as usize-1];
    }
    let sites=label.strip_prefix("g_").unwrap().chars().map(|c|c.to_digit(10).unwrap() as usize-1).collect::<BTreeSet<_>>();
    (0..5).filter(|edge|sites.contains(edge)!=sites.contains(&((edge+1)%5))).collect()
}

fn descriptor(label:&str)->String{
    if label=="G"{"T".to_owned()}
    else if label.starts_with("G_minus_e"){"M1".to_owned()}
    else{format!("A{}",label.strip_prefix("g_").unwrap().len())}
}

fn profile(labels:&[String])->String{
    let mut kinds=labels.iter().map(|label|descriptor(label)).collect::<Vec<_>>();kinds.sort();
    let supports=labels.iter().map(|label|cut_support(label).into_iter().collect::<BTreeSet<_>>()).collect::<Vec<_>>();
    let mut intersections=Vec::new();
    for i in 0..supports.len(){for j in i+1..supports.len(){intersections.push(supports[i].intersection(&supports[j]).count());}}
    intersections.sort();format!("{};cut_intersections={:?}",kinds.join("+"),intersections)
}

fn subsets(labels:&[String],size:usize)->Vec<Vec<String>>{
    fn rec(labels:&[String],size:usize,start:usize,current:&mut Vec<String>,out:&mut Vec<Vec<String>>){
        if current.len()==size{let mut value=current.clone();value.sort();out.push(value);return;}
        for index in start..labels.len(){current.push(labels[index].clone());rec(labels,size,index+1,current,out);current.pop();}
    }
    let mut out=Vec::new();rec(labels,size,0,&mut Vec::new(),&mut out);out
}

fn main(){
    let source:Value=serde_json::from_str(&fs::read_to_string("../results/five-cycle-ofpt-packet.json").unwrap()).unwrap();
    let cycle=&source["five_cycle"];
    let common=cycle["common_prefactor"].as_array().unwrap().iter().map(|x|x.as_str().unwrap().to_owned()).collect::<Vec<_>>();
    let mut packets=Vec::new();
    for size in [2_usize,3_usize]{
        let mut multiplicities=BTreeMap::<Vec<String>,usize>::new();
        for term in cycle["terms"].as_array().unwrap(){
            let mut labels=common.clone();labels.extend(term.as_array().unwrap().iter().map(|x|x.as_str().unwrap().to_owned()));
            assert_eq!(labels.len(),10);
            for subset in subsets(&labels,size){*multiplicities.entry(subset).or_default()+=1;}
        }
        let mut orbits=BTreeMap::<String,Vec<Vec<String>>>::new();
        let mut profiles=BTreeMap::<String,usize>::new();
        let mut term_multiplicity=BTreeMap::<usize,usize>::new();
        for (labels,count) in &multiplicities{
            orbits.entry(canonical_orbit(labels)).or_default().push(labels.clone());
            *profiles.entry(profile(labels)).or_default()+=1;
            *term_multiplicity.entry(*count).or_default()+=1;
        }
        assert!(orbits.values().all(|orbit|orbit.len()==1||orbit.len()==5));
        let fixed_orbits=orbits.values().filter(|orbit|orbit.len()==1).count();
        let free_orbits=orbits.values().filter(|orbit|orbit.len()==5).count();
        let representative_records=orbits.iter().map(|(canonical,orbit)|{
            let representative=&orbit[0];
            let supports=representative.iter().map(|label|cut_support(label)).collect::<Vec<_>>();
            let contains_total_energy=representative.iter().any(|label|label=="G");
            let complementary_same_cut=size==2
                && representative.iter().all(|label|label.starts_with("g_"))
                && supports[0].len()==2
                && supports[0]==supports[1];
            json!({
                "canonical_orbit":canonical,
                "representative":representative,
                "profile":profile(representative),
                "cut_supports":supports,
                "source_term_multiplicity":multiplicities[representative],
                "forces_t_zero":contains_total_energy || complementary_same_cut,
                "t_zero_reason":if contains_total_energy {
                    "contains total-energy wall G=5t"
                } else if complementary_same_cut {
                    "distinct connected regions have the same cut sum and unequal cardinalities"
                } else {
                    "not eliminated by the first algebraic gate"
                }
            })
        }).collect::<Vec<_>>();
        packets.push(json!({
            "active_wall_count":size,
            "unique_compatible_subsets":multiplicities.len(),
            "fixed_C5_orbits":fixed_orbits,
            "free_C5_orbits":free_orbits,
            "term_multiplicity_distribution":term_multiplicity,
            "coarse_profile_counts":profiles,
            "orbit_representatives":orbits.keys().collect::<Vec<_>>(),
            "representative_records":representative_records
        }));
    }
    let packet=json!({
        "schema":"marici.benincasa.five_site.compatible_landau_subsets.v1",
        "source_terms":180,
        "walls_per_term":10,
        "rule":"An active Landau set is admitted only when all its labelled walls co-occur in at least one frozen OFPT term.",
        "census":packets,
        "status":"finite source-derived representative list for pair/triple Landau elimination",
        "no_landau_solution_claim":true
    });
    fs::write("../results/five-site-compatible-landau-subsets.json",serde_json::to_string_pretty(&packet).unwrap()+"\n").unwrap();
    println!("wrote five-site-compatible-landau-subsets.json");
}
