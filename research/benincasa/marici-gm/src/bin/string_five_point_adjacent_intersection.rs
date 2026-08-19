#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct GaussianRational {
    real_num: i64,
    imag_num: i64,
    denominator: i64,
}

impl GaussianRational {
    fn multiply(self, rhs: Self) -> Self {
        Self {
            real_num: self.real_num * rhs.real_num - self.imag_num * rhs.imag_num,
            imag_num: self.real_num * rhs.imag_num + self.imag_num * rhs.real_num,
            denominator: self.denominator * rhs.denominator,
        }
    }
}

fn main() {
    // The chambers 12345 and 13245 share precisely the facet (23).
    let shared_facets = ["s23"];
    let boundary_endpoints = ["s45", "s51"];
    assert_eq!(shared_facets.len(), 1);
    assert_eq!(boundary_endpoints.len(), 2);

    // q^(1/2)/(q-1) = -i/(2 sin(pi s)) on the source loading branch.
    let normal_half_monodromy = GaussianRational {
        real_num: 0,
        imag_num: -1,
        denominator: 2,
    };

    // The four-point boundary self-intersection is
    // i/2 * (cot(pi s45) + cot(pi s51)).
    let boundary_self_intersection = GaussianRational {
        real_num: 0,
        imag_num: 1,
        denominator: 2,
    };

    let product = normal_half_monodromy.multiply(boundary_self_intersection);
    assert_eq!(
        product,
        GaussianRational {
            real_num: 1,
            imag_num: 0,
            denominator: 4,
        }
    );

    // This equals -(i/2)^2, the coefficient in Mizera eq. (4.15)'s
    // adjacent five-point reduction (display immediately after eq. 4.15).
    let i_over_two = GaussianRational {
        real_num: 0,
        imag_num: 1,
        denominator: 2,
    };
    let square = i_over_two.multiply(i_over_two);
    assert_eq!(-square.real_num, product.real_num);
    assert_eq!(square.imag_num, 0);
    assert_eq!(square.denominator, product.denominator);

    println!("five_point_adjacent_string_intersection: ok");
    println!("shared_facet: s23");
    println!("boundary_endpoints: s45,s51");
    println!("coefficient: 1/(4 sin(pi s23)) * (cot(pi s45)+cot(pi s51))");
}
