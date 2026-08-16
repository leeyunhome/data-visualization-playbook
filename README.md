# 32가지 데이터 시각화 전략 — 강의노트 & 실습

인프런 [32가지 데이터 시각화 전략 - 비전공자를 위한 기초이론 & 실습](https://www.inflearn.com/course/32-data-visualizatio) (반병현) 수강 노트.

이론 정리와 Python 실습을 하나의 노트북에 담아 강의 진행 순서대로 관리한다.

## 구성

노트북 번호는 **실제 강의 진행 순서(전체 27강)** 그대로다. 섹션 3은 엑셀/AI/Python 실습이 뒤섞여
나오므로 노트북도 그 순서를 그대로 따르고, 이론 축(1차원/2차원/...)으로 재배열하지 않는다.

| 노트북 | 전체 강의 | 섹션 | 내용 |
| --- | --- | --- | --- |
| [01_ai시대의_데이터_시각화.ipynb](notebooks/01_ai시대의_데이터_시각화.ipynb) | 1~3강 | 섹션 1 | 왜 배우는가, 도구 선택, 환경 점검 |
| [02_이론_시각화_전략과_기법.ipynb](notebooks/02_이론_시각화_전략과_기법.ipynb) | 4~11강 | 섹션 2 | 기법 선택 기준표 (이론) |
| [03_엑셀_히스토그램.ipynb](notebooks/03_엑셀_히스토그램.ipynb) | 12강 | 섹션 3 | 엑셀 — 히스토그램 |
| [04_AI_히스토그램_KDE플롯.ipynb](notebooks/04_AI_히스토그램_KDE플롯.ipynb) | 13강 | 섹션 3 | AI — 히스토그램, KDE 플롯 |
| [05_Python_VSCode_설치.ipynb](notebooks/05_Python_VSCode_설치.ipynb) | 14강 | 섹션 3 | Python, VS Code 설치 방법 |
| [06_AI_산점도_박스_스웜_바이올린.ipynb](notebooks/06_AI_산점도_박스_스웜_바이올린.ipynb) | 15강 | 섹션 3 | AI — Scatter, Box, Swarm, Violin Plot |
| [07_Python_ChatGPT_박스_히스토그램_ECDF.ipynb](notebooks/07_Python_ChatGPT_박스_히스토그램_ECDF.ipynb) | 16강 | 섹션 3 | Python/ChatGPT — 박스플롯, 히스토그램, ECDF |
| [08_AI_시계열_주식_회귀_워터폴_캔들.ipynb](notebooks/08_AI_시계열_주식_회귀_워터폴_캔들.ipynb) | 17강 | 섹션 3 | AI — 시계열(주식) Regression·Waterfall·Line·Candle·이동평균 |
| [09_엑셀_라인_슬로프차트.ipynb](notebooks/09_엑셀_라인_슬로프차트.ipynb) | 18강 | 섹션 3 | 엑셀 — Line Chart, Slope Chart |
| [10_AI_2D밀도_헥스빈.ipynb](notebooks/10_AI_2D밀도_헥스빈.ipynb) | 19강 | 섹션 3 | AI — 2D Density Plot, Hexabin Plot |
| [11_AI_히트맵.ipynb](notebooks/11_AI_히트맵.ipynb) | 20강 | 섹션 3 | AI — HeatMap |
| [12_엑셀_머신러닝_잔차플롯.ipynb](notebooks/12_엑셀_머신러닝_잔차플롯.ipynb) | 21강 | 섹션 3 | 엑셀 — 머신러닝과 예측오차, Residual Plot |
| [13_AI_센서_스무딩.ipynb](notebooks/13_AI_센서_스무딩.ipynb) | 22강 | 섹션 3 | AI — 아날로그 센서 Smoothing (이동평균·Peak 포락선·Savitzky-Golay) |
| [14_AI_음파_STFT_스펙트로그램.ipynb](notebooks/14_AI_음파_STFT_스펙트로그램.ipynb) | 23강 | 섹션 3 | AI — 음파 데이터, STFT & Spectrogram |
| [15_AI_클러스터링.ipynb](notebooks/15_AI_클러스터링.ipynb) | 24강 | 섹션 3 | AI — Clustering |
| [16_AI_차원축소_PCA.ipynb](notebooks/16_AI_차원축소_PCA.ipynb) | 25강 | 섹션 3 | AI — 차원축소, PCA |
| [17_Python_데이터익명화.ipynb](notebooks/17_Python_데이터익명화.ipynb) | 26강 | 섹션 3 | Python — 데이터 익명화 |
| [18_outro.ipynb](notebooks/18_outro.ipynb) | 27강 | 섹션 4 | Outro |

03~18은 강의를 들으며 채워가는 뼈대만 있다 (완성된 실습 코드가 아니다). 각 노트북은
`배운 내용 → 목표/재현할 것 → (엑셀/설치/실습) → 메모` 구조다.

공통 코드는 [viz_utils.py](viz_utils.py)에 있다. 필요한 노트북에서 `load_sample()`로 실습용 가상 데이터를
생성할 수 있지만, 강의가 제공하는 실제 데이터를 쓰는 게 우선이다.

```
notebooks/   강의노트 겸 실습
docs/        GitHub Pages 포트폴리오 (아래 참고)
data/raw/    강의에서 받은 원본 파일 (git 제외)
data/        가공 데이터
output/      저장한 그림 (git 제외)
viz_utils.py 한글 폰트 설정 + 샘플 데이터
```

## 포트폴리오 (GitHub Pages)

`docs/`에는 이 강의를 계기로 만든 시각화 포트폴리오를 별도로 관리한다. **노트북(.ipynb)은 학습
기록이라 그대로 올리지 않고**, 강의에서 배운 기법(히스토그램·KDE 등)을 실습용 예제 데이터가 아니라
개인 프로젝트에서 실제로 만든 데이터에 적용해 다듬은 결과만 정리한다. 각 페이지는 자바스크립트만으로
동작하는 정적 페이지라 백엔드 없이 GitHub Pages에 그대로 올라간다.

- 목록: [docs/index.html](docs/index.html)
- 배포: 저장소 Settings → Pages → Source를 "Deploy from a branch", 브랜치 `main` / 폴더 `/docs`로
  설정하면 `https://<username>.github.io/<repo>/`에 공개된다.
- **강의 출처 표기:** 각 페이지 하단에 인프런 [32가지 데이터 시각화 전략 - 비전공자를 위한 기초이론 & 실습](https://www.inflearn.com/course/32-data-visualizatio/dashboard?cid=343563)
  (반병현) 링크와 해당 강의 번호를 명시한다 — 어떤 강의에서 배운 기법을 어떤 데이터에 적용했는지
  추적 가능하게 유지한다.
- 사용한 실제 데이터·재현 코드의 출처(예: 개인 프로젝트 저장소)도 각 페이지에 링크로 표기한다.

## 시작하기

이 저장소는 프로젝트 전용 가상환경(`.venv`, Python 3.12)을 쓴다.
`dataviz-inflearn` 커널이 등록되어 있으므로 JupyterLab에서 노트북을 열면 자동으로 잡힌다.

```bash
.venv\Scripts\activate
jupyter lab
```

> **왜 별도 venv인가:** conda base 환경은 numpy 2.4 + matplotlib 3.7.1 조합이라
> `ImportError: numpy.core.multiarray failed to import`로 matplotlib이 아예 import되지 않는다.

환경을 처음부터 다시 만들려면:

```bash
uv venv --python 3.12 .venv
uv pip install -r requirements.txt
.venv\Scripts\python -m ipykernel install --user --name dataviz-inflearn --display-name "Python (dataviz-inflearn)"
```

`notebooks/01_ai시대의_데이터_시각화.ipynb` 마지막 셀이 에러 없이 돌고 한글 제목이 보이면 준비 완료다.
`□□□`로 보이면 한글 폰트가 없는 것이니 `viz_utils.py`의 `_KOREAN_FONTS`를 확인한다.

## ipynb를 git으로 관리하기

노트북은 실행 결과(이미지 base64, `execution_count`)까지 파일에 저장되므로
**아무것도 안 고쳐도 diff가 수천 줄 나온다.** 커밋 전에 출력을 지우면 해결된다.

이 저장소에는 [nbstripout](https://github.com/kynan/nbstripout)이 이미 설정되어 있다
(`.gitattributes` + `.git/config`의 filter). `git add`할 때 출력이 자동으로 제거되고,
**작업 중인 노트북 파일의 출력은 그대로 남는다.**

저장소를 새로 clone한 경우 filter를 다시 등록해야 한다 (`.git/config`는 clone되지 않는다):

```bash
.venv\Scripts\python -m nbstripout --install
```

- 그림을 기록으로 남기고 싶으면 `savefig(fig, "이름")`으로 `output/`에 저장하고,
  `.gitignore`에서 `output/` 줄을 지워 png를 커밋한다.
- 특정 노트북만 출력을 유지하려면 `.gitattributes`에 `notebooks/03_*.ipynb -filter` 처럼 추가한다.

### 커밋 메시지 규칙

```
notes(03): 엑셀 히스토그램 정리
practice(13): 센서 스무딩 필터 비교 추가
fix(viz_utils): macOS 폰트 이름 수정
```

## 진행 상황

각 노트북 상단의 체크박스가 실제 진행 상태다. 요약:

- [ ] 섹션 1. AI시대의 데이터 시각화 (1~3강)
- [ ] 섹션 2. [이론] 데이터 시각화 전략과 기법들 (4~11강)
- [x] 섹션 3-1. 엑셀을 활용한 히스토그램 (12강)
- [ ] 섹션 3-2 ~ 3-15 (13~26강)
- [ ] 섹션 4. Outro (27강)
