#include <stdio.h>

class Animal {
public:
    // Add virtual modifier
    virtual void speak()
    {
        printf("emm... \n");
    }
};

class Cat : public Animal {
public:
    void speak()
    {
        printf("Meow...\n");
    }
};

class Dog : public Animal {
public:
    void speak()
    {
        printf("Bark...\n");
    }
};

class Fox : public Animal {
public:
    void speak()
    {
        printf("Owooooo...\n");
    }
};

class Speaker {
public:
    void speak(Animal *obj)
    {
        obj->speak();
    }
};

int main() {
    Animal *a = new Dog();
    Animal *b = new Cat();
    Animal *c = new Fox();
    Speaker *s = new Speaker();
    s->speak(a);
    s->speak(b);
    s->speak(c);
}
