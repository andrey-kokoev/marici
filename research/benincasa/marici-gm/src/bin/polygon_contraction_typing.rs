use serde_json::json;
use std::fs;

fn facet(n:usize, sites:&[usize])->Vec<i32> {
    let mut q=vec![0;2*n];
    for &i in sites {q[i]=1;}
    for e in 0..n {
        let left=sites.contains(&e);
        let right=sites.contains(&((e+1)%n));
        if left!=right {q[n+e]=1;}
    }
    q
}

fn pullback_target_facet(n:usize,target_sites:&[usize])->Vec<i32> {
    // Contract source edge (n-1,0). Target site 0 has preimage {n-1,0};
    // every other target site i has preimage {i}.
    let mut source_sites=Vec::new();
    for &i in target_sites {
        if i==0 {source_sites.extend([n-1,0]);} else {source_sites.push(i);}
    }
    source_sites.sort_unstable();
    source_sites.dedup();
    facet(n,&source_sites)
}

fn main(){
    let mut audits=Vec::new();
    for n in 4..=8 {
        let target_n=n-1;
        let merged=pullback_target_facet(n,&[0]);
        let expected=facet(n,&[0,n-1]);
        assert_eq!(merged,expected);
        for i in 1..target_n {
            assert_eq!(pullback_target_facet(n,&[i]),facet(n,&[i]));
        }

        // q_0+q_{n-1}=q_{0,n-1}+2 y_{n-1}; hence equality holds only
        // after restriction to the contracted-edge divisor y_{n-1}=0.
        let q0=facet(n,&[0]);
        let qn=facet(n,&[n-1]);
        let pair=facet(n,&[0,n-1]);
        let residual=(0..2*n).map(|i|q0[i]+qn[i]-pair[i]).collect::<Vec<_>>();
        let mut expected_residual=vec![0;2*n];
        expected_residual[2*n-1]=2;
        assert_eq!(residual,expected_residual);

        audits.push(json!({
            "source_arity":n,
            "target_arity":target_n,
            "contracted_edge":[n-1,0],
            "target_merged_singleton_pullback":format!("g_{{{},1}}",n),
            "unaffected_singletons":target_n-1,
            "source_common_cell_contains_merged_wall":false,
            "target_common_cell_pullback_equals_source_common_cell":false,
            "wall_relation":format!("q_1+q_{}=q_{{1,{}}}+2*y_{{{},1}}",n,n,n),
            "relation_on_contraction_divisor":true
        }));
    }
    let packet=json!({
        "schema":"marici.benincasa.polygon_contraction_typing.v1",
        "operation":"contract the labelled cycle edge (n,1)",
        "audits":audits,
        "conclusion":{
            "strict_common_cell_map":false,
            "facet_pullback_exists":true,
            "comparison_required":"restriction to y_(n,1)=0 followed by a residue/Gysin or counit combining the two source singleton poles",
            "direct_period_recursion_authorized":false
        },
        "scope":"Exact labelled facet and common-cell typing for arities 4 through 8; no residue/Gysin normalization is inferred."
    });
    fs::write("../results/polygon-contraction-typing.json",serde_json::to_string_pretty(&packet).unwrap()+"\n").unwrap();
    println!("{}",serde_json::to_string(&packet["conclusion"]).unwrap());
}
