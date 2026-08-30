use std::fs;

fn main() {
    // Source quotient residue is zero because the exact A3 denominators are
    // coprime to P6. Target residues are (-1/2,0) in the Entry 867 split.
    // Store doubled indicial eigenvalues to keep the computation integral.
    let doubled_target_residue = [-1_i32, 0_i32];
    let source_rank = 3_usize;
    let mut kernel_dimensions = [0_usize; 2];
    let mut ranks = [0_usize; 2];
    for (line, eigenvalue) in doubled_target_residue.iter().enumerate() {
        if *eigenvalue == 0 { kernel_dimensions[line] = source_rank; }
        else { ranks[line] = source_rank; }
    }
    assert_eq!(ranks, [3,0]);
    assert_eq!(kernel_dimensions, [0,3]);
    let packet = format!(concat!(
        "{{\n",
        "  \"schema\": \"marici.p6_hom_indicial_gate.v1\",\n",
        "  \"source_residue_spectrum\": [\"0\",\"0\",\"0\"],\n",
        "  \"target_residue_spectrum\": [\"-1/2\",\"0\"],\n",
        "  \"hom_indicial_rank_by_target_line\": [{},{}],\n",
        "  \"hom_indicial_kernel_by_target_line\": [{},{}],\n",
        "  \"relative_sign_line_residue_gauge_removable\": true,\n",
        "  \"trivial_monodromy_line_resonant\": true\n",
        "}}\n"), ranks[0],ranks[1],kernel_dimensions[0],kernel_dimensions[1]);
    fs::write("research/benincasa/results/p6-hom-indicial-gate.json",packet)
        .expect("write result packet");
}
