#ifndef HI_INTEGER_HPP
#define HI_INTEGER_HPP

#include "object/hiObject.hpp"

class HiInteger: public HiObject {
private:
    int _value;

public:
    HiInteger(int x);
    int value() {
        return _value;
    }
};

#endif