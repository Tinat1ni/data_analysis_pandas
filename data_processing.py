import pandas as pd


def load_data(csv_file):
    df = pd.read_csv(csv_file)
    subjects = df.columns[2:]
    df.dropna(subset=subjects, how='all', inplace=True)
    return df, subjects


def students_who_didnt_pass(df, subjects):
    less_than_fifty = df[subjects].lt(50)
    students = df[less_than_fifty.any(axis=1)]
    return set(students['Student'])


def average_scores_in_each_semester(df, subjects):
    results = []
    for subject in subjects:
        a = df.groupby('Semester')[subject].mean()
        results.append(f'{subject}\n{a}')
    return '\n'.join(results)


def students_with_max_scores(df, subjects):
    average_scores_in_subjects = df.groupby(['Student'])[subjects].mean()
    overall_average_scores = average_scores_in_subjects.mean(axis=1)
    top_student_score = overall_average_scores.max()
    top_student = overall_average_scores.idxmax()
    return top_student_score, top_student


def subject_with_worst_score(df, subjects):
    semester_averages = df.groupby('Semester')[subjects].mean()
    overall_averages = semester_averages.mean()
    subject_with_min_score = overall_averages.idxmin()
    min_score = overall_averages.min()
    return f'\nsubject with worst scores is {subject_with_min_score} with average score: {min_score}'


def students_with_progress(df, subjects):
    scores_by_semester = df.groupby(['Student', 'Semester'])[subjects].mean()
    students_average_scores_by_semester = scores_by_semester.mean(axis=1).unstack(level=0)
    students_with_progress_semester = []
    for student in students_average_scores_by_semester.columns:
        if students_average_scores_by_semester[student].is_monotonic_increasing:
            students_with_progress_semester.append(student)
    return f'\nstudents who increased average score {students_with_progress_semester}'\
        if students_with_progress_semester else f'\n0 students had progress'