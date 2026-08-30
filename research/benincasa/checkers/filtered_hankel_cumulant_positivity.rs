fn binom(n:usize,k:usize)->i128{if k>n{return 0;}let mut z=1_i128;for i in 0..k{z=z*(n-i) as i128/(i+1) as i128;}z}

fn moments(kappa:&[i128],nmax:usize)->Vec<i128>{
    let mut m=vec![0_i128;nmax+1];m[0]=1;
    for n in 1..=nmax{
        for k in 1..=n{m[n]+=binom(n-1,k-1)*kappa[k]*m[n-k];}
    }
    m
}

fn det(a:&[Vec<i128>])->i128{
    let n=a.len();if n==0{return 1;}if n==1{return a[0][0];}
    let mut z=0_i128;
    for j in 0..n{
        let minor:Vec<Vec<i128>>=(1..n).map(|i|(0..n).filter(|&k|k!=j).map(|k|a[i][k]).collect()).collect();
        let term=a[0][j]*det(&minor);if j%2==0{z+=term}else{z-=term}
    }z
}

fn hankel_psd(m:&[i128],degree:usize)->bool{
    let n=degree+1;
    for mask in 1usize..(1usize<<n){
        let ids:Vec<usize>=(0..n).filter(|i|mask&(1<<i)!=0).collect();
        let a:Vec<Vec<i128>>=ids.iter().map(|&i|ids.iter().map(|&j|m[i+j]).collect()).collect();
        if det(&a)<0{return false;}
    }true
}

fn packet(k4:i128,k6:i128)->Vec<i128>{let mut k=vec![0_i128;7];k[2]=1;k[4]=k4;k[6]=k6;k}

fn main(){
    let mut fourth_order_checks=0usize;let mut sixth_order_checks=0usize;
    for k4 in -12_i128..=12{
        let m=moments(&packet(k4,0),4);
        assert_eq!(hankel_psd(&m,2),k4>=-2);fourth_order_checks+=1;
    }
    for k6 in -30_i128..=30{
        let m=moments(&packet(0,k6),6);
        assert_eq!(hankel_psd(&m,3),k6>=-6);sixth_order_checks+=1;
    }
    let positive_four=moments(&packet(0,-7),6);
    assert!(hankel_psd(&positive_four[..5],2));
    assert!(!hankel_psd(&positive_four,3));
    let gaussian=moments(&packet(0,0),6);
    assert!(hankel_psd(&gaussian,3));

    println!("{{");
    println!("  \"schema\": \"marici.filtered_hankel_cumulant_positivity.v1\",");
    println!("  \"fourth_order_boundary_checks\": {fourth_order_checks},");
    println!("  \"sixth_order_boundary_checks\": {sixth_order_checks},");
    println!("  \"kappa4_lower_bound_at_unit_variance\": -2,");
    println!("  \"kappa6_lower_bound_when_kappa4_zero\": -6,");
    println!("  \"positive_order_four_packet_can_fail_at_order_six\": true,");
    println!("  \"cumulant_species_have_independent_positivity\": false,");
    println!("  \"positivity_is_filtered_hankel_compatibility\": true");
    println!("}}");
}
