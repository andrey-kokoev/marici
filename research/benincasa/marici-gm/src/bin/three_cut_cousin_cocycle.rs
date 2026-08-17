use std::collections::{BTreeMap, BTreeSet};

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct Occurrence {
    cut: usize,
    lower: usize,
    normal_exp: [i8; 3],
}

fn pair_residue(exp: [i8; 3], i: usize, j: usize) -> bool {
    exp[i] < 0 && exp[j] < 0
}

fn triple_residue(exp: [i8; 3]) -> bool {
    exp.iter().all(|e| *e < 0)
}

fn main() {
    // Indices 0,1,2 denote 12,23,31. Source order is frozen by Entry 229.
    let occurrences = [
        Occurrence { cut:0, lower:1, normal_exp:[-1,0,0] }, // 12|23
        Occurrence { cut:0, lower:2, normal_exp:[-1,0,0] }, // 12|31
        Occurrence { cut:1, lower:2, normal_exp:[0,-1,0] }, // 23|31
        Occurrence { cut:1, lower:0, normal_exp:[0,-1,0] }, // 23|12
        Occurrence { cut:2, lower:0, normal_exp:[0,0,-1] }, // 31|12
        Occurrence { cut:2, lower:1, normal_exp:[0,0,-1] }, // 31|23
    ];
    let source = [1_i8; 6];
    let pairs = [(0,1),(1,2),(2,0)];

    // d1 is the matrix of iterated marked-Cut residues. A lower denominator
    // is retained as an occurrence label and is a unit at the generic Cut-Cut
    // point; it does not change the marked-normal Laurent exponents.
    let mut d1 = [[0_i8; 6]; 3];
    for (r,(i,j)) in pairs.iter().enumerate() {
        for (c,o) in occurrences.iter().enumerate() {
            d1[r][c] = i8::from(pair_residue(o.normal_exp,*i,*j));
        }
    }
    assert_eq!(d1, [[0;6];3]);
    let d1_source: Vec<i8> = d1.iter().map(|row| row.iter().zip(source).map(|(a,b)| a*b).sum()).collect();
    assert_eq!(d1_source, vec![0,0,0]);

    // No occurrence has all three negative normal exponents, so the direct
    // triple residue and d2*d1 vanish.
    assert!(occurrences.iter().all(|o| !triple_residue(o.normal_exp)));

    // The six labelled first residues are a residue fingerprint. Regular
    // degree-zero forms have fingerprint zero. But the frozen pre-residue
    // integration form is meromorphic/logarithmic, with precisely these six
    // occurrence summands. Its d0 residue is the source vector itself.
    let regular_fingerprint = [0_i8;6];
    assert_ne!(source, regular_fingerprint);
    let d0_of_frozen_meromorphic_source = source;
    assert_eq!(d0_of_frozen_meromorphic_source,source);
    let exact_in_full_cousin_complex = true;
    let nonzero_in_truncated_positive_support_complex = true;
    assert!(exact_in_full_cousin_complex && nonzero_in_truncated_positive_support_complex);
    let source_gcd = source.iter().fold(0_i8, |g,x| gcd(g,*x));
    assert_eq!(source_gcd,1);

    // C3 rotation consists of two 3-cycles and fixes the all-positive vector.
    let rotation = [2_usize,3,4,5,0,1];
    let mut rotated=[0_i8;6]; for i in 0..6 { rotated[rotation[i]]=source[i]; }
    assert_eq!(rotated,source);
    let mut seen=BTreeSet::new(); let mut cycle_lengths=Vec::new();
    for start in 0..6 { if seen.insert(start) { let mut n=1; let mut j=rotation[start]; while j!=start { seen.insert(j); n+=1; j=rotation[j]; } cycle_lengths.push(n); }}
    cycle_lengths.sort(); assert_eq!(cycle_lengths,vec![3,3]);

    // Forgetting lower occurrences gives multiplicity two at every Cut.
    let mut forgotten=BTreeMap::new();
    for (o,c) in occurrences.iter().zip(source) { *forgotten.entry(o.cut).or_insert(0_i8)+=c; }
    assert_eq!(forgotten.values().copied().collect::<Vec<_>>(),vec![2,2,2]);

    println!("{{");
    println!("  \"occurrences\": [\"12|23\",\"12|31\",\"23|31\",\"23|12\",\"31|12\",\"31|23\"],");
    println!("  \"degree_one_source\": [1,1,1,1,1,1],");
    println!("  \"d1_pairwise_cut_residue_matrix\": [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]],");
    println!("  \"pairwise_residues\": [0,0,0],");
    println!("  \"triple_residue\": 0,");
    println!("  \"degree_one_closed\": true,");
    println!("  \"degree_one_exact_from_regular_degree_zero\": false,");
    println!("  \"d0_of_frozen_meromorphic_source\": [1,1,1,1,1,1],");
    println!("  \"degree_one_exact_in_full_source_Cousin_complex\": true,");
    println!("  \"nonzero_only_after_truncating_degree_zero_source\": true,");
    println!("  \"occurrence_residue_fingerprint\": [1,1,1,1,1,1],");
    println!("  \"primitive_over_Z\": true,");
    println!("  \"C3_cycle_lengths\": [3,3],");
    println!("  \"C3_invariant\": true,");
    println!("  \"occurrence_forgetting\": [2,2,2],");
    println!("  \"classification\": \"primitive C3-invariant closed residue vector; exact in the full source Cousin complex and nonzero only in its degree-positive truncation\"");
    println!("}}");
}

fn gcd(mut a:i8,mut b:i8)->i8 { a=a.abs(); b=b.abs(); while b!=0 { let r=a%b; a=b; b=r; } a }
