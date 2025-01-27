#include "../main.hpp"

uint32_t gray_code(uint32_t n) noexcept
{
	if (!n) return 0;
	decltype(n) res = 0;
	unsigned i = 31;
	// skipping zeroes
	while (!(n & (1 << i)))
		   i--;
	res |= (1 << i); // first bit assignment
	while (i) {
		// set to true if n's prev bit is different than curerent
		if (bool(n & (1 << i)) != bool(n & (1 << (i-1))))
			res |= (1 << (i-1));
		i--;
	}
	return res;
}
