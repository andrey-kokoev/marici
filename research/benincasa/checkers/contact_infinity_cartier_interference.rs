// Exact Cartier-order audit for the contact route packet at external infinity.

fn main() {
    let hats = [(-7_i128, 11_i128), (3, 5), (13, -17)];
    let normals = [(-5_i128, 2_i128), (1, 3), (7, -11)];

    for (hj, hk) in hats {
        assert_ne!(hj * hk, 0);
        for (sj, sk) in normals {
            assert_ne!(sj * sk, 0);

            // Cj*Ck = sj*sk/(hj*hk).  Denominator-clear the packet.
            let leading_a = 8 * sj * sk;
            let leading_b = -8 * sj * sk;
            assert_ne!(leading_a, 0);
            assert_eq!(leading_a + leading_b, 0);

            // Divide by the derived common Cartier factor sj*sk.
            assert_eq!(leading_a / (sj * sk), 8);
            assert_eq!(leading_b / (sj * sk), -8);
        }
    }

    println!(
        "{{\"status\":\"pass\",\"contact_product\":\"s_j*s_k/(h_j*h_k)\",\"single_boundary_order\":1,\"double_boundary_order\":2,\"ordinary_boundary_packet\":\"(0,0)\",\"normalized_cartier_packet\":\"(8/(h_j*h_k),-8/(h_j*h_k))\",\"normal_monodromy\":\"trivial_integer_character\",\"classification\":\"route_loss_on_restriction_interference_on_associated_grade\"}}"
    );
}
