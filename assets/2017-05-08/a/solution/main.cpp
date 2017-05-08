#include <cassert>
#include <stdio.h>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <unordered_map>
#include <set>
#include <queue>
#include <stack>

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef vector<int> VI;
typedef pair<LL, LL> PII;

#define debug(args...) {vector<string> _v = split(#args, ','); err(_v.begin(), args); puts("");}
vector<string> split(const string& s, char c) {vector<string> v; stringstream ss(s); string x; while (getline(ss, x, c)) v.push_back(x); return v;}
void err(vector<string>::iterator it) {}
template<typename T, typename... Args> void err(vector<string>::iterator it, T a, Args... args) {cerr << it -> substr((*it)[0] == ' ', it -> length()) << " = " << a << ", "; err(++it, args...);}

#if (( _WIN32 || __WIN32__ ) && __cplusplus < 201103L)
#define lld I64d
#else
#define lld lld
#endif

#define pb push_back
#define mp make_pair
#define all(x)  (x).begin(),(x).end()
#define tr(c, it)   for(auto it=c.begin(); it!=c.end(); it++)
#define clr(a, b)   memset(a, b, sizeof(a))
#define forn(i, n)   for(int i=0; i<n; i++)

const int INF = 0x3f3f3f3f;

const int N = 22;
int ans[N][N];

void gen(){
    ans[1][1] = 2;
    ans[1][2] = 3;
    ans[1][3] = 4;
    ans[1][4] = 5;
    ans[1][5] = 6;
    ans[1][6] = 7;
    ans[1][7] = 8;
    ans[1][8] = 9;
    ans[1][9] = 10;
    ans[1][10] = 11;
    ans[2][1] = 3;
    ans[2][2] = 7;
    ans[2][3] = 13;
    ans[2][4] = 22;
    ans[2][5] = 34;
    ans[2][6] = 50;
    ans[2][7] = 70;
    ans[2][8] = 95;
    ans[2][9] = 125;
    ans[2][10] = 161;
    ans[3][1] = 4;
    ans[3][2] = 13;
    ans[3][3] = 36;
    ans[3][4] = 87;
    ans[3][5] = 190;
    ans[3][6] = 386;
    ans[3][7] = 734;
    ans[3][8] = 1324;
    ans[4][1] = 5;
    ans[4][2] = 22;
    ans[4][3] = 87;
    ans[4][4] = 317;
    ans[4][5] = 1053;
    ans[4][6] = 3250;
    ans[5][1] = 6;
    ans[5][2] = 34;
    ans[5][3] = 190;
    ans[5][4] = 1053;
    ans[5][5] = 5624;
    ans[6][1] = 7;
    ans[6][2] = 50;
    ans[6][3] = 386;
    ans[6][4] = 3250;
    ans[7][1] = 8;
    ans[7][2] = 70;
    ans[7][3] = 734;
    ans[8][1] = 9;
    ans[8][2] = 95;
    ans[8][3] = 1324;
    ans[9][1] = 10;
    ans[9][2] = 125;
    ans[10][1] = 11;
    ans[10][2] = 161;
}

int main()
{
#ifdef LOCAL
    //freopen("in", "r", stdin);
    //freopen("out2", "w", stdout);
    //
    freopen("sample_in", "r", stdin);
    freopen("sample_out", "w", stdout);
#endif

    gen();
    int T, n, m;
    cin >> T;

    while(T--)
    {
        cin >> n >> m;
        cout << ans[n][m] << endl;
    }



    return 0;
}

