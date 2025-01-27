#ifndef GET_LIST_H_
#define GET_LIST_H_

#include <string>
#include <map>
#include <vector>
#include <algorithm>
#include <unordered_set>

using std::string;
using std::vector;
using std::map;
using std::unordered_set;

vector<vector<bool>> get_list(const string& formula, const vector<char>& vars,
					 vector<bool> r = vector<bool>(),
					vector<vector<bool>> ret = vector<vector<bool>>());

#endif // GET_LIST_H_
