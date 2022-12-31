/**
 * @file d1.cpp
 * @author Peter Loyd
 * @brief Advent of Code 2022 Day 1
 * @version 1.0
 * @date 2022-12-30
 * 
 * @copyright Copyright (c) 2022
 * 
 */

#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

vector<int> get_data(string path) {
   int depth;
   string temp;
   vector<int> depth_arr = {};
   ifstream data_file;
   data_file.open(path);

   if (data_file.is_open()) {
      while (data_file >> temp) {
         depth_arr.push_back(stoi(temp));
      }
   }

   data_file.close();
   return depth_arr;
}

int sol(vector<int> &data, int window) {
   int last_sum = 0;
   for (int i = 0; i < window; i++)
      last_sum += data[i];
   int count = 0;
   int data_size = data.size();
   int end_at = data_size - (window - 1);
   int sm;
   for (int i = 1; i < end_at; i++) {
      sm = 0;
      for (int j = 0; j < window; j++)
         sm += data[i + j];
      if (sm > last_sum)
         count++;
      last_sum = sm;
   }
   return count;
}

//const string path = "resources/sample.txt";
const string path = "resources/d1.txt";

int main() {
   // get data
   vector<int> data = get_data(path);
   // part 1
   int result_1 = sol(data, 1);
   cout << result_1 << endl;
   // part 2
   int result_2 = sol(data, 3);
   cout << result_2 << endl;

   return 0;
}