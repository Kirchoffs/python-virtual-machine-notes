// Visitor mode

#include <iostream>
using namespace std;

class Visitor;

class Animal {
public:
    virtual void accept(Visitor* v) {
        cout << "emmm..." << endl;
    }
};

class Dog: public Animal {
public:
    void accept(Visitor* v);
};

class Cat: public Animal {
public:
    void accept(Visitor* v);
};

class Fox: public Animal {
public:
    void accept(Visitor* v);
};

class Visitor {
public:
    void visit(Animal* animal) {}
    virtual void visit(Dog* animal) {}
    virtual void visit(Cat* animal) {}
    virtual void visit(Fox* animal) {}
};

class Speaker: public Visitor {
public:
    void visit(Animal* pa) {
        pa->accept(this);
    }

    virtual void visit(Dog* pd) {
        cout << "Bark..." << endl;
    }

    virtual void visit(Cat* pt) {
        cout << "Meow..." << endl;
    }

    virtual void visit(Fox* pf) {
        cout << "Owooooo..." << endl;
    }
};

class Feeding: public Visitor {
public:
    void visit(Animal* pa) {
        pa->accept(this);
    }

    virtual void visit(Dog* pd) {
        cout << "Bone..." << endl;
    }

    virtual void visit(Cat* pt) {
        cout << "Fish..." << endl;
    }

    virtual void visit(Fox* pf) {
        cout << "Pork..." << endl;
    }
};

void Dog::accept(Visitor* v) {
    v->visit(this);
}

void Cat::accept(Visitor* v) {
    v->visit(this);
}

void Fox::accept(Visitor* v) {
    v->visit(this);
}

int main() {
    Animal* animals[] = {new Dog(), new Cat(), new Fox()};
    Speaker s;
    for (int i = 0; i < sizeof(animals) / sizeof(Animal*); i++) {
        s.visit(animals[i]);
    }

    Feeding f;
    for (int i = 0; i < sizeof(animals) / sizeof(Animal*); i++) {
        f.visit(animals[i]);
    }

    return 0;
}
