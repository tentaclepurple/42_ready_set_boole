#ifndef PARAMS_H_
#define PARAMS_H_

#include <string>
#include <iostream>
#include <memory>

struct Params {
	std::unique_ptr<Params> left = nullptr;
	std::unique_ptr<Params> right = nullptr;
	std::string value = "";
	friend std::ostream& operator<<(std::ostream& os, const Params& p) noexcept;
};
std::ostream& operator<<(std::ostream& os, const Params& p) noexcept;
Params get_params(const std::string& s, const int i) noexcept;


#endif // PARAMS_H_
