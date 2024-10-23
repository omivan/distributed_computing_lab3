#include <iostream>
#include <cstdlib>
#include <cmath>
#include <chrono>  
#include "IntegralCalculator.hpp"
#include "Function.hpp"

int main(int argc, char* argv[]) {
    if (argc != 3) {
        std::cerr << "Неправильна кількість аргументів. Використання: <program> <кількість інтервалів> <кількість потоків>\n";
        return 1;
    }

    int intervals = std::stoi(argv[1]);
    int threads = std::stoi(argv[2]);

    Function f;
    IntegralCalculator calculator;

    double a = 0;
    double b = M_PI / 2;

    auto start = std::chrono::high_resolution_clock::now();

    double result = calculator.calculate(a, b, intervals, f, threads);

    auto end = std::chrono::high_resolution_clock::now();
    
    std::chrono::duration<double> duration = end - start;

    std::cout << "Інтеграл від sin(2t) * cos(3t) на [0, pi/2] = " << result << std::endl;
    std::cout << "Час виконання: " << duration.count() << " секунд" << std::endl;

    return 0;
}
