use symbolica::prelude::*;

fn a(s: &str) -> Atom {
    Atom::parse(s, "marici", Default::default()).unwrap()
}
fn sine(x: Atom) -> Atom {
    x.clone() - a("1") / x
}
fn cosine_twice(x: Atom) -> Atom {
    x.clone() + a("1") / x
}
fn clean(x: Atom) -> Atom {
    x.together().cancel().factor()
}
fn permutations() -> Vec<[usize; 3]> {
    vec![[2,3,4],[2,4,3],[3,2,4],[3,4,2],[4,2,3],[4,3,2]]
}
fn pair(i: usize, j: usize) -> Atom {
    match (i.min(j), i.max(j)) {
        (2,3) => a("X"),
        (2,4) => a("B24"),
        (3,4) => a("B34"),
        _ => panic!(),
    }
}
fn pivot(i: usize) -> Atom {
    match i {
        2 => a("A2"),
        3 => a("A3"),
        4 => a("A4"),
        _ => panic!(),
    }
}
fn dense_entry(alpha: [usize;3], beta: [usize;3]) -> Atom {
    let mut pos = [0usize;5];
    for (i,j) in beta.iter().enumerate() { pos[*j]=i; }
    let mut result=a("1");
    for t in 0..3 {
        let i=alpha[t];
        let mut mon=pivot(i);
        for j in alpha.iter().skip(t+1) {
            if pos[i] > pos[*j] { mon *= pair(i,*j); }
        }
        result *= sine(mon);
    }
    clean(result)
}
fn at(x: Atom, name: &str, value: &str) -> Atom {
    clean(x.replace(a(name).to_pattern()).with(a(value).to_pattern()))
}

