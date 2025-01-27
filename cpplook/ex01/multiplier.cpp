#include "../main.hpp"

uint32_t multiplier(uint32_t a, uint32_t b) noexcept
{
	decltype(b) res = 0;
	for (auto i = 0u; i < 32; i++)
		if (a & (1 << i))
			res = adder(res, b << i);
	return res;
}
