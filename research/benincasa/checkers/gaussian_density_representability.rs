#[derive(Clone,Copy,Debug)]struct V{x:i128,z:i128,y:i128}
fn cov(k:i128,l:i128,nu:i128)->V{
    let a=1+k*l;V{x:nu*(a*a+k*k),z:nu*(a*l+k),y:nu*(l*l+1)}
}
fn det(v:V)->i128{v.x*v.y-v.z*v.z}

#[derive(Clone,Copy)]struct Rat{n:i128,d:i128}
fn gcd(mut a:i128,mut b:i128)->i128{a=a.abs();b=b.abs();while b!=0{let r=a%b;a=b;b=r;}a}
fn rat(n:i128,d:i128)->Rat{let g=gcd(n,d);Rat{n:n/g,d:d/g}}
fn add(a:Rat,b:Rat)->Rat{rat(a.n*b.d+b.n*a.d,a.d*b.d)}
fn mul(a:Rat,b:Rat)->Rat{rat(a.n*b.n,a.d*b.d)}
fn ge_one(a:Rat)->bool{a.n>=a.d}

fn main(){
    let mut gaussian_states=0usize;let mut thermal_checks=0usize;
    for k in -10_i128..=10{for l in -10_i128..=10{for nu in 1_i128..=8{
        let v=cov(k,l,nu);assert!(v.x>0&&v.y>0);assert_eq!(det(v),nu*nu);
        // Thermal seed has occupation (nu-1)/2 and geometric ratio
        // r=(nu-1)/(nu+1), including r=0 for the vacuum.
        let r=rat(nu-1,nu+1);assert!(r.n>=0&&r.n<r.d);thermal_checks+=1;gaussian_states+=1;
    }}}
    let mut merge_checks=0usize;
    for seed in 0_i128..5000{
        let v1=cov(seed%11-5,seed%7-3,seed%8+1);
        let v2=cov(seed%13-6,seed%9-4,(seed*3)%8+1);
        let m=seed%17+1;let n=seed%19+1;let den=m+n;
        let x=rat(m*v1.x+n*v2.x,den);let z=rat(m*v1.z+n*v2.z,den);let y=rat(m*v1.y+n*v2.y,den);
        let determinant=add(mul(x,y),rat(-z.n*z.n,z.d*z.d));assert!(ge_one(determinant));merge_checks+=1;
    }
    println!("{{");
    println!("  \"schema\": \"marici.gaussian_density_representability.v1\",");
    println!("  \"metaplectic_thermal_covariances_checked\": {gaussian_states},");
    println!("  \"thermal_geometric_ratio_checks\": {thermal_checks},");
    println!("  \"cardinality_weighted_gaussian_merges_checked\": {merge_checks},");
    println!("  \"determinant_identity\": \"det(V)=nu^2\",");
    println!("  \"gaussian_packets_density_representable\": true,");
    println!("  \"gaussian_merge_preserves_uncertainty\": true");
    println!("}}");
}
