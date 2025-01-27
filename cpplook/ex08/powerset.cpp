#include <vector>
#include <cmath>
#include <cstdint>

using std::vector;

// 0(e)
static auto mypow(const auto b, unsigned e)
{
	auto r = 1;
	while (e--)
		r *= b;
	return r;
}

// 0(1)
static auto bits_to_index(auto bits)
{
	unsigned max = sizeof(bits) * 8;
	vector<unsigned> r;
	for (auto i = 0u; i < max; i++)
		if (bits & (1 << i)) r.push_back(i);
	return r;
}

// 0(2^n)
using ret_type = vector<vector<int32_t>>;
ret_type powerset(const vector<int32_t>& set)
{
	auto n = mypow(2, set.size());
	ret_type r;
	while (--n + 1) {
		const auto indexes = bits_to_index(n);
		r.push_back(vector<int32_t>());
		// can't go over sizeof(n) * 8 -> O(1)
		for (const auto i : indexes)
			r.back().push_back(set[i]);
	}
	return r;
}
