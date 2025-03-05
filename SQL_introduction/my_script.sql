-- 3 premiers étudiants du Batch ID=3 -- parce que le Batch 3 est le meilleur !
SELECT id, name 
FROM students 
WHERE batch_id = 3 
ORDER BY created_at DESC 
LIMIT 3;
sudo mysqld_safe --skip-grant-tables &
