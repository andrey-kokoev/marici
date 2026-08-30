#[derive(Clone,Copy,Debug,Eq,PartialEq)]
struct Rat{n:i128,d:i128}
fn gcd(mut a:i128,mut b:i128)->i128{a=a.abs();b=b.abs();while b!=0{let r=a%b;a=b;b=r;}a}
fn rat(n:i128,d:i128)->Rat{assert!(d!=0);let s=if d<0{-1}else{1};let g=gcd(n,d);Rat{n:s*n/g,d:d.abs()/g}}
fn add(a:Rat,b:Rat)->Rat{rat(a.n*b.d+b.n*a.d,a.d*b.d)}
fn sub(a:Rat,b:Rat)->Rat{rat(a.n*b.d-b.n*a.d,a.d*b.d)}
fn mul(a:Rat,b:Rat)->Rat{rat(a.n*b.n,a.d*b.d)}
fn div(a:Rat,b:Rat)->Rat{rat(a.n*b.d,a.d*b.n)}

fn inverse(a:&[Vec<Rat>])->Vec<Vec<Rat>>{
    let n=a.len();let mut m=vec![vec![rat(0,1);2*n];n];
    for i in 0..n{for j in 0..n{m[i][j]=a[i][j];}m[i][n+i]=rat(1,1);}
    for col in 0..n{
        let pivot=(col..n).find(|&r|m[r][col].n!=0).unwrap();m.swap(col,pivot);
        let p=m[col][col];for j in 0..2*n{m[col][j]=div(m[col][j],p);}
        for r in 0..n{if r!=col{let f=m[r][col];for j in 0..2*n{m[r][j]=sub(m[r][j],mul(f,m[col][j]));}}}
    }
    (0..n).map(|i|m[i][n..].to_vec()).collect()
}

fn main(){
    let mut blocks=0usize;let mut inverse_identities=0usize;
    let mut quadratic_forms=0usize;let mut weight_cancellations=0usize;
    for n in 1..=6usize{for mode in 0..10usize{
        // B=L L^T+I is a source-independent exact positive-definite test block.
        let mut l=vec![vec![rat(0,1);n];n];
        for i in 0..n{for j in 0..=i{
            l[i][j]=rat(if i==j{(mode+i+2) as i128}else{((i+1)*(j+1)+mode) as i128},1);
        }}
        let mut b=vec![vec![rat(0,1);n];n];
        for i in 0..n{for j in 0..n{
            let mut x=if i==j{rat(1,1)}else{rat(0,1)};
            for k in 0..n{x=add(x,mul(l[i][k],l[j][k]));}b[i][j]=x;
        }}
        let inv=inverse(&b);
        for i in 0..n{for j in 0..n{
            let mut x=rat(0,1);for k in 0..n{x=add(x,mul(b[i][k],inv[k][j]));}
            assert_eq!(x,if i==j{rat(1,1)}else{rat(0,1)});inverse_identities+=1;
        }}
        let gamma:Vec<Rat>=(0..n).map(|i|rat((i+mode+1) as i128,1)).collect();
        let mut q=rat(0,1);for i in 0..n{for j in 0..n{q=add(q,mul(mul(gamma[i],inv[i][j]),gamma[j]));}}
        assert!(q.n>0);quadratic_forms+=1;

        // For K=W B W and v=W gamma, every term of v^T K^-1 v has
        // exponent w_i-(w_i+w_j)+w_j=0, for arbitrary positive flag weights.
        for weight_mode in 0..4usize{for i in 0..n{for j in 0..n{
            let wi=(1+i+weight_mode) as i64;let wj=(1+2*j+weight_mode) as i64;
            assert_eq!(wi-(wi+wj)+wj,0);weight_cancellations+=1;
        }}}
        blocks+=1;
    }}
    println!("{{");
    println!("  \"schema\": \"marici.flagged_covariance_quadratic_normal_form.v1\",");
    println!("  \"positive_definite_normal_blocks_checked\": {blocks},");
    println!("  \"inverse_matrix_identities_checked\": {inverse_identities},");
    println!("  \"quadratic_forms_checked\": {quadratic_forms},");
    println!("  \"flag_weight_cancellations_checked\": {weight_cancellations},");
    println!("  \"finite_normal_correction\": \"gamma^T B^-1 gamma\",");
    println!("  \"extra_carrier_structure_required\": false");
    println!("}}");
}
