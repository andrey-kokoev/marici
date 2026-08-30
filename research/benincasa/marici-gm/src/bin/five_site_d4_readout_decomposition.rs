use serde_json::json;
use std::fs;

fn main() {
    // Occurrence space V=Q^5 with cyclic shift. The source scalar readout is
    // augmentation epsilon(x)=sum_i x_i.
    let invariant = [1_i32, 1, 1, 1, 1];
    let augmentation_basis = [
        [1_i32, -1, 0, 0, 0],
        [0_i32, 1, -1, 0, 0],
        [0_i32, 0, 1, -1, 0],
        [0_i32, 0, 0, 1, -1],
    ];
    let epsilon = |vector: &[i32; 5]| vector.iter().sum::<i32>();
    assert_eq!(epsilon(&invariant), 5);
    assert!(augmentation_basis.iter().all(|vector| epsilon(vector) == 0));

    // In invariant basis (R=sum r_i,V=sum v_i), N(R)=V and N(V)=0.
    let n_invariant = [[0_i8, 0], [1_i8, 0]];
    let n2 = [
        [
            n_invariant[0][0] * n_invariant[0][0] + n_invariant[0][1] * n_invariant[1][0],
            n_invariant[0][0] * n_invariant[0][1] + n_invariant[0][1] * n_invariant[1][1],
        ],
        [
            n_invariant[1][0] * n_invariant[0][0] + n_invariant[1][1] * n_invariant[1][0],
            n_invariant[1][0] * n_invariant[0][1] + n_invariant[1][1] * n_invariant[1][1],
        ],
    ];
    assert_eq!(n2, [[0, 0], [0, 0]]);

    let packet = json!({
        "schema": "marici.benincasa.five_site.d4_readout_decomposition.v1",
        "occurrence_space": "Q[C5]",
        "rational_decomposition": "Q_triv direct_sum I_aug, with I_aug isomorphic to Q(zeta_5)",
        "scalar_readout_covector": [1,1,1,1,1],
        "scalar_value_on_invariant_generator": epsilon(&invariant),
        "augmentation_basis": augmentation_basis,
        "scalar_values_on_augmentation_basis": [0,0,0,0],
        "invariant_nilpotent_residue": n_invariant,
        "invariant_residue_rank": 1,
        "invariant_residue_squared_zero": true,
        "connection_convention": "nabla=d-(N/(2*pi*i))*dlog(tau), so positive monodromy is T=exp(N)=I+N",
        "local_exponents": [0,0],
        "nontrivial_character_visibility": "killed by the frozen equal-weight scalar readout",
        "labelled_visibility": "retained before scalar readout; a nontrivial-character observable would require an independently derived occurrence-sensitive source functional",
        "claim": "The physical cyclic scalar sees exactly the invariant rank-one logarithmic block and kills the four-dimensional augmentation sector."
    });
    fs::write(
        "../results/five-site-d4-readout-decomposition.json",
        serde_json::to_string_pretty(&packet).unwrap() + "\n",
    )
    .unwrap();
    println!("{}", serde_json::to_string_pretty(&packet).unwrap());
}
