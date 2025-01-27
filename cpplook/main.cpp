#include <iostream>
#include <string>
#include "main.hpp"

static void adder_tests()
{
	std::cout << "=== adder tests ===\n";
	uint32_t a, b, r;
	std::string mes;

	a = 3; b = 5;
	r = adder(a, b); mes = (r == a + b ? " OK" : " KO");
	std::cout << a << " + " << b << " = " << r << mes << '\n';
	a = 37; b = 0;
	r = adder(a, b); mes = (r == a + b ? " OK" : " KO");
	std::cout << a << " + " << b << " = " << r << mes << '\n';
	a = 0; b = 0;
	r = adder(a, b); mes = (r == a + b ? " OK" : " KO");
	std::cout << a << " + " << b << " = " << r << mes << '\n';
	a = (3 << 20); b = 269;
	r = adder(a, b); mes = (r == a + b ? " OK" : " KO");
	std::cout << a << " + " << b << " = " << r << mes << '\n';
	a = 0xff; b = 0xff;
	r = adder(a, b); mes = (r == a + b ? " OK" : " KO");
	std::cout << a << " + " << b << " = " << r << mes << '\n';
}

static void multiplier_tests()
{
	std::cout << "=== multiplier tests ===\n";
	uint32_t a, b, r;
	std::string mes;

	a = 3; b = 5;
	r = multiplier(a, b); mes = (r == a * b ? " OK" : " KO");
	std::cout << a << " * " << b << " = " << r << mes << '\n';
	a = 37; b = 0;
	r = multiplier(a, b); mes = (r == a * b ? " OK" : " KO");
	std::cout << a << " * " << b << " = " << r << mes << '\n';
	a = 0; b = 0;
	r = multiplier(a, b); mes = (r == a * b ? " OK" : " KO");
	std::cout << a << " * " << b << " = " << r << mes << '\n';
	a = (3 << 20); b = 269;
	r = multiplier(a, b); mes = (r == a * b ? " OK" : " KO");
	std::cout << a << " * " << b << " = " << r << mes << '\n';
	a = 0xff; b = 0xff;
	r = multiplier(a, b); mes = (r == a * b ? " OK" : " KO");
	std::cout << a << " * " << b << " = " << r << mes << '\n';
}

static void gray_code_tests()
{
	std::cout << "=== gray_code tests ===\n";
	uint32_t n, r, a;
	std::string mes;

	n = 0; a = 0;
	r = gray_code(n); mes = (r == a ? " OK" : " KO");
	std::cout << "gray_code(" << n << ") = " << r << mes << '\n';
	n = 1; a = 1;
	r = gray_code(n); mes = (r == a ? " OK" : " KO");
	std::cout << "gray_code(" << n << ") = " << r << mes << '\n';
	n = 2; a = 3;
	r = gray_code(n); mes = (r == a ? " OK" : " KO");
	std::cout << "gray_code(" << n << ") = " << r << mes << '\n';
	n = 3; a = 2;
	r = gray_code(n); mes = (r == a ? " OK" : " KO");
	std::cout << "gray_code(" << n << ") = " << r << mes << '\n';
	n = 4; a = 6;
	r = gray_code(n); mes = (r == a ? " OK" : " KO");
	std::cout << "gray_code(" << n << ") = " << r << mes << '\n';
	n = 5; a = 7;
	r = gray_code(n); mes = (r == a ? " OK" : " KO");
	std::cout << "gray_code(" << n << ") = " << r << mes << '\n';
	n = 6; a = 5;
	r = gray_code(n); mes = (r == a ? " OK" : " KO");
	std::cout << "gray_code(" << n << ") = " << r << mes << '\n';
	n = 7; a = 4;
	r = gray_code(n); mes = (r == a ? " OK" : " KO");
	std::cout << "gray_code(" << n << ") = " << r << mes << '\n';
	n = 8; a = 12;
	r = gray_code(n); mes = (r == a ? " OK" : " KO");
	std::cout << "gray_code(" << n << ") = " << r << mes << '\n';
}

