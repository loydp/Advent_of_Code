#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <iostream>
#include <unordered_map>
#include <tuple>
using namespace std;


const int board_size = 5;

/**
 * @brief Holds a bingo board.
 * Constructor takes a string of 25 numbers.
 * Numbers are placed into a map.
 * Also holds the numbers in a matrix to check positions.
 * Number 
 * 
 */
class Board {

   vector<vector<bool>> nums;
   unordered_map<int, tuple<int, int>> dict;
   int hello;

   public:
   Board(vector<int> input_nums) {
      int count = 0;
      hello = 0;
      for (int i = 0; i < board_size; i++) {
         vector<bool> row;
         for (int j = 0; j < board_size; j++) {
            dict[input_nums[count]] = make_tuple(i, j);
            row.push_back(0);
            count++;
         }
         nums.push_back(row);
      }
   }

   ~Board() {
      cout << "DESTROYING" << endl;
   }

   int fill_number(int num) {
      if (dict.count(num)) {
         tuple<int, int> coord = dict.at(num);
         int row = get<0>(coord);
         int col = get<1>(coord);
         this->nums[row][col] = true;
         hello += 1;
         if (bingo(row, col)) {
            cout << "Bingo!" << endl;
            print();
            return score(num);
         }
      }
      return 0;
   }

   void print() {
      /*
      printf("\nBoard dict keys: \n");
      for (auto coords : dict) {
         printf("keys: %i ", coords.first);
      }
      */
      printf("\nBoard: nums\n");
      for (auto row : this->nums) {
         for (int i = 0; i < board_size; i++) {
            cout << " " << row[i];
         }
         printf("\n");
      }
      printf("s: %i", hello);

   }

   private:

   int score(int num) {
      return 1;
   }

   bool bingo(int row, int col) {
      int r = 0;
      for (auto cell : nums[row]) {
         if (cell)
            r++;
         else
            break;
      }
      if (r == board_size)
         return true;

      int c = 0;
      for (int i = 0; i < board_size; i++) {
         if (nums[row][i])
            c++;
         else
            break;
      }
      if (c == board_size)
         return true;

      return false;
   }

};



/**
 * @brief Take in a path, return the data in the path in a vector of strings.
 * 
 * @param path a relative path to the input data
 * @return vector<string> the input data
 */
vector<string> get_data(string path) {
   vector<string> data;
   string temp;
   ifstream data_file(path);
   if (data_file.is_open()) {
      while (data_file >> temp) {
         data.push_back(temp);
      }
   }
   return data;
}

/**
 * @brief Look at the first line of the data, collect the numbers there and return them.
 * 
 * @param data the input data
 * @return vector<int> a list of numbers
 */
vector<int> get_nums(vector<string> &data) {
   vector<int> nums;
   stringstream numbers{data[0]};
   string called;
   while (std::getline(numbers, called, ',')) {
      nums.push_back(stoi(called));
   }
   return nums;
}

/**
 * @brief Generate boards using the input data
 * 
 * @param data 
 * @return vector<Board> 
 */
vector<Board> get_boards(vector<string> &data) {
   vector<Board> boards;
   vector<int> matrix;

   for (int i = 1; i < data.size(); i++) {
      int count = 0;
      matrix.push_back(stoi(data[i]));
      if (i % 25 == 0) {
         //printf("Before\n");
         printf("\nCount -> %i\n", count);
         count++;
         boards.push_back(Board(matrix));
         //printf("After\n");
         matrix.clear();
      }
   }
   boards.pop_back();
   boards.push_back(Board({1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5}));
   boards.push_back(Board({1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5}));
   boards.push_back(Board({1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5}));
   boards.push_back(Board({1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5}));
   boards.push_back(Board({1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5}));
   boards.push_back(Board({1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5}));
   boards.push_back(Board({1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5}));
   boards.push_back(Board({1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5}));
   boards.push_back(Board({1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5}));
   boards.push_back(Board({1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5}));
   boards.push_back(Board({1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5}));
   boards.push_back(Board({1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5}));
   printf("here");
   boards.pop_back();
   boards.push_back(Board({1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5}));
   boards.pop_back();
   boards.push_back(Board({1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5}));

   return boards;
}


int sol1(vector<int> &numbers, vector<Board> &boards) {
   int score;
   for (auto num : numbers) {
      for (int i = 0; i < boards.size(); i++) {
         score = boards[i].fill_number(num);
         if (score)
            return score;
      }
   }
   return 0;
}

//const string path = "data.txt";
const string path = "testdata.txt";


int main() {
   vector<string> data = get_data(path);
   vector<int> numbers = get_nums(data);
   vector<Board> boards = get_boards(data);

   int i = sol1(numbers, boards);
   cout << i << endl;

   return 0;
}