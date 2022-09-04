#include <bits/stdc++.h>
using namespace std;

int n;
int result = 0;
priority_queue <int> heapq;

int main(void) {
	cin >> n;

	// 힙에 초기 카드 묶음을 모두 삽입
	for (int i = 0; i < n; i++) {
		int x;
		cin >> x;
		heapq.push(-x);           // 음수 형태로 넣어야 min-heap이 됨
	}

	// 원소가 1개 남을 때까지
	while (heapq.size() != 1) {
		int a = -heapq.top();
		heapq.pop();              // c++의 pop()은 리턴값이 없음!!

		int b = -heapq.top();
		heapq.pop();

		result += a + b;
		heapq.push(-(a + b));    // 음수 형태로 넣어야됨!!
	}
	cout << result << endl;;
}