#ifndef MAIN_H_
#define MAIN_H_

#include <cstdint>
#include <string>
#include <vector>
#include <set>
#include <utility>

uint32_t adder(uint32_t a, uint32_t b) noexcept;
uint32_t multiplier(uint32_t a, uint32_t b) noexcept;
uint32_t gray_code(uint32_t n) noexcept;
bool eval_formula(const std::string& str);
void print_truth_table(const std::string& formula);
std::string negation_normal_form(const std::string& formula);
std::string conjunctive_normal_form(const std::string& formula);
bool sat(const std::string& formula);
std::vector<std::vector<int32_t>> powerset(const std::vector<int32_t>& set);
std::vector<int32_t> set_eval_formula(const std::string& str,
							   const std::vector<std::vector<int32_t>>& sets);
double map(uint16_t x, uint16_t y);
inline double map(const std::pair<uint16_t, uint16_t>& p) { // for tests
	return map(p.first, p.second);
};
std::pair<uint16_t, uint16_t> reverse_map(double n);

#endif // MAIN_H_