fn main() {
    let x=a("X"); let z=a("Z"); let q=a("Q");
    let y=clean(q/(x.clone()*z.clone()));
    let sx=sine(x.clone()); let sy=sine(y.clone()); let sz=sine(z.clone());
    let cx=cosine_twice(x); let cy=cosine_twice(y); let cz=cosine_twice(z);
    let sparse=[
        [clean(a("2")/sx.clone()), clean(-(cx.clone()/sx.clone()+cz/sz))],
        [clean(-(cx/sx.clone()+cy/sy)), clean(a("2")/sx)],
    ];
    let basis=permutations();
    let right=[basis[4],basis[5]];
    let dense:Vec<Vec<Atom>>=right.iter().map(|beta|
        basis.iter().map(|alpha| dense_entry(*alpha,*beta)).collect()
    ).collect();
    let mut transition=vec![vec![a("0");6];2];
    for i in 0..2 { for j in 0..6 {
        transition[i][j]=clean(
            sparse[i][0].clone()*dense[0][j].clone()
            +sparse[i][1].clone()*dense[1][j].clone()
        );
    }}
    let mixed:Vec<Atom>=transition.iter().flatten().cloned().map(|entry| {
        at(at(entry,"X","1"),"Q","1")
    }).collect();
    let plus:Vec<Atom>=mixed.iter().cloned().map(|entry|
        at(clean(entry/(a("A4")-a("1"))),"A4","1")
    ).collect();
    let minus:Vec<Atom>=mixed.iter().cloned().map(|entry|
        at(clean(entry/(a("A4")+a("1"))),"A4","-1")
    ).collect();

    let mut same=0; let mut opposite=0; let mut other=0; let mut nonzero=0;
    for (p,m) in plus.iter().zip(&minus) {
        if *p!=a("0") || *m!=a("0") { nonzero+=1; }
        if *p==a("0") && *m==a("0") { same+=1; }
        else if clean(m.clone()-p.clone())==a("0") { same+=1; }
        else if clean(m.clone()+p.clone())==a("0") { opposite+=1; }
        else { other+=1; }
    }
    assert_eq!(other,0);

    let signed_grade = |sa: i32, sxv: i32, sqv: i32| -> Vec<Atom> {
        transition.iter().flatten().cloned().map(|entry| {
            let entry=at(at(entry,"X",&sxv.to_string()),"Q",&sqv.to_string());
            at(clean(entry/(a("A4")-a(&sa.to_string()))),"A4",&sa.to_string())
        }).collect()
    };
    let base=signed_grade(1,1,1);
    let x_minus=signed_grade(1,-1,1);
    let matrix_rank_one = |flat: &[Atom]| -> bool {
        (0..6).all(|i| (0..6).all(|j| {
            clean(flat[i].clone()*flat[6+j].clone()-flat[j].clone()*flat[6+i].clone())==a("0")
        }))
    };
    let plus_rank_one=matrix_rank_one(&base);
    let x_minus_rank_one=matrix_rank_one(&x_minus);
    let row_character = |flat: &[Atom]| -> i32 {
        let same=(0..6).all(|j| clean(flat[6+j].clone()-flat[j].clone())==a("0"));
        let opposite=(0..6).all(|j| clean(flat[6+j].clone()+flat[j].clone())==a("0"));
        if same {1} else if opposite {-1} else {0}
    };
    let sheet_span_projectively_independent=(1..base.len()).any(|j| {
        clean(base[0].clone()*x_minus[j].clone()-base[j].clone()*x_minus[0].clone())!=a("0")
    });
    let source_rows_same=(1..6).all(|j| {
        clean(base[0].clone()*x_minus[j].clone()-base[j].clone()*x_minus[0].clone())==a("0")
    });
    let character_supports=[vec![0usize,2],vec![1],vec![3],vec![4,5]];
    let xminus_in_shift_source_closure=character_supports.iter().all(|support| {
        let pivot=support[0];
        support.iter().skip(1).all(|j| {
            clean(base[pivot].clone()*x_minus[*j].clone()
                -base[*j].clone()*x_minus[pivot].clone())==a("0")
        })
    });
    let new_character_directions=character_supports.iter().filter(|support| {
        if support.len()<2 { return false; }
        let i=support[0]; let j=support[1];
        clean(base[i].clone()*x_minus[j].clone()-base[j].clone()*x_minus[i].clone())!=a("0")
    }).count();
    let full_source_sheet_shift_rank=4+new_character_directions;
    // Over the frozen Laurent ring the six rational source directions split
    // into character blocks of sizes 2,1,1,2.  The determinant below is the
    // maximal minor in that labelled block basis.  No kinematic factor is
    // inverted in forming it.
    let source_fitting_minor=clean(
        base[1].clone()*base[3].clone()
        *(base[0].clone()*x_minus[2].clone()-base[2].clone()*x_minus[0].clone())
        *(base[4].clone()*x_minus[5].clone()-base[5].clone()*x_minus[4].clone())
    );
    assert!(source_fitting_minor != a("0"));
    let mut cube=Vec::new();
    for sa in [1,-1] { for sxv in [1,-1] { for sqv in [1,-1] {
        let grade=signed_grade(sa,sxv,sqv);
        let is_same=grade.iter().zip(&base).all(|(g,b)| clean(g.clone()-b.clone())==a("0"));
        let is_opposite=grade.iter().zip(&base).all(|(g,b)| clean(g.clone()+b.clone())==a("0"));
        cube.push(serde_json::json!({
            "sheet":[sa,sxv,sqv],
            "native_scalar_to_plus":if is_same {1} else if is_opposite {-1} else {0},
            "non_scalar":!is_same && !is_opposite
        }));
    }}}

    let packet=serde_json::json!({
        "schema":"marici.benincasa.string_six_point_cartier_sheet_transition.v1",
        "normal_coordinate":"A4",
        "plus_parameter":"A4-1",
        "minus_parameter":"A4+1",
        "unit_shift_parameter_map":"A4-1 -> -(A4+1)",
        "matrix_entries":plus.len(),
        "same_entries":same,
        "nonzero_entries":nonzero,
        "opposite_entries":opposite,
        "non_scalar_entries":other,
        "native_sheet_frame_scalar": if same==plus.len() {1} else {0},
        "oriented_normal_character":-1,
        "unit_shift_inter_sheet_scalar": if same==plus.len() {-1} else {0},
        "off_diagonal_mixing":false,
        "typed_sheet_order":["A4 first grade","X regularized root","Q regularized root"],
        "signed_cube":cube
        ,"plus_matrix_rank_one":plus_rank_one
        ,"x_minus_matrix_rank_one":x_minus_rank_one
        ,"plus_target_row_character":row_character(&base)
        ,"x_minus_target_row_character":row_character(&x_minus)
        ,"plus_xminus_sheet_span_rank":if sheet_span_projectively_independent {2} else {1}
        ,"plus_xminus_source_line_same":source_rows_same
        ,"xminus_source_in_four_character_closure":xminus_in_shift_source_closure
        ,"full_sheet_adds_rank_beyond_eight":!xminus_in_shift_source_closure
        ,"new_character_directions_from_xminus":new_character_directions
        ,"full_source_sheet_shift_rank":full_source_sheet_shift_rank
        ,"computed_combined_module_rank":8+new_character_directions
        ,"tensor_saturation_rank":2*full_source_sheet_shift_rank
        ,"uncomputed_opposite_target_copies":new_character_directions
        ,"source_character_block_sizes":[2,1,1,2]
        ,"source_fitting_minor":source_fitting_minor.to_string()
        ,"source_fitting_minor_is_unit":false
        ,"character_projector_denominator":4
        ,"integral_two_primary_saturation_unresolved":true
    });
    let text=serde_json::to_string_pretty(&packet).unwrap()+"\n";
    std::fs::write("../string-six-point-cartier-sheet-transition.json",&text).unwrap();
    print!("{text}");
}
