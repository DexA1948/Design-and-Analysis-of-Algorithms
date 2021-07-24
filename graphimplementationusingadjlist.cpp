//Convert given adjacent matrix for graph into adjacent list
#include<iostream>
#include<cstring>

using namespace std;

struct edgeGraph
{
    int start_ver, end_ver, weight;
};

struct adjNode
{
    int end_ver, weight;
    adjNode* next;
};

class diaGraph
{
private:
    int V, E;

    /*
    This function can also be used to create and add Nodes
    adjNode* addadjNode(int end_ver, int weight, adjNode* next)
    {
        adjNode* newNode = new adjNode;
        newNode->end_ver = end_ver;
        newNode->weight = weight;
        newNode->next = next;
        return newNode;
    }
    */
public:
    adjNode** head;
    diaGraph(edgeGraph edges[], int V, int E)
    {
        this->V = V;
        this->E = E;

        //head is a array which stores first adjacentNode address which then points next remaining till NULL
        head = new adjNode*[V];

        for(int i=0; i<V; i++)
        {
            head[i] = nullptr;
        }

        for(int i=0; i<E; ++i)
        {
            //head[edges[i].start_ver] = addadjNode(edges[i].end_ver, edges[i].weight, head[edges[i].start_ver]);
            adjNode* newNode = new adjNode;
            newNode->end_ver = edges[i].end_ver;
            newNode->weight = edges[i].weight;
            newNode->next = head[edges[i].start_ver];
            head[edges[i].start_ver] = newNode;
        }
    }

    ~diaGraph()
    {
        for(int i=0; i<V; i++)
            delete[] head[i];
        delete[] head;
    }
};

void printAdjNodes(adjNode* ptr)
{
    while(ptr!=nullptr)
    {
        cout<<ptr->end_ver<<":"<<ptr->weight<<"->";
        ptr = ptr->next;
    }
}

int main()
{
    //manually giving number of vertices and inserting edges
    int V = 5;
    edgeGraph edges[] = {
    {0,1,3}, {0,4,7}, {1,2,8}, {1,3,5}, {2,3,7}, {3,4,6}, {4,0,4}, {4,1,5}
    };

    //Calculating number of edges
    int E = sizeof(edges)/sizeof(edges[0]);

    //constructing a directional graph using edgelist
    diaGraph diagraph(edges, V, E);

    //printing the diagraph
    for(int i=0; i<V; i++)
    {
        cout<<i<<"->";
        printAdjNodes(diagraph.head[i]);
        cout<<endl;
    }
}
