SELECT subject_name
FROM subjects
WHERE teacher_name = 'Johnny Brown'
AND subject_name IN (SELECT subject_name FROM grades WHERE student_name = 'Nathan Phillips');