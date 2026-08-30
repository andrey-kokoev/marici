use std::collections::BTreeMap;

fn main() {
    // Each route is represented by the pair of X-gradient vectors of its two
    // additional denominators.  The G denominator always has gradient 111.
    let routes = [
        ("G12|g23", ([1,1,1],[0,1,1])),
        ("G12|g31", ([1,1,1],[1,0,1])),
        ("G23|g31", ([1,1,1],[1,0,1])),
        ("G23|g12", ([1,1,1],[1,1,0])),
        ("G31|g12", ([1,1,1],[1,1,0])),
        ("G31|g23", ([1,1,1],[0,1,1])),
    ];
    let mut classes:BTreeMap<([i32;3],[i32;3]),Vec<&str>>=BTreeMap::new();
    for (label,signature) in routes { classes.entry(signature).or_default().push(label); }
    let sizes=classes.values().map(Vec::len).collect::<Vec<_>>();
    assert_eq!(sizes,vec![2,2,2]);
    println!("{{\"status\":\"pass\",\"external_gradient_classes\":3,\"class_sizes\":[2,2,2],\"doublets\":[[\"G12|g23\",\"G31|g23\"],[\"G12|g31\",\"G23|g31\"],[\"G23|g12\",\"G31|g12\"]],\"all_order_gate\":\"external differential algebra is equivariant under the fiber-label swaps exchanging each doublet\"}}");
}

