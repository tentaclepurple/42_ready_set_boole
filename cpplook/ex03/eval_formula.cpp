#include "../main.hpp"
#include <string>
#include <stack>
#include <unordered_map>
#include <functional>
#include <utility>
#include <stdexcept>
#include <string>

// O(1)
static bool ctob(char c)
{
	if (c != '0' && c!= '1')
		throw std::runtime_error(
			std::string("Invalid boolean character: '") + c + "'");
	return c == '1';
}

// O(1)
static auto get_funcs() noexcept
{
	const auto btoc = [](bool b) { return b ? '1' : '0'; };
	std::unordered_map<char, std::function<char(bool, bool)>> s, d;
	s['!'] = [&btoc](bool a, bool) {
		return btoc(!a);
	};
	d['&'] = [&btoc](bool a, bool b) {
		return btoc(a & b);
	};
	d['|'] = [&btoc](bool a, bool b) {
		return btoc(a | b);
	};
	d['^'] = [&btoc](bool a, bool b) {
		return btoc(a ^ b);
	};
	d['>'] = [&btoc](bool a, bool b) {
		return btoc((!a) | b);
	};
	d['='] = [&btoc](bool a, bool b) {
		return btoc(a == b);
	};
	return std::pair<decltype(s), decltype(d)>(s, d);
}

// O(n)
bool eval_formula(const std::string& str)
{
	static const auto funcs = get_funcs();
	const auto one_params = funcs.first;
	const auto two_params = funcs.second;
	auto res = std::string();
	for (const char c : str) {
		if (c == '0' || c == '1') {
			res.push_back(c);
			continue;
		}
		auto it = one_params.find(c);
		auto is_one = true;
		if (it == one_params.end()) {
			it = two_params.find(c);
			is_one = false;
		}
		if (it == two_params.end())
			throw std::runtime_error(
				std::string("Invalid character '") + c + "'");
		if (is_one) {
			if (res.empty()) throw std::runtime_error("Invalid RPN string");
			const auto a = ctob(res[res.length() - 1]);
			res.pop_back();
			res.push_back((it->second)(a, a));
			continue;
		}
		if (res.empty()) throw std::runtime_error("Invalid RPN string");
		const auto b = ctob(res[res.length() - 1]);
		res.pop_back();
		if (res.empty()) throw std::runtime_error("Invalid RPN string");
		const auto a = ctob(res[res.length() - 1]);
		res.pop_back();
		res.push_back((it->second)(a, b));
	}
	if (res.length() == 0) throw std::runtime_error("Empty RPN string");
	if (res.length() != 1) throw std::runtime_error("Invalid RPN string");
	return res[0] == '1';
}
