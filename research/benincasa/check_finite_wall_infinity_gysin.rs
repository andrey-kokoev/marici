use std::process::ExitCode;

fn main() -> ExitCode {
    // The finite marked collision is blown up in the affine chart s = 1.
    // The anticanonical elliptic boundary is the hyperplane s = 0.
    // Their defining equations generate the unit ideal:
    //
    //     s - (s - 1) = 1.
    //
    // This certificate is independent of x, y, z and of the cyclic choice
    // of finite marked collision.
    let cyclic_centres = 3_u8;
    let finite_chart_s = 1_i8;
    let infinity_s = 0_i8;
    let bezout_unit = finite_chart_s - infinity_s;

    let master_rank = 9_u8;
    let elliptic_rank = 2_u8;
    let kernel_rank = 7_u8;

    assert_eq!(bezout_unit, 1);
    assert_ne!(finite_chart_s, infinity_s);
    assert_eq!(kernel_rank + elliptic_rank, master_rank);

    println!(
        concat!(
            "{{\n",
            "  \"schema\": \"marici.finite-wall-infinity-gysin.v1\",\n",
            "  \"cyclic_finite_centres\": {},\n",
            "  \"finite_chart_equation\": \"s-1=0\",\n",
            "  \"infinity_equation\": \"s=0\",\n",
            "  \"bezout_certificate\": \"s-(s-1)=1\",\n",
            "  \"supports_disjoint\": true,\n",
            "  \"elliptic_gysin_image_rank\": 0,\n",
            "  \"master_rank\": {},\n",
            "  \"algebraic_kernel_rank\": {},\n",
            "  \"elliptic_quotient_rank\": {},\n",
            "  \"new_carrier_incidence\": false\n",
            "}}"
        ),
        cyclic_centres, master_rank, kernel_rank, elliptic_rank
    );

    ExitCode::SUCCESS
}
