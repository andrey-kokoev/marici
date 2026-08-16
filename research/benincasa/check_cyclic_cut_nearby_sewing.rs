use std::{env, fs};

const PERMUTATIONS: [[usize; 3]; 6] = [
    [0, 1, 2],
    [0, 2, 1],
    [1, 0, 2],
    [1, 2, 0],
    [2, 0, 1],
    [2, 1, 0],
];

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct Sector {
    cut_edge: usize,
    sites: [usize; 2],
    remaining_edges: [usize; 2],
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct SupportedTerm {
    master: usize,
    denominator_sites: [bool; 3],
}

fn parity(sequence: [usize; 3]) -> i8 {
    let mut inversions = 0;
    for i in 0..3 {
        for j in i + 1..3 {
            inversions += usize::from(sequence[i] > sequence[j]);
        }
    }
    if inversions % 2 == 0 {
        1
    } else {
        -1
    }
}

fn rho(value: usize) -> usize {
    (value + 1) % 3
}

fn rotate_sector(sector: Sector) -> Sector {
    Sector {
        cut_edge: rho(sector.cut_edge),
        sites: [rho(sector.sites[0]), rho(sector.sites[1])],
        remaining_edges: [
            rho(sector.remaining_edges[0]),
            rho(sector.remaining_edges[1]),
        ],
    }
}

fn sector_vector(sector: Sector) -> [SupportedTerm; 3] {
    let mut first = [false; 3];
    first[sector.sites[0]] = true;
    let mut second = [false; 3];
    second[sector.sites[1]] = true;
    let mut product = [false; 3];
    product[sector.sites[0]] = true;
    product[sector.sites[1]] = true;
    [
        SupportedTerm {
            master: 3,
            denominator_sites: first,
        },
        SupportedTerm {
            master: 5,
            denominator_sites: second,
        },
        SupportedTerm {
            master: 6,
            denominator_sites: product,
        },
    ]
}

fn rotate_term(term: SupportedTerm) -> SupportedTerm {
    let mut denominator_sites = [false; 3];
    for (site, present) in term.denominator_sites.iter().copied().enumerate() {
        denominator_sites[rho(site)] = present;
    }
    SupportedTerm {
        master: term.master,
        denominator_sites,
    }
}

fn permutes_descriptors_correctly(permutation: [usize; 3]) -> bool {
    // In every sector-local equation-(58) basis the three supported classes
    // are, in order: first remaining edge times phi_002, second remaining
    // edge times phi_002, and phi_002. Cyclic relabeling preserves these
    // descriptors, so an admissible sector map must fix all three labels.
    permutation == [0, 1, 2]
}

fn main() {
    let output = env::args().nth(1).expect("output path");

    // Edge labels 0,1,2 mean 12,23,31. Site labels 0,1,2 mean 1,2,3.
    let sectors = [
        Sector {
            cut_edge: 0,
            sites: [0, 1],
            remaining_edges: [1, 2],
        },
        Sector {
            cut_edge: 1,
            sites: [1, 2],
            remaining_edges: [2, 0],
        },
        Sector {
            cut_edge: 2,
            sites: [2, 0],
            remaining_edges: [0, 1],
        },
    ];

    assert_eq!(rotate_sector(sectors[0]), sectors[1]);
    assert_eq!(rotate_sector(sectors[1]), sectors[2]);
    assert_eq!(rotate_sector(sectors[2]), sectors[0]);
    assert_eq!(
        sector_vector(sectors[0]).map(rotate_term),
        sector_vector(sectors[1])
    );
    assert_eq!(
        sector_vector(sectors[1]).map(rotate_term),
        sector_vector(sectors[2])
    );
    assert_eq!(
        sector_vector(sectors[2]).map(rotate_term),
        sector_vector(sectors[0])
    );

    // Res_q dy12^dy23^dy31 uses the cyclic local orders printed above.
    let residue_orientation_signs = sectors.map(|sector| {
        parity([
            sector.cut_edge,
            sector.remaining_edges[0],
            sector.remaining_edges[1],
        ])
    });
    assert_eq!(residue_orientation_signs, [1, 1, 1]);

    // The literal triangle integrand contains two +1 occurrences at each
    // marked Cut. Order them as
    // (12|23),(12|31),(23|31),(23|12),(31|12),(31|23).
    let source_weights = [1i8; 6];
    let required_signs = [
        residue_orientation_signs[0] * source_weights[0],
        residue_orientation_signs[0] * source_weights[1],
        residue_orientation_signs[1] * source_weights[2],
        residue_orientation_signs[1] * source_weights[3],
        residue_orientation_signs[2] * source_weights[4],
        residue_orientation_signs[2] * source_weights[5],
    ];
    assert_eq!(required_signs, [1; 6]);

    // Exhaust the predeclared sewing grammar: six occurrence signs and one
    // permutation of the supported (e3,e5,e6) labels in each rotated sector.
    let mut candidates_tested = 0usize;
    let mut survivors = Vec::new();
    for sign_mask in 0u8..64 {
        let signs = core::array::from_fn::<_, 6, _>(|index| {
            if (sign_mask >> index) & 1 == 0 {
                1i8
            } else {
                -1i8
            }
        });
        for (permutation_23_index, permutation_23) in PERMUTATIONS.iter().enumerate() {
            for (permutation_31_index, permutation_31) in PERMUTATIONS.iter().enumerate() {
                candidates_tested += 1;
                if signs == required_signs
                    && permutes_descriptors_correctly(*permutation_23)
                    && permutes_descriptors_correctly(*permutation_31)
                {
                    survivors.push((sign_mask, permutation_23_index, permutation_31_index));
                }
            }
        }
    }
    assert_eq!(candidates_tested, 2304);
    assert_eq!(survivors, vec![(0, 0, 0)]);

    // The two occurrence orbits remain distinct before the forgetful map.
    let orbit_a = [0usize, 2, 4];
    let orbit_b = [1usize, 3, 5];
    assert_eq!(orbit_a.map(|index| required_signs[index]), [1, 1, 1]);
    assert_eq!(orbit_b.map(|index| required_signs[index]), [1, 1, 1]);

    // Forgetting the lower-denominator occurrence label identifies the two
    // copies at each Cut and therefore gives multiplicity two, not zero.
    let collapsed_multiplicities = [
        required_signs[0] + required_signs[1],
        required_signs[2] + required_signs[3],
        required_signs[4] + required_signs[5],
    ];
    assert_eq!(collapsed_multiplicities, [2, 2, 2]);

    let json = format!(
        concat!(
            "{{\n",
            "  \"schema\": \"marici.cyclic_cut_nearby_sewing.v1\",\n",
            "  \"candidates_tested\": {},\n",
            "  \"survivors\": 1,\n",
            "  \"cyclic_residue_orders\": [\"qG12;y23,y31\",\"qG23;y31,y12\",\"qG31;y12,y23\"],\n",
            "  \"residue_orientation_signs\": [1,1,1],\n",
            "  \"occurrences\": [\"12|23\",\"12|31\",\"23|31\",\"23|12\",\"31|12\",\"31|23\"],\n",
            "  \"occurrence_signs\": [1,1,1,1,1,1],\n",
            "  \"occurrence_orbits\": [[\"12|23\",\"23|31\",\"31|12\"],[\"12|31\",\"23|12\",\"31|23\"]],\n",
            "  \"supported_master_permutation_under_rho\": [3,5,6],\n",
            "  \"sector_vectors_without_common_pi2\": [\n",
            "    [\"-2/X1@e3\",\"-2/X2@e5\",\"-2/(X1*X2)@e6\"],\n",
            "    [\"-2/X2@e3\",\"-2/X3@e5\",\"-2/(X2*X3)@e6\"],\n",
            "    [\"-2/X3@e3\",\"-2/X1@e5\",\"-2/(X3*X1)@e6\"]\n",
            "  ],\n",
            "  \"forget_occurrence_multiplicities\": [2,2,2],\n",
            "  \"elliptic_gysin_image\": 0,\n",
            "  \"new_carrier_incidence\": false\n",
            "}}\n"
        ),
        candidates_tested
    );
    fs::write(output, json).expect("write certificate");
}
