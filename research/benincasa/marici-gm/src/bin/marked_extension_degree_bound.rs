// Formal total-degree bounds for the characteristic-zero marked-extension solve.
// These are source-identity bounds, not inferred from modular output.

fn main() {
    // Common master columns in the fixed ordering q0,q1,q2,e1,...,e9.
    let common_degrees = [14u32, 15, 15, 16, 16, 15, 16, 15, 15, 16, 16, 16];
    // The generic rank-117 source minor uses 79,12,2,12 exact columns from
    // sectors (11),(10),(01),(00). Their cleared parameter degrees are 8,9,9,10.
    let exact_counts = [79u32, 12, 2, 12];
    let exact_degrees = [8u32, 9, 9, 10];
    assert_eq!(common_degrees.len() as u32 + exact_counts.iter().sum::<u32>(), 117);

    let denominator_bound = common_degrees.iter().sum::<u32>()
        + exact_counts.iter().zip(exact_degrees).map(|(n, d)| n * d).sum::<u32>();
    // Cramer's numerator replaces one selected column by a target column.
    // Every target has degree <=15; the smallest selected-column bound is 8.
    let numerator_bound = denominator_bound - 8 + 15;
    assert_eq!(denominator_bound, 1063);
    assert_eq!(numerator_bound, 1070);

    println!("{{");
    println!("  \"schema\": \"marici.benincasa.marked_extension_degree_bound.v1\",");
    println!("  \"cleared_identity_count\": 132,");
    println!("  \"generic_rank\": 117,");
    println!("  \"parameter_degrees\": {{\"K\":6,\"K1\":5,\"L1\":1,\"L2\":1,\"target_max\":15}},");
    println!("  \"common_column_degrees\": {:?},", common_degrees);
    println!("  \"exact_sector_counts\": {{\"11\":79,\"10\":12,\"01\":2,\"00\":12}},");
    println!("  \"exact_sector_degree_bounds\": {{\"11\":8,\"10\":9,\"01\":9,\"00\":10}},");
    println!("  \"cramer_total_degree_bounds\": {{\"denominator\":{},\"numerator\":{}}},", denominator_bound, numerator_bound);
    println!("  \"interpretation\": \"formal source-identity bounds; reconstruction candidates still require exact substitution\"");
    println!("}}");
}
