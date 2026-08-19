use serde_json::json;

type M = Vec<Vec<i64>>;
fn eye(n:usize)->M { (0..n).map(|i|(0..n).map(|j|if i==j {1}else{0}).collect()).collect() }
fn mul(a:&M,b:&M)->M { let n=a.len(); (0..n).map(|i|(0..n).map(|j|(0..n).map(|k|a[i][k]*b[k][j]).sum()).collect()).collect() }
fn perm_matrix(p:&[usize])->M { let n=p.len(); let mut m=vec![vec![0;n];n]; for i in 0..n {m[p[i]][i]=1;} m }
fn diag(v:&[i64])->M { let mut m=vec![vec![0;v.len()];v.len()]; for i in 0..v.len(){m[i][i]=v[i];} m }
fn transpose(a:&M)->M {(0..a.len()).map(|i|(0..a.len()).map(|j|a[j][i]).collect()).collect()}
fn det_signed_permutation(a:&M)->i64 {
    let mut p=Vec::new(); let mut sign=1;
    for j in 0..a.len(){let i=(0..a.len()).find(|&i|a[i][j]!=0).unwrap();p.push(i);sign*=a[i][j];}
    let inversions=(0..p.len()).map(|i|(i+1..p.len()).filter(|&j|p[i]>p[j]).count()).sum::<usize>();
    if inversions%2==0 {sign}else{-sign}
}

fn main(){
    // Frozen word order: 234,243,324,342,423,432.
    let cyclic=perm_matrix(&[3,2,5,4,0,1]);
    let reflection=perm_matrix(&[2,3,0,1,5,4]);
    let b24=diag(&[-1,-1,-1,1,1,1]);
    let b34=diag(&[-1,1,-1,-1,1,1]);
    let pivot=diag(&[-1,-1,-1,-1,-1,-1]);
    let i=eye(6);
    assert_eq!(mul(&mul(&cyclic,&cyclic),&cyclic),i);
    assert_eq!(mul(&reflection,&reflection),i);
    assert_eq!(mul(&mul(&reflection,&cyclic),&reflection),transpose(&cyclic));
    assert_eq!(mul(&b24,&b34),mul(&b34,&b24));
    for g in [&cyclic,&reflection,&b24,&b34,&pivot] { assert_eq!(det_signed_permutation(g).abs(),1); }

    let packet=json!({
      "schema":"marici.benincasa.string_six_point_integral_discrete_atlas.v1",
      "word_order":["234","243","324","342","423","432"],
      "cyclic_permutation":[3,2,5,4,0,1],
      "reflection_permutation":[2,3,0,1,5,4],
      "pair_shift_B24_diagonal":[-1,-1,-1,1,1,1],
      "pair_shift_B34_diagonal":[-1,1,-1,-1,1,1],
      "pivot_shift_diagonal":[-1,-1,-1,-1,-1,-1],
      "relations":{"cyclic_order":3,"reflection_order":2,"dihedral_conjugation":true,"pair_shifts_commute":true},
      "all_source_generators_unimodular":true,
      "target_sheet_shear":[[1,0],[2,1]],
      "target_sheet_shear_determinant":1,
      "rank_twelve_integral_discrete_atlas":true,
      "differential_parameter_connection":"not supplied and not inferred"
    });
    let text=serde_json::to_string_pretty(&packet).unwrap()+"\n";
    std::fs::write("../string-six-point-integral-discrete-atlas.json",&text).unwrap(); print!("{text}");
}
