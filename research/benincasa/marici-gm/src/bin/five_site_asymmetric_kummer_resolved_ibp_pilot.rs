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
fn grows_at_infinity(label:&str,mask:usize)->usize{
    if label=="G"{return 0}if label.starts_with("G_minus_e"){return 1}
    let cuts=cut_support(label);usize::from(((mask>>cuts[0])&1)==((mask>>cuts[1])&1))
}
fn in_cyclic_orbit(mut mask:usize,representative:usize)->bool{
    for _ in 0..5{if mask==representative{return true}mask=((mask<<1)&31)|((mask>>4)&1);}false
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
    let [u1,u2,u3]=u;let df=[
        [4*u1-2*u2,4*u2-2*u1-2*u3,2*u3-2*u2],
        [4*u1-2*u2-2,4*u2-2*u1-2*u3,2*u3-2*u2],
        [4*u1-2*u2,4*u2-2*u1-2*u3-2,2*u3-2*u2],
        [4*u1-2*u2,4*u2-2*u1-2*u3,2*u3-2*u2-2],
        [4*u1-2*u2+2,4*u2-2*u1-2*u3+2,2*u3-2*u2-8]];
    let mut dy=[[0_i64;3];5];for e in 0..5{if roots[e]==0{return None;}let d=inv(2*roots[e],p);
        for i in 0..3{dy[e][i]=mul(df[e][i].rem_euclid(p),d,p);}}Some(dy)
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
            a.swap(rank,pr);let pivot_inverse=inv(a[rank][col],p);
            for r in rank+1..rows{if a[r][col]!=0{
                let factor=mul(a[r][col],pivot_inverse,p);
                for j in col..=cols{a[r][j]=add(a[r][j],-mul(factor,a[rank][j],p),p);}
            }}
            rank+=1;
        }
    }
    let consistent=!(rank..rows).any(|r|(0..cols).all(|c|a[r][c]==0)&&a[r][cols]!=0);
    (rank,consistent)
}

fn inconsistency_certificate(mut a:Vec<Vec<i64>>,labels:&[[i32;4]],p:i64,cols:usize)->Value{
    let original=a.clone();let rows=a.len();let mut origins=(0..rows).collect::<Vec<_>>();
    let mut deps=vec![Vec::<(usize,i64)>::new();rows];let mut rank=0_usize;let mut bad=None;
    for col in 0..cols{
        let pivot=(rank..rows).find(|r|a[*r][col]!=0);
        if let Some(pr)=pivot{
            a.swap(rank,pr);origins.swap(rank,pr);deps.swap(rank,pr);
            let pivot_inverse=inv(a[rank][col],p);
            for r in rank+1..rows{if a[r][col]!=0{
                let factor=mul(a[r][col],pivot_inverse,p);
                for j in col..=cols{a[r][j]=add(a[r][j],-mul(factor,a[rank][j],p),p);}
                deps[r].push((rank,(-factor).rem_euclid(p)));
            }}rank+=1;
        }
    }
    for r in rank..rows{if(0..cols).all(|c|a[r][c]==0)&&a[r][cols]!=0{bad=Some(r);break;}}
    let bad=bad.expect("requested certificate for a consistent system");
    fn expand(row:usize,origins:&[usize],deps:&[Vec<(usize,i64)>],p:i64,memo:&mut[Option<Vec<(usize,i64)>>])->Vec<(usize,i64)>{
        if let Some(v)=&memo[row]{return v.clone();}
        let mut dense=std::collections::BTreeMap::new();dense.insert(origins[row],1_i64);
        for &(parent,factor) in &deps[row]{for (id,c) in expand(parent,origins,deps,p,memo){
            let next=add(*dense.get(&id).unwrap_or(&0),mul(factor,c,p),p);if next==0{dense.remove(&id);}else{dense.insert(id,next);}
        }}
        let out=dense.into_iter().collect::<Vec<_>>();memo[row]=Some(out.clone());out
    }
    let mut memo=vec![None;rows];let mut cert=expand(bad,&origins,&deps,p,&mut memo);
    let rhs=cert.iter().fold(0_i64,|s,(r,c)|add(s,mul(*c,original[*r][cols],p),p));
    let scale=inv(rhs,p);for (_,c) in &mut cert{*c=mul(*c,scale,p);}
    let verified=(0..cols).all(|j|cert.iter().fold(0_i64,|s,(r,c)|add(s,mul(*c,original[*r][j],p),p))==0)
        &&cert.iter().fold(0_i64,|s,(r,c)|add(s,mul(*c,original[*r][cols],p),p))==1;
    let terms=cert.iter().map(|(r,c)|json!({"row":r,"label":labels[*r],"coefficient":c})).collect::<Vec<_>>();
    json!({"verified":verified,"normalization":"certificate dot rhs = 1","trigger_original_row":origins[bad],
        "trigger_label":labels[origins[bad]],"nonzero_terms":terms.len(),"terms":terms})
}

