use serde_json::{json, Value};
use std::{collections::BTreeSet, fs};

fn add(a:i64,b:i64,p:i64)->i64{(a+b).rem_euclid(p)}
fn mul(a:i64,b:i64,p:i64)->i64{((a as i128*b as i128)%p as i128) as i64}
fn pow(mut a:i64,mut n:usize,p:i64)->i64{let mut r=1;while n>0{if n&1==1{r=mul(r,a,p);}a=mul(a,a,p);n>>=1;}r}
fn inv(a:i64,p:i64)->i64{pow(a.rem_euclid(p),(p-2)as usize,p)}
fn sqrt_mod(a:i64,p:i64)->Option<i64>{let a=a.rem_euclid(p);(0..p).find(|x|mul(*x,*x,p)==a)}

fn cut_support(label:&str)->Vec<usize>{
    let sites=label.strip_prefix("g_").unwrap().chars()
        .map(|d|d.to_digit(10).unwrap()as usize-1).collect::<BTreeSet<_>>();
    (0..5).filter(|e|sites.contains(e)!=sites.contains(&((e+1)%5))).collect()
}

fn wall(label:&str,z:i64,y:&[i64;5],dy:&[[i64;3];5],p:i64)->Option<(i64,i64,[i64;3])>{
    let (value,dz,du)=if label=="G"{
        (5*z,5,[0;3])
    }else if let Some(edge)=label.strip_prefix("G_minus_e"){
        let e=edge.chars().next().unwrap().to_digit(10).unwrap()as usize-1;
        let mut du=[0;3];for i in 0..3{du[i]=2*dy[e][i];}
        (5*z+2*y[e],5,du)
    }else{
        let size=label.strip_prefix("g_").unwrap().len()as i64;
        let cuts=cut_support(label);
        let mut du=[0;3];for i in 0..3{du[i]=dy[cuts[0]][i]+dy[cuts[1]][i];}
        (size*z+y[cuts[0]]+y[cuts[1]],size,du)
    };
    let value=value.rem_euclid(p);
    if value==0{None}else{Some((value,dz.rem_euclid(p),du.map(|x|x.rem_euclid(p))))}
}

fn omega_jet(z:i64,u:[i64;3],roots:[i64;5],common:&[String],terms:&[Vec<String>],p:i64,max_order:usize)
    ->Option<(Vec<i64>,[i64;3])>{
    let [u1,u2,u3]=u;
    let df=[
        [4*u1-2*u2,4*u2-2*u1-2*u3,2*u3-2*u2],
        [4*u1-2*u2-2,4*u2-2*u1-2*u3,2*u3-2*u2],
        [4*u1-2*u2,4*u2-2*u1-2*u3-2,2*u3-2*u2],
        [4*u1-2*u2,4*u2-2*u1-2*u3,2*u3-2*u2-2],
        [4*u1-2*u2+2,4*u2-2*u1-2*u3+2,2*u3-2*u2-8],
    ];
    let mut dy=[[0_i64;3];5];
    for e in 0..5{
        if roots[e]==0{return None;}
        let denominator=inv(2*roots[e],p);
        for i in 0..3{dy[e][i]=mul(df[e][i].rem_euclid(p),denominator,p);}
    }
    let all_terms=terms.iter().map(|selected|common.iter().chain(selected.iter())).collect::<Vec<_>>();
    let mut orders=vec![0_i64;max_order+1];let mut du_omega=[0;3];
    for labels in all_terms{
        let mut reciprocal=1;let mut powers=vec![0_i64;max_order+1];let mut log_u=[0;3];
        for label in labels{
            let (q,qz,qu)=wall(label,z,&roots,&dy,p)?;
            let iq=inv(q,p);
            reciprocal=mul(reciprocal,iq,p);
            let x=mul(qz,iq,p);let mut x_power=1;
            for n in 1..=max_order{x_power=mul(x_power,x,p);powers[n]=add(powers[n],x_power,p);}
            for i in 0..3{log_u[i]=add(log_u[i],mul(qu[i],iq,p),p);}
        }
        let mut h=vec![0_i64;max_order+1];h[0]=1;
        for n in 1..=max_order{let mut sum=0;for m in 1..=n{sum=add(sum,mul(powers[m],h[n-m],p),p);}h[n]=mul(sum,inv(n as i64,p),p);}
        let mut factorial=1_i64;
        for n in 0..=max_order{if n>0{factorial=mul(factorial,n as i64,p);}let signed=if n%2==0{factorial}else{-factorial};orders[n]=add(orders[n],mul(reciprocal,mul(signed,h[n],p),p),p);}
        for i in 0..3{du_omega[i]=add(du_omega[i],-mul(reciprocal,log_u[i],p),p);}
    }
    if orders[0]==0{None}else{Some((orders,du_omega))}
}

fn monomials(degree:usize)->Vec<[usize;3]>{
    let mut out=Vec::new();
    for a in 0..=degree{for b in 0..=degree-a{for c in 0..=degree-a-b{out.push([a,b,c]);}}}
    out
}

