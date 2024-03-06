SELECT grades.student_name, grade1, grade2, grade3, grade4
FROM grades
JOIN groups ON grades.student_name = groups.student_name
WHERE group_name = 'C' AND subject_name = 'exist';