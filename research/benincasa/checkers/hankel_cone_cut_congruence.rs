#[derive(Clone,Copy,Debug,Eq,PartialEq)]
struct Rat{n:i128,d:i128}
fn gcd(mut a:i128,mut b:i128)->i128{a=a.abs();b=b.abs();while b!=0{let r=a%b;a=b;b=r;}a}
fn rat(n:i128,d:i128)->Rat{assert!(d!=0);let s=if d<0{-1}else{1};let g=gcd(n,d);Rat{n:s*n/g,d:d.abs()/g}}
fn add(a:Rat,b:Rat)->Rat{rat(a.n*b.d+b.n*a.d,a.d*b.d)}
fn mul(a:Rat,b:Rat)->Rat{rat(a.n*b.n,a.d*b.d)}
fn pow(mut a:Rat,mut n:usize)->Rat{let mut z=rat(1,1);while n>0{if n%2==1{z=mul(z,a);}a=mul(a,a);n/=2;}z}
fn binom(n:usize,k:usize)->i128{if k>n{return 0;}let mut z=1_i128;for i in 0..k{z=z*(n-i) as i128/(i+1) as i128;}z}

fn moments(points:&[(Rat,Rat)],nmax:usize)->Vec<Rat>{
    (0..=nmax).map(|n|points.iter().fold(rat(0,1),|z,&(x,w)|add(z,mul(w,pow(x,n))))).collect()
}

fn main(){
    let weights=[(rat(3,5),rat(4,5)),(rat(5,13),rat(12,13)),(rat(8,17),rat(15,17))];
    let mut cases=0usize;let mut congruence_entries=0usize;let mut gram_entries=0usize;let mut positive_atoms=0usize;
    for mode in 0..5_i128{
        let apts=[(rat(-2-mode,1),rat(1,3)),(rat(1,1),rat(1,3)),(rat(3+mode,1),rat(1,3))];
        let bpts=[(rat(-1-mode,1),rat(1,2)),(rat(2+mode,1),rat(1,2))];
        for &(alpha,beta) in &weights{for d in 1..=4usize{
            let ma=moments(&apts,2*d);let mb=moments(&bpts,2*d);
            let side=d+1;let prod_n=side*side;
            let mut g=vec![vec![rat(0,1);prod_n];prod_n];
            for i in 0..side{for j in 0..side{for k in 0..side{for l in 0..side{
                g[i*side+j][k*side+l]=mul(ma[i+k],mb[j+l]);
            }}}}
            let mut t=vec![vec![rat(0,1);side];prod_n];
            for k in 0..side{for i in 0..=k{let j=k-i;
                t[i*side+j][k]=mul(rat(binom(k,i),1),mul(pow(alpha,i),pow(beta,j)));
            }}
            let mz:Vec<Rat>=(0..=2*d).map(|n|(0..=n).fold(rat(0,1),|z,i|
                add(z,mul(rat(binom(n,i),1),mul(mul(pow(alpha,i),pow(beta,n-i)),mul(ma[i],mb[n-i]))))
            )).collect();
            let hz:Vec<Vec<Rat>>=(0..side).map(|i|(0..side).map(|j|mz[i+j]).collect()).collect();
            for p in 0..side{for q in 0..side{
                let mut x=rat(0,1);
                for i in 0..prod_n{for j in 0..prod_n{x=add(x,mul(mul(t[i][p],g[i][j]),t[j][q]));}}
                assert_eq!(x,hz[p][q]);congruence_entries+=1;
            }}
            // Exact positive Gram certificate from the product atoms:
            // H_Z[p,q]=sum_ab w_a w_b z_ab^p z_ab^q.
            for p in 0..side{for q in 0..side{
                let mut x=rat(0,1);
                for &(xa,wa) in &apts{for &(xb,wb) in &bpts{
                    assert!(wa.n>0&&wb.n>0);let z=add(mul(alpha,xa),mul(beta,xb));
                    x=add(x,mul(mul(wa,wb),mul(pow(z,p),pow(z,q))));
                }}
                assert_eq!(x,hz[p][q]);gram_entries+=1;
            }}
            positive_atoms+=apts.len()*bpts.len();cases+=1;
        }}
    }
    println!("{{");
    println!("  \"schema\": \"marici.hankel_cone_cut_congruence.v1\",");
    println!("  \"positive_merge_cases\": {cases},");
    println!("  \"exact_congruence_entries_checked\": {congruence_entries},");
    println!("  \"exact_positive_gram_entries_checked\": {gram_entries},");
    println!("  \"positive_product_atoms_certified\": {positive_atoms},");
    println!("  \"hankel_congruence_identity\": \"H_Z=T^T(H_X tensor H_Y)T\",");
    println!("  \"finite_hankel_cones_preserved\": true");
    println!("}}");
}
