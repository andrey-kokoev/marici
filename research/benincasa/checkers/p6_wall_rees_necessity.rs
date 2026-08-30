use std::fs;

fn main(){
    // Quotient coordinates: bit 0=top, bit 1=wall1, bit 2=wall2.
    let d_mask=5_u8; // 101: wall1 is lost.
    let h_mask=3_u8; // 011: wall2 is lost.
    let d_resonant_bit=1_u8;
    let h_resonant_bit=2_u8;
    let d_resonant_fixed=(d_mask&(1<<d_resonant_bit))!=0;
    let h_resonant_fixed=(h_mask&(1<<h_resonant_bit))!=0;
    assert!(!d_resonant_fixed&&!h_resonant_fixed);
    let packet=format!(concat!(
        "{{\n",
        "  \"schema\": \"marici.p6_wall_rees_necessity.v1\",\n",
        "  \"quotient_order\": [\"top\",\"wall1\",\"wall2\"],\n",
        "  \"D_fixed_mask\": 5,\n",
        "  \"D_resonant_direction\": \"wall1\",\n",
        "  \"D_resonant_direction_fixed\": {},\n",
        "  \"H_fixed_mask\": 3,\n",
        "  \"H_resonant_direction\": \"wall2\",\n",
        "  \"H_resonant_direction_fixed\": {},\n",
        "  \"ordinary_specialization_sufficient\": false,\n",
        "  \"required_object\": \"two-normal labelled Rees lift of the complete source system\"\n",
        "}}\n"),d_resonant_fixed,h_resonant_fixed);
    fs::write("research/benincasa/results/p6-wall-rees-necessity.json",packet)
        .expect("write result packet");
}
