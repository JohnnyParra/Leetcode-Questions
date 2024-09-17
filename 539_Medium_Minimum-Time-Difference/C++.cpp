#include <iostream>
#include <algorithm>
#include <climits>
#include <vector>

int findMinDifference(std::vector<std::string>& timePoints) {
    std::vector<int> minutes = {};
    for (std::string time: timePoints) {
      int hour = stoi(time.substr(0, 2));
      int min = stoi(time.substr(3));
      minutes.push_back(hour * 60 + min);
    }

    std::sort(minutes.begin(), minutes.end());

    int minDiff = INT_MAX;
    for (int i = 0; i < timePoints.size() - 1; i++) {
      minDiff = std::min(minDiff, minutes[i + 1] - minutes[i]);
    }

    return std::min(minDiff, (minutes[0] + (1440 - minutes[minutes.size() - 1])));
}

int main() {
  std::vector<std::string> vector1 = {"23:59","00:00"};
  std::vector<std::string> vector2 = {"00:00","23:59","00:00"};
  std::vector<std::string> vector3 = {"12:12","00:13"};

  std::cout << findMinDifference(vector1) << std::endl;
  std::cout << findMinDifference(vector2) << std::endl;
  std::cout << findMinDifference(vector3) << std::endl;

  return 0;
}