fn nullspace_basis(mut a:Vec<Vec<i64>>,p:i64,cols:usize)->Vec<Vec<i64>>{
    let rows=a.len();let mut rank=0_usize;let mut pivots=Vec::new();
    for col in 0..cols{if let Some(pr)=(rank..rows).find(|r|a[*r][col]!=0){
        a.swap(rank,pr);let ip=inv(a[rank][col],p);
        for r in rank+1..rows{if a[r][col]!=0{let factor=mul(a[r][col],ip,p);
            for j in col..cols{a[r][j]=add(a[r][j],-mul(factor,a[rank][j],p),p);}
        }}pivots.push(col);rank+=1;
    }}
    let pivot_set=pivots.iter().copied().collect::<BTreeSet<_>>();let free=(0..cols).filter(|c|!pivot_set.contains(c)).collect::<Vec<_>>();
    let mut basis=Vec::with_capacity(free.len());
    for free_col in free{let mut x=vec![0_i64;cols];x[free_col]=1;
        for row in (0..rank).rev(){let pc=pivots[row];let mut sum=0_i64;
            for j in pc+1..cols{if a[row][j]!=0&&x[j]!=0{sum=add(sum,mul(a[row][j],x[j],p),p);}}
            x[pc]=mul((-sum).rem_euclid(p),inv(a[row][pc],p),p);
        }basis.push(x);
    }basis
}

fn solve_one(mut a:Vec<Vec<i64>>,p:i64,cols:usize)->Vec<i64>{
    let rows=a.len();let mut rank=0_usize;let mut pivots=Vec::new();
    for col in 0..cols{if let Some(pr)=(rank..rows).find(|r|a[*r][col]!=0){
        a.swap(rank,pr);let ip=inv(a[rank][col],p);
        for r in rank+1..rows{if a[r][col]!=0{let factor=mul(a[r][col],ip,p);
            for j in col..=cols{a[r][j]=add(a[r][j],-mul(factor,a[rank][j],p),p);}
        }}pivots.push(col);rank+=1;
    }}
    assert!(!(rank..rows).any(|r|(0..cols).all(|c|a[r][c]==0)&&a[r][cols]!=0));
    let mut x=vec![0_i64;cols];
    for row in (0..rank).rev(){let pc=pivots[row];let mut rhs=a[row][cols];
        for j in pc+1..cols{if a[row][j]!=0&&x[j]!=0{rhs=add(rhs,-mul(a[row][j],x[j],p),p);}}
        x[pc]=mul(rhs,inv(a[row][pc],p),p);
    }x
}

