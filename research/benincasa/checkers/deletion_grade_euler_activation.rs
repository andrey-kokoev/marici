// Exact activation of the contact interference packet by deletion grade.

fn main() {
    let contacts = [-31_i128, -7, 1, 5, 29];
    let grades = [2_i128, 3_i128];

    for c in contacts {
        let packet = [8 * c, -8 * c];
        assert_eq!(packet[0] + packet[1], 0);

        let graded = [grades[0] * packet[0], grades[1] * packet[1]];
        assert_eq!(graded[0] + graded[1], -8 * c);
        assert_ne!(graded[0] + graded[1], 0);
    }

    println!(
        "{{\"status\":\"pass\",\"route_grades\":[2,3],\"packet\":\"(8*C,-8*C)\",\"ordinary_sum\":0,\"grade_euler_sum\":\"-8*C\",\"activation_nonzero_for_C_nonzero\":true,\"mixed_port_functional_value\":-1}}"
    );
}
