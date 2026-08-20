use serde_json::json;
use std::fs;

fn det3(rows: [[i32;3];3]) -> i32 {
    rows[0][0]*(rows[1][1]*rows[2][2]-rows[1][2]*rows[2][1])
        -rows[0][1]*(rows[1][0]*rows[2][2]-rows[1][2]*rows[2][0])
        +rows[0][2]*(rows[1][0]*rows[2][1]-rows[1][1]*rows[2][0])
}

fn permutation_sign(values: &[usize]) -> i32 {
    let inversions=(0..values.len()).flat_map(|i|(i+1..values.len()).map(move|j|(i,j)))
        .filter(|(i,j)|values[*i]>values[*j]).count();
    if inversions%2==0 {1} else {-1}
}

fn exterior_trace(degree: usize, deck: usize) -> i32 {
    let mut trace=0;
    for subset in 0_usize..16 {
        if subset.count_ones() as usize != degree {continue;}
        let original=(0..4).filter(|i|subset&(1<<i)!=0).collect::<Vec<_>>();
        let transported=original.iter().map(|label|label^deck).collect::<Vec<_>>();
        let transported_set=transported.iter().fold(0_usize,|set,label|set|(1<<label));
        if transported_set==subset {trace+=permutation_sign(&transported);}
    }
    trace
}

fn main(){
    // Labels are the sign pairs (++),(+-),(-+),(--), with normal (1,sa,sb).
    let normals=[[1,1,1],[1,1,-1],[1,-1,1],[1,-1,-1]];
    let mut triple_determinants=Vec::new();
    for omitted in 0..4 {
        let rows=(0..4).filter(|i|*i!=omitted).map(|i|normals[i]).collect::<Vec<_>>();
        let determinant=det3([rows[0],rows[1],rows[2]]);
        assert_eq!(determinant.abs(),4);
        triple_determinants.push(determinant);
    }

    let mut characters=Vec::new();
    for deck in 0..4 {
        // Translation on four labels is even: identity or two transpositions.
        let degree0=exterior_trace(0,deck);
        let degree1=exterior_trace(1,deck);
        let degree2=exterior_trace(2,deck);
        let wedge3=exterior_trace(3,deck);
        let relation_character=1;
        let degree3=wedge3-relation_character;
        characters.push([degree0,degree1,degree2,degree3]);
    }
    assert_eq!(characters,vec![[1,4,6,3],[1,0,-2,-1],[1,0,-2,-1],[1,0,-2,-1]]);

    let packet=json!({
        "schema":"marici.benincasa.five_site.double_soft_wall_arrangement.v1",
        "corner":"F_i=F_j=0 away from det(H)=0 and all other F_k",
        "cover_coordinates":"R_i=y_i^2, R_j=y_j^2",
        "four_labelled_walls":["X+y_i+y_j","X+y_i-y_j","X-y_i+y_j","X-y_i-y_j"],
        "normal_vectors":normals,
        "triple_determinants":triple_determinants,
        "matroid":"uniform U(3,4): every triple is transverse; the four-set is the unique circuit",
        "central_OS_betti":[1,4,6,3],
        "deck_group":"(Z2)^2 translating the four sign labels",
        "deck_character_by_degree":{"identity":[1,4,6,3],"three_nonidentity_elements":[1,0,-2,-1]},
        "rational_character_decomposition":{"H0":"1","H1":"1+a+b+ab","H2":"2a+2b+2ab","H3":"a+b+ab"},
        "resolution":"blow up the existing fourfold marked-intersection center; exceptional P2 contains four lines with no triple concurrence",
        "coefficient_excess":false,
        "generated_by_existing_marked_OS_Cech":true,
        "new_carrier_datum":false
    });
    fs::write("../results/five-site-double-soft-wall-arrangement.json",serde_json::to_string_pretty(&packet).unwrap()+"\n").unwrap();
    println!("{}",serde_json::to_string(&packet).unwrap());
}
