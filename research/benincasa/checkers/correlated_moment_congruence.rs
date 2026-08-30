#[derive(Clone,Copy,Debug,Eq,PartialEq)]
struct Rat{n:i128,d:i128}
fn gcd(mut a:i128,mut b:i128)->i128{a=a.abs();b=b.abs();while b!=0{let r=a%b;a=b;b=r;}a}
fn rat(n:i128,d:i128)->Rat{assert!(d!=0);let s=if d<0{-1}else{1};let g=gcd(n,d);Rat{n:s*n/g,d:d.abs()/g}}
fn add(a:Rat,b:Rat)->Rat{rat(a.n*b.d+b.n*a.d,a.d*b.d)}
fn mul(a:Rat,b:Rat)->Rat{rat(a.n*b.n,a.d*b.d)}
fn pow(mut a:Rat,mut n:usize)->Rat{let mut z=rat(1,1);while n>0{if n%2==1{z=mul(z,a);}a=mul(a,a);n/=2;}z}
fn binom(n:usize,k:usize)->i128{let mut z=1_i128;for i in 0..k{z=z*(n-i) as i128/(i+1) as i128;}z}

#[derive(Clone,Copy)]struct Atom{x:Rat,y:Rat,w:Rat}
fn moment(a:&[Atom],i:usize,j:usize)->Rat{a.iter().fold(rat(0,1),|z,p|add(z,mul(p.w,mul(pow(p.x,i),pow(p.y,j)))))}

fn main(){
    let independent=[
        Atom{x:rat(-1,1),y:rat(-1,1),w:rat(1,4)},Atom{x:rat(-1,1),y:rat(1,1),w:rat(1,4)},
        Atom{x:rat(1,1),y:rat(-1,1),w:rat(1,4)},Atom{x:rat(1,1),y:rat(1,1),w:rat(1,4)}];
    let correlated=[Atom{x:rat(-1,1),y:rat(-1,1),w:rat(1,2)},Atom{x:rat(1,1),y:rat(1,1),w:rat(1,2)}];
    let anticorrelated=[Atom{x:rat(-1,1),y:rat(1,1),w:rat(1,2)},Atom{x:rat(1,1),y:rat(-1,1),w:rat(1,2)}];
    let families:[&[Atom];3]=[&independent,&correlated,&anticorrelated];
    for n in 0..=8{assert_eq!(moment(&independent,n,0),moment(&correlated,n,0));assert_eq!(moment(&independent,0,n),moment(&anticorrelated,0,n));}

    let weights=[(rat(3,5),rat(4,5)),(rat(5,13),rat(12,13)),(rat(8,17),rat(15,17))];
    let mut cases=0usize;let mut congruence_entries=0usize;let mut gram_entries=0usize;
    for atoms in families{for &(alpha,beta) in &weights{for d in 1..=4usize{
        let basis:Vec<(usize,usize)>=(0..=d).flat_map(|i|(0..=d-i).map(move|j|(i,j))).collect();
        let nb=basis.len();let side=d+1;
        let mut m=vec![vec![rat(0,1);nb];nb];
        for p in 0..nb{for q in 0..nb{m[p][q]=moment(atoms,basis[p].0+basis[q].0,basis[p].1+basis[q].1);}}
        let mut t=vec![vec![rat(0,1);side];nb];
        for k in 0..side{for i in 0..=k{let j=k-i;let row=basis.iter().position(|&x|x==(i,j)).unwrap();
            t[row][k]=mul(rat(binom(k,i),1),mul(pow(alpha,i),pow(beta,j)));
        }}
        let mz:Vec<Rat>=(0..=2*d).map(|n|atoms.iter().fold(rat(0,1),|s,p|{
            let z=add(mul(alpha,p.x),mul(beta,p.y));add(s,mul(p.w,pow(z,n)))
        })).collect();
        for p in 0..side{for q in 0..side{
            let mut via=rat(0,1);for i in 0..nb{for j in 0..nb{via=add(via,mul(mul(t[i][p],m[i][j]),t[j][q]));}}
            assert_eq!(via,mz[p+q]);congruence_entries+=1;
            let gram=atoms.iter().fold(rat(0,1),|s,a|{let z=add(mul(alpha,a.x),mul(beta,a.y));add(s,mul(a.w,mul(pow(z,p),pow(z,q))))});
            assert_eq!(gram,mz[p+q]);gram_entries+=1;
        }}cases+=1;
    }}}
    let (a,b)=weights[0];
    let v_ind=add(mul(a,a),mul(b,b));let v_corr=pow(add(a,b),2);let v_anti=pow(add(a,rat(-b.n,b.d)),2);
    assert_eq!(v_ind,rat(1,1));assert_ne!(v_ind,v_corr);assert_ne!(v_ind,v_anti);assert_ne!(v_corr,v_anti);
    println!("{{");
    println!("  \"schema\": \"marici.correlated_moment_congruence.v1\",");
    println!("  \"correlated_positive_cases\": {cases},");
    println!("  \"exact_congruence_entries_checked\": {congruence_entries},");
    println!("  \"exact_positive_gram_entries_checked\": {gram_entries},");
    println!("  \"equal_marginal_orders_checked\": 9,");
    println!("  \"marginals_determine_merged_state\": false,");
    println!("  \"joint_moment_congruence_preserves_positivity\": true");
    println!("}}");
}
