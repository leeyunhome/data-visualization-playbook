import os
import glob
import pandas as pd
import matplotlib.pyplot as plt

try:
    import seaborn as sns
    HAS_SEABORN = True
except ImportError:
    HAS_SEABORN = False

# 한글 폰트 설정 (Windows 환경: 맑은 고딕, 마이너스 부호 깨짐 방지)
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False


def load_csv_with_encoding(file_path):
    """
    UTF-8 및 CP949(EUC-KR) 인코딩을 자동으로 감지하여 CSV 파일을 읽어옵니다.
    """
    for enc in ['utf-8', 'cp949', 'euc-kr', 'utf-8-sig']:
        try:
            return pd.read_csv(file_path, encoding=enc)
        except (UnicodeDecodeError, LookupError):
            continue
    raise ValueError(f"지원하는 인코딩으로 {file_path} 파일을 열 수 없습니다.")


def select_item(prompt_title, items):
    """
    목록을 번호로 출력하고 사용자 입력을 받아 선택된 항목을 반환합니다.
    """
    print(f"\n[{prompt_title}]")
    for i, item in enumerate(items, 1):
        print(f"  {i}. {item}")

    while True:
        try:
            choice = input(f"번호를 입력하세요 (1~{len(items)}): ").strip()
            idx = int(choice) - 1
            if 0 <= idx < len(items):
                return items[idx]
            else:
                print(f"1부터 {len(items)} 사이의 번호를 입력해주세요.")
        except ValueError:
            print("올바른 숫자를 입력해주세요.")


