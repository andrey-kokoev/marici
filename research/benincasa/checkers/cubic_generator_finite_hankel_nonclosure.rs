#[derive(Clone,Copy)]struct Atom{q:i64,p:i64,wn:i64,wd:i64}
fn moment(a:&[Atom],iq:u32,ip:u32)->(i64,i64){
    let common=12_i64;let mut n=0_i64;
    for x in a{n+=common/x.wd*x.wn*x.q.pow(iq)*x.p.pow(ip);}
    let g=gcd(n,common);(n/g,common/g)
}
fn gcd(mut a:i64,mut b:i64)->i64{a=a.abs();while b!=0{let r=a%b;a=b;b=r;}a}

fn main(){
    let symmetric=[
        Atom{q:-2,p:-2,wn:1,wd:4},Atom{q:0,p:0,wn:1,wd:2},Atom{q:2,p:2,wn:1,wd:4}];
    let asymmetric=[Atom{q:-1,p:-1,wn:2,wd:3},Atom{q:2,p:2,wn:1,wd:3}];
    let mut retained_equalities=0usize;
    for total in 0..=2_u32{for iq in 0..=total{let ip=total-iq;
        assert_eq!(moment(&symmetric,iq,ip),moment(&asymmetric,iq,ip));retained_equalities+=1;
    }}
    assert_eq!(moment(&symmetric,3,0),(0,1));
    assert_eq!(moment(&asymmetric,3,0),(2,1));

    // For Dq=p, Dp=-q^2:
    // D(p^2)=-2 p q^2, and both supports have p=q.
    let ds=-2*moment(&symmetric,3,0).0;
    let da=-2*moment(&asymmetric,3,0).0;
    assert_eq!(ds,0);assert_eq!(da,-4);assert_ne!(ds,da);

    // Their common degree-one Hankel matrix on (1,q,p) is PSD and singular:
    // [[1,0,0],[0,2,2],[0,2,2]].
    let h=[[1_i64,0,0],[0,2,2],[0,2,2]];
    assert_eq!(h[0][0],1);assert_eq!(h[1][1],2);assert_eq!(h[1][1]*h[2][2]-h[1][2]*h[2][1],0);

    println!("{{");
    println!("  \"schema\": \"marici.cubic_generator_finite_hankel_nonclosure.v1\",");
    println!("  \"retained_moment_equalities_through_degree_two\": {retained_equalities},");
    println!("  \"symmetric_third_moment\": 0,");
    println!("  \"asymmetric_third_moment\": 2,");
    println!("  \"symmetric_derivative_of_p2\": {ds},");
    println!("  \"asymmetric_derivative_of_p2\": {da},");
    println!("  \"same_truncated_positive_state_has_unique_cubic_derivative\": false,");
    println!("  \"next_moment_grade_required\": true");
    println!("}}");
}
