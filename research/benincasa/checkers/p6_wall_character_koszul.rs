use std::fs;

fn rank(mut a:Vec<Vec<i64>>)->usize{let rows=a.len();let cols=a.first().map_or(0,Vec::len);let mut r=0;for c in 0..cols{let Some(p)=(r..rows).find(|i|a[*i][c]!=0)else{continue};a.swap(r,p);for i in r+1..rows{if a[i][c]!=0{let x=a[i][c];let y=a[r][c];for j in c..cols{a[i][j]=a[i][j]*y-a[r][j]*x}}}r+=1;}r}
fn main(){
    // Character ratio target/source is (-1,-1), hence chi_i-1=-2.
    // Cochains: C -> C^2 -> C with d0=(-2,-2)^T and d1=(-2,2).
    let d0=vec![vec![-2],vec![-2]];
    let d1=vec![vec![-2,2]];
    let r0=rank(d0);let r1=rank(d1);
    assert_eq!((r0,r1),(1,1));
    let h0=1-r0;let h1=2-r0-r1;let h2=1-r1;
    assert_eq!((h0,h1,h2),(0,0,0));
    let packet=format!(concat!(
        "{{\n",
        "  \"schema\": \"marici.p6_wall_character_koszul.v1\",\n",
        "  \"relative_character\": [-1,-1],\n",
        "  \"d0\": [[-2],[-2]],\n",
        "  \"d1\": [[-2,2]],\n",
        "  \"differential_ranks\": [{},{}],\n",
        "  \"cohomology_dimensions\": [{},{},{}],\n",
        "  \"exceptional_product_character\": 1,\n",
        "  \"exceptional_resonance_descends\": false\n",
        "}}\n"),r0,r1,h0,h1,h2);
    fs::write("research/benincasa/results/p6-wall-character-koszul.json",packet).unwrap();
}
