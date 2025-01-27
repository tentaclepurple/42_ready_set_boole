#include <string>
#include <map>
#include <vector>
#include <algorithm>
#include <unordered_set>
#include "../ex04/get_list.hpp"

using std::string;
using std::vector;
using std::map;
using std::unordered_set;

bool sat(const string& formula)
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
	// O(2^n)
	try {
		const auto results = get_list(formula, vars);
		for (const auto& i : results)
			if (i.back()) return true;
	} catch (...) {}
	return false;
}
