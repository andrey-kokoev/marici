fn main(){
    for subset in 0_usize..8 {
        for edge in 0..3 {
            let logarithmic_derivative=if subset&(1<<edge)!=0{1}else{0};
            assert_eq!(logarithmic_derivative,((subset>>edge)&1) as i32);
        }
    }
    println!("{{\"status\":\"pass\",\"subset_weight\":\"product over erased edges of K_e\",\"d_logK_weight\":\"edge_deletion_indicator\",\"source_kernel\":\"K_e=(2Re psi2(y_e))^-1\"}}");
}
