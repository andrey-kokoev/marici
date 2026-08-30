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

fn reflect(label:&str)->String{
    if label=="G"{return "G".to_owned();}
    let reflect_site=|site:usize|->usize{(5-site)%5};
    if let Some(edge)=label.strip_prefix("G_minus_e"){
        let digits=edge.chars().map(|c|c.to_digit(10).unwrap() as usize-1).collect::<Vec<_>>();
        let mut left=reflect_site(digits[0]);let mut right=reflect_site(digits[1]);
        if (left+1)%5!=right{std::mem::swap(&mut left,&mut right);}
        assert_eq!((left+1)%5,right);
        return format!("G_minus_e{}{}",left+1,right+1);
    }
    let mut sites=label.strip_prefix("g_").unwrap().chars()
        .map(|c|reflect_site(c.to_digit(10).unwrap() as usize-1)+1).collect::<Vec<_>>();
    sites.sort();format!("g_{}",sites.iter().map(|i|i.to_string()).collect::<String>())
}

fn canonical_dihedral_orbit(labels:&[String])->String{
    let reflected=labels.iter().map(|label|reflect(label)).collect::<Vec<_>>();
    canonical_orbit(labels).min(canonical_orbit(&reflected))
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

fn forces_t_zero(labels:&[String])->bool{
    if labels.iter().any(|label|label=="G"){return true;}
    for left in 0..labels.len(){for right in left+1..labels.len(){
        if labels[left].starts_with("g_") && labels[right].starts_with("g_")
            && cut_support(&labels[left])==cut_support(&labels[right])
            && labels[left].strip_prefix("g_").unwrap().len()!=labels[right].strip_prefix("g_").unwrap().len()
        {return true;}
    }}
    false
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
        let mut dihedral_orbits=BTreeMap::<String,BTreeSet<String>>::new();
        let mut profiles=BTreeMap::<String,usize>::new();
        let mut term_multiplicity=BTreeMap::<usize,usize>::new();
        for (labels,count) in &multiplicities{
            let cyclic=canonical_orbit(labels);
            orbits.entry(cyclic.clone()).or_default().push(labels.clone());
            dihedral_orbits.entry(canonical_dihedral_orbit(labels)).or_default().insert(cyclic);
            *profiles.entry(profile(labels)).or_default()+=1;
            *term_multiplicity.entry(*count).or_default()+=1;
        }
        assert!(orbits.values().all(|orbit|orbit.len()==1||orbit.len()==5));
        let fixed_orbits=orbits.values().filter(|orbit|orbit.len()==1).count();
        let free_orbits=orbits.values().filter(|orbit|orbit.len()==5).count();
        assert!(dihedral_orbits.values().all(|cyclic_orbits|cyclic_orbits.len()==1||cyclic_orbits.len()==2));
        let reflection_fixed_dihedral_orbits=dihedral_orbits.values().filter(|cyclic_orbits|cyclic_orbits.len()==1).count();
        let reflection_paired_dihedral_orbits=dihedral_orbits.values().filter(|cyclic_orbits|cyclic_orbits.len()==2).count();
        let forced_zero_cyclic_orbits=orbits.keys().filter(|canonical|forces_t_zero(&canonical.split('|').map(str::to_owned).collect::<Vec<_>>())).count();
        let forced_zero_dihedral_orbits=dihedral_orbits.keys().filter(|canonical|forces_t_zero(&canonical.split('|').map(str::to_owned).collect::<Vec<_>>())).count();
        let mut nonzero_dihedral_profile_counts=BTreeMap::<String,usize>::new();
        let mut nonzero_dihedral_representatives=Vec::new();
        for canonical in dihedral_orbits.keys(){
            let labels=canonical.split('|').map(str::to_owned).collect::<Vec<_>>();
            if !forces_t_zero(&labels){
                *nonzero_dihedral_profile_counts.entry(profile(&labels)).or_default()+=1;
                nonzero_dihedral_representatives.push(canonical.clone());
            }
        }
        let representative_records=orbits.iter().map(|(canonical,orbit)|{
            let representative=&orbit[0];
            let supports=representative.iter().map(|label|cut_support(label)).collect::<Vec<_>>();
            let contains_total_energy=representative.iter().any(|label|label=="G");
            let complementary_same_cut=representative.iter().enumerate().any(|(left,left_label)|
                representative.iter().enumerate().skip(left+1).any(|(_,right_label)|
                    left_label.starts_with("g_") && right_label.starts_with("g_")
                    && cut_support(left_label)==cut_support(right_label)
                    && left_label.strip_prefix("g_").unwrap().len()!=right_label.strip_prefix("g_").unwrap().len()));
            json!({
                "canonical_orbit":canonical,
                "representative":representative,
                "profile":profile(representative),
                "cut_supports":supports,
                "source_term_multiplicity":multiplicities[representative],
                "forces_t_zero":forces_t_zero(representative),
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
            "D5_orbits":dihedral_orbits.len(),
            "reflection_fixed_D5_orbits":reflection_fixed_dihedral_orbits,
            "reflection_paired_D5_orbits":reflection_paired_dihedral_orbits,
            "forced_t_zero_C5_orbits":forced_zero_cyclic_orbits,
            "nonzero_candidate_C5_orbits":orbits.len()-forced_zero_cyclic_orbits,
            "forced_t_zero_D5_orbits":forced_zero_dihedral_orbits,
            "nonzero_candidate_D5_orbits":dihedral_orbits.len()-forced_zero_dihedral_orbits,
            "nonzero_D5_profile_counts":nonzero_dihedral_profile_counts,
            "nonzero_D5_representatives":nonzero_dihedral_representatives,
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