static void boolean_evaluation_tests()
{
	std::cout << "=== boolean_evaluation tests ===\n";
	std::string s;
	bool r, a;
	std::string mes;

	s = "0!"; a = 1;
	r = eval_formula(s); mes = (r == a ? " OK" : " KO");
	std::cout << "eval_formula(" << s << ") = " << r << mes << '\n';
	s = "10&"; a = 0;
	r = eval_formula(s); mes = (r == a ? " OK" : " KO");
	std::cout << "eval_formula(" << s << ") = " << r << mes << '\n';
	s = "10|"; a = 1;
	r = eval_formula(s); mes = (r == a ? " OK" : " KO");
	std::cout << "eval_formula(" << s << ") = " << r << mes << '\n';
	s = "10&0|"; a = 0;
	r = eval_formula(s); mes = (r == a ? " OK" : " KO");
	std::cout << "eval_formula(" << s << ") = " << r << mes << '\n';
	s = "10|1&"; a = 1;
	r = eval_formula(s); mes = (r == a ? " OK" : " KO");
	std::cout << "eval_formula(" << s << ") = " << r << mes << '\n';
	s = "101|&"; a = 1;
	r = eval_formula(s); mes = (r == a ? " OK" : " KO");
	std::cout << "eval_formula(" << s << ") = " << r << mes << '\n';
	s = "11>"; a = 1;
	r = eval_formula(s); mes = (r == a ? " OK" : " KO");
	std::cout << "eval_formula(" << s << ") = " << r << mes << '\n';
	s = "10="; a = 0;
	r = eval_formula(s); mes = (r == a ? " OK" : " KO");
	std::cout << "eval_formula(" << s << ") = " << r << mes << '\n';
	s = "1011||="; a = 1;
	r = eval_formula(s); mes = (r == a ? " OK" : " KO");
	std::cout << "eval_formula(" << s << ") = " << r << mes << '\n';
	s = "1011^|="; a = 0;
	r = eval_formula(s); mes = (r == a ? " OK" : " KO");
	std::cout << "eval_formula(" << s << ") = " << r << mes << '\n';
	s = "1001^|="; a = 1;
	r = eval_formula(s); mes = (r == a ? " OK" : " KO");
	std::cout << "eval_formula(" << s << ") = " << r << mes << '\n';
	s = "11^"; a = 0;
	r = eval_formula(s); mes = (r == a ? " OK" : " KO");
	std::cout << "eval_formula(" << s << ") = " << r << mes << '\n';
	s = "10^"; a = 1;
	r = eval_formula(s); mes = (r == a ? " OK" : " KO");
	std::cout << "eval_formula(" << s << ") = " << r << mes << '\n';
	try {
		a = 0;
		eval_formula("");
	} catch (const std::runtime_error& e) {
		a = 1;
		std::cout << "" << e.what() << " OK\n";
	}
	try {
		a = 0;
		eval_formula("!");
	} catch (const std::runtime_error& e) {
		a = 1;
		std::cout << "" << e.what() << " OK\n";
	}
	if (!a) std::cout << "KO\n";
	try {
		a = 0;
		eval_formula("11bonour&0");
	} catch (const std::runtime_error& e) {
		a = 1;
		std::cout << "" << e.what() << " OK\n";
	}
	if (!a) std::cout << "KO\n";
	try {
		a = 0;
		eval_formula("110011");
	} catch (const std::runtime_error& e) {
		a = 1;
		std::cout << "" << e.what() << " OK\n";
	}
	if (!a) std::cout << "KO\n";
}

static void print_truth_table_tests()
{
	std::cout << "=== print_truth_table tests ===\n";
	std::string s;

	s = "AB&C|";
	std::cout << s << ":\n";
	print_truth_table(s);
	s = "AB&C|A&";
	std::cout << s << ":\n";
	print_truth_table(s);
	s = "A";
	std::cout << s << ":\n";
	print_truth_table(s);
	s = "at&";
	std::cout << s << ":\n";
	print_truth_table(s);
	s = "a!t&";
	std::cout << s << ":\n";
	print_truth_table(s);
	s = "aa^";
	std::cout << s << ":\n";
	print_truth_table(s);
	s = "aA|";
	std::cout << s << ":\n";
	print_truth_table(s);
	try {
		s = "bonjour";
		std::cout << s << ":\n";
		print_truth_table(s);
	} catch (const std::exception& e) {
		std::cout << e.what() << std::endl;
	}
	try {
		s = "";
		std::cout << s << ":\n";
		print_truth_table(s);
	} catch (const std::exception& e) {
		std::cout << e.what() << std::endl;
	}
}

