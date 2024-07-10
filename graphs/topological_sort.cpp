// topological sort -- for a DAG - Directed Acyclic Graph

DFS(int i){
    if(visited[i]) return

    visited[i] = true
    for(int j : adjList[i]){
        if(!visited[j]){
             DFS(j)
        }
       
    }

    stack.push(i)  //  basically push the end nodes first 
}

for(int i : vertices){
    if(!visited[i]){
        DFS(i)
    }
}



// this is good algo for dependency resolution 
// can help in scheduling in such cases


