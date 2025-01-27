#include "get_list.hpp"

bool eval_formula(const string& r);

// O(formula.size()) == O(n)
static string resolve_vars(const string& formula,
						   const vector<char>& vars,
						   const vector<bool>& r) noexcept
{
	auto res = string();
	for (const auto c : formula) {
		const auto it = std::find(vars.begin(), vars.end(), std::toupper(c));
		if (it != vars.end())
			res += std::to_string(r[std::distance(vars.begin(), it)]);
		else
			res.push_back(c);
	}
	return res;
}

// O(2^vars.size())
vector<vector<bool>> get_list(const string& formula, const vector<char>& vars,
					 vector<bool> r,
					 vector<vector<bool>> ret)
{
	if (r.size() == vars.size()) {
		r.emplace_back(eval_formula(resolve_vars(formula, vars, r)));
		ret.emplace_back(r);
		return ret;
	}
	r.emplace_back(false);
	ret = get_list(formula, vars, r, ret);
	r.pop_back();
	r.emplace_back(true);
	ret = get_list(formula, vars, r, ret);
	return ret;
}
