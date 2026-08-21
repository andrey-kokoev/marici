use serde_json::{json,Value};
use std::{collections::{BTreeMap,BTreeSet},fs};

fn add(a:i64,b:i64,p:i64)->i64{(a+b).rem_euclid(p)}
fn mul(a:i64,b:i64,p:i64)->i64{((a as i128*b as i128)%p as i128)as i64}
fn pow(mut a:i64,mut n:usize,p:i64)->i64{let mut r=1;while n>0{if n&1==1{r=mul(r,a,p);}a=mul(a,a,p);n>>=1;}r}
fn inv(a:i64,p:i64)->i64{pow(a.rem_euclid(p),(p-2)as usize,p)}

fn cut_support(label:&str)->Vec<usize>{
    let sites=label.strip_prefix("g_").unwrap().chars().map(|d|d.to_digit(10).unwrap()as usize-1).collect::<BTreeSet<_>>();
    (0..5).filter(|e|sites.contains(e)!=sites.contains(&((e+1)%5))).collect()
}
fn grows(label:&str,mask:usize)->usize{if label=="G"{0}else if label.starts_with("G_minus_e"){1}else{
    let c=cut_support(label);usize::from(((mask>>c[0])&1)==((mask>>c[1])&1))}}

fn rotate5(mask:usize)->usize{((mask<<1)&31)|(mask>>4)}
fn orbit_rep(mut mask:usize)->usize{let mut rep=mask;for _ in 1..5{mask=rotate5(mask);rep=rep.min(mask);}rep}
fn cycle_cut_size(mask:usize)->usize{(0..5).filter(|i|((mask>>i)&1)!=((mask>>((i+1)%5))&1)).count()}

fn wall(label:&str,z:i64,y:&[i64;5],p:i64)->Option<(i64,i64,[i64;5])>{
    let(mut q,qz,mut ds)=if label=="G"{(5*z,5,[0;5])}else if let Some(edge)=label.strip_prefix("G_minus_e"){
        let e=edge.chars().next().unwrap().to_digit(10).unwrap()as usize-1;let mut d=[0;5];d[e]=inv(y[e],p);(5*z+2*y[e],5,d)
    }else{let size=label.strip_prefix("g_").unwrap().len()as i64;let c=cut_support(label);let mut d=[0;5];
        d[c[0]]=mul(inv(2*y[c[0]],p),1,p);d[c[1]]=mul(inv(2*y[c[1]],p),1,p);(size*z+y[c[0]]+y[c[1]],size,d)};
    q=q.rem_euclid(p);ds=ds.map(|x|x.rem_euclid(p));if q==0{None}else{Some((q,qz,ds))}
}

fn omega_jet(z:i64,y:[i64;5],common:&[String],terms:&[Vec<String>],p:i64)->Option<(i64,i64,[i64;5])>{
    if y.contains(&0){return None;}let mut omega=0;let mut dz=0;let mut ds=[0;5];
    for selected in terms{let mut reciprocal=1;let mut lz=0;let mut ls=[0;5];
        for label in common.iter().chain(selected.iter()){let(q,qz,qd)=wall(label,z,&y,p)?;let iq=inv(q,p);
            reciprocal=mul(reciprocal,iq,p);lz=add(lz,mul(qz,iq,p),p);for i in 0..5{ls[i]=add(ls[i],mul(qd[i],iq,p),p);}}
        omega=add(omega,reciprocal,p);dz=add(dz,-mul(reciprocal,lz,p),p);for i in 0..5{ds[i]=add(ds[i],-mul(reciprocal,ls[i],p),p);}
    }if omega==0{None}else{Some((omega,dz,ds))}
}

fn monomials(degree:usize)->Vec<[usize;5]>{let mut out=Vec::new();
    for a in 0..=degree{for b in 0..=degree-a{for c in 0..=degree-a-b{for d in 0..=degree-a-b-c{for e in 0..=degree-a-b-c-d{out.push([a,b,c,d,e]);}}}}}out}
fn monomial(s:&[i64;5],e:&[usize;5],p:i64)->i64{(0..5).fold(1,|r,i|mul(r,pow(s[i],e[i],p),p))}
fn rotate_exp(e:[usize;5])->[usize;5]{[e[4],e[0],e[1],e[2],e[3]]}
fn exp_orbit_rep(mut e:[usize;5])->[usize;5]{let mut rep=e;for _ in 1..5{e=rotate_exp(e);rep=rep.min(e);}rep}
fn orbit_monomial(y:&[i64;5],e:[usize;5],p:i64)->i64{let mut seen=BTreeSet::new();let mut cur=e;let mut out=0;for _ in 0..5{if seen.insert(cur){out=add(out,monomial(y,&cur,p),p);}cur=rotate_exp(cur);}out}

