#include <cstdint>
#include <iostream>

static constexpr unsigned get_count(bool ba, bool bb, bool prev) noexcept
{
	if (ba & bb & prev)
		return 3;
	if ((ba & bb) | (ba & prev) | (bb & prev))
		return 2;
	if (ba | bb | prev)
		return 1;
	return 0;
}

uint32_t adder(uint32_t a, uint32_t b) noexcept
{
	bool prev = false;
	uint32_t res = 0;
	for (auto i = 0u; i < 32; i++) {
		const bool ba = a & (1 << i);
		const bool bb = b & (1 << i);
		const unsigned count = get_count(ba, bb, prev);
		prev = false;
		switch (count) {
			case 1:
				res = res | (1 << i);
				break;
			case 2:
				prev = true;
				break;
			case 3:
				res = res | (1 << i);
				prev = true;
				break;
		}
	}
	return res;
}
