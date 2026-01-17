use code_timing_macros::time_function;
use num_bigint::BigUint;
use num_traits::identities::One;

const UNIQUE_SOLUTIONS: i32 = 4_000_000;
// If there are UNIQUE_SOLUTION, this means n should have double the amount of divisors
// plus one for the squares.
const REQUIED_DIVISORS: i32 = 2 * UNIQUE_SOLUTIONS + 1;

// First 15 primes, to be used in prime factorization
const PRIMES: [u128; 15] = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47];

const UPPER_BOUND: i32 = 30;

fn search(
    prime_idx: i64,
    max_exp: i32,
    current_n: BigUint,
    current_divisors: i32,
    best_n: &mut Option<BigUint>,
) {
    // Prune, current value is already too high.
    if let &mut Some(ref best) = best_n {
        if current_n >= *best {
            return;
        }
    }

    // Found a better candidate?
    if current_divisors > REQUIED_DIVISORS {
        if best_n.is_none() || current_n < *best_n.as_ref().unwrap() {
            println!("Found solution: {} ", current_n);
            *best_n = Some(current_n.clone());
        }
    }

    // Depleted all primes
    if prime_idx >= PRIMES.len() as i64 {
        return;
    }

    let p = BigUint::from(PRIMES[prime_idx as usize]);
    let mut new_n = current_n.clone() * p.pow(max_exp as u32 + 1);

    // Try all exponents for this prime_idx from the maximum to 0,
    // This enforces decreasing exponents.
    for exp in (0..=max_exp).rev() {
        new_n /= &p;

        if let &mut Some(ref best) = best_n {
            if new_n > *best {
                continue;
            }
        }

        let new_divisors = current_divisors * (2 * exp + 1);
        search(prime_idx + 1, exp, new_n.clone(), new_divisors, best_n);
    }
}

#[time_function]
fn main() {
    let mut n: Option<BigUint> = None;
    let prime_idx: i64 = 0;
    search(prime_idx, UPPER_BOUND, BigUint::one(), 1, &mut n);

    println!("{}", n.unwrap());
}
