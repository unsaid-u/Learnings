// #include <bits/stdc++.h>
#include <iostream>
#include <map>
#include <vector> 
#include <unordered_set>
#include <queue>
using namespace std;

// graphs 
//  - adjacency list
//  - adjacency matrix



// Adjescency List representation in C++

// Add edge
void addEdge(vector<int> adj[], int s, int d) {
  adj[s].push_back(d);
  adj[d].push_back(s);
}

// Print the graph
void printGraph(vector<int> adj[], int V) {
  for (int d = 0; d < V; ++d) {
    cout << "\n Vertex "
       << d << ":";
    for (auto x : adj[d])
      cout << "-> " << x;
    printf("\n");
  }
}


// DFS 
//  Time complexity - 
// we will take a node - visit all its connected component A then visit its connected component -> B -> C 
// exploring the depth
// we will do recursively , while maintaining a visited nodes. 

void traverse(int V, vector<int> graph[], unordered_set<int>& visited, vector<int>& result){
	if(!V || visited.find(V) != visited.end()){
		return;
	}
	result.push_back(V);
	visited.insert(V);
	for(int i =0; i<graph[V].size(); i++){
		traverse(graph[V][i], graph, visited, result);
	}
}

vector<int> DFS(int V, vector<int> graph[]){
	unordered_set<int> visited;
	vector<int> result ;
	// V is the starting node - we can start from any node
	traverse(V, graph, visited, result);
	return result;
}

bool CyclicGraph_BFS(vector<int> graph[]){
	// check if the graph is cyclic using BFS 
}


// BFS 
//  Time complexity - 
// we will take a node - visit all its connected components A -> B -> C 
// we will do recursively , while maintaining a visited nodes. 

// This is implemented using queue

vector<int> BFS(int V, const vector<int> Graph[]) {
    vector<int> res;
    vector<bool> visited(Graph.size(), false);  // To keep track of visited vertices
    queue<int> q;

    q.push(V);
    visited[V] = true;

    while (!q.empty()) {	
        int currentVertex = q.front();
        q.pop();
        res.push_back(currentVertex);

        // Enqueue unvisited neighbors
        for (int neighbor : Graph[currentVertex]) {
            if (!visited[neighbor]) {
                q.push(neighbor);
                visited[neighbor] = true;
            }
        }
    }

    return res;
}

int main()
{
	int V = 5;

	// Create a graph
	vector<int> adj[V];
//	data_type	array[array_size]


	// Add edges
	addEdge(adj, 0, 1);
	addEdge(adj, 0, 2);
	addEdge(adj, 0, 3);
	addEdge(adj, 1, 2);
	printGraph(adj, V);
	// vector<int> dfs = DFS(0, adj);
	vector<int> bfs = BFS(0, adj);
	// for (int i : dfs)
	// {
	// 	cout<<"DFS\n";
	// 	cout<<i<<" ";
	// }

	for (int i : bfs)
	{
		cout<<"BFS\n";
		cout<<i<<" ";
	}

}
