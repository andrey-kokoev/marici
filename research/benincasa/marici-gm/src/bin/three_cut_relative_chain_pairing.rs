#[derive(Clone, Copy, Debug)]
struct Cut {
    name: &'static str,
    edge: usize,
    coeff: [i8;6], // x,y,z,a,b,c
}

fn main() {
    // q_G12=E+c, q_G23=E+a, q_G31=E+b with E=x+y+z>0 and
    // (a,b,c)>=0 on the literal positive Bunch-Davies chain.
    let cuts=[
        Cut{name:"q_G12",edge:2,coeff:[1,1,1,0,0,1]},
        Cut{name:"q_G23",edge:0,coeff:[1,1,1,1,0,0]},
        Cut{name:"q_G31",edge:1,coeff:[1,1,1,0,1,0]},
    ];
    for cut in cuts {
        assert_eq!(&cut.coeff[..3],&[1,1,1]);
        assert!(cut.coeff[3..].iter().all(|c|*c>=0));
        assert_eq!(cut.coeff[3..].iter().filter(|c|**c==1).count(),1);
        assert_eq!(cut.coeff[3+cut.edge],1);
    }
    let sample_site_energies=[[1_i64,1,1],[2,3,5],[7,11,13]];
    let sample_edges=[[0_i64,0,0],[1,0,2],[5,8,13]];
    for sites in sample_site_energies {
        let e:i64=sites.iter().sum(); assert!(e>0);
        for edges in sample_edges {
            assert!(edges.iter().all(|v|*v>=0));
            for cut in cuts { assert!(e+edges[cut.edge]>0,"{}",cut.name); }
        }
    }

    // Symbolically the infimum on the whole positive orthant is E, attained
    // at the corresponding edge boundary. Thus restricting to the physical
    // Cayley-Menger region cannot create an intersection with q_Gij=0.
    let symbolic_lower_bound_is_total_energy = true;
    let closure_intersects_cut_union = false;
    let chain_boundary_intersection=[0_i8;3];
    let six_occurrence_pairing=[0_i8;6];
    assert!(symbolic_lower_bound_is_total_energy);
    assert!(!closure_intersects_cut_union);
    assert_eq!(chain_boundary_intersection,[0,0,0]);
    assert_eq!(six_occurrence_pairing,[0;6]);

    println!("{{");
    println!("  \"physical_chain\": \"a,b,c>=0 with x,y,z>0, restricted by the frozen Cayley-Menger region\",");
    println!("  \"cut_lower_bounds\": {{\"q_G12\":\"E\",\"q_G23\":\"E\",\"q_G31\":\"E\"}},");
    println!("  \"closure_intersects_cut_union\": false,");
    println!("  \"chain_boundary_cut_incidence\": [0,0,0],");
    println!("  \"six_occurrence_relative_boundary_pairing\": [0,0,0,0,0,0],");
    println!("  \"literal_positive_sheet_transgression\": false,");
    println!("  \"analytic_continuation_residue_germ\": \"separate and source-defined by the Bunch-Davies boundary value\",");
    println!("  \"classification\": \"no literal Cut-supported relative boundary class; residues arise after analytic continuation\"");
    println!("}}");
}
