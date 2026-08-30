use std::fs;

fn main() {
    // Doubled residues on an ordinary exceptional divisor over a transverse
    // P6-(D or H) crossing. Target algebraic lines: (-1,0). Source marked
    // quotient: (0,0,-1), from Entries 864 and 874.
    let target = [-1_i8,0_i8];
    let source = [0_i8,0_i8,-1_i8];
    let mut zero_pairs=Vec::new();
    for (ti,t) in target.iter().enumerate(){for(si,s)in source.iter().enumerate(){
        if t-s==0{zero_pairs.push((ti,si));}
    }}
    assert_eq!(zero_pairs,vec![(0,2),(1,0),(1,1)]);
    let relative_sign_slots=zero_pairs.iter().filter(|(t,_)|*t==0).count();
    assert_eq!(relative_sign_slots,1);
    let packet=format!(concat!(
        "{{\n",
        "  \"schema\": \"marici.p6_wall_exceptional_indicial.v1\",\n",
        "  \"doubled_target_residues\": [-1,0],\n",
        "  \"doubled_source_residues\": [0,0,-1],\n",
        "  \"zero_indicial_pairs\": [[0,2],[1,0],[1,1]],\n",
        "  \"relative_sign_line_slots\": {},\n",
        "  \"total_zero_exponent_slots\": {},\n",
        "  \"actual_extension_class_computed\": false\n",
        "}}\n"),relative_sign_slots,zero_pairs.len());
    fs::write("research/benincasa/results/p6-wall-exceptional-indicial.json",packet)
        .expect("write result packet");
}
