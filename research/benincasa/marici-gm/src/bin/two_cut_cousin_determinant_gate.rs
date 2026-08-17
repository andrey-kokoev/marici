use std::collections::BTreeSet;

type Exponent = (i8, i8); // powers of (u,v)

fn top_cousin_projection(support: &BTreeSet<Exponent>) -> BTreeSet<Exponent> {
    support.iter().copied().filter(|(u,v)| *u < 0 && *v < 0).collect()
}

fn main() {
    // On the generic common open every lower denominator is a unit. Its
    // Taylor expansion has nonnegative normal exponents. Multiplying by a
    // singly marked Cut pole therefore gives these minimal Laurent supports.
    let sector_12 = BTreeSet::from([(-1,0)]);
    let sector_23 = BTreeSet::from([(0,-1)]);
    let source_sum: BTreeSet<_> = sector_12.union(&sector_23).copied().collect();
    assert!(top_cousin_projection(&sector_12).is_empty());
    assert!(top_cousin_projection(&sector_23).is_empty());
    assert!(top_cousin_projection(&source_sum).is_empty());

    // H^2_(u,v) is represented in the Cech quotient by Laurent monomials
    // negative in both variables. Its primitive ordered determinant is (uv)^-1.
    let determinant = BTreeSet::from([(-1,-1)]);
    assert_eq!(top_cousin_projection(&determinant), determinant);
    assert!(!source_sum.contains(&(-1,-1)));

    // Addition and linear residue/Cousin maps do not multiply the two source
    // summands. Producing (-1,-1) requires adjoining their product pole.
    let source_realizes_determinant = false;
    assert!(!source_realizes_determinant);

    println!("{{");
    println!("  \"normals\": [\"u=q_G12\", \"v=q_G23\"],");
    println!("  \"frozen_source_principal_support\": [[-1,0],[0,-1]],");
    println!("  \"top_Cech_rule\": \"retain Laurent monomials negative in both u and v\",");
    println!("  \"source_top_projection\": [],");
    println!("  \"Koszul_determinant_support\": [[-1,-1]],");
    println!("  \"determinant_representative\": \"1/(u*v)\",");
    println!("  \"source_realizes_determinant\": false,");
    println!("  \"required_change\": \"adjoin a joint marked-Cut pole or an independently derived secondary kernel\",");
    println!("  \"change_authorized\": false,");
    println!("  \"classification\": \"geometric Tor/Koszul class absent from the frozen physical coefficient form\"");
    println!("}}");
}