def draw_boxplot(plot_data, class_col, feature_col, save_path):
    """
    박스플롯을 생성하고 JPG 파일로 저장합니다.
    """
    plt.figure(figsize=(10, 6))

    if HAS_SEABORN:
        sns.boxplot(
            data=plot_data,
            x=class_col,
            y=feature_col,
            palette='Set2'
        )
    else:
        grouped = [group[feature_col].values for _, group in plot_data.groupby(class_col)]
        labels = [str(name) for name, _ in plot_data.groupby(class_col)]
        box = plt.boxplot(grouped, labels=labels, patch_artist=True, showmeans=True)
        colors = ['#8dd3c7', '#ffffb3', '#bebada', '#fb8072', '#80b1d3', '#fdb462', '#b3de69', '#fccde5']
        for patch, color in zip(box['boxes'], colors * (len(grouped) // len(colors) + 1)):
            patch.set_facecolor(color)
            patch.set_alpha(0.7)

    plt.title(f"Box Plot: {feature_col} by {class_col}", fontsize=14, pad=12)
    plt.xlabel(class_col, fontsize=12)
    plt.ylabel(feature_col, fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.savefig(save_path, format='jpg', dpi=300)
    plt.close()
    print(f" -> [박스플롯 저장 완료] {save_path}")


def draw_histogram(plot_data, class_col, feature_col, save_path):
    """
    히스토그램 및 KDE(밀도 곡선)를 생성하고 JPG 파일로 저장합니다.
    """
    plt.figure(figsize=(10, 6))

    if HAS_SEABORN:
        sns.histplot(
            data=plot_data,
            x=feature_col,
            hue=class_col,
            kde=True,
            element="step",
            palette='Set2',
            alpha=0.4
        )
    else:
        for name, group in plot_data.groupby(class_col):
            plt.hist(group[feature_col], bins=20, alpha=0.5, label=str(name))
        plt.legend(title=class_col)

    plt.title(f"Histogram & KDE: {feature_col} by {class_col}", fontsize=14, pad=12)
    plt.xlabel(feature_col, fontsize=12)
    plt.ylabel("빈도수 (Count)", fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.savefig(save_path, format='jpg', dpi=300)
    plt.close()
    print(f" -> [히스토그램 저장 완료] {save_path}")


def draw_ecdf(plot_data, class_col, feature_col, save_path):
    """
    ECDF(경험적 누적분포함수) 그래프를 생성하고 JPG 파일로 저장합니다.
    """
    plt.figure(figsize=(10, 6))

    if HAS_SEABORN:
        sns.ecdfplot(
            data=plot_data,
            x=feature_col,
            hue=class_col,
            palette='Set2',
            linewidth=2
        )
    else:
        import numpy as np
        for name, group in plot_data.groupby(class_col):
            vals = np.sort(group[feature_col].values)
            yvals = np.arange(1, len(vals) + 1) / len(vals)
            plt.step(vals, yvals, label=str(name), where='post', linewidth=2)
        plt.legend(title=class_col)

    plt.title(f"ECDF (누적분포함수): {feature_col} by {class_col}", fontsize=14, pad=12)
    plt.xlabel(feature_col, fontsize=12)
    plt.ylabel("누적 확률 (Cumulative Probability)", fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.savefig(save_path, format='jpg', dpi=300)
    plt.close()
    print(f" -> [ECDF 플롯 저장 완료] {save_path}")


def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # 1. 폴더 안에 있는 .csv 파일 자동 인식
    csv_files = glob.glob(os.path.join(current_dir, "*.csv"))
    if not csv_files:
        csv_files = glob.glob(os.path.join(current_dir, "**", "*.csv"), recursive=True)

    if not csv_files:
        print("폴더에 .csv 파일이 존재하지 않습니다.")
        return

    if len(csv_files) == 1:
        selected_file = csv_files[0]
        print(f"CSV 파일 자동 선택: {os.path.basename(selected_file)}")
    else:
        file_display = [os.path.relpath(f, current_dir) for f in csv_files]
        chosen_rel_path = select_item("분석할 CSV 파일을 선택하세요", file_display)
        selected_file = os.path.join(current_dir, chosen_rel_path)

    # 데이터 로드
    df = load_csv_with_encoding(selected_file)
    print(f"\n데이터 로드 완료! (총 {len(df):,}행, {len(df.columns)}열)")

    columns = list(df.columns)

    # 2. 클래스(Class, 그룹 변수) 선택
    class_col = select_item("클래스(그룹/범주형)로 사용할 컬럼을 선택하세요", columns)

    # 3. 피처(Feature, 수치형 변수) 선택
    feature_col = select_item("피처(수치형 데이터)로 사용할 컬럼을 선택하세요", columns)

    # 수치형 변환 및 결측치 제거
    df[feature_col] = pd.to_numeric(df[feature_col], errors='coerce')
    plot_data = df[[class_col, feature_col]].dropna()

    if plot_data.empty:
        print("선택한 컬럼에 유효한 수치 데이터가 없습니다.")
        return

    # 4. 시각화 그래프 종류 선택
    chart_options = [
        "박스플롯 (Box Plot)",
        "히스토그램 (Histogram & KDE)",
        "ECDF (경험적 누적분포함수)",
        "전체 한 번에 생성 (Box Plot + Histogram + ECDF)"
    ]
    chosen_chart = select_item("생성할 그래프 종류를 선택하세요", chart_options)

    # 안전한 파일명 생성
    safe_class = str(class_col).replace("/", "_").replace("\\", "_").replace(" ", "_")
    safe_feat = str(feature_col).replace("/", "_").replace("\\", "_").replace(" ", "_")

    print("\n[그래프 생성 및 저장 시작]")
    if "박스플롯" in chosen_chart or "전체" in chosen_chart:
        save_path = os.path.join(current_dir, f"boxplot_{safe_class}_{safe_feat}.jpg")
        draw_boxplot(plot_data, class_col, feature_col, save_path)

    if "히스토그램" in chosen_chart or "전체" in chosen_chart:
        save_path = os.path.join(current_dir, f"histogram_{safe_class}_{safe_feat}.jpg")
        draw_histogram(plot_data, class_col, feature_col, save_path)

    if "ECDF" in chosen_chart or "전체" in chosen_chart:
        save_path = os.path.join(current_dir, f"ecdf_{safe_class}_{safe_feat}.jpg")
        draw_ecdf(plot_data, class_col, feature_col, save_path)

    print("\n[완료] 모든 요청 작업이 끝났습니다!")


if __name__ == "__main__":
    main()
