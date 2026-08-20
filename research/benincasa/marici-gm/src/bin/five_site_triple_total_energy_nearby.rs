use serde_json::{json,Value};
use std::{collections::BTreeMap,fs};

fn main(){
    let source:Value=serde_json::from_str(&fs::read_to_string("../results/five-site-triple-collision-cech.json").unwrap()).unwrap();
    let records=source["records"].as_array().unwrap();
    assert_eq!(records.len(),80);
    let mut before=BTreeMap::<usize,usize>::new();
    let mut after=BTreeMap::<usize,usize>::new();
    let mut newly_resonant=0_usize;
    let mut preexisting_relation=0_usize;
    for record in records{
        let rank=record["energy_rank"].as_u64().unwrap() as usize;
        let forces=record["forces_total_energy_zero"].as_bool().unwrap();
        *before.entry(3-rank).or_default()+=1;
        // In Q^5/<E>, rank is rank(rows,E)-1. If E is in the row span this
        // is rank-1; otherwise it remains rank. Both source profiles give 2.
        let quotient_rank=if forces{rank-1}else{rank};
        assert_eq!(quotient_rank,2);
        let relation_rank=3-quotient_rank;
        assert_eq!(relation_rank,1);
        *after.entry(relation_rank).or_default()+=1;
        if forces{newly_resonant+=1;}else{preexisting_relation+=1;}
    }
    assert_eq!(newly_resonant,50);
    assert_eq!(preexisting_relation,30);

    // The A2 incidence row is constant over the energy base and therefore
    // survives specialization unchanged.
    let row=source["pair_to_triple_cech_row"].as_array().unwrap().iter().map(|x|x.as_i64().unwrap()).collect::<Vec<_>>();
    assert_eq!(row,vec![1,-1,1]);
    let a2_kernel_rank=source["cech_kernel_rank"].as_u64().unwrap() as usize;
    assert_eq!(a2_kernel_rank,2);

    let packet=json!({
        "schema":"marici.benincasa.five_site.triple_total_energy_nearby.v1",
        "labelled_triples":80,
        "generic_energy_relation_nullity_counts":before,
        "after_ET_zero_relation_nullity_counts":after,
        "new_ET_induced_relation_count":newly_resonant,
        "preexisting_relation_count":preexisting_relation,
        "A2_cech_row":row,
        "A2_kernel_rank":a2_kernel_rank,
        "nearby_conormal_ranks_per_new_overlap":[1,1],
        "A2_tensor_nearby_ranks_per_new_overlap":[2,2],
        "total_new_nearby_ranks_across_50_overlaps":[100,100],
        "C5_assembly_per_nearby_degree":"20 copies of Q[C5]",
        "specialization_commutator":0,
        "ordinary_second_Rees_grade":"zero for this incidence subsystem because all source energy walls are linear",
        "classification":"canonical total-energy conormal nearby layer tensored with existing A2 marked-incidence kernel",
        "coefficient_excess":false,
        "new_carrier_datum":false
    });
    fs::write("../results/five-site-triple-total-energy-nearby.json",serde_json::to_string_pretty(&packet).unwrap()+"\n").unwrap();
    println!("{}",serde_json::to_string(&packet).unwrap());
}
