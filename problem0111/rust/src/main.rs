use code_timing_macros::{time_function, time_snippet};

fn get_s(n: u32, d: u32) -> u64 {
    for m in (1..n).rev() {
        let mut primes = std::collections::HashSet::new();
        let wildcards = (n - m) as usize;

        // Generate all combinations of positions for wildcards
        generate_candidates(n, d, wildcards, 0, 0, &mut primes);

        if !primes.is_empty() {
            let sum: u64 = primes.iter().sum();
            println!("S({n}, {d}) = {sum} (M={m})");
            return sum;
        }
    }
    0
}

fn generate_candidates(
    n: u32,
    digit: u32,
    wildcards_left: usize,
    current_pos: u32,
    current_val: u64,
    found: &mut std::collections::HashSet<u64>,
) {
    if current_pos == n {
        if miller_rabin::is_prime(&current_val, 2) {
            found.insert(current_val);
        }
        return;
    }

    if wildcards_left > 0 && (n - current_pos) as usize >= wildcards_left {
        // Option A: Use a wildcard here (any digit except the repeating one)
        for d in 0..10 {
            if d == digit {
                continue;
            }
            if current_pos == 0 && d == 0 {
                continue;
            } // No leading zero

            generate_candidates(
                n,
                digit,
                wildcards_left - 1,
                current_pos + 1,
                current_val * 10 + d as u64,
                found,
            );
        }
    }

    // Option B: Use the repeating digit 'digit' here
    // Only if we aren't forced to use a wildcard to reach the required count
    if (n - current_pos) as usize > wildcards_left {
        if !(current_pos == 0 && digit == 0) {
            // No leading zero
            generate_candidates(
                n,
                digit,
                wildcards_left,
                current_pos + 1,
                current_val * 10 + digit as u64,
                found,
            );
        }
    }
}

#[time_function]
fn main() {
    for n in [4, 10] {
        time_snippet!({
            let mut sum: u64 = 0;
            for i in 0..10 {
                sum += get_s(n, i);
            }
            println!("{sum}");
        });
    }
}
