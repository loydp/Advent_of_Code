#include <iostream>
using namespace std;
#include <tuple>
#include <vector>
#include <string>
#include <fstream>

typedef vector<tuple<char, int>> cmd_tuple;

cmd_tuple get_data(string path) {
   cmd_tuple commands;
   ifstream directions(path);
   string temp;

   char next_char;
   char next_int;

   if (directions.is_open()) {
      int count = 0;
      while (directions >> temp) {
         if (count % 2 == 0) {
            next_char = (char) temp[0];
         } else {
            next_int = stoi(temp);
            commands.push_back(make_tuple(next_char, next_int));
         }
         count++;
      }
   }
   return commands;
}


const string path = "directions.txt";


int part1(cmd_tuple data) {
   int forward = 0;
   int depth = 0;
   for (auto cmd : data) {
      if (get<0>(cmd) == 'd') {
         depth += get<1>(cmd);
      } else if (get<0>(cmd) == 'u')
      {
         depth -= get<1>(cmd);
      } else
      {
         forward += get<1>(cmd);
      }
   }
   return forward * depth;
}

int part2(cmd_tuple data) {
   int forward = 0;
   int aim = 0;
   int depth;
   for (auto cmd : data) {
      if (get<0>(cmd) == 'd') {
         aim += get<1>(cmd);
      } else if (get<0>(cmd) == 'u')
      {
         aim -= get<1>(cmd);
      } else
      {
         forward += get<1>(cmd);
         depth += aim * get<1>(cmd);
      }
   }
   return forward * depth;
}

int main() {
   // get data
   cmd_tuple data = get_data(path);

   int sol1 = part1(data);
   cout << sol1 << endl;

   int sol2 = part2(data);
   cout << sol2 << endl;

   return 0;
}