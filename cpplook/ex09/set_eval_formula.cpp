#include "../main.hpp"
#include <string>
#include <set>
#include <unordered_map>
#include <functional>
#include <utility>
#include <stdexcept>
#include <string>
#include <algorithm>

using set_t = std::vector<int32_t>;

static set_t set_xor(const set_t& a, const set_t& b)
{
	set_t r;
	for (auto i : b)
		if (std::find(a.begin(), a.end(), i) == a.end())
			r.emplace_back(i);
	for (auto i : a)
		if (std::find(b.begin(), b.end(), i) == b.end())
			r.emplace_back(i);
	return r;
}
static set_t set_not(const set_t& a, const set_t& global_set)
{
	set_t r;
	for (auto i : global_set)
		if (std::find(a.begin(), a.end(), i) == a.end())
			r.emplace_back(i);
	return r;
}
static set_t set_or(const set_t& a, const set_t& b)
{
	set_t r;
	for (auto i : a)
		r.emplace_back(i);
	for (auto i : b)
		if (std::find(r.begin(), r.end(), i) == r.end())
			r.emplace_back(i);
	return r;
}
static set_t set_and(const set_t& a, const set_t& b)
{
	set_t r;
	for (auto i : a)
		if (std::find(b.begin(), b.end(), i) != b.end())
			r.emplace_back(i);
	return r;
}
static set_t set_mat_cond(const set_t& a, const set_t& b,
						  const set_t& global_set)
{
	return set_or(set_not(a, global_set), b);
}

static auto get_funcs() noexcept
{
	std::unordered_map<char, std::function<set_t(set_t, set_t, set_t)>> s, d;
	s['!'] = [](set_t a, set_t global_set, set_t) {
		return set_not(a, global_set);
	};
	d['&'] = [](set_t a, set_t b, set_t) {
		return set_and(a, b);
	};
	d['|'] = [](set_t a, set_t b, set_t) {
		return set_or(a, b);
	};
	d['^'] = [](set_t a, set_t b, set_t) {
		return set_xor(a, b);
	};
	d['>'] = [](set_t a, set_t b, set_t global_set) {
		return set_mat_cond(a, b, global_set);
	};
	// removed '=' as it makes no sense for a functino returning a set...
	return std::pair<decltype(s), decltype(d)>(s, d);
}

// renamed it to set_eval_formula to avoid name clashing
set_t set_eval_formula(const std::string& str,
				  const std::vector<set_t>& sets)
{
	static const auto funcs = get_funcs();
	const auto one_params = funcs.first;
	const auto two_params = funcs.second;
	std::vector<set_t> res;
	const auto global_set = [](const auto& sets) {
		set_t r;
		for (const auto& i : sets) r = set_or(r, i);
		return r;
	}(sets);

	for (const char c : str) {
		if (std::isalpha(c)) {
			res.push_back(sets[std::toupper(c) - 'A']);
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
			const auto a = res[res.size() - 1];
			res.pop_back();
			res.push_back((it->second)(a, global_set, a));
			continue;
		}
		if (res.empty()) throw std::runtime_error("Invalid RPN string");
		const auto b = res[res.size() - 1];
		res.pop_back();
		if (res.empty()) throw std::runtime_error("Invalid RPN string");
		const auto a = res[res.size() - 1];
		res.pop_back();
		res.push_back((it->second)(a, b, global_set));
	}
	if (res.size() == 0) throw std::runtime_error("Empty RPN string");
	if (res.size() != 1) throw std::runtime_error("Invalid RPN string");
	return res[0];
}
