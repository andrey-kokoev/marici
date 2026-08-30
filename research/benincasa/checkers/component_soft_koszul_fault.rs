// Exact rank audit of the two-route component/soft Koszul packet.

fn fiber_homology(q: i128, y: i128) -> [usize; 3] {
    let rank_d1 = usize::from(q != 0 || y != 0);
    let rank_d0 = usize::from(q != 0 || y != 0);

    // d1=(2q,y)^T and d0=(y,-2q), hence d0*d1=0.
    assert_eq!(y * (2 * q) + (-2 * q) * y, 0);
    [1 - rank_d1, 2 - rank_d1 - rank_d0, 1 - rank_d0]
}

fn main() {
    assert_eq!(fiber_homology(3, 5), [0, 0, 0]);
    assert_eq!(fiber_homology(0, 5), [0, 0, 0]);
    assert_eq!(fiber_homology(3, 0), [0, 0, 0]);
    assert_eq!(fiber_homology(0, 0), [1, 2, 1]);

    println!(
        "{{\"status\":\"pass\",\"generic\":[0,0,0],\"component_only\":[0,0,0],\"soft_only\":[0,0,0],\"corner\":[1,2,1],\"complex\":\"Koszul(2q,y)\"}}"
    );
}
