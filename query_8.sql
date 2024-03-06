SELECT teacher_name, AVG((grade1 + grade2 + grade3 + grade4) / 4) AS avg_grade
FROM subjects
JOIN grades ON subjects.subject_name = grades.subject_name
GROUP BY teacher_name;