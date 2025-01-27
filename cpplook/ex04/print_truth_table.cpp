#include <string>
#include <map>
#include <vector>
#include <algorithm>
#include <iostream>
#include <unordered_set>
#include "get_list.hpp"

using std::string;
using std::vector;
using std::map;
using std::unordered_set;

// 3*O(n) + O(2^n) + O(n*n) == O(2^n)
void print_truth_table(const string& formula)
{
	vector<char> vars;
	unordered_set<char> vars_set;
	// filling map
	for (const auto c : formula) {
		const char var_up = std::toupper(c);
		if (!vars_set.contains(var_up) && 'A' <= var_up && var_up <= 'Z') {
			vars_set.insert(var_up);
			vars.push_back(var_up);
		}
	}

	using std::cout;
	using std::endl;
	const auto results = get_list(formula, vars);
	cout << "| ";
	for (const auto i : vars) cout << i << " | ";
	cout << "= |" << endl << "|";
	for (decltype(vars.size()) i = 0; i <= vars.size(); i++) cout << "---|";
	cout << endl;
	// O(n^2)
	for (const auto& i : results) {
		cout << "|";
		for (const auto j : i) {
			cout << ' ' << j << " |";
		}
		cout << endl;
	}
}