static void negation_normal_form_tests()
{
	std::cout << "=== negation_normal_form tests ===\n";
	std::string s, r, a, mes;

	s = "AB&!"; a = "A!B!|";
	r = negation_normal_form(s); mes = (r == a ? " OK" : " KO");
	std::cout << "negation_normal_form(" << s << ") = " << r << mes << '\n';
	s = "AB|!"; a = "A!B!&";
	r = negation_normal_form(s); mes = (r == a ? " OK" : " KO");
	std::cout << "negation_normal_form(" << s << ") = " << r << mes << '\n';
	s = "AB>"; a = "A!B|";
	r = negation_normal_form(s); mes = (r == a ? " OK" : " KO");
	std::cout << "negation_normal_form(" << s << ") = " << r << mes << '\n';
	s = "AB="; a = "A!B|B!A|&"; // == AB&A!B!&|
	r = negation_normal_form(s); mes = (r == a ? " OK" : " KO");
	std::cout << "negation_normal_form(" << s << ") = " << r << mes << '\n';
	s = "AB|C&!"; a = "A!B!&C!|";
	r = negation_normal_form(s); mes = (r == a ? " OK" : " KO");
	std::cout << "negation_normal_form(" << s << ") = " << r << mes << '\n';
	s = "AB^"; a = "AB!&BA!&|";
	r = negation_normal_form(s); mes = (r == a ? " OK" : " KO");
	std::cout << "negation_normal_form(" << s << ") = " << r << mes << '\n';
	s = "AB^AB^|"; a = "AB!&BA!&|AB!&BA!&||"; // == AB!&BA!&|
	r = negation_normal_form(s); mes = (r == a ? " OK" : " KO");
	std::cout << "negation_normal_form(" << s << ") = " << r << mes << '\n';
}

// conjunctive normal for does not require '|' to be at the end
static void conjunctive_normal_form_tests()
{
	std::cout << "=== conjunctive_normal_form tests ===\n";
	std::string s, r, a, mes;

	s = "AB&!"; a = "A!B!|";
	r = conjunctive_normal_form(s); mes = (r == a ? " OK" : " KO");
	std::cout << "conjunctive_normal_form(" << s << ") = " << r << mes << '\n';
	s = "AB|!"; a = "A!B!&";
	r = conjunctive_normal_form(s); mes = (r == a ? " OK" : " KO");
	std::cout << "conjunctive_normal_form(" << s << ") = " << r << mes << '\n';
	s = "AB|C&"; a = "AB|C&";
	r = conjunctive_normal_form(s); mes = (r == a ? " OK" : " KO");
	std::cout << "conjunctive_normal_form(" << s << ") = " << r << mes << '\n';
	s = "AB|C|D|"; a = "AB|C|D|"; // == ABCD|||
	r = conjunctive_normal_form(s); mes = (r == a ? " OK" : " KO");
	std::cout << "conjunctive_normal_form(" << s << ") = " << r << mes << '\n';
	s = "AB&C&D&"; a = "ABCD&&&";
	r = conjunctive_normal_form(s); mes = (r == a ? " OK" : " KO");
	std::cout << "conjunctive_normal_form(" << s << ") = " << r << mes << '\n';
	s = "AB&!C!|"; a = "A!B!|C!|"; // == A!B!C!||
	r = conjunctive_normal_form(s); mes = (r == a ? " OK" : " KO");
	std::cout << "conjunctive_normal_form(" << s << ") = " << r << mes << '\n';
	s = "AB|!C!&"; a = "A!B!C!&&";
	r = conjunctive_normal_form(s); mes = (r == a ? " OK" : " KO");
	std::cout << "conjunctive_normal_form(" << s << ") = " << r << mes << '\n';
}

