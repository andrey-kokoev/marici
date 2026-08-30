use serde_json::json;
use std::{collections::BTreeSet, fs};

fn components(contracted: &BTreeSet<usize>) -> Vec<BTreeSet<usize>> {
    let mut parent = (0..5).collect::<Vec<_>>();
    fn root(parent: &mut [usize], mut i: usize) -> usize {
        while parent[i] != i {
            parent[i] = parent[parent[i]];
            i = parent[i];
        }
        i
    }
    for &edge in contracted {
        let (left, right) = (edge, (edge + 1) % 5);
        let (a, b) = (root(&mut parent, left), root(&mut parent, right));
        parent[a] = b;
    }
    let mut out = Vec::<BTreeSet<usize>>::new();
    for site in 0..5 {
        let r = root(&mut parent, site);
        if let Some(block) = out
            .iter_mut()
            .find(|block| root(&mut parent, *block.first().unwrap()) == r)
        {
            block.insert(site);
        } else {
            out.push([site].into_iter().collect());
        }
    }
    out.sort();
    out
}

fn main() {
    let active = vec![
        [0usize, 1].into_iter().collect::<BTreeSet<_>>(),
        [2usize, 3].into_iter().collect::<BTreeSet<_>>(),
        [4usize].into_iter().collect::<BTreeSet<_>>(),
    ];
    let mut admissible = Vec::new();
    for left in 0..5 {
        for right in left + 1..5 {
            let contracted = [left, right].into_iter().collect::<BTreeSet<_>>();
            let blocks = components(&contracted);
            if active.iter().all(|region| blocks.contains(region)) {
                admissible.push(json!({
                    "contracted_edges": [left + 1, right + 1],
                    "blocks": blocks.iter().map(|block| block.iter().map(|site| site + 1).collect::<Vec<_>>()).collect::<Vec<_>>()
                }));
            }
        }
    }
    assert_eq!(admissible.len(), 1);
    assert_eq!(admissible[0]["contracted_edges"], json!([1, 3]));

    // On Entry 1234's regular-cone slice, adjacent dot products are
    // (3+sqrt(5))/4 and every P_i^2=2.
    // Therefore (P_1+P_2)^2=(P_3+P_4)^2=(11+sqrt(5))/2.
    let packet = json!({
        "schema": "marici.benincasa.five_to_three.active_wall_contraction.v1",
        "active_regions": [[1,2],[3,4],[5]],
        "admissible_two_edge_contractions": admissible,
        "triangle_edges_after_contraction": ["e23","e45","e51"],
        "contracted_site_energies": ["2*t","2*t","t"],
        "contracted_resultant_norm_squares": ["(11+sqrt(5))/2","(11+sqrt(5))/2","2"],
        "homogeneous_massless_conditions": [
            "4*t^2=(11+sqrt(5))/2",
            "4*t^2=(11+sqrt(5))/2",
            "t^2=2"
        ],
        "compatibility_difference": "2-(11+sqrt(5))/8=(5-sqrt(5))/8 != 0",
        "homogeneous_intersection_exists": false,
        "claim": "The active-wall contraction is canonical, but the frozen five-site slice does not map into the homogeneous three-site Q locus.",
        "scope": "Graph contraction and induced kinematics only; no specialization of the five-site Landau divisor is asserted."
    });
    fs::write(
        "../results/five-to-three-active-wall-contraction.json",
        serde_json::to_string_pretty(&packet).unwrap() + "\n",
    )
    .unwrap();
    println!("{}", serde_json::to_string_pretty(&packet).unwrap());
}
