# [level 0] 옹알이 (1) - 120956 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120956) 

### 성능 요약

메모리: 10.3 MB, 시간: 0.14 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 08월 20일 16:56:00

### 문제 설명

<p style="user-select: auto !important;">머쓱이는 태어난 지 6개월 된 조카를 돌보고 있습니다. 조카는 아직 "aya", "ye", "woo", "ma" 네 가지 발음을 최대 한 번씩 사용해 조합한(이어 붙인) 발음밖에 하지 못합니다. 문자열 배열 <code style="user-select: auto !important;">babbling</code>이 매개변수로 주어질 때, 머쓱이의 조카가 발음할 수 있는 단어의 개수를 return하도록 solution 함수를 완성해주세요.</p>

<hr style="user-select: auto !important;">

<h5 style="user-select: auto !important;">제한사항</h5>

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;">1 ≤ <code style="user-select: auto !important;">babbling</code>의 길이 ≤ 100</li>
<li style="user-select: auto !important;">1 ≤ <code style="user-select: auto !important;">babbling[i]</code>의 길이 ≤ 15</li>
<li style="user-select: auto !important;"><code style="user-select: auto !important;">babbling</code>의 각 문자열에서 "aya", "ye", "woo", "ma"는 각각 최대 한 번씩만 등장합니다.

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;">즉, 각 문자열의 가능한 모든 부분 문자열 중에서 "aya", "ye", "woo", "ma"가 한 번씩만 등장합니다.</li>
</ul></li>
<li style="user-select: auto !important;">문자열은 알파벳 소문자로만 이루어져 있습니다.</li>
</ul>

<hr style="user-select: auto !important;">

<h5 style="user-select: auto !important;">입출력 예</h5>
<table class="table" style="user-select: auto !important;">
        <thead style="user-select: auto !important;"><tr style="user-select: auto !important;">
<th style="user-select: auto !important;">babbling</th>
<th style="user-select: auto !important;">result</th>
</tr>
</thead>
        <tbody style="user-select: auto !important;"><tr style="user-select: auto !important;">
<td style="user-select: auto !important;">["aya", "yee", "u", "maa", "wyeoo"]</td>
<td style="user-select: auto !important;">1</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]</td>
<td style="user-select: auto !important;">3</td>
</tr>
</tbody>
      </table>
<hr style="user-select: auto !important;">

<h5 style="user-select: auto !important;">입출력 예 설명</h5>

<p style="user-select: auto !important;">입출력 예 #1</p>

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;">["aya", "yee", "u", "maa", "wyeoo"]에서 발음할 수 있는 것은 "aya"뿐입니다. 따라서 1을 return합니다.</li>
</ul>

<p style="user-select: auto !important;">입출력 예 #2</p>

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;">["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]에서 발음할 수 있는 것은 "aya" + "ye" = "ayaye", "ye", "ye" + "ma" + "woo" = "yemawoo"로 3개입니다. 따라서 3을 return합니다.</li>
</ul>

<hr style="user-select: auto !important;">

<h5 style="user-select: auto !important;">유의사항</h5>

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;">네 가지를 붙여 만들 수 있는 발음 이외에는 어떤 발음도 할 수 없는 것으로 규정합니다. 예를 들어 "woowo"는 "woo"는 발음할 수 있지만 "wo"를 발음할 수 없기 때문에 할 수 없는 발음입니다.</li>
</ul>

<hr style="user-select: auto !important;">

<p style="user-select: auto !important;">※ 공지 - 2022년 10월 27일 문제 지문이 리뉴얼되었습니다. 기존에 제출한 코드가 통과하지 못할 수도 있습니다.</p>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges