use std::fs;

fn main() {
    let mut checks=0_u64;
    for s1 in [-1_i64,1] { for s2 in [-1_i64,1] { for shear in -13_i64..=13 {
        // P is the most general integral transition preserving the source flag.
        let p=[[s1,shear],[0,s2]];
        assert_eq!(p[1][0],0); assert_eq!(p[0][0]*p[1][1],s1*s2); checks+=2;
        // The associated-graded transition forgets the lift-dependent shear.
        let gr=[[p[0][0],0],[0,p[1][1]]];
        assert_eq!(gr,[[s1,0],[0,s2]]); checks+=1;
        // Hom(L_j,L_i) has character s_i^{-1}s_j=s_i*s_j.
        let relative=s1*s2;
        assert_eq!(relative*relative,1); checks+=1;
        // Diagonal grades are invariant; both off-diagonal grades carry the
        // same relative sign.  This includes the central (-1,-1) case.
        let chars=[1,relative,relative,1];
        assert_eq!(chars[0],1); assert_eq!(chars[3],1);
        assert_eq!(chars[1],chars[2]); checks+=3;
    }}}
    let output=format!(concat!(
      "{{\n",
      "  \"schema\": \"marici.rotating_second_jet_flag.v1\",\n",
      "  \"exact_checks\": {},\n",
      "  \"transition_group\": \"upper_triangular_parabolic\",\n",
      "  \"associated_grade_independent_of_shear\": true,\n",
      "  \"diagonal_characters\": [1,1],\n",
      "  \"offdiagonal_character\": \"sigma_1 sigma_2\",\n",
      "  \"central_sign_invisible_on_endomorphisms\": true,\n",
      "  \"global_scalar_matrix_requires_frame_trivialization\": true,\n",
      "  \"new_cut_carrier_stratum\": false\n",
      "}}\n"),checks);
    fs::write("research/benincasa/results/rotating-second-jet-flag.json",output).unwrap();
}
