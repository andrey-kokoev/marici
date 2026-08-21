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

fn root_du(u:[i64;3],roots:[i64;5],p:i64)->Option<[[i64;3];5]>{
    let [u1,u2,u3]=u;
    let df=[
        [4*u1-2*u2,4*u2-2*u1-2*u3,2*u3-2*u2],
        [4*u1-2*u2-2,4*u2-2*u1-2*u3,2*u3-2*u2],
        [4*u1-2*u2,4*u2-2*u1-2*u3-2,2*u3-2*u2],
        [4*u1-2*u2,4*u2-2*u1-2*u3,2*u3-2*u2-2],
        [4*u1-2*u2+2,4*u2-2*u1-2*u3+2,2*u3-2*u2-8],
    ];
    let mut dy=[[0_i64;3];5];
    for e in 0..5{if roots[e]==0{return None;}let den=inv(2*roots[e],p);
        for i in 0..3{dy[e][i]=mul(df[e][i].rem_euclid(p),den,p);}}
    Some(dy)
}

fn omega_jet(z:i64,u:[i64;3],roots:[i64;5],common:&[String],terms:&[Vec<String>],p:i64)
    ->Option<(i64,i64,[i64;3])>{
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
    let mut omega=0;let mut dz_omega=0;let mut du_omega=[0;3];
    for labels in all_terms{
        let mut reciprocal=1;let mut log_z=0;let mut log_u=[0;3];
        for label in labels{
            let (q,qz,qu)=wall(label,z,&roots,&dy,p)?;
            let iq=inv(q,p);
            reciprocal=mul(reciprocal,iq,p);
            log_z=add(log_z,mul(qz,iq,p),p);
            for i in 0..3{log_u[i]=add(log_u[i],mul(qu[i],iq,p),p);}
        }
        omega=add(omega,reciprocal,p);
        dz_omega=add(dz_omega,-mul(reciprocal,log_z,p),p);
        for i in 0..3{du_omega[i]=add(du_omega[i],-mul(reciprocal,log_u[i],p),p);}
    }
    if omega==0{None}else{Some((omega,dz_omega,du_omega))}
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

fn test(prime:i64,z:i64,degree:usize,pole:&str,common:&[String],terms:&[Vec<String>])->Value{
    let mons=monomials(degree);
    let fields=(0..3).flat_map(|i|mons.iter().copied().map(move |exp|(i,exp))).collect::<Vec<_>>();
    let columns=1+fields.len();let target_points=columns+24;
    let mut rows=Vec::new();let mut attempts=0_i64;let mut accepted_points=0_usize;
    let mut state=[17_i64,29_i64,43_i64];
    while accepted_points<target_points&&attempts<200_000{
        attempts+=1;
        state[0]=(37*state[0]+11).rem_euclid(prime);
        state[1]=(53*state[1]+19).rem_euclid(prime);
        state[2]=(71*state[2]+23).rem_euclid(prime);
        let u=state;
        let u1=u[0];let u2=u[1];let u3=u[2];
        let f1=(2*u1*u1+2*u2*u2+u3*u3-2*u1*u2-2*u2*u3).rem_euclid(prime);
        let f=[f1,(f1-2*u1+1).rem_euclid(prime),(f1-2*u2+2).rem_euclid(prime),
            (f1-2*u3+3).rem_euclid(prime),(f1+2*u1+2*u2-8*u3+29).rem_euclid(prime)];
        let Some(base_roots)=f.map(|x|sqrt_mod(x,prime)).into_iter().collect::<Option<Vec<_>>>() else{continue;};
        let mut orbit_rows=Vec::new();
        for sign_mask in 0_usize..32{
            let roots:[i64;5]=std::array::from_fn(|e|if sign_mask&(1<<e)==0{base_roots[e]}else{-base_roots[e]});
            let Some((omega,dz,du))=omega_jet(z,u,roots,common,terms,prime)else{continue;};
            let Some(root_derivatives)=root_du(u,roots,prime)else{continue;};
            let Some((q,_,q_du))=wall(pole,z,&roots,&root_derivatives,prime)else{continue;};
            let iq=inv(q,prime);let iq2=mul(iq,iq,prime);
            let mut row=vec![0_i64;columns+1];row[0]=omega;
            for (m,(i,exp)) in fields.iter().enumerate(){
                let value=mul(pow(u[0],exp[0],prime),mul(pow(u[1],exp[1],prime),pow(u[2],exp[2],prime),prime),prime);
                let derivative=if exp[*i]==0{0}else{
                    let mut lowered=*exp;lowered[*i]-=1;
                    mul(exp[*i]as i64,mul(pow(u[0],lowered[0],prime),mul(pow(u[1],lowered[1],prime),pow(u[2],lowered[2],prime),prime),prime),prime)
                };
                let derivative_over_q=add(mul(derivative,iq,prime),-mul(mul(value,q_du[*i],prime),iq2,prime),prime);
                row[1+m]=add(mul(derivative_over_q,omega,prime),mul(mul(value,iq,prime),du[*i],prime),prime);
            }
            row[columns]=(-dz).rem_euclid(prime);orbit_rows.push(row);
        }
        if orbit_rows.len()==32{rows.extend(orbit_rows);accepted_points+=1;}
    }
    assert_eq!(accepted_points,target_points);
    let row_count=rows.len();
    let no_scalar=rows.iter().map(|row|{
        let mut reduced=row[1..columns].to_vec();
        reduced.push(row[columns]);
        reduced
    }).collect::<Vec<_>>();
    let (rank_no_scalar,consistent_no_scalar)=matrix_rank(no_scalar,prime,columns-1);
    let (rank,consistent)=matrix_rank(rows,prime,columns);
    json!({"prime":prime,"z":z,"vector_degree":degree,"pole":pole,"unknowns":columns,"rows":row_count,"base_points":accepted_points,
        "rank":rank,"consistent":consistent,"rank_no_scalar":rank_no_scalar,
        "consistent_no_scalar":consistent_no_scalar,"scalar_coefficient_required":consistent&&!consistent_no_scalar,"attempts":attempts})
}

fn main(){
    let source:Value=serde_json::from_str(&fs::read_to_string("../results/five-cycle-ofpt-packet.json").unwrap()).unwrap();
    let cycle=&source["five_cycle"];
    let common=cycle["common_prefactor"].as_array().unwrap().iter().map(|x|x.as_str().unwrap().to_owned()).collect::<Vec<_>>();
    let terms=cycle["terms"].as_array().unwrap().iter().map(|t|t.as_array().unwrap().iter().map(|x|x.as_str().unwrap().to_owned()).collect()).collect::<Vec<Vec<String>>>();
    let poles=common.iter().chain(terms.iter().flatten()).cloned().collect::<BTreeSet<_>>();
    let mut tests=Vec::new();
    for (prime,z) in [(1009,7),(1013,11)]{for pole in &poles{tests.push(test(prime,z,2,pole,&common,&terms));}}
    let packet=json!({"schema":"marici.benincasa.five_site.asymmetric.single_wall_logarithmic_ibp_pilot.v1",
        "ansatz":"d_z Omega + a(z) Omega = sum_i d_ui(P_i Omega/L), P_i polynomial of total degree <=1 and L one frozen labelled wall",
        "tests":tests,
        "interpretation":"Inconsistency at a generic fiber falsifies the bounded polynomial-vector-field ansatz at that degree. Consistency is discovery evidence requiring reconstruction in z."
    });
    fs::write("../results/five-site-asymmetric-logarithmic-ibp-pilot.json",serde_json::to_string_pretty(&packet).unwrap()+"\n").unwrap();
    println!("{}",serde_json::to_string(&packet["tests"]).unwrap());
}