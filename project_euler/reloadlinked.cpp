#include <iostream>
using namespace std;
class LinkedList
{    
    struct Node
    {
        int x;
        Node *next;

     };
    private:
    Node *head;

    
    public:
    LinkedList();
    {
        head = NULL;
    }
     
    void prepend(int data)
    {
        Node *k = new Node();
        k->x = data;
        k->next = head;
        head = k;
    }

/*    void insert(int data)
    {
        Node *n = head;
        int ntx = ntx->x;
        head = head->ntx;
        return nxt;
    }
        
  */  

};
int main()
{
    LinkedList list;
    list.prepend(2);
    list.prepend(3);
    list.prepend(4);


    cout << list.insert(2) << endl;
    cout << list.insert(3) << endl;
    cout << list.insert(4) << endl;

  return 0;

}

  
