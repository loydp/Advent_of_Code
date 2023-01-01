#include <iostream>
#include <vector>
using namespace std;
#include <fstream>
#include <string>

#include <list>


vector<string> get_data(string path) {
   vector<string> data;
   ifstream data_file(path);
   string temp_str;
   if (data_file.is_open()) {
      while (data_file >> temp_str) {
         data.push_back(temp_str);
      }
   }
   return data;
}

int sol1(vector<string> &data, int string_length) {
   int *records = new int[string_length]();
   for (auto str : data) {
      for (int i = 0; i < string_length; i++) {
         int bit = str[i] - '0';
         records[i] += bit;
      }
   }
   int half_val = data.size() / 2;
   for (int i = 0; i < string_length; i++) {
      if (records[i] > half_val) {
         records[i] = 1;
      } else {
         records[i] = 0;
      }
   }

   int gamma = 0;
   for (int i = string_length - 1; i >= 0; i--) {
      if (records[i] == 1) {
         int k = (string_length - 1) - i;
         gamma += (1 << k);
      }
   }

   int epsilon = 0;
   for (int i = string_length - 1; i >= 0; i--) {
      if (records[i] == 0) {
         int k = (string_length - 1) - i;
         epsilon += (1 << k);
      }
   }
   delete[] records;
   return gamma * epsilon;
}

int bin_string_2_int(string str) {
   int ret = 0;
   for (int i = str.length() -1; i >= 0; i--) {
      if (str[i] == '1') {
         int k = (str.length() - 1) - i;
         ret += (1 << k);
      }
   }
   return ret;
}

int sol2(vector<string> &data, int string_length) {
   vector<string> oxy = data;
   vector<string> co2 = data;

   vector<string> keep;

   string final_oxy;
   string final_co2;

   for (int i = 0; i < string_length; i++) {
      int oxy_count = 0;
      for (auto str : oxy) {
         if (str[i] == '1') {
            oxy_count++;
         }
      }

      // determine relevant bit
      int oxy_negate = oxy.size() - oxy_count;
      if (oxy_count >= oxy_negate) {
         oxy_count = 1;
      } else {
         oxy_count = 0;
      }

      for (auto str : oxy) {
         if (str[i] == oxy_count + '0') {
            keep.push_back(str);
         }
      }
      if (keep.size() == 1) {
         final_oxy = keep.front();
         keep.clear();
         break;
      }
      oxy = keep;
      keep.clear();
   }

   // -------

   for (int i = 0; i < string_length; i++) {
      int co2_count = 0;
      for (auto str : co2) {
         if (str[i] == '1') {
            co2_count++;
         }
      }

      // determine relevant bit
      int co2_negate = co2.size() - co2_count;
      if (co2_count < co2_negate) {
         co2_count = 1;
      } else {
         co2_count = 0;
      }

      for (auto str : co2) {
         if (str[i] == co2_count + '0') {
            keep.push_back(str);
         }
      }
      if (keep.size() == 1) {
         final_co2 = keep.front();
         keep.clear();
         break;
      }
      co2 = keep;
      keep.clear();
   }

   int final_o = bin_string_2_int(final_oxy);
   int final_c = bin_string_2_int(final_co2);

   return final_c * final_o;
}

const string path = "data.txt";
//const string path = "sample.txt";

int main() {
   // get the data as a list of strings
   vector<string> data = get_data(path);
   // sol 1
   int result_1 = sol1(data, data[0].length());
   cout << "Result 1: " << result_1 << endl;

   int result_2 = sol2(data, data[0].length());
   cout << "result 2: " << result_2 << endl;
   return 0;
} 