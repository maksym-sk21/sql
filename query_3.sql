SELECT group_name, AVG((grade1 + grade2 + grade3 + grade4) / 4) AS avg_grade
FROM grades
JOIN groups ON grades.student_name = groups.student_name
WHERE subject_name = 'add'
GROUP BY group_name;