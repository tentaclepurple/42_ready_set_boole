#include <string>
#include <utility>
#include <optional>
#include <vector>
#include <iostream>
#include "../utils/params.hpp"

using std::string;
using std::vector;
using std::pair;

// (¬¬A) ⇔ A
static string rm_double_negations(const string& s) noexcept
{
	string r;
	auto should_pass = false;
	for (decltype(s.length()) i = 0; i < s.length(); i++) {
		if (should_pass) {
			should_pass = false;
			continue;
		}
		if (s[i] != '!') {
			r.push_back(s[i]);
			continue;
		}
		if (i + 1 == s.length() || s[i + 1] != '!') {
			r.push_back(s[i]);
			continue;
		}
		should_pass = true;
	}
	return r;
}

// (A ⇒ B) ⇔ (¬A ∨ B)
static string rm_material_conditions(const string& s) noexcept
{
	auto r = string();
	for (auto i = 0u; i < s.length(); i++) {
		if (s[i] != '>') {
			r.push_back(s[i]);
			continue;
		}
		const auto ps = get_params(r + ">", r.length());
		const auto a = ps.left->value;
		const auto b = ps.right->value;
		// removing b to insert '!'
		r = r.substr(0, r.length() - b.length());
		// a!b|
		r += "!" + b + "|";
	}
	return r;
}

// (A ⇔ B) ⇔ ((A ⇒ B) ∧ (B ⇒ A))
static string rm_equivalence(const string& s) noexcept
{
	auto r = string();
	for (auto i = 0u; i < s.length(); i++) {
		if (s[i] != '=') {
			r.push_back(s[i]);
			continue;
		}
		const auto ps = get_params(r + "=", r.length());
		const auto a = ps.left->value;
		const auto b = ps.right->value;
		// ab>ba>& but first ab is already written
		r += ">" + b + a + ">&";
	}
	return r;
}

// (A ^ B) ⇔ !(A ⇔ B)
static string rm_xor(const string& s) noexcept
{
	auto r = string();
	for (auto i = 0u; i < s.length(); i++) {
		if (s[i] != '^') {
			r.push_back(s[i]);
			continue;
		}
		const auto ps = get_params(r + "^", r.length());
		const auto a = ps.left->value;
		const auto b = ps.right->value;
		// ab>ba>& but first ab is already written
		r += "!&" + b + a + "!&|";
	}
	return r;
}

static string apply_morgan(const string& s) noexcept
{
	auto r = string();
	auto should_skip = false;
	for (auto i = 0u; i < s.length(); i++) {
		if (should_skip) {
			should_skip = false;
			continue;
		}
		if (i == s.length() - 1 ||
			!((s[i + 1] == '!') && (s[i] == '&' || s[i] == '|')))
		{
			r.push_back(s[i]);
			continue;
		}
		const auto ps = get_params(r + "&", r.length());
		const auto a = ps.left->value;
		const auto b = ps.right->value;
		// removing b to insert '!'
		r = r.substr(0, r.length() - b.length());
		// ab&! -> a!b!|
		// ab|! -> a!b!&
		r += "!" + b + "!" + ((s[i] == '|') ? "&" : "|");
		should_skip = true;
	}
	return r;
}

static bool is_valid(const string& s) noexcept
{
	if (s.find("!!") != s.npos) return false;
	if (s.find("&!") != s.npos) return false;
	if (s.find("|!") != s.npos) return false;
	if (s.find("=") != s.npos) return false;
	if (s.find("^") != s.npos) return false;
	if (s.find(">") != s.npos) return false;
	return true;
}

string negation_normal_form(const string& formula) noexcept
{
	std::string s = formula;
	do {
		s = rm_xor(s);
		s = rm_equivalence(s);
		s = rm_material_conditions(s);
		s = apply_morgan(s);
		s = rm_double_negations(s);
	}
	while (!is_valid(s));
	return s;
}
