#include <stdio.h>
#include "util/arrayList.hpp"

template<typename T>
ArrayList<T>::ArrayList(int n) {
    _length = n;
    _size = 0;
    _array = new T[n];
}

template<typename T>
void ArrayList<T>::add(T t) {
    if (_size >= _length) {
        expand();
    }

    _array[_size++] = t;
}

template<typename T>
void ArrayList<T>::insert(int index, T t) {
    add(NULL);
    for (int i = _size; i > index; i--) {
        _array[i] = _array[i-1];
    }

    _array[index] = t;
}

template<typename T>
void ArrayList<T>::expand() {
    T* new_array = new T[_length] << 1];

    for (int i = 0; i < _length; i++) {
        new_array[i] = _array[i];
    }

    delete[] _array;
    _array = new_array;
    _length <<= 1;
    printf("Expand an array to %d, size is %d\n", _length, _size);
}

