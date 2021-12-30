CC = g++
CFLAGS = -Wall -std=c++17
SHELL = /bin/bash
TARGET = hello
LIBS =

SOURCES = $(shell find -type f -name '*.cc' | sort)

OBJS = $(shell find -type f -name '*.cc' | sort | sed -e 's/.cc/.o/g' -e 's/src\//obj\//g')

all: debug

debug: CFLAGS += -g
debug: $(TARGET)

release: CFLAGS += -O2 -DNDEBUG -fPIC
release: $(TARGET)

profile: CFLAGS += -g -pg -O2 -DNDEBUG -fPIC -fno-omit-frame-pointer -fno-inline-functions -fno-inline-functions-called-once -fno-optimize-sibling-calls
profile: $(TARGET)

depend: _depend

_depend: $(SOURCES)
	rm -f ./.depend
	$(CC) $(CFLAGS) $(INCLUDE) -MM $^ > ./.depend;

-include .depend

$(TARGET): $(OBJS)
	$(CC) $(CFLAGS) $(OBJS) $(LIBS) -o $(TARGET)

obj/%.o: src/%.cc
	@mkdir -m 755 -p $$(dirname $@)
	$(CC) -c $(CFLAGS) $(INCLUDE) $< -o $@

clean:
	@rm -f .depend
	@rm -rf ./*.o
	@rm -rf ./*.list
	@rm -f $(TARGET)
