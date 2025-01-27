SOURCES := $(shell find . -name "*.cpp")
OBJECTS := $(patsubst %.cpp,%.o,$(SOURCES))
DEPENDS := $(patsubst %.cpp,%.d,$(SOURCES))
NAME := ready-set-boole
CXX := g++
# To add more warnings + make errors shorter + add debug info
#CXXFLAGS := -Wall -Wextra -Wfatal-errors -ggdb -std=c++20 # debug small errors
CXXFLAGS := -Wall -Wextra -ggdb -O0 -std=c++20 # debug full error
#CXXFLAGS := -Ofast -std=c++20 # release w optimizations

# execute these rules even if files of those names exist.
.PHONY: all clean fclean run

# Default rule
all: $(NAME)

# Compile + run
run: all
	./$(NAME)

fclean: clean
	$(RM) $(NAME)

clean:
	$(RM) $(OBJECTS) $(DEPENDS)

# Linking the executable from the object files
$(NAME): $(OBJECTS)
	$(CXX) $(CXXFLAGS) $^ -o $@

# Start reading dependency files (.d files here)
-include $(DEPENDS)

%.o: %.cpp Makefile
	$(CXX) $(CXXFLAGS) -MMD -MP -c $< -o $@
