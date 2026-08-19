use serde_json::json;
use symbolica::prelude::*;

fn a(s:&str)->Atom { Atom::parse(s,"marici",Default::default()).unwrap() }
fn clean(x:Atom)->Atom { x.together().cancel().factor() }
fn euler(x:&Atom)->Atom { clean(a("B34")*x.derivative(symbol!("marici::B34"))) }
fn row_times_matrix(row:&[Atom],m:&[Vec<Atom>])->Vec<Atom>{
    (0..m[0].len()).map(|j|clean((0..row.len()).map(|i|row[i].clone()*m[i][j].clone()).fold(a("0"),|p,x|p+x))).collect()
}

fn main(){
    let u=vec![a("B34"),a("B24"),a("X"),a("1/B34"),a("1/B24"),a("1/X")];
    let mut d0=vec![vec![a("0");6];6];
    for k in 0..6 { d0[k][k]=clean(-u[k].clone()); d0[k][(k+1)%6]=a("1"); }
    let d1:Vec<Atom>=(0..6).map(|j|((j+1)..6).map(|k|u[k].clone()).fold(a("1"),|p,x|clean(p*x))).collect();
    assert!(row_times_matrix(&d1,&d0).iter().all(|x|*x==a("0")));
    let kd0:Vec<Vec<Atom>>=d0.iter().map(|r|r.iter().map(euler).collect()).collect();
    let kd1:Vec<Atom>=d1.iter().map(euler).collect();
    let lhs1=row_times_matrix(&kd1,&d0);
    let lhs2=row_times_matrix(&d1,&kd0);
    let coherence:Vec<Atom>=(0..6).map(|j|clean(lhs1[j].clone()+lhs2[j].clone())).collect();
    assert!(coherence.iter().all(|x|*x==a("0")));
    let mut d0_support=Vec::new();
    for i in 0..6 { for j in 0..6 { if kd0[i][j]!=a("0") { d0_support.push((i,j)); } } }
    let d1_support:Vec<usize>=(0..6).filter(|&j|kd1[j]!=a("0")).collect();
    assert_eq!(d0_support,vec![(0,0),(3,3)]);
    assert_eq!(d1_support,vec![0,1,2]);
    let packet=json!({
      "schema":"marici.benincasa.string_six_point_b34_cellular_deformation.v1",
      "operator":"K_34=B34*d/dB34",
      "degree_zero_one_support":d0_support,
      "degree_one_two_support":d1_support,
      "labelled_b34_edges":[0,3],
      "rank_degree_zero_one_symbol":2,
      "coherence_identity":"(K_34 delta1) delta0 + delta1 (K_34 delta0)=0",
      "coherence_verified":true,
      "new_cells":false,
      "loaded_single_circuit_sufficient":false,
      "physical_de_rham_comparison_constructed":false,
      "conclusion":"The B34 first coefficient deformation is a canonical endomorphism cocycle of the full hexagon complex supported on both labelled 34-occurrences. One loaded circuit column alone cannot represent it."
    });
    let text=serde_json::to_string_pretty(&packet).unwrap()+"\n";
    std::fs::write("../string-six-point-b34-cellular-deformation.json",&text).unwrap();
    print!("{text}");
}
