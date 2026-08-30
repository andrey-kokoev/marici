#[derive(Clone,Copy,Debug,Eq,PartialEq)]
struct Rat{n:i128,d:i128}
fn gcd(mut a:i128,mut b:i128)->i128{a=a.abs();b=b.abs();while b!=0{let r=a%b;a=b;b=r;}a}
fn rat(n:i128,d:i128)->Rat{assert!(d!=0);let s=if d<0{-1}else{1};let g=gcd(n,d);Rat{n:s*n/g,d:d.abs()/g}}
fn sub(a:Rat,b:Rat)->Rat{rat(a.n*b.d-b.n*a.d,a.d*b.d)}
fn mul(a:Rat,b:Rat)->Rat{rat(a.n*b.n,a.d*b.d)}
fn div(a:Rat,b:Rat)->Rat{rat(a.n*b.d,a.d*b.n)}
fn sq(a:Rat)->Rat{mul(a,a)}

fn main(){
    let mut positive_families=0usize;
    let mut order_comparisons=0usize;
    let mut exceptional_determinants=0usize;
    for b in 1_i128..=10{for d in 1_i128..=10{for z in -5_i128..=5{
        let det=b*d-z*z;
        if det<=0{continue;}
        exceptional_determinants+=1;
        for x in -5_i128..=5{for y in -5_i128..=5{
            let a=rat(20,1);
            let numerator=d*x*x-2*z*x*y+b*y*y;
            let joint=sub(a,rat(numerator,det));
            if joint.n<0{continue;}

            let after_b_a=sub(a,rat(x*x,b));
            let after_b_cross=sub(rat(y,1),rat(x*z,b));
            let after_b_d=sub(rat(d,1),rat(z*z,b));
            let b_then_d=sub(after_b_a,div(sq(after_b_cross),after_b_d));

            let after_d_a=sub(a,rat(y*y,d));
            let after_d_cross=sub(rat(x,1),rat(y*z,d));
            let after_d_b=sub(rat(b,1),rat(z*z,d));
            let d_then_b=sub(after_d_a,div(sq(after_d_cross),after_d_b));

            assert_eq!(joint,b_then_d);
            assert_eq!(joint,d_then_b);
            positive_families+=1;
            order_comparisons+=2;
        }}
    }}}
    assert!(positive_families>1000);
    println!("{{");
    println!("  \"schema\": \"marici.three_block_weighted_schur_overlap.v1\",");
    println!("  \"invertible_exceptional_blocks_checked\": {exceptional_determinants},");
    println!("  \"positive_covariance_families_checked\": {positive_families},");
    println!("  \"sequential_order_comparisons\": {order_comparisons},");
    println!("  \"joint_equals_b_then_d\": true,");
    println!("  \"joint_equals_d_then_b\": true,");
    println!("  \"generic_exceptional_overlap_obstruction\": false,");
    println!("  \"remaining_support\": \"b*d-z^2=0\"");
    println!("}}");
}
