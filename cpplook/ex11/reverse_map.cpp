#include <stdint.h>
#include <utility>
#include <iostream>

// just does the opposite of map
std::pair<uint16_t, uint16_t> reverse_map(double n)
{
	uint32_t r = static_cast<double>(n) * 0xff'ff'ff'ff;
	uint16_t x = 0, y = 0;
	for (auto i = 0u; i < sizeof(x) * 8; i++) {
		y |= ((r >> (i * 2)) & 1) << i;
		x |= ((r >> (i * 2 + 1)) & 1) << i;
	}
	return {x, y};
}
