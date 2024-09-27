#include <iostream>
#include <unordered_map>
#include <vector>
#include <cstdlib>

class RandomizedSet {
  std::unordered_map<int, int> indexes;
  std::vector<int> data;

  public:
    RandomizedSet() = default;

    bool insert(int val) {
      if (indexes.find(val) != indexes.end()) {
        return false;
      }
      data.push_back(val);
      indexes[val] = data.size() - 1;
      return true;
    }

    bool remove(int val) {
      if (indexes.find(val) == indexes.end()) {
        return false;
      }

      int temp = data[data.size() - 1];
      data[data.size() - 1] = val;
      data[indexes[val]] = temp;
      indexes[temp] = indexes[val];
      data.pop_back();
      indexes.erase(val);

      return true;
    }

    int getRandom() {
      int randomIndex = std::rand() % data.size();
      return data[randomIndex];
    }
};


int main() {
  RandomizedSet randomSet;

  bool param1 = randomSet.insert(1);
  bool param2 = randomSet.remove(2);
  bool param3 = randomSet.insert(2);
  int param4 = randomSet.getRandom();
  bool param5 = randomSet.remove(1);
  bool param6 = randomSet.insert(2);
  int param7 = randomSet.getRandom();

  std::cout << param1 << std::endl;
  std::cout << param2 << std::endl;
  std::cout << param3 << std::endl;
  std::cout << param4 << std::endl;
  std::cout << param5 << std::endl;
  std::cout << param6 << std::endl;
  std::cout << param7 << std::endl;

  return 0;
}