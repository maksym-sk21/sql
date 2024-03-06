SELECT student_name, AVG((grade1 + grade2 + grade3 + grade4) / 4) AS avg_grade
FROM grades
WHERE subject_name = 'economic'
GROUP BY student_name
ORDER BY avg_grade DESC
LIMIT 1;