fn test(prime:i64,z:i64,degree:usize,impose_radial_kernel:bool,growth_filter:Option<usize>,orbit_filter:Option<usize>,common:&[String],terms:&[Vec<String>])->Value{
    let mons=monomials(degree);
    let mut fields=Vec::new();for i in 0..3{for mask in 0_usize..32{for exp in &mons{fields.push((i,mask,*exp));}}}
    // A complete 32-sheet orbit Fourier-separates the Kummer characters.
    // Independent base-point count is therefore controlled by the polynomial
    // monomial count, not by 32 times that count.
    let columns=1+fields.len();let target_points=3*mons.len()+24;
    let mut rows=Vec::new();let mut labels=Vec::<[i32;4]>::new();let mut attempts=0_i64;let mut accepted_points=0_usize;
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
            let mut row=vec![0_i64;columns+1];row[0]=omega;
            for (m,(i,mask,exp)) in fields.iter().enumerate(){
                let value=mul(pow(u[0],exp[0],prime),mul(pow(u[1],exp[1],prime),pow(u[2],exp[2],prime),prime),prime);
                let derivative=if exp[*i]==0{0}else{
                    let mut lowered=*exp;lowered[*i]-=1;
                    mul(exp[*i]as i64,mul(pow(u[0],lowered[0],prime),mul(pow(u[1],lowered[1],prime),pow(u[2],lowered[2],prime),prime),prime),prime)
                };
                let mut character=1_i64;let mut log_character=0_i64;
                for e in 0..5{if mask&(1<<e)!=0{character=mul(character,roots[e],prime);
                    log_character=add(log_character,mul(root_derivatives[e][*i],inv(roots[e],prime),prime),prime);}}
                let differentiated=add(derivative,mul(value,log_character,prime),prime);
                row[1+m]=mul(character,add(mul(differentiated,omega,prime),mul(value,du[*i],prime),prime),prime);
            }
            row[columns]=(-dz).rem_euclid(prime);orbit_rows.push(row);
        }
        if orbit_rows.len()==32{for sign_mask in 0..32{labels.push([0,accepted_points as i32,sign_mask,0]);}rows.extend(orbit_rows);accepted_points+=1;}
    }
    assert_eq!(accepted_points,target_points);
    let affine_row_count=rows.len();
    let mut radial_constraints=0_usize;
    if impose_radial_kernel{
        let mut direction_state=[101_i64,211_i64,307_i64];
        let mut accepted_directions=0_usize;let mut direction_attempts=0_usize;
        while accepted_directions<12&&direction_attempts<10_000{
            direction_attempts+=1;
            direction_state[0]=(37*direction_state[0]+11).rem_euclid(prime);
            direction_state[1]=(53*direction_state[1]+19).rem_euclid(prime);
            direction_state[2]=(71*direction_state[2]+23).rem_euclid(prime);
            let v=direction_state;
            let f=(2*v[0]*v[0]+2*v[1]*v[1]+v[2]*v[2]-2*v[0]*v[1]-2*v[1]*v[2]).rem_euclid(prime);
            let Some(root)=sqrt_mod(f,prime)else{continue;};if root==0{continue;}
            accepted_directions+=1;
            for sheet in 0_usize..32{
                let growth=terms.iter().map(|term|common.iter().chain(term).map(|label|grows_at_infinity(label,sheet)).sum::<usize>()).min().unwrap();
                if growth_filter.is_some()&&growth_filter!=Some(growth){continue;}
                if let Some(filter)=orbit_filter{
                    let admitted=if filter>=64{(filter-64)&(1<<sheet.count_ones())!=0}else{in_cyclic_orbit(sheet,filter)};
                    if !admitted{continue;}
                }
                for level in 0_i32..=9{
                    let mut row=vec![0_i64;columns+1];let mut active=false;
                    for (column,(i,character,exp)) in fields.iter().enumerate(){
                        let weight=character.count_ones()as i32;let polynomial_degree=exp.iter().sum::<usize>()as i32;
                        if polynomial_degree+weight+2-growth as i32!=level{continue;}
                        let sign=if(sheet&character).count_ones()%2==0{1}else{-1};
                        let monomial=mul(pow(v[0],exp[0],prime),mul(pow(v[1],exp[1],prime),pow(v[2],exp[2],prime),prime),prime);
                        row[1+column]=mul(sign,mul(pow(root,weight as usize,prime),mul(v[*i],monomial,prime),prime),prime);active=true;
                    }
                    if active{labels.push([1,accepted_directions as i32-1,sheet as i32,level]);rows.push(row);radial_constraints+=1;}
                }
            }
        }
        assert_eq!(accepted_directions,12);
    }
    if let Some(last_weight)=std::env::var("MARICI_LAST_WEIGHT").ok().and_then(|x|x.parse::<u32>().ok()){
        let mut boundary=rows.drain(affine_row_count..).zip(labels.drain(affine_row_count..)).collect::<Vec<_>>();
        boundary.sort_by_key(|(_,label)|((label[2] as u32).count_ones()==last_weight,label[1],label[2],label[3]));
        for(row,label)in boundary{rows.push(row);labels.push(label);}
    }
    let row_count=rows.len();
    let (rank_affine,consistent_affine)=matrix_rank(rows[..affine_row_count].to_vec(),prime,columns);
    let deck_audit=if std::env::var("MARICI_DECK_AUDIT").ok().as_deref()==Some("1"){
        let mut stacked=rows[..affine_row_count].to_vec();
        for row in &rows[..affine_row_count]{let mut transformed=row.clone();
            for (m,(_,character,_)) in fields.iter().enumerate(){if character.count_ones()%2==1{transformed[1+m]=(-transformed[1+m]).rem_euclid(prime);}}
            stacked.push(transformed);
        }
        let combined_rank=matrix_rank(stacked,prime,columns).0;
        Some(json!({"parity_transformed_combined_affine_rank":combined_rank,
            "affine_rank":rank_affine,"preserves_affine_kernel":combined_rank==rank_affine}))
    }else{None};
    let need_certificate=std::env::var("MARICI_CERTIFICATE").ok().as_deref()==Some("1")&&row_count>affine_row_count;
    let certificate=if need_certificate{Some(inconsistency_certificate(rows.clone(),&labels,prime,columns))}else{None};
    let torsor_complex=if std::env::var("MARICI_TORSOR_COMPLEX").ok().as_deref()==Some("1"){
        let weight_mask=orbit_filter.expect("torsor complex requires an encoded weight mask")-64;
        let active_weights=(1_u32..=4).filter(|w|weight_mask&(1<<w)!=0).collect::<Vec<_>>();
        assert_eq!(active_weights.len(),3);
        let pair_order=[[active_weights[0],active_weights[1]],[active_weights[0],active_weights[2]],[active_weights[1],active_weights[2]]];
        let mut bases=Vec::new();let mut dimensions=Vec::new();let mut sections=Vec::new();
        for pair in pair_order{
            let selected=rows.iter().zip(labels.iter()).filter(|(_,label)|label[0]==0||pair.contains(&(label[2]as u32).count_ones()))
                .map(|(row,_)|row.clone()).collect::<Vec<_>>();
            sections.push(solve_one(selected.clone(),prime,columns));
            let basis=nullspace_basis(selected,prime,columns);dimensions.push(basis.len());bases.extend(basis);
        }
        let sum_rank=matrix_rank(bases.iter().map(|v|{let mut r=v.clone();r.push(0);r}).collect(),prime,columns).0;
        let differences=[[0_usize,1_usize],[1,2]].map(|[i,j]|(0..columns).map(|c|add(sections[i][c],-sections[j][c],prime)).collect::<Vec<_>>());
        let mut with_classes=bases.clone();with_classes.extend(differences.clone());
        let class_span_rank=matrix_rank(with_classes.iter().map(|v|{let mut r=v.clone();r.push(0);r}).collect(),prime,columns).0-sum_rank;
        let individual_class_nonzero=differences.iter().map(|d|{
            let mut augmented=bases.clone();augmented.push(d.clone());
            matrix_rank(augmented.iter().map(|v|{let mut r=v.clone();r.push(0);r}).collect(),prime,columns).0>sum_rank
        }).collect::<Vec<_>>();
        Some(json!({"triple_weights":active_weights,"pair_order":pair_order,"pair_direction_dimensions":dimensions,
            "sum_rank":sum_rank,"ambient_affine_kernel_dimension":columns-rank_affine,
            "residual_quotient_dimension":columns-rank_affine-sum_rank,
            "difference_order":["x12-x13","x13-x23"],"individual_difference_classes_nonzero":individual_class_nonzero,
            "difference_class_span_rank":class_span_rank}))
    }else{None};
    let (rank,consistent)=if row_count==affine_row_count{(rank_affine,consistent_affine)}else{matrix_rank(rows,prime,columns)};
    json!({"prime":prime,"z":z,"vector_degree":degree,"kummer_characters":32,"impose_radial_kernel":impose_radial_kernel,"growth_filter":growth_filter,"orbit_filter":orbit_filter,
        "radial_constraints":radial_constraints,"unknowns":columns,"rows":row_count,"base_points":accepted_points,
        "rank_affine":rank_affine,"consistent_affine":consistent_affine,
        "rank":rank,"boundary_image_rank_on_affine_kernel":rank-rank_affine,"consistent":consistent,"attempts":attempts,
        "certificate":certificate,"torsor_complex":torsor_complex,"deck_audit":deck_audit})
}

