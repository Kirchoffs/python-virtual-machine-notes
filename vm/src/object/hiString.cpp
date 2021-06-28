#include <string.h>
#include "object/hiString.hpp"

HiString::HiString(const char* s) {
    _length = strlen(s);
    _value = new char[_length];
    strcpy(_value, s);
}

HiString::HiString(const char* x, const int length) {
    _length = length;
    _value = new char[length];

    for (int i = 0; i < length; i++) {
        _value[i] = x[i];
    }
}