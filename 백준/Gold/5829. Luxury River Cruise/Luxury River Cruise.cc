#include<bits/stdc++.h>
using namespace std;
using ll = long long;

ll N, M, K;
int adj[1005][2];
bool vis[1005];
vector<int> path;
vector<int> G(1005);

void dfs(int start, int cur, int idx) {
    if(idx == M) {
        G[start] = cur; return ;
    }
    int nxt = adj[cur][path[idx]];
    dfs(start, nxt, idx+1);
}

int main() {
    cin.tie(nullptr); ios::sync_with_stdio(false);
    cin >> N >> M >> K;
    for(int i=1;i<=N;++i) {
        int l, r;
        cin >> l >> r;
        adj[i][0] = l; adj[i][1] = r;
    }
    for(int i=0;i<M;++i) {
        string s;
        cin >> s;
        if(s[0] == 'L') path.push_back(0);
        else path.push_back(1);
    }
    for(int i=1;i<=N;++i) dfs(i,i,0);
    int cur = 1;
    int len = 0;
    int start;
    for(int i=0;i<=N;++i) {
        if(vis[cur]) {
            start = cur; len = i; break;
        }
        vis[cur] = true;
        cur = G[cur];
    }
    cur = 1;
    for(int i=0;i<=N;++i) {
        if(cur == start) {
            len -= i;
            break;
        }
        cur = G[cur];
        --K;
        if(K == 0) break;
    }
    if(K == 0) {
        cout << cur << '\n';
        return 0;
    }
    K %= len;
    cur = start;
    while(K--) cur = G[cur];
    cout << cur << '\n';
    return 0;
}