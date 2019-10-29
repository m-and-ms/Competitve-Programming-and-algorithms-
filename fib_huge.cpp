#include <iostream>
long long get_fib_huge(long long n, long long m) {
    if (n <= 1)
        return n;

    long long b = 0;
    long long a  = 1;

    for (long long i = 0; i < n - 1; ++i) {
        long long tmp_previous = b;
        b = a;
        a = tmp_previous + a;
    }

    return a % m;
}

int main() {
    long long n, m;
    std::cin >> n >> m;
    std::cout << get_fib_huge(n, m) << '\n';
}
