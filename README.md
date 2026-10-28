# MY_HARNESS

제조 데이터 분석·문제 해결 과제를 AI 코딩 에이전트(Codex)와 함께 수행할 때 쓰는 개인 작업 하네스입니다.
과정의 증거(합의, 결정, 검증, 인계)를 파일과 커밋으로 남기는 데 초점을 둡니다.

## 사용법 (작업 공간 루트에서)
```
git clone <이 저장소 URL> /tmp/kit && bash /tmp/kit/bootstrap.sh
```
- 작업 공간 밖(/tmp/kit)에 clone 한 뒤 실행합니다.
- 기존 파일(README, AGENTS.md 등)은 덮어쓰지 않습니다.
- 스킬 6개를 `.agents/skills` 에 연결해 Codex 에서 `/skills`, `$이름` 으로 쓸 수 있게 합니다.
- 옵션: `--ws <경로>`, `--user-skills`, `--no-repo-skills`, `--no-install`

## 구성
| 경로 | 내용 |
|---|---|
| AGENTS.md | 에이전트 작업 규칙 (작업 공간 루트로 복사됨) |
| harness/skills/ | interview, decision-log, stratify-analysis, redteam, handoff, explain-pack |
| harness/templates/ | STATE, INTERVIEW, AGREEMENT, DECISIONS, FINDINGS, EXPLAIN, REVIEW, HANDOFF, REPORT, ACTIONS, README_RUN |
| harness/scaffold/ | analysis_utils.py (+테스트), 불변식 테스트·재현 진입점 템플릿, UI 템플릿(Streamlit / FastAPI) |
| harness/playbook/ | 단계별 절차와 프롬프트 (00_flow 부터) |

## 원칙
- 결정론 코어: 숫자는 스크립트가 계산하고 문서는 출처를 인용한다.
- 결정·발견·검토는 D/F/R 번호로 기록하고 커밋 메시지와 연결한다.
- UI 는 코어의 결과를 표시만 한다.
- 세션은 단계 경계에서 HANDOFF 문서로 교대한다.
