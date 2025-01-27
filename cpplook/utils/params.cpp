#include <algorithm>
#include "params.hpp"

std::ostream& operator<<(std::ostream& os, const Params& p) noexcept {
	os << "l: " << p.left->value << " r: " << p.right->value << "\nv: " << p.value << '\n';
	return os;
}
Params get_params(const std::string& s, const int i) noexcept
{
	Params r;
	r.left = std::make_unique<Params>();
	r.right = std::make_unique<Params>();
	switch (s[i]) {
		case '!':
			r.left->value = s.substr(i - 1, 1);
			r.value = r.left->value + "!";
			return r;
		case '&':
			r.right = std::make_unique<Params>(get_params(s, i - 1));
			r.left = std::make_unique<Params>(get_params(
				s, i - 1 - r.right->value.length()));
			r.value = r.left->value + r.right->value + "&";
			return r;
		case '|':
			r.right = std::make_unique<Params>(get_params(s, i - 1));
			r.left = std::make_unique<Params>(get_params(
				s, i - 1 - r.right->value.length()));
			r.value = r.left->value + r.right->value + "|";
			return r;
		case '>':
			r.right = std::make_unique<Params>(get_params(s, i - 1));
			r.left = std::make_unique<Params>(get_params(
				s, i - 1 - r.right->value.length()));
			r.value = r.left->value + r.right->value + ">";
			return r;
		case '=':
			r.right = std::make_unique<Params>(get_params(s, i - 1));
			r.left = std::make_unique<Params>(get_params(
				s, i - 1 - r.right->value.length()));
			r.value = r.left->value + r.right->value + "=";
			return r;
		case '^':
			r.right = std::make_unique<Params>(get_params(s, i - 1));
			r.left = std::make_unique<Params>(get_params(
				s, i - 1 - r.right->value.length()));
			r.value = r.left->value + r.right->value + "^";
			return r;
		default:
			r.value = s.substr(i, 1);
			return r;
	}
}
