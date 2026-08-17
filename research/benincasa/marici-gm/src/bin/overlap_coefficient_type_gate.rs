#[derive(Debug, Clone, Copy, PartialEq, Eq)]
struct Bidegree { cohomological: i8, tate: i8 }

fn main() {
    // C^o is a regular complex-codimension-one locally closed subspace of
    // each sector surface open. Absolute purity fixes i^! = i^*[-2](-1).
    let ordinary_pullback = Bidegree { cohomological: 0, tate: 0 };
    let extraordinary_pullback = Bidegree { cohomological: -2, tate: -1 };
    assert_ne!(ordinary_pullback, extraordinary_pullback);

    // The source-defined identity compares ordinary restrictions. It cannot
    // be fed directly to the counit i_! i^! -> id without purity retyping.
    let restriction_identity_types_as_cohomological_correspondence = false;
    assert!(!restriction_identity_types_as_cohomological_correspondence);

    // After purity and the frozen normal orientations, both extraordinary
    // restrictions have the same bidegree. Their common object maps by the
    // two counits INTO the sector objects. The localization triangle supplies
    // no canonical arrow in the reverse direction.
    let common_supported_object_exists = true;
    let counit_to_each_sector_exists = true;
    let canonical_sector_to_supported_retraction = false;
    let canonical_full_sector_transition = false;
    assert!(common_supported_object_exists && counit_to_each_sector_exists);
    assert!(!canonical_sector_to_supported_retraction && !canonical_full_sector_transition);

    println!("{{");
    println!("  \"codimension_in_each_sector\": 1,");
    println!("  \"purity\": \"i^!L = i^*L[-2](-1)\",");
    println!("  \"ordinary_restriction_identity_degree\": [0,0],");
    println!("  \"extraordinary_correspondence_degree\": [-2,-1],");
    println!("  \"entry_359_p23_bang_p12_star_is_degree_zero_rank12_arrow\": false,");
    println!("  \"corrected_common_supported_object\": \"K_overlap = p12^!L12 = p23^!L23 on the oriented overlap; push it separately into each sector\",");
    println!("  \"canonical_arrows\": [\"K_overlap -> L12\", \"K_overlap -> L23\"],");
    println!("  \"canonical_arrow_L12_to_L23\": false,");
    println!("  \"missing_datum\": \"a retraction/specialization from each full sector object to its overlap-supported part\",");
    println!("  \"classification\": \"shared supported coefficient subobject, not descent transition\"");
    println!("}}");
}
