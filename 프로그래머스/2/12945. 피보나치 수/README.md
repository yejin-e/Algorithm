# [level 2] 피보나치 수 - 12945 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/12945?itm_content=course14743) 

### 성능 요약

메모리: 456 MB, 시간: 457.01 ms

### 구분

코딩테스트 연습 > 연습문제

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 08월 22일 17:25:56

### 문제 설명

<p style="user-select: auto !important;">피보나치 수는 F(0) = 0, F(1) = 1일 때, 1 이상의 n에 대하여 F(n) = F(n-1) + F(n-2) 가 적용되는 수 입니다. </p>

<p style="user-select: auto !important;">예를들어 </p>

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;">F(2) = F(0) + F(1) = 0 + 1 = 1</li>
<li style="user-select: auto !important;">F(3) = F(1) + F(2) = 1 + 1 = 2</li>
<li style="user-select: auto !important;">F(4) = F(2) + F(3) = 1 + 2 = 3</li>
<li style="user-select: auto !important;">F(5) = F(3) + F(4) = 2 + 3 = 5</li>
</ul>

<p style="user-select: auto !important;">와 같이 이어집니다.</p>

<p style="user-select: auto !important;">2 이상의 n이 입력되었을 때, n번째 피보나치 수를 1234567으로 나눈 나머지를 리턴하는 함수, solution을 완성해 주세요.</p>

<h5 style="user-select: auto !important;">제한 사항</h5>

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;">n은 2 이상 100,000 이하인 자연수입니다.</li>
</ul>

<h5 style="user-select: auto !important;">입출력 예</h5>
<table class="table" style="user-select: auto !important;">
        <thead style="user-select: auto !important;"><tr style="user-select: auto !important;">
<th style="user-select: auto !important;">n</th>
<th style="user-select: auto !important;">return</th>
</tr>
</thead>
        <tbody style="user-select: auto !important;"><tr style="user-select: auto !important;">
<td style="user-select: auto !important;">3</td>
<td style="user-select: auto !important;">2</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">5</td>
<td style="user-select: auto !important;">5</td>
</tr>
</tbody>
      </table>
<h5 style="user-select: auto !important;">입출력 예 설명</h5>

<p style="user-select: auto !important;">피보나치수는 0번째부터 0, 1, 1, 2, 3, 5, ... 와 같이 이어집니다.</p>

<h5 style="user-select: auto !important;">문제가 잘 안풀린다면😢</h5>

<p style="user-select: auto !important;">힌트가 필요한가요? [코딩테스트 연습 힌트 모음집]으로 오세요! → <a href="https://school.programmers.co.kr/learn/courses/14743?itm_content=lesson12945" target="_blank" rel="noopener" style="user-select: auto !important;">클릭</a></p>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges