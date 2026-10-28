# 06. S5 산출물과 제출 (135–170분)

## 1. 필수 파일 매핑 (135–137)
README 필수 파일명을 기준으로 work/ 문서의 내용을 어디에 담을지 정한다.
| README 필수 | 담을 내용 (출처) |
|---|---|
| 계획 문서 류 | AGREEMENT + 단계 구성 + 결정 요지 |
| 협업 기록 류 | INTERVIEW 요약, DECISIONS, REVIEW 판정, AI 제안 수용/기각 |
| 결과 보고 류 | REPORT 템플릿 구조 |
필수 지정이 없으면 REPORT.md, ACTIONS.md, README_RUN.md 를 루트에 둔다.

## 2. 보고서 (137–145)
```
AGENTS.md 를 따른다. harness/templates/REPORT.md 형식으로 <필수 파일명> 초안을 써라.
숫자는 outputs/tables/ 에서 가져와 출처를 괄호로. 근거는 FINDINGS 의 강·중만. 한계 절에 REVIEW 의 수용-한계와 sensitivity 결과.
"확정" "원인이다" 를 쓰지 말고 확인 실험 전 단계임을 드러내라. 1장 이내.
```
결론 3줄과 메커니즘 문장은 사람이 직접 다시 쓴다.

## 3. 조치안 (145–150)
```
INTERVIEW 의 제약과 REVIEW 의 한계를 반영해 ACTIONS.md 를 써라. 즉시 조치 선택지 비교표(영향·리스크), 확인 실험(설계·판정 기준), 하지 말 것. 최종 선택은 업무 담당자에게 열어둬라.
```

## 4. 재현 (150–155)
```
src/run_all.py 를 harness/scaffold/run_all_template.py 기반으로 만들고, data/clean·outputs 를 비운 깨끗한 상태에서 실행해 모든 표·그림이 다시 생성되는지 확인하라.
README_RUN.md 를 템플릿대로 작성하라 (UI 실행 명령과 미리보기 포트 포함).
```
```
rm -rf data/clean/* outputs/tables/* outputs/figures/*
python -m src.run_all && python -m pytest -q
git add -A && git commit -m "[S5] 산출물, clean run 통과"
```
UI 가 있으면 서버를 재시작하고 Browser 미리보기에서 한 번 더 확인.

## 5. 업무 담당자 최종 회신 (155–158)
요약 2줄 + 권고 조치 + 보류 권고 + 타 부서 확인 요청. 답변을 INTERVIEW 에 기록.

## 6. 제출 (168–170) — 마감(08) 뒤에
1. 탭 줄의 저장 상태 "저장됨" 확인, 필수 파일 경로 확인, `git status` 깨끗한지 확인
2. 상단 "제출하고 문제풀기" → 미리보기 (일부만 표시될 수 있음)
3. "제출물 확정하고 문제풀기" → 확정 후 수정 불가
4. 서술형 준비 대기 (최대 10분) → 08 의 서술형 절차