fn rank(mut a:Vec<Vec<i64>>,p:i64,cols:usize)->(usize,bool){let rows=a.len();let mut r=0;
    for c in 0..cols{if let Some(pr)=(r..rows).find(|i|a[*i][c]!=0){a.swap(r,pr);let ip=inv(a[r][c],p);
        for i in r+1..rows{if a[i][c]!=0{let f=mul(a[i][c],ip,p);for j in c..=cols{a[i][j]=add(a[i][j],-mul(f,a[r][j],p),p);}}}r+=1;}}
    let ok=!(r..rows).any(|i|(0..cols).all(|c|a[i][c]==0)&&a[i][cols]!=0);(r,ok)}

fn solve_unique(mut a:Vec<Vec<i64>>,p:i64,cols:usize)->Vec<i64>{let rows=a.len();let mut r=0;let mut pivots=Vec::new();
    for c in 0..cols{if let Some(pr)=(r..rows).find(|i|a[*i][c]!=0){a.swap(r,pr);let ip=inv(a[r][c],p);
        for i in r+1..rows{if a[i][c]!=0{let f=mul(a[i][c],ip,p);for j in c..=cols{a[i][j]=add(a[i][j],-mul(f,a[r][j],p),p);}}}pivots.push(c);r+=1;}}
    assert_eq!(r,cols);let mut x=vec![0_i64;cols];for row in(0..r).rev(){let c=pivots[row];let mut rhs=a[row][cols];
        for j in c+1..cols{rhs=add(rhs,-mul(a[row][j],x[j],p),p);}x[c]=mul(rhs,inv(a[row][c],p),p);}x}

