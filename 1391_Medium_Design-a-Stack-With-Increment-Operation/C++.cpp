#include <iostream>
#include <vector>

class CustomStack {
  public:
    int maxSize;
    std::vector<int> stack;
    std::vector<int> inc;

    CustomStack(int maxSize) {
      this->maxSize = maxSize;
    }
    
    void push(int x) {
      if (stack.size() < maxSize) {
        stack.push_back(x);
        inc.push_back(0);
      }
    }
    
    int pop() {
      if (stack.size() > 0) {
        int index = stack.size() - 1;
        int results = stack[index] + inc[index];
        if (index > 0) {
            inc[index - 1] += inc[index];
        }
        stack.pop_back();
        inc.pop_back();
        return results;
      }
      return -1;
    }
    
    void increment(int k, int val) {
      int index = std::min(k, (int)stack.size()) - 1;
      if (index >= 0) {
        inc[index] += val;
      }
    }
};

int main() {
  CustomStack obj(3);

  obj.push(1);
  obj.push(2);
  int popped1 = obj.pop();

  std::cout << popped1 << std::endl;

  obj.push(2);
  obj.push(3);
  obj.increment(5, 100);
  obj.increment(2, 100);
  int popped2 = obj.pop();
  int popped3 = obj.pop();
  int popped4 = obj.pop();
  int popped5 = obj.pop();

  std::cout << popped2 << std::endl;
  std::cout << popped3 << std::endl;
  std::cout << popped4 << std::endl;
  std::cout << popped5 << std::endl;

  return 0;
}