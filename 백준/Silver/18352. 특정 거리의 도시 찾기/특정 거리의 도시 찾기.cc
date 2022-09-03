#include <bits/stdc++.h>
using namespace std;

int n, m, k, x;
vector<int> graph[300001];        // (중요) 2차원 배열은 이렇게!
vector<int> visiting(300001, -1);    // (중요) 모든 도시에 대한 최단 거리 -> 초기화 방법
bool flag = false;

void bfs(int x) {
	// (중요) cpp에선 큐를 queue라이프러리로 사용 (사용법은 vector와 동일)
	queue<int> que;
	que.push(x);
	visiting[x]++;

	while (!que.empty()) {
		//int a = que.pop();      // (매우 중요) 이게 불가하다!
		int cur = que.front();    // = .popleft()
		que.pop();

		for (int i = 0; i < graph[cur].size(); i++) {
			int nx = graph[cur][i];     // (매우 중요) 인접리스트 노드 이렇게 가져와야 함!!

			if (visiting[nx] == -1) {
				que.push(nx);
				visiting[nx] = visiting[cur] + 1;
			}
		}
	}

	// flag를 사용해서, 브루트포스 검색 => 하나라도 있으면 출력, 없으면 -1을 출력해야함
	for (int i = 1; i <= n; i++) {
		if (visiting[i] == k) {
			cout << i << endl;
			flag = true;
		}
	}
	if (flag == false) {
		cout << -1 << endl;
	}
}

int main(void) {
	cin >> n >> m >> k >> x;

	for (int i = 0; i < m; i++) {
		int a, b;
		cin >> a >> b;
		graph[a].push_back(b);         // 위와 같이 생성할 경우 이렇게 가능!
	}

	bfs(x);
	return 0;
}