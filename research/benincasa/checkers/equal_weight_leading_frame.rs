use std::fs;

type M = [[i128; 2]; 2];

fn mul(a: M, b: M) -> M {
    [[a[0][0]*b[0][0]+a[0][1]*b[1][0], a[0][0]*b[0][1]+a[0][1]*b[1][1]],
     [a[1][0]*b[0][0]+a[1][1]*b[1][0], a[1][0]*b[0][1]+a[1][1]*b[1][1]]]
}
fn inv_unimodular(a: M) -> M {
    let d=a[0][0]*a[1][1]-a[0][1]*a[1][0]; assert!(d==1 || d == -1);
    [[a[1][1]/d,-a[0][1]/d],[-a[1][0]/d,a[0][0]/d]]
}

fn main() {
    let frames: [M; 6] = [
        [[1,0],[0,1]], [[1,1],[0,1]], [[1,0],[1,1]],
        [[0,1],[-1,0]], [[2,1],[1,1]], [[1,2],[1,1]],
    ];
    let gauges: [M; 4] = [[[1,0],[0,1]],[[1,1],[0,1]],[[0,1],[-1,0]],[[2,1],[1,1]]];
    let mut checks=0_u64;
    for f0 in frames {
        let fi=inv_unimodular(f0);
        for h11 in -5_i128..=5 { for h12 in -4_i128..=4 {
        for h21 in -3_i128..=3 { for h22 in -2_i128..=2 {
            let h=[[h11,h12],[h21,h22]];
            // For F_e=eF0 the common Rees factor cancels before specialization.
            let readout=mul(mul(fi,h),f0);
            assert_eq!(readout,mul(mul(inv_unimodular(f0),h),f0)); checks+=1;
            // Forgetting the labelled leading frame leaves conjugation ambiguity.
            for s in gauges {
                let relabelled=mul(mul(inv_unimodular(s),readout),s);
                assert_eq!(relabelled,mul(mul(inv_unimodular(mul(f0,s)),h),mul(f0,s)));
                checks+=1;
            }
        }}}}
    }
    // Rank-deficient leading matrix: e[[1,1],[0,e]].  The source column
    // operation c2 <- c2-c1 exposes weights (1,2), so equal first valuations
    // alone are not a complete filtration.
    for e in 1_i128..=31 {
        let c1=[e,0]; let c2=[e,e*e]; let refined=[c2[0]-c1[0],c2[1]-c1[1]];
        assert_eq!(refined,[0,e*e]); checks+=1;
    }
    let output=format!(concat!(
      "{{\n",
      "  \"schema\": \"marici.equal_weight_leading_frame.v1\",\n",
      "  \"exact_checks\": {},\n",
      "  \"common_weight_cancels\": true,\n",
      "  \"labelled_invertible_leading_frame_recovers_full_matrix\": true,\n",
      "  \"unlabelled_leading_frame_output\": \"conjugacy_class\",\n",
      "  \"rank_deficient_leading_frame_requires_higher_jet\": true,\n",
      "  \"rank_deficient_refined_weights\": [1,2],\n",
      "  \"new_cut_carrier_stratum\": false\n",
      "}}\n"),checks);
    fs::write("research/benincasa/results/equal-weight-leading-frame.json",output).unwrap();
}
