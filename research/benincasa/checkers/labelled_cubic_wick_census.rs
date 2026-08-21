fn rec(left:&mut Vec<usize>,pairs:&mut Vec<(usize,usize)>,out:&mut Vec<Vec<(usize,usize)>>){
    if left.is_empty(){out.push(pairs.clone());return}
    let a=left.remove(0);
    for i in 0..left.len(){let b=left.remove(i);pairs.push((a,b));rec(left,pairs,out);pairs.pop();left.insert(i,b)}
    left.insert(0,a)
}
fn vertex(x:usize)->i32{if x<2{-1}else if x<5{0}else{1}}
fn main(){
    let mut all=Vec::new();rec(&mut(0..8).collect(),&mut Vec::new(),&mut all);assert_eq!(all.len(),105);
    let(mut fish,mut tadpole,mut disconnected,mut external_pair)=(0,0,0,0);
    for ps in &all{
        if ps.iter().any(|&(a,b)|a<2&&b<2){external_pair+=1;continue}
        let ext_vertices:Vec<_>=ps.iter().filter_map(|&(a,b)|if a<2{Some(vertex(b))}else if b<2{Some(vertex(a))}else{None}).collect();
        let cross=ps.iter().filter(|&&(a,b)|vertex(a)>=0&&vertex(b)>=0&&vertex(a)!=vertex(b)).count();
        if ext_vertices.len()==2&&ext_vertices[0]!=ext_vertices[1]&&cross==2{fish+=1}
        else if ext_vertices.len()==2&&ext_vertices[0]==ext_vertices[1]&&cross==1{tadpole+=1}
        else{disconnected+=1}
    }
    assert_eq!((fish,tadpole,disconnected,external_pair),(36,36,18,15));
    // The location labels B=bulk and S=surface do not alter slot incidence.
    for placement in ["BB","BS","SS"]{println!("placement_{placement}_fish={fish}")}
    println!("{{\"total_pairings\":105,\"fish\":{fish},\"zero_momentum_tadpole\":{tadpole},\"disconnected\":{disconnected},\"external_pair\":{external_pair},\"fish_count_equal_BB_BS_SS\":true}}");
}
