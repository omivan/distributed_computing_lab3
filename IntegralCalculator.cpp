#include "IntegralCalculator.hpp"
#include <omp.h> 
#include <cmath>

double IntegralCalculator::calculate(double a, double b, int n, const Function& f, int numThreads) {
    double step = (b - a) / n; 
    double sum = 0.0;


    omp_set_num_threads(numThreads);

    #pragma omp parallel for reduction(+:sum)
    for (int i = 0; i < n; ++i) {
        double x = a + (i + 0.5) * step; 
        sum += f.calculate(x);         
    }

    return sum * step;
}
