#include <iostream>
#include <string.h>
#include <stdlib.h>
#include <vector>
#include <algorithm>

using namespace std;


class Strategy
{
public:
    virtual ~Strategy() {}
    virtual string DoAlgorithm(const std::vector<std::string>& data) const = 0;
};



class Context
{
   
private:
    Strategy* strategy_;
    
public:
    Context(Strategy* strategy = nullptr) : strategy_(strategy)
    {
    }
    ~Context()
    {
        delete this->strategy_;
    }
    
    void set_strategy(Strategy* strategy)
    {
        delete this->strategy_;
        this->strategy_ = strategy;
    }
    
    void DoSomeBusinessLogic() const
    {
        
        std::string result = this->strategy_->DoAlgorithm(std::vector<std::string>{"a", "e", "c", "b", "d"});
        std::cout << result << "\n";
    }
};


class ConcreteStrategyA : public Strategy
{
public:
    string DoAlgorithm(const std::vector<std::string>& data) const override
    {
        string result;
        for_each(begin(data), end(data), [&result](const string& letter) {
            result += letter;
        });
        sort(begin(result), std::end(result));

        return result;
    }
};
class ConcreteStrategyB : public Strategy
{
    string DoAlgorithm(const vector<string>& data) const override
    {
        string result;
        for_each(begin(data), end(data), [&result](const string& letter) {
            result += letter;
            });
        sort(begin(result), end(result));
        for (int i = 0; i < result.size() / 2; i++)
        {
            swap(result[i], result[result.size() - i - 1]);
        }

        return result;
    }
};

void ClientCode()
{
    std::cout << "Реализация паттерна стратегии\n\n";
    Context* context = new Context(new ConcreteStrategyA);
    cout << "Результат в контексте 1(нормальная сортировка)\n";
    context->DoSomeBusinessLogic();
    cout << "\n";
    cout << "Результат в контексте 2(реверсивная сортировка)\n";
    context->set_strategy(new ConcreteStrategyB);
    context->DoSomeBusinessLogic();
    delete context;
}

int main()
{
    ClientCode();
    return 0;
}