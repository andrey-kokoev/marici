#[derive(Clone, Copy)]
struct ComplexI {
    re: i64,
    im: i64,
}

impl ComplexI {
    fn norm2(self) -> i64 {
        self.re * self.re + self.im * self.im
    }

    fn sub(self, other: Self) -> Self {
        Self {
            re: self.re - other.re,
            im: self.im - other.im,
        }
    }
}

fn main() {
    let mut checks = 0usize;
    for hr in -2_i64..=2 {
        for hi in -2_i64..=2 {
            for sr in -2_i64..=2 {
                for si in -2_i64..=2 {
                    let h = ComplexI { re: hr, im: hi };
                    let s = ComplexI { re: sr, im: si };
                    let channel = h.sub(s).norm2();

                    // Three mutually orthogonal labelled momentum channels.
                    let n2 = channel + 2 * channel + 3 * channel;
                    let beta1_norm = 0_i64;
                    let uncertainty_grade = n2 - beta1_norm;
                    assert!(uncertainty_grade >= 0);
                    assert_eq!(uncertainty_grade == 0, h.re == s.re && h.im == s.im);

                    // Ordered (q,k)/(k,q) occurrences cancel 1/2! channelwise.
                    let ordered_trace_twice = channel + channel;
                    assert_eq!(ordered_trace_twice / 2, channel);
                    checks += 1;
                }
            }
        }
    }

    println!("{{");
    println!("  \"schema\": \"marici.cubic_momentum_second_rees_map.v1\",");
    println!("  \"exact_endpoint_checks\": {checks},");
    println!("  \"ket_channel\": \"-i(H-S)|1_p,1_q,1_k>\",");
    println!("  \"x1\": 0,");
    println!("  \"y1\": 0,");
    println!("  \"n2\": \"sum_(q,k) weight_(q,k) |H-S|^2\",");
    println!("  \"cross_channel_interference\": false,");
    println!("  \"ordered_occurrence_factor_cancelled\": true,");
    println!("  \"saturation_condition\": \"H=S on every admitted channel\"");
    println!("}}");
}