fn main(){
    let source:Value=serde_json::from_str(&fs::read_to_string("../results/five-cycle-ofpt-packet.json").unwrap()).unwrap();
    let cycle=&source["five_cycle"];
    let common=cycle["common_prefactor"].as_array().unwrap().iter().map(|x|x.as_str().unwrap().to_owned()).collect::<Vec<_>>();
    let terms=cycle["terms"].as_array().unwrap().iter().map(|t|t.as_array().unwrap().iter().map(|x|x.as_str().unwrap().to_owned()).collect()).collect::<Vec<Vec<String>>>();
    let mut tests=Vec::new();
    let z=std::env::var("MARICI_Z").ok().and_then(|x|x.parse::<i64>().ok()).unwrap_or(13);
    let weight_mask=std::env::var("MARICI_WEIGHT_MASK").ok().and_then(|x|x.parse::<usize>().ok()).unwrap_or(14);
    tests.push(test(1019,z,3,true,Some(4),Some(64+weight_mask),&common,&terms));
    let packet=json!({"schema":"marici.benincasa.five_site.asymmetric.kummer_resolved_ibp_pilot.v1",
        "ansatz":"full-Kummer affine IBP at the declared polynomial degree; generic-rank gate required before interpreting consistency",
        "tests":tests,
        "interpretation":"Inconsistency at a generic fiber falsifies the bounded polynomial-vector-field ansatz at that degree. Consistency is discovery evidence requiring reconstruction in z."
    });
    fs::write("../results/five-site-asymmetric-kummer-resolved-ibp-pilot.json",serde_json::to_string_pretty(&packet).unwrap()+"\n").unwrap();
    println!("{}",serde_json::to_string(&packet["tests"]).unwrap());
}