fn main(){
    let source:Value=serde_json::from_str(&fs::read_to_string("../results/five-cycle-ofpt-packet.json").unwrap()).unwrap();let cycle=&source["five_cycle"];
    let common=cycle["common_prefactor"].as_array().unwrap().iter().map(|x|x.as_str().unwrap().to_owned()).collect::<Vec<_>>();
    let terms=cycle["terms"].as_array().unwrap().iter().map(|t|t.as_array().unwrap().iter().map(|x|x.as_str().unwrap().to_owned()).collect()).collect::<Vec<Vec<String>>>();
    let p=std::env::var("MARICI_PRIME").ok().and_then(|x|x.parse::<i64>().ok()).unwrap_or(1019_i64);
    let z=std::env::var("MARICI_Z").ok().and_then(|x|x.parse::<i64>().ok()).unwrap_or(7_i64);
    let degree=std::env::var("MARICI_DEGREE").ok().and_then(|x|x.parse::<usize>().ok()).unwrap_or(1);
    let augmentation=std::env::var("MARICI_AUGMENTATION").ok().as_deref()==Some("1");
    let mons=monomials(degree).into_iter().filter(|e|!augmentation||e[4]==0).collect::<Vec<_>>();
    let nvars=if augmentation{4}else{5};
    let mut square_root=vec![None;p as usize];for y in 1..p{square_root[mul(y,y,p)as usize]=Some(y);}
    let mut fields=Vec::new();for i in 0..nvars{for mask in 0_usize..32{for e in &mons{fields.push((i,mask,*e));}}}
    let cols=1+fields.len();let mut rows=Vec::new();let mut labels=Vec::<[i32;4]>::new();let mut state=[11_i64,23,37,41,53];let mut accepted=0_i32;let mut attempts=0;
    let target_points=(nvars*mons.len()+24)as i32;
    while accepted<target_points{attempts+=1;assert!(attempts<100_000);for i in 0..nvars{state[i]=(state[i]*(37+2*i as i64)+11+3*i as i64).rem_euclid(p);if state[i]==0{state[i]=1;}}
        if augmentation{let s5=-(0..4).map(|i|mul(state[i],state[i],p)).sum::<i64>();let Some(y5)=square_root[s5.rem_euclid(p)as usize]else{continue;};state[4]=y5;}
        let roots=state;let s=roots.map(|x|mul(x,x,p));let mut orbit=Vec::new();
        for sheet in 0_usize..32{let y=std::array::from_fn(|i|if sheet&(1<<i)==0{roots[i]}else{-roots[i]});let Some((omega,dz,ds))=omega_jet(z,y,&common,&terms,p)else{continue;};
            let mut row=vec![0_i64;cols+1];row[0]=omega;
            for(m,(i,mask,e))in fields.iter().enumerate(){let v=monomial(&s,e,p);let derivative=if e[*i]==0{0}else{let mut low=*e;low[*i]-=1;mul(e[*i]as i64,monomial(&s,&low,p),p)};
                let sign=if(sheet&mask).count_ones()%2==0{1}else{-1};let character=(0..5).filter(|j|mask&(1<<j)!=0).fold(sign,|r,j|mul(r,roots[j],p));
                let mut log=if mask&(1<<i)!=0{inv(2*s[*i],p)}else{0};if augmentation&&mask&(1<<4)!=0{log=add(log,-inv(2*s[4],p),p);}
                let differentiated=add(derivative,mul(v,log,p),p);let source_derivative=if augmentation{add(ds[*i],-ds[4],p)}else{ds[*i]};
                row[1+m]=mul(character,add(mul(differentiated,omega,p),mul(v,source_derivative,p),p),p);
            }row[cols]=(-dz).rem_euclid(p);orbit.push(row);
        }if orbit.len()!=32{continue;}for sheet in 0..32{labels.push([0,accepted,sheet,0]);}rows.extend(orbit);accepted+=1;
    }
    let affine_count=rows.len();let(arank,aok)=rank(rows[..affine_count].to_vec(),p,cols);
    if std::env::var("MARICI_AFFINE_ONLY").ok().as_deref()==Some("1"){
        let packet=json!({"schema":"marici.benincasa.five_site.cyclic_kummer_ibp_pilot.v1","base":"five independent labelled radicands y_i^2=s_i","prime":p,"z":z,"degree":degree,
            "augmentation_quotient":augmentation,"unknowns":cols,"base_points":target_points,"affine_rank":arank,"affine_kernel_dimension":cols-arank,"affine_consistent":aok,"scope":"affine-only bounded modular gate"});
        fs::write("../results/five-site-cyclic-kummer-ibp-pilot.json",serde_json::to_string_pretty(&packet).unwrap()+"\n").unwrap();println!("{}",serde_json::to_string(&packet).unwrap());return;
    }
    let direction_count=std::env::var("MARICI_DIRECTIONS").ok().and_then(|x|x.parse::<usize>().ok()).unwrap_or(12);
    let cyclic_directions=std::env::var("MARICI_CYCLIC_DIRECTIONS").ok().as_deref()==Some("1");
    let mut dir=[71_i64,83,97,101,107];let mut boundary_roots=Vec::<[i64;5]>::new();
    for _ in 0..direction_count{loop{for i in 0..nvars{dir[i]=(dir[i]*(43+2*i as i64)+17).rem_euclid(p);if dir[i]==0{dir[i]=1;}}if !augmentation{break;}let s5=-(0..4).map(|i|mul(dir[i],dir[i],p)).sum::<i64>();if let Some(y5)=square_root[s5.rem_euclid(p)as usize]{dir[4]=y5;break;}}boundary_roots.push(dir);if cyclic_directions{let mut rotated=dir;for _ in 1..5{rotated=[rotated[4],rotated[0],rotated[1],rotated[2],rotated[3]];boundary_roots.push(rotated);}}}
    let mut direction_points=Vec::<[i64;5]>::new();let mut direction_roots=Vec::<[i64;5]>::new();
    for(direction,roots)in boundary_roots.into_iter().enumerate(){let s=roots.map(|x|mul(x,x,p));direction_points.push(s);direction_roots.push(roots);
        for sheet in 0_usize..32{let growth=terms.iter().map(|t|common.iter().chain(t).map(|q|grows(q,sheet)).sum::<usize>()).min().unwrap();if growth!=4{continue;}
            for level in 0_i32..=10{let mut row=vec![0_i64;cols+1];let mut active=false;
                for(m,(i,mask,e))in fields.iter().enumerate(){let weight=mask.count_ones()as i32;let d=e.iter().sum::<usize>()as i32;if 2*d+weight+2-growth as i32!=level{continue;}
                    let sign=if(sheet&mask).count_ones()%2==0{1}else{-1};let ch=(0..5).filter(|j|mask&(1<<j)!=0).fold(sign,|r,j|mul(r,roots[j],p));
                    row[1+m]=mul(ch,mul(s[*i],monomial(&s,e,p),p),p);active=true;}
                if active{rows.push(row);labels.push([1,direction as i32,sheet as i32,level]);}
            }
        }
    }
    let orbit_reps=(1_usize..31).map(orbit_rep).collect::<BTreeSet<_>>().into_iter().collect::<Vec<_>>();
    let mut census=Vec::new();let mut obstruction_residuals=None::<BTreeMap<i32,i64>>;
    if arank==cols{let solution=solve_unique(rows[..affine_count].to_vec(),p,cols);
        for rep in &orbit_reps{let mut boundary_rows=0_usize;let mut nonzero=0_usize;let mut first=None;let mut levels=BTreeMap::<i32,usize>::new();let mut directions=BTreeMap::<i32,i64>::new();
            for(row,label)in rows[affine_count..].iter().zip(labels[affine_count..].iter()).filter(|(_,l)|orbit_rep(l[2]as usize)==*rep){
                boundary_rows+=1;
                let residual=add(row[..cols].iter().zip(solution.iter()).fold(0_i64,|s,(a,x)|add(s,mul(*a,*x,p),p)),-row[cols],p);
                if residual!=0{nonzero+=1;*levels.entry(label[3]).or_default()+=1;directions.entry(label[1]).or_insert(residual);if first.is_none(){first=Some(json!({"direction":label[1],"sheet":label[2],"level":label[3],"residual":residual}));}}
            }
            if *rep==1{obstruction_residuals=Some(directions.clone());}
            census.push(json!({"cyclic_orbit_rep":rep,"hamming_weight":rep.count_ones(),"cycle_cut_size":cycle_cut_size(*rep),"cut_defect_indicator":(4-cycle_cut_size(*rep))/2,"orbit_size":5,"rank":arank,"boundary_rank_on_affine_kernel":0,
                "boundary_row_count":boundary_rows,"status":if boundary_rows==0{"absent_from_growth_four_grade"}else if nonzero==0{"satisfied"}else{"obstructed"},
                "consistent":boundary_rows>0&&nonzero==0,"nonzero_boundary_rows":nonzero,"nonzero_level_histogram":levels,"direction_residuals":directions,"first_nonzero":first}));}
    }else{for rep in &orbit_reps{let selected=rows.iter().zip(labels.iter()).filter(|(_,l)|l[0]==0||orbit_rep(l[2]as usize)==*rep).map(|(r,_)|r.clone()).collect::<Vec<_>>();
        let(r,ok)=rank(selected,p,cols);census.push(json!({"cyclic_orbit_rep":rep,"hamming_weight":rep.count_ones(),"cycle_cut_size":cycle_cut_size(*rep),"cut_defect_indicator":(4-cycle_cut_size(*rep))/2,"orbit_size":5,"rank":r,"boundary_rank_on_affine_kernel":r-arank,"consistent":ok}));}}
    let scalar_fit=obstruction_residuals.as_ref().and_then(|rho|{if direction_points.len()<2{return None;}let invs=direction_points.iter().map(|s|{
        let q0=(0..5).fold(0_i64,|r,i|add(r,mul(s[i],s[i],p),p));let q1=(0..5).fold(0_i64,|r,i|add(r,mul(s[i],s[(i+1)%5],p),p));[q0,q1]}).collect::<Vec<_>>();
        let det=add(mul(invs[0][0],invs[1][1],p),-mul(invs[0][1],invs[1][0],p),p);if det==0{return None;}let r0=*rho.get(&0)?;let r1=*rho.get(&1)?;
        let a=mul(add(mul(r0,invs[1][1],p),-mul(invs[0][1],r1,p),p),inv(det,p),p);let b=mul(add(mul(invs[0][0],r1,p),-mul(r0,invs[1][0],p),p),inv(det,p),p);
        let verified=invs.iter().enumerate().all(|(d,q)|add(mul(a,q[0],p),mul(b,q[1],p),p)==*rho.get(&(d as i32)).unwrap());Some(json!({"basis":["sum_i s_i^2","sum_i s_i s_(i+1)"],"coefficients":[a,b],"verified_all_directions":verified}))});
    let kummer_quartic_fit=obstruction_residuals.as_ref().map(|rho|{let basis=monomials(4).into_iter().filter(|e|e.iter().sum::<usize>()==4).map(exp_orbit_rep).collect::<BTreeSet<_>>().into_iter().collect::<Vec<_>>();
        let matrix=direction_roots.iter().enumerate().map(|(d,y)|{let mut row=basis.iter().map(|e|orbit_monomial(y,*e,p)).collect::<Vec<_>>();row.push(*rho.get(&(d as i32)).unwrap());row}).collect::<Vec<_>>();
        let(r,ok)=rank(matrix,p,basis.len());json!({"cyclic_orbit_basis_size":basis.len(),"evaluation_rank":r,"consistent":ok,"kernel_dimension":basis.len()-r,"directions":direction_roots.len()})});
    let packet=json!({"schema":"marici.benincasa.five_site.cyclic_kummer_ibp_pilot.v1","base":"five independent labelled radicands y_i^2=s_i","augmentation_quotient":augmentation,"prime":p,"z":z,"degree":degree,
        "unknowns":cols,"affine_rank":arank,"affine_kernel_dimension":cols-arank,"affine_consistent":aok,"census":census,
        "cyclic_quadratic_scalar_fit":scalar_fit,
        "cyclic_kummer_quartic_fit":kummer_quartic_fit,
        "scope":"bounded fixed-degree modular falsifier; radial grading uses wt(s)=2, wt(y)=1"});
    fs::write("../results/five-site-cyclic-kummer-ibp-pilot.json",serde_json::to_string_pretty(&packet).unwrap()+"\n").unwrap();println!("{}",serde_json::to_string(&packet).unwrap());
}
