use serde_json::json;
use std::{collections::BTreeMap,fs};
use symbolica::prelude::*;

fn atom(text:&str)->Atom{Atom::parse(text,"marici",Default::default()).unwrap().expand()}
fn scalar_sign(expression:&Atom,z:&str,s:&str)->i8{
    let value=expression.clone().replace(atom("5^(1/2)").to_pattern()).with(atom(s).to_pattern())
        .replace(atom("z").to_pattern()).with(atom(z).to_pattern()).together().cancel().expand().to_string();
    if value=="0"{0}else if value.starts_with('-'){-1}else{1}
}
fn positive_on_box(expression:&Atom,left:&str,right:&str)->bool{
    [left,right].iter().flat_map(|z|["2236067977/1000000000","2236067978/1000000000"].iter()
        .map(move|s|scalar_sign(expression,z,s))).all(|sign|sign>0)
}

fn wall_sign(label:&str)->i8{
    // On the certified D4 box: t=-T, T>0,
    // 19/10 < y1/T < 2 and 1 < y3/T < 11/10,
    // while (y2,y4,y5)/T=(3/2,1/2,1/2).
    match label {
        "G" => -1,
        "g_1"|"g_2"|"g_3"|"g_4" => 1,
        "g_12"|"g_34"|"g_5" => 0,
        "G_minus_e23"|"G_minus_e45"|"G_minus_e51"|"g_125"|"g_345"|"g_1234" => -1,
        _=>panic!("unexpected D4 source wall {label}"),
    }
}

fn run(){
    let source:serde_json::Value=serde_json::from_str(&fs::read_to_string("../results/five-cycle-ofpt-packet.json").unwrap()).unwrap();
    let census:serde_json::Value=serde_json::from_str(&fs::read_to_string("../results/five-site-cyclic-triple-region-census.json").unwrap()).unwrap();
    let roots:serde_json::Value=serde_json::from_str(&fs::read_to_string("../results/five-site-cyclic-triple-region-real-roots.json").unwrap()).unwrap();
    let record=census["records"].as_array().unwrap().iter().find(|record|record["representative"]=="g_12|g_34|g_5").unwrap();
    let root=roots["records"].as_array().unwrap().iter().find(|record|record["representative"]=="g_12|g_34|g_5").unwrap()["refined_branch_and_square_signs"]
        .as_array().unwrap().iter().find(|root|root["common_nonzero_wall_multiplier_sign"]==true).unwrap();
    let left=root["left"].as_str().unwrap();let right=root["right"].as_str().unwrap();
    let x=atom(record["repeated_critical_squares"]["first_free_y_squared"].as_str().unwrap());
    let v=atom(record["repeated_critical_squares"]["second_free_y_squared"].as_str().unwrap());
    assert!(positive_on_box(&(x.clone()/atom("z")-atom("361/100")).together().cancel().expand(),left,right));
    assert!(positive_on_box(&(atom("4")-x/atom("z")).together().cancel().expand(),left,right));
    assert!(positive_on_box(&(v.clone()/atom("z")-atom("1")).together().cancel().expand(),left,right));
    assert!(positive_on_box(&(atom("121/100")-v/atom("z")).together().cancel().expand(),left,right));
    let common=source["five_cycle"]["common_prefactor"].as_array().unwrap();
    let active=["g_12","g_34","g_5"];
    let mut terms=Vec::new();
    for (index,term) in source["five_cycle"]["terms"].as_array().unwrap().iter().enumerate(){
        let walls=common.iter().chain(term.as_array().unwrap()).map(|value|value.as_str().unwrap()).collect::<Vec<_>>();
        if active.iter().all(|active|walls.contains(active)){
            let uncut=walls.iter().filter(|wall|!active.contains(wall)).copied().collect::<Vec<_>>();
            assert!(uncut.iter().all(|wall|wall_sign(wall)!=0));
            let residue_sign=uncut.iter().map(|wall|wall_sign(wall)).product::<i8>();
            terms.push(json!({"source_term_index":index,"uncut_walls":uncut,"uncut_wall_signs":uncut.iter().map(|wall|wall_sign(wall)).collect::<Vec<_>>(),"local_residue_sign":residue_sign}));
        }
    }
    assert_eq!(terms.len(),8);
    assert!(terms.iter().all(|term|term["local_residue_sign"]==-1));
    let packet=json!({
        "schema":"marici.five_site_cyclic_triple_d4_source_residue.v1",
        "representative":"g_12|g_34|g_5",
        "certified_positive_sheet_box":{"t_sign":-1,"y1_over_minus_t":["19/10","2"],"y3_over_minus_t":["1","11/10"],"fixed_y_over_minus_t":[null,"3/2",null,"1/2","1/2"]},
        "active_walls":active,
        "source_term_count":terms.len(),
        "source_terms":terms,
        "common_local_residue_sign":-1,
        "termwise_cancellation_possible":false,
        "scope":"uncut source-denominator coefficient only; Cayley-Menger measure orientation and global contour intersection remain separate"
    });
    fs::write("../results/five-site-cyclic-triple-d4-source-residue.json",serde_json::to_string_pretty(&packet).unwrap()+"\n").unwrap();
    let mut counts=BTreeMap::new();for term in packet["source_terms"].as_array().unwrap(){*counts.entry(term["local_residue_sign"].as_i64().unwrap()).or_insert(0usize)+=1;}
    println!("{}",json!({"source_term_count":8,"residue_sign_counts":counts,"termwise_cancellation_possible":false}));
}

fn main(){
    std::thread::Builder::new().name("d4-source-residue".into()).stack_size(32*1024*1024)
        .spawn(run).unwrap().join().unwrap();
}
