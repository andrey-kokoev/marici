use serde_json::json;
type V=[i32;9];
fn add(a:V,b:V)->V{let mut r=[0;9];for i in 0..9{r[i]=a[i]+b[i];}r}
fn neg(a:V)->V{let mut r=[0;9];for i in 0..9{r[i]=-a[i];}r}
fn sub(a:V,b:V)->V{add(a,neg(b))}
fn in_normal_span(v:V)->bool{
    // normals: s14=e2, s23=e3, s235=e3+e6+e7
    // therefore all coordinates except 2,3,6,7 vanish and v6=v7.
    (0..9).all(|i|matches!(i,2|3|6|7)||v[i]==0) && v[6]==v[7]
}
fn main(){
    // coordinates: 12,13,14,23,24,34,25,35,45
    let e=|i:usize|{let mut v=[0;9];v[i]=1;v};
    let branch=[
      ("A2",e(0)),("A3",e(1)),("A2*B24",add(e(0),e(4))),
      ("A3*B34",add(e(1),e(5))),("Z*A2",add(e(7),e(0))),
      ("Z*A2*B24",add(add(e(7),e(0)),e(4))),("A3/Z",sub(e(1),e(7))),
      ("A3*B34/Z",sub(add(e(1),e(5)),e(7)))
    ];
    let channels=[
      ("s23",e(3)),("s24",e(4)),("s34",e(5)),
      ("s123",add(add(e(0),e(1)),e(3))),
      ("s124",add(add(e(0),e(2)),e(4))),
      ("s134",add(add(e(1),e(2)),e(5))),
      ("s234",add(add(e(3),e(4)),e(5))),
      ("s1234",add(add(add(add(add(e(0),e(1)),e(2)),e(3)),e(4)),e(5))),
      ("s25",e(6)),("s35",e(7)),("s45",e(8)),
      ("s235",add(add(e(3),e(6)),e(7))),
      ("s245",add(add(e(4),e(6)),e(8))),
      ("s345",add(add(e(5),e(7)),e(8)))
    ];
    let matches:Vec<_>=branch.iter().map(|(name,v)|{
      let hit=channels.iter().find_map(|(c,w)|if in_normal_span(sub(*v,*w))||in_normal_span(add(*v,*w)){Some(*c)}else{None});
      json!({"branch_factor":name,"matched_transition_channel":hit})
    }).collect();
    let matched=matches.iter().filter(|x|!x["matched_transition_channel"].is_null()).count();
    assert_eq!(matched,2);
    let packet=json!({
      "schema":"marici.benincasa.string_six_point_branch_dense_channel_match.v1",
      "additive_coordinates":["s12","s13","s14","s23","s24","s34","s25","s35","s45"],
      "frozen_normal_relations":["s14=0","s23=0","s235=s23+s25+s35=0"],
      "matches":matches,
      "matched_count":matched,
      "unmatched_count":branch.len()-matched,
      "determinant_divisor_pullback_closes_branch_support":matched==branch.len(),
      "matrix_level_residue_data_required":true
    });
    let text=serde_json::to_string_pretty(&packet).unwrap()+"\n";
    std::fs::write("../string-six-point-branch-dense-channel-match.json",&text).unwrap();print!("{text}");
}
