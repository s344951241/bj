
using System.Collections.Generic;

public class Graph
{
    private int V;//点数
    private int E;//边数

    private List<int>[] adj;//邻接表

    public Graph(int V)
    {
        this.V = V;
        this.E = 0;
        adj = new List<int>[V];
        for (int v = 0; v < V; v++)
        {
            adj[v] = new List<int>();
        }
    }
    public int V()
    {
        return V;
    }

    public int E()
    {
        return E;
    }

    public void addEdge(int v, int w)
    {
        adj[v].Add(w);
        adj[w].Add(v);
        E++;
    }

    public List<int> adj(int v)
    {
        return adj[v];
    }

    public string toString()
    {
        string s = V + "vertices," + E + "edges\n";
        for (int v = 0; v < V; v++)
        {
            s += v + ":";
            foreach (int w in this.adj(v))
            {
                s += w + ":";
            }
            s += "\n";
        }
        return s;
    }
}