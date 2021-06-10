// Visitor mode

#include <stdio.h>

class Speaker;

class Animal {
public:
    virtual void accept(Speaker* v);
};

class Dog;
class Cat;
class Fox;

class Speaker {
public:
    void visit(Animal* a) {
        a->accept(this);
    }

    void visit(Dog* d) {
        printf("Bark...\n");
    }

    void visit(Cat* c) {
        printf("Meow...\n");
    }

    void visit(Fox* f) {
        printf("Owooooo...\n");
    }
};

void Animal::accept(Speaker* v) {
    // this refers to Animal pointer
    v->visit(this);
}


class Dog: public Animal {
public:
    void accept(Speaker* v) {
        // this refers to Dog pointer
        v->visit(this);
    }
};

// Dog must implement accept method,
// otherwise it will call Animal's accept method.
// In Animal's accept method, "this" refer to animal,
// then Animal's accept(Speaker) will be called,
// then Speaker.visit(Animal) will be called.

// d.accept(s) -> a(d).accept(s)
// s.visit(a) -> a.accept(s)
// infinite recursion

// class Dog: public Animal {
// };

class Cat: public Animal {
public:
    void accept(Speaker* v) {
        v->visit(this);
    }
};


class Fox: public Animal {
public:
    void accept(Speaker* v) {
        v->visit(this);
    }
};

int main() {
    Animal* a = new Dog();
    Animal* b = new Cat();
    Animal* c = new Fox();
    Speaker* s = new Speaker();
    s->visit(a);
    s->visit(b);
    s->visit(c);
}
