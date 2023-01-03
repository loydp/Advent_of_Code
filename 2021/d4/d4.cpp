/**
 * @file d4.cpp
 * @author Peter Loyd
 * @brief Day 4 of Advent of Code 2021
 * @version 0.1
 * @date 2023-01-02
 * 
 * @copyright Copyright (c) 2023
 * 
 */

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
 * Also holds the numbers in a matrix to check filled positions
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

   Board(const Board &t) {
      this->nums = t.nums;
      this->dict = t.dict;
   }

   int fill_number(int num) {
      if (dict.count(num)) {
         tuple<int, int> coord = dict.at(num);
         int row = get<0>(coord);
         int col = get<1>(coord);
         this->nums[row][col] = true;
         hello += 1;
         if (bingo(row, col)) {
            return score(num);
         }
      }
      return 0;
   }

   void print() {
      printf("\nBoard: nums\n");
      for (auto row : this->nums) {
         for (int i = 0; i < board_size; i++) {
            cout << " " << row[i];
         }
         printf("\n");
      }
   }

   private:

   int score(int num) {
      int leftover = 0;
      for (auto coord : dict) {
         int k = coord.first;
         int row = get<0>(coord.second);
         int col = get<1>(coord.second);
         if (!nums[row][col]) {
            leftover += k;
         }
      }
      return leftover * num;
   }

   /**
    * @brief Check to see if a bingo board has achieved a bingo
    * 
    * @param row 
    * @param col 
    * @return true 
    * @return false 
    */
   bool bingo(int row, int col) {
      // take a row, check every cell in it
      int r = 0;
      for (auto cell : nums[row]) {
         if (cell)
            r++;
         else
            break;
      }
      if (r == board_size)
         return true;

      // hold the column, check each row for that column
      int c = 0;
      for (int i = 0; i < board_size; i++) {
         if (nums[i][col])
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
         count++;
         boards.emplace_back(Board(matrix));
         //boards.push_back(Board(matrix));
         matrix.clear();
      }
   }

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

int sol2(vector<int> &numbers, vector<Board> &boards) {
   int score;
   vector<int> scores;
   vector<bool> won(boards.size(), false);
   for (auto num : numbers) {
      for (int i = 0; i < boards.size(); i++) {
         if (won[i] == true)
            continue;
         score = boards[i].fill_number(num);
         if (score) {
            won[i] = true;
            scores.push_back(score);
            score = 0;
            if (boards.size() == scores.size()) {
               return scores[scores.size() - 1];
            }
         }
      }
   }
   return -1;
}

const string path = "data.txt";
//const string path = "testdata.txt";


int main() {
   vector<string> data = get_data(path);
   vector<int> numbers = get_nums(data);
   vector<Board> boards = get_boards(data);

   vector<int> numbers2 = numbers;
   vector<Board> boards2 = boards;

   int i = sol1(numbers, boards);
   cout << i << endl;

   int k = sol2(numbers2, boards2);
   cout << k << endl;

   return 0;
}