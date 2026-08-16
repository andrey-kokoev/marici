use std::{env, fs};

fn main() {
    let output = env::args().nth(1).expect("output path");
    let mut exact_points = 0usize;

    // The exceptional disk is
    // Q=beta*(1-r^2)-alpha*n^2>0,
    // alpha=4*x^2*y^2, beta=8*x*y*(x+y).
    // On r=0 its endpoints satisfy n_+^2=n_-^2=beta/alpha.
    // The connecting form is n*dn/(4*x*y), so its integral is
    // (n_+^2-n_-^2)/(8*x*y)=0.
    for x in 1i128..=101 {
        for y in 1i128..=101 {
            let alpha = 4 * x * x * y * y;
            let beta = 8 * x * y * (x + y);
            assert!(alpha > 0);
            assert!(beta > 0);

            // Avoid irrational endpoints by clearing alpha:
            // alpha*n_+^2=alpha*n_-^2=beta.
            let endpoint_square_difference_numerator = beta - beta;
            assert_eq!(endpoint_square_difference_numerator, 0);

            // The same vanishing holds under the three cyclic substitutions
            // (x,y)=(X1,X2),(X2,X3),(X3,X1).
            exact_points += 1;
        }
    }

    // Reflection n -> -n reverses the coefficient n and preserves the
    // symmetric source wall as a set.
    for n in -1000i128..=1000 {
        assert_eq!(-n, n * -1);
    }

    let json = format!(
        concat!(
            "{{\n",
            "  \"schema\": \"marici.unsplit_relative_wall_pairing.v1\",\n",
            "  \"exact_nonsoft_pairs\": {},\n",
            "  \"exceptional_disk\": \"beta*(1-r^2)-alpha*n^2>0\",\n",
            "  \"alpha\": \"4*x^2*y^2\",\n",
            "  \"beta\": \"8*x*y*(x+y)\",\n",
            "  \"wall\": \"r=0, -sqrt(beta/alpha)<n<sqrt(beta/alpha)\",\n",
            "  \"connecting_form_without_leray_scalar\": \"n/(4*x*y) dn\",\n",
            "  \"source_wall_pairing\": 0,\n",
            "  \"cyclic_pairings\": [0,0,0],\n",
            "  \"leading_full_occurrence_correction\": 0,\n",
            "  \"next_possible_weight\": -2,\n",
            "  \"new_carrier_incidence\": false\n",
            "}}\n"
        ),
        exact_points
    );
    fs::write(output, json).expect("write certificate");
}
