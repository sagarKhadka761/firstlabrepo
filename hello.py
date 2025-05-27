print("First devops lab")
print("Using GitHub")
print("Change for Jenkins")
print("commit after cloning")
print("changing again")
print("For learning in vm")

https://arduino.esp8266.com/stable/package_esp8266com_index.json

SELECT * FROM Borrowings WHERE return_date IS NULL;
 select category , sum(copava) from books group by category;
SELECT name, Br.borrowed_date FROM Mem M JOIN Borrgs Br ON M.member_id = Br.member_id WHERE Br.borrowed_date BETWEEN '2023-01-01' AND '2023-01-31'; 1900 and 1999
SELECT M.name FROM Members M JOIN Borrowings Br ON M.member_id = Br.member_id JOIN Books B ON Br.book_id = B.book_id WHERE B.title = '1984';
SELECT A.nameFROM Authors A JOIN Books B ON A.author_id = B.author_id GROUP BY A.name ORDER BY COUNT(B.book_id) DESCLIMIT 1; having count()>3
 select b.title from books b join borrowings br on b.bookid=br.bookid where br.returndate is null or br.bordate< returndate-interval '30 days'; left join,bor id is null
SELECT COUNT(DISTINCT A.author_id) AS total_authorsFROM Authors AJOIN Books B ON A.author_id = B.author_idJOIN Borrowings Br ON B.book_id = Br.book_idWHERE Br.borrowed_date BETWEEN '2023-01-01' AND '2023-12-31';

create or replace function copies_ava() returns trigger as $$
begin
if new.returndate is not null then
   update books
     set copava=copava+1
   where bookid-new.bookid;
  else
    update books
   set copava=copava-1
     where bookid=new.bookid;
   end if;
  return new;
end;
$$ language plpgsql;

CREATE TRIGGER update_copies_on_borrow_return
AFTER INSERT OR UPDATE ON Borrowings
FOR EACH ROW
EXECUTE FUNCTION update_copies_available();

UPDATE Borrowings
SET return_date = '2023-06-01'
WHERE borrowing_id = 1;

 COALESCE(SUM(o.amount), 0) --> left join
SELECT e.employee_id, 
       e.name AS employee_name, 
       e.salary, 
       d.department_name,
       SUM(e.salary) OVER (PARTITION BY e.department_id ORDER BY e.employee_id) AS running_salary_total
FROM employees e
JOIN departments d ON e.department_id = d.department_id;

CREATE OR REPLACE PROCEDURE delete_orders_and_log(customer_id INT)
LANGUAGE plpgsql
AS $$
BEGIN
    -- Log the deletion before deleting orders
    INSERT INTO deletion_log (customer_id, deleted_at)
    SELECT customer_id, CURRENT_TIMESTAMP
    FROM customers
    WHERE customer_id = customer_id;

    -- Delete the orders
    DELETE FROM orders
    WHERE customer_id = customer_id;
END;
$$;

-- Trigger function to log employee additions
CREATE OR REPLACE FUNCTION log_employee_addition()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO audit_log (employee_id, employee_name, department_name, action_type)
    SELECT NEW.employee_id, NEW.name, d.department_name, 'INSERT'
    FROM departments d
    WHERE d.department_id = NEW.department_id;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Trigger to log new employees
CREATE TRIGGER employee_added_trigger
AFTER INSERT ON employees
FOR EACH ROW
EXECUTE FUNCTION log_employee_addition();
curl -X POST http://admin:admin@localhost:5984/studentdb \
-H "Content-Type: application/json" \
-d '{
  "SRN": "1",
  "Sname": "Rahul",
  "Degree": "BCA",
  "Sem": 5,
  "CGPA": 7.0
}'

curl -X PUT http://localhost:5984/library/_design/book_views \
-H "Content-Type: application/json" \
-d '{
"_id": "_design/book_views",
"views": {
"by_author": {
"map": "function (doc) { if (doc.type === \"book\" && doc.author) {
emit(doc.author, doc.title); } }"
}
},
"language": "javascript"
}'

CREATE (a:User {UserID: 1, Username: "Alice"}),
(f)-[:FOLLOWS]->(b);
MATCH (me:User {Username: 'Jane'})-[:FOLLOWS]->(:User)-[:FOLLOWS]->(suggested:User)
WHERE NOT (me)-[:FOLLOWS]->(suggested) AND me <> suggested
RETURN DISTINCT suggested.Username AS SuggestedToFollow  collect


HSET employee:101 Name "Alice" Department "HR" Position "Manager" Salary 60000
SADD department:HR 101 103
ZADD employees_by_salary 60000 101 75000 102 45000 103 55000 104
ZRANGEBYSCORE employees_by_salary 50001 +inf