static void sat_tests()
{
	std::cout << "=== sat tests ===\n";
	std::string s, mes;
	bool a, r;

	s = "AB|"; a = true;
	r = sat(s); mes = (r == a ? " OK" : " KO");
	std::cout << "sat(" << s << ") = " << r << mes << '\n';
	s = "AB&"; a = true;
	r = sat(s); mes = (r == a ? " OK" : " KO");
	std::cout << "sat(" << s << ") = " << r << mes << '\n';
	s = "AA!&"; a = false;
	r = sat(s); mes = (r == a ? " OK" : " KO");
	std::cout << "sat(" << s << ") = " << r << mes << '\n';
	s = "AA^"; a = false;
	r = sat(s); mes = (r == a ? " OK" : " KO");
	std::cout << "sat(" << s << ") = " << r << mes << '\n';
	s = ""; a = false;
	r = sat(s); mes = (r == a ? " OK" : " KO");
	std::cout << "sat(" << s << ") = " << r << mes << '\n';
	s = "bonour"; a = false;
	r = sat(s); mes = (r == a ? " OK" : " KO");
	std::cout << "sat(" << s << ") = " << r << mes << '\n';
}

static void powerset_tests()
{
	std::cout << "=== powerset tests ===\n";
	using std::vector;
	vector<vector<int32_t>> a, r;
	vector<int32_t> s;
	std::string mes;

	s = {1, 2, 3};
	r = powerset(s);
	std::cout << "{1, 2, 3}: \n";
	for (const auto& i : r) {
		for (const auto j : i) {
			std::cout << j << ' ';
		}
		std::cout << std::endl;
	}
	s = {6, 4};
	r = powerset(s);
	std::cout << "{6, 4}: \n";
	for (const auto& i : r) {
		for (const auto j : i) {
			std::cout << j << ' ';
		}
		std::cout << std::endl;
	}
	s = {9};
	r = powerset(s);
	std::cout << "{9}: \n";
	for (const auto& i : r) {
		for (const auto j : i) {
			std::cout << j << ' ';
		}
		std::cout << std::endl;
	}
	s = {};
	r = powerset(s);
	std::cout << "{}: \n";
	for (const auto& i : r) {
		for (const auto j : i) {
			std::cout << j << ' ';
		}
		std::cout << std::endl;
	}
}

static void set_evaluation_tests()
{
	std::cout << "=== set_evaluation tests ===\n";
	std::string s;
	std::vector<int32_t> r, a;
	std::vector<std::vector<int32_t>> sets;

	auto print_sets = [](const auto& sets) {
		std::cout << ">>> {";
		for (const auto& i : sets) {
			std::cout << '{';
			for (const auto& j : i)
				std::cout << j << ',';
			std::cout << "},";
		}
		std::cout << "}\n";
	};

	s = "ab&"; sets = {{0, 1, 2}, {0, 3, 4}};
	r = set_eval_formula(s, sets);
	print_sets(sets);
	std::cout << "set_eval_formula(" << s << ") = " << '\n';
	for (const auto i : r) {
		std::cout << i << ' ';
	}
	std::cout << std::endl;
	s = "ab|"; sets = {{0, 1, 2}, {3, 4, 5}};
	r = set_eval_formula(s, sets);
	print_sets(sets);
	std::cout << "set_eval_formula(" << s << ") = " << '\n';
	for (const auto i : r) {
		std::cout << i << ' ';
	}
	std::cout << std::endl;
	s = "a!"; sets = {{0, 1, 2}};
	r = set_eval_formula(s, sets);
	print_sets(sets);
	std::cout << "set_eval_formula(" << s << ") = " << '\n';
	for (const auto i : r) {
		std::cout << i << ' ';
	}
	std::cout << std::endl;
	//(1 2 3 4 7)
	s = "a!b^c>"; sets = {{0, 1, 2}, {7, 4, 0}, {1, 2, 3}};
	r = set_eval_formula(s, sets);
	print_sets(sets);
	std::cout << "set_eval_formula(" << s << ") = " << '\n';
	for (const auto i : r) {
		std::cout << i << ' ';
	}
	std::cout << std::endl;
}

