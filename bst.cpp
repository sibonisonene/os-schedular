#include <iostream>
#include <limits>

using namespace std;

class TreeNode
{
public:
    // Pointer to the left child
    //  Initialised to nullptr
    TreeNode *left = nullptr;
    // Pointer to the right child
    //  Initialised to nullptr
    TreeNode *right = nullptr;

    // Value in the node
    int value;

    // Constructor, sets the value
    TreeNode(int v) : value(v) {}
};

class Tree
{
public:
    TreeNode *root = nullptr;

    // Insert works correctly
    void insert(int v)
    {
        insert(v, root);
    }
    void insert(int v, TreeNode *&subtree)
    {
        if (subtree == nullptr)
        {
            subtree = new TreeNode(v);
        }
        else if (v < subtree->value)
        {
            insert(v, subtree->left);
        }
        else
        {
            insert(v, subtree->right);
        }
    }

    ////////////////////////////////////////////////////
    // Question 1 -- Traversals
    void preOrderTraversal()
    {
        preOrderTraversal(root);
        cout << endl;
    }
    void inOrderTraversal()
    {
        inOrderTraversal(root);
        cout << endl;
    }
    void postOrderTraversal()
    {
        postOrderTraversal(root);
        cout << endl;
    }
    void preOrderTraversal(TreeNode *subtree)
    {
        if(subtree == nullptr){
            return;
        }
        cout << subtree->value <<" ";
        preOrderTraversal(subtree->left);
        preOrderTraversal(subtree->right);

    }
    void inOrderTraversal(TreeNode *subtree)
    {
        if(subtree == nullptr){
            return;
        }
        inOrderTraversal(subtree->left);
        cout<< subtree->value <<" ";
        inOrderTraversal(subtree->right);


    }
    void postOrderTraversal(TreeNode *subtree)
    {
        if(subtree == nullptr){
            return;
       }
        postOrderTraversal(subtree->left);
        postOrderTraversal(subtree->right);
        cout<< subtree->value <<" ";

    }

    ////////////////////////////////////////////////////
    // Question 2 -- Descending Order
    void descendingOrder()
    {
        descendingOrder(root);
        cout << endl;
    }
    void descendingOrder(TreeNode *subtree)
    {
        if(subtree == nullptr){
            return;
        }
       descendingOrder(subtree->right);
       cout<< subtree->value <<" ";
       descendingOrder(subtree->left);

    }

    ////////////////////////////////////////////////////
    // Question 3 -- Depth of value
    void depth(int value)
    {
        cout << depth(root, value) << endl;
    }
    int depth(TreeNode *subtree, int value)
    {
        int count = 0;
        if(subtree == nullptr){
            return 0;
        }
        else if(subtree->value == value){
            count = 1;
        }
        while(subtree->value != value){
            if(value < subtree->value){
                subtree = subtree->left;
                count ++;
        }
            else if(value > subtree->value){
                subtree = subtree->right;
                count ++;
            }
        }
        return count;

    }

    ////////////////////////////////////////////////////
    // Question 4 -- Internal Nodes
    void internalNodes()
    {
        cout << internalNodes(root) << endl;
    }
    int internalNodes(TreeNode *subtree)
    {
        int lcount = 0;
        int rcount = 0;
        if(subtree == nullptr){
            return 0;
        }
        while(subtree->left != nullptr){
            subtree = subtree->left;
            lcount ++;
        }
        while(subtree->right != nullptr){
            subtree = subtree->right;
            rcount ++;
        }
        return lcount + rcount;

    }

    ////////////////////////////////////////////////////
    // Question 5 -- Equality
    void equals(Tree *otherTree)
    {
        bool result = equals(root, otherTree->root);
        cout << (result ? "true" : "false") << endl;
    }
    bool equals(TreeNode *subtree1, TreeNode *subtree2)
    {
        if(subtree1 != subtree2){
            return false;
        }
        while(subtree1 == subtree2){
            if(subtree1->left == subtree2->left && subtree1->right == subtree2->right ){
                return true;
            }
            else{
                return false;
            }

        }


    }

    ////////////////////////////////////////////////////
    // Question 6 -- Distance
    void distance(int value1, int value2)
    {
        cout << distance(root, value1, value2) << endl;
    }
    int distance(TreeNode *subtree, int value1, int value2)
    {
        int fcount = 0;
        int Scount = 0;
        if(subtree == nullptr){
            return 0;
        }
        else if (subtree->value == value1){
            fcount = 0;
        }
        else if (subtree->value == value2){
            Scount = 0;
        }
        while(subtree->value != value1){
            if (value1 < subtree->value){
                        subtree = subtree->left;
                        fcount ++;
                    }
            else if (value1 > subtree->value){
                subtree = subtree->right;
                fcount ++;
            }
        }
        while(subtree->value != value2){
            if (value2 < subtree->value){
                        subtree = subtree->left;
                        Scount ++;
                    }
            else if (value2 > subtree->value){
                subtree = subtree->right;
                Scount ++;
            }
        }
        return fcount + Scount;

    }
};

int main()
{
    // This function works correctly, don't change it unless you really need to.
    Tree t;

    int value;
    // Read and construct the tree.
    while (cin >> value && value != -1)
    {
        t.insert(value);
    }

    // Read a command
    string command;
    cin >> command;

    // Decide which command we saw and call that function
    if (command == "pre")
    {
        t.preOrderTraversal();
    }
    else if (command == "in")
    {
        t.inOrderTraversal();
    }
    else if (command == "post")
    {
        t.postOrderTraversal();
    }
    else if (command == "desc")
    {
        t.descendingOrder();
    }
    else if (command == "depth")
    {
        cin >> value;
        t.depth(value);
    }
    else if (command == "internal")
    {
        t.internalNodes();
    }
    else if (command == "equals")
    {
        Tree t2;
        while (cin >> value && value != -1)
        {
            t2.insert(value);
        }
        t.equals(&t2);
    }
    else if (command == "distance")
    {
        int value2;
        cin >> value >> value2;
        t.distance(value, value2);
    }
}
