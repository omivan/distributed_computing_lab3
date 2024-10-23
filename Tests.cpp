#include <cassert>
#include <iostream>
#include <cmath>
#include "IntegralCalculator.hpp"
#include "Function.hpp"

int total_tests = 0;
int passed_tests = 0;

void run_test(double a, double b, int n, int numThreads, double expected_value) {
    Function f;
    IntegralCalculator calculator;
    
    double result = calculator.calculate(a, b, n, f, numThreads);

    std::cout << "Фактичне значення: " << result << std::endl;
    std::cout << "Очікуване значення: " << expected_value << std::endl;

    total_tests++;

    if (std::abs(result - expected_value) < 1e-5) {
        std::cout << "Тест виконано успішно!" << std::endl;
        passed_tests++;  
    } else {
        std::cout << "Тест провалено!" << std::endl;
    }

    assert(std::abs(result - expected_value) < 1e-5);
}

void test_integral_1() {
    std::cout << "-------------------------------\n";
    std::cout << "Тест 1: Інтеграл від 0 до π/2 на 10000 розбиттів, 1 поток" << std::endl;
    run_test(0, M_PI / 2, 10000, 1, -0.4);
}

void test_integral_2() {
    std::cout << "-------------------------------\n";
    std::cout << "Тест 2: Інтеграл від 0 до π/2 на 1000000 розбиттів, 4 потоки" << std::endl;
    run_test(0, M_PI / 2, 1000000, 4, -0.4);
}

void run_all_tests() {
    test_integral_1();
    std::cout << std::endl;
    test_integral_2();
    std::cout << std::endl;

    std::cout << "-------------------------------\n";
    std::cout << "Результат тестування: " << passed_tests << " з " << total_tests << " тестів пройшли успішно.\n";
    if (passed_tests == total_tests) {
        std::cout << "Всі тести пройшли успішно!" << std::endl;
    } else {
        std::cout << "Деякі тести не пройшли." << std::endl;
    }
}

int main() {
    run_all_tests();
    return 0;
}
