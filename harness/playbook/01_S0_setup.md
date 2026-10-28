# 01. S0 감독 절차와 셋업 (0–10분)

## 0. "과제 시작" 직후 (녹화·타이머 시작)
1. 미리 둔 거치대에 휴대폰 세로 거치, 충전선 연결, 손·키보드·얼굴·모니터 구도
2. 신분증(가림 처리된 것) 얼굴 옆 제시 → 안경 앞면·안경다리 양쪽 제시 → 착용
3. 신분증은 내려놓고 구도 유지

## 1. 하네스 설치 (터미널 T4)
```
git clone <저장소 URL> /tmp/kit && bash /tmp/kit/bootstrap.sh
```
- 과제 AGENTS.md 가 이미 있으면 AGENTS.kit.md 로 저장된다. 과제 것을 우선한다.
- 스캐폴드 테스트 통과 메시지 확인.

## 2. Codex 기동 (터미널 T1, 반드시 작업 공간 루트에서)
```
cd <작업 공간 루트>
codex
/status      # 모델·권한 확인
/model       # 사전체험에서 정한 모델 선택
/skills      # interview, decision-log, stratify-analysis, redteam, handoff, explain-pack 6개 확인
```
첫 메시지: `시작` → 첫 줄 `[harness loaded]` 확인. 없으면 "AGENTS.md 를 먼저 읽고 따르라" 고 지시.

## 3. README 필수 조건 (사람이 직접 읽기)
work/STATE.md 의 "README 필수 조건" 표를 채운다: 필수 산출물, 파일명, 형태(보고서/서비스/둘 다), 제출 위치.

## 4. 원본 보호와 인벤토리 (T1 에 위임 → 바로 S1 인터뷰로 이동)
```
AGENTS.md 를 따른다.
1) 과제가 제공한 데이터 파일을 data/raw/ 로 복사하고 읽기 전용으로 바꿔라 (원본 위치의 파일은 그대로 둔다).
2) harness/scaffold/analysis_utils.py 의 profile() 로 data/raw 의 모든 파일을 요약하는 src/inventory.py 를 만들고 실행해 outputs/inventory.md 에 저장하라.
3) 분석·원인 추정은 하지 마라. 마지막에 세 가지만 요약하라:
   (a) 파일별 기간과 행 수 (b) 날짜·설비·자재·측정 조건 관련 열 (c) 이상해 보이는 값의 종류 (포맷 혼재, 범위 이탈, 중복)
4) 커밋: [S0] 데이터 인벤토리
```
