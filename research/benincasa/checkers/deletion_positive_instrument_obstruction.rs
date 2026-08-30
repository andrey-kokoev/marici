fn main(){
    let weights=[1_i64,-2,-2,-2,4,4,4,-8];
    let negative:Vec<usize>=weights.iter().enumerate().filter_map(|(i,w)|(*w<0).then_some(i)).collect();
    assert_eq!(negative.len(),4);
    assert_eq!(weights.iter().sum::<i64>(),-1);
    println!("{{\"status\":\"pass\",\"weights\":[1,-2,-2,-2,4,4,4,-8],\"negative_outcomes\":4,\"positive_instrument_directly\":false,\"signed_total\":-1}}");
}
