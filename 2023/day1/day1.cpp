/**
 * @file day1.cpp
 * @author Peter Loyd
 * @brief For Advent of Code
 * @version 0.1
 * @date 2023-12-03
 *
 * @copyright Copyright (c) 2023
 *
 */

#include <vector>
#include <string>
#include <iostream>
#include <fstream>
#include <unordered_map>

std::string INPUT_URL = "input.dat";
// std::string INPUT_URL = "example.dat";
// std::string INPUT_URL = "example2.dat";

std::vector<std::string> get_input(const std::string &input_url)
{
	std::vector<std::string> lines;
	std::ifstream file(input_url);
	if (file.is_open())
	{
		std::string temp_string;
		while (file.good())
		{
			std::getline(file, temp_string);
			lines.emplace_back(temp_string);
		}
	}

	return lines;
}

char get_first_digit(const std::string &line)
{
	for (char c : line)
	{
		if (isdigit(c))
		{
			return c;
		}
	}
	return '0';
}

char get_last_digit(const std::string &line)
{
	for (int i = line.length() - 1; i >= 0; i--)
	{
		if (isdigit(line[i]))
		{
			return line[i];
		}
	}
	return '0';
}

int sol_1(const std::vector<std::string> &input)
{
	int total = 0;
	for (std::string line : input)
	{
		char first = get_first_digit(line);
		char last = get_last_digit(line);
		std::string combined = std::string() + first + last;
		total = total + stoi(combined);
	}

	return total;
}

int get_first_num(const std::string &line, const std::unordered_map<std::string, int> &map)
{
	int min_int;
	int min_val = line.length();

	for (auto kv : map)
	{
		int pos = line.find(kv.first);
		if (pos < min_val && pos != -1)
		{
			min_val = pos;
			min_int = kv.second;
		}
	}

	return min_int;
}

int get_last_num(const std::string &line, const std::unordered_map<std::string, int> &map)
{
	int last_int;
	int last_pos = 0;

	for (auto kv : map)
	{
		int pos = line.rfind(kv.first);
		if (pos > last_pos)
		{
			last_pos = pos;
			last_int = kv.second;
		}
	}
	return last_int;
}

int sol_2(const std::vector<std::string> &input)
{
	int total = 0;

	std::unordered_map<std::string, int> num_map = {
		{"one", 1},
		{"two", 2},
		{"three", 3},
		{"four", 4},
		{"five", 5},
		{"six", 6},
		{"seven", 7},
		{"eight", 8},
		{"nine", 9},
		{"1", 1},
		{"2", 2},
		{"3", 3},
		{"4", 4},
		{"5", 5},
		{"6", 6},
		{"7", 7},
		{"8", 8},
		{"9", 9},
	};

	for (std::string line : input)
	{
		int first = get_first_num(line, num_map);
		first = first * 10;
		// std::cout << first << std::endl;
		int last = get_last_num(line, num_map);
		// std::cout << last << std::endl;
		total = total + first + last;
	}

	return total;
}

int main()
{
	std::vector<std::string> input = get_input(INPUT_URL);

	int res1 = sol_1(input);
	std::cout << "sol1 -> " << res1 << std::endl;

	int res2 = sol_2(input);
	std::cout << "sol2 -> " << res2 << std::endl;

	return 0;
}