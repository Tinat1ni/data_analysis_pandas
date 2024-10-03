import pandas as pd

from data_processing import(
       load_data, students_who_didnt_pass,
       average_scores_in_each_semester,
       students_with_max_scores,
       subject_with_worst_score,
       students_with_progress
)


def main():
    df, subjects = load_data('student_scores_random_names.csv')


    print(
        f"\n{len(students_who_didnt_pass(df, subjects))} students who didn't pass "
        f"in at least one subject:\n{students_who_didnt_pass(df, subjects)}")

    print(f'\naverage scores for each subject in each semester:'
          f'\n{average_scores_in_each_semester(df, subjects)}')

    top_student_score, top_student = students_with_max_scores(df, subjects)
    print(f"\nTop student: {top_student} score: {top_student_score}")

    print(subject_with_worst_score(df, subjects))
    print(students_with_progress(df, subjects))

    average_scores_by_semester = df.groupby('Semester')[subjects].mean()
    average_scores_dataframe = pd.DataFrame(average_scores_by_semester)
    average_scores_dataframe.to_excel('average_scores_by_semester.xlsx', index=True)

if __name__ == '__main__':
    main()
