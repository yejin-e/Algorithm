# [level 0] 연속된 수의 합 - 120923 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120923#) 

### 성능 요약

메모리: 10.2 MB, 시간: 0.02 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 08월 13일 13:29:41

### 문제 설명

<p style="user-select: auto !important;">연속된 세 개의 정수를 더해 12가 되는 경우는 3, 4, 5입니다. 두 정수 <code style="user-select: auto !important;">num</code>과 <code style="user-select: auto !important;">total</code>이 주어집니다. 연속된 수 <code style="user-select: auto !important;">num</code>개를 더한 값이 <code style="user-select: auto !important;">total</code>이 될 때, 정수 배열을 오름차순으로 담아 return하도록 solution함수를 완성해보세요.</p>

<hr style="user-select: auto !important;">

<h5 style="user-select: auto !important;">제한사항</h5>

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;">1 ≤ <code style="user-select: auto !important;">num</code> ≤ 100</li>
<li style="user-select: auto !important;">0 ≤ <code style="user-select: auto !important;">total</code> ≤ 1000</li>
<li style="user-select: auto !important;"><code style="user-select: auto !important;">num</code>개의 연속된 수를 더하여 <code style="user-select: auto !important;">total</code>이 될 수 없는 테스트 케이스는 없습니다.</li>
</ul>

<hr style="user-select: auto !important;">

<h5 style="user-select: auto !important;">입출력 예</h5>
<table class="table" style="user-select: auto !important;">
        <thead style="user-select: auto !important;"><tr style="user-select: auto !important;">
<th style="user-select: auto !important;">num</th>
<th style="user-select: auto !important;">total</th>
<th style="user-select: auto !important;">result</th>
</tr>
</thead>
        <tbody style="user-select: auto !important;"><tr style="user-select: auto !important;">
<td style="user-select: auto !important;">3</td>
<td style="user-select: auto !important;">12</td>
<td style="user-select: auto !important;">[3, 4, 5]</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">5</td>
<td style="user-select: auto !important;">15</td>
<td style="user-select: auto !important;">[1, 2, 3, 4, 5]</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">4</td>
<td style="user-select: auto !important;">14</td>
<td style="user-select: auto !important;">[2, 3, 4, 5]</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">5</td>
<td style="user-select: auto !important;">5</td>
<td style="user-select: auto !important;">[-1, 0, 1, 2, 3]</td>
</tr>
</tbody>
      </table>
<hr style="user-select: auto !important;">

<h5 style="user-select: auto !important;">입출력 예 설명</h5>

<p style="user-select: auto !important;">입출력 예 #1</p>

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;"><code style="user-select: auto !important;">num</code> = 3, <code style="user-select: auto !important;">total</code> = 12인 경우 [3, 4, 5]를 return합니다.</li>
</ul>

<p style="user-select: auto !important;">입출력 예 #2</p>

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;"><code style="user-select: auto !important;">num</code> = 5, <code style="user-select: auto !important;">total</code> = 15인 경우 [1, 2, 3, 4, 5]를 return합니다.</li>
</ul>

<p style="user-select: auto !important;">입출력 예 #3</p>

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;">4개의 연속된 수를 더해 14가 되는 경우는 2, 3, 4, 5입니다.</li>
</ul>

<p style="user-select: auto !important;">입출력 예 #4</p>

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;">설명 생략</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges