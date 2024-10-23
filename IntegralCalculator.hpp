#ifndef INTEGRALCALCULATOR_HPP
#define INTEGRALCALCULATOR_HPP

#include "Function.hpp"

class IntegralCalculator {
public:
    double calculate(double a, double b, int n, const Function& f, int numThreads);
};

#endif 
