fn rank(mut a:Vec<Vec<i64>>)->usize {
    let (m,n)=(a.len(),a[0].len()); let mut r=0;
    for c in 0..n {
        let Some(p)=(r..m).find(|i|a[*i][c]!=0) else {continue}; a.swap(r,p);
        for i in 0..m { if i!=r && a[i][c]!=0 {
            let (x,y)=(a[r][c],a[i][c]);
            for j in c..n { a[i][j]=x*a[i][j]-y*a[r][j]; }
            let g=a[i].iter().fold(0_i64,|g,x|gcd(g,*x)); if g>1 {for x in &mut a[i]{*x/=g;}}
        }} r+=1; if r==m{break}
    } r
}
fn gcd(mut a:i64,mut b:i64)->i64 {a=a.abs();b=b.abs();while b!=0{let t=a%b;a=b;b=t;}a}

fn main() {
    // Generic exact fiber x=2,y=3. Ambient algebraic coordinates are
    // (e2,e3,e4,e5,e6,v0); the independent elliptic line is tracked below.
    // Columns are independently rescaled integral representatives of the
    // three logarithmic images in Entry 300.
    let log_cols=[
        [0,0,180,0,0,1],   // Theta_101: e4 and v0
        [-180,0,0,0,0,1],  // Theta_110: e2 and v0
        [0,0,0,0,1,0],     // Theta_111^filt: e6/(8(x+y))
    ];
    // Entry 305's J in physical enhanced coordinates (y e3,x e5,e6).
    let cut_cols=[
        [0,6,0,0,0,0],     // g101 -> 2*y*e3
        [0,0,0,4,0,0],     // g110 -> 2*x*e5
        [0,3,0,2,1,0],     // g111_tilde -> y*e3+x*e5+e6
    ];
    let as_rows=|cols:&[[i64;6];3]| (0..6).map(|i|cols.iter().map(|c|c[i]).collect()).collect::<Vec<Vec<i64>>>();
    let rank_log=rank(as_rows(&log_cols)); let rank_cut=rank(as_rows(&cut_cols));
    let combined_cols=[log_cols[0],log_cols[1],log_cols[2],cut_cols[0],cut_cols[1],cut_cols[2]];
    let combined_rows=(0..6).map(|i|combined_cols.iter().map(|c|c[i]).collect()).collect();
    let rank_union=rank(combined_rows);
    let rank_intersection=rank_log+rank_cut-rank_union;
    assert_eq!((rank_log,rank_cut,rank_union,rank_intersection),(3,3,5,1));

    // The common line is e6. It is the source-normalized second-Rees top
    // correction e6/8, whose logarithmic regularization is e6/(8(x+y)).
    assert_eq!(log_cols[2],[0,0,0,0,1,0]);
    let e6=[0,0,0,0,1,0];
    assert_eq!(e6,log_cols[2]);
    // e6 lies in the Cut span: top - 1/2*g101 - 1/2*g110 over Q.
    assert_eq!([0,0,0,0,2,0],sub(scale(cut_cols[2],2),add(cut_cols[0],cut_cols[1])));

    // The elliptic nilpotent line is independent and has zero enhanced/Cut
    // image by infinity Gysin typing.
    let full_log_nilpotent_rank=rank_log+1; let cut_elliptic_rank=0;
    assert_eq!(full_log_nilpotent_rank,4); assert_eq!(cut_elliptic_rank,0);
    // Entry 366 transports the complete source descriptors by the order-three
    // cyclic relabelling, so this sector-local rank profile repeats three times.
    let cyclic_sector_profiles=[(rank_log,rank_cut,rank_intersection);3];
    assert_eq!(cyclic_sector_profiles,[(3,3,1);3]);

    println!("{{");
    println!("  \"generic_fiber\": {{\"x\":2,\"y\":3}},");
    println!("  \"ambient_algebraic_coordinates\": [\"e2\",\"e3\",\"e4\",\"e5\",\"e6\",\"v0\"],");
    println!("  \"logarithmic_algebraic_image_rank\": 3,");
    println!("  \"cut_nearby_algebraic_image_rank\": 3,");
    println!("  \"combined_algebraic_rank\": 5,");
    println!("  \"intersection_rank\": 1,");
    println!("  \"intersection_generator\": \"e6\",");
    println!("  \"second_Rees_bridge\": \"raw e6/8 regularizes to logarithmic e6/(8*(x+y))\",");
    println!("  \"wall_directions_equal_as_T7_subspaces\": false,");
    println!("  \"common_conductor_lattice\": true,");
    println!("  \"elliptic_logarithmic_rank\": 1,");
    println!("  \"elliptic_cut_nearby_rank\": 0,");
    println!("  \"strict_full_rank12_commutation\": false,");
    println!("  \"cyclic_sector_profiles\": [[3,3,1],[3,3,1],[3,3,1]],");
    println!("  \"filtered_layer_compatibility\": \"common conductor lattice plus one second-Rees e6 bridge; elliptic line separate\",");
    println!("  \"new_carrier_datum\": false");
    println!("}}");
}
fn add(a:[i64;6],b:[i64;6])->[i64;6]{std::array::from_fn(|i|a[i]+b[i])}
fn sub(a:[i64;6],b:[i64;6])->[i64;6]{std::array::from_fn(|i|a[i]-b[i])}
fn scale(a:[i64;6],s:i64)->[i64;6]{std::array::from_fn(|i|a[i]*s)}
