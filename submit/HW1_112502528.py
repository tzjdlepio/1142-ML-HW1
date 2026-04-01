# -*- coding: utf-8 -*-
import os
import pandas as pd

def load_and_explore_data(file_path):
    """任務一：讀取 CSV 並初步探索資料"""
    df = pd.read_csv(file_path, encoding='utf-8-sig')  # ← 請勿修改此行

    # TODO 1.1: 顯示前 5 筆資料
    print(df.head())

    # TODO 1.2: 查看資料結構（欄位、型態、缺失值）
    print(df.columns)
    print(df.dtypes)
    print(df.isnull().sum())


    return df  # ← 請勿修改 return


def feature_engineering(df):
    """任務二：計算總分、平均分數與是否及格"""

    subject = ["數學", "英文", "國文", "自然", "社會"]

    # TODO 2.1: 計算總分（五科加總）
    df['總分'] = df[subject].sum(axis = 1)

    # TODO 2.2: 計算平均分數
    df['平均'] = df[subject].mean(axis = 1)

    # TODO 2.3: 新增是否及格欄位（平均 >= 60 為及格）
    df['是否及格'] = df['平均'] >= 60

    return df  # ← 請勿修改 return


def filter_and_analyze_data(df):
    """任務三與五：篩選資料與統計"""

    # TODO 3.1: 找出數學成績 < 60 的學生
    math_failed = df[df["數學"] < 60]

    # TODO 3.2: 找出班級為 'A' 且英文 > 90 的學生
    high_A = df[(df["班級"] == 'A') & (df["英文"] > 90)]

    # TODO 5.1: 顯示所有科目及平均分數的統計摘要
    summary = df[['國文', '英文', '數學', '自然', '社會', '平均']].describe()

    # TODO 5.2: 找出總分最高的學生
    # Hint: 可以先找到總分最高分，再篩選對應學生
    max_total = df['總分'].max()
    top_student = df[df['總分']  == max_total]

    return {  # ← 請勿修改 return 結構（key 名稱不可變動）
        "processed_df": df,
        "math_failed": math_failed,
        "high_A": high_A,
        "summary": summary,
        "top_student": top_student
    }


def group_statistics(df):
    """任務四：使用 groupby 進行分組統計"""

    # TODO 4.1: 計算各班級的平均總分
    # Hint: df.groupby(...)['總分'].mean()
    class_avg_total = df.groupby('班級')['總分'].mean()

    # TODO 4.2: 計算各性別的及格率
    # Hint: 是否及格欄位為 True/False，mean() 可直接計算比例
    gender_pass_rate = df.groupby('性別')['是否及格'].mean()

    return {  # ← 請勿修改 return 結構（key 名稱不可變動）
        "class_avg_total": class_avg_total,
        "gender_pass_rate": gender_pass_rate
    }


def save_results(df, output_file_path):
    """任務六：儲存為 CSV"""

    # TODO 6.1: 儲存 CSV，避免中文亂碼
    # Hint: df.to_csv(...)
    df.to_csv(output_file_path, index=False, encoding='utf-8-sig')



if __name__ == "__main__":
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    INPUT_CSV = os.path.join(BASE_DIR, '..', 'grades.csv')
    OUTPUT_CSV = os.path.join(BASE_DIR, 'grades_analyzed.csv')

    df = load_and_explore_data(INPUT_CSV)
    df = feature_engineering(df)
    result = filter_and_analyze_data(df)
    group_result = group_statistics(result["processed_df"])
    save_results(result["processed_df"], OUTPUT_CSV)

    print("完成所有分析任務")