fn matrix_rank(mut a:Vec<Vec<i64>>,p:i64,coefficient_columns:usize)->(usize,bool){
    let rows=a.len();let cols=coefficient_columns;let mut rank=0;
    for col in 0..cols{
        let pivot=(rank..rows).find(|r|a[*r][col]!=0);
        if let Some(pr)=pivot{
            a.swap(rank,pr);let scale=inv(a[rank][col],p);
            for j in col..=cols{a[rank][j]=mul(a[rank][j],scale,p);}
            for r in 0..rows{if r!=rank&&a[r][col]!=0{
                let factor=a[r][col];
                for j in col..=cols{a[r][j]=add(a[r][j],-mul(factor,a[rank][j],p),p);}
            }}
            rank+=1;
        }
    }
    let consistent=!(rank..rows).any(|r|(0..cols).all(|c|a[r][c]==0)&&a[r][cols]!=0);
    (rank,consistent)
}
fn test(prime:i64,z:i64,degree:usize,max_order:usize,common:&[String],terms:&[Vec<String>])->Value{
    let mons=monomials(degree);
    let fields=(0..3).flat_map(|i|mons.iter().copied().filter(move |exp|exp[i]>0).map(move |exp|(i,exp))).collect::<Vec<_>>();
    let exact_columns=fields.len();let target_points=exact_columns+max_order+32;
    let mut rows=Vec::new();let mut attempts=0_i64;let mut accepted_points=0_usize;
    let mut state=[17_i64,29_i64,43_i64];
    while accepted_points<target_points&&attempts<300_000{
        attempts+=1;
        state[0]=(37*state[0]+11).rem_euclid(prime);
        state[1]=(53*state[1]+19).rem_euclid(prime);
        state[2]=(71*state[2]+23).rem_euclid(prime);
        let u=state;let [u1,u2,u3]=u;
        let f1=(2*u1*u1+2*u2*u2+u3*u3-2*u1*u2-2*u2*u3).rem_euclid(prime);
        let f=[f1,(f1-2*u1+1).rem_euclid(prime),(f1-2*u2+2).rem_euclid(prime),
            (f1-2*u2+2).rem_euclid(prime),(f1-2*u3+3).rem_euclid(prime),
            (f1+2*u1+2*u2-8*u3+29).rem_euclid(prime)];
        let f=[f[0],f[1],f[2],f[4],f[5]];
        let Some(base_roots)=f.map(|x|sqrt_mod(x,prime)).into_iter().collect::<Option<Vec<_>>>() else{continue;};
        let mut orbit_rows=Vec::new();
        for sign_mask in 0_usize..32{
            let roots:[i64;5]=std::array::from_fn(|e|if sign_mask&(1<<e)==0{base_roots[e]}else{-base_roots[e]});
            let Some((orders,du))=omega_jet(z,u,roots,common,terms,prime,max_order)else{continue;};
            let omega=orders[0];let mut row=vec![0_i64;exact_columns+max_order+1];
            for (m,(i,exp)) in fields.iter().enumerate(){
                let value=mul(pow(u[0],exp[0],prime),mul(pow(u[1],exp[1],prime),pow(u[2],exp[2],prime),prime),prime);
                let derivative=if exp[*i]==0{0}else{let mut lowered=*exp;lowered[*i]-=1;
                    mul(exp[*i]as i64,mul(pow(u[0],lowered[0],prime),mul(pow(u[1],lowered[1],prime),pow(u[2],lowered[2],prime),prime),prime),prime)};
                row[m]=add(mul(derivative,omega,prime),mul(value,du[*i],prime),prime);
            }
            for k in 0..=max_order{row[exact_columns+k]=orders[k];}
            orbit_rows.push(row);
        }
        if orbit_rows.len()==32{rows.extend(orbit_rows);accepted_points+=1;}
    }
    assert_eq!(accepted_points,target_points);
    let rank_of=|derivative_count:usize|{
        let cols=exact_columns+derivative_count;
        let matrix=rows.iter().map(|row|{let mut out=row[..cols].to_vec();out.push(0);out}).collect::<Vec<_>>();
        matrix_rank(matrix,prime,cols).0
    };
    let rank_exact=rank_of(0);let mut growth=Vec::new();
    for k in 0..=max_order{let rank=rank_of(k+1);growth.push(json!({
        "max_derivative_order":k,"total_rank":rank,"quotient_rank":rank-rank_exact
    }));}
    json!({"prime":prime,"z":z,"vector_degree":degree,"max_order":max_order,
        "exact_columns":exact_columns,"rank_exact":rank_exact,"rows":rows.len(),
        "base_points":accepted_points,"attempts":attempts,"growth":growth})
}

fn main(){
    let source:Value=serde_json::from_str(&fs::read_to_string("../results/five-cycle-ofpt-packet.json").unwrap()).unwrap();
    let cycle=&source["five_cycle"];
    let common=cycle["common_prefactor"].as_array().unwrap().iter().map(|x|x.as_str().unwrap().to_owned()).collect::<Vec<_>>();
    let terms=cycle["terms"].as_array().unwrap().iter().map(|t|t.as_array().unwrap().iter().map(|x|x.as_str().unwrap().to_owned()).collect()).collect::<Vec<Vec<String>>>();
    let tests=[(1009,7),(1013,11)].into_iter().map(|(p,z)|test(p,z,5,12,&common,&terms)).collect::<Vec<_>>();
    let packet=json!({"schema":"marici.benincasa.five_site.asymmetric.derivative_rank_growth.v1",
        "quotient":"successive z-derivatives modulo polynomial divergence image of vector degree <=5",
        "deck_sheets":32,"tests":tests});
    fs::write("../results/five-site-asymmetric-derivative-rank-growth.json",serde_json::to_string_pretty(&packet).unwrap()+"\n").unwrap();
    println!("{}",serde_json::to_string(&packet["tests"]).unwrap());
}