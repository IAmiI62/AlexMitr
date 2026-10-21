#include <iostream>
#include <cmath>

int main() {
    double x = 0; // Обязательно объявляем x
    constexpr auto Pi = std::acos(x) * 2; // ОШИБКА КОМПИЛЯЦИИ
    std::cout << Pi << std::endl;
    return 0;
}