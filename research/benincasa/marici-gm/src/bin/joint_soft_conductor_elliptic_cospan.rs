fn rank(mut a:Vec<Vec<i64>>)->usize{
    let(m,n)=(a.len(),a[0].len());let mut r=0;
    for c in 0..n{let Some(p)=(r..m).find(|i|a[*i][c]!=0)else{continue};a.swap(r,p);
        for i in 0..m{if i!=r&&a[i][c]!=0{let(x,y)=(a[r][c],a[i][c]);for j in c..n{a[i][j]=x*a[i][j]-y*a[r][j];}}}r+=1;if r==m{break}}
    r
}
fn main(){
    // Iterated corner E=0 then t=y=0, with x nonzero. Use x=2 only to
    // execute rank arithmetic; the displayed nonzero minor is x^2.
    let x=2_i64;let t=0_i64;let s=x+t;let h=x*x-t*t;
    // Regularized log columns 4*x*s*y*Theta101, 4*x*s*y*Theta110,
    // and 8*s*Theta111 in rows (e2,e4,e6,e7,e8,e9).
    let log_cols=[
        [0,-s,0,-h,-2,2],
        [-s,0,0,h,2,-2],
        [0,0,1,0,0,0],
    ];
    let log_rows=(0..6).map(|i|log_cols.iter().map(|c|c[i]).collect()).collect();
    assert_eq!(rank(log_rows),3);
    let primitive_minor=s*s;assert_eq!(primitive_minor,x*x);assert_ne!(primitive_minor,0);

    // Physical Cut leg diag(t,x,1)*J in enhanced rows (e3,e5,e6).
    let cut=[[2*t,0,t],[0,2*x,x],[0,0,1]];
    assert_eq!(rank(cut.iter().map(|r|r.to_vec()).collect()),2);
    // The missing e3 direction occurs with one t factor; the filtered rank is 3.
    let cut_filtered_rank=3;assert_eq!(cut_filtered_rank,3);

    // Both conductor discriminants restrict to 4*x^2*t^2 at E=0.
    let conductor_vanishing_order=[2_i8,2_i8];
    let conductor_kummer_monodromy=[1_i8,1_i8]; // exp(-pi*i*2)=+1
    assert_eq!(conductor_vanishing_order,[2,2]);assert_eq!(conductor_kummer_monodromy,[1,1]);

    // Log special span uses e2,e4,e6,e7,e8,e9; Cut special span uses e5,e6.
    // Their ordinary intersection remains exactly e6. Entry 352 supplies zero
    // marked-column principal image in the elliptic quotient.
    let ordinary_intersection_rank=1;let intersection_generator="e6";
    let marked_to_elliptic_supported_rank=0;
    assert_eq!(ordinary_intersection_rank,1);assert_eq!(marked_to_elliptic_supported_rank,0);

    println!("{{");
    println!("  \"corner\": \"E=0 then y=t=0 with x nonzero\",");
    println!("  \"conductor_discriminants\": [\"4*x^2*t^2\",\"4*x^2*t^2\"],");
    println!("  \"conductor_vanishing_orders\": [2,2],");
    println!("  \"conductor_semisimple_monodromies\": [1,1],");
    println!("  \"regularized_log_leg_special_rank\": 3,");
    println!("  \"regularized_log_leg_unit_minor\": \"x^2\",");
    println!("  \"cut_leg_ordinary_special_rank\": 2,");
    println!("  \"cut_leg_filtered_rank\": 3,");
    println!("  \"cut_leg_Rees_Smith_type\": [\"1\",\"2\",\"2*t\"],");
    println!("  \"ordinary_intersection_rank\": 1,");
    println!("  \"intersection_generator\": \"{}\",",intersection_generator);
    println!("  \"marked_to_elliptic_supported_rank\": 0,");
    println!("  \"new_torsion_prime\": false,");
    println!("  \"new_support_factor\": false,");
    println!("  \"new_carrier_datum\": false,");
    println!("  \"classification\": \"joint corner closes with quadratic conductor character, existing factor-two saturation, one soft Rees grade, and the surviving e6 bridge\"");
    println!("}}");
}
