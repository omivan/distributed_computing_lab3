#include "Function.hpp"
#include <cmath>

double Function::calculate(double t) const {
    return std::sin(2 * t) * std::cos(3 * t);
}
