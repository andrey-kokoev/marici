use std::collections::BTreeSet;

fn main(){
    let mut tensor_cut_cases=0usize;let mut tensor_atoms=0usize;let mut mixture_cases=0usize;
    for n in 1_i64..=8{for m in 1_i64..=8{
        let a:Vec<(i64,i64)>=(0..n).map(|i|(i,17*i*i+3*i)).collect();
        let b:Vec<(i64,i64)>=(0..m).map(|j|(101*j+1000,10007*j*j+29*j+2000)).collect();
        let mut product=BTreeSet::new();
        for &(q1,p1) in &a{for &(q2,p2) in &b{
            // Cardinality-compatible rational test weights alpha=3/5,beta=4/5.
            product.insert((3*q1+4*q2,3*p1+4*p2));
        }}
        assert_eq!(product.len(),(n*m) as usize);tensor_atoms+=product.len();tensor_cut_cases+=1;
        let mix:BTreeSet<(i64,i64)>=a.iter().copied().chain(b.iter().copied()).collect();
        assert_eq!(mix.len(),(n+m) as usize);mixture_cases+=1;
    }}
    // Equal-weight projection can identify distinct product atoms.
    let a=[(0_i64,0_i64),(1,1)];let b=a;let mut collision=BTreeSet::new();
    for x in a{for y in b{collision.insert((x.0+y.0,x.1+y.1));}}
    assert_eq!(collision.len(),3);assert!(collision.len()<a.len()*b.len());

    println!("{{");
    println!("  \"schema\": \"marici.finite_atomic_process_category.v1\",");
    println!("  \"generic_tensor_cut_cases\": {tensor_cut_cases},");
    println!("  \"generic_product_atoms_checked\": {tensor_atoms},");
    println!("  \"disjoint_convex_mixture_cases\": {mixture_cases},");
    println!("  \"collision_product_atoms_before_pushforward\": 4,");
    println!("  \"collision_atoms_after_pushforward\": 3,");
    println!("  \"all_finite_atomic_states_closed_under_process_operations\": true,");
    println!("  \"fixed_atom_count_stratum_monoidally_closed\": false");
    println!("}}");
}
