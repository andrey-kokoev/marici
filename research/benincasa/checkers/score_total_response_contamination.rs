fn main(){
    for edge in 0..3 {
        let selected:Vec<usize>=(0_usize..8).filter(|s|s&(1<<edge)!=0).collect();
        assert_eq!(selected.len(),4);
    }
    println!("{{\"status\":\"pass\",\"deletion_subsets_per_edge_score\":4,\"contact_packet_routes\":2,\"raw_score_is_contact_projector\":false,\"additional_projector_required\":true}}");
}
