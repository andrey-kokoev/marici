use serde_json::json;
use std::fs;
use symbolica::prelude::*;

fn atom(text:&str)->Atom{Atom::parse(text,"marici",Default::default()).unwrap().expand()}

fn scalar_sign(expression:&Atom,z:&str,s:&str)->i8{
    let value=expression.clone()
        .replace(atom("5^(1/2)").to_pattern()).with(atom(s).to_pattern())
        .replace(atom("z").to_pattern()).with(atom(z).to_pattern())
        .together().cancel().expand().to_string();
    if value=="0"{0}else if value.starts_with('-'){-1}else{1}
}

fn corner_signs(expression:&Atom,left:&str,right:&str,negative_sqrt:bool)->Vec<i8>{
    let sqrt_bounds=if negative_sqrt {
        ["-2236067978/1000000000","-2236067977/1000000000"]
    } else {
        ["2236067977/1000000000","2236067978/1000000000"]
    };
    [left,right].iter().flat_map(|z|sqrt_bounds.iter().map(move|s|scalar_sign(expression,z,s))).collect()
}

fn run() {
    let source:serde_json::Value=serde_json::from_str(
        &fs::read_to_string("../results/five-site-cyclic-triple-region-census.json").unwrap()).unwrap();
    let mut records=Vec::new();
    for record in source["records"].as_array().unwrap() {
        let text=record["rational_field_norm_raw"].as_str().unwrap();
        let polynomial=Atom::parse(text,"marici",Default::default()).unwrap()
            .to_polynomial::<_,u8>(&Q,None).to_univariate_from_univariate(0);
        let roots=polynomial.isolate_roots(None).into_iter().map(|(left,right,multiplicity)|{
            let (left,right)=polynomial.refine_root_interval((left,right),&(1,1_000_000_000).into());
            (left,right,multiplicity)
        }).collect::<Vec<_>>();
        let positive=roots.iter().filter(|(left,right,_)|*left>=(0,1)&&*right>(0,1)).count();
        let negative=roots.iter().filter(|(left,right,_)|*left<(0,1)&&*right<=(0,1)).count();
        let discriminant=atom(record["critical_discriminant_over_Qsqrt5"].as_str().unwrap());
        let x=atom(record["repeated_critical_squares"]["first_free_y_squared"].as_str().unwrap());
        let v=atom(record["repeated_critical_squares"]["second_free_y_squared"].as_str().unwrap());
        let wall_multipliers=record["multiplier_saturation"]["wall_multiplier_zero_numerators_over_Qsqrt5"]
            .as_array().unwrap().iter().map(|value|atom(value.as_str().unwrap())).collect::<Vec<_>>();
        let fixed_coefficients=record["fixed_linear_y_over_t"].as_array().unwrap();
        let fixed_signs=fixed_coefficients.iter().filter_map(|value|value.as_str()).map(|value|{
            if value.starts_with('-'){-1}else{1}
        }).collect::<Vec<_>>();
        let positive_linear_sheet_exists=!fixed_signs.is_empty()&&fixed_signs.iter().all(|sign|*sign==fixed_signs[0]);
        let required_t_sign_for_positive_fixed_y=if positive_linear_sheet_exists{fixed_signs[0]}else{0};
        let branch_records=roots.iter().map(|(left,right,_)|{
            let left=left.to_string();let right=right.to_string();
            let plus_disc=corner_signs(&discriminant,&left,&right,false);
            let minus_disc=corner_signs(&discriminant,&left,&right,true);
            let plus_branch=plus_disc.contains(&-1)&&plus_disc.contains(&1);
            let minus_branch=minus_disc.contains(&-1)&&minus_disc.contains(&1);
            let x_signs=if plus_branch{corner_signs(&x,&left,&right,false)}else{Vec::new()};
            let v_signs=if plus_branch{corner_signs(&v,&left,&right,false)}else{Vec::new()};
            let wall_signs=if plus_branch{wall_multipliers.iter().map(|value|{
                let signs=corner_signs(value,&left,&right,false);
                if signs.iter().all(|sign|*sign>0){1}else if signs.iter().all(|sign|*sign<0){-1}else{0}
            }).collect::<Vec<_>>()}else{Vec::new()};
            let common_nonzero_wall_sign=plus_branch&&!wall_signs.is_empty()&&wall_signs.iter().all(|sign|*sign==wall_signs[0]&&*sign!=0);
            json!({
                "left":left,"right":right,
                "belongs_to_plus_sqrt5_branch":plus_branch,
                "belongs_to_minus_sqrt5_branch":minus_branch,
                "plus_branch_first_free_square_positive":plus_branch&&x_signs.iter().all(|sign|*sign>0),
                "plus_branch_second_free_square_positive":plus_branch&&v_signs.iter().all(|sign|*sign>0),
                "positive_linear_loop_sheet_exists":plus_branch&&positive_linear_sheet_exists,
                "required_t_sign_for_positive_fixed_y":if plus_branch{required_t_sign_for_positive_fixed_y}else{0},
                "projective_wall_multiplier_signs":wall_signs,
                "common_nonzero_wall_multiplier_sign":common_nonzero_wall_sign
            })
        }).collect::<Vec<_>>();
        records.push(json!({
            "representative":record["representative"],
            "real_root_intervals":roots.iter().map(|(left,right,multiplicity)|json!({
                "left":left.to_string(),"right":right.to_string(),"multiplicity":multiplicity
            })).collect::<Vec<_>>(),
            "positive_real_roots":positive,
            "negative_real_roots":negative,
            "nonreal_roots":4-positive-negative
            ,"refined_branch_and_square_signs":branch_records
        }));
    }
    let packet=json!({
        "schema":"marici.five_site_cyclic_triple_region_real_roots.v1",
        "method":"Symbolica exact rational root isolation",
        "records":records,
        "scope":"real-sheet accessibility only; no Betti pairing or monodromy conclusion"
    });
    fs::write("../results/five-site-cyclic-triple-region-real-roots.json",
        serde_json::to_string_pretty(&packet).unwrap()+"\n").unwrap();
    println!("{}",json!({"records":records}));
}

fn main(){
    std::thread::Builder::new().name("exact-root-isolation".into()).stack_size(32*1024*1024)
        .spawn(run).unwrap().join().unwrap();
}
