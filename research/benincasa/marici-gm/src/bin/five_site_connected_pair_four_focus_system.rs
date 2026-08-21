use serde_json::{json, Value};
use std::fs;
use symbolica::prelude::*;

fn atom(text:&str)->Atom { Atom::parse(text,"marici",Default::default()).unwrap().expand() }
fn dist(i:usize,j:usize)->Atom {
    atom(match i.abs_diff(j) {1=>"2",2=>"(11+z)/2",3=>"(21+z)/2",4=>"17",_=>"0"})
}
fn det3(h:&[[Atom;3];3])->Atom {
    (&h[0][0]*(&h[1][1]*&h[2][2]-&h[1][2]*&h[2][1])
    -&h[0][1]*(&h[1][0]*&h[2][2]-&h[1][2]*&h[2][0])
    +&h[0][2]*(&h[1][0]*&h[2][1]-&h[1][1]*&h[2][0])).expand()
}
fn adj3(h:&[[Atom;3];3])->[[Atom;3];3] {
    [
        [(&h[1][1]*&h[2][2]-&h[1][2]*&h[2][1]).expand(),(&h[0][2]*&h[2][1]-&h[0][1]*&h[2][2]).expand(),(&h[0][1]*&h[1][2]-&h[0][2]*&h[1][1]).expand()],
        [(&h[1][2]*&h[2][0]-&h[1][0]*&h[2][2]).expand(),(&h[0][0]*&h[2][2]-&h[0][2]*&h[2][0]).expand(),(&h[0][2]*&h[1][0]-&h[0][0]*&h[1][2]).expand()],
        [(&h[1][0]*&h[2][1]-&h[1][1]*&h[2][0]).expand(),(&h[0][1]*&h[2][0]-&h[0][0]*&h[2][1]).expand(),(&h[0][0]*&h[1][1]-&h[0][1]*&h[1][0]).expand()]
    ]
}
fn arc_size(label:&str)->usize { label.strip_prefix("g_").unwrap().chars().count() }

fn main(){
    let source:Value=serde_json::from_str(&fs::read_to_string("../results/five-site-compatible-landau-subsets.json").unwrap()).unwrap();
    let pair=source["census"].as_array().unwrap().iter().find(|x|x["active_wall_count"]==2).unwrap();
    let selected=pair["representative_records"].as_array().unwrap().iter().filter(|record|{
        let profile=record["profile"].as_str().unwrap();
        !profile.contains("M1")&&!profile.contains("+T")&&profile.contains("cut_intersections=[0]")
    }).collect::<Vec<_>>();
    assert_eq!(selected.len(),7);
    let mut records=Vec::new();
    for record in selected {
        let labels=record["representative"].as_array().unwrap();
        let m=arc_size(labels[0].as_str().unwrap());
        let n=arc_size(labels[1].as_str().unwrap());
        let supports=record["cut_supports"].as_array().unwrap();
        let left=supports[0].as_array().unwrap().iter().map(|x|x.as_u64().unwrap() as usize).collect::<Vec<_>>();
        let right=supports[1].as_array().unwrap().iter().map(|x|x.as_u64().unwrap() as usize).collect::<Vec<_>>();
        let f=[left[0],left[1],right[0],right[1]];
        let y=[atom("b"),atom(&format!("-{m}*t-b")),atom("c"),atom(&format!("-{n}*t-c"))];
        let mut h:[[Atom;3];3]=std::array::from_fn(|_|std::array::from_fn(|_|Atom::new()));
        for i in 0..3 { for j in 0..3 {
            h[i][j]=((&dist(f[0],f[i+1])+&dist(f[0],f[j+1])-&dist(f[i+1],f[j+1]))/atom("2")).expand();
        }}
        let determinant=det3(&h);
        let adj=adj3(&h);
        let p:[Atom;3]=std::array::from_fn(|i| ((&y[0]*&y[0]+dist(f[0],f[i+1])-&y[i+1]*&y[i+1])/atom("2")).expand());
        let xnum:[Atom;3]=std::array::from_fn(|i|(0..3).fold(Atom::new(),|sum,j|sum+&adj[i][j]*&p[j]).expand());
        let existence=(&determinant*&y[0]*&y[0]-(0..3).fold(Atom::new(),|sum,i|sum+&p[i]*&xnum[i])).expand();
        let u:[Atom;3]=std::array::from_fn(|i|((&y[0]+&y[1])*&xnum[i]-if i==0{&determinant*&y[0]}else{Atom::new()}).expand());
        let v:[Atom;3]=std::array::from_fn(|i|((&y[2]+&y[3])*&xnum[i]-if i==1{&determinant*&y[3]}else if i==2{&determinant*&y[2]}else{Atom::new()}).expand());
        let minors=[(&u[0]*&v[1]-&u[1]*&v[0]).expand(),(&u[0]*&v[2]-&u[2]*&v[0]).expand(),(&u[1]*&v[2]-&u[2]*&v[1]).expand()];
        records.push(json!({
            "representative":record["representative"],"profile":record["profile"],"arc_sizes":[m,n],"ordered_foci":f,
            "routing_gram":h.iter().map(|row|row.iter().map(ToString::to_string).collect::<Vec<_>>()).collect::<Vec<_>>(),
            "routing_gram_determinant":determinant.to_string(),
            "root_assignment":y.iter().map(ToString::to_string).collect::<Vec<_>>(),
            "realization_equation":existence.to_string(),
            "gradient_vector_left":u.iter().map(ToString::to_string).collect::<Vec<_>>(),
            "gradient_vector_right":v.iter().map(ToString::to_string).collect::<Vec<_>>(),
            "collinearity_minors":minors.iter().map(ToString::to_string).collect::<Vec<_>>()
        }));
    }
    let packet=json!({
        "schema":"marici.benincasa.five_site.connected_pair_four_focus_system.v1",
        "quadratic_field_relation":"z^2=5","variables":["b","c","t"],"records":records,
        "acceptance":"Landau support is the elimination of b,c from the realization equation and all three labelled collinearity minors.",
        "no_solution_claim":true
    });
    fs::write("../results/five-site-connected-pair-four-focus-system.json",serde_json::to_string_pretty(&packet).unwrap()+"\n").unwrap();
    println!("wrote five-site-connected-pair-four-focus-system.json");
}
