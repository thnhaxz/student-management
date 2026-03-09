# Student Management System

## 23709251 - Võ Thanh Nhã

---

## Tech stack

* FastAPI
* SQLite
* HTML / Jinja2

---

## Tools

* VS Code
* Git
* GitHub
* Cursor
* Windsurf
* ChatGPT

---

## Log (quá trình thực hiện)

### Version 1 – MVP

* Phân tích yêu cầu bài toán: xây dựng web app quản lý sinh viên đơn giản.
* Tạo cấu trúc project FastAPI.
* Thiết kế database SQLite cho bảng **students** gồm:

  * student_id
  * name
  * birth_year
  * major
  * gpa
* Xây dựng các chức năng cơ bản:

  * Thêm sinh viên (Add student)
  * Xem danh sách sinh viên (List students)
  * Xóa sinh viên (Delete student)
* Tạo giao diện HTML hiển thị bảng sinh viên và form thêm sinh viên.
* Commit và push **Version 1** lên GitHub.

### Version 2 – Mở rộng chức năng

* Thêm bảng **Class**:

  * class_id
  * class_name
  * advisor
* Cập nhật bảng **Student** để mỗi sinh viên thuộc một lớp.
* Thêm chức năng **Search student by name**.
* Thêm trang **Statistics** hiển thị:

  * Tổng số sinh viên
  * GPA trung bình
  * Số sinh viên theo ngành
* Thêm chức năng **Export dữ liệu sang file CSV**.
* Commit và push **Version 2** lên GitHub.

---

## File data dùng để sinh dữ liệu

* students.db (SQLite database dùng để lưu dữ liệu sinh viên)
