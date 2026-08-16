"""강의 실습용 공통 유틸.

노트북 첫 셀에서 아래처럼 불러 쓴다.

    import sys; sys.path.append("..")
    from viz_utils import setup, load_sample
    setup()
"""

from __future__ import annotations

import platform

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

__all__ = ["setup", "load_sample", "savefig"]

# OS별 한글 폰트. 없으면 matplotlib 기본 폰트로 두고 경고만 남긴다.
_KOREAN_FONTS = {
    "Windows": "Malgun Gothic",
    "Darwin": "AppleGothic",
    "Linux": "NanumGothic",
}


def setup(figsize=(8, 5), dpi=110, style="seaborn-v0_8-whitegrid"):
    """한글 폰트 + 공통 그림 스타일을 적용한다."""
    if style in plt.style.available:
        plt.style.use(style)

    font = _KOREAN_FONTS.get(platform.system())
    installed = {f.name for f in mpl.font_manager.fontManager.ttflist}
    if font in installed:
        mpl.rcParams["font.family"] = font
    else:
        print(f"[warn] 한글 폰트 '{font}'를 찾지 못했습니다. 축 라벨이 □로 보일 수 있습니다.")

    mpl.rcParams["axes.unicode_minus"] = False  # 한글 폰트에서 음수 기호 깨짐 방지
    mpl.rcParams["figure.figsize"] = figsize
    mpl.rcParams["figure.dpi"] = dpi
    mpl.rcParams["savefig.bbox"] = "tight"


def load_sample(name: str, seed: int = 0) -> pd.DataFrame:
    """실습용 가상 데이터셋. 외부 다운로드 없이 항상 같은 값을 만든다.

    name: "sales" | "sensor" | "students" | "iris_like"
    """
    rng = np.random.default_rng(seed)

    if name == "sales":
        # 1~2차원 시각화용: 지역 x 분기 매출
        regions = ["서울", "경기", "부산", "대구", "광주"]
        quarters = ["1Q", "2Q", "3Q", "4Q"]
        rows = [
            {"지역": r, "분기": q, "매출": int(rng.normal(100 + 20 * i, 15) * 10)}
            for i, r in enumerate(regions)
            for q in quarters
        ]
        return pd.DataFrame(rows)

    if name == "sensor":
        # 시계열용: 10분 간격 온도/습도 (추세 + 일주기 + 노이즈 + 이상치)
        idx = pd.date_range("2026-01-01", periods=24 * 6 * 14, freq="10min")
        t = np.arange(len(idx))
        temp = 20 + 5 * np.sin(2 * np.pi * t / (24 * 6)) + t * 0.0005 + rng.normal(0, 0.6, len(idx))
        temp[rng.choice(len(idx), 12, replace=False)] += rng.normal(0, 8, 12)  # 이상치
        humid = 55 - 0.8 * (temp - 20) + rng.normal(0, 3, len(idx))
        return pd.DataFrame({"시각": idx, "온도": temp, "습도": humid}).set_index("시각")

    if name == "students":
        # 1차원 분포 + 그룹 비교용
        n = 300
        group = rng.choice(["A반", "B반", "C반"], n, p=[0.4, 0.35, 0.25])
        base = {"A반": 72, "B반": 78, "C반": 65}
        score = np.clip([rng.normal(base[g], 11) for g in group], 0, 100)
        study = np.clip(score / 10 + rng.normal(0, 1.5, n), 0, None)
        return pd.DataFrame({"반": group, "점수": score.round(1), "공부시간": study.round(1)})

    if name == "iris_like":
        # 다차원/차원축소용: 3개 군집 x 6개 변수
        per, dims = 60, 6
        centers = rng.normal(0, 4, (3, dims))
        X = np.vstack([c + rng.normal(0, 1, (per, dims)) for c in centers])
        df = pd.DataFrame(X.round(3), columns=[f"x{i + 1}" for i in range(dims)])
        df["군집"] = np.repeat(["1군", "2군", "3군"], per)
        return df

    raise ValueError(f"알 수 없는 샘플 이름: {name!r}")


def savefig(fig, name: str, outdir: str = "../output") -> str:
    """그림을 output/ 아래 png로 저장하고 경로를 돌려준다."""
    import os

    os.makedirs(outdir, exist_ok=True)
    path = os.path.join(outdir, f"{name}.png")
    fig.savefig(path)
    return path
