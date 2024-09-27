#include <iostream>
#include <vector>

class MyCalendarTwo {
    std::vector<std::pair<int, int>> singleBookings;
    std::vector<std::pair<int, int>> doubleBookings;

public:
    MyCalendarTwo() = default;
    
    bool book(int start, int end) {
        for (const auto& [s, e] : doubleBookings) {
            if (std::max(s, start) < std::min(e, end)) {
                return false;
            }
        }

        for (const auto& [s, e] : singleBookings) {
            if (std::max(s, start) < std::min(e, end)) {
                doubleBookings.push_back({std::max(s, start), std::min(e, end)});
            }
        }

        singleBookings.push_back({start, end});
        return true;
    }
};


int main() {
    MyCalendarTwo calendar;
    
    bool param_1 = calendar.book(10, 20);
    bool param_2 = calendar.book(50, 60);
    bool param_3 = calendar.book(10, 40);
    bool param_4 = calendar.book(5, 15);
    bool param_5 = calendar.book(5, 10);

    std::cout << std::boolalpha;
    std::cout << param_1 << std::endl;
    std::cout << param_2 << std::endl;
    std::cout << param_3 << std::endl;
    std::cout << param_4 << std::endl;
    std::cout << param_5 << std::endl;

  return 0;
}