#include "../main.hpp"
#include "../utils/params.hpp"

using std::string;

static auto is_operator(const char c)
{
	return (c == '&' || c == '|');
}

static string move_and_back(const string& s) noexcept
{
	auto r = string();
	for (auto i = 0u; i < s.length(); i++) {
		r.push_back(s[i]);
		if (!is_operator(s[i])) continue;

		const auto ps = get_params(r, r.length() - 1);
		const auto& le = *(ps.left);
		const auto& ri = *(ps.right);


		// ab&c& => abc&&
		if (ps.value.back() == '&' && le.value.back() == '&') {
			const auto a = le.left->value;
			const auto b = le.right->value;
			const auto c = ri.value;
			// removing &c& to insert 'c&&'
			r = r.substr(0, r.length() - c.length() - 2);
			r += c + std::string("&&");
		}
		// abc&| => ab|ac|b&
		else if (ps.value.back() == '|' && ri.value.back() == '&') {
			const auto a = le.value;
			const auto b = ri.left->value;
			const auto c = ri.right->value;
			// removing c&| to insert |ac|b&
			r = r.substr(0, r.length() - c.length() - 2);
			r += "|" + a + c + "|" + b + "&";
		}
		// bc&a| => ab|ac|b&
		else if (ps.value.back() == '|' && le.value.back() == '&') {
			const auto a = le.value;
			const auto b = ri.left->value;
			const auto c = ri.right->value;
			// removing bc&a| to insert ab|ac|b&
			r = r.substr(0, r.length() + a.length()
						 + b.length() + c.length() - 2);
			r += a + b + "|" + a + c + "|" + b + "&";
		}
	}
	return r;
}

static auto is_valid(const string& r) noexcept
{
	bool and_zone = true;
	for (auto i = r.rbegin(); i != r.rend(); i++) {
		if (*i == '&' && !and_zone) return false;
		if (*i == '&' && and_zone) continue;
		if (*i != '&') and_zone = false;
	}
	return true;
}

string conjunctive_normal_form(const string& formula)
{
	auto r = negation_normal_form(formula);
	while (!is_valid(r))
		r = move_and_back(r);
	return r;
}
