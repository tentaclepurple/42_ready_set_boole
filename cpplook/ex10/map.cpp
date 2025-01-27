#include <stdint.h>

// gets coordiantes of space filled by z-order curve
// returns index of order of filled cell (mapped to 0 - 1)
double map(uint16_t x, uint16_t y)
{
	uint32_t r = 0;
	// y0,x0,y1,x1,y2,x2,etc...
	for (auto i = 0u; i < sizeof(x) * 8; i++) {
		r |= ((y >> i) & 1) << (i * 2);
		r |= ((x >> i) & 1) << (i * 2 + 1);
	}
	// mapoping 0 - UINT32_MAX to 0 - 1
	return static_cast<double>(r) / static_cast<double>(0xff'ff'ff'ff);
}
