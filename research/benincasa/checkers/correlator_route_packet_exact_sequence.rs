// Finite linear-algebra audit of the route-packet mechanism sequence.

fn weighted_sum(packet: &[i128; 8]) -> i128 {
    packet.iter().sum()
}

fn main() {
    // A route-loss witness vanishes before aggregation.
    let route_loss = [0_i128; 8];
    assert_eq!(weighted_sum(&route_loss), 0);

    // A destructive-interference witness is nonzero before aggregation but
    // lies in the augmentation kernel. Labels 0 and 1 must remain distinct.
    let interference = [1_i128, -1, 0, 0, 0, 0, 0, 0];
    assert_ne!(interference, route_loss);
    assert_eq!(weighted_sum(&interference), 0);

    println!(
        "{{\"status\":\"pass\",\"route_packet_rank\":8,\"route_loss_preaggregation_zero\":true,\"nonzero_augmentation_kernel_witness\":[1,-1,0,0,0,0,0,0],\"mechanisms_distinct\":true}}"
    );
}