static void map_tests()
{
	std::cout << "=== map tests ===\n";
	std::string mes;
	std::uint16_t x, y;
	double r, a;

	x = 0; y = 0; a = 0. / 0xff'ff'ff'ff;
	r = ::map(x, y); mes = (r == a ? " OK" : " KO");
	std::cout << "map(" << x << ", " << y << ") = " << r << " " << mes << '\n';
	x = 0; y = 1; a = 1. / 0xff'ff'ff'ff;
	r = ::map(x, y); mes = (r == a ? " OK" : " KO");
	std::cout << "map(" << x << ", " << y << ") = " << r << " " << mes << '\n';
	x = 1; y = 0; a = 2. / 0xff'ff'ff'ff;
	r = ::map(x, y); mes = (r == a ? " OK" : " KO");
	std::cout << "map(" << x << ", " << y << ") = " << r << " " << mes << '\n';
	x = 1; y = 1; a = 3. / 0xff'ff'ff'ff;;
	r = ::map(x, y); mes = (r == a ? " OK" : " KO");
	std::cout << "map(" << x << ", " << y << ") = " << r << " " << mes << '\n';
	x = 3; y = 3; a = 15. / 0xff'ff'ff'ff;;
	r = ::map(x, y); mes = (r == a ? " OK" : " KO");
	std::cout << "map(" << x << ", " << y << ") = " << r << " " << mes << '\n';
	x = 0xffff; y = 0xffff; a = 0xff'ff'ff'ff / 0xff'ff'ff'ff;;
	r = ::map(x, y); mes = (r == a ? " OK" : " KO");
	std::cout << "map(" << x << ", " << y << ") = " << r << " " << mes << '\n';
	x = 0; y = 4; a = 16. / 0xff'ff'ff'ff;;
	r = ::map(x, y); mes = (r == a ? " OK" : " KO");
	std::cout << "map(" << x << ", " << y << ") = " << r << " " << mes << '\n';
}


static void reverse_map_tests()
{
	using std::uint16_t;

	std::cout << "=== reverse_map tests ===\n";
	std::string mes;
	std::uint16_t x, y;
	std::pair<uint16_t, uint16_t> r;

	x = 0; y = 0;
	r = reverse_map(::map(x, y)); mes = (r == decltype(r)({x, y}) ? " OK" : " KO");
	std::cout << "reverse_map(map(" << x << ", " << y << ")) = {" << r.first << ", " << r.second <<  "} " << mes << '\n';
	x = 1; y = 1;
	r = reverse_map(::map(x, y)); mes = (r == decltype(r)({x, y}) ? " OK" : " KO");
	std::cout << "reverse_map(map(" << x << ", " << y << ")) = {" << r.first << ", " << r.second <<  "} " << mes << '\n';
	x = 4; y = 3;
	r = reverse_map(::map(x, y)); mes = (r == decltype(r)({x, y}) ? " OK" : " KO");
	std::cout << "reverse_map(map(" << x << ", " << y << ")) = {" << r.first << ", " << r.second <<  "} " << mes << '\n';
	x = 23; y = 107;
	r = reverse_map(::map(x, y)); mes = (r == decltype(r)({x, y}) ? " OK" : " KO");
	std::cout << "reverse_map(map(" << x << ", " << y << ")) = {" << r.first << ", " << r.second <<  "} " << mes << '\n';
	x = -1; y = -1;
	r = reverse_map(::map(x, y)); mes = (r == decltype(r)({x, y}) ? " OK" : " KO");
	std::cout << "reverse_map(map(" << x << ", " << y << ")) = {" << r.first << ", " << r.second <<  "} " << mes << '\n';
	x = 0xffff; y = 0xff;
	r = reverse_map(::map(x, y)); mes = (r == decltype(r)({x, y}) ? " OK" : " KO");
	std::cout << "reverse_map(map(" << x << ", " << y << ")) = {" << r.first << ", " << r.second <<  "} " << mes << '\n';
	// test for otherway around
	x = 0xffff; y = 0xff;
	r = reverse_map(::map(reverse_map(::map(x, y)))); mes = (r == decltype(r)({x, y}) ? " OK" : " KO");
	std::cout << "reverse_map(map(reverse_map(map(" << x << ", " << y << ")))) = {" << r.first << ", " << r.second <<  "} " << mes << '\n';
}

int main()
{
	adder_tests();
	multiplier_tests();
	gray_code_tests();
	boolean_evaluation_tests();
	print_truth_table_tests();
	negation_normal_form_tests();
	conjunctive_normal_form_tests();
	sat_tests();
	powerset_tests();
	set_evaluation_tests();
	map_tests();
	reverse_map_tests();
}
