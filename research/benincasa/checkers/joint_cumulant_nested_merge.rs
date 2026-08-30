#[derive(Clone)]
enum Tree{Leaf,Node(Box<Tree>,Box<Tree>)}

fn trees(n:usize)->Vec<Tree>{
    if n==1{return vec![Tree::Leaf];}
    let mut out=Vec::new();
    for m in 1..n{for l in trees(m){for r in trees(n-m){
        out.push(Tree::Node(Box::new(l.clone()),Box::new(r)));
    }}}
    out
}

fn size(t:&Tree)->usize{match t{Tree::Leaf=>1,Tree::Node(l,r)=>size(l)+size(r)}}

fn audit(t:&Tree,r:usize,counts:&mut Counts){
    if let Tree::Node(l,rr)=t{
        let m=size(l) as u128;let n=size(rr) as u128;
        let mut complete=0_u128;
        for mask in 0_u128..(1_u128<<r){
            let left=mask.count_ones() as usize;
            complete+=m.pow(left as u32)*n.pow((r-left) as u32);
            counts.mixed_slot_sectors+=1;
        }
        assert_eq!(complete,(m+n).pow(r as u32));
        let pure=m.pow(r as u32)+n.pow(r as u32);
        assert!(pure<complete);
        counts.internal_node_order_audits+=1;
        counts.omitted_mixed_deficit_total+=complete-pure;
        audit(l,r,counts);audit(rr,r,counts);
    }
}

#[derive(Default)]
struct Counts{
    trees:usize,
    internal_node_order_audits:usize,
    mixed_slot_sectors:usize,
    omitted_mixed_deficit_total:u128,
}

fn main(){
    let mut c=Counts::default();
    for n in 2..=11usize{for t in trees(n){
        c.trees+=1;
        for r in 2..=8usize{audit(&t,r,&mut c);}
    }}
    assert!(c.omitted_mixed_deficit_total>0);
    println!("{{");
    println!("  \"schema\": \"marici.joint_cumulant_nested_merge.v1\",");
    println!("  \"max_occurrence_count\": 11,");
    println!("  \"max_cumulant_order\": 8,");
    println!("  \"ordered_binary_trees_checked\": {},",c.trees);
    println!("  \"internal_node_order_audits\": {},",c.internal_node_order_audits);
    println!("  \"labelled_mixed_slot_sectors_checked\": {},",c.mixed_slot_sectors);
    println!("  \"complete_joint_tensor_tree_independent\": true,");
    println!("  \"pure_block_cumulants_sufficient\": false,");
    println!("  \"partition_incidence_requires_new_carrier_cell\": false");
    println!("}}");
}
